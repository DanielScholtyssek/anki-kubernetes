# KCNA - Kubernetes and Cloud Native Associate — Cloud Native Architecture

> Deck: `KCNA - Kubernetes and Cloud Native Associate` · Group: `Cloud Native Architecture` · Notes: 22 · Models: Basic++, Basic+++

<!-- note:1755880202648 model:Basic++ -->
**Front:** Why is container orchestration essential for managing microservices at scale?<br><br>A. It simplifies writing microservice code
<br>B. It automatically converts monolithic apps to microservices
<br>C. It handles service discovery, scaling, and fault tolerance
<br>D. It provides a centralized logging solution by default
<br>E. It guarantees zero-downtime deployments
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: Orchestrators like Kubernetes automate complex tasks
like service discovery, load balancing, scaling based on demand, and selfhealing, which are crucial for managing a distributed microservices architecture.

---

<!-- note:1755880537022 model:Basic++ -->
**Front:** What fundamental problem does a <b>Service Mesh</b> like <b>Istio </b>or
<b>Linkerd </b>aim to solve in a microservices architecture?
<br><br>A. Simplifying container image building
<br>B. Automating infrastructure provisioning
<br>C. Managing and observing inter-service communication
<br>D. Providing persistent storage for stateful applications
<br>E. Abstracting server management
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: Service meshes provide a dedicated infrastructure layer for
handling service-to-service communication, offering features 1 like traffic
management, security (mTLS), and observability (metrics, traces) without
requiring changes to application code.

---

<!-- note:1755880758526 model:Basic++ -->
**Front:** How does Serverless (e.g., FaaS like AWS Lambda or Knative
Serving) <b>primarily </b>differ from traditional PaaS offerings?<br><br>A. Serverless does not use containers
<br>B. Serverless applications cannot be stateful
<br>C. Serverless abstracts away all underlying server management
<br>D. PaaS does not offer auto-scaling capabilities
<br>E. Serverless is only for event-driven functions
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: Serverless computing (especially FaaS) aims to abstract
away all infrastructure management, including servers, OS, and runtimes,
allowing developers to focus solely on writing code that executes in response to events.

---

<!-- note:1755880801919 model:Basic++ -->
**Front:** What is <b>the primary role</b> of the Cloud Native Computing Foundation (CNCF) in the Kubernetes ecosystem?<br><br>A. To directly employ Kubernetes core developers
<br>B. To sell Kubernetes enterprise support subscriptions
<br>C. To foster and sustain an ecosystem of open source projects
<br>D. To define mandatory cloud provider APIs
<br>E. To own the intellectual property of Linux
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: The CNCF hosts and promotes a wide range of open source
projects (including Kubernetes, Prometheus, Envoy) to advance cloud native computing, providing governance, support, and community building.

---

<!-- note:1755880861102 model:Basic++ -->
**Front:** In a typical cloud native environment, which persona<b> is most
concerned with</b> ensuring application uptime, performance, and
managing incident response?<br><br>A. Application Developer
<br>B. Platform Consumer
<br>C. Site Reliability Engineer (SRE) / Platform Operator
<br>D. Business Analyst
<br>E. End User
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: SREs and Platform Operators are responsible for the reliability, scalability, and overall operational health of the platform and the
applications running on it, including monitoring, alerting, and incident
management.

---

<!-- note:1755881877995 model:Basic++ -->
**Front:** Which of the following is NOT a core characteristic of cloud
native architectures?<div><br>A. Microservices
<br>B. Containers
<br>C. Monolithic application design
<br>D. DevOps practices
<br>E. Automation</div>
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: Cloud native architectures typically favor microservices,
containers, dynamic orchestration (like Kubernetes), and DevOps/Agile
practices, moving away from large, tightly coupled monolithic designs.

---

<!-- note:1755882478920 model:Basic++ -->
**Front:** What is a primary characteristic of Vertical Pod Autoscaling
(VPA)?&nbsp;<div><br></div><div>A. It adjusts the number of Pod replicas.
<br>B. It adjusts the CPU and memory requests and limits for Pods.
<br>C. It adds or removes Nodes from the cluster.
<br>D. It automatically selects the optimal storage class.
<br>E. It scales the number of available IP addresses.</div>
**Back:** Correct Answer: <b>B</b>
<br><br><b>Explanation</b>: VPA recommends or automatically updates the resource
requests and limits for containers within Pods to match actual usage,
helping to optimize resource allocation. It does not change the number of
replicas (that’s HPA).

---

<!-- note:1755882853962 model:Basic++ -->
**Front:** Which of these is a <b>primary </b>goal of the CNCF’s "Trail Map" for
cloud native adoption?
<br><br>A. To mandate specific vendor products for each stage.
<br>B. To provide a prescriptive path for building cloud native apps.
<br>C. To offer a recommended journey and project choices for adopters.
<br>D. To rank cloud providers based on their Kubernetes offerings.
<br>E. To certify individual developers as cloud native experts.
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: The CNCF Trail Map suggests a path for organizations
adopting cloud native technologies, highlighting CNCF projects that can
help at different stages (e.g., containerization, CI/CD, orchestration, observability).

---

<!-- note:1755882964773 model:Basic++ -->
**Front:** What is the <b>primary </b>motivation behind using ”Serverless Functions” (FaaS)?<div>&nbsp;
<br>A. To achieve higher compute density on physical servers.
<br>B. To run long-lived, stateful batch processing jobs.
<br>C. To execute event-driven code without managing infrastructure.&nbsp;<div>D. To gain fine-grained control over OS-level configurations.
<br>E. To build complex, monolithic application backends.</div></div>
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: Serverless functions are designed for short-lived, eventdriven computations where the underlying infrastructure (servers, OS) is
completely managed by the platform, allowing developers to focus on code.

---

<!-- note:1756920574395 model:Basic++ -->
**Front:** <div>What type of software package bundles application code with all its dependencies, libraries, and configuration files?</div><div><br></div><div>A. Virtual Machine</div><div>B. Container</div><div>C. Operating System</div><div>D. Serverless Function</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div><div><b>Explanation</b>: Containers package application code and dependencies together, isolating them from the underlying infrastructure.</div>

---

