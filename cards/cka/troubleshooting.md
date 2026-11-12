# CKA - Certified Kubernetes Administrator — Troubleshooting

> Deck: `CKA - Certified Kubernetes Administrator` · Group: `Troubleshooting` · Notes: 5 · Models: Basic, Cloze

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
