# Kubernetes for Beginners — networking

> Deck: `Kubernetes for Beginners` · Group: `networking` · Notes: 9 · Models: Basic, Basic (and reversed card), Cloze, Many

<!-- note:1793733804357 model:Basic -->
**Front:** How does a pod get its IP address in Kubernetes?
**Back:** When a pod is created, the CNI plugin assigns it a unique, cluster-wide IP address from the pod network (invoked via the kubelet → container runtime chain). Every container INSIDE one pod shares that single IP and network namespace — they reach each other over localhost. A pod's IP dies with the pod; a new pod gets a new IP.
**Tags:** k8s::beginners topic::networking topic::pods src::session

---

<!-- note:1793733804358 model:Basic -->
**Front:** What are the connectivity rules every Kubernetes cluster network must satisfy?
**Back:** The Kubernetes network model guarantees: (1) every pod gets its own cluster-wide IP; (2) all pods can talk to all other pods on ANY node, directly, without NAT or proxies — the destination IP is the pod's real IP; (3) node agents (kubelet, system daemons) can talk to all pods on their node. A pod sees its own IP as the same address others see it as. (Intentional segmentation is possible via NetworkPolicy.)
**Tags:** k8s::beginners topic::networking topic::pods src::session

---

<!-- note:1793733804359 model:Basic -->
**Front:** Why does Kubernetes require pod-to-pod communication without NAT?
**Back:** It makes pods behave like independent machines on one flat network: no port mapping, no NAT, no links needed — pod A on node 1 reaches pod B on node 3 directly by its pod IP. Older container systems forced you to map container ports onto host ports to make containers reachable across hosts; Kubernetes removed that pain by design.
**Tags:** k8s::beginners topic::networking topic::pods src::session

---

<!-- note:1793733804360 model:Basic -->
**Front:** How does traffic between pods on DIFFERENT nodes actually get delivered?
**Back:** The CNI plugin builds a cluster-wide virtual network. When pod A on node 1 sends traffic to pod B's IP on node 2, the plugin routes it there — either by programming real routes or by encapsulating packets (e.g. VXLAN tunnels) over the physical node network. To the pods it looks like a single flat network; the cross-node mechanics are invisible.
**Tags:** k8s::beginners topic::cni topic::networking src::session

---

<!-- note:1793733804394 model:Basic (and reversed card) -->
**Front:** What is the pod network CIDR in Kubernetes, and what is it separate from?
**Back:** The internal virtual IP range reserved for pod IPs across the whole cluster — the CIDR the pod network draws addresses from (e.g. 10.244.0.0/16 for default Flannel). It's separate from the Service CIDR (ClusterIP range, e.g. 10.96.0.0/12), which is for stable Service IPs, not pods.
**Tags:** k8s::beginners topic::networking topic::services src::session

---

<!-- note:1793733804395 model:Basic (and reversed card) -->
**Front:** What is CNI in Kubernetes?
**Back:** Container Network Interface — the plugin standard Kubernetes uses (via the container runtime) to wire pods into the network. CNI plugins like Calico, Flannel or Cilium assign pod IPs (IPAM) and build the virtual/overlay network that connects all pods across all nodes — they implement the pod network the k8s model requires; many also enforce NetworkPolicy.
**Tags:** k8s::beginners topic::cni topic::networking src::session

---

<!-- note:1793733804424 model:Cloze -->
**Text:** The Kubernetes network model:<br><br>Every pod gets its own {{c1::cluster-wide IP address}}.<br>All pods can talk to all pods on any node {{c2::without NAT}}.<br>Nodes can talk to pods and vice versa {{c2::without NAT}}.<br>The pod network itself is built by {{c3::CNI}} plugins (e.g. Calico, Flannel, Cilium).
**Back Extra:** These are the guarantees the pod network must provide — no NAT between pods on any node. The CNI plugin (Calico/Flannel/Cilium) is what builds that network: assigns IPs and routes/encapsulates traffic across nodes.
**Tags:** k8s::beginners topic::cni topic::networking src::session

---

<!-- note:1793733804451 model:Many -->
**Domain:** Networking
**Question:** Which statement is a requirement of the Kubernetes network model?
**Options:** A. Every pod shares its node's IP address<br>B. Pods on any node can reach pods on other nodes directly, without NAT<br>C. Cross-node pod traffic must go through NAT/port-forwarding<br>D. Only pods on the same node may communicate
**Answer:** B (2) – Pods on any node can reach pods on other nodes directly, without NAT
**Explanation:** The Kubernetes network model requires flat pod-to-pod connectivity: every pod has its own cluster-wide IP and can reach any other pod without NAT, regardless of which node it's on. Pods do NOT share the node IP, and cross-node traffic is allowed by default.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/" target="_blank">Kubernetes Documentation - Services, Load Balancing, and Networking</a>
**Tags:** k8s::beginners topic::networking topic::pods src::session

---

<!-- note:1793733804452 model:Many -->
**Domain:** Networking
**Question:** What does a CNI plugin like Calico, Flannel, or Cilium provide?
**Options:** A. It schedules pods onto nodes<br>B. It load-balances Service traffic<br>C. It assigns pod IPs and builds the network connecting pods across nodes<br>D. It stores cluster state in etcd
**Answer:** C (3) – It assigns pod IPs and builds the network connecting pods across nodes
**Explanation:** CNI (Container Network Interface) plugins implement the pod network: they give each pod an IP and route or tunnel traffic between pods on different nodes — that's how the k8s 'no NAT' model is realized. Scheduling is the kube-scheduler's job, Service load balancing is kube-proxy's (or the plugin's own proxy), and object storage is etcd's.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/" target="_blank">Kubernetes Documentation - Services, Load Balancing, and Networking</a>
**Tags:** k8s::beginners topic::cni topic::networking src::session

---
