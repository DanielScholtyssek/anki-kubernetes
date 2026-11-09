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

<!-- note:1794083549726 model:Many -->
**Domain:** Cluster DNS - subdomain branches
**Question:** Pod IP-based DNS records like 10-244-1-1.apps.pod.cluster.local live under which subdomain branch of cluster.local?
**Options:** A. svc.cluster.local — same branch as Services<br>B. pod.cluster.local — a dedicated branch parallel to svc.cluster.local<br>C. cluster.local root directly — pods have no subdomain<br>D. apps.cluster.local — the namespace becomes the branch
**Answer:** B (2) – pod.cluster.local — a dedicated branch parallel to svc.cluster.local
**Explanation:** cluster.local is the ROOT zone; below it sit dedicated subdomain branches: svc.cluster.local holds SERVICE records (<svc>.<ns>.svc.cluster.local) and pod.cluster.local holds POD IP-based records (<ip-dashes>.<ns>.pod.cluster.local). Reading 10-244-1-1.apps.pod.cluster.local right-to-left: pod.cluster.local branch → namespace 'apps' → the dashed-IP label. The namespace is a LEVEL inside the branch, not the branch itself — 'apps' is not a top-level subdomain.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/" target="_blank">Kubernetes Docs - DNS for Services and Pods</a>
**Tags:** k8s::kcna topic::networking topic::dns src::session

---

<!-- note:1794258268157 model:Many -->
**Domain:** Monoliths vs Microservices - monolith definition
**Question:** What characterizes a monolithic application architecture?
**Options:** A. Functionality split into small independently deployable services<br>B. All application functionality in a single deployable unit with a shared codebase, typically no clear module boundaries and often one shared database<br>C. Each team owns a separate service with its own datastore<br>D. Event-driven functions executed on demand without servers
**Answer:** B (2) – All application functionality in a single deployable unit with a shared codebase, typically no clear module boundaries and often one shared database
**Explanation:** Monolith = ALL functionality in ONE deployable program — one codebase, one deployment artifact, typically one shared database. Modules may exist in the code but cannot run or scale independently, and boundaries blur over time ('big ball of mud'). NOT the same as 'bad code' — a monolith can be well-structured; what defines it is that components can't deploy/scale independently. It's the simplest place to start; it becomes a problem at scale.
**Sources:** <a href="https://glossary.cncf.io/monolithic-apps/" target="_blank">CNCF Glossary - Monolithic Apps</a>
**Tags:** k8s::kcna topic::microservices topic::architecture src::session

---

<!-- note:1794258268158 model:Many -->
**Domain:** Monoliths vs Microservices - monolith problems
**Question:** Which are characteristic problems of monolithic architectures? (Select all that apply)
**Options:** A. Every change requires redeploying the entire application — no partial releases<br>B. A bug in one module can break unrelated functionality (large blast radius)<br>C. Scaling one busy feature means scaling the whole app<br>D. Modules develop tight version dependencies on each other<br>E. Independent per-service scaling and polyglot languages
**Answer:** A, B, C, D – all-or-nothing deploys; blast radius; whole-app scaling; module version coupling
**Explanation:** The monolith trap: (A) all-or-nothing deploys — any change ships the whole app, slowing releases and raising risk; (B) shared runtime + shared DB means one bug/schema change hits everything; (C) a signup spike forces scaling the ENTIRE app including idle components — wasted resources (the CNCF Netflix example); (D) modules accrete version couplings ('works only with lib v2.3') — calcifying into 'big ball of mud'. E is a MICROservices benefit, not a monolith problem.
**Sources:** <a href="https://glossary.cncf.io/monolithic-apps/" target="_blank">CNCF Glossary - Monolithic Apps</a>
**Tags:** k8s::kcna topic::microservices topic::architecture src::session

---

<!-- note:1794258268159 model:Many -->
**Domain:** Monoliths vs Microservices - microservices definition
**Question:** What is a microservices architecture?
**Options:** A. An app split into small independent services, each focused on one functionality, independently deployable and scalable, appearing as one system to the user<br>B. A single binary containing all app functionality<br>C. A networking pattern for container pods<br>D. A CI/CD pipeline stage
**Answer:** A (1) – An app split into small independent services, each focused on one functionality, independently deployable and scalable, appearing as one system to the user
**Explanation:** Microservices = app decomposed into a collection of loosely coupled services — each owns its concern, runs in its own process, deploys and scales independently, and communicates over the network (APIs/events). To the end user it's still ONE application (Netflix: auth, search, and preview streaming are separate services behind one UI). 'Micro' refers to bounded scope, not literal size — a service can be large if its domain is.
**Sources:** <a href="https://glossary.cncf.io/microservices-architecture/" target="_blank">CNCF Glossary - Microservices Architecture</a>
**Tags:** k8s::kcna topic::microservices topic::architecture src::session