<!-- note:1756921658932 model:Basic++ -->
**Front:** <div>What is <b>the primary purpose</b> of a Service Mesh like Istio or Linkerd?</div><div><br></div><div>A. Container image building</div><div>B. Cluster storage management</div><div>C. Managing inter-service comms</div><div>D. Node provisioning</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: Service meshes add observability, security, and reliability features to communication between microservices (service-to-service).</div>

---

<!-- note:1756922958222 model:Basic++ -->
**Front:** <div>Which mechanism allows Kubernetes to automatically adjust the number of Pods in a Deployment based on CPU utilization or custom metrics?</div><div><br></div><div>A. Vertical Pod Autoscaler (VPA)</div><div>B. Cluster Autoscaler (CA)</div><div>C. Horizontal Pod Autoscaler (HPA)</div><div>D. Node Problem Detector (NPD)</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: The HPA automatically scales the number of Pod replicas based on observed metrics like CPU or memory usage.</div>

---

<!-- note:1756923052337 model:Basic++ -->
**Front:** <div>What term describes an architectural approach where applications are built as small, independent services that run in their own processes?</div><div><br></div><div>A. Monolithic</div><div>B. Microservices</div><div>C. Serverless</div><div>D. N-Tier</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div><div><b>Explanation</b>: Microservices architecture structures an application as a collection of loosely coupled, independently deployable services.</div>

---

<!-- note:1756923133935 model:Basic++ -->
**Front:** <div>What does ”Serverless” computing primarily abstract away from the developer?</div><div><br></div><div><div>A. Networking</div><div>B. Storage</div><div>C. Server Management</div><div>D. Operating System choice</div></div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: Serverless platforms (like FaaS) manage the underlying infrastructure, allowing developers to focus solely on code execution.</div>

---

<!-- note:1756923163328 model:Basic++ -->
**Front:** <div>Which organization hosts Kubernetes and promotes the growth of the cloud native ecosystem?</div><div><br></div><div>A. Linux Foundation (LF)</div><div>B. Apache Software Foundation (ASF)</div><div>C. Cloud Native Computing Foundation (CNCF)</div><div>D. Open Source Initiative (OSI)</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: The CNCF, part of the Linux Foundation, stewards Kubernetes and many other cloud native projects.</div>

---

<!-- note:1756923197607 model:Basic++ -->
**Front:** <div>What is the benefit of using open standards in cloud native technologies?</div><div><br></div><div>A. Vendor lock-in</div><div>B. Increased complexity</div><div>C. Interoperability Portability</div><div>D. Reduced security</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: Open standards (like OCI, CRI, CNI) ensure that different tools and platforms can work together, preventing vendor lock-in.</div>

---

<!-- note:1756923227133 model:Basic++ -->
**Front:** <div>In a typical cloud native environment, which persona is <b>primarily responsible</b> for designing and building the application?</div><div><br></div><div>A. Operator</div><div>B. Developer</div><div>C. Site Reliability Engineer (SRE)</div><div>D. Security Engineer</div>
**Back:** <div>Correct Answer: <b>B<br><br></b></div><div><b>Explanation</b>: Developers focus on writing, building, and testing the application code that runs within the cloud native platform.</div>

---

<!-- note:1756923272014 model:Basic++ -->
**Front:** <div>Which persona is typically focused on the reliability, scalability, and maintenance of the underlying Kubernetes platform?</div><div><br></div><div>A. End User</div><div><div>B. Application Developer</div><div>C. Platform Operator / SRE</div><div>D. Data Scientist</div></div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: Operators or SREs manage the Kubernetes cluster itself, ensuring it’s healthy, scalable, and available for developers.</div>

---

<!-- note:1767560194445 model:Basic+++ -->
**Front:** Which are key service mesh features? Select two answers<br><br><div>A. Load balancing and discovery<br> B. mTLS security<br> C. Image storage<br> D. CI/CD automation</div>
**Back:** <div>Correct Answers: <b>A</b> and<b> B</b></div><div><br></div>
<div><b>Explanation</b>: Service meshes handle traffic management and secure service-to-service communication.</div>

---

<!-- note:1767560833637 model:Basic+++ -->
**Front:** How do service meshes benefit microservices? <br><br><div>A. Network abstractions<br> B. Centralized logging<br> C. Remove containers<br> D. Auto-scale servers</div>
**Back:** <div>Correct Answer: <b>A</b></div><div><br></div> <div><b>Explanation</b>: They abstract networking concerns away from application code.</div>

---

<!-- note:1767561260722 model:Basic+++ -->
**Front:** What is a key serverless characteristic? <br><br><div>A. Manual scaling<br> B. Pay per execution time<br> C. Server management<br> D. Manual start/stop</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div> <div><b>Explanation</b>: Serverless charges based on actual compute usage.</div>

---

<!-- note:1767561281344 model:Basic+++ -->
**Front:** What does FaaS stand for? <br><br><div>A. Function as a Service<br> B. File as a Service<br> C. Fragmentation as a Service<br> D. Framework as a Service</div>
**Back:** <div>Correct Answer: <b>A</b></div><div><br></div> <div><b>Explanation</b>: FaaS allows execution of functions without managing servers.</div>

---

<!-- note:1794007966270 model:Many -->
**Domain:** Cluster Networking - apiserver port
**Question:** Which port does the Kubernetes API server listen on by default?
**Options:** A. TCP 6443<br>B. TCP 443<br>C. TCP 2379<br>D. TCP 10250
**Answer:** A (1) – TCP 6443 — the Kubernetes API server, the port EVERY component talks through
**Explanation:** kube-apiserver listens on TCP 6443 inbound by default — it's the single front door: kubelets, kube-proxy, controllers, scheduler, kubectl, and every Pod's ServiceAccount token all authenticate to it. In firewall-restricted environments (on-prem DCs, VPC security groups) 6443 is the one port that must be reachable by everything. It's a default, not a law — teams often put the API server behind a load balancer on 443 and route to 6443 internally.
**Sources:** <a href="https://kubernetes.io/docs/reference/networking/ports-and-protocols/" target="_blank">Kubernetes Docs - Ports and Protocols</a>
**Tags:** k8s::kcna topic::networking topic::control-plane src::session

---

