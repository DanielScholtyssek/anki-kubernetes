# KCNA - Kubernetes and Cloud Native Associate — Cloud Native Application Delivery

> Deck: `KCNA - Kubernetes and Cloud Native Associate` · Group: `Cloud Native Application Delivery` · Notes: 14 · Models: Many

<!-- note:1793915795947 model:Many -->
**Domain:** Helm - values
**Question:** Which Helm option overrides chart values from the command line?
**Options:** A. <code>--values</code><br>B. <code>--namespace</code><br>C. <code>--kubeconfig</code><br>D. <code>--set</code>
**Answer:** D – <code>--set</code> key=value overrides Helm values inline
**Explanation:** <code>--set</code> overrides individual chart values inline as key=value pairs — repeatable and comma-separable (<code>helm install web ./chart --set image.tag=2.0 --set replicas=3</code>). Precedence: <code>--set</code> beats -f/<code>--values</code> files, which beat the chart's values.yaml defaults. The distractors do unrelated things: <code>--values</code>/-f supplies a whole YAML file of overrides (not inline), <code>--namespace</code> picks the install namespace, <code>--kubeconfig</code> points at a cluster credentials file. For strings that look like numbers or file-sourced values there are <code>--set-string</code> and <code>--set-file</code>.
**Sources:** <a href="https://helm.sh/docs/intro/using_helm/" target="_blank">Helm Docs - Using Helm</a>
**Tags:** k8s::kcna src::session topic::helm topic::packaging

---

<!-- note:1793919187035 model:Many -->
**Domain:** Helm - install flags
**Question:** What is the purpose of Helm's --atomic flag?
**Options:** A. Dry-run only<br>B. Roll back automatically on failure<br>C. Create CRDs<br>D. Render templates only
**Answer:** B (2) – roll back automatically on failure
**Explanation:** --atomic makes helm install/upgrade all-or-nothing: if any resource fails to become ready, Helm rolls the release back to its previous revision instead of leaving a half-installed release behind. It builds on --wait (Helm waits for readiness) plus automatic rollback — without it a failed upgrade can strand the cluster in a mixed old/new state. The distractors describe other flags: --dry-run only renders templates client-side without touching the cluster, and CRDs come from the chart's crds/ directory (installed before templates, never templated).
**Sources:** <a href="https://helm.sh/docs/intro/using_helm/" target="_blank">Helm Docs - Using Helm</a>
**Tags:** k8s::kcna src::session topic::helm topic::packaging

---

