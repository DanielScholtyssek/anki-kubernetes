# KCNA - Kubernetes and Cloud Native Associate — Cloud Native Architecture

> Deck: `KCNA - Kubernetes and Cloud Native Associate` · Group: `Cloud Native Architecture` · Notes: 24 · Models: Many

<!-- note:1793920205003 model:Many -->
**Domain:** CNCF Governance
**Question:** What is the preferred decision-making style in CNCF governance groups?
**Options:** A. CEO-only decisions<br>B. Consensus-seeking<br>C. Random selection<br>D. Majority vote always
**Answer:** B (2) – consensus-seeking
**Explanation:** Consensus-seeking means the group works toward a decision everyone can accept through open discussion (mailing lists, Slack, recorded meetings) rather than forcing a vote — proposals stay open for review and only move forward when there's no unresolved objection. It's a process goal, NOT strict unanimity: the TOC charter says decisions are 'driven by consensus', and only if consensus can't be reached does a binding vote get called as deadlock fallback. That's why 'majority vote always' is wrong — winner-take-all voting lets a bare majority override minority concerns and fractures communities; 'CEO-only' and 'random' aren't governance at all.
**Sources:** <a href="https://github.com/cncf/foundation/blob/main/charter.md" target="_blank">CNCF Charter - TOC Mandate</a>
**Tags:** k8s::kcna src::session topic::ecosystem topic::governance

---

<!-- note:1794078127989 model:Many -->
**Domain:** Resiliency Patterns - bulkhead
**Question:** Which resiliency pattern prevents a cascade of failures by isolating each component so a failure in one does not affect others?
**Options:** A. Retry<br>B. Circuit breaker<br>C. Timeout<br>D. Bulkhead
**Answer:** D (4) – Bulkhead
**Explanation:** Bulkhead isolates resources — separate thread pools, connection pools, or replicas per dependency — so one failing component can't consume everything and cascade. Named after ship compartments: a hull breach floods one section, not the ship. Contrast with the others: Circuit breaker stops CALLING a failing dependency (failure handling, not isolation); Timeout caps how long a caller waits; Retry re-attempts failed calls. Bulkhead is the only one that prevents failure PROPAGATION by partitioning capacity.
**Sources:** <a href="https://microservices.io/patterns/reliability/bulkhead-pattern.html" target="_blank">microservices.io - Bulkhead Pattern</a>
**Tags:** k8s::kcna src::session topic::architecture topic::resiliency

---