<!-- note:1794007966271 model:Many -->
**Domain:** Cluster Networking - control plane ports
**Question:** Which ports must be open on control plane nodes? (Select all that apply)
**Options:** A. 6443 — kube-apiserver<br>B. 2379-2380 — etcd client API<br>C. 10257 — kube-controller-manager<br>D. 10259 — kube-scheduler<br>E. 10255 — kubelet read-only API
**Answer:** A, B, C, D – 6443 apiserver, 2379-2380 etcd, 10257 controller-manager, 10259 scheduler
**Explanation:** (Select all that apply) Control plane inbound TCP ports: 6443 kube-apiserver (all components), 2379-2380 etcd client API (apiserver↔etcd), 10257 kube-controller-manager (self only — its secure endpoint), 10259 kube-scheduler (self only). NOT on the list: 10255 is the long-deprecated kubelet read-only port, 10256 is kube-proxy (worker-side health endpoint), and 443 is only there if you override the API server port.
**Sources:** <a href="https://kubernetes.io/docs/reference/networking/ports-and-protocols/" target="_blank">Kubernetes Docs - Ports and Protocols</a>
**Tags:** k8s::kcna topic::networking topic::control-plane src::session

---

<!-- note:1794007966272 model:Many -->
**Domain:** Cluster Networking - etcd ports
**Question:** Which ports does etcd need open, and who talks to it?
**Options:** A. TCP 2379-2380 — etcd's client API range; 2379 for client traffic, 2380 for peer replication<br>B. TCP 6443-6444 — etcd mirrors the API server ports<br>C. TCP 10250 — etcd shares the kubelet port<br>D. UDP 2379 — etcd uses UDP for replication
**Answer:** A (1) – TCP 2379-2380 — etcd's client API range; 2379 for client traffic, 2380 for peer replication
**Explanation:** etcd listens on TCP 2379-2380 inbound: 2379 serves the client API (kube-apiserver is the client — it's the only regular consumer), 2380 handles peer-to-peer replication between etcd members. etcd stores ALL cluster state so these ports matter for quorum. The doc notes etcd can also run EXTERNAL to the control plane or on custom ports — then only the apiserver↔etcd path needs opening, not the whole range everywhere.
**Sources:** <a href="https://kubernetes.io/docs/reference/networking/ports-and-protocols/" target="_blank">Kubernetes Docs - Ports and Protocols</a>
**Tags:** k8s::kcna topic::networking topic::etcd topic::control-plane src::session

---

<!-- note:1794007966273 model:Many -->
**Domain:** Cluster Networking - kubelet port
**Question:** Which port does the kubelet serve its API on?
**Options:** A. TCP 10250 — the kubelet API: self plus the control plane (logs, exec, metrics, probes)<br>B. TCP 10257 — kubelets share the controller-manager port<br>C. TCP 4194 — the kubelet's flannel VXLAN port<br>D. TCP 6782-6784 — kubelet metrics ports
**Answer:** A (1) – TCP 10250 — the kubelet API: self plus the control plane (logs, exec, metrics, probes)
**Explanation:** kubelet serves its API on TCP 10250 inbound — used by the kubelet itself AND the control plane, which reaches in for kubectl logs/exec, metrics scraping, and probe results. On worker nodes this is THE port that must be open to the control plane subnet. (Historical note: 10255 was the old read-only kubelet port — deprecated and gone from the docs because it leaked pod specs without auth.)
**Sources:** <a href="https://kubernetes.io/docs/reference/networking/ports-and-protocols/" target="_blank">Kubernetes Docs - Ports and Protocols</a>
**Tags:** k8s::kcna topic::networking topic::kubelet src::session

---

<!-- note:1794007966274 model:Many -->
**Domain:** Cluster Networking - kube-proxy port
**Question:** What is TCP 10256 for?
**Options:** A. TCP 10256 — kube-proxy's healthz/metrics endpoint, used by itself and load balancers<br>B. TCP 10250 — kube-proxy shares the kubelet port<br>C. TCP 30000-32767 — kube-proxy's own management range<br>D. UDP 10256 — kube-proxy uses UDP for service traffic
**Answer:** A (1) – TCP 10256 — kube-proxy's healthz/metrics endpoint, used by itself and load balancers
**Explanation:** kube-proxy opens TCP 10256 inbound — it's NOT the port that carries Service traffic (that's whatever NodePort/hostPort the Service uses); 10256 is kube-proxy's own health/metrics endpoint so load balancers and monitoring can check whether the proxy is alive on each node. If you health-check kube-proxy through an LB or scrape its metrics, this is the port to allow.
**Sources:** <a href="https://kubernetes.io/docs/reference/networking/ports-and-protocols/" target="_blank">Kubernetes Docs - Ports and Protocols</a>
**Tags:** k8s::kcna topic::networking topic::services src::session

---

<!-- note:1794007966275 model:Many -->
**Domain:** Cluster Networking - NodePort range
**Question:** Which port range must be open on worker nodes for NodePort Services?
**Options:** A. TCP and UDP 30000-32767 — the default NodePort range, open on every worker node<br>B. TCP 3000-3010 — the default HTTP service range<br>C. TCP 8080-8090 — the kube-proxy forwarding range<br>D. UDP 53 only — NodePort uses DNS ports
**Answer:** A (1) – TCP and UDP 30000-32767 — the default NodePort range, open on every worker node
**Explanation:** NodePort Services get a port in the default range 30000-32767 on EVERY node — both TCP and UDP are listed because the Service protocol decides which. kube-proxy on each node catches traffic arriving at nodeIP:nodePort and forwards it to a ready pod. The range is customizable (--service-node-port-range on the API server) — if you change it, open the NEW range instead. This is why NodePort is 'expose on all nodes': any node's IP works as an entry point.
**Sources:** <a href="https://kubernetes.io/docs/reference/networking/ports-and-protocols/" target="_blank">Kubernetes Docs - Ports and Protocols</a>
**Tags:** k8s::kcna topic::networking topic::services src::session

---

