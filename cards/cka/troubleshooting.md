# CKA - Certified Kubernetes Administrator — Troubleshooting

> Deck: `CKA - Certified Kubernetes Administrator` · Group: `Troubleshooting` · Notes: 21 · Models: Basic, Cloze

<!-- note:1794496839293 model:Basic -->
**Front:** Why is crictl useful when kubectl or docker cannot help during node debugging?
**Back:** On modern clusters there is no Docker daemon and kubectl may not help when the problem is the node itself. crictl talks to the runtime via the CRI endpoint even while kubelet or the API server is having trouble.
**Tags:** k8s::cka topic::troubleshooting src::session

---

<!-- note:1794496839296 model:Basic -->
**Front:** While debugging a worker node, which crictl command lists the containers currently running on it?
**Back:** crictl ps<br><br>crictl mirrors the docker CLI vocabulary: ps lists running containers (ps -a includes stopped ones). For the Kubernetes-level view use crictl pods; crictl images lists images. There is no 'crictl list/containers/status' subcommand.
**Tags:** k8s::cka topic::troubleshooting src::session

---

<!-- note:1794496839568 model:Basic -->
**Front:** A container in a pod has been restarted multiple times with 'CrashLoopBackOff' state. What does this indicate?
**Back:** The container exits with a non-zero exit code soon after starting<br><br>CrashLoopBackOff = the container STARTS, exits non-zero almost immediately, kubelet restarts it, repeat — with exponential backoff between attempts. The process itself is failing (bad command, missing file, crash on startup, failed liveness probe). Distractors map to OTHER states: unpullable image → ImagePullBackOff/ErrImagePull (never starts); running-but-unhealthy → liveness probe restarts (which CAUSES CrashLoopBackOff but the state itself means exit); memory → OOMKilled. Triage: kubectl logs --previous + kubectl describe pod.
**Tags:** k8s::cka topic::pods topic::troubleshooting src::session

---

<!-- note:1794496839569 model:Basic -->
**Front:** What does the 'BackOff' part of CrashLoopBackOff mean?
**Back:** Exponential backoff — the kubelet waits progressively longer between restart attempts to avoid hammering a failing container<br><br>The 'BackOff' suffix means the restart delay grows exponentially (10s, 20s, 40s, up to 5min cap) — kubelet won't hot-loop a crash-looping container forever. You see it in events as 'Back-off restarting failed container'. The loop only breaks when the container stays up past the failure window or the pod is fixed/deleted. To debug the ACTUAL cause use 'kubectl logs <pod> --previous' (last crashed instance) — current logs may be empty if it's mid-backoff.
**Tags:** k8s::cka topic::pods topic::troubleshooting src::session

---

<!-- note:1794496839788 model:Cloze -->
**Text:** kubectl logs cheatsheet:<br><br>Basic: <code>kubectl logs {{c1::pod-name}}</code><br>Specific container: <code>-c {{c2::container-name}}</code><br>Last crashed instance: <code>--{{c3::previous}}</code><br>Follow live: <code>-{{c4::f}}</code> / <code>--follow</code><br>Last N lines: <code>--tail={{c5::N}}</code>
**Back Extra:** Full family: kubectl logs <pod> [-c container] [--previous] [-f] [--tail=N] [--since=...]. -c needed only for multi-container pods. --previous shows the last terminated instance's logs (crash debugging). --timestamps adds timestamps. kubectl logs -f streams live.
**Tags:** k8s::cka topic::kubectl topic::logging src::session

---

<!-- note:1794498397421 model:Basic -->
**Front:** What is the correct order for troubleshooting an application failure in Kubernetes?
**Back:** Work from the user-facing end inward: (1) test the user endpoint — curl the NodePort from outside or the Service ClusterIP/DNS from inside a debug pod; (2) inspect the Service — <code>kubectl describe service</code> and check it has Endpoints (empty endpoints = selector matches no pods); (3) check the backing pods — status, restart count, CrashLoopBackOff, <code>kubectl describe pod</code> events; (4) read app logs — <code>kubectl logs -f</code>, <code>-p</code> for the crashed instance, <code>-c</code> for multi-container pods; (5) if the frontend looks healthy, repeat the same Service→Pod→Logs walk on the next tier (e.g. the database). Map the topology first (user → web Service → web Pod → DB Service → DB Pod) so you know which layer to start at.
**Tags:** k8s::cka src::course-kodekloud topic::services topic::troubleshooting