<!-- note:1794080037260 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** Which principle is central to the GitOps methodology for application and infrastructure deployment?
**Options:** A. Using imperative scripts stored in Git<br>B. Managing only stateless applications via Git<br>C. Treating Git as the single source of truth for desired state<br>D. Requiring manual approval for all Git commits<br>E. Using Git LFS for storing container images
**Answer:** C – Treating Git as the single source of truth for desired state
**Explanation:** GitOps emphasizes a declarative approach where the entire<br>desired state of the system (applications, infrastructure) is described in<br>Git, and an automated process ensures the live environment converges to<br>this state.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037261 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** In a CI/CD pipeline for a cloud native application, what is the typical output of the "Continuous Integration" (CI) phase?
**Options:** A. A running application in production<br>B. A new Kubernetes cluster provisioned<br>C. A tested and versioned container image/artifact<br>D. A detailed cost analysis report<br>E. A set of user stories for the next sprint
**Answer:** C – A tested and versioned container image/artifact
**Explanation:** The CI phase focuses on building the application, running automated tests, and producing a reliable, versioned artifact (often<br>a container image) that is ready for deployment.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037262 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** What is the <b>primary </b>benefit of implementing CI/CD pipelines for application delivery?
**Options:** A. It eliminates the need for testing<br>B. It reduces infrastructure costs significantly<br>C. It enables faster, more reliable software releases<br>D. It automatically writes application code<br>E. It replaces the need for version control systems
**Answer:** C – It enables faster, more reliable software releases
**Explanation:** Explanation: CI/CD automates the build, test, and deployment processes, leading to increased release velocity, improved code quality through<br>automated testing, and more consistent deployments.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037263 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** What is a key advantage of using GitOps for managing Kubernetes deployments compared to traditional CI/CD push-based deployments?
**Options:** A. GitOps pipelines are significantly faster to execute.<br>B. GitOps eliminates the need for container registries.<br>C. GitOps enhances security by reducing direct cluster access for CI.<br>D. GitOps does not require YAML manifests for resources.<br>E. GitOps is only suitable for small-scale deployments.
**Answer:** C – GitOps enhances security by reducing direct cluster access for CI.
**Explanation:** In GitOps, the CI system typically pushes an image to a<br>registry and updates a Git repo. An agent inside the cluster pulls changes<br>from Git, reducing the CI system’s need for direct cluster credentials and<br>providing a stronger security posture.<br>Domain: Cloud
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037264 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** Which of these is a core component of a "Continuous Delivery" pipeline but <b>NOT </b>necessarily "Continuous Deployment"?
**Options:** A. Automated building of code into an artifact.<br>B. Automated execution of unit and integration tests.<br>C. Automated deployment to a staging/QA environment.<br>D. Automated deployment to the production environment.<br>E. Manual approval gate before production deployment.
**Answer:** E – Manual approval gate before production deployment.
**Explanation:** Continuous Delivery ensures every validated change is releasable to production, often with a manual approval step. Continuous<br>Deployment automates the release to production without manual intervention if all prior stages pass. Both include A, B, C.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037265 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** What is the practice of using Git repositories as the single source of truth for defining and managing infrastructure and applications?
**Options:** A. CI/CD<br>B. DevOps<br>C. GitOps<br>D. Infrastructure as Code (IaC)
**Answer:** C – GitOps
**Explanation:** GitOps leverages Git’s features (versioning, history, PRs) to manage infrastructure and application deployment declaratively.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037266 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** Which core principle differentiates GitOps from general Infrastructure as Code (IaC)?
**Options:** A. Using code for infra config<br>B. Automating infrastructure tests<br>C. Using Git as the source of truth<br>D. Manual deployment approval
**Answer:** C – Using Git as the source of truth
**Explanation:** While IaC uses code, GitOps specifically mandates Git as the declarative source of truth and uses agents to enforce that state.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037267 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** What does ”CI” stand for in the context of application delivery?
**Options:** A. Continuous Integration<br>B. Cluster Infrastructure<br>C. Container Interface<br>D. Cloud Instance
**Answer:** A – Continuous Integration
**Explanation:** Continuous Integration involves frequently merging code changes into a central repository, followed by automated builds and tests.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037268 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** What does ”CD” stand for in CI/CD?
**Options:** A. Container Deployment<br>B. Continuous Delivery/Deployment<br>C. Cluster Discovery<br>D. Centralized Dashboard
**Answer:** B – Continuous Delivery/Deployment
**Explanation:** Continuous Delivery ensures code changes can be released quickly, while Continuous Deployment automatically deploys them to production.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037269 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** Which stage in a typical CI/CD pipeline for Kubernetes usually involves creating a container image?
**Options:** A. Testing<br>B. Building<br>C. Deployment<br>D. Monitoring
**Answer:** B – Building
**Explanation:** The build stage compiles code (if necessary) and packages the application and its dependencies into a container image (e.g., Docker).
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037270 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** Which tool is commonly used in CI/CD pipelines to automate the build, test, and deployment processes?
**Options:** A. Kubernetes<br>B. Docker<br>C. Jenkins / GitLab CI / GitHub Actions<br>D. Prometheus
**Answer:** C – Jenkins / GitLab CI / GitHub Actions
**Explanation:** Tools like Jenkins, GitLab CI, GitHub Actions, Argo CD, Flux etc., orchestrate the steps within a CI/CD pipeline.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037271 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** What is <b>the primary goal</b> of Application Delivery in a cloud native context?
**Options:** A. To secure the cluster<br>B. To monitor resource usage<br>C. To reliably deploy manage apps<br>D. To provision infrastructure
**Answer:** C – To reliably deploy manage apps
**Explanation:** Application delivery focuses on the processes and tools used to get applications running reliably and efficiently in the environment.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794082905876 model:Many -->
**Domain:** Application Delivery - queue load leveling
**Question:** A microservice application is experiencing high latency during traffic spikes. The team identifies that the database connection pool is exhausted. They want to implement a pattern that helps decouple the microservice from direct database connections and smooth out traffic bursts. Which design pattern should they apply?
**Options:** A. Bulkhead pattern<br>B. Circuit Breaker pattern<br>C. Queue-based Load Leveling pattern<br>D. Retry pattern
**Answer:** C (3) – Queue-based Load Leveling pattern
**Explanation:** Queue-based Load Leveling inserts a message queue (RabbitMQ, SQS, Kafka, etc.) between producer and consumer: requests enqueue instantly and a consumer drains them at a rate the database can sustain — bursts get absorbed as queue depth instead of exhausted connection pools. This is a LOAD-SMOOTHING pattern, not a failure-handling one: Circuit breaker stops calls to FAILING deps, Retry re-attempts failures, Bulkhead partitions resources — none decouple the caller or buffer bursts.
**Sources:** <a href="https://learn.microsoft.com/en-us/azure/architecture/patterns/queue-based-load-leveling" target="_blank">Microsoft Azure Architecture - Queue-Based Load Leveling</a>
**Tags:** k8s::kcna topic::application-delivery topic::messaging src::session