<!-- note:1794007966276 model:Many -->
**Domain:** Cluster Networking - port overrides
**Question:** Can the default component ports be changed?
**Options:** A. All of them are defaults — e.g. API server is often moved behind a 443 load balancer<br>B. Only the API server port can be changed<br>C. Ports are compiled into the kubelet binary<br>D. Changing ports requires recompiling Kubernetes
**Answer:** A (1) – All of them are defaults — e.g. API server is often moved behind a 443 load balancer
**Explanation:** Every port in the table is a default, not fixed: --secure-port on kube-apiserver, --etcd-servers for etcd placement, kubelet's --port, kube-proxy's --healthz-port/metrics-port, and --service-node-port-range for NodePort. The classic pattern: keep the API server on 6443 internally but front it with a load balancer listening on 443 that routes to it — external clients hit 443, internal traffic stays on 6443.
**Sources:** <a href="https://kubernetes.io/docs/reference/networking/ports-and-protocols/" target="_blank">Kubernetes Docs - Ports and Protocols</a>
**Tags:** k8s::kcna topic::networking topic::control-plane src::session

---

<!-- note:1794007966277 model:Many -->
**Domain:** Cluster Networking - node prereqs
**Question:** What network prerequisites must every node in a Kubernetes cluster satisfy?
**Options:** A. Each node needs ≥1 networked interface with an IP, a unique hostname, a unique MAC, and the documented ports open<br>B. All nodes must share one flat L2 broadcast domain<br>C. Each node needs a public IP address<br>D. Hostnames must match pod names exactly
**Answer:** A (1) – Each node needs ≥1 networked interface with an IP, a unique hostname, a unique MAC, and the documented ports open
**Explanation:** Cluster networking prerequisites per node: at least one interface connected to a network, each interface has an IP address, and the host has a unique hostname and unique MAC address — pod networking overlays (VXLAN etc.) and kubelet identity assume no two nodes look alike at L2. On top of that, the firewall must allow the documented component ports (6443, 2379-2380, 10250, 10256, 10257, 10259, NodePort range). Break any of these and you get subtle failures: duplicate hostnames confuse node identity, missing ports show up as probe/metrics timeouts.
**Sources:** <a href="https://kubernetes.io/docs/reference/networking/ports-and-protocols/" target="_blank">Kubernetes Docs - Ports and Protocols</a>
**Tags:** k8s::kcna topic::networking topic::cluster-setup src::session

---

<!-- note:1794007966278 model:Cloze -->
**Text:** Default Kubernetes ports — control plane then workers:<br><br>Control plane (all TCP inbound):<br>{{c1::kube-apiserver}} → {{c2::6443}} (all components)<br>{{c3::etcd}} → {{c4::2379-2380}} (client API)<br>{{c5::kube-controller-manager}} → {{c6::10257}} (self)<br>{{c7::kube-scheduler}} → {{c8::10259}} (self)<br><br>Worker nodes:<br>{{c9::kubelet}} → {{c10::10250}}<br>kube-proxy → {{c11::10256}} (healthz)<br>NodePort Services → {{c12::30000-32767}} TCP+UDP
**Back Extra:** Direction is always INBOUND to the listed component. kubelet 10250 appears on BOTH control plane and workers (control plane reaches in for logs/exec/metrics). etcd can live externally or on custom ports. NodePort range is a default — change it and open the new range instead. kube-proxy 10256 is health/metrics only, NOT service traffic.
**Tags:** k8s::kcna topic::networking topic::control-plane src::session

---