---

<!-- note:1794258268160 model:Many -->
**Domain:** Monoliths vs Microservices - benefits
**Question:** Which benefits does a microservices architecture provide over a monolith? (Select all that apply)
**Options:** A. Independent deployments — small frequent releases per service<br>B. Independent scaling — scale only the busy service<br>C. Fault isolation — one service failing doesn't take down the whole app<br>D. Team autonomy — squads own services end-to-end, parallel work<br>E. Polyglot freedom — each service can use the best language/runtime<br>F. Simpler operations — fewer moving parts to run
**Answer:** A, B, C, D, E – independent releases, independent scaling, fault isolation, team autonomy, polyglot freedom
**Explanation:** The wins: (A) ship changes to one service without redeploying others — faster, safer releases; (B) scale only what's hot; (C) blast radius shrinks to one service; (D) Conway-aligned teams own their service fully and work in parallel; (E) right language/runtime per service. F is FALSE — the trade-off is the opposite: operational overhead grows by orders of magnitude (more services to deploy, monitor, debug, secure). That overhead is exactly what orchestrators like Kubernetes exist to absorb.
**Sources:** <a href="https://glossary.cncf.io/microservices-architecture/" target="_blank">CNCF Glossary - Microservices Architecture</a>
**Tags:** k8s::kcna topic::microservices topic::architecture src::session

---

<!-- note:1794258268161 model:Many -->
**Domain:** Monoliths vs Microservices - caveats
**Question:** What does adopting microservices require BEYOND rewriting code?
**Options:** A. Only a new deployment pipeline<br>B. Organizational/cultural change — teams restructured to own services end-to-end, plus orchestration to manage the operational overhead<br>C. A bigger monolith database<br>D. Nothing — it's purely a technical refactor
**Answer:** B (2) – Organizational/cultural change — teams restructured to own services end-to-end, plus orchestration to manage the operational overhead
**Explanation:** Microservices is as much an ORG design as an architecture: Conway's law — you get the system your org structure produces. Teams must own services end-to-end (build/run/scale/monitor). And the CNCF glossary's warning: microservices multiply the things you must deploy, test, and keep running 'by order of magnitude' — that's WHY Kubernetes/container orchestration exists: it makes the distributed system manageable. Premature microservices on an unproven product = wasted engineering effort.
**Sources:** <a href="https://glossary.cncf.io/microservices-architecture/" target="_blank">CNCF Glossary - Microservices Architecture</a>
**Tags:** k8s::kcna topic::microservices topic::architecture src::session

---

<!-- note:1794258268162 model:Many -->
**Domain:** Monoliths vs Microservices - when monolith fits
**Question:** When is a monolithic architecture a reasonable — even preferred — choice?
**Options:** A. Never — microservices are always better<br>B. Early in a product's lifecycle or for small teams, when the product's value isn't proven — simplest path to market, decompose later<br>C. When you need independent scaling of every feature<br>D. When services must communicate over the network
**Answer:** B (2) – Early in a product's lifecycle or for small teams, when the product's value isn't proven — simplest path to market, decompose later
**Explanation:** CNCF's nuance: a well-designed monolith is the SIMPLEST way to get an app running — early on, the operational overhead of microservices (more deployables, distributed debugging, network calls) may not pay off. If the product fails, microservice effort was wasted; if it succeeds, decompose then. Monolith does NOT mean bad code — it becomes a problem only when growth makes independent deployment/scaling necessary. 'Microservices always win' is the trap answer.
**Sources:** <a href="https://glossary.cncf.io/monolithic-apps/" target="_blank">CNCF Glossary - Monolithic Apps</a>
**Tags:** k8s::kcna topic::microservices topic::architecture src::session

---

<!-- note:1794258271292 model:Basic -->
**Front:** What does the term 'big ball of mud' describe?
**Back:** A software system — typically a monolith — that has decayed into an unstructured mass: modules without clear boundaries, pervasive tight coupling, and changes that unpredictably break unrelated parts. Coined by Foote & Yoder (1997). Monoliths drift toward this as shared code + shared DB + accreted dependencies erase module boundaries — the architectural reason microservices enforce hard service boundaries instead.
**Tags:** k8s::kcna topic::microservices topic::architecture src::session

---

<!-- note:1794258271293 model:Basic -->
**Front:** How should data stores be handled in a microservices architecture, and why does it matter?
**Back:** Each service should OWN its data — its own database/schema that no other service touches directly (database-per-service). Sharing one database between services recreates the monolith's coupling: schema changes ripple across teams, services can't evolve independently, and you can't scale or replace a service's storage alone. Services exchange data through APIs/events, not shared tables. The cost: data consistency moves from ACID transactions to eventual consistency + sagas — a real trade-off, not free.
**Tags:** k8s::kcna topic::microservices topic::architecture src::session

