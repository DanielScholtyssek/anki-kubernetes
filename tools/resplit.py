#!/usr/bin/env python3
"""Re-split a deck's cards/ files into thematic topic files.

Thematic split is the preferred repo layout (see AGENTS.md), but
export_anki.py can only use signals that exist in the data (a shared
`prefix::topic` tag family or a `Domain` field). For decks without one,
this script classifies notes into topic buckets by scoring their tags and
field text against per-deck keyword maps, then rewrites the files.

CKS   -> CKS exam domains, scored per lecture segment (note-id bursts)
KCNA  -> KCNA exam domains, scored per note (deck has no tags)

Usage:
    tools/resplit.py                 # resplit cks/ and kcna/
    tools/resplit.py --deck cks      # one dir
    tools/resplit.py --dry-run       # print assignments, don't write

Review the printed assignment table before/after runs — the keyword maps
below are heuristics; OVERRIDES pins notes/segments that scored wrong
(keyed by first note id of a segment, which never changes).
"""

import argparse
import re
import sys
import tempfile
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from export_anki import (DEFAULT_DB, MODEL_FIELDS, load, render_file,
                         slugify, snapshot)

# ---------------------------------------------------------------- CKS ---

CKS_KEYWORDS = {
 'cluster-setup': ['network-policy', 'networkpolicy', 'ingress', 'kube-bench',
   'cis-benchmark', 'kubeconfig', 'node-metadata', 'dashboard',
   'binary-verification', 'checksum', 'gui', 'ca-certificate', 'csr',
   'certificates-api', 'server-certificates'],
 'cluster-hardening': ['rbac', 'role', 'authorization', 'authentication',
   'service-account', 'kubelet', 'upgrade', 'version', 'api-priority',
   'api-access', 'kubectl-proxy', 'password', 'token', 'basic-auth',
   'impersonat', 'kube-apiserver', 'account'],
 'system-hardening': ['apparmor', 'seccomp', 'capabilit', 'syscall', 'kernel',
   'ufw', 'firewall', 'ssh', 'sudo', 'iam-', 'port', 'package', 'host-os',
   'footprint', 'systemd', 'least-privilege', 'linux', 'hardening',
   'docker', 'daemon', 'reconnaissance', 'attack-surface'],
 'microservice-vulnerabilities': ['opa', 'gatekeeper', 'pod-security', 'psa',
   'psp', 'securitycontext', 'security-context', 'secret', 'mtls', 'cilium',
   'gvisor', 'kata', 'sandbox', 'multi-tenan', 'tenant', 'namespace',
   'admission', 'qos', 'resourcequota', 'taints', 'tolerations',
   'data-plane', 'storage-class', 'runtimeclass', 'isolation',
   'immutab', 'pod-to-pod', 'encryption'],
 'supply-chain-security': ['image', 'registry', 'trivy', 'cve', 'sbom',
   'spdx', 'cyclonedx', 'supply', 'static-analysis', 'kubelinter', 'lint',
   'ci-cd', 'scan', 'whitelist', 'allowlist', 'vulnerabilit', 'base-image',
   'dockerfile', 'dependency', 'registries'],
 'monitoring-logging-runtime': ['falco', 'audit', 'tracee', 'ebpf-tracing',
   'monitor', 'log', 'behavioral', 'syscall-monitoring', 'incident',
   'detection', 'runtime-security', 'immutable-infrastructure'],
 'exam-prep': ['cks-exam', 'exam-fee', 'prerequisite', 'certification',
   'course-material', 'course-structure', 'learning-strategy',
   'exam-format', 'exam-policy', 'validity'],
 'security-fundamentals': ['symmetric', 'asymmetric', 'ssl', 'one-way',
   'encryption-types', 'key-pair', 'ssh-basics', 'ssh-keygen', 'ssh-config',
   'docker-concepts', 'docker-run', 'cloud-security', '4cs', 'pki',
   'tls-certificates', 'digital-certificates', 'certificate-authorities',
   'trust-model', 'https', 'secure-communications', 'file-naming',
   'key-naming'],
}

# Segments whose keyword score landed wrong (key: first note id of the
# segment — stable even if note order changes).
CKS_OVERRIDES = {
    1772498902937: 'cluster-setup',                # access-control/network isolation analogies
    1772499076463: 'cluster-setup',                # node metadata protection (official: setup)
    1772499239663: 'security-fundamentals',        # TLS/cert file-extension basics
    1772499288135: 'cluster-setup',                # CIS benchmarks/org overview
    1772499486548: 'microservice-vulnerabilities', # namespace isolation
    1772500513626: 'security-fundamentals',        # docker run basics
    1772501069302: 'monitoring-logging-runtime',   # immutable infrastructure (runtime domain)
    1772501723030: 'supply-chain-security',        # registry allow-listing (supply chain)
}