---

<!-- note:1794082905877 model:Many -->
**Domain:** Application Delivery - load leveling mechanism
**Question:** How does Queue-based Load Leveling actually smooth out traffic bursts?
**Options:** A. The queue retries failed database writes automatically<br>B. Producers enqueue requests instantly; a consumer processes them at a controlled rate, so bursts become queue depth<br>C. The queue load-balances requests across database replicas<br>D. Producers block until the database has free connections
**Answer:** B (2) – Producers enqueue requests instantly; a consumer processes them at a controlled rate, so bursts become queue depth
**Explanation:** Mechanics: producer publishes to queue → queue buffers → consumer(s) pull work at whatever rate the downstream (DB) can handle. Spike = deeper queue, not more concurrent DB connections. Trade-offs: requests become ASYNC (higher latency per request, but bounded); needs a queue tech (RabbitMQ/SQS/Kafka/NATS); consumer count controls throughput. Sibling patterns in the same family: Throttling (reject/slow requests at the edge), Autoscaling (add replicas — helps compute-bound, not a fixed pool like DB connections).
**Sources:** <a href="https://learn.microsoft.com/en-us/azure/architecture/patterns/queue-based-load-leveling" target="_blank">Microsoft Azure Architecture - Queue-Based Load Leveling</a>
**Tags:** k8s::kcna topic::application-delivery topic::messaging src::session

---

<!-- note:1794096372824 model:Many -->
**Domain:** Application Delivery - ingress vs service
**Question:** What problem does Ingress solve that exposing each Service via type LoadBalancer cannot?
**Options:** A. Pod-to-pod communication across nodes<br>B. Giving every Service its own L4 load balancer — expensive at scale<br>C. A single L7 entry point routing HTTP/HTTPS by host and path, with TLS termination — one LB instead of many<br>D. Encrypting traffic between pods inside the cluster
**Answer:** C (3) – A single L7 entry point routing HTTP/HTTPS by host and path, with TLS termination — one LB instead of many
**Explanation:** type: LoadBalancer on every Service = one cloud LB (cost + IP) PER service — doesn't scale. Ingress is a Layer-7 (HTTP/HTTPS only!) reverse proxy: ONE exposed endpoint routes to many Services by Host header and URL path, terminates TLS, does name-based virtual hosting. Services still handle L4 pod selection — ingress sits in front of them. Rule of thumb: Service LB/NodePort for non-HTTP protocols or exposing a single service; Ingress when many HTTP services share one entry point.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/ingress/" target="_blank">Kubernetes Docs - Ingress</a>
**Tags:** k8s::kcna topic::networking topic::ingress src::session

---