---

<!-- note:1794258702718 model:Many -->
**Domain:** Microservices - cross-cutting concerns
**Question:** What are 'cross-cutting concerns' in a microservices architecture?
**Options:** A. Features unique to each service's business logic<br>B. Concerns that span ALL services regardless of function — authentication, networking, logging, monitoring, tracing, TLS, retries — that every service must handle<br>C. Database schema shared across services<br>D. CI/CD pipeline stages
**Answer:** B (2) – Concerns that span ALL services regardless of function — authentication, networking, logging, monitoring, tracing, TLS, retries — that every service must handle
**Explanation:** Cross-cutting = orthogonal to business logic: authN/authZ, mTLS, logging, metrics, tracing, rate limiting, retries, service discovery. In a MONOLITH these live ONCE in shared libraries/middleware — write once, every module gets them. In MICROservices each service must implement them separately → duplication, drift, inconsistent behavior → the 'fat microservice' trap. This is THE structural cost of distribution.
**Sources:** <a href="https://glossary.cncf.io/microservices-architecture/" target="_blank">CNCF Glossary - Microservices Architecture</a>
**Tags:** k8s::kcna topic::microservices topic::architecture src::session

---

<!-- note:1794258702719 model:Many -->
**Domain:** Microservices - cross-cutting examples
**Question:** Which are typical cross-cutting concerns every microservice must handle? (Select all that apply)
**Options:** A. Authentication and authorization of callers<br>B. Encryption/TLS (mTLS) on every hop<br>C. Logging, metrics, and distributed tracing<br>D. The service's core business logic<br>E. Retry and circuit-breaking policies
**Answer:** A, B, C, E – auth, transport encryption, observability, and resilience policies
**Explanation:** Cross-cutting = infrastructure concerns EVERY service needs regardless of its job: auth (who may call me), transport security (mTLS per hop), observability (logs/metrics/traces — a request crosses N services so tracing is mandatory), resilience (retries/timeouts/breakers). D is the OPPOSITE — business logic is what makes each service unique; it's the only thing that should differ. Rule of thumb: if EVERY service needs it → cross-cutting; if only ONE service does it → business logic.
**Sources:** <a href="https://glossary.cncf.io/microservices-architecture/" target="_blank">CNCF Glossary - Microservices Architecture</a>
**Tags:** k8s::kcna topic::microservices topic::architecture src::session

---

