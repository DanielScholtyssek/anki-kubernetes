<!-- note:1793756864965 model:Many -->
**Domain:** Namespaces - defaults
**Question:** Which namespaces exist in a fresh Kubernetes cluster by default?
**Options:** A. only 'default'<br>B. default, prod, staging<br>C. default, kube-system, kube-public, kube-node-lease<br>D. master, worker, default
**Answer:** C (3) – default, kube-system, kube-public, kube-node-lease
**Explanation:** Every cluster starts with four: 'default' (objects with no namespace set), 'kube-system' (the cluster's own infrastructure — CoreDNS, kube-proxy, control-plane pods in kubeadm clusters), 'kube-public' (publicly readable info, mostly unused), 'kube-node-lease' (node heartbeat Lease objects). Create your own for teams/apps via kubectl create ns.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Documentation - Namespaces</a>
**Tags:** k8s::kcna topic::architecture topic::namespaces src::session

---

<!-- note:1793756864966 model:Many -->
**Domain:** Namespaces - kubectl
**Question:** Which kubectl command makes 'dev' your DEFAULT namespace for all subsequent commands?
**Options:** A. kubectl use namespace dev<br>B. kubectl config set-context --current --namespace=dev<br>C. kubectl set namespace dev<br>D. kubectl switch-context dev
**Answer:** B (2) – kubectl config set-context --current --namespace=dev
**Explanation:** set-context --current --namespace=dev writes 'dev' into your kubeconfig's current context — every subsequent kubectl command defaults to it, no -n flag needed. The alternative is passing -n dev (or --namespace=dev) on each command. kubectl get ns lists namespaces; create ns makes one.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Documentation - Namespaces</a>
**Tags:** k8s::kcna topic::kubectl topic::namespaces src::session

---

<!-- note:1793756864967 model:Many -->
**Domain:** Namespaces - scoping
**Question:** Which of these resources is cluster-scoped — i.e. does NOT live inside a namespace?
**Options:** A. Pod<br>B. Service<br>C. Deployment<br>D. Node
**Answer:** D (4) – Node
**Explanation:** Nodes, PersistentVolumes, ClusterRoles — and Namespaces themselves — are cluster-scoped: they live outside any namespace (metadata.namespace must be empty). Pods, Services, Deployments, Secrets, ConfigMaps are namespaced. Discover which is which with kubectl api-resources --namespaced=true/false.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Documentation - Namespaces</a>
**Tags:** k8s::kcna topic::api topic::namespaces src::session

---

<!-- note:1793756864968 model:Many -->
**Domain:** Namespaces - isolation
**Question:** Do namespaces on their own provide hard isolation between workloads?
**Options:** A. Yes — namespaces fully isolate workloads from each other<br>B. No — namespaces are logical grouping; real isolation needs NetworkPolicy, RBAC and quotas on top<br>C. Yes — pods cannot communicate across namespaces<br>D. Only if ResourceQuota is configured
**Answer:** B (2) – No — namespaces are logical grouping; real isolation needs NetworkPolicy, RBAC and quotas on top
**Explanation:** Namespaces partition names and org ownership — but the pod network stays flat by default: a pod in ns 'dev' can still reach a pod in ns 'prod'. Hard isolation is layered on: NetworkPolicies for traffic, RBAC for API access, ResourceQuota/LimitRange for resources. Namespaces are the boundary those features scope to, not the isolation itself.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Documentation - Namespaces</a>
**Tags:** k8s::kcna topic::namespaces topic::networking src::session

---

<!-- note:1793757640845 model:Many -->
**Domain:** Namespaces - kube-system
**Question:** A fresh cluster's DNS pods (CoreDNS) and kube-proxy land in which namespace — deliberately separated from user workloads so they can't be accidentally deleted?
**Options:** A. default<br>B. kube-system<br>C. kube-public<br>D. kube-node-lease
**Answer:** B (2) – kube-system
**Explanation:** kube-system holds the cluster's own objects — CoreDNS, kube-proxy, and (in kubeadm clusters) the control-plane static pods. Putting them in their own namespace keeps them out of your 'kubectl get all' view and protects them from accidental deletion — you have to explicitly target -n kube-system. kube-public is for data readable by ALL users; kube-node-lease holds node heartbeats.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Documentation - Namespaces</a>
**Tags:** k8s::kcna topic::architecture topic::namespaces src::session

---

<!-- note:1793757640846 model:Many -->
**Domain:** Namespaces - DNS
**Question:** A pod in namespace 'dev' must reach the Service 'api' living in namespace 'prod'. Which DNS name works?
**Options:** A. api<br>B. api.prod<br>C. api.prod.svc.cluster.local<br>D. api.dev.svc.cluster.local
**Answer:** C (3) – api.prod.svc.cluster.local
**Explanation:** Services are registered in CoreDNS as <service>.<namespace>.svc.cluster.local. The SHORT name (api) only resolves inside the caller's own namespace — a dev pod asking for 'api' gets dev's api (or NXDOMAIN). Cross-namespace calls need the namespace in the name: api.prod.svc.cluster.local.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/" target="_blank">Kubernetes Documentation - DNS for Services and Pods</a>
**Tags:** k8s::kcna topic::dns topic::namespaces src::session

---

<!-- note:1793757640855 model:Basic (and reversed card) -->
**Front:** In Service DNS names like <code>api.prod.svc.cluster.local</code>, what is the final domain component?
**Back:** <code>cluster.local</code> — it completes the Service FQDN <code>&lt;svc&gt;.&lt;ns&gt;.svc.cluster.local</code>. It's the cluster's default DNS domain (the 'base domain' CoreDNS serves); kubelet hands it to pods via <code>clusterDomain</code>/resolv.conf. Custom clusters can change it, but stock installs use cluster.local.
**Tags:** k8s::kcna topic::dns topic::namespaces src::session

---

<!-- note:1793757640856 model:Basic (and reversed card) -->
**Front:** How do you place a new object into namespace 'dev' instead of 'default' when creating it?
**Back:** Set its <code>metadata.namespace</code> field (e.g. <code>namespace: dev</code>) — or pass <code>-n dev</code> at creation with an imperative command. If you omit it, the object lands in your current context's namespace (usually <code>default</code>).
**Tags:** k8s::kcna topic::namespaces topic::yaml src::session

---