<!-- note:1794096372825 model:Many -->
**Domain:** Application Delivery - ingress controller
**Question:** What actually implements the routing rules defined in an Ingress resource?
**Options:** A. kube-proxy — it programs the iptables rules for ingress<br>B. CoreDNS — it resolves ingress hostnames<br>C. An Ingress controller — a third-party reverse proxy (nginx, Traefik, HAProxy, AWS ALB…) deployed in the cluster<br>D. kube-apiserver — it proxies requests to backend services
**Answer:** C (3) – An Ingress controller — a third-party reverse proxy (nginx, Traefik, HAProxy, AWS ALB…) deployed in the cluster
**Explanation:** The Ingress resource is ONLY config — Kubernetes ships no built-in implementation. You must deploy an ingress controller (nginx-ingress, Traefik, HAProxy Ingress, AWS Load Balancer Controller, etc.); it watches Ingress resources and programs its proxy/LB accordingly. Exam trap: Ingress ≠ the load balancer itself — it's the API object describing desired routing; the controller is the thing that implements it.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/ingress/" target="_blank">Kubernetes Docs - Ingress</a>
**Tags:** k8s::kcna topic::networking topic::ingress src::session

---

<!-- note:1794096372826 model:Many -->
**Domain:** Application Delivery - ingress controller deployment
**Question:** To manually deploy an nginx ingress controller you need which objects? (Select all that apply)
**Options:** A. Deployment — runs the controller pods<br>B. ConfigMap — holds controller args/configuration<br>C. Service (type NodePort or LoadBalancer) — exposes the controller to traffic<br>D. ServiceAccount + RBAC — permissions to watch Ingress/Services/Endpoints<br>E. PersistentVolumeClaim — required storage for routing rules<br>F. Ingress resource — defines the actual host/path routing rules
**Answer:** A, B, C, D – Deployment, ConfigMap, Service, ServiceAccount/RBAC
**Explanation:** The classic four-object pattern for a manual controller deploy: Deployment runs the controller pods; ConfigMap carries args/config; Service (NodePort or LoadBalancer) is the ONE exposed endpoint — the single LB you actually pay for; ServiceAccount+RBAC grant it permission to watch Ingresses/Services/Endpoints and update status. NOT required: a PVC (routing state lives in the Ingress resources/etcd, not controller storage). The Ingress resource itself comes AFTER — it defines routing rules, not the controller.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/" target="_blank">Kubernetes Docs - Ingress Controllers</a>
**Tags:** k8s::kcna topic::networking topic::ingress src::session

---

<!-- note:1794096372827 model:Many -->
**Domain:** Application Delivery - ingress path types
**Question:** An Ingress rule has path /api with pathType Prefix. Which requests match?
**Options:** A. Only exactly /api<br>B. /api, /api/, /api/v1/users — but NOT /apiserver<br>C. Any path containing the string 'api' anywhere<br>D. /api and /apiserver both
**Answer:** B (2) – /api, /api/, /api/v1/users — but NOT /apiserver
**Explanation:** Prefix matching is ELEMENT-WISE on '/'-separated segments and case-sensitive: /api matches /api/v1/users but NOT /apiserver (last segment differs) and NOT /API (case). Exact = full path identical, case-sensitive (/foo ≠ /foo/). ImplementationSpecific = up to the controller (may behave as Prefix or Exact). When multiple rules match: longest path wins; on tie, Exact beats Prefix. No host in a rule = matches ALL hosts.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/ingress/" target="_blank">Kubernetes Docs - Ingress</a>
**Tags:** k8s::kcna topic::networking topic::ingress src::session

---

