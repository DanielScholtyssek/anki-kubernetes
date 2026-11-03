# Kubernetes for Beginners — services

> Deck: `Kubernetes for Beginners` · Group: `services` · Notes: 10 · Models: Basic, Basic (and reversed card), Cloze, Many

<!-- note:1793737589629 model:Basic -->
**Front:** What problem does a Kubernetes Service solve, and how does it enable loose coupling?
**Back:** Pods are ephemeral — they're created, destroyed and rescheduled, so their IPs churn constantly. A Service puts a STABLE virtual IP and DNS name in front of a selector-matched set of pods: clients talk to one fixed endpoint while the backend pods come and go. This decouples microservices — a frontend never tracks pod IPs — and the Service load-balances across whichever pods match its selector right now.
**Tags:** k8s::beginners topic::networking topic::services src::session

---

<!-- note:1793737589630 model:Basic -->
**Front:** In a Service manifest, what is the difference between <code>port</code>, <code>targetPort</code> and <code>nodePort</code>?
**Back:** Three different port roles: <code>port</code> — the port the Service itself listens on (what clients connect to, on the clusterIP). <code>targetPort</code> — the port on the backend pods traffic is forwarded to (defaults to the same value as <code>port</code>; can also be a named container port). <code>nodePort</code> — only for type NodePort: the static port opened on every node's IP (default range 30000-32767) that outside traffic hits.
**Tags:** k8s::beginners topic::networking topic::services src::session

---

<!-- note:1793737589631 model:Basic -->
**Front:** When you create a NodePort Service, what happens on the cluster's nodes?
**Back:** The same port number is opened on EVERY node in the cluster — each node proxies <code>nodePort</code> into the Service, which forwards to a ready backend pod (which may live on a different node). So you can reach the app from outside via <code>&lt;any-node-IP&gt;:&lt;nodePort&gt;</code> — no single node is special. A NodePort Service also gets a clusterIP automatically; it builds on ClusterIP.
**Tags:** k8s::beginners topic::networking topic::services src::session

---

<!-- note:1793737589638 model:Basic (and reversed card) -->
**Front:** What does the ClusterIP Service type do?
**Back:** The default Service type — assigns a stable virtual IP reachable only INSIDE the cluster (from the Service CIDR, e.g. 10.96.0.0/12). Use it for internal microservice-to-microservice communication; outside access would need Ingress/Gateway or a different type.
**Tags:** k8s::beginners topic::networking topic::services src::session

---

<!-- note:1793737589639 model:Basic (and reversed card) -->
**Front:** What does the NodePort Service type do?
**Back:** Builds on ClusterIP — additionally opens the same static port (the nodePort, 30000-32767 by default) on EVERY node's IP. External traffic to <code>&lt;any-node-IP&gt;:&lt;nodePort&gt;</code> is forwarded to the Service and on to a ready pod. It's the simplest built-in way to expose an app outside the cluster.
**Tags:** k8s::beginners topic::networking topic::services src::session

---

<!-- note:1793737589640 model:Basic (and reversed card) -->
**Front:** What does the LoadBalancer Service type do?
**Back:** Builds on NodePort+ClusterIP — asks the environment (cloud provider integration, or MetalLB on bare-metal) for an external load balancer with a public IP. Traffic flows: external client → cloud LB → node's nodePort → Service → pod. It's the standard way to get a real public IP per service; without LB support the Service stays pending.
**Tags:** k8s::beginners topic::networking topic::services src::session

---

<!-- note:1793737589683 model:Cloze -->
**Text:** Service manifest (NodePort):<br><br><code>apiVersion: {{c1::v1}}<br>kind: {{c2::Service}}<br>metadata:<br>&nbsp;&nbsp;name: web-svc<br>spec:<br>&nbsp;&nbsp;type: {{c3::NodePort}}<br>&nbsp;&nbsp;{{c4::selector}}:<br>&nbsp;&nbsp;&nbsp;&nbsp;app: web<br>&nbsp;&nbsp;ports:<br>&nbsp;&nbsp;- port: 80<br>&nbsp;&nbsp;&nbsp;&nbsp;{{c5::targetPort}}: 8080<br>&nbsp;&nbsp;&nbsp;&nbsp;{{c6::nodePort}}: 30080</code>
**Back Extra:** apiVersion: v1 — Service lives in the core API group. selector must match pod labels (that's how the Service finds backends). targetPort is the port ON the pods; nodePort is only needed for type NodePort — omit it and the control plane auto-allocates from 30000-32767.
**Tags:** k8s::beginners topic::networking topic::services topic::yaml src::session

---

<!-- note:1793737589735 model:Many -->
**Domain:** Services
**Question:** What is the DEFAULT port range a NodePort Service can be allocated from?
**Options:** A. 1024-29999<br>B. 30000-32767<br>C. 1-65535<br>D. 32768-60999
**Answer:** B (2) – 30000-32767
**Explanation:** The control plane allocates NodePorts from the --service-node-port-range flag, default 30000-32767. You can pin a specific port via the nodePort field as long as it's inside that range and free; leave it empty for auto-allocation.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/service/" target="_blank">Kubernetes Documentation - Service</a>
**Tags:** k8s::beginners topic::networking topic::services src::session

---

<!-- note:1793737589736 model:Many -->
**Domain:** Services
**Question:** Which Service type gives a stable IP reachable only from inside the cluster — and is the default when <code>spec.type</code> is omitted?
**Options:** A. NodePort<br>B. ClusterIP<br>C. LoadBalancer<br>D. ExternalName
**Answer:** B (2) – ClusterIP
**Explanation:** ClusterIP is the default: a stable virtual IP reachable only inside the cluster — used for internal service-to-service traffic. NodePort exposes it on every node's IP; LoadBalancer asks for an external LB; ExternalName is just a DNS CNAME with no proxying.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/service/" target="_blank">Kubernetes Documentation - Service</a>
**Tags:** k8s::beginners topic::networking topic::services src::session

---

<!-- note:1793737589737 model:Many -->
**Domain:** Services
**Question:** A NodePort Service is created with nodePort 30080. What can clients connect to?
**Options:** A. Only the node running the pods opens the port<br>B. The pod's node IP gets the port; other nodes don't<br>C. Every node opens the same nodePort and forwards to a ready backend pod<br>D. One dedicated ingress node is chosen
**Answer:** C (3) – Every node opens the same nodePort and forwards to a ready backend pod
**Explanation:** The nodePort is allocated cluster-wide: each node proxies that port into the Service, so <any-node-IP>:<nodePort> works — the backend pod may even be on another node. The Service also gets a clusterIP (NodePort builds on ClusterIP).
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/service/" target="_blank">Kubernetes Documentation - Service</a>
**Tags:** k8s::beginners topic::networking topic::services src::session

---