<!-- note:1794258702720 model:Many -->
**Domain:** Microservices - fat microservice
**Question:** What is a 'fat microservice'?
**Options:** A. A service that is too large to fit on one node<br>B. A microservice bloated with duplicated cross-cutting code — auth, logging, retries, TLS — so infrastructure boilerplate outweighs its business logic<br>C. A service consuming too many CPU resources<br>D. A monolith that was split in half
**Answer:** B (2) – A microservice bloated with duplicated cross-cutting code — auth, logging, retries, TLS — so infrastructure boilerplate outweighs its business logic
**Explanation:** 'Fat microservice' = the microservice failure mode: every service re-implements the same cross-cutting concerns (auth checks, log shipping, retry logic, mTLS setup) → each carries hundreds of lines of infrastructure boilerplate around a thin slice of business logic. Result: 'micro' in name only — still hard to understand, change, and test; implementations drift apart (one service retries, another doesn't). This is precisely what sidecars/service meshes were invented to fix — move the cross-cutting code OUT of the app into a shared proxy.
**Sources:** <a href="https://glossary.cncf.io/microservices-architecture/" target="_blank">CNCF Glossary - Microservices Architecture</a>
**Tags:** k8s::kcna topic::microservices topic::architecture src::session

---

<!-- note:1794258702721 model:Many -->
**Domain:** Microservices - network reality
**Question:** Why are calls between microservices fundamentally harder than calls between modules in a monolith?
**Options:** A. Microservice calls use a different programming language<br>B. In-process function calls become network calls — adding latency, serialization, service discovery, timeouts, retries, and partial-failure modes that don't exist inside one process<br>C. Monolith modules can't communicate at all<br>D. Network calls are always faster
**Answer:** B (2) – In-process function calls become network calls — adding latency, serialization, service discovery, timeouts, retries, and partial-failure modes that don't exist inside one process
**Explanation:** Inside a monolith, module A calls module B via a FUNCTION CALL — same process, same memory, fast, and if it fails the whole app fails together (simple!). Across microservices the same call crosses a NETWORK: serialize/deserialize, DNS/service-discovery lookup, TCP+TLS handshake, latency, and NEW failure modes — timeout, connection reset, peer crashed mid-request (partial failure), version skew. Every monolith 'free' behavior becomes an explicit engineering concern: retries, circuit breakers, deadlines, idempotency.
**Sources:** <a href="https://glossary.cncf.io/microservices-architecture/" target="_blank">CNCF Glossary - Microservices Architecture</a>
**Tags:** k8s::kcna topic::microservices topic::architecture src::session

---

<!-- note:1794258702722 model:Many -->
**Domain:** Microservices - security boundaries
**Question:** How does security differ between monolith-internal calls and microservice-to-microservice calls?
**Options:** A. No difference — both are trusted equally<br>B. Monolith modules implicitly trust each other (same process); microservice calls cross trust boundaries — every hop needs authentication AND encryption (mTLS), ideally zero-trust<br>C. Microservices are more secure because they're smaller<br>D. Only the entry-point service needs security
**Answer:** B (2) – Monolith modules implicitly trust each other (same process); microservice calls cross trust boundaries — every hop needs authentication AND encryption (mTLS), ideally zero-trust
**Explanation:** Monolith: modules share a process — internal calls are implicitly trusted, no auth needed between them, security enforced once at the edge. Microservices: every service-to-service call crosses a NETWORK and a trust boundary — 'inside the cluster' is NOT 'trusted'. Defense in depth means authenticate+encrypt EVERY hop (mTLS — both sides prove identity), authorize per-call, never assume the caller is friendly just because it's another pod. This is why service meshes exist: they automate per-hop mTLS uniformly.
**Sources:** <a href="https://glossary.cncf.io/microservices-architecture/" target="_blank">CNCF Glossary - Microservices Architecture</a>
**Tags:** k8s::kcna topic::microservices topic::security src::session

---

<!-- note:1794258702723 model:Many -->
**Domain:** Microservices - mesh solution
**Question:** How do sidecar proxies / service meshes address the fat-microservice problem?
**Options:** A. They make each microservice larger<br>B. They move cross-cutting concerns (mTLS, retries, rate limits, telemetry) OUT of application code into a shared proxy (e.g. Envoy) injected alongside every service — app stays thin, behavior stays uniform<br>C. They merge microservices back into a monolith<br>D. They replace Kubernetes entirely
**Answer:** B (2) – They move cross-cutting concerns (mTLS, retries, rate limits, telemetry) OUT of application code into a shared proxy (e.g. Envoy) injected alongside every service — app stays thin, behavior stays uniform
**Explanation:** The sidecar pattern (Envoy/Istio/Linkerd): inject a proxy container next to each app — it intercepts all traffic and applies mTLS, retries, circuit breaking, rate limiting, metrics, and tracing UNIFORMLY, configured centrally via xDS. Apps write ZERO infrastructure code — no more fat microservices, no implementation drift, upgrades roll out proxy-wide without touching app images. This is the architectural answer to the cross-cutting-concern problem — and the entire reason 'service mesh' exists.
**Sources:** <a href="https://www.envoyproxy.io/docs/envoy/latest/intro/what_is_envoy" target="_blank">Envoy Docs - What is Envoy</a>
**Tags:** k8s::kcna topic::microservices topic::service-mesh src::session

---

<!-- note:1794258706134 model:Basic -->
**Front:** What is 'partial failure' and why is it unique to distributed systems like microservices?
**Back:** Partial failure = some parts of the system fail while others keep running — impossible inside a monolith (one process: it either works or crashes entirely). In microservices a network call can fail in dozens of ways while the caller stays alive: timeout, connection reset, peer crashed mid-request, slow-but-alive dependency. You can't just 'try again' naively — retries can double-load a struggling service, and a caller can't tell 'service down' from 'service slow'. Hence the entire resilience toolkit: timeouts, retries with backoff+jitter, circuit breakers, bulkheads, health checks, fallbacks.
**Tags:** k8s::kcna topic::microservices topic::resiliency src::session

---

<!-- note:1794258706135 model:Basic -->
**Front:** Why does observability become dramatically harder in microservices, and what solves it?
**Back:** A single user request in a monolith produces ONE log stream in one process. In microservices it fans out across N services on N pods on N nodes — logs scatter, and 'which service caused the 3s delay?' is unanswerable without correlation. The fix is DISTRIBUTED TRACING: a trace ID injected at the edge propagates through every hop, each service records SPANS (its slice of the request) — Jaeger/Tempo assemble the full request timeline. Plus centralized log aggregation (Fluent Bit → Loki/ES) carrying the same trace ID in every line, and RED/USE metrics per service. In microservices observability isn't optional — it's the only way to see the system.
**Tags:** k8s::kcna topic::microservices topic::observability src::session

---

<!-- note:1794259442606 model:Many -->
**Domain:** Service Mesh - definition
**Question:** What is a service mesh?
**Options:** A. A CI/CD system for deploying microservices<br>B. A dedicated, configurable infrastructure layer that manages service-to-service communication — traffic, security, observability — without application code changes<br>C. A container orchestrator like Kubernetes<br>D. A monitoring dashboard for pod metrics
**Answer:** B (2) – A dedicated, configurable infrastructure layer that manages service-to-service communication — traffic, security, observability — without application code changes
**Explanation:** A service mesh is a dedicated infrastructure layer that handles ALL service-to-service communication: traffic management, mTLS security, telemetry/observability, retries, discovery — configured centrally, applied uniformly, with ZERO application code changes. It's the architectural answer to the 'fat microservice' problem: instead of every service re-implementing auth/logging/tracing, the mesh does it for all of them. Most meshes (Istio, Linkerd) implement this via sidecar proxies + a control plane; Envoy is the most common proxy.
**Sources:** <a href="https://glossary.cncf.io/service-mesh/" target="_blank">CNCF Glossary - Service Mesh</a><br><a href="https://istio.io/latest/docs/concepts/what-is-istio/" target="_blank">Istio Docs - What is Istio</a>
**Tags:** k8s::kcna topic::service-mesh topic::architecture src::session

---

<!-- note:1794259442607 model:Many -->
**Domain:** Service Mesh - capabilities
**Question:** Which capabilities does a service mesh provide? (Select all that apply)
**Options:** A. Traffic management — routing, canary deploys, retries, timeouts<br>B. Security — automatic mTLS between all services<br>C. Observability — metrics, traces, and logs generated per hop<br>D. Replacing Prometheus/Grafana as the observability backend<br>E. Service discovery, health checking, and load balancing
**Answer:** A, B, C, E – traffic management, mTLS security, observability, and discovery/health/load-balancing
**Explanation:** The mesh provides four capability families uniformly across ALL services: (A) TRAFFIC MANAGEMENT — routing rules, canary/blue-green splits, retries, timeouts, fault injection; (B) SECURITY — automatic mTLS between every service, zero-trust identity; (C) OBSERVABILITY — golden metrics (request rate, error rate, latency), distributed traces, access logs generated at every hop automatically; (E) RESILIENCE/DISCOVERY — service discovery, health checking, load balancing, outlier detection. D is wrong — a mesh doesn't replace observability BACKENDS (Prometheus/Grafana/Jaeger still store and display the data the mesh produces).
**Sources:** <a href="https://istio.io/latest/docs/concepts/what-is-istio/" target="_blank">Istio Docs - What is Istio</a>
**Tags:** k8s::kcna topic::service-mesh topic::architecture src::session

---

<!-- note:1794259442608 model:Many -->
**Domain:** Service Mesh - architecture
**Question:** How is a service mesh architecturally divided?
**Options:** A. Data plane configures policies; control plane proxies traffic<br>B. Data plane = sidecar proxies intercepting all pod traffic; control plane = central component (e.g. Istio Pilot) that configures policies and pushes them to proxies<br>C. Control plane runs inside each pod; data plane is centralized<br>D. Both planes run only on master nodes
**Answer:** B (2) – Data plane = sidecar proxies intercepting all pod traffic; control plane = central component (e.g. Istio Pilot) that configures policies and pushes them to proxies
**Explanation:** Every mesh has TWO planes: the DATA PLANE does the actual work — a proxy (usually Envoy) runs as a sidecar in EVERY pod, intercepting all inbound/outward traffic and applying mTLS/retries/telemetry per request. The CONTROL PLANE is the brain — it watches Kubernetes services and pushes configuration (via xDS APIs) telling every proxy how to route, secure, and observe traffic. You configure the CONTROL plane; the DATA plane enforces it on every hop. This separation is why mesh changes roll out instantly without restarting apps.
**Sources:** <a href="https://istio.io/latest/docs/concepts/what-is-istio/" target="_blank">Istio Docs - What is Istio</a>
**Tags:** k8s::kcna topic::service-mesh topic::architecture src::session

---

<!-- note:1794259442609 model:Many -->
**Domain:** Service Mesh - traffic management
**Question:** What traffic-management capabilities does a service mesh enable?
**Options:** A. Only basic round-robin load balancing<br>B. Canary/blue-green deploys, percentage-based traffic splits, A/B testing, plus retries/timeouts/fault injection — all configured without code changes<br>C. Automatic scaling of pod replicas<br>D. DNS-based service discovery only
**Answer:** B (2) – Canary/blue-green deploys, percentage-based traffic splits, A/B testing, plus retries/timeouts/fault injection — all configured without code changes
**Explanation:** Traffic management is the mesh's killer feature for releases: split traffic by percentage (5% to canary, 95% to stable), route by headers/URI for A/B tests, mirror requests for shadow testing, inject artificial latency/failures to test resilience, and set retries/timeouts per route — ALL via configuration on the control plane, no app redeploys. This turns risky 'big bang' releases into gradual, observable rollouts. These are the same L7 routing powers Envoy provides — the mesh just makes them cluster-wide and declarative.
**Sources:** <a href="https://istio.io/latest/docs/concepts/what-is-istio/" target="_blank">Istio Docs - What is Istio</a>
**Tags:** k8s::kcna topic::service-mesh topic::architecture src::session

---

<!-- note:1794259442610 model:Many -->
**Domain:** Service Mesh - security
**Question:** How does a service mesh handle security between services?
**Options:** A. Optional encryption only at the cluster edge<br>B. Automatic mutual TLS (mTLS) between all services — every hop authenticated and encrypted, zero-trust by default<br>C. A web application firewall for HTTP traffic<br>D. Encryption only for external traffic
**Answer:** B (2) – Automatic mutual TLS (mTLS) between all services — every hop authenticated and encrypted, zero-trust by default
**Explanation:** The mesh's security story: STRICT mTLS by default — every service-to-service call is mutually authenticated (both sides present certificates proving identity) and encrypted, automatically, with no app code. Authorization policies ('service A may call service B on port 8080') are enforced at the proxy level. This delivers zero-trust INSIDE the cluster: 'it's another pod' no longer means 'trusted'. Certificates are issued/rotated by the control plane — apps never handle keys. Without a mesh, every service would need its own TLS/auth implementation (the fat-microservice problem).
**Sources:** <a href="https://istio.io/latest/docs/concepts/what-is-istio/" target="_blank">Istio Docs - What is Istio</a>
**Tags:** k8s::kcna topic::service-mesh topic::security src::session

---

<!-- note:1794259442611 model:Many -->
**Domain:** Service Mesh - observability
**Question:** How does a service mesh provide observability?
**Options:** A. Only if developers add instrumentation code<br>B. Automatically — the mesh generates golden metrics (request rate, errors, latency), distributed traces, and access logs at every hop without app instrumentation<br>C. Only for external-facing traffic<br>D. Through periodic health-check pings
**Answer:** B (2) – Automatically — the mesh generates golden metrics (request rate, errors, latency), distributed traces, and access logs at every hop without app instrumentation
**Explanation:** Because ALL traffic passes through the sidecar proxies, the mesh sees every request/response automatically — it generates the 'golden signals' (request rate, error rate, duration) per service pair, produces distributed traces showing exactly which hop was slow, and emits access logs — WITHOUT requiring apps to add instrumentation code. This telemetry feeds existing backends (Prometheus for metrics, Jaeger/Zipkin for traces, ELK/Loki for logs). The mesh PRODUCES the data; Prometheus/Grafana/Jaeger still STORE and visualize it — mesh ≠ observability backend.
**Sources:** <a href="https://istio.io/latest/docs/concepts/what-is-istio/" target="_blank">Istio Docs - What is Istio</a>
**Tags:** k8s::kcna topic::service-mesh topic::observability src::session

---

<!-- note:1794259442612 model:Many -->
**Domain:** Service Mesh - sidecar vs ambient
**Question:** What is the difference between sidecar and ambient (sidecarless) mesh modes?
**Options:** A. Ambient mode requires a proxy in every pod; sidecar mode uses none<br>B. Sidecarless/ambient mode moves mesh functions to the OS level via eBPF — no per-pod proxy container, less overhead and latency; sidecar mode offers finer per-pod control<br>C. Ambient mode only works without Kubernetes<br>D. Sidecar mode is always faster because proxies are local
**Answer:** B (2) – Sidecarless/ambient mode moves mesh functions to the OS level via eBPF — no per-pod proxy container, less overhead and latency; sidecar mode offers finer per-pod control
**Explanation:** Two data-plane modes exist: SIDECAR mode runs an Envoy proxy container in every pod — maximum control and per-service policy, but costs CPU/memory per pod and adds a localhost hop. AMBIENT (sidecarless) mode uses kernel eBPF to redirect traffic at the node level — no proxy containers, dramatically lower resource usage and latency, simpler at scale — but coarser-grained control (L4-focused, per-namespace rather than per-pod policies). Istio supports both; Linkerd is primarily sidecar. Trade-off: control granularity vs efficiency.
**Sources:** <a href="https://glossary.cncf.io/service-mesh/" target="_blank">CNCF Glossary - Service Mesh</a><br><a href="https://istio.io/latest/docs/overview/dataplane-modes/" target="_blank">Istio Docs - Data Plane Modes</a>
**Tags:** k8s::kcna topic::service-mesh topic::architecture src::session

---

<!-- note:1794259446783 model:Basic -->
**Front:** What is the difference between a service mesh and an Ingress controller — which traffic does each handle?
**Back:** Service mesh handles EAST-WEST traffic — pod-to-pod, service-to-service INSIDE the cluster (mTLS between services, retries, telemetry per hop). Ingress/Gateway API handles NORTH-SOUTH traffic — external client → cluster entry point (TLS termination, host/path routing to Services). They are complementary layers, not competitors: external request hits Ingress → routed to a Service → pod-to-pod hops inside are handled by the mesh. Rule of thumb: Ingress = the front door; mesh = the building's interior hallways.
**Tags:** k8s::kcna topic::service-mesh topic::ingress src::session

---

<!-- note:1794260586107 model:Many -->
**Domain:** Istio - overview
**Question:** What is Istio?
**Options:** A. A Kubernetes add-on for pod autoscaling<br>B. A free, open-source service mesh (CNCF graduated, founded 2016 by Google/IBM/Lyft) that secures, connects, and monitors services using Envoy-based sidecar proxies<br>C. A container runtime for running pods<br>D. A CI/CD pipeline for microservice deployments
**Answer:** B (2) – A free, open-source service mesh (CNCF graduated, founded 2016 by Google/IBM/Lyft) that secures, connects, and monitors services using Envoy-based sidecar proxies
**Explanation:** Istio = the most widely used open-source service mesh (Apache 2.0, CNCF graduated project, founded 2016 by Google, IBM and Lyft). It provides zero-trust security (automatic mTLS), traffic management (canary deploys, traffic splits), and observability (metrics/traces/logs) for microservices — WITHOUT application code changes. Architecture: Envoy-based sidecar proxies form the DATA plane in every pod; the istiod control plane configures them. Two modes: sidecar (per-pod proxy) and ambient (eBPF/ztunnel, sidecarless).
**Sources:** <a href="https://istio.io/latest/docs/concepts/what-is-istio/" target="_blank">Istio Docs - What is Istio</a>
**Tags:** k8s::kcna topic::istio topic::service-mesh src::session

---

<!-- note:1794260586108 model:Many -->
**Domain:** Istio - pod components
**Question:** Which components are injected into a pod when Istio sidecar mode is enabled? (Select all that apply)
**Options:** A. The application container(s)<br>B. istio-proxy — an Envoy sidecar intercepting all traffic<br>C. istiod — the control plane<br>D. istio-init or CNI rules redirecting traffic into the proxy
**Answer:** A, B, D – app container(s), istio-proxy (Envoy), and istio-init/CNI traffic redirection
**Explanation:** Sidecar injection adds to EVERY meshed pod: (A) the app container(s) themselves — untouched; (B) istio-proxy — the Envoy sidecar that intercepts all traffic; (D) an init mechanism — traditionally an istio-init container running iptables rules to redirect pod traffic into Envoy (newer installs use the Istio CNI node agent instead). C is wrong — istiod is NOT in the pod; it runs centralized in istio-system. The pod-level components are app + proxy + init/redirect.
**Sources:** <a href="https://istio.io/latest/docs/ops/deployment/architecture/" target="_blank">Istio Docs - Architecture</a>
**Tags:** k8s::kcna topic::istio topic::service-mesh src::session

---

<!-- note:1794260586109 model:Many -->
**Domain:** Istio - istio-proxy role
**Question:** What is the role of istio-proxy in an Istio mesh?
**Options:** A. It configures routing rules for the whole mesh<br>B. istio-proxy (Envoy) mediates ALL inbound/outbound pod traffic — the only Istio component that touches data-plane traffic<br>C. It generates the mTLS certificates for services<br>D. It validates Istio configuration files
**Answer:** B (2) – istio-proxy (Envoy) mediates ALL inbound/outbound pod traffic — the only Istio component that touches data-plane traffic
**Explanation:** istio-proxy is Istio's EXTENDED Envoy — a high-performance C++ proxy deployed as a sidecar in every pod. It is the ONLY Istio component that interacts with actual data-plane traffic: it intercepts all inbound and outbound requests and applies L7 features — dynamic service discovery, load balancing, TLS termination/origination, circuit breakers, health checks, %-based traffic splits, fault injection, rich metrics. Because it sits in the traffic path, it can enforce policies and emit telemetry WITHOUT the app knowing.
**Sources:** <a href="https://istio.io/latest/docs/ops/deployment/architecture/" target="_blank">Istio Docs - Architecture</a>
**Tags:** k8s::kcna topic::istio topic::service-mesh src::session

---

<!-- note:1794260586110 model:Many -->
**Domain:** Istio - istio-agent role
**Question:** What does the istio-agent (pilot-agent) do in a meshed pod?
**Options:** A. It intercepts and forwards all pod network traffic<br>B. The per-pod agent (pilot-agent) that bootstraps Envoy, proxies xDS configuration from istiod to Envoy, and serves SDS certificates/secrets<br>C. It is the centralized control plane for the mesh<br>D. It validates Kubernetes pod specifications
**Answer:** B (2) – The per-pod agent (pilot-agent) that bootstraps Envoy, proxies xDS configuration from istiod to Envoy, and serves SDS certificates/secrets
**Explanation:** The istio-agent (pilot-agent process, PID 1 inside the istio-proxy container) is the pod's control-plane CLIENT: it connects to istiod over mTLS, receives xDS configuration (routes, clusters, listeners) and SDS secrets (workload certs), and serves them to the local Envoy over localhost. It also supervises/restarts Envoy if it crashes, handles DNS capture for mesh services, and translates k8s readiness probes. Separation of concerns: the AGENT talks to the control plane; ENVOY talks to the traffic.
**Sources:** <a href="https://istio.io/latest/docs/ops/deployment/architecture/" target="_blank">Istio Docs - Architecture</a>
**Tags:** k8s::kcna topic::istio topic::service-mesh src::session

---

<!-- note:1794260586111 model:Many -->
**Domain:** Istio - control plane history
**Question:** What were Istio's original control-plane components before istiod?
**Options:** A. Pilot, Proxy, and Gateway<br>B. Pilot (service discovery + Envoy config generation), Citadel (certificate authority for mTLS), and Galley (config validation) — merged into the single istiod daemon in Istio 1.5<br>C. Envoy, Linkerd, and Consul<br>D. Citadel, Pilot, and Kubernetes
**Answer:** B (2) – Pilot (service discovery + Envoy config generation), Citadel (certificate authority for mTLS), and Galley (config validation) — merged into the single istiod daemon in Istio 1.5
**Explanation:** Early Istio (pre-1.5, 2020) ran THREE control-plane components: PILOT = service discovery + translated routing rules into Envoy config; CITADEL = the Certificate Authority generating mTLS workload certs; GALLEY = validated and distributed configuration. They were merged into ONE daemon, ISTIOD, to simplify deployment and ops — same three jobs, one process. Exam trap: 'istiod' is not a new component, it's the consolidation of Pilot+Citadel+Galley. istiod runs centralized (istio-system namespace), NEVER inside app pods.
**Sources:** <a href="https://istio.io/latest/docs/ops/deployment/architecture/" target="_blank">Istio Docs - Architecture</a>
**Tags:** k8s::kcna topic::istio topic::service-mesh src::session

---

<!-- note:1794260586112 model:Many -->
**Domain:** Istio - component roles
**Question:** Which Istio component generates the certificates used for mutual TLS between services?
**Options:** A. istio-proxy<br>B. istiod — it acts as the mesh Certificate Authority, generating the workload certificates used for mTLS<br>C. istio-agent<br>D. Galley
**Answer:** B (2) – istiod — it acts as the mesh Certificate Authority, generating the workload certificates used for mTLS
**Explanation:** Component-function map: mTLS workload CERTIFICATES → istiod (the old Citadel function — istiod IS the CA); Envoy-specific routing config → istiod (old Pilot — translates high-level rules into xDS config for proxies); actual traffic forwarding → istio-proxy/Envoy (data plane); config+secret DELIVERY to the local proxy → istio-agent/pilot-agent; config VALIDATION → istiod (old Galley). The classic exam trap: istiod never touches traffic — it only configures the proxies that do.
**Sources:** <a href="https://istio.io/latest/docs/ops/deployment/architecture/" target="_blank">Istio Docs - Architecture</a>
**Tags:** k8s::kcna topic::istio topic::service-mesh src::session

---

<!-- note:1794260591453 model:Basic -->
**Front:** What are istiod's responsibilities in the Istio control plane?
**Back:** istiod is the single control-plane daemon (merger of Pilot+Citadel+Galley) providing four jobs: (1) SERVICE DISCOVERY — watches Kubernetes services/endpoints and abstracts platform differences into a standard format; (2) CONFIG DISTRIBUTION — converts high-level routing rules into Envoy-specific xDS config and pushes it to every sidecar at runtime; (3) CERTIFICATE MANAGEMENT — acts as the mesh Certificate Authority, generating/rotating workload certs for mTLS; (4) CONFIG VALIDATION — accepts/rejects config before it reaches proxies. It NEVER touches data-plane traffic — it only configures the proxies that do.
**Tags:** k8s::kcna topic::istio topic::service-mesh src::session

---

<!-- note:1794260591454 model:Basic -->
**Front:** Why does an Istio pod have both an istio-agent AND an istio-proxy (Envoy) — what does each do?
**Back:** They split control-plane vs data-plane duties inside the pod: istio-agent (pilot-agent) is the pod's CLIENT to istiod — it fetches xDS config and SDS certificates over mTLS and serves them to the local Envoy on localhost, plus supervises Envoy's lifecycle. istio-proxy IS the Envoy data-plane proxy — it intercepts all pod traffic and enforces the policies/telemetry it receives. Think: agent = the messenger between istiod and the proxy; proxy = the worker actually handling traffic. Envoy could not do the agent's job (it has no control-plane credentials) and the agent cannot proxy traffic.
**Tags:** k8s::kcna topic::istio topic::service-mesh src::session

---