---

<!-- note:1794498397422 model:Basic -->
**Front:** A Kubernetes Service shows an empty Endpoints list. What are the two usual causes?
**Back:** The Service selector matches no pods, or the port mapping is wrong. Endpoints are populated by matching the Service's <code>spec.selector</code> against pod labels — a typo or label drift means zero endpoints and the ClusterIP accepts nothing. Second cause: <code>targetPort</code> doesn't match the container's <code>containerPort</code> — endpoints exist but traffic lands nowhere. Check with <code>kubectl describe svc &lt;name&gt;</code> (Endpoints: line) and compare selector vs <code>kubectl get pods --show-labels</code>.
**Tags:** k8s::cka src::course-kodekloud topic::services topic::troubleshooting

---

<!-- note:1794498397423 model:Basic -->
**Front:** Why does <code>kubectl logs -p &lt;pod&gt;</code> exist, and when do you need it?
**Back:** It prints logs from the pod's PREVIOUS container instance — needed whenever the current container already restarted. After CrashLoopBackOff the live container is a fresh process whose log only covers the new attempt; the crash evidence (the exception, the config error) lives in the previous instance's log, reachable only via -p. Without -p you debug the wrong run.
**Tags:** k8s::cka src::course-kodekloud topic::kubectl topic::troubleshooting

---

<!-- note:1794498397424 model:Basic -->
**Front:** What do node conditions in <code>kubectl describe node</code> tell you, and what does Ready=Unknown with reason NodeStatusUnknown mean?
**Back:** Conditions report kubelet-posted health: OutOfDisk, MemoryPressure, DiskPressure, PIDPressure and Ready (True/False/Unknown). Ready=Unknown + NodeStatusUnknown means the kubelet STOPPED POSTING status — check LastHeartbeatTime for when it went silent, then verify the node itself (power, hypervisor, network) before blaming Kubernetes. A NotReady node usually means kubelet is down or can't reach the API server; pressure conditions (DiskPressure etc.) mean the kubelet is alive but the node is resource-starved and the scheduler will avoid it / evict pods.
**Tags:** k8s::cka src::course-kodekloud topic::nodes topic::troubleshooting

---

<!-- note:1794498397425 model:Basic -->
**Front:** A worker node shows MemoryPressure=True in its conditions. What happens and what's the first thing to check?
**Back:** MemoryPressure means the node is under memory stress — the kubelet reports it so the scheduler stops placing new pods there and may evict pods to relieve pressure. First checks on the node: <code>top</code>/<code>free -m</code> for what's consuming memory, then kubelet logs (<code>journalctl -u kubelet</code>) for eviction events naming the culprit pods. The condition clears when memory frees up; it does NOT fix itself if a pod has a leak.
**Tags:** k8s::cka src::course-kodekloud topic::nodes topic::troubleshooting

---

<!-- note:1794498397426 model:Basic -->
**Front:** What is the correct order for troubleshooting a control-plane failure?
**Back:** Nodes first, then components, then logs, then dependencies. (1) <code>kubectl get nodes</code> — are nodes Ready? If NotReady, fix node/kubelet/networking first. (2) Inspect control-plane components — pod-managed clusters (kubeadm): <code>kubectl get pods -n kube-system</code> looking for CrashLoopBackOff/ImagePullBackOff on etcd, kube-apiserver, kube-controller-manager, kube-scheduler; host-managed: <code>systemctl status kube-apiserver</code>. (3) Logs — <code>kubectl logs &lt;cp-pod&gt; -n kube-system</code> or <code>journalctl -u kube-apiserver</code>. (4) Dependencies — etcd quorum, certificate expiry, clock skew (NTP), firewall/ports between nodes, recent config changes, CPU/memory/disk pressure. If the API server is down, restore it and etcd before chasing app issues — nothing else works without them.
**Tags:** k8s::cka src::course-kodekloud topic::control-plane topic::troubleshooting

---

<!-- note:1794498397427 model:Basic -->
**Front:** How do you check control-plane component health on a kubeadm cluster vs a host-installed cluster?
**Back:** Kubeadm runs control-plane components as STATIC PODS: <code>kubectl get pods -n kube-system</code> (look for etcd-*, kube-apiserver-*, kube-controller-manager-*, kube-scheduler-*), <code>kubectl describe pod &lt;name&gt; -n kube-system</code> for events, <code>kubectl logs &lt;name&gt; -n kube-system</code> for output. Host-installed (systemd/service) clusters: SSH to the control-plane node and use <code>systemctl status kube-apiserver</code> / <code>service kube-apiserver status</code>, logs via <code>journalctl -u kube-apiserver</code>. Same logic extends to kubelet/kube-proxy on workers.
**Tags:** k8s::cka src::course-kodekloud topic::control-plane topic::troubleshooting

