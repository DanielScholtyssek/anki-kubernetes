# Kubernetes for Beginners — architecture

> Deck: `Kubernetes for Beginners` · Group: `architecture` · Notes: 15 · Models: Basic, Basic (and reversed card), Cloze, Many

<!-- note:1793643778643 model:Basic (and reversed card) -->
**Front:** What is a node in Kubernetes?
**Back:** A physical or virtual machine on which Kubernetes is installed. It is a worker machine — Kubernetes launches the application's containers on nodes.
**Tags:** k8s::beginners topic::architecture src::session

---

<!-- note:1793643778656 model:Basic -->
**Front:** What happens to your application if the node it runs on fails?
**Back:** If the application only runs on that single node, it goes down. That is why applications run on a cluster of multiple nodes — the remaining nodes can take over the workload.
**Tags:** k8s::beginners topic::architecture src::session

---

<!-- note:1793643778644 model:Basic (and reversed card) -->
**Front:** What is a cluster in Kubernetes?
**Back:** A set of nodes grouped together to run containerized applications. Workloads are spread across the nodes, so the application survives the failure of any single node.
**Tags:** k8s::beginners topic::architecture src::session

---

<!-- note:1793643778666 model:Cloze -->
**Text:** Control plane nodes were previously called {{c1::master}} nodes.
**Back Extra:** The term was renamed to 'control plane'; 'master' still appears in older courses and docs.
**Tags:** k8s::beginners topic::architecture src::session

---

<!-- note:1793643778645 model:Basic (and reversed card) -->
**Front:** What is the control plane in Kubernetes?
**Back:** The set of components that manages the cluster: it stores all cluster state, monitors nodes, assigns workloads to nodes, and moves workloads off nodes that fail. Previously called the 'master'.
**Tags:** k8s::beginners topic::architecture src::session

---

<!-- note:1793643778657 model:Basic -->
**Front:** What is the difference between a worker node and a control plane node?
**Back:** Worker nodes run the actual application containers. Control plane nodes run the components that manage the cluster (API server, etcd, scheduler, controller-manager) and do not normally run user workloads.
**Tags:** k8s::beginners topic::architecture src::session

---

<!-- note:1793643778658 model:Basic -->
**Front:** Which Kubernetes components run on the control plane, and which run on every node?
**Back:** Control plane only: kube-apiserver, etcd, kube-scheduler, controller-manager (+ cloud-controller-manager for cloud-integrated control loops). Every node (control plane AND workers): kubelet, container runtime, AND kube-proxy — kube-proxy runs as a DaemonSet so every node gets service networking rules.
**Tags:** k8s::beginners topic::architecture src::session

---

<!-- note:1793643778646 model:Basic (and reversed card) -->
**Front:** What does the kube-apiserver do?
**Back:** It is the frontend of Kubernetes. All clients — kubectl, the web UI, and the cluster's own components — talk to the API server to interact with the cluster.
**Tags:** k8s::beginners topic::architecture src::session

---

<!-- note:1793643778647 model:Basic (and reversed card) -->
**Front:** What is etcd in Kubernetes?
**Back:** A distributed, reliable key-value store used by Kubernetes to persist all cluster data — node state, configuration, and the desired and current state of every workload.
**Tags:** k8s::beginners topic::architecture src::session

---

<!-- note:1793643778648 model:Basic (and reversed card) -->
**Front:** What does the kube-scheduler do?
**Back:** It assigns new workloads (pods) to nodes. It picks a suitable node for each workload based on criteria like resource requirements, node capacity, and placement rules.
**Tags:** k8s::beginners topic::architecture src::session

---

<!-- note:1793643778649 model:Basic (and reversed card) -->
**Front:** What does the controller-manager do in Kubernetes?
**Back:** It runs the controllers — the brain behind orchestration. They watch the cluster state through the API server and respond to changes, e.g. moving workloads off a node that failed.
**Tags:** k8s::beginners topic::architecture src::session

---

<!-- note:1793643778650 model:Basic (and reversed card) -->
**Front:** What is a kubelet?
**Back:** An agent that runs on every node. It receives instructions from the API server, makes sure the containers assigned to that node run as expected, and reports their status back.
**Tags:** k8s::beginners topic::architecture src::session

---

<!-- note:1793643778651 model:Basic (and reversed card) -->
**Front:** What is the container runtime in Kubernetes?
**Back:** The software on each node that actually runs containers — pulling images and starting/stopping containers (e.g. containerd, CRI-O).
**Tags:** k8s::beginners topic::architecture src::session

---

<!-- note:1793643778652 model:Basic (and reversed card) -->
**Front:** What is kubectl?
**Back:** The Kubernetes command-line tool used to deploy and manage applications on a cluster — deploy workloads, get cluster and resource status, and manage cluster objects.
**Tags:** k8s::beginners topic::architecture src::session

---

<!-- note:1793643778696 model:Many -->
**Domain:** Kubernetes Architecture
**Question:** You run kubectl get pods to inspect a cluster. Which component receives and answers the request?
**Options:** A. etcd<br>B. kubelet on a worker node<br>C. kube-apiserver<br>D. kube-scheduler
**Answer:** C (3) – kube-apiserver
**Explanation:** The API server is the cluster's frontend: kubectl and every other client (and the cluster's own components) send requests to it. etcd only stores the data the API server reads, the scheduler places new workloads, and kubelets manage containers on their own node.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/components/" target="_blank">Kubernetes Documentation - Kubernetes Components</a>
**Tags:** k8s::beginners topic::architecture src::session

---
