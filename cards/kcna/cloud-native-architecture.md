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