<!-- note:1794080037272 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** Why is container orchestration essential for managing microservices at scale?
**Options:** A. It simplifies writing microservice code<br>B. It automatically converts monolithic apps to microservices<br>C. It handles service discovery, scaling, and fault tolerance<br>D. It provides a centralized logging solution by default<br>E. It guarantees zero-downtime deployments
**Answer:** C – It handles service discovery, scaling, and fault tolerance
**Explanation:** Orchestrators like Kubernetes automate complex tasks<br>like service discovery, load balancing, scaling based on demand, and selfhealing, which are crucial for managing a distributed microservices architecture.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037273 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** What fundamental problem does a <b>Service Mesh</b> like <b>Istio </b>or <b>Linkerd </b>aim to solve in a microservices architecture?
**Options:** A. Simplifying container image building<br>B. Automating infrastructure provisioning<br>C. Managing and observing inter-service communication<br>D. Providing persistent storage for stateful applications<br>E. Abstracting server management
**Answer:** C – Managing and observing inter-service communication
**Explanation:** Service meshes provide a dedicated infrastructure layer for<br>handling service-to-service communication, offering features 1 like traffic<br>management, security (mTLS), and observability (metrics, traces) without<br>requiring changes to application code.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037274 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** How does Serverless (e.g., FaaS like AWS Lambda or Knative Serving) <b>primarily </b>differ from traditional PaaS offerings?
**Options:** A. Serverless does not use containers<br>B. Serverless applications cannot be stateful<br>C. Serverless abstracts away all underlying server management<br>D. PaaS does not offer auto-scaling capabilities<br>E. Serverless is only for event-driven functions
**Answer:** C – Serverless abstracts away all underlying server management
**Explanation:** Serverless computing (especially FaaS) aims to abstract<br>away all infrastructure management, including servers, OS, and runtimes,<br>allowing developers to focus solely on writing code that executes in response to events.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037275 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** What is <b>the primary role</b> of the Cloud Native Computing Foundation (CNCF) in the Kubernetes ecosystem?
**Options:** A. To directly employ Kubernetes core developers<br>B. To sell Kubernetes enterprise support subscriptions<br>C. To foster and sustain an ecosystem of open source projects<br>D. To define mandatory cloud provider APIs<br>E. To own the intellectual property of Linux
**Answer:** C – To foster and sustain an ecosystem of open source projects
**Explanation:** The CNCF hosts and promotes a wide range of open source<br>projects (including Kubernetes, Prometheus, Envoy) to advance cloud native computing, providing governance, support, and community building.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037276 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** In a typical cloud native environment, which persona<b> is most concerned with</b> ensuring application uptime, performance, and managing incident response?
**Options:** A. Application Developer<br>B. Platform Consumer<br>C. Site Reliability Engineer (SRE) / Platform Operator<br>D. Business Analyst<br>E. End User
**Answer:** C – Site Reliability Engineer (SRE) / Platform Operator
**Explanation:** SREs and Platform Operators are responsible for the reliability, scalability, and overall operational health of the platform and the<br>applications running on it, including monitoring, alerting, and incident<br>management.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037277 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** Which of the following is NOT a core characteristic of cloud native architectures?
**Options:** A. Microservices<br>B. Containers<br>C. Monolithic application design<br>D. DevOps practices<br>E. Automation
**Answer:** C – Monolithic application design
**Explanation:** Cloud native architectures typically favor microservices,<br>containers, dynamic orchestration (like Kubernetes), and DevOps/Agile<br>practices, moving away from large, tightly coupled monolithic designs.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037278 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** What is a primary characteristic of Vertical Pod Autoscaling (VPA)?
**Options:** A. It adjusts the number of Pod replicas.<br>B. It adjusts the CPU and memory requests and limits for Pods.<br>C. It adds or removes Nodes from the cluster.<br>D. It automatically selects the optimal storage class.<br>E. It scales the number of available IP addresses.
**Answer:** B – It adjusts the CPU and memory requests and limits for Pods.
**Explanation:** VPA recommends or automatically updates the resource<br>requests and limits for containers within Pods to match actual usage,<br>helping to optimize resource allocation. It does not change the number of<br>replicas (that’s HPA).
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037279 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** Which of these is a <b>primary </b>goal of the CNCF’s "Trail Map" for cloud native adoption?
**Options:** A. To mandate specific vendor products for each stage.<br>B. To provide a prescriptive path for building cloud native apps.<br>C. To offer a recommended journey and project choices for adopters.<br>D. To rank cloud providers based on their Kubernetes offerings.<br>E. To certify individual developers as cloud native experts.
**Answer:** C – To offer a recommended journey and project choices for adopters.
**Explanation:** The CNCF Trail Map suggests a path for organizations<br>adopting cloud native technologies, highlighting CNCF projects that can<br>help at different stages (e.g., containerization, CI/CD, orchestration, observability).
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037280 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** What is the <b>primary </b>motivation behind using ”Serverless Functions” (FaaS)?
**Options:** A. To achieve higher compute density on physical servers.<br>B. To run long-lived, stateful batch processing jobs.<br>C. To execute event-driven code without managing infrastructure.<br>D. To gain fine-grained control over OS-level configurations.<br>E. To build complex, monolithic application backends.
**Answer:** C – To execute event-driven code without managing infrastructure.
**Explanation:** Serverless functions are designed for short-lived, eventdriven computations where the underlying infrastructure (servers, OS) is<br>completely managed by the platform, allowing developers to focus on code.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037281 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** What type of software package bundles application code with all its dependencies, libraries, and configuration files?
**Options:** A. Virtual Machine<br>B. Container<br>C. Operating System<br>D. Serverless Function
**Answer:** B – Container
**Explanation:** Containers package application code and dependencies together, isolating them from the underlying infrastructure.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037282 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** What is <b>the primary purpose</b> of a Service Mesh like Istio or Linkerd?
**Options:** A. Container image building<br>B. Cluster storage management<br>C. Managing inter-service comms<br>D. Node provisioning
**Answer:** C – Managing inter-service comms
**Explanation:** Service meshes add observability, security, and reliability features to communication between microservices (service-to-service).
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037283 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** Which mechanism allows Kubernetes to automatically adjust the number of Pods in a Deployment based on CPU utilization or custom metrics?
**Options:** A. Vertical Pod Autoscaler (VPA)<br>B. Cluster Autoscaler (CA)<br>C. Horizontal Pod Autoscaler (HPA)<br>D. Node Problem Detector (NPD)
**Answer:** C – Horizontal Pod Autoscaler (HPA)
**Explanation:** The HPA automatically scales the number of Pod replicas based on observed metrics like CPU or memory usage.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037284 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** What term describes an architectural approach where applications are built as small, independent services that run in their own processes?
**Options:** A. Monolithic<br>B. Microservices<br>C. Serverless<br>D. N-Tier
**Answer:** B – Microservices
**Explanation:** Microservices architecture structures an application as a collection of loosely coupled, independently deployable services.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037285 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** What does ”Serverless” computing primarily abstract away from the developer?
**Options:** A. Networking<br>B. Storage<br>C. Server Management<br>D. Operating System choice
**Answer:** C – Server Management
**Explanation:** Serverless platforms (like FaaS) manage the underlying infrastructure, allowing developers to focus solely on code execution.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037286 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** Which organization hosts Kubernetes and promotes the growth of the cloud native ecosystem?
**Options:** A. Linux Foundation (LF)<br>B. Apache Software Foundation (ASF)<br>C. Cloud Native Computing Foundation (CNCF)<br>D. Open Source Initiative (OSI)
**Answer:** C – Cloud Native Computing Foundation (CNCF)
**Explanation:** The CNCF, part of the Linux Foundation, stewards Kubernetes and many other cloud native projects.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037287 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** What is the benefit of using open standards in cloud native technologies?
**Options:** A. Vendor lock-in<br>B. Increased complexity<br>C. Interoperability Portability<br>D. Reduced security
**Answer:** C – Interoperability Portability
**Explanation:** Open standards (like OCI, CRI, CNI) ensure that different tools and platforms can work together, preventing vendor lock-in.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037288 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** In a typical cloud native environment, which persona is <b>primarily responsible</b> for designing and building the application?
**Options:** A. Operator<br>B. Developer<br>C. Site Reliability Engineer (SRE)<br>D. Security Engineer
**Answer:** B – Developer
**Explanation:** Developers focus on writing, building, and testing the application code that runs within the cloud native platform.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037289 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** Which persona is typically focused on the reliability, scalability, and maintenance of the underlying Kubernetes platform?
**Options:** A. End User<br>B. Application Developer<br>C. Platform Operator / SRE<br>D. Data Scientist
**Answer:** C – Platform Operator / SRE
**Explanation:** Operators or SREs manage the Kubernetes cluster itself, ensuring it’s healthy, scalable, and available for developers.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037290 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** Which are key service mesh features? Select two answers
**Options:** A. Load balancing and discovery<br>B. mTLS security<br>C. Image storage<br>D. CI/CD automation
**Answer:** A, B – Load balancing and discovery; mTLS security
**Explanation:** Service meshes handle traffic management and secure service-to-service communication.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037291 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** How do service meshes benefit microservices?
**Options:** A. Network abstractions<br>B. Centralized logging<br>C. Remove containers<br>D. Auto-scale servers
**Answer:** A – Network abstractions
**Explanation:** They abstract networking concerns away from application code.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037292 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** What is a key serverless characteristic?
**Options:** A. Manual scaling<br>B. Pay per execution time<br>C. Server management<br>D. Manual start/stop
**Answer:** B – Pay per execution time
**Explanation:** Serverless charges based on actual compute usage.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794080037293 model:Many -->
**Domain:** KCNA - Cloud Native Architecture
**Question:** What does FaaS stand for?
**Options:** A. Function as a Service<br>B. File as a Service<br>C. Fragmentation as a Service<br>D. Framework as a Service
**Answer:** A – Function as a Service
**Explanation:** FaaS allows execution of functions without managing servers.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::architecture topic::mcq