<!-- note:1794096372828 model:Many -->
**Domain:** Application Delivery - ingress TLS
**Question:** Where does TLS terminate for traffic passing through an Ingress?
**Options:** A. At the backend pod — end-to-end encryption<br>B. At the ingress controller — client↔LB leg is TLS, controller→Service→pods is plaintext HTTP<br>C. At kube-proxy on each node<br>D. TLS is not supported by Ingress at all
**Answer:** B (2) – At the ingress controller — client↔LB leg is TLS, controller→Service→pods is plaintext HTTP
**Explanation:** Ingress supports ONE TLS port (443) and assumes TERMINATION at the ingress point: spec.tls references a Secret of type kubernetes.io/tls containing tls.crt + tls.key; the cert CN/FQDN must match the rule's host. Multiple TLS hosts multiplex on 443 via SNI. Backend traffic controller→pods is PLAINTEXT — TLS does not extend to pods (end-to-end encryption needs service mesh mTLS, not Ingress). Wildcard/default rules can't do TLS — certs must match specific hosts.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/ingress/" target="_blank">Kubernetes Docs - Ingress</a>
**Tags:** k8s::kcna topic::networking topic::ingress topic::tls src::session

---

<!-- note:1794096372829 model:Many -->
**Domain:** Application Delivery - ingress class
**Question:** How does an Ingress resource specify which ingress controller should implement it?
**Options:** A. Via a kubernetes.io/ingress.class annotation only — the modern way<br>B. Via spec.ingressClassName referencing an IngressClass resource, whose spec.controller names the controller<br>C. Via the controller's namespace — it only sees Ingresses in its own namespace<br>D. Automatically — the first deployed controller takes all Ingresses
**Answer:** B (2) – Via spec.ingressClassName referencing an IngressClass resource, whose spec.controller names the controller
**Explanation:** spec.ingressClassName → IngressClass resource → spec.controller (e.g. k8s.io/ingress-nginx) tells WHICH implementation handles the Ingress. IngressClass is cluster-scoped and can carry parameters (Cluster or Namespace scope) for controller config — e.g. which LB algorithm to use. The old kubernetes.io/ingress.class annotation is DEPRECATED. A default class is set via annotation ingressclass.kubernetes.io/is-default-class: "true" — at most ONE default allowed, otherwise the admission controller rejects Ingresses without ingressClassName.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/ingress/" target="_blank">Kubernetes Docs - Ingress</a>
**Tags:** k8s::kcna topic::networking topic::ingress src::session

---

