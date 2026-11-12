# CKA - Certified Kubernetes Administrator — Services & Networking

> Deck: `CKA - Certified Kubernetes Administrator` · Group: `Services & Networking` · Notes: 81 · Models: Basic, Basic (and reversed card), Cloze

<!-- note:1794496839257 model:Basic -->
**Front:** How does traffic between pods on DIFFERENT nodes actually get delivered?
**Back:** The CNI plugin builds a cluster-wide virtual network. When pod A on node 1 sends traffic to pod B's IP on node 2, the plugin routes it there — either by programming real routes or by encapsulating packets (e.g. VXLAN tunnels) over the physical node network. To the pods it looks like a single flat network; the cross-node mechanics are invisible.
**Tags:** k8s::cka topic::cni topic::networking src::session

---

<!-- note:1794496839259 model:Basic -->
**Front:** What does a CNI plugin like Calico, Flannel, or Cilium provide?
**Back:** It assigns pod IPs and builds the network connecting pods across nodes<br><br>CNI (Container Network Interface) plugins implement the pod network: they give each pod an IP and route or tunnel traffic between pods on different nodes — that's how the k8s 'no NAT' model is realized. Scheduling is the kube-scheduler's job, Service load balancing is kube-proxy's (or the plugin's own proxy), and object storage is etcd's.
**Tags:** k8s::cka topic::cni topic::networking src::session

---

<!-- note:1794496839260 model:Basic -->
**Front:** Why does Kubernetes wrap containers in pods instead of deploying bare containers?
**Back:** The pod is the unit Kubernetes schedules and manages: it gives its container(s) a shared environment — one IP address and network namespace plus shared storage volumes — so the runtime treats them as one application instance.
**Tags:** k8s::cka topic::pods src::session

---

<!-- note:1794496839280 model:Basic -->
**Front:** In a Service manifest, what is the difference between <code>port</code>, <code>targetPort</code> and <code>nodePort</code>?
**Back:** Three different port roles: <code>port</code> — the port the Service itself listens on (what clients connect to, on the clusterIP). <code>targetPort</code> — the port on the backend pods traffic is forwarded to (defaults to the same value as <code>port</code>; can also be a named container port). <code>nodePort</code> — only for type NodePort: the static port opened on every node's IP (default range 30000-32767) that outside traffic hits.
**Tags:** k8s::cka topic::networking topic::services src::session

---

<!-- note:1794496839281 model:Basic -->
**Front:** When you create a NodePort Service, what happens on the cluster's nodes?
**Back:** The same port number is opened on EVERY node in the cluster — each node proxies <code>nodePort</code> into the Service, which forwards to a ready backend pod (which may live on a different node). So you can reach the app from outside via <code>&lt;any-node-IP&gt;:&lt;nodePort&gt;</code> — no single node is special. A NodePort Service also gets a clusterIP automatically; it builds on ClusterIP.
**Tags:** k8s::cka topic::networking topic::services src::session

---

<!-- note:1794496839282 model:Basic -->
**Front:** What is the DEFAULT port range a NodePort Service can be allocated from?
**Back:** 30000-32767<br><br>The control plane allocates NodePorts from the --service-node-port-range flag, default 30000-32767. You can pin a specific port via the nodePort field as long as it's inside that range and free; leave it empty for auto-allocation.
**Tags:** k8s::cka topic::networking topic::services src::session

---

<!-- note:1794496839283 model:Basic -->
**Front:** Which Service type gives a stable IP reachable only from inside the cluster — and is the default when <code>spec.type</code> is omitted?
**Back:** ClusterIP<br><br>ClusterIP is the default: a stable virtual IP reachable only inside the cluster — used for internal service-to-service traffic. NodePort exposes it on every node's IP; LoadBalancer asks for an external LB; ExternalName is just a DNS CNAME with no proxying.
**Tags:** k8s::cka topic::networking topic::services src::session

---

<!-- note:1794496839284 model:Basic -->
**Front:** A NodePort Service is created with nodePort 30080. What can clients connect to?
**Back:** Every node opens the same nodePort and forwards to a ready backend pod<br><br>The nodePort is allocated cluster-wide: each node proxies that port into the Service, so <any-node-IP>:<nodePort> works — the backend pod may even be on another node. The Service also gets a clusterIP (NodePort builds on ClusterIP).
**Tags:** k8s::cka topic::networking topic::services src::session

---

<!-- note:1794496839285 model:Basic -->
**Front:** A frontend microservice needs to call backend pods whose IPs keep changing. What should it connect to, and why?
**Back:** It connects to the backend's ClusterIP Service — by its stable name or cluster IP, never to individual pod IPs. Pod IPs change on every reschedule/restart; the Service's clusterIP stays fixed for the Service's lifetime and load-balances across whichever pods currently match its selector. This is THE standard way microservices call each other inside a cluster.
**Tags:** k8s::cka topic::networking topic::services src::session

---

<!-- note:1794496839286 model:Basic -->
**Front:** How does a ClusterIP Service give a group of pods (e.g. all backend pods) a single name?
**Back:** Creating a Service named <code>backend</code> registers a cluster-internal DNS name for that whole group of selector-matched pods — CoreDNS publishes <code>backend.&lt;namespace&gt;.svc.cluster.local</code>, which resolves to the Service's clusterIP. Pods in the same namespace can just use <code>backend</code>; other namespaces need <code>backend.&lt;namespace&gt;</code>. So one name stands in for the entire, ever-changing pod group.
**Tags:** k8s::cka topic::dns topic::networking topic::services src::session

---

<!-- note:1794496839287 model:Basic -->
**Front:** Frontend pods must reach a backend group of pods inside the cluster. The backend pods are rescheduled frequently. Which object provides a stable internal endpoint, DNS name and load balancing?
**Back:** ClusterIP Service<br><br>ClusterIP is built exactly for this: one stable internal IP + DNS name that load-balances across selector-matched pods, so rescheduling never breaks callers. NodePort/LoadBalancer expose traffic OUTSIDE the cluster — wrong tool for internal calls. Hardcoding pod IPs breaks on every reschedule.
**Tags:** k8s::cka topic::networking topic::services src::session

---