<!-- note:1794009250197 model:Many -->
**Domain:** CNI - ipMasquerade
**Question:** What does the "ipMasquerade" field in a Container Network Interface (CNI) plugin configuration file determine?
**Options:** A. Whether the plugin configuration file is valid<br>B. Whether the bridge network should have an assigned IP address<br>C. Whether a NAT rule should be added for IP masquerading<br>D. Whether the plugin supports IP masquerading
**Answer:** C (3) – Whether a NAT rule should be added for IP masquerading
**Explanation:** ipMasquerade (written ipMasq in the bridge plugin) is the on/off switch telling the CNI plugin to program iptables NAT MASQUERADE rules: pod traffic leaving the node gets its source IP rewritten to the node's IP — SNAT, same trick as a home router. It's needed because pod CIDR addresses (10.x) aren't routable outside the cluster — without masquerade, pod→internet egress has no return path. The field CONFIGURES masquerading; it doesn't validate the config file (schema does that), assign the bridge IP (that's ipam/isGateway), or declare plugin capability (capability is fixed — this is the per-config toggle).
**Sources:** <a href="https://kubernetes.io/docs/concepts/cluster-administration/networking/" target="_blank">Kubernetes Docs - Cluster Networking</a>
**Tags:** k8s::kcna topic::networking topic::cni src::session

---

<!-- note:1794009611473 model:Many -->
**Domain:** CNI - disabling masquerade
**Question:** When would you set ipMasquerade/ipMasq to false in a CNI configuration? (Select all that apply)
**Options:** A. Pod CIDRs are routable outside the cluster and you need end-to-end pod addressing<br>B. External systems must see real pod source IPs for whitelists or audit<br>C. Pods never need external connectivity — internal-only or air-gapped<br>D. Pods need outbound internet access
**Answer:** A, B, C – routable pod CIDR / source-IP preservation / internal-only clusters
**Explanation:** (Select all that apply) Masquerade trades source-IP fidelity for reachability — disable it (ipMasq/ipMasquerade/natOutgoing=false) when: pod CIDRs are externally routable and you want end-to-end pod addressing (routed/BGP networks); external systems must see REAL pod source IPs for whitelisting or audit (masquerade hides every pod behind its node's IP); or pods never need external connectivity (air-gapped/internal-only) so NAT is pure overhead. NOT a reason: pods needing internet access — that's exactly when masquerade must stay ON.
**Sources:** <a href="https://kubernetes.io/docs/concepts/cluster-administration/networking/" target="_blank">Kubernetes Docs - Cluster Networking</a>
**Tags:** k8s::kcna topic::networking topic::cni src::session

---

<!-- note:1794009827922 model:Many -->
**Domain:** CNI - isGateway
**Question:** What does the "isGateway" field in a Container Network Interface (CNI) plugin configuration file determine?
**Options:** A. Whether the bridge network should act as a gateway<br>B. Whether the bridge network should have an assigned IP address<br>C. Whether the plugin configuration file is valid<br>D. Whether the plugin supports gateway functionality
**Answer:** A (1) – Whether the bridge network should act as a gateway
**Explanation:** isGateway (default false) tells the bridge plugin to assign the bridge the IPAM-provided gateway IP — turning the bridge into the containers' gateway so pod traffic can route out of the pod network. Without it the bridge is pure L2 (container-to-container on the host only, no routing). Getting an IP is the mechanism; acting as gateway is the purpose — pods' default route points at the bridge IP. Sibling field isDefaultGateway additionally makes that IP the containers' default route. Like ipMasq, it CONFIGURES behavior — doesn't validate the file or declare plugin capability.
**Sources:** <a href="https://www.cni.dev/plugins/current/main/bridge/" target="_blank">CNI Docs - bridge plugin</a>
**Tags:** k8s::kcna topic::networking topic::cni src::session

---

<!-- note:1794009945361 model:Many -->
**Domain:** CNI - ipam type
**Question:** In a CNI plugin configuration file, what does the "type" field indicate when set to "host-local" under the IPAM section?
**Options:** A. The type of DNS resolution method used for pods<br>B. The type of network protocol used for pod communication<br>C. The type of network interface used for communication<br>D. The type of IP address management used for pods
**Answer:** D (4) – The type of IP address management used for pods
**Explanation:** ipam.type selects WHICH IPAM plugin allocates pod IPs: host-local = file-based allocation on each node from its podCIDR slice (the standard choice — no central allocator needed); dhcp delegates to an external DHCP server; static uses fixed IPs; whereabouts coordinates a shared pool across nodes. Watch the nesting: the TOP-LEVEL type field picks the main plugin (bridge, vlan…), while ipam.type picks only the address allocator — two different 'type' fields at different levels of the same JSON.
**Sources:** <a href="https://www.cni.dev/plugins/current/ipam/host-local/" target="_blank">CNI Docs - host-local IPAM plugin</a>
**Tags:** k8s::kcna topic::networking topic::cni src::session

---

<!-- note:1794010073685 model:Many -->
**Domain:** CNI - runtime responsibility
**Question:** What is the responsibility of a container runtime in terms of networking?
**Options:** A. All of the options are correct<br>B. Identifying and attaching namespaces to the appropriate network<br>C. Calling the appropriate network plugin<br>D. Creating container network namespaces
**Answer:** A (1) – All of the options are correct
**Explanation:** All three are genuine runtime jobs in the CNI flow: the container runtime (containerd/CRI-O) creates each container's network namespace, selects which CNI configuration applies (the .conflist in /etc/cni/net.d/), and invokes the CNI plugin's ADD/DEL commands to attach that namespace to the configured network. The kubelet delegates this via CRI — the runtime is the component that actually calls CNI; the plugin then does the hands-on work (veth pair, bridge, IPAM). Runtime orchestrates, plugin executes.
**Sources:** <a href="https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/" target="_blank">Kubernetes Docs - Network Plugins</a>
**Tags:** k8s::kcna topic::networking topic::cni topic::cri-oci src::session

---

<!-- note:1794016331742 model:Many -->
**Domain:** Pod Networking - requirements
**Question:** What does the Kubernetes network model require of pod networking? (Select all that apply)
**Options:** A. Every Pod gets its own IP address<br>B. Pods on the same node can communicate with each other<br>C. Pods on different nodes can communicate without NAT<br>D. Pods must communicate with each other through a NAT gateway<br>E. Every Pod must have a unique MAC address cluster-wide
**Answer:** A, B, C – every pod gets an IP; same-node pods reach each other; cross-node pods reach each other WITHOUT NAT
**Explanation:** (Select all that apply) The Kubernetes network model's core requirements: every Pod gets its own routable IP address; Pods on the same node communicate (localhost/bridge); Pods on DIFFERENT nodes communicate directly — WITHOUT NAT, meaning pod IPs are end-to-end routable across the cluster network. 'Without NAT' is the key constraint — it forbids hiding pod IPs behind node IPs for in-cluster traffic (that's what masquerade does only for EXTERNAL egress).
**Sources:** <a href="https://kubernetes.io/docs/concepts/cluster-administration/networking/" target="_blank">Kubernetes Docs - Cluster Networking</a>
**Tags:** k8s::kcna topic::networking topic::podnetwork src::session

---

<!-- note:1794016331743 model:Many -->
**Domain:** Pod Networking - who implements
**Question:** Kubernetes does not solve pod networking itself — what actually implements it?
**Options:** A. CNI plugins via the container runtime — Kubernetes only defines the requirements<br>B. kube-proxy alone handles all pod networking<br>C. The kube-apiserver assigns pod IPs directly<br>D. kubelet writes iptables rules for pod traffic
**Answer:** A (1) – CNI plugins via the container runtime — Kubernetes only defines the requirements
**Explanation:** Kubernetes deliberately does NOT implement pod networking — it specifies what must be true (IP per pod, NAT-free pod-to-pod) and lets CNIs satisfy it. The container runtime on each node invokes CNI plugins (bridge, Calico, Cilium, flannel…) which actually create interfaces, assign IPs, and wire routes. Many vendor CNIs exist offering different features — basic interface management up to integrated NetworkPolicy, advanced IPAM, multi-plugin chaining.
**Sources:** <a href="https://kubernetes.io/docs/concepts/cluster-administration/networking/" target="_blank">Kubernetes Docs - Cluster Networking</a>
**Tags:** k8s::kcna topic::networking topic::cni src::session

---

<!-- note:1794016331744 model:Many -->
**Domain:** Pod Networking - IP allocation
**Question:** Who assigns IP addresses to Pods, Services, and Nodes respectively?
**Options:** A. Network plugin assigns Pod IPs, kube-apiserver assigns Service IPs, kubelet/cloud-controller-manager assigns Node IPs<br>B. kube-apiserver assigns all three types<br>C. kubelet assigns Pod and Node IPs, network plugin assigns Service IPs<br>D. The CNI plugin assigns Service IPs too
**Answer:** A (1) – Network plugin assigns Pod IPs, kube-apiserver assigns Service IPs, kubelet/cloud-controller-manager assigns Node IPs
**Explanation:** Three different allocators for three object types, all from non-overlapping configured ranges: the NETWORK PLUGIN (CNI/IPAM) assigns Pod IPs; the kube-APISERVER assigns Service ClusterIPs; the KUBELET or cloud-controller-manager assigns Node IPs (cloud provider reports them). Knowing who owns which range matters for debugging IP conflicts and understanding why pod IPs and service IPs live in different CIDRs.
**Sources:** <a href="https://kubernetes.io/docs/concepts/cluster-administration/networking/" target="_blank">Kubernetes Docs - Cluster Networking</a>
**Tags:** k8s::kcna topic::networking topic::services src::session

---

<!-- note:1794016331745 model:Many -->
**Domain:** Pod Networking - NAT-free
**Question:** Why does the Kubernetes network model require pod-to-pod communication WITHOUT NAT?
**Options:** A. Pod IPs must be end-to-end routable — NAT would hide the real pod IP and break the return path/identity<br>B. NAT is faster than direct routing for pod traffic<br>C. Kubernetes requires NAT for pod-to-pod encryption<br>D. NAT is only needed on Windows nodes
**Answer:** A (1) – Pod IPs must be end-to-end routable — NAT would hide the real pod IP and break the return path/identity
**Explanation:** 'Without NAT' means pod-to-pod packets keep their real pod IPs all the way across nodes — the cluster network routes them directly. NAT is only acceptable for traffic LEAVING the cluster (that's what CNI masquerade/ipMasq does for external egress). If pod-to-pod used NAT, source identity would collapse to node IPs, conntrack state would multiply, and asymmetric paths could break replies — the model forbids it so pods have stable, meaningful IPs everywhere in the cluster.
**Sources:** <a href="https://kubernetes.io/docs/concepts/cluster-administration/networking/" target="_blank">Kubernetes Docs - Cluster Networking</a>
**Tags:** k8s::kcna topic::networking topic::cni src::session

---

<!-- note:1794016331746 model:Many -->
**Domain:** Pod Networking - CNI commands
**Question:** What commands does a CNI plugin implement for the container lifecycle?
**Options:** A. ADD connects the container to the network; DEL tears the interfaces down; plus CHECK and VERSION<br>B. Only ADD and DELETE — no other commands exist<br>C. START and STOP like systemd services<br>D. Only VERSION — the runtime does all the work
**Answer:** A (1) – ADD connects the container to the network; DEL tears the interfaces down; plus CHECK and VERSION
**Explanation:** A CNI plugin is an executable that implements spec commands: ADD — called when a container is created, attaches its interface to the network (veth, IP, routes); DEL — called on teardown, removes interfaces and releases the IP; CHECK — verifies config is still applied (optional); VERSION — reports supported spec version. The runtime invokes these per container lifecycle — 'the script' your lecture demoed is exactly this ADD/DEL contract.
**Sources:** <a href="https://www.cni.dev/docs/spec/" target="_blank">CNI Spec - Container Network Interface</a>
**Tags:** k8s::kcna topic::networking topic::cni src::session

---

<!-- note:1794016331747 model:Many -->
**Domain:** Pod Networking - cni dirs
**Question:** What do --cni-conf-dir and --cni-bin-dir point at?
**Options:** A. kubelet --cni-conf-dir=/etc/cni/net.d holds the .conflist configs; --cni-bin-dir=/opt/cni/bin holds the plugin executables<br>B. --cni-conf-dir holds binaries; --cni-bin-dir holds configs<br>C. Both flags point at /etc/cni by default<br>D. These are containerd flags, not kubelet flags
**Answer:** A (1) – kubelet --cni-conf-dir=/etc/cni/net.d holds the .conflist configs; --cni-bin-dir=/opt/cni/bin holds the plugin executables
**Explanation:** Two kubelet flags wire CNI in: --cni-conf-dir (default /etc/cni/net.d) contains the network CONFIG files — JSON .conflist files naming which plugins/IPAM to use (this is where 'bridge', 'host-local' etc. get selected); --cni-bin-dir (default /opt/cni/bin) contains the plugin EXECUTABLES the configs point at. Flow: kubelet reads the conflist → picks plugin name → runtime executes that binary from bin-dir with ADD + the container's ID/netns. Wrong dir or missing binary = pods stuck in ContainerCreating.
**Sources:** <a href="https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/parameters/" target="_blank">Kubernetes Docs - kubelet parameters</a>
**Tags:** k8s::kcna topic::networking topic::cni topic::kubelet src::session

---

<!-- note:1794016331748 model:Many -->
**Domain:** Pod Networking - who solves what
**Question:** Which component solves which networking problem?
**Options:** A. pod-to-pod is CNI's job; pod-to-Service and external-to-Service are Services' job<br>B. CNI handles everything including Service load balancing<br>C. kube-proxy handles pod-to-pod; CNI handles Services<br>D. The kube-apiserver routes all four types
**Answer:** A (1) – pod-to-pod is CNI's job; pod-to-Service and external-to-Service are Services' job
**Explanation:** The docs split cluster networking into 4 problems with different owners: container-to-container on one pod = localhost (free); POD-TO-POD = CNI plugins (the network model — IPs, interfaces, routes); POD-TO-SERVICE and EXTERNAL-TO-SERVICE = Services (ClusterIP, kube-proxy, Ingress). This is why kube-proxy doesn't assign pod IPs (CNI does) and CNI doesn't load-balance service names (Services do) — complementary layers, not competing ones.
**Sources:** <a href="https://kubernetes.io/docs/concepts/cluster-administration/networking/" target="_blank">Kubernetes Docs - Cluster Networking</a>
**Tags:** k8s::kcna topic::networking topic::cni topic::services src::session

---

<!-- note:1794016331749 model:Many -->
**Domain:** Pod Networking - IP families
**Question:** How are Kubernetes clusters categorized by IP family?
**Options:** A. IPv4-only, IPv6-only, or dual-stack — and all components must agree on the primary IP family<br>B. Only IPv4 is supported for pod networking<br>C. Dual-stack requires a special CNI license<br>D. Each node can independently choose its IP family
**Answer:** A (1) – IPv4-only, IPv6-only, or dual-stack — and all components must agree on the primary IP family
**Explanation:** Clusters are categorized by configured IP families: IPv4-only, IPv6-only, or dual-stack (IPv4/IPv6 or IPv6/IPv4). For dual-stack ALL components must agree — network plugin assigns both families to pods, kube-apiserver assigns both to services, kubelet/CCM assigns node IPs, and they must agree on which family is PRIMARY. Only IPs in pod.status.ips/node.status.addresses count for the model — extra interface IPs are ignored.
**Sources:** <a href="https://kubernetes.io/docs/concepts/cluster-administration/networking/" target="_blank">Kubernetes Docs - Cluster Networking</a>
**Tags:** k8s::kcna topic::networking topic::cluster-setup src::session

---

<!-- note:1794016331753 model:Cloze -->
**Text:** Kubernetes pod networking model — the requirements and who implements them:<br><br>K8s requires: every Pod gets {{c1::its own IP address}}; Pods on the same node can {{c2::communicate}}; Pods on different nodes can communicate {{c3::without NAT}}.<br><br>K8s does NOT implement this — the {{c4::container runtime}} invokes {{c5::CNI plugins}} on each node.<br><br>IP allocation: {{c6::network plugin}} → Pod IPs; {{c7::kube-apiserver}} → Service IPs; {{c8::kubelet/cloud-controller-manager}} → Node IPs.
**Back Extra:** K8s defines the WHAT, CNIs provide the HOW — the container runtime invokes CNI plugins per node. IP owners: network plugin→Pods, kube-apiserver→Services, kubelet/CCM→Nodes (all non-overlapping). Pod-to-pod = CNI; pod/service/external-to-service = Services. Runtime reads .conflist from --cni-conf-dir, executes plugin from --cni-bin-dir with ADD/DEL commands.
**Tags:** k8s::kcna topic::networking topic::cni topic::podnetwork src::session

---

<!-- note:1794076936965 model:Many -->
**Domain:** CNI Config - conflist structure
**Question:** What are the top-level keys of a CNI .conflist network configuration?
**Options:** A. cniVersion/cniVersions, name, and plugins[] — bridge/ipam/dns live INSIDE each plugin object<br>B. bridge, ipam, dns, and name at the top level<br>C. Only name and type — everything else is optional<br>D. YAML keys: apiVersion, kind, metadata like other K8s objects
**Answer:** A (1) – cniVersion/cniVersions, name, and plugins[] — bridge/ipam/dns live INSIDE each plugin object
**Explanation:** A .conflist network config is a JSON object with top-level keys: cniVersion (spec version string like "1.1.0") or cniVersions (list of supported versions), name (unique network name per host), and plugins — an array of plugin config objects. Fields like type, bridge, ipam, dns, capabilities are PER-PLUGIN, nested inside each plugins[] entry — not top-level. Think of it as: envelope (version+name) → list of plugin instructions.
**Sources:** <a href="https://www.cni.dev/docs/spec/" target="_blank">CNI Spec - Network configuration format</a>
**Tags:** k8s::kcna topic::networking topic::cni topic::yaml src::session

---

<!-- note:1794076936966 model:Many -->
**Domain:** CNI Config - type binary
**Question:** In a CNI plugin config, what does the "type" field specify?
**Options:** A. The filename of the plugin executable in the CNI bin dir — type: bridge → /opt/cni/bin/bridge<br>B. The network type like bridge or vlan only<br>C. The plugin's version number<br>D. Whether the plugin is enabled or disabled
**Answer:** A (1) – The filename of the plugin executable in the CNI bin dir — type: bridge → /opt/cni/bin/bridge
**Explanation:** Each plugin object's "type" field names the plugin BINARY on disk — it's how the config points at the executable: type: "bridge" makes the runtime look for /opt/cni/bin/bridge. This is the exact mechanism from your lecture: config in net.d identifies the script name, runtime finds that binary in the bin dir and executes it with ADD/DEL. Same for ipam.type — it names the IPAM plugin's executable, not a behavior.
**Sources:** <a href="https://www.cni.dev/docs/spec/" target="_blank">CNI Spec - Plugin configuration objects</a>
**Tags:** k8s::kcna topic::networking topic::cni src::session

---

<!-- note:1794076936967 model:Many -->
**Domain:** CNI Config - plugin chaining
**Question:** What does the plugins[] array in a .conflist enable?
**Options:** A. Multiple plugins can be chained — a main plugin (bridge) plus meta plugins (tuning, portmap, firewall) that adjust the result<br>B. Only one plugin can ever be configured per network<br>C. plugins[] lists backup plugins used if the first fails<br>D. Each plugins[] entry runs on a different node
**Answer:** A (1) – Multiple plugins can be chained — a main plugin (bridge) plus meta plugins (tuning, portmap, firewall) that adjust the result
**Explanation:** The plugins[] array enables CHAINING: the runtime executes each plugin in order, passing each one's result (prevResult) to the next. Typically the first entry is the 'interface' plugin that creates the interface+IP (bridge), followed by 'meta' plugins that modify the already-created interface — tuning (sysctl, MAC), portmap (hostPort mapping), firewall, bandwidth. Spec v0.3.0 introduced chaining; v1.0.0 then REQUIRED the plugins array even for a single plugin.
**Sources:** <a href="https://www.cni.dev/docs/spec/" target="_blank">CNI Spec - plugin chaining</a>
**Tags:** k8s::kcna topic::networking topic::cni src::session

---

<!-- note:1794076936968 model:Many -->
**Domain:** CNI Config - spec versions
**Question:** Since CNI spec v1.0.0, can a network config omit the plugins[] array for a single plugin?
**Options:** A. No — spec v1.0.0 removed non-list configs; every network config must use the plugins[] array<br>B. Yes — bare single-plugin configs are still valid<br>C. Only on Windows nodes<br>D. Only if cniVersion is below 1.0.0
**Answer:** A (1) – No — spec v1.0.0 removed non-list configs; every network config must use the plugins[] array
**Explanation:** Spec history that matters: v0.3.0 added plugin chaining + rich results; v0.4.0 added CHECK; v1.0.0 REMOVED non-list configurations — a bare single-plugin JSON without plugins[] is invalid in modern CNI; v1.1.0 added STATUS and GC commands plus cniVersions for multi-version support. So even a one-plugin network must be wrapped: {"cniVersion":"1.0.0","name":"x","plugins":[{"type":"bridge",...}]}. The cniVersions list field lets one config declare which spec versions it supports.
**Sources:** <a href="https://www.cni.dev/docs/spec/" target="_blank">CNI Spec - version history</a>
**Tags:** k8s::kcna topic::networking topic::cni src::session

---

<!-- note:1794076936969 model:Many -->
**Domain:** CNI Config - env params
**Question:** What parameters does the container runtime pass to CNI plugins? (Select all that apply)
**Options:** A. CNI_CONTAINERID — the unique container identifier<br>B. CNI_NETNS — path to the container's network namespace<br>C. CNI_IFNAME — the interface name to create in the container<br>D. CNI_PATH — the plugin binary search path
**Answer:** A, B, C, D – CNI_CONTAINERID, CNI_NETNS, CNI_IFNAME, CNI_ARGS/CNI_PATH all passed by the runtime
**Explanation:** (Select all that apply) The runtime passes per-attachment context to plugins via env vars/parameters: CNI_CONTAINERID (unique container ID), CNI_NETNS (path to the container's network namespace, e.g. /run/netns/...), CNI_IFNAME (interface name to create inside the container), CNI_ARGS (extra key-value args), and CNI_PATH (the plugin search path so plugins can find delegated binaries like IPAM). These are what the ADD/DEL calls carry — the 'name and namespaceID' your lecture mentioned.
**Sources:** <a href="https://www.cni.dev/docs/spec/" target="_blank">CNI Spec - Attachment Parameters</a>
**Tags:** k8s::kcna topic::networking topic::cni src::session

---

<!-- note:1794076936970 model:Many -->
**Domain:** CNI Config - lifecycle rules
**Question:** Which lifecycle rules does the CNI spec mandate? (Select all that apply)
**Options:** A. The runtime creates the network namespace before invoking plugins and cleans it up itself<br>B. Every ADD must eventually be followed by a DEL — even if the ADD failed<br>C. The network config must not change between ADD and DEL<br>D. Plugins create and destroy the network namespace themselves
**Answer:** A, B, C – runtime creates netns first; add must be followed by delete; delete runs even if add fails; runtime owns netns cleanup
**Explanation:** (Select all that apply) Spec-mandated lifecycle: the runtime creates the container's network namespace BEFORE invoking any plugin and is responsible for cleaning it up afterward; every ADD must eventually be followed by a DEL (even if ADD failed); DEL may be retried; config must not change between add and delete; runtimes may parallelize across containers but not for the same container; GC operations must not overlap with add/delete.
**Sources:** <a href="https://www.cni.dev/docs/spec/" target="_blank">CNI Spec - Lifecycle & Ordering</a>
**Tags:** k8s::kcna topic::networking topic::cni src::session

---

<!-- note:1794076936975 model:Cloze -->
**Text:** Spec example — 'dbnet' conflist chaining bridge + tuning + portmap:<br><br><code>{<br>  cniVersion: {{c1::"1.1.0"}},<br>  name: {{c2::dbnet}},<br>  plugins: [<br>    { type: {{c3::bridge}}, bridge: cni0,<br>      ipam: { type: {{c4::host-local}}, subnet: 10.1.0.0/16 } },<br>    { type: {{c5::tuning}}, capabilities: { mac: true } },<br>    { type: {{c6::portmap}}, capabilities: { portMappings: true } }<br>  ]<br>}</code>
**Back Extra:** dbnet example from the spec: bridge creates cni0 + assigns IP via host-local IPAM (10.1.0.0/16, gw 10.1.0.1, default route); dns sets pod resolv.conf nameserver; tuning adjusts sysctls/MAC via capabilities; portmap exposes hostPort mappings via capabilities.portMappings. 'type' in each entry = binary filename in /opt/cni/bin. ipam is itself a plugin delegation (ipam.type = IPAM binary).
**Tags:** k8s::kcna topic::networking topic::cni topic::yaml src::session

---

<!-- note:1794078127989 model:Many -->
**Domain:** Resiliency Patterns - bulkhead
**Question:** Which resiliency pattern prevents a cascade of failures by isolating each component so a failure in one does not affect others?
**Options:** A. Retry<br>B. Circuit breaker<br>C. Timeout<br>D. Bulkhead
**Answer:** D (4) – Bulkhead
**Explanation:** Bulkhead isolates resources — separate thread pools, connection pools, or replicas per dependency — so one failing component can't consume everything and cascade. Named after ship compartments: a hull breach floods one section, not the ship. Contrast with the others: Circuit breaker stops CALLING a failing dependency (failure handling, not isolation); Timeout caps how long a caller waits; Retry re-attempts failed calls. Bulkhead is the only one that prevents failure PROPAGATION by partitioning capacity.
**Sources:** <a href="https://microservices.io/patterns/reliability/bulkhead-pattern.html" target="_blank">microservices.io - Bulkhead Pattern</a>
**Tags:** k8s::kcna topic::architecture topic::resiliency src::session

---

<!-- note:1794078127990 model:Many -->
**Domain:** Resiliency Patterns - circuit breaker
**Question:** A payment API dependency keeps failing. Which pattern makes callers fail fast instead of waiting for it, then probes for recovery?
**Options:** A. Bulkhead<br>B. Circuit breaker<br>C. Timeout<br>D. Retry
**Answer:** B (2) – Circuit breaker
**Explanation:** Circuit breaker monitors calls to a dependency and, after a failure threshold, 'opens' — callers fail fast instead of waiting on a dead service, then periodically 'half-opens' to test recovery. It's about STOPPING traffic to a failing dependency, not partitioning resources (that's bulkhead) or retrying (that's retry's job — dangerous combined with a breaker since retries amplify load).
**Sources:** <a href="https://microservices.io/patterns/reliability/circuit-breaker.html" target="_blank">microservices.io - Circuit Breaker</a>
**Tags:** k8s::kcna topic::architecture topic::resiliency src::session

---

<!-- note:1794078127998 model:Cloze -->
**Text:** Resiliency pattern family — purpose of each:<br><br>{{c1::Retry}} — re-attempt a failed call (transient errors)<br>{{c2::Timeout}} — cap how long a caller waits<br>{{c3::Circuit breaker}} — stop calling a failing dependency, probe for recovery<br>{{c4::Bulkhead}} — isolate resources so one component's failure can't cascade
**Back Extra:** Full mapping: Retry = re-attempt transient failures (watch for retry storms amplifying load); Timeout = cap caller wait (frees threads but doesn't isolate); Circuit breaker = fail-fast + probe recovery on a failing dependency; Bulkhead = partition resources so one failure can't cascade. In Kubernetes these are app-level patterns — the platform gives you probes/replicas, but the code implements the patterns.
**Tags:** k8s::kcna topic::architecture topic::resiliency src::session

---