<!-- note:1794096372830 model:Many -->
**Domain:** Application Delivery - ingress wildcards
**Question:** Which hosts does an Ingress rule with host '*.foo.com' match?
**Options:** A. foo.com and bar.foo.com<br>B. bar.foo.com only — one DNS label; NOT foo.com itself, NOT baz.bar.foo.com<br>C. Any host ending in .foo.com at any depth<br>D. All hosts in the cluster
**Answer:** B (2) – bar.foo.com only — one DNS label; NOT foo.com itself, NOT baz.bar.foo.com
**Explanation:** Wildcard host *.foo.com covers exactly ONE DNS label: matches bar.foo.com but NOT foo.com (the wildcard needs that extra label to exist) and NOT baz.bar.foo.com (two labels deep — wildcard doesn't recurse). Precise hosts like foo.bar.com require exact Host header match. A rule with NO host field matches ALL hosts — that's the default/fallback route.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/ingress/" target="_blank">Kubernetes Docs - Ingress</a>
**Tags:** k8s::kcna topic::networking topic::ingress src::session

---

<!-- note:1794096372831 model:Many -->
**Domain:** Application Delivery - gateway api overview
**Question:** What is the Gateway API in Kubernetes?
**Options:** A. A replacement Service type for Layer-4 load balancing<br>B. The next-generation, role-oriented API for L4/L7 traffic routing — successor to Ingress, covering north-south ingress AND east-west mesh<br>C. A mandatory component installed by kubeadm<br>D. An API for managing TLS certificates
**Answer:** B (2) – The next-generation, role-oriented API for L4/L7 traffic routing — successor to Ingress, covering north-south ingress AND east-west mesh
**Explanation:** Gateway API (kubernetes-sigs project, graduated to official Kubernetes project) is the next-gen standard for service networking: Gateway/GatewayClass/HTTPRoute resources. Design goals: ROLE-ORIENTED (infra provider / cluster operator / app developer personas), portable across implementations, EXPRESSIVE (header matching, traffic weights — no annotations needed), extensible. Key fact: Kubernetes docs now RECOMMEND Gateway over Ingress — the Ingress API is GA but NO LONGER BEING DEVELOPED. Gateway+GatewayClass+HTTPRoute reached Standard channel (stable) in v0.5.0; GAMMA service-mesh support GA in v1.1.0.
**Sources:** <a href="https://gateway-api.sigs.k8s.io/" target="_blank">Gateway API</a>
**Tags:** k8s::kcna topic::networking topic::gateway-api src::session

---

<!-- note:1794096372832 model:Many -->
**Domain:** Application Delivery - gateway api resources
**Question:** In Gateway API, which resource holds the actual routing rules (hostnames, paths, backends)?
**Options:** A. Gateway — it contains all route rules<br>B. GatewayClass — it defines routing logic per controller type<br>C. HTTPRoute (or GRPCRoute etc.) — route resources attach to Gateways and define matches/backends<br>D. Ingress — Gateway API reuses Ingress rules
**Answer:** C (3) – HTTPRoute (or GRPCRoute etc.) — route resources attach to Gateways and define matches/backends
**Explanation:** Role-oriented split of responsibilities: GatewayClass = the KIND of controller implementation (like IngressClass — 'nginx', 'istio'); Gateway = an instance/point of access bound to a GatewayClass (holds the LB VIP); HTTPRoute/GRPCRoute/TCPRoute/TLSRoute = the routing RULES attached to a Gateway (match host/path/headers → backend Service or other typed backend). The separation lets multiple teams share one Gateway safely — routes attach via labels/sectionName without coordinating on the Gateway object itself. For service mesh (GAMMA), routes attach directly to Services instead.
**Sources:** <a href="https://gateway-api.sigs.k8s.io/" target="_blank">Gateway API</a>
**Tags:** k8s::kcna topic::networking topic::gateway-api src::session

---

<!-- note:1794096372833 model:Many -->
**Domain:** Application Delivery - gateway vs ingress
**Question:** Which capability does Gateway API provide that Ingress could only achieve via custom annotations?
**Options:** A. Path-based routing<br>B. TLS termination<br>C. Header/method/query matching and traffic weighting across backends<br>D. Hostname-based virtual hosting
**Answer:** C (3) – Header/method/query matching and traffic weighting across backends
**Explanation:** Native Ingress does host+path→service ONLY — header matching, HTTP method matching, query param matching, and traffic splitting/weights required controller-specific annotations (non-portable, breaks if you switch controllers). Gateway API bakes all of these into typed Route resources portably across implementations. Path routing, TLS termination, and hostname vhosts are native to BOTH — those aren't differentiators.
**Sources:** <a href="https://gateway-api.sigs.k8s.io/" target="_blank">Gateway API</a>
**Tags:** k8s::kcna topic::networking topic::gateway-api src::session

---

<!-- note:1794096386555 model:Cloze -->
**Text:** Minimal Ingress manifest — the routing skeleton:<br><br>apiVersion: networking.k8s.io/v1<br>kind: {{c1::Ingress}}<br>metadata:<br>  name: {{c2::my-ingress}}<br>spec:<br>  ingressClassName: {{c3::nginx}}<br>  rules:<br>  - host: {{c4::app.example.com}}<br>    http:<br>      paths:<br>      - path: {{c5::/api}}<br>        pathType: {{c6::Prefix}}<br>        backend:<br>          service:<br>            name: {{c7::my-service}}<br>            port:<br>              number: {{c8::80}}
**Back Extra:** Fill-ins: metadata.name = any name for the object; ingressClassName picks the controller (must match an IngressClass's spec.controller, e.g. k8s.io/ingress-nginx — omit only if a default class exists); host = the DNS name clients use (must match cert CN if TLS); path+pathType = Exact|Prefix|ImplementationSpecific; backend.service.name/port = the target Service and its port (name or number). spec.tls adds a secretName referencing a kubernetes.io/tls Secret (tls.crt+tls.key) whose hosts must match rule hosts. spec.defaultBackend catches requests matching no rule.
**Tags:** k8s::kcna topic::networking topic::ingress src::session

---
