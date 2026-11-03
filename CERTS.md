# Golden Kubestronaut — exam formats

Reference for the full Golden Kubestronaut track: pass **all CNCF
certifications + LFCS**. Every exam-format entry below was confirmed on
the certification's official CNCF page (Nov 2026); durations and pass
scores come from the same pages, LF exam FAQs, and — where not
published officially — community-maintained tables. CNCF adds certs
over time — re-check the
[official list](https://training.linuxfoundation.org/resources/kubestronaut-program/)
before relying on this.

**The split that matters:** 6 exams are hands-on (a terminal and a live
environment — no multiple choice to fall back on), 10 are pure
multiple choice. Studying for the hands-on ones means hours at a
command line; Anki decks mainly help with the MCQ material and with
commands/flags you need memorized for the practical ones.

## Hands-on (performance-based) — 6 exams

Tasks solved in a real environment (live cluster / Linux remote
desktop). All include access to a killer.sh-style exam simulator.

| Cert | Deck folder | Duration | Pass | Notes |
|---|---|---|---|---|
| CKA | `cards/cka/` | 2 h | 66% | cluster admin tasks on live clusters |
| CKAD | `cards/ckad/` | 2 h | 66% | app-dev tasks on live clusters |
| CKS | `cards/cks/` | 2 h | 67% | **requires an active CKA first** |
| ICA | `cards/ica/` | 2 h | 68% | **hybrid** — performance-based items AND MCQ; the odd one out among associates |
| CNPE | `cards/cnpe/` | 2 h | 64% | platform engineering; terminal + web UIs |
| LFCS | `cards/lfcs/` | 2 h | 67% | Linux sysadmin; not CNCF but required for Golden |

## Multiple choice — 10 exams

Online proctored MCQ. Roughly 60 questions unless noted.

| Cert | Deck folder | Duration | Pass | Notes |
|---|---|---|---|---|
| KCNA | `cards/kcna/` | 90 min | 75% | entry-level k8s + cloud native overview |
| KCSA | `cards/kcsa/` | 90 min | 75% | baseline security concepts |
| PCA | `cards/pca/` | 90 min | 75% | Prometheus, PromQL |
| CCA | `cards/cca/` | 90 min | 75% | Cilium / eBPF networking |
| CAPA | `cards/capa/` | 90 min | 75% | Argo project (CD, Rollouts, Workflows, Events) |
| CGOA | `cards/cgoa/` | 90 min | 75% | GitOps principles, tool-agnostic |
| CBA | `cards/cba/` | 90 min | 75% | Backstage / developer portals |
| OTCA | `cards/otca/` | 90 min | 75% | OpenTelemetry traces/metrics/Collector |
| KCA | `cards/kca/` | 90 min | 75% | Kyverno policy engine |
| CNPA | `cards/cnpa/` | **120 min** | 75% | ~85 questions — the longest MCQ; platform engineering concepts (CNCF Platforms white paper) |

## Common to all

- Online, proctored (streaming audio/video/screenshare).
- One free retake, 12-month exam eligibility, 2-year certification
  validity.
- Golden Kubestronaut is for life once earned — new certs added later
  don't revoke it (but you do need to *earn* it against the list
  current at the time).

## Study-order suggestion

Beginners deck (`cards/kubernetes-for-beginners/`) covers shared
foundations (YAML, ReplicaSets, Deployments, labels/selectors). A
sensible order: KCNA → KCSA → associates (PCA/CGOA/CAPA/etc.) → CKA →
CKAD → CKS → ICA → LFCS → CNPA → CNPE. The MCQ certs map 1:1 to this
repo's card decks; for the hands-on exams the cards are a supplement to
lab practice, not a substitute.