CKS_DOMAIN_TITLES = {
    'cluster-setup': 'Cluster Setup',
    'cluster-hardening': 'Cluster Hardening',
    'system-hardening': 'System Hardening',
    'microservice-vulnerabilities': 'Minimize Microservice Vulnerabilities',
    'supply-chain-security': 'Supply Chain Security',
    'monitoring-logging-runtime': 'Monitoring, Logging and Runtime Security',
    'security-fundamentals': 'Security Fundamentals',
    'exam-prep': 'Exam Prep',
}

# ---------------------------------------------------------------- KCNA --

# (phrase, weight) — strong phrases win over generic words like 'service'.
KCNA_KEYWORDS = {
 'kubernetes-fundamentals': {
   'replicaset': 4, 'statefulset': 4, 'daemonset': 4, 'kubelet': 4,
   'kube-proxy': 4, 'etcd': 4, 'kube-scheduler': 4, 'kubescheduler': 4,
   'kube-apiserver': 4, 'apiserver': 4, 'api server': 4,
   'control plane': 4, 'controller manager': 4, 'rbac': 4, 'role-based': 4,
   'serviceaccount': 4, 'service account': 4, 'networkpolicy': 4,
   'network policy': 4, 'configmap': 4, 'secret': 3, 'namespace': 3,
   'admission controller': 4, 'limitrange': 4, 'resourcequota': 4,
   'ownerreference': 4, 'kubectl': 4, 'nodeport': 3, 'clusterip': 3,
   'pod security': 3, 'endpoint': 3, 'job': 2, 'ingress': 3, 'pod': 2,
   'deployment': 2, 'service': 2, 'node': 2, 'label': 2, 'selector': 2,
   'declarative': 2, 'desired state': 2, 'reconcil': 2, 'manifest': 2,
   'replicas': 2, 'restart': 2, 'rolling': 2, 'workload': 2, 'volume type': 2,
   'external access': 2, 'api request': 2, 'init': 1, 'command': 1,
 },
 'container-orchestration': {
   'orchestrat': 4, 'container runtime': 4, 'containerd': 4, ' cri ': 4,
   ' oci': 4, 'oci ': 4, 'open container initiative': 4, 'docker': 3,
   'container image': 3, 'containerization': 3, 'persistentvolume': 4,
   'pvc': 4, 'storageclass': 4, 'storage': 3, 'volume': 2, 'cni': 4,
   'networking model': 4, 'runtime': 2, 'containers': 1,
 },
 'cloud-native-architecture': {
   'cncf': 5, 'cloud native': 4, 'microservice': 4, 'service mesh': 5,
   'istio': 5, 'linkerd': 5, 'serverless': 5, 'faas': 5, 'knative': 5,
   'autoscal': 4, 'hpa': 4, 'vpa': 4, 'persona': 4, 'open standard': 4,
   'trail map': 4, 'sidecar': 3, 'architectur': 2, 'scale': 1,
 },
 'cloud-native-observability': {
   'prometheus': 5, 'telemetry': 5, 'observab': 5, 'tracing': 4,
   'metrics': 4, 'monitor': 4, 'grafana': 5, 'opentelemetry': 5,
   'finops': 5, 'cost': 3, 'three pillars': 4, 'logs': 2,
 },
 'cloud-native-app-delivery': {
   'gitops': 5, 'ci/cd': 5, 'continuous delivery': 5,
   'continuous integration': 5, 'application delivery': 5, 'argo': 4,
   'helm': 4, 'flux': 4, 'pipeline': 3, '"ci"': 4, '"cd"': 4,
   'canary': 4, 'git repositor': 4, 'deliver': 2,
 },
}

KCNA_DOMAIN_TITLES = {
    'kubernetes-fundamentals': 'Kubernetes Fundamentals',
    'container-orchestration': 'Container Orchestration',
    'cloud-native-architecture': 'Cloud Native Architecture',
    'cloud-native-observability': 'Cloud Native Observability',
    'cloud-native-app-delivery': 'Cloud Native Application Delivery',
}

# Notes that still misland after scoring (key: note id).
KCNA_OVERRIDES = {
    1767561281344: 'cloud-native-architecture',    # "What does FaaS stand for?"
    1767561126861: 'container-orchestration',      # PV/PVC storage question
}