<!-- note:1794496839288 model:Basic -->
**Front:** On a supported cloud platform, what provisions the external load balancer for a <code>type: LoadBalancer</code> Service?
**Back:** The cloud provider integration (cloud-controller-manager) asynchronously provisions a real external load balancer — e.g. an AWS/GCP/Azure LB — and publishes its public IP/hostname in the Service's <code>.status.loadBalancer.ingress</code>. Under the hood the Service still gets a clusterIP and nodePort first; the cloud LB is then configured to forward to the nodePort (unless <code>spec.allocateLoadBalancerNodePorts: false</code>).
**Tags:** k8s::cka topic::networking topic::services src::session

---

<!-- note:1794496839289 model:Basic -->
**Front:** How can <code>type: LoadBalancer</code> Services work on bare-metal or homelab clusters with no cloud provider?
**Back:** You must install a tool that fills the cloud provider's role. Options: <b>MetalLB</b> (assigns IPs from a configured pool, announces via ARP/BGP), <b>Cilium LB IPAM</b> (built into the Cilium CNI), kube-vip, or similar. Without one, <code>type: LoadBalancer</code> Services sit at EXTERNAL-IP <code>&lt;pending&gt;</code> forever — Kubernetes itself ships no LB implementation.
**Tags:** k8s::cka topic::networking topic::services src::session

---

<!-- note:1794496839290 model:Basic -->
**Front:** How does Cilium provide <code>type: LoadBalancer</code> Services without a cloud provider?
**Back:** Two pieces: (1) <b>LB IPAM</b> — the administrator creates <code>CiliumLoadBalancerIPPool</code> CRDs defining allocatable IP blocks (CIDRs or start/stop ranges, optionally scoped by a <code>serviceSelector</code>); Cilium assigns an IP from a matching pool to each LoadBalancer Service. (2) <b>Announcement</b> — Cilium advertises reachability via its BGP Control Plane or L2 announcements (ARP/NDP). The EXTERNAL-IP stays <code>&lt;pending&gt;</code> until a pool matches and assigns.
**Tags:** k8s::cka topic::cni topic::networking topic::services src::session

---

<!-- note:1794496839291 model:Basic -->
**Front:** On a local test cluster, a Service with type: LoadBalancer shows EXTERNAL-IP &lt;pending&gt; for hours. What's the most likely reason?
**Back:** No load balancer implementation exists to provision the external IP<br><br>type: LoadBalancer delegates to an external implementation: on cloud platforms the cloud-controller-manager, on bare metal a tool like MetalLB or Cilium LB IPAM. Without one, EXTERNAL-IP stays <pending> — the nodePort and selector are fine, nothing is missing in the manifest itself.
**Tags:** k8s::cka topic::networking topic::services src::session

---

<!-- note:1794496839292 model:Basic -->
**Front:** What role does a CiliumLoadBalancerIPPool play?
**Back:** The CiliumLoadBalancerIPPool defines which external IPs Cilium can assign to LoadBalancer Services<br><br>Cilium's LB IPAM draws Service external IPs from CiliumLoadBalancerIPPool CRDs (CIDRs or start/stop ranges, optionally restricted per-Service via serviceSelector). BGP Control Plane or L2 announcements then advertise the assigned IP. No pool → EXTERNAL-IP stays <pending>.
**Tags:** k8s::cka topic::cni topic::networking topic::services src::session

---

<!-- note:1794496839294 model:Basic -->
**Front:** How does crictl connect to the container runtime?
**Back:** It talks to the runtime's CRI endpoint — a Unix socket such as unix:///run/containerd/containerd.sock (or CRI-O's socket). The endpoint is passed with --runtime-endpoint or configured in /etc/crictl.yaml.
**Tags:** k8s::cka topic::troubleshooting src::session

---

<!-- note:1794496839304 model:Basic -->
**Front:** Which kubectl command exposes a Deployment named <code>web</code> as a NodePort Service on port 80?
**Back:** <code>kubectl expose deployment web --type=NodePort --port=80</code> — <code>--port</code> is the port the Service listens on; <code>--type=NodePort</code> makes it open a 30000-32767 port on every node. Alternative: <code>kubectl create service nodeport web --tcp=80:8080</code> (servicePort:targetPort). To convert an existing service: <code>kubectl patch svc web -p '{"spec":{"type":"NodePort"}}'</code>.
**Tags:** k8s::cka src::session topic::kubectl topic::services

---

<!-- note:1794496839323 model:Basic -->
**Front:** A fresh cluster's DNS pods (CoreDNS) and kube-proxy land in which namespace — deliberately separated from user workloads so they can't be accidentally deleted?
**Back:** kube-system<br><br>kube-system holds the cluster's own objects — CoreDNS, kube-proxy, and (in kubeadm clusters) the control-plane static pods. Putting them in their own namespace keeps them out of your '<code>kubectl get all</code>' view and protects them from accidental deletion — you have to explicitly target -n kube-system. kube-public is for data readable by ALL users; kube-node-lease holds node heartbeats.
**Tags:** k8s::cka src::session topic::architecture topic::namespaces

---

<!-- note:1794496839369 model:Basic -->
**Front:** Before applying Kubernetes-level security controls, what should be hardened first?
**Back:** harden the underlying hosts first: SSH key-only login, no password auth, patched OS<br><br>Defense starts below Kubernetes: the cluster lives on its nodes, and a rooted node means a rooted cluster. Baseline host hardening — SSH key-only access, password auth disabled, OS patched, no unneeded services/ports — comes before any Kubernetes-level control. Only after the hosts are secured does the k8s-specific layering matter: API access control, RBAC, NetworkPolicies, pod security.
**Tags:** k8s::cka src::session topic::architecture topic::security

---

<!-- note:1794496839384 model:Basic -->
**Front:** If a Pod is selected by at least one NetworkPolicy for ingress, what's the default behavior for ingress traffic?
**Back:** deny all ingress except what policies allow<br><br>Selection triggers default-deny for that direction, then allow rules apply. Pods selected by NO NetworkPolicy are fully open (allow-all); the moment ≥1 policy's podSelector matches, that direction flips to isolated and ONLY traffic matching the policy's ingress rules passes — everything else is dropped. Three nuances: isolation is per-direction (ingress selection leaves egress open unless a policy also lists egress); policies are additive — multiple selecting policies OR their rules together (union, not strictest-wins); and enforcement depends on the CNI plugin supporting NetworkPolicy — unsupported CNIs silently ignore policies, leaving the pod open.
**Tags:** k8s::cka src::session topic::networking topic::networkpolicy topic::security

---