---

<!-- note:1794083436738 model:Many -->
**Domain:** Cluster DNS - FQDN
**Question:** What is a Fully Qualified Domain Name (FQDN)?
**Options:** A. The shortest possible name for a resource inside a cluster<br>B. An absolute domain name giving the complete path from the DNS root — unambiguous no matter where the query originates<br>C. A name that only resolves inside the namespace where it was created<br>D. The IP address assigned to a Service
**Answer:** B (2) – An absolute domain name giving the complete path from the DNS root — unambiguous no matter where the query originates
**Explanation:** FQDN = Fully Qualified Domain Name: the COMPLETE, absolute name — every label spelled out from the root down, e.g. my-svc.my-namespace.svc.cluster.local. Because it's absolute, it resolves identically no matter which pod/namespace asks (technically it ends at the root '.'). Contrast with SHORT names like 'my-svc' or 'my-svc.my-namespace' — those only resolve because /etc/resolv.conf search domains expand them. In Kubernetes every DNS record IS an FQDN under the cluster.local root zone; short forms are just conveniences.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/" target="_blank">Kubernetes Docs - DNS for Services and Pods</a>
**Tags:** k8s::kcna topic::networking topic::dns src::session

---

<!-- note:1794083495923 model:Many -->
**Domain:** Cluster DNS - pod IP records
**Question:** A Pod has IP address 10.244.1.5 and runs in namespace 'prod'. What is its IP-based DNS name (assuming cluster domain cluster.local)?
**Options:** A. 10.244.1.5.prod.pod.cluster.local<br>B. 10-244-1-5.prod.pod.cluster.local<br>C. 10-244-1-5.prod.svc.cluster.local<br>D. prod.10-244-1-5.pod.cluster.local
**Answer:** B (2) – 10-244-1-5.prod.pod.cluster.local
**Explanation:** Every Pod gets an A/AAAA DNS record built from its IP: replace each DOT with a DASH (DNS labels can't contain dots), then append <namespace>.pod.cluster.local. So 10.244.1.5 in namespace prod → 10-244-1-5.prod.pod.cluster.local. Dots can't appear inside a DNS label, which is WHY the transformation exists. Note the .pod. subdomain — distinct from .svc. which is for Services. Pods can ALSO get friendlier names via spec.hostname+spec.subdomain (the StatefulSet pattern) and service-associated records.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/" target="_blank">Kubernetes Docs - DNS for Services and Pods</a>
**Tags:** k8s::kcna topic::networking topic::dns src::session

---

<!-- note:1794083495924 model:Many -->
**Domain:** Cluster DNS - pod name forms
**Question:** Which DNS names can a Pod have? (Select all that apply)
**Options:** A. <pod-ip-with-dashes>.<namespace>.pod.cluster.local<br>B. <hostname>.<subdomain>.<namespace>.svc.cluster.local<br>C. <pod-name>.<namespace>.svc.cluster.local (automatic for every pod)<br>D. <pod-ip-with-dots>.<namespace>.pod.cluster.local
**Answer:** A, B – IP-dashes form always; hostname.subdomain form when spec.hostname+subdomain set
**Explanation:** Pod DNS names come in forms (select all that apply): (A) <ip-dashes>.<ns>.pod.cluster.local — created for EVERY pod from its IP; (B) <hostname>.<subdomain>.<ns>.svc.cluster.local — when spec.hostname AND spec.subdomain are set (StatefulSet pods get pod-name + service-name, e.g. busybox-1.busybox-subdomain.ns.svc.cluster.local); pods backing a service can also get <ip-dashes>.<svc>.<ns>.svc.cluster.local. NOT valid: <pod-name>.<ns>.svc.cluster.local is NOT automatic — pod names aren't DNS records unless hostname/subdomain configured; and IPs keep dashes, never dots, inside a label.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/" target="_blank">Kubernetes Docs - DNS for Services and Pods</a>
**Tags:** k8s::kcna topic::networking topic::dns src::session

---