# Priority order on score ties — fundamentals is the catch-all domain.
KCNA_PRIORITY = ['kubernetes-fundamentals', 'container-orchestration',
                 'cloud-native-architecture', 'cloud-native-observability',
                 'cloud-native-app-delivery']
CKS_PRIORITY = ['cluster-setup', 'cluster-hardening', 'system-hardening',
                'microservice-vulnerabilities', 'supply-chain-security',
                'monitoring-logging-runtime', 'security-fundamentals',
                'exam-prep']

# --------------------------------------------------------------- logic ---

def score_text(text, kw_map):
    text = ' ' + text.lower() + ' '
    return {d: sum(w * text.count(k) for k, w in kws.items())
            for d, kws in kw_map.items()}

def score_flat(text, kw_map):
    text = text.lower()
    return {d: sum(text.count(k) for k in kws) for d, kws in kw_map.items()}

def pick(scores, priority):
    best = max(priority, key=lambda d: (scores[d], -priority.index(d)))
    return best if scores[best] > 0 else 'misc'

def kcna_domain(nid, notes):
    if nid in KCNA_OVERRIDES:
        return KCNA_OVERRIDES[nid]
    flds = notes[nid]["fields"]
    front = flds[0] if flds else ''
    back = ' '.join(flds[1:])
    sc = score_text(front + ' ' + front + ' ' + back, KCNA_KEYWORDS)
    return pick(sc, KCNA_PRIORITY)

def cks_domains(nids, notes, gap=1000):
    """Split into id-burst segments, score each, return {nid: domain}."""
    segs, cur = [], [nids[0]]
    for a, b in zip(nids, nids[1:]):
        if b - a > gap:
            segs.append(cur)
            cur = []
        cur.append(b)
    segs.append(cur)
    out = {}
    for s in segs:
        if s[0] in CKS_OVERRIDES:
            dom = CKS_OVERRIDES[s[0]]
        else:
            agg = Counter()
            for n in s:
                tags = ' '.join(t for t in notes[n]["tags"]
                                if t != 'ankidote')
                text = tags + ' ' + tags + ' ' + tags + ' ' + \
                    notes[n]["fields"][0]
                agg.update(score_flat(text, CKS_KEYWORDS))
            dom = pick(dict(agg), CKS_PRIORITY)
        for n in s:
            out[n] = dom
    return out

def resplit(deck_dir, deck_name, nids, notes, assign, titles, dry):
    groups = {}
    for n in nids:
        groups.setdefault(assign[n], []).append(n)
    counts = Counter()
    for dom in sorted(groups, key=lambda d: titles.get(d, d)):
        members = sorted(groups[dom])
        counts[dom] = len(members)
        if not dry:
            path = deck_dir / f"{slugify(titles.get(dom, dom))}.md"
            path.write_text(render_file(deck_name, titles.get(dom, dom),
                                        members, notes))
        print(f"  {titles.get(dom, dom):<45} {len(members)} notes")
    if not dry:
        for stale in deck_dir.glob('part-*.md'):
            stale.unlink()
    return counts

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--deck', choices=['cks', 'kcna'], nargs='*',
                    default=['cks', 'kcna'])
    ap.add_argument('--db', default=DEFAULT_DB)
    ap.add_argument('--out', default='cards')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    with tempfile.NamedTemporaryFile(suffix='.anki2') as tmp:
        con = snapshot(args.db, tmp.name)
        decks, note_deck, notes = load(con)
        con.close()
    name2id = {v: k for k, v in decks.items()}

    for which in args.deck:
        if which == 'cks':
            dname = next(d for d in decks.values() if d.startswith('CKS '))
            nids = sorted(n for n, d in note_deck.items()
                          if d == name2id[dname])
            assign = cks_domains(nids, notes)
            print(f"== {dname}")
            resplit(Path(args.out) / 'cks', dname, nids, notes,
                    assign, CKS_DOMAIN_TITLES, args.dry_run)
        else:
            dname = next(d for d in decks.values() if d.startswith('KCNA '))
            nids = sorted(n for n, d in note_deck.items()
                          if d == name2id[dname])
            assign = {n: kcna_domain(n, notes) for n in nids}
            titles = dict(KCNA_DOMAIN_TITLES, misc='Misc')
            print(f"== {dname}")
            resplit(Path(args.out) / 'kcna', dname, nids, notes,
                    assign, titles, args.dry_run)

if __name__ == '__main__':
    main()
