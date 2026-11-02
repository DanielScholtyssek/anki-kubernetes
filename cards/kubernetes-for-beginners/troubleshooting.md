# Kubernetes for Beginners — troubleshooting

> Deck: `Kubernetes for Beginners` · Group: `troubleshooting` · Notes: 5 · Models: Basic, Basic (and reversed card), Many

<!-- note:1793645234411 model:Basic (and reversed card) -->
**Front:** What is crictl?
**Back:** A command-line client for CRI-compatible container runtimes (containerd, CRI-O). It talks to the runtime directly through the Container Runtime Interface — no Docker daemon or Kubernetes API needed — and is mainly used to inspect and debug containers on a node.
**Tags:** k8s::beginners topic::troubleshooting src::session

---

<!-- note:1793645234402 model:Basic -->
**Front:** Why is crictl useful when kubectl or docker cannot help during node debugging?
**Back:** On modern clusters there is no Docker daemon and kubectl may not help when the problem is the node itself. crictl talks to the runtime via the CRI endpoint even while kubelet or the API server is having trouble.
**Tags:** k8s::beginners topic::troubleshooting src::session

---

<!-- note:1793645234403 model:Basic -->
**Front:** How does crictl connect to the container runtime?
**Back:** It talks to the runtime's CRI endpoint — a Unix socket such as unix:///run/containerd/containerd.sock (or CRI-O's socket). The endpoint is passed with --runtime-endpoint or configured in /etc/crictl.yaml.
**Tags:** k8s::beginners topic::troubleshooting src::session

---

<!-- note:1793645234404 model:Basic -->
**Front:** Name useful crictl commands for debugging containers on a node.
**Back:** crictl ps — running containers; crictl pods — pod sandboxes; crictl images — images; crictl logs — container logs; crictl exec — run a command inside a container; crictl inspect — full container/pod details; crictl stats — resource usage.
**Tags:** k8s::beginners topic::troubleshooting src::session

---

<!-- note:1793645234470 model:Many -->
**Domain:** Troubleshooting
**Question:** While debugging a worker node, which crictl command lists the containers currently running on it?
**Options:** A. crictl list<br>B. crictl ps<br>C. crictl containers<br>D. crictl status
**Answer:** B (2) – crictl ps
**Explanation:** crictl mirrors the docker CLI vocabulary: ps lists running containers (ps -a includes stopped ones). For the Kubernetes-level view use crictl pods; crictl images lists images. There is no 'crictl list/containers/status' subcommand.
**Sources:** <a href="https://kubernetes.io/docs/tasks/debug/debug-cluster/crictl/" target="_blank">Kubernetes Documentation - Debugging Kubernetes nodes with crictl</a>
**Tags:** k8s::beginners topic::troubleshooting src::session

---