---

<!-- note:1794498397428 model:Basic -->
**Front:** A worker node is unreachable (NotReady, conditions Unknown). Walk through the troubleshooting steps.
**Back:** (1) Confirm scope — <code>kubectl get nodes</code> + <code>kubectl describe node &lt;name&gt;</code>: check Conditions and LastHeartbeatTime to see when the kubelet went silent. (2) If conditions are Unknown, verify the node itself first — power, hypervisor/cloud instance state, network reachability; try SSH or the provider console. (3) On the node: host health — <code>top</code>, <code>df -h</code>, <code>df -i</code>, <code>free -m</code> for CPU/mem/disk/inode pressure. (4) Kubelet — <code>systemctl status kubelet</code> and <code>journalctl -u kubelet -n 200</code> for auth/cert/network/filesystem errors. (5) Kubelet certificate — <code>openssl x509 -in /var/lib/kubelet/&lt;node&gt;.crt -text -noout</code>: expired cert or wrong Subject/SAN breaks API authentication and the node drops to NotReady. Fix by rotating credentials or rejoining the node.
**Tags:** k8s::cka src::course-kodekloud topic::nodes topic::troubleshooting

---

<!-- note:1794498397429 model:Basic -->
**Front:** How do you verify a kubelet's client certificate on a node, and what should it contain?
**Back:** <code>openssl x509 -in /var/lib/kubelet/&lt;node-name&gt;.crt -text -noout</code> — check Validity (expired = kubelet can't authenticate to the API server → node goes NotReady), Issuer (should be the cluster CA), Subject <code>CN = system:node:&lt;node-name&gt;</code> with <code>O = system:nodes</code>, and SANs covering the node's DNS name and IP addresses. A kubelet cert whose SANs don't include the node IP breaks TLS verification and node registration.
**Tags:** k8s::cka src::course-kodekloud topic::nodes topic::troubleshooting

---

<!-- note:1794498397430 model:Basic -->
**Front:** What is the recommended order for troubleshooting Kubernetes service/network connectivity?
**Back:** Work outward from the pod: (1) Pod health — <code>kubectl get pods -l app=&lt;name&gt;</code>, logs, describe; a Service only routes to Ready pods. (2) Direct pod connectivity — bypass the Service entirely: get pod IPs (<code>kubectl get pods -o wide</code> or <code>-o jsonpath='{.items[*].status.podIP}'</code>) and curl/wget podIP:port from a temp busybox pod — if this fails it's the app or CNI, not the Service. (3) Service layer — <code>kubectl get svc &lt;name&gt; -o yaml</code> (selector + port→targetPort) and <code>kubectl get endpointslices -l kubernetes.io/service-name=&lt;name&gt;</code> for actual backends. (4) DNS — CoreDNS pods in kube-system, kube-dns endpoints, pod's /etc/resolv.conf. (5) CNI — pod IP assignment and pod-to-pod networking. (6) kube-proxy — the iptables/IPVS rules that actually forward Service traffic.
**Tags:** k8s::cka src::course-kodekloud topic::networking topic::troubleshooting

---

<!-- note:1794498397431 model:Basic -->
**Front:** How do you test connectivity between two pods directly, removing the Service from the equation?
**Back:** Run a temporary pod and hit the target pod's IP directly: <code>kubectl run -it --rm --restart=Never busybox --image=busybox -- sh</code> then inside it <code>wget -qO- http://&lt;pod-ip&gt;:&lt;port&gt;</code>. Get pod IPs with <code>kubectl get pods -o wide</code> or <code>kubectl get pods -l app=x -o=jsonpath='{.items[*].status.podIP}'</code>. If direct podIP access works but the Service doesn't, the problem is in the Service/endpoints/kube-proxy layer; if direct access fails too, it's the app or CNI.
**Tags:** k8s::cka src::course-kodekloud topic::networking topic::troubleshooting

---

<!-- note:1794498397432 model:Basic -->
**Front:** Walk through troubleshooting cluster DNS (CoreDNS) failures.
**Back:** (1) CoreDNS pods — they run in kube-system: <code>kubectl get pods -n kube-system -l k8s-app=kube-dns</code>; Pending suggests CNI problems, CrashLoopBackOff → <code>kubectl logs -n kube-system &lt;coredns-pod&gt;</code>. (2) kube-dns Service endpoints — <code>kubectl get endpointslices -l kubernetes.io/service-name=kube-dns -n kube-system</code>; empty means the selector isn't matching CoreDNS pods. (3) Pod resolver config — <code>kubectl exec -it &lt;pod&gt; -- cat /etc/resolv.conf</code>: nameserver should be the kube-dns Service ClusterIP; check search domains and ndots. (4) Test resolution — <code>kubectl exec -it busybox -- nslookup &lt;svc&gt;.&lt;ns&gt;.svc.cluster.local</code>. CoreDNS is configured via its Corefile ConfigMap in kube-system.
**Tags:** k8s::cka src::course-kodekloud topic::coredns topic::troubleshooting

---

<!-- note:1794498397433 model:Basic -->
**Front:** What are the symptoms of a broken CNI plugin, and what's the alphabetical-config gotcha?
**Back:** Symptoms: pods stuck Pending with no IP (CNI can't allocate), or pods Running but with no pod-to-pod connectivity. The kubelet uses the FIRST CNI config file it finds ALPHABETICALLY in the CNI config directory — if multiple CNI configs exist (e.g. two plugins installed), the alphabetically-first wins and the other is silently ignored; remove or rename unwanted configs. Debug by checking the CNI DaemonSet pods are Running (<code>kubectl get ds -n &lt;cni-ns&gt;</code>), their logs for allocation errors, and kubelet logs for CNI failures.
**Tags:** k8s::cka src::course-kodekloud topic::cni topic::troubleshooting

---

<!-- note:1794498397434 model:Basic -->
**Front:** How do you troubleshoot kube-proxy when Services have endpoints but traffic doesn't flow?
**Back:** kube-proxy programs the node-level forwarding rules (iptables or IPVS mode) that map Service IPs to pod backends. Check: (1) pods — <code>kubectl get pods -n kube-system -l k8s-app=kube-proxy</code> all Running; (2) logs — <code>kubectl logs -n kube-system &lt;kube-proxy-pod&gt;</code> for sync errors; (3) mode — <code>kubectl get configmap kube-proxy -n kube-system -o yaml</code> shows mode: iptables or ipvs; (4) actual rules on the node — iptables mode: inspect iptables NAT rules; ipvs mode: <code>ipvsadm -Ln</code> should list Service VIPs mapped to pod backend IPs. Empty ipvsadm output or missing iptables DNAT rules = kube-proxy isn't programming correctly.
**Tags:** k8s::cka src::course-kodekloud topic::networking topic::troubleshooting

---

<!-- note:1794498397435 model:Basic -->
**Front:** What does Metrics Server do, how does <code>kubectl top</code> work, and why is Heapster mentioned in old docs?
**Back:** Metrics Server is the lightweight in-cluster metrics pipeline: it scrapes each node's kubelet Summary API (cAdvisor stats), aggregates in memory, and serves the Kubernetes Metrics API that <code>kubectl top nodes</code> / <code>kubectl top pods [--all-namespaces]</code> query. It stores NO history — for trends you need Prometheus or a TSDB. Heapster was the original metrics project and is DEPRECATED — replaced by Metrics Server. If <code>kubectl top</code> returns nothing, check the metrics-server pods in kube-system and that kubelet Summary endpoints are reachable (firewall/RBAC can block it).
**Tags:** k8s::cka src::course-kodekloud topic::monitoring topic::troubleshooting

---

<!-- note:1794498397436 model:Basic -->
**Front:** When would you use crictl instead of kubectl or docker on a node?
**Back:** crictl talks to the container runtime through the CRI socket — it's the tool for debugging at the CONTAINER level on a node: <code>crictl ps</code> lists containers, <code>crictl images</code>, <code>crictl logs &lt;container-id&gt;</code>. Use it when kubectl can't help (node-level issues, pod won't start, kubelet problems) or when docker isn't the runtime — modern clusters run containerd/CRI-O which have no docker CLI. It shows what the kubelet sees: containers, images, and their logs independent of pod state.
**Tags:** k8s::cka src::course-kodekloud topic::cri-oci topic::troubleshooting

---