<!-- note:1794496839388 model:Basic -->
**Front:** Which is a valid Ingress apiVersion/kind in modern Kubernetes?
**Back:** networking.k8s.io/v1 / Ingress<br><br>networking.k8s.io/v1 has been the stable Ingress API since Kubernetes 1.19 — extensions/v1beta1 and networking.k8s.io/v1beta1 were removed in 1.22. The v1beta1→v1 jump had real breaking changes: pathType became required on every path, backend.service.port.name was dropped (number only), and ingressClassName became a spec field. The 'something different' to know: the Ingress API is FROZEN — generally available but no longer developed, no new features. Kubernetes officially recommends the Gateway API (gateway.networking.k8s.io/v1, GA since Oct 2023, v1.4 Oct 2025) as its successor — same job (HTTP routing to Services), richer model: Gateway + GatewayClass + HTTPRoute objects instead of one Ingress.
**Tags:** k8s::cka src::session topic::ingress topic::networking

---

<!-- note:1794496839406 model:Basic -->
**Front:** What is the purpose of Kube Proxy in a Kubernetes cluster?
**Back:** enable connectivity between pods and services across different nodes in the cluster<br><br>kube-proxy runs on EVERY node (workers AND control plane — it's not a control-plane component) and implements Services at the node level: it watches Service and EndpointSlice objects through the API server and programs per-node packet rules — iptables, IPVS, nftables, or eBPF depending on proxy mode — that DNAT traffic destined for a ClusterIP to a ready pod IP, and that catch NodePort traffic arriving on the node. So 'pod → Service ClusterIP → some pod, possibly on another node' works transparently. It's not monitoring (that's kubelet probes/metrics-server), not object management (that's controllers), not storage. kube-proxy itself doesn't health-check pods — EndpointSlices only contain ready endpoints, maintained by the endpointslice mirroring controller.
**Tags:** k8s::cka src::session topic::networking topic::services

---

<!-- note:1794496839409 model:Basic -->
**Front:** Which of the following solutions support Kubernetes network policies?<br><br>A. Flannel, weave-net, and kube-proxy<br>B. Calico, weave-net, and flannel<br>C. Kube router, calico, and flannel<br>D. Kube router, calico, and weave-net
**Back:** D – kube-router, calico, and weave-net<br><br>NetworkPolicy is just an API — the CNI plugin must actually ENFORCE it, so support is entirely CNI-dependent. Calico, weave-net and kube-router all ship NetworkPolicy controllers (kube-router even has an official Kubernetes docs page for it; Cilium and Antrea do too). Flannel is the classic 'no' — flanneld only does overlay networking/routing and is policy-unaware (newer flannel charts can bundle a separate policy controller, but that's an add-on, not flannel itself). kube-proxy isn't a CNI at all — it programs Service ClusterIP/NodePort rules on each node; it has nothing to do with pod ingress/egress policy.
**Tags:** k8s::cka src::session topic::cni topic::networking topic::networkpolicy

---

<!-- note:1794496839410 model:Basic -->
**Front:** If you have only the ingress in the policyTypes, what does it mean?
**Back:** only the ingress traffic is isolated, and all egress traffic is unaffected<br><br>policyTypes declares which traffic DIRECTIONS the policy governs. Listing only Ingress means: selected pods get default-deny on inbound traffic, then the policy's ingress rules carve out exceptions — while egress is completely untouched, pods can still initiate any outbound connection. policyTypes: [Egress] does the reverse. The subtle default: if you OMIT policyTypes, Kubernetes infers it — an ingress: rules section implies Ingress, an egress: section implies Egress; and a policy with podSelector but NO rule lists at all defaults to BOTH directions (full isolation). Also note: NetworkPolicy never filters traffic to/from the node itself (hostNetwork/kubelet traffic is exempt).
**Tags:** k8s::cka src::session topic::networking topic::networkpolicy topic::yaml

---

<!-- note:1794496839465 model:Basic -->
**Front:** Which apiVersion/kind defines a Kubernetes NetworkPolicy?
**Back:** apiVersion: networking.k8s.io/v1, kind: NetworkPolicy<br><br>NetworkPolicy lives in the networking.k8s.io API group at v1: apiVersion: networking.k8s.io/v1, kind: NetworkPolicy — namespaced, so metadata.namespace matters (a policy only selects pods in its own namespace). Mandatory fields beyond the usual apiVersion/kind/metadata: spec.podSelector (which pods it applies to — empty {} selects ALL pods in the namespace), spec.policyTypes (Ingress/Egress/both), and spec.ingress/spec.egress rule lists. Without a CNI that enforces NetworkPolicy, the object is accepted but does NOTHING.
**Tags:** k8s::cka src::session topic::networking topic::networkpolicy topic::yaml

---

<!-- note:1794496839466 model:Basic -->
**Front:** For a connection from pod A to pod B to be allowed by NetworkPolicies, what must be true?
**Back:** BOTH — the source pod's egress policy AND the destination pod's ingress policy must allow it<br><br>A NetworkPolicy connection requires consent from BOTH ends: the source pod's egress rules must allow the destination, AND the destination pod's ingress rules must allow the source. If either side doesn't permit it, the connection never happens — you can't open egress on the client and expect it to reach an isolated server. This is why 'default deny ingress' on a backend forces you to also think about what clients are allowed to initiate.
**Tags:** k8s::cka src::session topic::networking topic::networkpolicy

---

<!-- note:1794496839469 model:Basic -->
**Front:** Which statements about Kubernetes NetworkPolicy behavior are true? (Select all that apply)<br><br>A. When multiple policies select the same pod, their allowed rules combine additively<br>B. Both the source's egress and the destination's ingress must allow a connection<br>C. Reply traffic for allowed connections is implicitly permitted<br>D. Policies are evaluated in creation order — first match wins<br>E. Traffic between a pod and its own node is always allowed
**Back:** A, B, C, E – policies union additively; both ends must allow; reply traffic is implicit; node traffic always allowed<br><br>(Select all that apply) NetworkPolicies never conflict — when several select the same pod+direction, the allowed connections are the UNION of all their rules; evaluation order is irrelevant. Both ends of a connection must permit it (source egress + dest ingress). Reply traffic for allowed connections is implicitly permitted — you don't write return-path rules. Edge cases: a pod can't block traffic to itself, and traffic to/from the pod's own node is always allowed regardless of policy.
**Tags:** k8s::cka src::session topic::networking topic::networkpolicy

---

<!-- note:1794496839474 model:Basic -->
**Front:** What is TCP 10256 for?
**Back:** TCP 10256 — kube-proxy's healthz/metrics endpoint, used by itself and load balancers<br><br>kube-proxy opens TCP 10256 inbound — it's NOT the port that carries Service traffic (that's whatever NodePort/hostPort the Service uses); 10256 is kube-proxy's own health/metrics endpoint so load balancers and monitoring can check whether the proxy is alive on each node. If you health-check kube-proxy through an LB or scrape its metrics, this is the port to allow.
**Tags:** k8s::cka src::session topic::networking topic::services

---

<!-- note:1794496839475 model:Basic -->
**Front:** Which port range must be open on worker nodes for NodePort Services?
**Back:** TCP and UDP 30000-32767 — the default NodePort range, open on every worker node<br><br>NodePort Services get a port in the default range 30000-32767 on EVERY node — both TCP and UDP are listed because the Service protocol decides which. kube-proxy on each node catches traffic arriving at nodeIP:nodePort and forwards it to a ready pod. The range is customizable (--service-node-port-range on the API server) — if you change it, open the NEW range instead. This is why NodePort is 'expose on all nodes': any node's IP works as an entry point.
**Tags:** k8s::cka src::session topic::networking topic::services

---

<!-- note:1794496839476 model:Basic -->
**Front:** Can the default component ports be changed?
**Back:** All of them are defaults — e.g. API server is often moved behind a 443 load balancer<br><br>Every port in the table is a default, not fixed: --secure-port on kube-apiserver, --etcd-servers for etcd placement, kubelet's --port, kube-proxy's --healthz-port/metrics-port, and --service-node-port-range for NodePort. The classic pattern: keep the API server on 6443 internally but front it with a load balancer listening on 443 that routes to it — external clients hit 443, internal traffic stays on 6443.
**Tags:** k8s::cka src::session topic::control-plane topic::networking

---

<!-- note:1794496839477 model:Basic -->
**Front:** What network prerequisites must every node in a Kubernetes cluster satisfy?
**Back:** Each node needs ≥1 networked interface with an IP, a unique hostname, a unique MAC, and the documented ports open<br><br>Cluster networking prerequisites per node: at least one interface connected to a network, each interface has an IP address, and the host has a unique hostname and unique MAC address — pod networking overlays (VXLAN etc.) and kubelet identity assume no two nodes look alike at L2. On top of that, the firewall must allow the documented component ports (6443, 2379-2380, 10250, 10256, 10257, 10259, NodePort range). Break any of these and you get subtle failures: duplicate hostnames confuse node identity, missing ports show up as probe/metrics timeouts.
**Tags:** k8s::cka src::session topic::cluster-setup topic::networking

---

<!-- note:1794496839478 model:Basic -->
**Front:** How can a pod within a Kubernetes cluster reach a service?
**Back:** By using the service name<br><br>A pod reaches a Service by connecting to its NAME (my-service or my-service.ns.svc.cluster.local) — the stable identifier you configure in the app. CoreDNS then resolves that name to the ClusterIP, and kube-proxy forwards ClusterIP traffic to a ready pod. Why not the others: the DNS record and DNS server are the RESOLUTION MECHANISM that makes the name work — they describe how the name is looked up, not what the pod connects to (and resolv.conf already points at CoreDNS automatically). Pod IP bypasses the Service completely — no ClusterIP, no load balancing, and pod IPs are ephemeral. Name vs IP is the real distinction: stable vs unstable.
**Tags:** k8s::cka src::session topic::dns topic::networking topic::services

---

<!-- note:1794496839479 model:Basic -->
**Front:** When would you set ipMasquerade/ipMasq to false in a CNI configuration? (Select all that apply)<br><br>A. Pod CIDRs are routable outside the cluster and you need end-to-end pod addressing<br>B. External systems must see real pod source IPs for whitelists or audit<br>C. Pods never need external connectivity — internal-only or air-gapped<br>D. Pods need outbound internet access
**Back:** A, B, C – routable pod CIDR / source-IP preservation / internal-only clusters<br><br>(Select all that apply) Masquerade trades source-IP fidelity for reachability — disable it (ipMasq/ipMasquerade/natOutgoing=false) when: pod CIDRs are externally routable and you want end-to-end pod addressing (routed/BGP networks); external systems must see REAL pod source IPs for whitelisting or audit (masquerade hides every pod behind its node's IP); or pods never need external connectivity (air-gapped/internal-only) so NAT is pure overhead. NOT a reason: pods needing internet access — that's exactly when masquerade must stay ON.
**Tags:** k8s::cka src::session topic::cni topic::networking

---

<!-- note:1794496839481 model:Basic -->
**Front:** How are Kubernetes clusters categorized by IP family?
**Back:** IPv4-only, IPv6-only, or dual-stack — and all components must agree on the primary IP family<br><br>Clusters are categorized by configured IP families: IPv4-only, IPv6-only, or dual-stack (IPv4/IPv6 or IPv6/IPv4). For dual-stack ALL components must agree — network plugin assigns both families to pods, kube-apiserver assigns both to services, kubelet/CCM assigns node IPs, and they must agree on which family is PRIMARY. Only IPs in pod.status.ips/node.status.addresses count for the model — extra interface IPs are ignored.
**Tags:** k8s::cka src::session topic::cluster-setup topic::networking

---

<!-- note:1794496839484 model:Basic -->
**Front:** A developer needs to expose a web application running in a set of Pods within the cluster using a stable internal IP address. Which Kubernetes resource <b>is most</b> appropriate?
**Back:** ClusterIP Service<br><br>A ClusterIP Service provides a stable internal IP address<br>and DNS name for accessing Pods, only reachable from within the cluster.<br>NodePort exposes on nodes, Ingress is for external HTTP/S.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839490 model:Basic -->
**Front:** What is the function of a NetworkPolicy in Kubernetes?
**Back:** To define how Pods are allowed to communicate with each other<br><br>NetworkPolicy resources specify how groups of Pods are<br>allowed to communicate with each other and other network endpoints,<br>acting as a firewall at the Pod level.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839496 model:Basic -->
**Front:** What is <b>the primary function</b> of kube-proxy when a Service of type ClusterIP is created?
**Back:** It modifies iptables or IPVS rules on nodes to route traffic.<br><br>kube-proxy watches the API server for new Services and<br>Endpoints. For ClusterIP Services, it configures network rules (e.g., iptables, IPVS) on each node to capture traffic destined for the Service’s IP<br>and load balance it to the backend Pods.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839500 model:Basic -->
**Front:** What is the role of an "Ingress Controller" in a Kubernetes cluster?
**Back:** It implements the rules defined in Ingress resources.<br><br>An Ingress resource defines HTTP/S routing rules, but an<br>Ingress Controller (e.g., Nginx, Traefik) is the actual reverse proxy/load<br>balancer that reads these rules and routes external traffic accordingly.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839508 model:Basic -->
**Front:** What Kubernetes object provides a stable IP address and DNS name for accessing a set of Pods?
**Back:** Service<br><br>A Service defines a logical set of Pods and a policy by which to access them, providing load balancing and service discovery.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839510 model:Basic -->
**Front:** Which Kubernetes object defines rules about how Pods are allowed to communicate with each other and network endpoints?
**Back:** NetworkPolicy<br><br>NetworkPolicies allow specifying traffic flow rules at the IP address or port level (OSI layer 3 or 4).
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839515 model:Basic -->
**Front:** Which Kubernetes API object is used to manage external access to services in a cluster, typically HTTP/S?
**Back:** Ingress<br><br>Ingress provides HTTP/S routing rules to manage external users’ access to services within the cluster based on hostnames or paths.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839530 model:Basic -->
**Front:** Which API object represents a single point of access to a set of Pods providing the same functionality, acting as an internal load balancer?
**Back:** Service<br><br>A Service defines a logical set of Pods (usually selected by labels) and provides a stable IP address and DNS name. kube-proxy ensures traffic to the Service IP is load-balanced across the healthy backend Pods.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839540 model:Basic -->
**Front:** What part of the Kubernetes system is responsible for managing the lifecycle of EndpointSlice objects, which track Pod IPs for Services?
**Back:** endpointslice-controller (within kube-controller-manager)<br><br>The endpointslice-controller (part of kube-controller-manager) watches Services and their selector-matched Pods, creating and managing EndpointSlices to store the Pod IP addresses and port information efficiently. kube-proxy consumes this information.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839541 model:Basic -->
**Front:** Which component translates a Service’s virtual IP address into actual Pod IP addresses on each node?
**Back:** kube-proxy<br><br>kube-proxy, running on each node, watches Services and Endpoints/EndpointSlices. It programs network rules (e.g., iptables, IPVS) to intercept traffic destined for a Service’s ClusterIP and directs it to one of the healthy backend Pod IPs.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839553 model:Basic -->
**Front:** What Kubernetes resource is used to expose an application running on a set of pods as a network service
**Back:** Service<br><br>A Service provides a stable network endpoint and load-balancing for accessing a group of Pods.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839555 model:Basic -->
**Front:** Which component of a Kubernetes node <b>is responsible for</b> managing network rules and IP addresses?
**Back:** Kube-proxy<br><br>Kube-proxy manages networking rules and enables service-to-pod communication within the cluster.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839562 model:Basic -->
**Front:** Which resource exposes services to external traffic?
**Back:** Ingress<br><br>Ingress manages external HTTP/HTTPS access to services.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839564 model:Basic -->
**Front:** A user reports that a web application is not accessible via its Service. The Service is of type ClusterIP. Which TWO steps should be taken to troubleshoot?
**Back:** verify kube-proxy is running on the node AND check the Service has endpoints via kubectl get endpoints<br><br>(Select TWO) ClusterIP traffic flows: client -> ClusterIP -> kube-proxy iptables/IPVS rules -> ready Pod IPs. Two failure points to check first: (A) kube-proxy down on the node = no DNAT rules programmed, ClusterIP goes nowhere; (D) empty endpoints = the Service selector matches no READY pods — the most common cause (pods crashed, labels changed, readiness failing). Distractors: container runtime failure breaks pods broadly, not Service-specific; kube-apiserver down breaks kubectl itself; restarting all nodes is disruptive non-diagnostic.
**Tags:** k8s::cka topic::services topic::endpoints src::session

---

<!-- note:1794496839565 model:Basic -->
**Front:** kubectl get endpoints <service-name> shows no addresses for a ClusterIP Service. What is the most likely cause?
**Back:** The selector matches no ready pods — Endpoints only lists pods that are Running AND Ready<br><br>The Endpoints object is auto-populated by the control plane with the IPs of pods matching the Service's selector that are Ready. Empty endpoints = kube-proxy has nothing to DNAT to, so the ClusterIP accepts nothing. Causes: selector/label mismatch, pods CrashLoopBackOff, readiness probe failing, or pods in wrong namespace. Inspect with 'kubectl get endpoints <svc>' or 'kubectl describe svc <svc>' (shows Endpoints: field). Note: modern clusters use EndpointSlices internally, but 'kubectl get endpoints' still works.
**Tags:** k8s::cka topic::services topic::endpoints src::session

---

<!-- note:1794496839654 model:Basic -->
**Front:** What does the "ipMasquerade" field in a Container Network Interface (CNI) plugin configuration file determine?
**Back:** Whether a NAT rule should be added for IP masquerading<br><br>ipMasquerade (written ipMasq in the bridge plugin) is the on/off switch telling the CNI plugin to program iptables NAT MASQUERADE rules: pod traffic leaving the node gets its source IP rewritten to the node's IP — SNAT, same trick as a home router. It's needed because pod CIDR addresses (10.x) aren't routable outside the cluster — without masquerade, pod→internet egress has no return path. The field CONFIGURES masquerading; it doesn't validate the config file (schema does that), assign the bridge IP (that's ipam/isGateway), or declare plugin capability (capability is fixed — this is the per-config toggle).
**Tags:** k8s::cka src::session topic::cni topic::networking

---

<!-- note:1794496839655 model:Basic -->
**Front:** What does the "isGateway" field in a Container Network Interface (CNI) plugin configuration file determine?
**Back:** Whether the bridge network should act as a gateway<br><br>isGateway (default false) tells the bridge plugin to assign the bridge the IPAM-provided gateway IP — turning the bridge into the containers' gateway so pod traffic can route out of the pod network. Without it the bridge is pure L2 (container-to-container on the host only, no routing). Getting an IP is the mechanism; acting as gateway is the purpose — pods' default route points at the bridge IP. Sibling field isDefaultGateway additionally makes that IP the containers' default route. Like ipMasq, it CONFIGURES behavior — doesn't validate the file or declare plugin capability.
**Tags:** k8s::cka src::session topic::cni topic::networking

---

<!-- note:1794496839656 model:Basic -->
**Front:** In a CNI plugin configuration file, what does the "type" field indicate when set to "host-local" under the IPAM section?
**Back:** The type of IP address management used for pods<br><br>ipam.type selects WHICH IPAM plugin allocates pod IPs: host-local = file-based allocation on each node from its podCIDR slice (the standard choice — no central allocator needed); dhcp delegates to an external DHCP server; static uses fixed IPs; whereabouts coordinates a shared pool across nodes. Watch the nesting: the TOP-LEVEL type field picks the main plugin (bridge, vlan…), while ipam.type picks only the address allocator — two different 'type' fields at different levels of the same JSON.
**Tags:** k8s::cka src::session topic::cni topic::networking

---

<!-- note:1794496839659 model:Basic -->
**Front:** What do --cni-conf-dir and --cni-bin-dir point at?
**Back:** kubelet --cni-conf-dir=/etc/cni/net.d holds the .conflist configs; --cni-bin-dir=/opt/cni/bin holds the plugin executables<br><br>Two kubelet flags wire CNI in: --cni-conf-dir (default /etc/cni/net.d) contains the network CONFIG files — JSON .conflist files naming which plugins/IPAM to use (this is where 'bridge', 'host-local' etc. get selected); --cni-bin-dir (default /opt/cni/bin) contains the plugin EXECUTABLES the configs point at. Flow: kubelet reads the conflist → picks plugin name → runtime executes that binary from bin-dir with ADD + the container's ID/netns. Wrong dir or missing binary = pods stuck in ContainerCreating.
**Tags:** k8s::cka src::session topic::cni topic::kubelet topic::networking

---

<!-- note:1794496839660 model:Basic -->
**Front:** What are the top-level keys of a CNI .conflist network configuration?
**Back:** cniVersion/cniVersions, name, and plugins[] — bridge/ipam/dns live INSIDE each plugin object<br><br>A .conflist network config is a JSON object with top-level keys: cniVersion (spec version string like "1.1.0") or cniVersions (list of supported versions), name (unique network name per host), and plugins — an array of plugin config objects. Fields like type, bridge, ipam, dns, capabilities are PER-PLUGIN, nested inside each plugins[] entry — not top-level. Think of it as: envelope (version+name) → list of plugin instructions.
**Tags:** k8s::cka src::session topic::cni topic::networking topic::yaml

---

<!-- note:1794496839661 model:Basic -->
**Front:** In a CNI plugin config, what does the "type" field specify?
**Back:** The filename of the plugin executable in the CNI bin dir — type: bridge → /opt/cni/bin/bridge<br><br>Each plugin object's "type" field names the plugin BINARY on disk — it's how the config points at the executable: type: "bridge" makes the runtime look for /opt/cni/bin/bridge. This is the exact mechanism from your lecture: config in net.d identifies the script name, runtime finds that binary in the bin dir and executes it with ADD/DEL. Same for ipam.type — it names the IPAM plugin's executable, not a behavior.
**Tags:** k8s::cka src::session topic::cni topic::networking

---

<!-- note:1794496839662 model:Basic -->
**Front:** What does the plugins[] array in a .conflist enable?
**Back:** Multiple plugins can be chained — a main plugin (bridge) plus meta plugins (tuning, portmap, firewall) that adjust the result<br><br>The plugins[] array enables CHAINING: the runtime executes each plugin in order, passing each one's result (prevResult) to the next. Typically the first entry is the 'interface' plugin that creates the interface+IP (bridge), followed by 'meta' plugins that modify the already-created interface — tuning (sysctl, MAC), portmap (hostPort mapping), firewall, bandwidth. Spec v0.3.0 introduced chaining; v1.0.0 then REQUIRED the plugins array even for a single plugin.
**Tags:** k8s::cka src::session topic::cni topic::networking

---

<!-- note:1794496839663 model:Basic -->
**Front:** Since CNI spec v1.0.0, can a network config omit the plugins[] array for a single plugin?
**Back:** No — spec v1.0.0 removed non-list configs; every network config must use the plugins[] array<br><br>Spec history that matters: v0.3.0 added plugin chaining + rich results; v0.4.0 added CHECK; v1.0.0 REMOVED non-list configurations — a bare single-plugin JSON without plugins[] is invalid in modern CNI; v1.1.0 added STATUS and GC commands plus cniVersions for multi-version support. So even a one-plugin network must be wrapped: {"cniVersion":"1.0.0","name":"x","plugins":[{"type":"bridge",...}]}. The cniVersions list field lets one config declare which spec versions it supports.
**Tags:** k8s::cka src::session topic::cni topic::networking

---

<!-- note:1794496839664 model:Basic -->
**Front:** What parameters does the container runtime pass to CNI plugins? (Select all that apply)<br><br>A. CNI_CONTAINERID — the unique container identifier<br>B. CNI_NETNS — path to the container's network namespace<br>C. CNI_IFNAME — the interface name to create in the container<br>D. CNI_PATH — the plugin binary search path
**Back:** A, B, C, D – CNI_CONTAINERID, CNI_NETNS, CNI_IFNAME, CNI_ARGS/CNI_PATH all passed by the runtime<br><br>(Select all that apply) The runtime passes per-attachment context to plugins via env vars/parameters: CNI_CONTAINERID (unique container ID), CNI_NETNS (path to the container's network namespace, e.g. /run/netns/...), CNI_IFNAME (interface name to create inside the container), CNI_ARGS (extra key-value args), and CNI_PATH (the plugin search path so plugins can find delegated binaries like IPAM). These are what the ADD/DEL calls carry — the 'name and namespaceID' your lecture mentioned.
**Tags:** k8s::cka src::session topic::cni topic::networking

---

<!-- note:1794496839665 model:Basic -->
**Front:** Which lifecycle rules does the CNI spec mandate? (Select all that apply)<br><br>A. The runtime creates the network namespace before invoking plugins and cleans it up itself<br>B. Every ADD must eventually be followed by a DEL — even if the ADD failed<br>C. The network config must not change between ADD and DEL<br>D. Plugins create and destroy the network namespace themselves
**Back:** A, B, C – runtime creates netns first; add must be followed by delete; delete runs even if add fails; runtime owns netns cleanup<br><br>(Select all that apply) Spec-mandated lifecycle: the runtime creates the container's network namespace BEFORE invoking any plugin and is responsible for cleaning it up afterward; every ADD must eventually be followed by a DEL (even if ADD failed); DEL may be retried; config must not change between add and delete; runtimes may parallelize across containers but not for the same container; GC operations must not overlap with add/delete.
**Tags:** k8s::cka src::session topic::cni topic::networking

---

<!-- note:1794496839667 model:Basic -->
**Front:** What is the fundamental reason Kubernetes uses Pods as the smallest deployable unit, rather than individual containers directly?
**Back:** To enable co-location and shared resources for containers<br><br>Pods allow tightly coupled containers to share resources<br>like network namespace (IP, port space) and storage volumes, facilitating<br>communication and data sharing for helper or sidecar patterns.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839677 model:Basic -->
**Front:** What is the role of a CNI (Container Network Interface) plugin in Kubernetes?
**Back:** Providing container networking<br><br>Explanation: CNI plugins are responsible for configuring network interfaces for containers and managing IP address allocation within the cluster.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839690 model:Basic -->
**Front:** Which networking model does Kubernetes use?
**Back:** Flat networking<br><br>Kubernetes uses a flat network model where all Pods can communicate without NAT.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839715 model:Basic (and reversed card) -->
**Front:** What is the pod network CIDR in Kubernetes, and what is it separate from?
**Back:** The internal virtual IP range reserved for pod IPs across the whole cluster — the CIDR the pod network draws addresses from (e.g. 10.244.0.0/16 for default Flannel). It's separate from the Service CIDR (ClusterIP range, e.g. 10.96.0.0/12), which is for stable Service IPs, not pods.
**Tags:** k8s::cka topic::networking topic::services src::session

---

<!-- note:1794496839716 model:Basic (and reversed card) -->
**Front:** What is CNI in Kubernetes?
**Back:** Container Network Interface — the plugin standard Kubernetes uses (via the container runtime) to wire pods into the network. CNI plugins like Calico, Flannel or Cilium assign pod IPs (IPAM) and build the virtual/overlay network that connects all pods across all nodes — they implement the pod network the k8s model requires; many also enforce NetworkPolicy.
**Tags:** k8s::cka topic::cni topic::networking src::session

---

<!-- note:1794496839720 model:Basic (and reversed card) -->
**Front:** What does the ClusterIP Service type do?
**Back:** The default Service type — assigns a stable virtual IP reachable only INSIDE the cluster (from the Service CIDR, e.g. 10.96.0.0/12). Use it for internal microservice-to-microservice communication; outside access would need Ingress/Gateway or a different type.
**Tags:** k8s::cka topic::networking topic::services src::session

---

<!-- note:1794496839721 model:Basic (and reversed card) -->
**Front:** What does the NodePort Service type do?
**Back:** Builds on ClusterIP — additionally opens the same static port (the nodePort, 30000-32767 by default) on EVERY node's IP. External traffic to <code>&lt;any-node-IP&gt;:&lt;nodePort&gt;</code> is forwarded to the Service and on to a ready pod. It's the simplest built-in way to expose an app outside the cluster.
**Tags:** k8s::cka topic::networking topic::services src::session

---

<!-- note:1794496839722 model:Basic (and reversed card) -->
**Front:** What does the LoadBalancer Service type do?
**Back:** Builds on NodePort+ClusterIP — asks the environment (cloud provider integration, or MetalLB on bare-metal) for an external load balancer with a public IP. Traffic flows: external client → cloud LB → node's nodePort → Service → pod. It's the standard way to get a real public IP per service; without LB support the Service stays pending.
**Tags:** k8s::cka topic::networking topic::services src::session

---

<!-- note:1794496839723 model:Basic (and reversed card) -->
**Front:** What happens if you omit <code>spec.type</code> in a Service manifest?
**Back:** ClusterIP — it's the default: omitting <code>spec.type</code> is equivalent to <code>type: ClusterIP</code>. The Service gets a stable cluster-internal virtual IP (auto-assigned from the Service CIDR, shown in <code>.spec.clusterIP</code>) reachable only inside the cluster.
**Tags:** k8s::cka topic::networking topic::services topic::yaml src::session

---

<!-- note:1794496839724 model:Basic (and reversed card) -->
**Front:** A LoadBalancer Service's EXTERNAL-IP stays &lt;pending&gt;. What does that mean?
**Back:** No load balancer implementation has provisioned one. Kubernetes doesn't include a built-in external LB — <code>type: LoadBalancer</code> only resolves to a real public IP where a supported cloud provider integration exists, or where a tool like MetalLB or Cilium LB IPAM is configured to supply one. On an unsupported cluster the Service works internally (clusterIP+nodePort) but never gets an external address.
**Tags:** k8s::cka topic::networking topic::services src::session

---

<!-- note:1794496839730 model:Basic (and reversed card) -->
**Front:** In Service DNS names like <code>api.prod.svc.cluster.local</code>, what is the final domain component?
**Back:** <code>cluster.local</code> — it completes the Service FQDN <code>&lt;svc&gt;.&lt;ns&gt;.svc.cluster.local</code>. It's the cluster's default DNS domain (the 'base domain' CoreDNS serves); kubelet hands it to pods via <code>clusterDomain</code>/resolv.conf. Custom clusters can change it, but stock installs use cluster.local.
**Tags:** k8s::cka src::session topic::dns topic::namespaces

---

<!-- note:1794496839751 model:Cloze -->
**Text:** The Kubernetes network model:<br><br>Every pod gets its own {{c1::cluster-wide IP address}}.<br>All pods can talk to all pods on any node {{c2::without NAT}}.<br>Nodes can talk to pods and vice versa {{c2::without NAT}}.<br>The pod network itself is built by {{c3::CNI}} plugins (e.g. Calico, Flannel, Cilium).
**Back Extra:** These are the guarantees the pod network must provide — no NAT between pods on any node. The CNI plugin (Calico/Flannel/Cilium) is what builds that network: assigns IPs and routes/encapsulates traffic across nodes.
**Tags:** k8s::cka topic::cni topic::networking src::session

---

<!-- note:1794496839754 model:Cloze -->
**Text:** Service manifest (NodePort):<br><br><code>apiVersion: {{c1::v1}}<br>kind: {{c2::Service}}<br>metadata:<br>&nbsp;&nbsp;name: web-svc<br>spec:<br>&nbsp;&nbsp;type: {{c3::NodePort}}<br>&nbsp;&nbsp;{{c4::selector}}:<br>&nbsp;&nbsp;&nbsp;&nbsp;app: web<br>&nbsp;&nbsp;ports:<br>&nbsp;&nbsp;- port: 80<br>&nbsp;&nbsp;&nbsp;&nbsp;{{c5::targetPort}}: 8080<br>&nbsp;&nbsp;&nbsp;&nbsp;{{c6::nodePort}}: 30080</code>
**Back Extra:** apiVersion: v1 — Service lives in the core API group. selector must match pod labels (that's how the Service finds backends). targetPort is the port ON the pods; nodePort is only needed for type NodePort — omit it and the control plane auto-allocates from 30000-32767.
**Tags:** k8s::cka topic::networking topic::services topic::yaml src::session

---

<!-- note:1794496839755 model:Cloze -->
**Text:** A Service named <code>backend</code> in namespace <code>web</code> gets the DNS record<br><br><code>{{c1::backend}}.{{c2::web}}.{{c3::svc}}.{{c4::cluster.local}}</code><br><br>which resolves to the Service's {{c5::clusterIP}}.
**Back Extra:** The clusterIP is auto-assigned from the service-cluster-ip-range CIDR (e.g. 10.96.0.0/12) and never changes for the Service's lifetime. Pods find it via the Service's DNS name (backend.web.svc.cluster.local) — they resolve the name, not the raw IP.
**Tags:** k8s::cka topic::dns topic::networking topic::services src::session

---

<!-- note:1794496839756 model:Cloze -->
**Text:** <code>$ kubectl get svc web-svc<br>NAME&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TYPE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CLUSTER-IP&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EXTERNAL-IP<br>web-svc&nbsp;&nbsp;&nbsp;{{c1::LoadBalancer}}&nbsp;&nbsp;&nbsp;10.96.1.5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{c2::&lt;pending&gt;}}</code><br><br>The {{c2}} EXTERNAL-IP means no load balancer implementation has provisioned an external IP yet.
**Back Extra:** The clusterIP was still assigned — the Service works inside the cluster and via nodePort even while pending. An external IP appears only when a cloud provider integration (or MetalLB/Cilium LB IPAM on-prem) provisions it; the provider writes it to .status.loadBalancer.ingress.
**Tags:** k8s::cka topic::kubectl topic::networking topic::services src::session

---

<!-- note:1794496839758 model:Cloze -->
**Text:** A Service named <code>backend</code> in namespace <code>prod</code> gets the in-cluster DNS name<br><br><code>{{c1::backend}}.{{c2::prod}}.{{c3::svc}}.{{c4::cluster.local}}</code><br><br>resolving to the Service's {{c5::clusterIP}}.
**Back Extra:** CoreDNS publishes &lt;service&gt;.&lt;namespace&gt;.svc.cluster.local for every Service; it resolves to the clusterIP. Inside the same namespace the short name (backend) is enough; from another namespace you need backend.&lt;ns&gt;.
**Tags:** k8s::cka src::session topic::dns topic::services

---

<!-- note:1794498397449 model:Basic -->
**Front:** What are the cluster DNS record formats for pods, services and nodes?
**Back:** CoreDNS serves cluster.local: Pods get <pod-ip-with-dashes>.<namespace>.pod.cluster.local (e.g. 10-244-0-5.default.pod.cluster.local); Services get <service>.<namespace>.svc.cluster.local — short form <service>.<namespace> also resolves via search domains; Nodes get <node-ip-with-dashes>.<namespace>.node.cluster.local. Pods' /etc/resolv.conf points nameserver at the kube-dns Service ClusterIP with search domains so 'myservice' resolves to myservice.default.svc.cluster.local.
**Tags:** k8s::cka src::course-kodekloud topic::coredns topic::networking

---

<!-- note:1794498397450 model:Basic -->
**Front:** How does the Gateway API relate to Ingress, and why is it in the current CKA curriculum?
**Back:** Gateway API is the successor-standard to Ingress: instead of one Ingress resource doing everything, it splits roles — GatewayClass (the implementation, e.g. 'istio'), Gateway (a listener/entrypoint instance), and routes like HTTPRoute/TCPRoute (L7/L4 traffic rules) — giving typed, role-based, more expressive traffic management that Ingress's single-resource model can't express. The 2025 CKA updates added 'Introduction to Gateway API'; the classic Ingress + annotations (nginx.ingress.kubernetes.io/rewrite-target etc.) remains exam content too. Know both: Ingress = single resource per host/path rules; Gateway API = Gateway + HTTPRoute separation.
**Tags:** k8s::cka src::course-kodekloud topic::gateway-api topic::networking

---

<!-- note:1794506309318 model:Basic -->
**Front:** What are the parts of an Ingress resource and how does traffic reach pods?
**Back:** Ingress (networking.k8s.io/v1) declares HTTP routing rules; an INGRESS CONTROLLER (nginx, traefik, ALB) watches them and programs the actual load balancer. Structure: <code>spec.rules[].host</code> (hostname, empty = all hosts) → <code>http.paths[]</code> with <code>path</code> + <code>pathType</code> + <code>backend.service</code> (name+port) pointing at a Service — the Service's endpoints then reach pods. Ingress itself creates NO pods or IPs — without a controller installed, the Ingress object exists but nothing routes traffic.
**Tags:** k8s::cka topic::ingress topic::networking src::course-kodekloud

---

<!-- note:1794506309319 model:Basic -->
**Front:** What are the three Ingress pathType values and when does each match?
**Back:** <b>Exact</b> — matches the path character-for-character, nothing else. <b>Prefix</b> — matches on a path ELEMENT boundary (split by /): /foo matches /foo and /foo/bar but NOT /foobar. <b>ImplementationSpecific</b> — matching is up to the Ingress controller (nginx treats it like Prefix-ish regex-ish behavior; used for custom matching). Most exam examples use Prefix; Exact for single endpoints, ImplementationSpecific when you need controller-specific features.
**Tags:** k8s::cka topic::ingress topic::networking src::course-kodekloud

---

<!-- note:1794506309320 model:Basic -->
**Front:** How does IngressClass control which controller serves an Ingress?
**Back:** IngressClass (networking.k8s.io/v1) names a controller implementation via spec.controller (e.g. k8s.io/ingress-nginx). An Ingress sets <code>spec.ingressClassName: nginx</code> to bind to that class; if omitted, the cluster's default IngressClass (annotation ingressclass.kubernetes.io/is-default-class) applies. Multiple controllers can coexist — routes go only to the controller whose class the Ingress names. Check installed classes: <code>kubectl get ingressclass</code>.
**Tags:** k8s::cka topic::ingress topic::networking src::course-kodekloud

---
