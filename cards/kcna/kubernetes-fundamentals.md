# KCNA - Kubernetes and Cloud Native Associate — Kubernetes Fundamentals

> Deck: `KCNA - Kubernetes and Cloud Native Associate` · Group: `Kubernetes Fundamentals` · Notes: 329 · Models: Basic, Basic (and reversed card), Cloze, Many

<!-- note:1793752347323 model:Basic -->
**Front:** Which kubectl command exposes a Deployment named <code>web</code> as a NodePort Service on port 80?
**Back:** <code>kubectl expose deployment web --type=NodePort --port=80</code> — <code>--port</code> is the port the Service listens on; <code>--type=NodePort</code> makes it open a 30000-32767 port on every node. Alternative: <code>kubectl create service nodeport web --tcp=80:8080</code> (servicePort:targetPort). To convert an existing service: <code>kubectl patch svc web -p '{"spec":{"type":"NodePort"}}'</code>.
**Tags:** k8s::kcna src::session topic::kubectl topic::services

---

<!-- note:1793752347334 model:Cloze -->
**Text:** A Service named <code>backend</code> in namespace <code>prod</code> gets the in-cluster DNS name<br><br><code>{{c1::backend}}.{{c2::prod}}.{{c3::svc}}.{{c4::cluster.local}}</code><br><br>resolving to the Service's {{c5::clusterIP}}.
**Back Extra:** CoreDNS publishes &lt;service&gt;.&lt;namespace&gt;.svc.cluster.local for every Service; it resolves to the clusterIP. Inside the same namespace the short name (backend) is enough; from another namespace you need backend.&lt;ns&gt;.
**Tags:** k8s::kcna src::session topic::dns topic::services

---

<!-- note:1793752354576 model:Many -->
**Domain:** Service Types - ClusterIP
**Question:** Which Service type is the default when <code>spec.type</code> is not specified, and is reachable only inside the cluster?
**Options:** A. NodePort<br>B. ClusterIP<br>C. LoadBalancer<br>D. ExternalName
**Answer:** B (2) – ClusterIP
**Explanation:** ClusterIP is the default Service type: a stable virtual IP reachable only inside the cluster — used for internal pod-to-pod / microservice traffic. NodePort and LoadBalancer build on it to expose traffic externally; ExternalName is pure DNS.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/service/" target="_blank">Kubernetes Documentation - Service</a>
**Tags:** k8s::kcna src::session topic::networking topic::services

---

<!-- note:1793752354577 model:Many -->
**Domain:** Service Types - NodePort
**Question:** Which Service type opens the same port (e.g. 30080) on EVERY node's IP so external clients can reach the service?
**Options:** A. ClusterIP<br>B. ExternalName<br>C. NodePort<br>D. Ingress
**Answer:** C (3) – NodePort
**Explanation:** A NodePort Service allocates the same static port (default range 30000-32767) on EVERY node — each node proxies &lt;node-IP&gt;:&lt;nodePort&gt; into the Service, which forwards to a ready backend pod. It's the simplest built-in way to accept outside traffic.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/service/" target="_blank">Kubernetes Documentation - Service</a>
**Tags:** k8s::kcna src::session topic::networking topic::services

---

<!-- note:1793752354578 model:Many -->
**Domain:** Service Types - LoadBalancer
**Question:** Which Service type asks the cloud provider (or an LB implementation like MetalLB/Cilium) to provision an external load balancer with a public IP?
**Options:** A. NodePort<br>B. LoadBalancer<br>C. ClusterIP<br>D. ExternalName
**Answer:** B (2) – LoadBalancer
**Explanation:** type: LoadBalancer delegates to an external implementation — the cloud-controller-manager on AWS/GCP/Azure, or tools like MetalLB/Cilium LB IPAM on bare metal. The provisioned IP lands in .status.loadBalancer.ingress. With no implementation, EXTERNAL-IP stays &lt;pending&gt;.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/service/" target="_blank">Kubernetes Documentation - Service</a>
**Tags:** k8s::kcna src::session topic::networking topic::services

---

<!-- note:1793752354579 model:Many -->
**Domain:** Service Port Fields
**Question:** In a Service manifest, which field specifies the port ON THE BACKEND PODS that traffic is forwarded to?
**Options:** A. port<br>B. nodePort<br>C. targetPort<br>D. hostPort
**Answer:** C (3) – targetPort
**Explanation:** port = what the Service itself listens on (clients connect to clusterIP:port); targetPort = the port on the backend pods traffic is forwarded to (defaults to the port value); nodePort = the per-node external port for NodePort Services.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/service/" target="_blank">Kubernetes Documentation - Service</a>
**Tags:** k8s::kcna src::session topic::networking topic::services topic::yaml

---

<!-- note:1793752354580 model:Many -->
**Domain:** ReplicaSet Selectors
**Question:** How does a ReplicaSet identify which pods it manages and counts toward spec.replicas?
**Options:** A. Pods register themselves with the ReplicaSet via the API<br>B. Its spec.selector.matchLabels must match the labels in spec.template.metadata.labels<br>C. The kubelet reports pod names to the ReplicaSet<br>D. Namespaces define which pods belong to a ReplicaSet
**Answer:** B (2) – Its spec.selector.matchLabels must match the labels in spec.template.metadata.labels
**Explanation:** A ReplicaSet counts and manages every pod whose labels satisfy spec.selector.matchLabels — the selector must equal the pod template's labels or the API rejects the object. It can even adopt pre-existing matching pods that have no controller ownerReference.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/" target="_blank">Kubernetes Documentation - ReplicaSet</a>
**Tags:** k8s::kcna src::session topic::labels topic::replicasets

---

<!-- note:1793752906100 model:Many -->
**Domain:** Cluster Architecture - Control Plane
**Question:** Which of these components runs ONLY on control-plane nodes, not on worker nodes?
**Options:** A. kubelet<br>B. container runtime<br>C. kube-apiserver<br>D. kube-proxy
**Answer:** C (3) – kube-apiserver
**Explanation:** kube-apiserver, etcd, kube-scheduler and kube-controller-manager run only on control-plane nodes — they manage the cluster. kubelet, kube-proxy and the container runtime run on every node (workers AND control plane) so any node can host pods.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/components/" target="_blank">Kubernetes Documentation - Kubernetes Components</a>
**Tags:** k8s::kcna src::session topic::architecture topic::control-plane

---

<!-- note:1793752906116 model:Basic -->
**Front:** What is the difference between a control-plane node and a worker node in Kubernetes?
**Back:** Control-plane nodes run the cluster's management components — kube-apiserver, etcd, kube-scheduler, kube-controller-manager — and normally run no user workloads (protected by a taint). Worker nodes run the application pods: each has kubelet, kube-proxy and a container runtime. Every node needs the per-node components; only control-plane nodes need the management stack.
**Tags:** k8s::kcna src::session topic::architecture topic::control-plane

---

<!-- note:1793752918693 model:Cloze -->
**Text:** Control plane nodes were previously called {{c1::master}} nodes.
**Back Extra:** The old term 'master node' is still common in older courses, books and docs — e.g. 'master components'. Same thing; 'control plane' is the current name.
**Tags:** k8s::kcna src::session topic::architecture topic::control-plane

---

<!-- note:1793753105610 model:Many -->
**Domain:** Cluster Architecture - etcd
**Question:** What is the role of etcd in a Kubernetes cluster?
**Options:** A. It implements locks to prevent conflicts between the masters.<br>B. It ensures distributed storage of information across all nodes in the cluster.<br>C. All of the options are correct<br>D. It stores all the data used to manage the cluster.
**Answer:** C (3) – All of the options are correct
**Explanation:** Per the course framing, all three describe etcd: it stores ALL data used to manage the cluster (D), it keeps that data as distributed replicated storage so control-plane nodes share one consistent view (B), and its distributed consensus — leader election/quorum via Raft, described as 'locks' — prevents conflicting writes between the masters (A). Nuance for the real world: etcd members run only on control-plane nodes ('all nodes' is loose phrasing for the etcd members), and 'locks' really means Raft consensus, not literal locking.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/components/" target="_blank">Kubernetes Documentation - Kubernetes Components</a>
**Tags:** k8s::kcna src::session topic::architecture topic::etcd

---

<!-- note:1793754672879 model:Many -->
**Domain:** ReplicaSet Self-healing
**Question:** A pod managed by a ReplicaSet is deleted (or its node fails). What happens?
**Options:** A. Nothing — the pod is gone permanently<br>B. The ReplicaSet controller notices actual < desired and creates a replacement pod to restore the count<br>C. The kubelet restarts the deleted pod's containers<br>D. The Deployment re-creates the ReplicaSet
**Answer:** B (2) – The ReplicaSet controller notices actual < desired and creates a replacement pod to restore the count
**Explanation:** A ReplicaSet's reconcile loop continuously compares spec.replicas to the number of matching pods alive. Delete a pod (or lose a node) and the count drops — the controller immediately creates a new pod from spec.template to restore it. That's the self-healing/HA behavior ReplicaSets provide.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/" target="_blank">Kubernetes Documentation - ReplicaSet</a>
**Tags:** k8s::kcna src::session topic::pods topic::replicasets

---

<!-- note:1793754672880 model:Many -->
**Domain:** Deployment Rolling Update Internals
**Question:** You change a Deployment's pod template (e.g. new image). What happens internally during the rolling update?
**Options:** A. The existing ReplicaSet edits its pods in place<br>B. A new ReplicaSet is created for the new pod template and scaled up while the old one scales down<br>C. All pods are deleted, then recreated<br>D. The Service is re-pointed first, then pods update
**Answer:** B (2) – A new ReplicaSet is created for the new pod template and scaled up while the old one scales down
**Explanation:** Every change to .spec.template creates a new ReplicaSet — during a RollingUpdate the new RS scales up gradually as the old scales down (maxSurge/maxUnavailable control the pace). Old RSs stay at 0 replicas so <code>kubectl rollout undo</code> can scale one back up.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/deployment/" target="_blank">Kubernetes Documentation - Deployment</a>
**Tags:** k8s::kcna src::session topic::deployments topic::rollouts

---

<!-- note:1793754672881 model:Many -->
**Domain:** Rollout & Rollback
**Question:** A Deployment's latest rollout is broken. Which command rolls it back to the previous pod-template version?
**Options:** A. <code>kubectl rollout restart deployment/web</code><br>B. <code>kubectl rollout undo deployment/web</code><br>C. <code>kubectl delete deployment/web</code><br>D. <code>kubectl scale deployment/web --replicas=0</code>
**Answer:** B (2) – <code>kubectl rollout undo deployment/web</code>
**Explanation:** <code>kubectl rollout undo</code> scales an OLD ReplicaSet back up — the pod template returns to the previous revision (<code>kubectl rollout history</code> lists them; <code>--to-revision=N</code> picks a specific one). Only the pod template rolls back; scaling/config changes aren't revisions.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/deployment/" target="_blank">Kubernetes Documentation - Deployment</a>
**Tags:** k8s::kcna src::session topic::deployments topic::kubectl

---

<!-- note:1793754672882 model:Many -->
**Domain:** kubectl create deployment
**Question:** Which command creates a Deployment named web running 3 replicas of nginx?
**Options:** A. <code>kubectl run web --image=nginx --replicas=3</code><br>B. kubectl new deployment web <code>--image=nginx</code><br>C. <code>kubectl create deployment web --image=nginx --replicas=3</code><br>D. <code>kubectl apply deployment web --image=nginx --replicas=3</code>
**Answer:** C (3) – <code>kubectl create deployment web --image=nginx --replicas=3</code>
**Explanation:** <code>kubectl create deployment</code> makes the Deployment object; <code>--image</code> sets the pod template's container image, <code>--replicas</code> sets the desired count (default 1). Imperative equivalent of a YAML Deployment manifest. (<code>kubectl run</code> creates a bare Pod, not a Deployment.)
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_deployment/" target="_blank">Kubernetes Documentation - kubectl create deployment</a>
**Tags:** k8s::kcna src::session topic::deployments topic::kubectl

---

<!-- note:1793754672883 model:Many -->
**Domain:** kubectl explain
**Question:** Which kubectl command shows documentation for a resource's fields, e.g. <code>kubectl explain pod.spec.containers</code>?
**Options:** A. <code>kubectl describe</code><br>B. <code>kubectl explain</code><br>C. kubectl doc<br>D. <code>kubectl get -o yaml</code>
**Answer:** B (2) – <code>kubectl explain</code>
**Explanation:** <code>kubectl explain</code> prints the schema/documentation for a resource's fields — e.g. <code>kubectl explain deployment.spec.strategy</code> describes every field, its type and meaning. It's the built-in way to answer 'what does this manifest field do' without leaving the terminal.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/generated/kubectl_explain/" target="_blank">Kubernetes Documentation - kubectl explain</a>
**Tags:** k8s::kcna src::session topic::kubectl topic::yaml

---

<!-- note:1793754672884 model:Many -->
**Domain:** Manifest Structure
**Question:** Which four top-level fields are required in every Kubernetes object manifest?
**Options:** A. name, image, replicas, port<br>B. apiVersion, metadata, spec, status<br>C. apiVersion, kind, metadata and spec<br>D. kind, spec, status, data
**Answer:** C (3) – apiVersion, kind, metadata and spec
**Explanation:** Every manifest needs all four top-level fields: apiVersion (API group+version, e.g. apps/v1), kind (object type → its schema), metadata (name/namespace/labels), spec (the desired state — its contents depend on the kind). status exists too but is written by Kubernetes, not required in your file.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/" target="_blank">Kubernetes Documentation - Objects In Kubernetes</a>
**Tags:** k8s::kcna src::session topic::api topic::yaml

---

<!-- note:1793754672885 model:Many -->
**Domain:** kubectl run
**Question:** Which command creates a pod named 'nginx' running the nginx image?
**Options:** A. <code>kubectl create pod nginx</code><br>B. <code>kubectl run nginx --image=nginx</code><br>C. kubectl deploy nginx <code>--image=nginx</code><br>D. kubectl start nginx <code>--image=nginx</code>
**Answer:** B (2) – <code>kubectl run nginx --image=nginx</code>
**Explanation:** <code>kubectl run</code> creates a single pod; <code>--image</code> names the container image to pull (Docker Hub by default — use a full registry path for private repos). Note: <code>kubectl create</code> has NO pod subcommand (only deployment, service, job, etc.) — pods are created via kubectl run or a manifest with kubectl create/apply -f. deploy/start are not pod commands.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/pods/" target="_blank">Kubernetes Documentation - Pods</a>
**Tags:** k8s::kcna src::session topic::kubectl topic::pods

---

<!-- note:1793754672890 model:Cloze -->
**Text:** Minimal pod manifest:<br><br><code>apiVersion: {{c1::v1}}<br>kind: {{c2::Pod}}<br>metadata:<br>&nbsp;&nbsp;{{c3::name}}: nginx<br>spec:<br>&nbsp;&nbsp;{{c4::containers}}:<br>&nbsp;&nbsp;- name: nginx<br>&nbsp;&nbsp;&nbsp;&nbsp;{{c5::image}}: nginx</code>
**Back Extra:** v1 = core API group (named groups use group/version, e.g. apps/v1 for Deployments). metadata.name is how you identify the pod; spec.containers is a LIST (note the dash) — even a single-container pod needs the list item.
**Tags:** k8s::kcna src::session topic::pods topic::yaml

---

<!-- note:1793754672900 model:Basic -->
**Front:** How do you list pods with kubectl, and what do the flags <code>-o wide</code>, <code>-A</code> and <code>-w</code> add?
**Back:** <code>kubectl get pods</code> lists pods in the current namespace with status. Useful variants: <code>-o wide</code> (adds pod IPs + which node each runs on), <code>-A</code>/<code>--all-namespaces</code> (every namespace), <code>-w</code> (watch for changes). For detail on one pod incl. events: <code>kubectl describe pod &lt;name&gt;</code>.
**Tags:** k8s::kcna src::session topic::kubectl topic::pods

---

<!-- note:1793755549227 model:Many -->
**Domain:** Imperative vs Declarative - apply
**Question:** Which of these is the DECLARATIVE object-management approach in Kubernetes?
**Options:** A. <code>kubectl create deployment web --image=nginx</code><br>B. <code>kubectl replace -f deployment.yaml</code><br>C. <code>kubectl apply -f deployment.yaml</code><br>D. <code>kubectl edit deployment web</code>
**Answer:** C (3) – <code>kubectl apply -f deployment.yaml</code>
**Explanation:** apply -f is the DECLARATIVE path: it merges the file's desired state into the live object and records last-applied-configuration to compute future diffs. create/replace -f are the middle tier ('imperative object configuration' — file-driven but verb-led: create fails if it exists, replace swaps the whole object). create/edit/run/expose are pure imperative commands.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna src::session topic::kubectl topic::yaml

---

<!-- note:1793755549228 model:Many -->
**Domain:** Imperative vs Declarative - commands
**Question:** Which group contains ONLY imperative commands (no manifest file involved)?
**Options:** A. <code>kubectl run</code>, <code>kubectl create deployment</code>, <code>kubectl expose</code><br>B. <code>kubectl apply -f</code>, <code>kubectl diff</code><br>C. <code>kubectl create -f</code>, <code>kubectl replace -f</code><br>D. <code>kubectl get</code>, <code>kubectl describe</code>
**Answer:** A (1) – <code>kubectl run</code>, <code>kubectl create deployment</code>, <code>kubectl expose</code>
**Explanation:** Imperative commands tell the cluster WHAT to do right now: run, create deployment, expose, scale, delete — no file, no recorded desired state. The -f variants of create/replace are imperative object configuration (middle tier); apply -f is the declarative tier. get/describe are read-only, not management.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna src::session topic::kubectl topic::yaml

---

<!-- note:1793755549229 model:Many -->
**Domain:** Imperative vs Declarative - why
**Question:** Why is the declarative approach preferred for production and GitOps workflows?
**Options:** A. It executes faster than imperative commands<br>B. Manifests live in Git as a reviewable source of truth, and apply is idempotent and detects drift via last-applied-configuration<br>C. Imperative commands cannot create objects<br>D. The API server only accepts YAML
**Answer:** B (2) – Manifests live in Git as a reviewable source of truth, and apply is idempotent and detects drift via last-applied-configuration
**Explanation:** Declarative YAML can be versioned, reviewed and audited in Git (the GitOps model), re-applied safely (idempotent), and apply's last-applied annotation reveals drift. Imperative commands leave no record — nothing to diff, review or re-converge from.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna src::session topic::gitops topic::kubectl

---

<!-- note:1793756257574 model:Basic (and reversed card) -->
**Front:** What is the IMPERATIVE approach to managing infrastructure or Kubernetes objects?
**Back:** The approach where you spell out WHAT you want AND HOW to get there — every step explicitly, in order (<code>run this</code>, <code>create that</code>, <code>scale this to 5</code>). The tool executes commands; it doesn't reason about an end state. Examples: kubectl run/create/expose/scale/edit/set image — and shell scripts in the DevOps world.
**Tags:** k8s::kcna src::session topic::declarative topic::kubectl

---

<!-- note:1793756257575 model:Basic (and reversed card) -->
**Front:** What is the DECLARATIVE approach to managing infrastructure or Kubernetes objects?
**Back:** The approach where you describe only WHAT the end state should look like — a manifest of desired state — and the system works out the HOW itself (diff, plan, reconcile). Examples: <code>kubectl apply -f</code>, Terraform plans, Kubernetes controllers converging actual→desired state.
**Tags:** k8s::kcna src::session topic::declarative topic::kubectl

---

<!-- note:1793756257583 model:Many -->
**Domain:** Imperative vs Declarative - DevOps
**Question:** You write a Terraform config describing what infrastructure SHOULD exist, and Terraform works out the steps to reach it. Which approach is this?
**Options:** A. Imperative<br>B. Declarative<br>C. Procedural<br>D. Manual
**Answer:** B (2) – Declarative
**Explanation:** Terraform is the classic declarative IaC tool: you write config describing the END state (which resources should exist), and Terraform's engine computes the plan — what to create/change/destroy to get there. Same model as <code>kubectl apply</code>. Imperative tools/scripts instead encode each step to execute.
**Sources:** <a href="https://developer.hashicorp.com/terraform/intro" target="_blank">HashiCorp Documentation - What is Terraform</a>
**Tags:** k8s::kcna src::session topic::declarative topic::gitops

---

<!-- note:1793756257584 model:Many -->
**Domain:** Imperative vs Declarative - set image
**Question:** <code>kubectl set image deployment/web nginx=nginx:2.0</code> — which management approach is this?
**Options:** A. A declarative update<br>B. Imperative object configuration<br>C. An imperative command — it directly instructs the cluster to change the image NOW, with no declared desired state<br>D. A GitOps operation
**Answer:** C (3) – An imperative command — it directly instructs the cluster to change the image NOW, with no declared desired state
**Explanation:** set image, like run/create/expose/scale/edit/delete, is imperative: one-shot instruction, nothing recorded to converge against. The declarative equivalent is editing the image in the manifest and re-running <code>kubectl apply -f</code>
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna src::session topic::declarative topic::kubectl

---

<!-- note:1793756257585 model:Many -->
**Domain:** Imperative vs Declarative - apply mechanics
**Question:** You run <code>kubectl apply -f app.yaml</code> on an object that already exists. What does apply do?
**Options:** A. It fails because the resource already exists<br>B. It compares the manifest, the live object AND last-applied-configuration, then applies only the needed changes (create or patch)<br>C. It deletes and recreates the object from scratch<br>D. It replaces the whole object, losing unmanaged fields
**Answer:** B (2) – It compares the manifest, the live object AND last-applied-configuration, then applies only the needed changes (create or patch)
**Explanation:** apply is a three-way merge: file's desired state vs the object's live state vs the recorded last-applied-configuration. Object missing → created; exists → patched to match the declaration. That's why the same file can be applied repeatedly and why it's the declarative workflow.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna src::session topic::declarative topic::kubectl

---

<!-- note:1793756257586 model:Many -->
**Domain:** Imperative vs Declarative - contrast
**Question:** Which statement correctly contrasts the imperative and declarative approaches?
**Options:** A. Imperative describes the end state; declarative lists the steps<br>B. Imperative = you specify WHAT you want AND HOW (the steps); declarative = you specify only WHAT the result should be<br>C. They are two names for the same workflow<br>D. Declarative requires typing more commands
**Answer:** B (2) – Imperative = you specify WHAT you want AND HOW (the steps); declarative = you specify only WHAT the result should be
**Explanation:** Imperative: the operator encodes the path — every command/step explicitly. Declarative: the operator encodes the destination — the system derives the path (diff + reconcile). Kubernetes manifests+apply and Terraform are declarative; ad-hoc kubectl commands and shell scripts are imperative.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna src::session topic::declarative topic::kubectl

---

<!-- note:1793756656941 model:Many -->
**Domain:** kubectl apply - last-applied
**Question:** What does the <code>kubectl.kubernetes.io/last-applied-configuration</code> annotation on an object store?
**Options:** A. The object's current live spec<br>B. The JSON of the manifest most recently applied via <code>kubectl apply</code><br>C. The default values the API server filled in<br>D. The object's original creation manifest from any tool
**Answer:** B (2) – The JSON of the manifest most recently applied via <code>kubectl apply</code>
**Explanation:** Each apply writes the applied manifest (as JSON) into the kubectl.kubernetes.io/last-applied-configuration annotation on the object. It's the third leg of apply's three-way merge — file vs live vs last-applied — letting kubectl compute diffs, detect drift, and delete fields removed from the file. <code>kubectl get -o yaml</code> shows LIVE state; this annotation remembers what YOU declared.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna src::session topic::declarative topic::kubectl topic::yaml

---

<!-- note:1793756864965 model:Many -->
**Domain:** Namespaces - defaults
**Question:** Which namespaces exist in a fresh Kubernetes cluster by default?
**Options:** A. only 'default'<br>B. default, prod, staging<br>C. default, kube-system, kube-public, kube-node-lease<br>D. master, worker, default
**Answer:** C (3) – default, kube-system, kube-public, kube-node-lease
**Explanation:** Every cluster starts with four: 'default' (objects with no namespace set), 'kube-system' (the cluster's own infrastructure — CoreDNS, kube-proxy, control-plane pods in kubeadm clusters), 'kube-public' (publicly readable info, mostly unused), 'kube-node-lease' (node heartbeat Lease objects). Create your own for teams/apps via <code>kubectl create ns</code>
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Documentation - Namespaces</a>
**Tags:** k8s::kcna src::session topic::architecture topic::namespaces

---

<!-- note:1793756864966 model:Many -->
**Domain:** Namespaces - kubectl
**Question:** Which kubectl command makes 'dev' your DEFAULT namespace for all subsequent commands?
**Options:** A. kubectl use namespace dev<br>B. <code>kubectl config set-context --current --namespace=dev</code><br>C. <code>kubectl set namespace dev</code><br>D. kubectl switch-context dev
**Answer:** B (2) – <code>kubectl config set-context --current --namespace=dev</code>
**Explanation:** set-context <code>--current</code> <code>--namespace=dev</code> writes 'dev' into your kubeconfig's current context — every subsequent kubectl command defaults to it, no -n flag needed. The alternative is passing -n dev (or <code>--namespace=dev</code>) on each command. <code>kubectl get ns</code> lists namespaces; create ns makes one.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Documentation - Namespaces</a>
**Tags:** k8s::kcna src::session topic::kubectl topic::namespaces

---

<!-- note:1793756864967 model:Many -->
**Domain:** Namespaces - scoping
**Question:** Which of these resources is cluster-scoped — i.e. does NOT live inside a namespace?
**Options:** A. Pod<br>B. Service<br>C. Deployment<br>D. Node
**Answer:** D (4) – Node
**Explanation:** Nodes, PersistentVolumes, ClusterRoles — and Namespaces themselves — are cluster-scoped: they live outside any namespace (metadata.namespace must be empty). Pods, Services, Deployments, Secrets, ConfigMaps are namespaced. Discover which is which with <code>kubectl api-resources --namespaced=true/false</code>
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Documentation - Namespaces</a>
**Tags:** k8s::kcna src::session topic::api topic::namespaces

---

<!-- note:1793756864968 model:Many -->
**Domain:** Namespaces - isolation
**Question:** Do namespaces on their own provide hard isolation between workloads?
**Options:** A. Yes — namespaces fully isolate workloads from each other<br>B. No — namespaces are logical grouping; real isolation needs NetworkPolicy, RBAC and quotas on top<br>C. Yes — pods cannot communicate across namespaces<br>D. Only if ResourceQuota is configured
**Answer:** B (2) – No — namespaces are logical grouping; real isolation needs NetworkPolicy, RBAC and quotas on top
**Explanation:** Namespaces partition names and org ownership — but the pod network stays flat by default: a pod in ns 'dev' can still reach a pod in ns 'prod'. Hard isolation is layered on: NetworkPolicies for traffic, RBAC for API access, ResourceQuota/LimitRange for resources. Namespaces are the boundary those features scope to, not the isolation itself.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Documentation - Namespaces</a>
**Tags:** k8s::kcna src::session topic::namespaces topic::networking

---

<!-- note:1793757640845 model:Many -->
**Domain:** Namespaces - kube-system
**Question:** A fresh cluster's DNS pods (CoreDNS) and kube-proxy land in which namespace — deliberately separated from user workloads so they can't be accidentally deleted?
**Options:** A. default<br>B. kube-system<br>C. kube-public<br>D. kube-node-lease
**Answer:** B (2) – kube-system
**Explanation:** kube-system holds the cluster's own objects — CoreDNS, kube-proxy, and (in kubeadm clusters) the control-plane static pods. Putting them in their own namespace keeps them out of your '<code>kubectl get all</code>' view and protects them from accidental deletion — you have to explicitly target -n kube-system. kube-public is for data readable by ALL users; kube-node-lease holds node heartbeats.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Documentation - Namespaces</a>
**Tags:** k8s::kcna src::session topic::architecture topic::namespaces

---

<!-- note:1793757640846 model:Many -->
**Domain:** Namespaces - DNS
**Question:** A pod in namespace 'dev' must reach the Service 'api' living in namespace 'prod'. Which DNS name works?
**Options:** A. api<br>B. api.prod<br>C. api.prod.svc.cluster.local<br>D. api.dev.svc.cluster.local
**Answer:** C (3) – api.prod.svc.cluster.local
**Explanation:** Services are registered in CoreDNS as &lt;service&gt;.&lt;namespace&gt;.svc.cluster.local. The SHORT name (api) only resolves inside the caller's own namespace — a dev pod asking for 'api' gets dev's api (or NXDOMAIN). Cross-namespace calls need the namespace in the name: api.prod.svc.cluster.local.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/" target="_blank">Kubernetes Documentation - DNS for Services and Pods</a>
**Tags:** k8s::kcna src::session topic::dns topic::namespaces

---

<!-- note:1793757640855 model:Basic (and reversed card) -->
**Front:** In Service DNS names like <code>api.prod.svc.cluster.local</code>, what is the final domain component?
**Back:** <code>cluster.local</code> — it completes the Service FQDN <code>&lt;svc&gt;.&lt;ns&gt;.svc.cluster.local</code>. It's the cluster's default DNS domain (the 'base domain' CoreDNS serves); kubelet hands it to pods via <code>clusterDomain</code>/resolv.conf. Custom clusters can change it, but stock installs use cluster.local.
**Tags:** k8s::kcna src::session topic::dns topic::namespaces

---

<!-- note:1793757640856 model:Basic (and reversed card) -->
**Front:** How do you place a new object into namespace 'dev' instead of 'default' when creating it?
**Back:** Set its <code>metadata.namespace</code> field (e.g. <code>namespace: dev</code>) — or pass <code>-n dev</code> at creation with an imperative command. If you omit it, the object lands in your current context's namespace (usually <code>default</code>).
**Tags:** k8s::kcna src::session topic::dns topic::namespaces

---

<!-- note:1793807595536 model:Many -->
**Domain:** Scheduling - pod selection
**Question:** Which pods does the kube-scheduler pick up and try to place?
**Options:** A. Pods whose spec.nodeName is still unset<br>B. Pods that failed health checks<br>C. Pods on overloaded nodes<br>D. All newly created pods regardless of fields
**Answer:** A (1) – pods whose spec.nodeName is still unset (unassigned)
**Explanation:** The scheduler watches for newly created pods that have no node assigned — i.e. spec.nodeName is empty. For each it runs filtering (which nodes are feasible) then scoring (which is best), then binds the pod. Pods already carrying a nodeName never reach the scheduler — that's why manually setting it bypasses scheduling entirely.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/" target="_blank">Kubernetes Documentation - kube-scheduler</a>
**Tags:** k8s::kcna src::session topic::pods topic::scheduling

---

<!-- note:1793807595537 model:Many -->
**Domain:** Scheduling - nodeName immutability
**Question:** Can you change spec.nodeName on an already-created pod to move it to another node?
**Options:** A. Yes — <code>kubectl patch pod --type merge</code> works<br>B. Yes — kubectl edit pod and update the field<br>C. No — nodeName is immutable after creation; recreate the pod to move it<br>D. Only if the pod is restarted first
**Answer:** C (3) – no — nodeName is immutable after creation; recreate the pod to move it
**Explanation:** spec.nodeName can only be written at two moments: by you at pod creation, or by the scheduler via a Binding while the pod is still unassigned. Once set it's read-only — kubectl patch/edit on it is rejected. To move a scheduled pod you must delete and recreate it (or let a Deployment do the rollout).
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/" target="_blank">Kubernetes Documentation - kube-scheduler</a>
**Tags:** k8s::kcna src::session topic::pods topic::scheduling

---

<!-- note:1793807595538 model:Many -->
**Domain:** Scheduling - manual binding
**Question:** Without kube-scheduler, how do you assign an already-created pod that has no nodeName to a node?
**Options:** A. kubectl annotate the pod with the target node<br>B. Create a Binding object (POST JSON to the pod's binding subresource naming the target node)<br>C. Patch spec.nodeName directly<br>D. Add the node's name to metadata.labels
**Answer:** B (2) – create a Binding object (POST JSON to the pod's binding subresource naming the target node)
**Explanation:** The Binding object is what the scheduler itself creates after picking a node. Doing it manually: POST to /api/v1/namespaces/&lt;ns&gt;/pods/&lt;pod&gt;/binding with a body like {"target": {"kind": "Node", "name": "node2"}} — the API server then writes nodeName and the kubelet takes over. It only works while nodeName is still empty.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/" target="_blank">Kubernetes Documentation - kube-scheduler</a>
**Tags:** k8s::kcna src::session topic::api topic::scheduling

---

<!-- note:1793807595548 model:Basic (and reversed card) -->
**Front:** What is the <code>spec.nodeName</code> field on a pod?
**Back:** It holds the name of the node the pod is bound to run on. It's empty when you submit the pod — the scheduler fills it (via a Binding) after choosing a node. If you set <code>spec.nodeName</code> yourself at creation time, the pod skips the scheduler entirely: manual scheduling. Immutable afterwards.
**Tags:** k8s::kcna src::session topic::pods topic::scheduling

---

<!-- note:1793807595549 model:Basic (and reversed card) -->
**Front:** Mechanically, what does the kube-scheduler DO once it picks a node for a pod?
**Back:** The scheduler creates a <code>Binding</code> object — a POST to the pod's <code>binding</code> subresource naming the chosen node. The API server records the decision by writing <code>spec.nodeName</code> on the pod; the kubelet on that node then sees the pod is assigned to it and starts the containers.
**Tags:** k8s::kcna src::session topic::architecture topic::scheduling

---

<!-- note:1793808319432 model:Many -->
**Domain:** Labels - multi-criteria
**Question:** What does <code>kubectl get pods -l 'app=web,env=prod'</code> return?
**Options:** A. Pods matching ANY of the criteria<br>B. Only pods matching ALL criteria — multiple -l requirements are ANDed<br>C. Pods matching the first criterion only<br>D. Pods in the 'prod' namespace labelled web
**Answer:** B (2) – only pods matching ALL criteria — multiple -l requirements are ANDed
**Explanation:** Comma-separated selector requirements must ALL be satisfied — it's an AND, not OR. Equality selectors match exact values (app=web, env!=dev); set-based selectors match membership (env in (prod,qa), tier notin (cache), !key = absence). Everything from kubectl -l to NetworkPolicy podSelector uses the same requirement logic.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/" target="_blank">Kubernetes Documentation - Labels and Selectors</a>
**Tags:** k8s::kcna src::session topic::kubectl topic::labels

---

<!-- note:1793808319433 model:Many -->
**Domain:** Labels - manifest placement
**Question:** Where in a pod/Deployment manifest do an object's OWN labels always go?
**Options:** A. spec.labels<br>B. spec.selector.labels<br>C. metadata.labels<br>D. status.labels
**Answer:** C (3) – metadata.labels — the object's own label set
**Explanation:** Labels always go under metadata.labels on the object itself: metadata: {labels: {app: web, tier: frontend}}. The consumers live elsewhere in OTHER objects' specs: Service spec.selector, ReplicaSet/Deployment spec.selector.matchLabels, NetworkPolicy podSelector. 'Label everything, select from outside' is the pattern.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/" target="_blank">Kubernetes Documentation - Labels and Selectors</a>
**Tags:** k8s::kcna src::session topic::labels topic::yaml

---

<!-- note:1793808319514 model:Basic (and reversed card) -->
**Front:** Labels vs selectors — which side does what?
**Back:** Labels are key-value pairs ATTACHED to objects under <code>metadata.labels</code> — the grouping side (tag by app, tier, env, version…). Selectors are QUERIES that filter objects by their labels — the selection side (<code>kubectl -l</code>, Service <code>spec.selector</code>, ReplicaSet <code>matchLabels</code>, NetworkPolicy). Labels tag things; selectors find them.
**Tags:** k8s::kcna src::session topic::api topic::labels

---

<!-- note:1793808323513 model:Cloze -->
**Text:** List only pods labelled <code>app=web</code>:<br><br><code>kubectl get pods {{c1::-l}} {{c2::app=web}}</code><br><br>(<code>-l</code> is short for <code>{{c3::--selector}}</code>)
**Back Extra:** The flag works on most list commands (get pods, get svc, get all, delete). Multiple requirements AND together: -l 'app=web,env=prod'. Set-based form: -l 'env in (prod,qa)'. Combine with <code>--show-labels</code> to see each object's full label set.
**Tags:** k8s::kcna src::session topic::kubectl topic::labels

---

<!-- note:1793808422503 model:Many -->
**Domain:** Annotations - purpose
**Question:** You want to record build version, release notes and owner contact on Deployments — purely for humans and tooling to READ, never to filter on. What should you attach?
**Options:** A. Labels — key-value pairs under metadata.labels<br>B. Annotations — informational metadata not meant for selecting objects<br>C. ConfigMaps — dedicated configuration storage<br>D. Environment variables on the container spec
**Answer:** B (2) – annotations — informational metadata not meant for selecting objects
**Explanation:** Annotations record non-identifying, informational metadata — build versions, release notes, owner/contact info, doc links, tool config. Labels would technically hold short strings too, but labels exist to be SELECTED on (Services, ReplicaSets, -l flags). Rule of thumb: if controllers need to filter on it → label; if humans/tools just need to read it → annotation.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/" target="_blank">Kubernetes Documentation - Annotations</a>
**Tags:** k8s::kcna src::session topic::annotations topic::labels

---

<!-- note:1793808422504 model:Many -->
**Domain:** Annotations - limitations
**Question:** Which statement about annotations is TRUE?
**Options:** A. They can be selected with kubectl get -l just like labels<br>B. They're required on every object<br>C. They cannot be used in selectors — no -l flag or matchExpressions can filter on annotations<br>D. They can only hold values under 63 characters like labels
**Answer:** C (3) – they cannot be used in selectors — no -l flag or matchExpressions can filter on annotations
**Explanation:** The annotation API has no selector mechanism: kubectl -l doesn't see them, spec.selector/matchExpressions ignore them, Services can't pick pods by them. They're write-and-read metadata only (get -o yaml / describe shows them). Also unlike labels they aren't size-constrained the same way — they can hold larger structured blobs (that's how last-applied fits a whole manifest).
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/" target="_blank">Kubernetes Documentation - Annotations</a>
**Tags:** k8s::kcna src::session topic::annotations topic::api

---

<!-- note:1793808422514 model:Basic (and reversed card) -->
**Front:** What are annotations in Kubernetes — and a few typical examples?
**Back:** Key-value string metadata for informational purposes — recording details that identify nothing and select nothing: build/release version, git commit, owner contact, docs links, or config for tools and controllers (e.g. <code>kubectl.kubernetes.io/last-applied-configuration</code>, Prometheus <code>scrape</code> hints). They live under <code>metadata.annotations</code>, beside <code>metadata.labels</code>.
**Tags:** k8s::kcna src::session topic::annotations topic::api

---

<!-- note:1793808422523 model:Cloze -->
**Text:** Record a build version on a pod imperatively:<br><br><code>kubectl {{c1::annotate}} pod web {{c2::build-version}}={{c3::v1.4.2}}</code>
**Back Extra:** Same shape as <code>kubectl label</code>: &lt;resource&gt; &lt;name&gt; &lt;key&gt;=&lt;value&gt;. Re-running with an existing key fails unless you add <code>--overwrite</code>. Remove with a trailing minus: <code>kubectl annotate pod web build-version-</code>. In YAML the same data sits under metadata.annotations.
**Tags:** k8s::kcna src::session topic::annotations topic::kubectl

---

<!-- note:1793809412430 model:Many -->
**Domain:** Taints - effects
**Question:** Which taint effect removes ALREADY-RUNNING pods from a node if they don't tolerate it?
**Options:** A. NoSchedule<br>B. PreferNoSchedule<br>C. NoExecute<br>D. Evict
**Answer:** C (3) – NoExecute
**Explanation:** NoSchedule: no new pods without a matching toleration (existing pods stay). PreferNoSchedule: soft version — scheduler tries to avoid but no guarantee. NoExecute: evicts running pods that don't tolerate it (immediately, or after tolerationSeconds if set) AND blocks new ones.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/" target="_blank">Kubernetes Documentation - Taints and Tolerations</a>
**Tags:** k8s::kcna src::session topic::scheduling topic::taints

---

<!-- note:1793809412431 model:Many -->
**Domain:** Taints - toleration semantics
**Question:** A pod tolerates node1's taint. Is it guaranteed to be scheduled on node1?
**Options:** A. Yes — a matching toleration binds the pod to that node<br>B. No — a toleration only PERMITS placement; nodeAffinity/nodeSelector attracts pods to nodes<br>C. Yes — but only for NoSchedule taints<br>D. No — tolerations and taints are unrelated
**Answer:** B (2) – no — a toleration only PERMITS placement; nodeAffinity/nodeSelector attracts pods to nodes
**Explanation:** Tolerations are a pass, not a magnet: the scheduler may still place the pod on any node — tainted or untainted. Taints REPEL (set on nodes); affinity/nodeSelector ATTRACT (set on pods). For 'must run on node X' you combine them: taint the node to keep others out + nodeAffinity on the pod to pin it there.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/" target="_blank">Kubernetes Documentation - Taints and Tolerations</a>
**Tags:** k8s::kcna src::session topic::scheduling topic::taints

---

<!-- note:1793809412432 model:Many -->
**Domain:** Taints - control plane
**Question:** Why don't regular workload pods land on the control-plane node by default?
**Options:** A. Pods can't reach the control-plane network<br>B. kubelet refuses to run user pods on it<br>C. The control-plane node carries a default taint (node-role.kubernetes.io/control-plane:NoSchedule) that user pods don't tolerate<br>D. Control-plane nodes only accept static pods
**Answer:** C (3) – the control-plane node carries a default taint (node-role.kubernetes.io/control-plane:NoSchedule) that user pods don't tolerate
**Explanation:** kubeadm clusters taint control-plane nodes by default (node-role.kubernetes.io/control-plane:NoSchedule) so workloads stay off them — protection, not magic. DaemonSets and system pods carry matching tolerations. You CAN remove the taint (<code>kubectl taint nodes &lt;cp&gt; node-role.kubernetes.io/control-plane:NoSchedule-</code>) e.g. on single-node labs like minikube — it's just not done on real clusters.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/" target="_blank">Kubernetes Documentation - Taints and Tolerations</a>
**Tags:** k8s::kcna src::session topic::architecture topic::taints

---

<!-- note:1793809412438 model:Basic (and reversed card) -->
**Front:** Taints vs tolerations — which object gets which, and what's the pair for?
**Back:** A scheduling restriction pair: <b>taints on NODES repel</b> pods (the node says 'stay away unless allowed'); <b>tolerations on PODS</b> let them bypass a matching taint. Effect: keeps pods off unsuitable nodes — dedicated hardware, control plane, special workloads. Tolerations permit but never attract — pods can still land anywhere.
**Tags:** k8s::kcna src::session topic::scheduling topic::taints

---

<!-- note:1793809412490 model:Cloze -->
**Text:** Taint node1 so only pods tolerating <code>dedicated=gpu</code> may schedule:<br><br><code>kubectl taint nodes node1 {{c1::dedicated=gpu}}:{{c2::NoSchedule}}</code>
**Back Extra:** Format: <code>kubectl taint nodes &lt;node&gt; &lt;key&gt;=&lt;value&gt;:&lt;effect&gt;</code>. Remove a taint by appending a minus: <code>kubectl taint nodes node1 dedicated=gpu:NoSchedule-</code>. Effects: NoSchedule / PreferNoSchedule / NoExecute.
**Tags:** k8s::kcna src::session topic::kubectl topic::taints

---

<!-- note:1793809412491 model:Cloze -->
**Text:** Pod spec tolerating a <code>dedicated=gpu:NoSchedule</code> taint — fields under <code>{{c1::spec.tolerations}}</code>:<br><br><code>tolerations:<br>- key: {{c2::"dedicated"}}<br>  operator: {{c3::"Equal"}}<br>  value: {{c4::"gpu"}}<br>  effect: {{c5::"NoSchedule"}}</code>
**Back Extra:** operator defaults to Equal (needs a matching value); Exists matches the key regardless of value (omit 'value'). Effect must equal the taint's effect. Add tolerationSeconds: 3600 under a NoExecute toleration to survive the taint for one hour before eviction.
**Tags:** k8s::kcna src::session topic::taints topic::yaml

---

<!-- note:1793810135656 model:Many -->
**Domain:** NodeSelector - limitations
**Question:** Can spec.nodeSelector express 'run on nodes labelled size=large OR size=medium'?
**Options:** A. Yes — separate values with commas<br>B. No — nodeSelector only does equality-AND on labels; OR/prefer logic needs nodeAffinity/nodeAntiAffinity<br>C. Yes — use a YAML list under nodeSelector<br>D. Yes — use two nodeSelector blocks
**Answer:** B (2) – no — nodeSelector only does equality-AND on labels; OR/prefer logic needs nodeAffinity/nodeAntiAffinity
**Explanation:** nodeSelector accepts only exact key=value pairs, ANDed together — you can't say 'large OR medium', 'not small', or 'prefer fast'. Node affinity adds expressive rules: the In operator (size In [large, medium]), NotIn, plus requiredDuringScheduling (hard) vs preferredDuringScheduling (soft) terms. Anti-affinity is the inverse — keep pods OFF matching nodes (or spread them).
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Documentation - Assign Pods to Nodes</a>
**Tags:** k8s::kcna src::session topic::nodeselector topic::scheduling

---

<!-- note:1793810135657 model:Many -->
**Domain:** NodeSelector - hard requirement
**Question:** A pod has spec.nodeSelector {size: large} but NO node carries that label. What happens?
**Options:** A. It schedules anyway on a random node<br>B. It's deleted after a timeout<br>C. It stays Pending/unschedulable until a node with matching labels appears<br>D. kubelet runs it on the control-plane node
**Answer:** C (3) – it stays Pending/unschedulable until a node with matching labels appears
**Explanation:** nodeSelector is a HARD constraint — the scheduler won't place the pod anywhere else and won't retry-error; the pod just sits unscheduled. Events show '0/N nodes are available'. Fixes: label a node, relax the selector, or switch to nodeAffinity preferredDuringScheduling for a soft preference.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Documentation - Assign Pods to Nodes</a>
**Tags:** k8s::kcna src::session topic::nodeselector topic::scheduling

---

<!-- note:1793810135666 model:Basic (and reversed card) -->
**Front:** What is <code>spec.nodeSelector</code> on a pod?
**Back:** A pod-spec field holding key-value pairs that constrain WHERE the pod may run: the scheduler only picks nodes whose labels satisfy ALL listed pairs. <code>spec.nodeSelector: {size: large}</code> = 'nodes labelled size=large only'. It's the simplest node-constraint mechanism — hard equality matching only, no OR/preferences.
**Tags:** k8s::kcna src::session topic::nodeselector topic::scheduling

---

<!-- note:1793810135683 model:Basic -->
**Front:** Recipe: pin a pod to SSD nodes using nodeSelector
**Back:** Two steps, in order: 1) LABEL the node — <code>kubectl label nodes node1 disktype=ssd</code>. 2) Add the selector in the pod spec — <code>spec.nodeSelector: {disktype: ssd}</code>. The nodeSelector never labels anything itself; it only matches labels nodes already carry. Labels on the node, selector on the pod.
**Tags:** k8s::kcna src::session topic::nodeselector topic::scheduling

---

<!-- note:1793810943058 model:Many -->
**Domain:** NodeAffinity - types
**Question:** Which node affinity type schedules the pod ANYWAY when no node satisfies the rule?
**Options:** A. requiredDuringSchedulingIgnoredDuringExecution<br>B. preferredDuringSchedulingIgnoredDuringExecution<br>C. requiredDuringSchedulingRequiredDuringExecution<br>D. softDuringScheduling
**Answer:** B (2) – preferredDuringSchedulingIgnoredDuringExecution
**Explanation:** requiredDuringSchedulingIgnoredDuringExecution is the HARD type: no matching node = pod stays Pending (like nodeSelector but expressive). preferredDuringSchedulingIgnoredDuringExecution is SOFT: scheduler scores matching nodes higher using weight 1-100, but schedules anyway if none match. The 'IgnoredDuringExecution' suffix on BOTH means label changes after scheduling don't evict the pod.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Documentation - Assign Pods to Nodes</a>
**Tags:** k8s::kcna src::session topic::affinity topic::scheduling

---

<!-- note:1793810943059 model:Many -->
**Domain:** NodeAffinity - IgnoredDuringExecution
**Question:** A pod required a node label via nodeAffinity, gets scheduled, then the node's label is REMOVED. What does 'IgnoredDuringExecution' mean happens?
**Options:** A. The pod is evicted when the label changes<br>B. The pod reschedules to a compliant node<br>C. Nothing — node label changes after scheduling don't evict the pod<br>D. The pod enters a failed state
**Answer:** C (3) – nothing — node label changes after scheduling don't evict the pod
**Explanation:** Affinity rules are evaluated only at SCHEDULING time. Once bound, the pod is immune to node-label changes: if the node loses its 'size=large' label later, the pod keeps running. (Contrast: NoExecute taints DO evict.) The never-implemented RequiredDuringExecution variant would have evicted — hence the verbose naming.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Documentation - Assign Pods to Nodes</a>
**Tags:** k8s::kcna src::session topic::affinity topic::scheduling

---

<!-- note:1793810943060 model:Many -->
**Domain:** NodeAffinity - match logic
**Question:** How are nodeSelectorTerms and the matchExpressions inside them logically combined?
**Options:** A. Both ORed<br>B. Terms ORed, expressions ANDed — pod needs any ONE term fully satisfied<br>C. Both ANDed<br>D. Terms ANDed, expressions ORed
**Answer:** B (2) – terms ORed, expressions ANDed — pod needs any ONE term fully satisfied
**Explanation:** Two levels of logic inside requiredDuringScheduling...: the list nodeSelectorTerms[] is ORed (match ANY term); the matchExpressions[] inside ONE term are ANDed (ALL expressions in that term must match). Bonus: if both nodeSelector AND nodeAffinity are set on a pod, BOTH must be satisfied.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Documentation - Assign Pods to Nodes</a>
**Tags:** k8s::kcna src::session topic::affinity topic::scheduling

---

<!-- note:1793810943061 model:Many -->
**Domain:** NodeAffinity - operators
**Question:** With nodeAffinity matchExpressions, how do you require a pod to avoid nodes labelled zone=east?
**Options:** A. operator: NotIn (or DoesNotExist for 'label absent' — anti-affinity behavior)<br>B. operator: Exclude<br>C. operator: NotEqual<br>D. operator: Neq
**Answer:** A (1) – operator: NotIn (or DoesNotExist for 'label absent' — anti-affinity behavior)
**Explanation:** matchExpressions operators: In (value in list — this gives the OR nodeSelector lacks: size In [large, medium]), NotIn (value NOT in list), Exists (key present, any value), DoesNotExist (key absent), Gt/Lt (integer compare). NotIn and DoesNotExist are how you express node ANTI-affinity — keep pods off matching nodes.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Documentation - Assign Pods to Nodes</a>
**Tags:** k8s::kcna src::session topic::affinity topic::scheduling

---

<!-- note:1793810943068 model:Basic (and reversed card) -->
**Front:** What is node affinity — and what does it add over nodeSelector?
**Back:** The expressive version of nodeSelector — pod-specified rules under <code>spec.affinity.nodeAffinity</code> that attract pods to (or repel from) nodes based on node labels. Adds what nodeSelector lacks: OR logic (values lists, multiple terms), NOT operators (NotIn/DoesNotExist = anti-affinity), and SOFT preferences (preferredDuringScheduling... with weights). Exists purely to control pod placement.
**Tags:** k8s::kcna src::session topic::affinity topic::scheduling

---

<!-- note:1793810943076 model:Cloze -->
**Text:** Require the pod on large-or-medium nodes via affinity:<br><br><code>spec:<br>  affinity:<br>    {{c1::nodeAffinity}}:<br>      {{c2::requiredDuringSchedulingIgnoredDuringExecution}}:<br>        {{c3::nodeSelectorTerms}}:<br>        - {{c4::matchExpressions}}:<br>          - {key: size, operator: {{c5::In}}, values: [large, medium]}</code>
**Back Extra:** Hierarchy: spec.affinity.nodeAffinity.&lt;type&gt;.nodeSelectorTerms[].matchExpressions[] — each expression is {key, operator, values[]}. values is a LIST (In = OR across values). Preferred type uses - weight: N / preference: matchExpressions instead of plain terms.
**Tags:** k8s::kcna src::session topic::affinity topic::yaml

---

<!-- note:1793820261525 model:Many -->
**Domain:** Resources - units
**Question:** In a container spec, what does <code>cpu: 250m</code> request?
**Options:** A. 250 CPU cores<br>B. 250 megahertz<br>C. 0.25 of one CPU core<br>D. 250 megabytes of RAM
**Answer:** C (3) – 0.25 of one CPU core
**Explanation:** CPU is measured in cores: 1 = one full (v)CPU/hyperthread, and m = millicores (1/1000) — 250m = 0.25 core, 500m = half. Memory uses bytes with suffixes: Mi/Gi = mebibytes/gibibytes (2^20, 2^30 — binary), M/G = megabytes/gigabytes (10^6, 10^9 — decimal). Requests/limits accept either but Mi/Gi is the convention.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/" target="_blank">Kubernetes Documentation - Resource Management for Pods and Containers</a>
**Tags:** k8s::kcna src::session topic::resources topic::scheduling

---

<!-- note:1793820261526 model:Many -->
**Domain:** Resources - scheduler accounting
**Question:** Every node's allocatable CPU minus existing pods' requests is BELOW a new pod's request. What happens?
**Options:** A. Schedules anyway — limits are what count<br>B. Stays Pending — scheduler sums requests already on each node against node allocatable; nowhere fits<br>C. Schedules on the least-loaded node regardless<br>D. Kubernetes reduces the request automatically
**Answer:** B (2) – stays Pending — scheduler sums requests already on each node against node allocatable; nowhere fits
**Explanation:** The scheduler filters on REQUESTS (not limits, not actual usage): a node fits if allocatable − sum(existing pod requests) ≥ new pod's request. 4-CPU allocatable with 3.5 CPU already requested leaves 0.5 — a 1-CPU request fails the filter everywhere → pod Pending until capacity frees or a node is added. Limits don't factor into this math.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/" target="_blank">Kubernetes Documentation - Resource Management for Pods and Containers</a>
**Tags:** k8s::kcna src::session topic::resources topic::scheduling

---

<!-- note:1793820261527 model:Many -->
**Domain:** Resources - LimitRange defaulting
**Question:** A pod manifest sets NO resources, but its namespace has a LimitRange with defaults. What happens at creation?
**Options:** A. The pod is rejected<br>B. The LimitRange admission controller injects the namespace's default requests/limits<br>C. It gets zero resources<br>D. kubelet assigns values at runtime
**Answer:** B (2) – the LimitRange admission controller injects the namespace's default requests/limits
**Explanation:** LimitRange does double duty in a namespace: it VALIDATES min/max bounds and supplies DEFAULTS. A pod omitting resources gets the LimitRange defaults patched in at admission time — so quota accounting works even for lazy manifests. If the defaults don't exist either, the pod gets no requests (scheduler treats it as ~0 → QoS BestEffort).
**Sources:** <a href="https://kubernetes.io/docs/concepts/policy/limit-range/" target="_blank">Kubernetes Documentation - Limit Ranges</a>
**Tags:** k8s::kcna src::session topic::namespaces topic::resources

---

<!-- note:1793820261535 model:Basic (and reversed card) -->
**Front:** resources.requests vs resources.limits — what does each actually do?
**Back:** <b>requests</b> = the reservation — what the scheduler assumes the container needs, used to pick a node (guaranteed share at runtime). <b>limits</b> = the ceiling — how much it may use AT MOST. Exceed the CPU limit → throttled; exceed the memory limit → the container is killed (OOMKilled) and restarted per restartPolicy. Rule: requests for scheduling, limits for containment.
**Tags:** k8s::kcna src::session topic::containers topic::resources

---

<!-- note:1793821101844 model:Many -->
**Domain:** Resources - defaulting
**Question:** A container declares <code>limits: {cpu: 250m}</code> and no requests. What's its effective cpu request?
**Options:** A. requests.cpu stays unset (0)<br>B. requests.cpu also becomes 250m — the request defaults to the limit<br>C. The pod is rejected as invalid<br>D. The limit is ignored
**Answer:** B (2) – requests.cpu also becomes 250m — the request defaults to the limit
**Explanation:** When a container sets a limit but no request, Kubernetes copies the limit value INTO the request. The reverse is not true: a request alone leaves the limit unset (container may burst beyond it). One-directional rule: limit → fills request; request → limit stays empty.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/" target="_blank">Kubernetes Documentation - Resource Management</a>
**Tags:** k8s::kcna src::session topic::containers topic::resources

---

<!-- note:1793821101845 model:Many -->
**Domain:** Resources - sizing strategy
**Question:** What's a common sizing recommendation for Deployments?
**Options:** A. Set limits on everything, requests optional<br>B. Set neither — Kubernetes handles it<br>C. Requests everywhere, limits carefully — lets pods burst into idle capacity instead of being throttled<br>D. Only limits matter — requests are optional metadata
**Answer:** C (3) – requests everywhere, limits carefully — lets pods burst into idle capacity instead of being throttled
**Explanation:** A common recommendation: always set requests (scheduling + guarantees) but leave CPU limits off — a container over its limit gets THROTTLED even while the node sits idle, needlessly slowing bursts. Memory is different: it can't be throttled, only reclaimed by killing (OOMKilled), so memory limits still earn their place. Defaults: no request/no limit = BestEffort, evicted first under pressure.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/" target="_blank">Kubernetes Documentation - Resource Management</a>
**Tags:** k8s::kcna src::session topic::containers topic::resources

---

<!-- note:1793821101846 model:Many -->
**Domain:** Resources - quota coupling
**Question:** A namespace's ResourceQuota covers cpu. What does that force on new pods?
**Options:** A. Nothing — quota only tracks usage<br>B. Every new pod must specify cpu (request or limit); pods without it are rejected (403)<br>C. Existing pods are rescheduled<br>D. The namespace gets locked
**Answer:** B (2) – every new pod must specify cpu (request or limit); pods without it are rejected (403)
**Explanation:** A ResourceQuota covering cpu or memory forces the issue: any new pod lacking a request OR limit for that resource gets rejected with 403 Forbidden at admission — there's nothing to charge the quota against. That's exactly why LimitRange pairs with ResourceQuota: LimitRange injects defaults so manifests still get accepted. Quota violations never affect already-running pods.
**Sources:** <a href="https://kubernetes.io/docs/concepts/policy/resource-quotas/" target="_blank">Kubernetes Documentation - Resource Quotas</a>
**Tags:** k8s::kcna src::session topic::namespaces topic::resources

---

<!-- note:1793821101854 model:Basic (and reversed card) -->
**Front:** What problem do resource requests and limits solve?
**Back:** Without limits one pod can consume ALL of a node's CPU/memory — starving every other workload on it ('noisy neighbor'). requests fix placement: the scheduler guarantees the pod its share and won't overbook the node. limits fix containment: CPU over-limit → throttled; memory over-limit → OOMKilled, because memory can't be throttled — you can't take RAM back from a process except by killing it.
**Tags:** k8s::kcna src::session topic::resources topic::scheduling

---

<!-- note:1793821101864 model:Cloze -->
**Text:** LimitRange manifest — sets defaults + bounds for containers in its namespace:<br><br><code>apiVersion: {{c1::v1}}<br>kind: {{c2::LimitRange}}<br>metadata: {name: limits}<br>spec:<br>  {{c3::limits}}:<br>  - {{c4::default}}: {cpu: 500m}        # default limit<br>    {{c5::defaultRequest}}: {cpu: 100m} # default request<br>    max: {cpu: "1"}<br>    min: {cpu: 100m}<br>    {{c6::type}}: Container</code>
**Back Extra:** spec.limits[] is a list; each entry has default (default LIMIT), defaultRequest (default request), max, min, and type (Container or PersistentVolumeClaim). Only enforced at admission — existing pods keep their values. Two LimitRanges in one namespace → nondeterministic defaults.
**Tags:** topic::resources topic::yaml

---

<!-- note:1793821101865 model:Cloze -->
**Text:** ResourceQuota manifest — aggregate caps for one namespace:<br><br><code>apiVersion: {{c1::v1}}<br>kind: {{c2::ResourceQuota}}<br>metadata:<br>  name: compute-quota<br>  namespace: {{c3::dev}}<br>spec:<br>  {{c4::hard}}:<br>    {{c5::requests.cpu}}: "4"<br>    requests.memory: 4Gi<br>    {{c6::limits.cpu}}: "8"<br>    pods: "10"</code>
**Back Extra:** spec.hard maps resource names → totals for the namespace: requests.cpu/requests.memory, limits.cpu/limits.memory, plus object counts (pods, services, persistentvolumeclaims). Exceeding any entry → new object rejected with 403. A cpu/memory quota forces every pod to declare that resource — pair it with LimitRange for defaults.
**Tags:** topic::namespaces topic::yaml

---

<!-- note:1793822816861 model:Many -->
**Domain:** DaemonSet - scheduling
**Question:** How does a DaemonSet actually get its pods onto each node?
**Options:** A. It sets spec.nodeName directly — no scheduler involved<br>B. The DaemonSet controller creates a pod per node with a nodeAffinity pinning it to that hostname; the default scheduler then binds it<br>C. kubelet on each node pulls the template itself<br>D. The ReplicationController schedules copies to nodes
**Answer:** B (2) – the DaemonSet controller creates a pod per node with a nodeAffinity pinning it to that hostname; the default scheduler then binds it
**Explanation:** DaemonSet pods do NOT bypass the scheduler: the controller creates one Pod per eligible node and injects nodeAffinity (matchFields metadata.name In [node]) — the DEFAULT scheduler then binds each pod to its node via spec.nodeName. You can point DS pods at a custom scheduler with spec.template.spec.schedulerName.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/" target="_blank">Kubernetes Documentation - DaemonSet</a>
**Tags:** k8s::kcna src::session topic::daemonsets topic::scheduling

---

<!-- note:1793822816862 model:Many -->
**Domain:** DaemonSet - lifecycle
**Question:** A cluster running a DaemonSet gets a NEW node. What happens?
**Options:** A. Nothing until the next reconcile<br>B. The DaemonSet must be reapplied<br>C. A pod lands on the new node automatically; pods on removed nodes are garbage-collected<br>D. Only if the DS has replicas: N set
**Answer:** C (3) – a pod lands on the new node automatically; pods on removed nodes are garbage-collected
**Explanation:** The DaemonSet controller continuously reconciles: any node joining the cluster that matches the selector gets a pod; nodes leaving take their DS pods with them (garbage collection). That's the whole point vs a Deployment — replica count follows node count, not a fixed number.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/" target="_blank">Kubernetes Documentation - DaemonSet</a>
**Tags:** k8s::kcna src::session topic::daemonsets topic::scheduling

---

<!-- note:1793822816863 model:Many -->
**Domain:** DaemonSet - tolerations
**Question:** Why do DaemonSet pods keep running on nodes that become NotReady or pressure-tainted?
**Options:** A. They get special scheduler priority only<br>B. Automatic tolerations — the controller adds not-ready/unreachable/pressure tolerations so DS pods survive node problems<br>C. Nothing — DS pods are immune by default<br>D. The nodeName field bypasses taints
**Answer:** B (2) – automatic tolerations — the controller adds not-ready/unreachable/pressure tolerations so DS pods survive node problems
**Explanation:** The DaemonSet controller pre-adds tolerations: node.kubernetes.io/not-ready (NoExecute), unreachable (NoExecute), disk/memory/pid-pressure (NoSchedule) — so node agents keep running through failures (when they're needed MOST). To also land on control-plane nodes, the template must tolerate node-role.kubernetes.io/control-plane explicitly.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/" target="_blank">Kubernetes Documentation - DaemonSet</a>
**Tags:** k8s::kcna src::session topic::daemonsets topic::taints

---

<!-- note:1793822816871 model:Basic (and reversed card) -->
**Front:** What is a DaemonSet — and which workloads belong in one?
**Back:** A workload controller that runs ONE copy of a pod on every node (or a subset via nodeSelector/affinity in the template). Replica count follows node count — nodes joining get the pod automatically. Used for node-local agents that must exist everywhere: monitoring exporters, log collectors (fluentd), kube-proxy, CNI plugins like Calico. apiVersion: apps/v1.
**Tags:** k8s::kcna src::session topic::daemonsets topic::workloads

---

<!-- note:1793822816917 model:Cloze -->
**Text:** DaemonSet manifest skeleton (fluentd on every node):<br><br><code>apiVersion: {{c1::apps/v1}}<br>kind: {{c2::DaemonSet}}<br>metadata: {name: fluentd}<br>spec:<br>  {{c3::selector}}:<br>    {{c4::matchLabels}}: {name: fluentd}<br>  {{c5::template}}:<br>    metadata: {labels: {name: fluentd}}<br>    spec: {containers: [...], restartPolicy: {{c6::Always}}}</code>
**Back Extra:** Same skeleton as a Deployment MINUS the replicas field — count is implied (one per node). selector.matchLabels must equal template.metadata.labels and is immutable after creation. Pod template's restartPolicy must be Always (default). Add spec.template.spec.nodeSelector/affinity to cover only a subset of nodes.
**Tags:** k8s::kcna src::session topic::daemonsets topic::yaml

---

<!-- note:1793823868597 model:Many -->
**Domain:** Static Pods - mirror pods
**Question:** <code>kubectl get pods</code> shows 'static-web-my-node1' — you kubectl delete it and it instantly reappears. What is it and how do you actually remove it?
**Options:** A. The pod is stuck terminating<br>B. RBAC is blocking the delete<br>C. It's a mirror of a static pod — the kubelet manages it from a manifest file on the node; delete the file, not the object<br>D. The pod has a finalizer
**Answer:** C (3) – it's a mirror of a static pod — the kubelet manages it from a manifest file on the node; delete the file, not the object
**Explanation:** The kubelet creates a read-only MIRROR of each static pod in the API server (named &lt;pod&gt;-&lt;nodename&gt;) so kubectl visibility works. Deleting the mirror does nothing — kubelet's source of truth is the manifest file in staticPodPath (e.g. /etc/kubernetes/manifests). To change/kill the pod: edit or remove the file ON THE NODE.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/" target="_blank">Kubernetes Documentation - Create static Pods</a>
**Tags:** k8s::kcna src::session topic::pods topic::staticpods

---

<!-- note:1793823868598 model:Many -->
**Domain:** Static Pods - limitations
**Question:** Which object kinds can a kubelet create from the static pod manifest directory?
**Options:** A. Any workload object<br>B. Only Pods — kubelet understands no other kind; no Deployments, ReplicaSets or Services<br>C. Pods and Services only<br>D. Pods and ConfigMaps
**Answer:** B (2) – only Pods — kubelet understands no other kind; no Deployments, ReplicaSets or Services
**Explanation:** Static manifests must be kind: Pod, apiVersion: v1 — nothing else exists without the API server. There's no controller to honor replicas, no scheduler (the pod lands on this node, period), no etcd. The kubelet alone watches the directory, creates the pod, and restarts it on failure — a one-node control loop.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/" target="_blank">Kubernetes Documentation - Create static Pods</a>
**Tags:** k8s::kcna src::session topic::kubelet topic::staticpods

---

<!-- note:1793823868599 model:Many -->
**Domain:** Static Pods - control plane
**Question:** In a kubeadm cluster, how do kube-apiserver, etcd and friends actually run on the control-plane node?
**Options:** A. As a Deployment in kube-system<br>B. As systemd services only<br>C. As static pods — kubelet runs them from manifests in /etc/kubernetes/manifests, no API server dependency<br>D. As DaemonSet pods
**Answer:** C (3) – as static pods — kubelet runs them from manifests in /etc/kubernetes/manifests, no API server dependency
**Explanation:** Kubeadm clusters bootstrap the control plane via static pods: manifests for kube-apiserver, etcd, kube-controller-manager and kube-scheduler sit in /etc/kubernetes/manifests and the kubelet runs them. Elegant because the control plane can't be hosted by the cluster it's bootstrapping — kubelet is the only piece that must exist first.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/" target="_blank">Kubernetes Documentation - Create static Pods</a>
**Tags:** k8s::kcna src::session topic::architecture topic::staticpods

---

<!-- note:1793823868607 model:Basic (and reversed card) -->
**Front:** What is a static pod?
**Back:** A pod created and managed directly by the kubelet — no API server, no scheduler, no controller. The kubelet periodically scans a configured directory (staticPodPath in the KubeletConfiguration, commonly /etc/kubernetes/manifests; deprecated flag: <code>--pod-manifest-path</code>) and runs every pod manifest found there, restarting them on failure. For visibility it mirrors each into the API server as a read-only object.
**Tags:** topic::pods topic::staticpods

---

<!-- note:1793823868617 model:Cloze -->
**Text:** Enable static pods via kubelet config file:<br><br><code>apiVersion: {{c1::kubelet.config.k8s.io/v1beta1}}<br>kind: {{c2::KubeletConfiguration}}<br>{{c3::staticPodPath}}: {{c4::/etc/kubernetes/manifests}}</code><br><br>then <code>systemctl {{c5::restart}} kubelet</code>
**Back Extra:** staticPodPath points kubelet at a directory it scans periodically — pod YAMLs appearing there get created, files removed get their pods deleted. Deprecated alternative: <code>--pod-manifest-path</code> flag. Web-hosted variant: staticPodURL / <code>--manifest-url</code>. Check the live kubelet's config on the node (e.g. /var/lib/kubelet/config.yaml) or ps aux | grep kubelet for the flag.
**Tags:** k8s::kcna src::session topic::kubelet topic::staticpods

---

<!-- note:1793835711168 model:Many -->
**Domain:** Schedulers - selection
**Question:** How does a pod say 'schedule me with my-scheduler, not the default'?
**Options:** A. A label on the pod<br>B. spec.schedulerName must equal the scheduler's unique name<br>C. An annotation requesting it<br>D. The pod's namespace
**Answer:** B (2) – spec.schedulerName must equal the scheduler's unique name
**Explanation:** Each scheduler owns a unique name cluster-wide (the default is 'default-scheduler'). A pod opts in via spec.schedulerName: my-scheduler — unset means the default scheduler claims it. Two schedulers never fight over a pod: each only watches unbound pods bearing its own name.
**Sources:** <a href="https://kubernetes.io/docs/tasks/extend-kubernetes/configure-multiple-schedulers/" target="_blank">Kubernetes Documentation - Configure Multiple Schedulers</a>
**Tags:** k8s::kcna src::session topic::pods topic::scheduling

---

<!-- note:1793835711169 model:Many -->
**Domain:** Schedulers - profiles
**Question:** How can one kube-scheduler process act as several different schedulers?
**Options:** A. It can't — you must run separate binaries<br>B. <code>--replicas</code> flag on kube-scheduler<br>C. KubeSchedulerConfiguration profiles[] — one process, multiple profiles, each with its own schedulerName<br>D. Namespaces scope the schedulers
**Answer:** C (3) – KubeSchedulerConfiguration profiles[] — one process, multiple profiles, each with its own schedulerName
**Explanation:** Profiles let ONE kube-scheduler binary wear multiple hats: the config's profiles[] list gives each profile a distinct schedulerName + its own plugin config, and pods pick a profile via spec.schedulerName — but only a single scheduler process runs. Alternative: separate scheduler PROCESSES (e.g. a second kube-scheduler Deployment with its own config/name). Both patterns give 'multiple schedulers'.
**Sources:** <a href="https://kubernetes.io/docs/tasks/extend-kubernetes/configure-multiple-schedulers/" target="_blank">Kubernetes Documentation - Configure Multiple Schedulers</a>
**Tags:** k8s::kcna src::session topic::api topic::scheduling

---

<!-- note:1793835711170 model:Many -->
**Domain:** Schedulers - naming
**Question:** What constraint applies to a scheduler's name in the cluster?
**Options:** A. Must equal the pod's name<br>B. Unique per scheduler cluster-wide — it's the identity pods reference in spec.schedulerName<br>C. Can be shared across schedulers<br>D. Is always 'default-scheduler'
**Answer:** B (2) – unique per scheduler cluster-wide — it's the identity pods reference in spec.schedulerName
**Explanation:** The schedulerName is how kube-scheduler instances/profile claim ownership of pods — collisions mean two processes racing to bind the same pods. The stock scheduler answers to 'default-scheduler'; your second scheduler (or profile) needs its own name like 'my-scheduler', set in KubeSchedulerConfiguration profiles[].schedulerName.
**Sources:** <a href="https://kubernetes.io/docs/tasks/extend-kubernetes/configure-multiple-schedulers/" target="_blank">Kubernetes Documentation - Configure Multiple Schedulers</a>
**Tags:** k8s::kcna src::session topic::api topic::scheduling

---

<!-- note:1793835711180 model:Basic -->
**Front:** Can a cluster run more than one scheduler — and why would it?
**Back:** Yes — a cluster can run several schedulers side by side. Each has a unique name and only watches unbound pods whose <code>spec.schedulerName</code> matches it; pods default to 'default-scheduler'. Use cases: custom placement logic, batch/ML schedulers, testing new scheduling behavior. Deploy one as a Deployment running a second kube-scheduler binary with its own config.
**Tags:** k8s::kcna src::session topic::architecture topic::scheduling

---

<!-- note:1793835711181 model:Basic -->
**Front:** How do you deploy a second scheduler (e.g. 'my-scheduler') into a cluster?
**Back:** The docs' recipe: 1) containerize kube-scheduler, 2) Deployment (kube-system, replicas:1) running <code>kube-scheduler --config=&lt;file&gt;</code>, 3) a ConfigMap holding a <code>KubeSchedulerConfiguration</code> with <code>profiles: [{schedulerName: my-scheduler}]</code> and <code>leaderElect: false</code>, 4) a ServiceAccount bound to <code>system:kube-scheduler</code> ClusterRole so it can watch/bind pods. Pods opt in via <code>spec.schedulerName: my-scheduler</code>.
**Tags:** k8s::kcna src::session topic::scheduling topic::yaml

---

<!-- note:1793836413421 model:Many -->
**Domain:** Scheduling - filter phase
**Question:** Which scheduling step eliminates nodes that CAN'T run the pod (resources, taints, selectors)?
**Options:** A. QueueSort — orders the queue<br>B. Filter — every plugin marks each node feasible or infeasible; survivors move on<br>C. Score — ranks nodes<br>D. Bind — writes the decision
**Answer:** B (2) – Filter — every plugin marks each node feasible or infeasible; survivors move on
**Explanation:** Filter plugins eliminate nodes that CANNOT run the pod: insufficient resources vs requests, taints without tolerations, nodeSelector/affinity mismatch, port conflicts. Each node is evaluated until one plugin rejects it (short-circuit); anything surviving is 'feasible'. If zero nodes pass → PostFilter kicks in (preemption: evict lower-priority pods to make room) or the pod stays Pending.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/" target="_blank">Kubernetes Documentation - Scheduling Framework</a>
**Tags:** k8s::kcna src::session topic::pods topic::scheduling

---

<!-- note:1793836413422 model:Many -->
**Domain:** Scheduling - score phase
**Question:** Filtering left 5 feasible nodes. How does the scheduler pick ONE?
**Options:** A. Filter plugins re-run<br>B. First feasible node wins<br>C. Score plugins rank the feasible nodes (weighted scores); highest wins, ties broken randomly<br>D. kubelet picks
**Answer:** C (3) – Score plugins rank the feasible nodes (weighted scores); highest wins, ties broken randomly
**Explanation:** After filtering leaves multiple feasible nodes, each Score plugin (e.g. NodeResourcesFit, ImageLocality) assigns every node a number; NormalizeScore scales them, weights combine them into a total per node. The pod binds to the highest total — equal scores → random choice. This is the 'prefer' side of scheduling: all surviving nodes CAN run it, scoring picks the best.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/" target="_blank">Kubernetes Documentation - Scheduling Framework</a>
**Tags:** k8s::kcna src::session topic::pods topic::scheduling

---

<!-- note:1793836413423 model:Many -->
**Domain:** Scheduling - queue sort
**Question:** How does the scheduler order pods waiting in its internal scheduling queue?
**Options:** A. FIFO — creation time<br>B. By pod priority — the QueueSort plugin (default PrioritySort) orders the queue, high-priority pods first<br>C. Alphabetically by namespace<br>D. By resource size, smallest first
**Answer:** B (2) – by pod priority — the QueueSort plugin (default PrioritySort) orders the queue, high-priority pods first
**Explanation:** Before anything else, pods wait in the scheduler's internal queue. The QueueSort extension point decides order — only ONE QueueSort plugin may be enabled — and the default, PrioritySort, sorts by pod priority so important workloads get scheduled first. That's why PriorityClass exists: it moves pods up the queue AND drives preemption.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/" target="_blank">Kubernetes Documentation - Scheduling Framework</a>
**Tags:** k8s::kcna src::session topic::pods topic::scheduling

---

<!-- note:1793836413424 model:Many -->
**Domain:** Scheduling - profiles rationale
**Question:** Why did Kubernetes add scheduling PROFILES instead of just recommending multiple scheduler deployments?
**Options:** A. Profiles are faster<br>B. Two schedulers double throughput<br>C. Separate scheduler processes can race each other on the same node; profiles give one process multiple configured personalities<br>D. Profiles enable leader election
**Answer:** C (3) – separate scheduler processes can race each other on the same node; profiles give one process multiple configured personalities
**Explanation:** Multiple scheduler PROCESSES each see only their own queue and can pick the same node concurrently — the loser discovers the conflict at bind time (retry, wasted work). Profiles (stable since v1.19) let ONE kube-scheduler expose several schedulerNames, each with its own plugin config — variety without a second process and without the race window.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/" target="_blank">Kubernetes Documentation - Scheduling Framework</a>
**Tags:** k8s::kcna src::session topic::api topic::scheduling

---

<!-- note:1793836413442 model:Basic (and reversed card) -->
**Front:** How does the kube-scheduler place a pod, step by step?
**Back:** Two cycles: the <b>scheduling cycle</b> (serial — one pod at a time) runs QueueSort → Filter → Score and PICKS a node; the <b>binding cycle</b> (concurrent) applies it via a Binding object → writes <code>spec.nodeName</code>. Between them sits Reserve — marks the node's resources as taken so concurrent binds can't collide. Failed/aborted cycles return the pod to the queue for a retry.
**Tags:** k8s::kcna src::session topic::pods topic::scheduling

---

<!-- note:1793836413443 model:Basic (and reversed card) -->
**Front:** What are scheduler plugins in kube-scheduler?
**Back:** Pluggable extension points in the scheduling framework, compiled into kube-scheduler: QueueSort (queue order), PreFilter/Filter (eliminate infeasible nodes), PostFilter (runs only if nothing fits — e.g. preemption), PreScore/Score (rank feasible nodes), Reserve (claim node before bind), Permit (approve/deny/wait), PreBind/Bind/PostBind (write the assignment). You can compile in your own and toggle them per profile.
**Tags:** k8s::kcna src::session topic::api topic::scheduling

---

<!-- note:1793836413464 model:Cloze -->
**Text:** Second profile with customized plugins:<br><br><code>apiVersion: {{c1::kubescheduler.config.k8s.io/v1}}<br>kind: {{c2::KubeSchedulerConfiguration}}<br>{{c3::profiles}}:<br>- {{c4::schedulerName}}: default-scheduler<br>- schedulerName: no-scoring<br>  {{c5::plugins}}:<br>    {{c6::score}}:<br>      {{c7::disabled}}: [{name: NodeResourcesFit}]<br>      {{c8::enabled}}: [{name: MyScorer}]</code>
**Back Extra:** Each profile = its own schedulerName (pods select via spec.schedulerName) + plugin config. plugins.&lt;extensionPoint&gt;.disabled removes stock plugins (name: '*' disables all at that point); enabled adds custom ones (compiled into the scheduler). Extension points: queueSort, preFilter, filter, postFilter, preScore, score, reserve, permit, preBind, bind, postBind.
**Tags:** topic::scheduling topic::yaml

---

<!-- note:1793837227572 model:Many -->
**Domain:** Taints - NoExecute meaning
**Question:** What does the taint effect "NoExecute" indicate in Kubernetes?
**Options:** A. Pods will be evicted immediately from the node, if they do not tolerate the taint<br>B. Pods will not be scheduled on the node.<br>C. Pods will be scheduled with a higher priority on the node.<br>D. System will try to avoid placing a pod on the node, but it is not guaranteed.
**Answer:** A (1) – Pods will be evicted immediately from the node, if they do not tolerate the taint
**Explanation:** NoExecute is the aggressive effect: it evicts running pods that don't tolerate the taint AND blocks new ones. (Pods that DO tolerate without tolerationSeconds stay forever; with tolerationSeconds they survive only that long.) The course's other options map to the remaining effects: 'pods will not be scheduled' = NoSchedule; 'try to avoid, not guaranteed' = PreferNoSchedule.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/" target="_blank">Kubernetes Documentation - Taints and Tolerations</a>
**Tags:** k8s::kcna src::session topic::scheduling topic::taints

---

<!-- note:1793837334262 model:Many -->
**Domain:** NodeAffinity - type semantics
**Question:** What does the TYPE of node affinity in Kubernetes define?
**Options:** A. How many nodes can match the rule<br>B. The scheduler's behavior regarding the rule at scheduling time AND during the pod's execution<br>C. Which node labels exist in the cluster<br>D. The weight given to preferred rules
**Answer:** B (2) – the scheduler's behavior regarding the rule at scheduling time AND during the pod's execution
**Explanation:** The type name literally spells out behavior at two lifecycle stages: 'required/preferred' + 'DuringScheduling' = hard rule (pod won't place without a match) vs soft preference (schedules anyway); 'IgnoredDuringExecution' = after the pod runs, node-label changes are ignored — no eviction. The unimplemented 'requiredDuringExecution' would have evicted on label changes.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Documentation - Assign Pods to Nodes</a>
**Tags:** k8s::kcna src::session topic::affinity topic::scheduling

---

<!-- note:1793906734606 model:Many -->
**Domain:** Security Primitives
**Question:** In which order does the kube-apiserver process an incoming request?
**Options:** A. TLS terminates, then Authentication, Authorization, Admission Control, persist to etcd<br>B. Authentication, Authorization, Admission Control, then TLS terminates<br>C. Authorization, Authentication, Admission Control, persist to etcd<br>D. Authentication, Admission Control, Authorization, persist to etcd
**Answer:** A – TLS terminates first, then Authentication, Authorization, Admission Control, then the object persists to etcd
**Explanation:** Every API request passes the same pipeline: transport security (TLS cert check) → Authentication (WHO are you — cert/token/service account) → Authorization (WHAT may you do — RBAC/ABAC/Node/Webhook) → Admission Control (mutate or reject writes, e.g. LimitRange injecting defaults, PSA). Note that admission only acts on create/update/delete/connect requests — pure reads skip it — and the object is only written to etcd after surviving all stages.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/controlling-access/" target="_blank">Kubernetes Docs - Controlling Access to the API</a>
**Tags:** k8s::kcna src::session topic::api topic::security

---

<!-- note:1793906734607 model:Many -->
**Domain:** Security Primitives
**Question:** Which mechanisms can authenticate a caller to the kube-apiserver? (Select all that apply)
**Options:** A. X.509 client certificates signed by the cluster CA<br>B. ServiceAccount tokens (JWTs)<br>C. Static token or password file<br>D. External identity providers (OIDC, webhook, LDAP)<br>E. SSH keys
**Answer:** A, B, C, D – client certs, ServiceAccount tokens, static token/password file, and external providers (OIDC/webhook/LDAP)
**Explanation:** Authentication answers WHO can access the cluster. The API server supports client certificates signed by the cluster CA, bearer tokens (static token file, bootstrap tokens, ServiceAccount JWTs), basic password auth via a static file, and external providers (OIDC, authentication webhook — which bridges LDAP/other IdPs). Multiple modules can be configured and are tried in sequence until one succeeds. SSH keys secure access to the HOSTS, not the Kubernetes API.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/controlling-access/" target="_blank">Kubernetes Docs - Controlling Access to the API</a>
**Tags:** k8s::kcna src::session topic::api topic::security

---

<!-- note:1793906734608 model:Many -->
**Domain:** Security Primitives
**Question:** Which authorization modes can the kube-apiserver enforce? (Select all that apply)
**Options:** A. RBAC — roles bound to users/groups/service accounts<br>B. ABAC — attribute-based access control policies<br>C. Node authorization — constrains kubelets to their own node's objects<br>D. Webhook — delegates the decision to an external service<br>E. OAuth — OAuth2 access tokens
**Answer:** A, B, C, D – RBAC, ABAC, Node authorization, and Webhook mode
**Explanation:** Authorization answers WHAT an authenticated caller may do. The API server can run multiple authorization modules: RBAC (role-based, the common one — Roles/ClusterRoles + bindings), ABAC (attribute-based policies on user/verb/resource), Node authorization (special mode that constrains what kubelets may read/write to the objects their node needs), and Webhook (delegates the decision to an external service). If several modules are configured, each is checked — the request proceeds if ANY module authorizes it.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/controlling-access/" target="_blank">Kubernetes Docs - Controlling Access to the API</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security

---

<!-- note:1793906734609 model:Many -->
**Domain:** Security Primitives
**Question:** Which statement about encryption between Kubernetes components is TRUE?
**Options:** A. All control-plane traffic is TLS-encrypted: kubectl→apiserver, apiserver↔etcd, and apiserver to kubelets/other components<br>B. Only kubectl→apiserver is encrypted; inter-component traffic is plain HTTP<br>C. TLS is an optional add-on installed by the CNI plugin<br>D. Components authenticate each other with bearer tokens, so TLS is unnecessary
**Answer:** A – all control-plane component traffic plus client traffic to the apiserver is TLS-encrypted
**Explanation:** TLS secures the entire control plane: kubectl/clients to kube-apiserver, apiserver to etcd, and apiserver's calls to kubelets, kube-proxy and the other components are all encrypted in transit (with a cluster CA — typically etcd, /etc/kubernetes/pki, issued by kubeadm or your own PKI). Plaintext is not a supported posture for API traffic; the 'insecure port' was removed entirely in Kubernetes 1.20.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/controlling-access/" target="_blank">Kubernetes Docs - Controlling Access to the API</a>
**Tags:** k8s::kcna src::session topic::control-plane topic::security

---

<!-- note:1793906734610 model:Many -->
**Domain:** Security Primitives
**Question:** Before applying Kubernetes-level security controls, what should be hardened first?
**Options:** A. The underlying hosts — SSH key-only auth, no password logins, patched OS<br>B. The pod manifests — set a securityContext first<br>C. The CNI plugin — enable its security features first<br>D. The container registry — sign all images first
**Answer:** A – harden the underlying hosts first: SSH key-only login, no password auth, patched OS
**Explanation:** Defense starts below Kubernetes: the cluster lives on its nodes, and a rooted node means a rooted cluster. Baseline host hardening — SSH key-only access, password auth disabled, OS patched, no unneeded services/ports — comes before any Kubernetes-level control. Only after the hosts are secured does the k8s-specific layering matter: API access control, RBAC, NetworkPolicies, pod security.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/controlling-access/" target="_blank">Kubernetes Docs - Controlling Access to the API</a>
**Tags:** k8s::kcna src::session topic::architecture topic::security

---

<!-- note:1793906741654 model:Basic (and reversed card) -->
**Front:** By default, how much pod-to-pod traffic does Kubernetes allow, and what restricts it?
**Back:** Open — the pod network is flat: every pod can reach every other pod and namespace by default (no built-in isolation). NetworkPolicy is the opt-in control: a policy selects pods (podSelector) and whitelists ingress/egress; once a pod is selected by any policy, only matching traffic is allowed. Policies are enforced by the CNI plugin — a CNI that doesn't support NetworkPolicies silently ignores them.
**Tags:** k8s::kcna src::session topic::networking topic::security

---

<!-- note:1793913170420 model:Many -->
**Domain:** Authentication
**Question:** In X.509 client-certificate authentication, how does Kubernetes map a certificate's subject to a user identity?
**Options:** A. The Issuer field becomes the username<br>B. CN maps to the username; O entries map to groups<br>C. The certificate serial number becomes the UID<br>D. Validity dates decide the session timeout
**Answer:** B – the Common Name (CN) maps to the username and Organization (O) entries map to groups
**Explanation:** Certificate attributes become identity: CN → username, each O → a group (order doesn't matter). So a cert with subject '/CN=alice/O=devs/O=ops' authenticates as user 'alice' in groups 'devs'+'ops' — plus everyone authentic'd also joins 'system:authenticated'. Signed by the cluster's client CA, the identity is then passed to authorization (RBAC) for permission checks.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Docs - Authentication</a>
**Tags:** k8s::kcna src::session topic::authentication topic::security topic::tls

---

<!-- note:1793913170421 model:Many -->
**Domain:** Authentication
**Question:** How does the static token file authentication method work?
**Options:** A. A ConfigMap listing users and passwords<br>B. A Secret of type kubernetes.io/service-account-token<br>C. CSV rows of 'token,user,uid,"groups"' served by <code>--token-auth-file</code><br>D. A users.yaml inside /etc/kubernetes/manifests
**Answer:** C – CSV rows of 'token,user,uid,"group1,group2"' served by the apiserver flag <code>--token-auth-file</code>
**Explanation:** The static token file is a CSV on the control-plane node passed via '--token-auth-file=/path/file.csv'; each row is token,user,uid,"groups". Callers present the token as 'Authorization: Bearer &lt;token&gt;'. It's simple but static — changing users means editing the file and restarting kube-apiserver, and tokens are plaintext on disk, so it's discouraged for production.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Docs - Authentication</a>
**Tags:** k8s::kcna src::session topic::api topic::authentication topic::security

---

<!-- note:1793913170422 model:Many -->
**Domain:** Authentication
**Question:** What happens to an API request that presents NO credentials at all?
**Options:** A. They are rejected with 403 Forbidden<br>B. They map to system:anonymous in group system:unauthenticated (if anonymous auth is on)<br>C. They get read-only guest permissions<br>D. They retry after a backoff
**Answer:** B – unauthenticated calls map to system:anonymous / system:unauthenticated (401 if disabled)
**Explanation:** Requests that pass no credentials don't automatically get rejected: if anonymous auth is enabled they become 'system:anonymous' in group 'system:unauthenticated' and RBAC decides if that identity may act (usually it can't). Disable with '--anonymous-auth=false' on kube-apiserver. Every request is thus either an authenticated identity (users get 'system:authenticated' added) or the anonymous identity.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Docs - Authentication</a>
**Tags:** k8s::kcna src::session topic::api topic::authentication topic::security

---

<!-- note:1793913170423 model:Many -->
**Domain:** Authentication
**Question:** How can external identity systems like LDAP or Kerberos authenticate Kubernetes users? (Select all that apply)
**Options:** A. LDAP via a built-in <code>--ldap-server</code> flag<br>B. An authenticating proxy that forwards identity headers<br>C. An authentication webhook (TokenReview API)<br>D. Kerberos tickets passed directly to the apiserver
**Answer:** B, C – authenticating proxy or authentication webhook; native OIDC is the built-in IdP path
**Explanation:** There is no native LDAP/Kerberos/SAML plugin: Kubernetes natively supports client certs, bearer tokens (incl. ServiceAccount JWTs), and OIDC. To reach LDAP/Kerberos/etc. you front the API with an authenticating proxy that maps headers to user identity, or use an authentication webhook — the apiserver calls your token-review service which returns the user info. OIDC (e.g. Dex/Keycloak/Entra) is the one external-identity mechanism the API server supports natively.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Docs - Authentication</a>
**Tags:** k8s::kcna src::session topic::api topic::authentication topic::security

---

<!-- note:1793913170424 model:Many -->
**Domain:** Authentication
**Question:** After '<code>kubectl create serviceaccount jenkins</code>', what username does the API server assign that identity?
**Options:** A. system:serviceaccount:&lt;namespace&gt;:jenkins<br>B. jenkins@&lt;namespace&gt;.svc<br>C. system:user:jenkins<br>D. user:jenkins:service
**Answer:** A – <code>kubectl create serviceaccount jenkins</code> produces identity 'system:serviceaccount:&lt;namespace&gt;:jenkins'
**Explanation:** ServiceAccounts ARE API objects — namespaced and creatable via kubectl or YAML (unlike normal users). Pods mount the SA's token, and in-cluster processes authenticate as 'system:serviceaccount:&lt;ns&gt;:&lt;name&gt;' in groups 'system:serviceaccounts' and 'system:serviceaccounts:&lt;ns&gt;'; the signed JWT also works for clients outside the cluster. Because SA tokens can be stored in Secrets, be careful who can read them.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Docs - Authentication</a>
**Tags:** k8s::kcna src::session topic::authentication topic::security topic::serviceaccounts

---

<!-- note:1793913173620 model:Basic (and reversed card) -->
**Front:** Users vs ServiceAccounts in Kubernetes — which ones can you '<code>kubectl create</code>'?
**Back:** Only ServiceAccounts — they ARE API objects (namespaced, kubectl-creatable). Normal users are NOT Kubernetes objects at all: 'Kubernetes does not have objects which represent normal user accounts.' Humans/automation get identity from an external source — a client cert signed by the cluster CA, an OIDC/IdP login, a static token file — and the apiserver just validates it. Rule of thumb: humans = external user identity; in-cluster processes = ServiceAccount.
**Tags:** k8s::kcna src::session topic::authentication topic::security topic::serviceaccounts

---

<!-- note:1793913972240 model:Many -->
**Domain:** TLS Certificates
**Question:** What is a Certificate Authority (CA) and what does it do?
**Options:** A. A service that stores certificates for retrieval<br>B. The trusted issuer that signs certificates; everything trusts certs signed by it<br>C. A load balancer that terminates TLS<br>D. An etcd key that encrypts secrets
**Answer:** B – the trusted issuer that signs certificates; everything trusts certs it signs
**Explanation:** A CA is the root of trust: it holds a key pair (ca.key private + ca.crt public cert). It validates CSRs and signs them with ca.key — the signature is what makes a certificate trustworthy. Every client/server carries a copy of ca.crt and accepts any cert signed by that CA. In a cluster the CA is how all components verify each other's identity; keep ca.key private on the signing host — whoever has it can mint identities.
**Sources:** <a href="https://kubernetes.io/docs/setup/best-practices/certificates/" target="_blank">Kubernetes Docs - PKI certificates and requirements</a>
**Tags:** k8s::kcna src::session topic::certificates topic::security topic::tls

---

<!-- note:1793913972241 model:Many -->
**Domain:** TLS Certificates
**Question:** To mint a cluster-admin user cert for kubectl access, what must the certificate subject contain?
**Options:** A. CN=system:masters<br>B. O=system:masters — the O field carries the group<br>C. OU=admin plus CN=system:masters<br>D. A special flag in the CSR's extensions
**Answer:** B – the O (Organization) field carries group membership; O=system:masters grants cluster-admin
**Explanation:** Groups come from the cert's O field — 'openssl req -subj "/CN=kube-admin/O=system:masters"' makes an identity that authenticates as user 'kube-admin' in group 'system:masters'. system:masters is bound to the cluster-admin ClusterRole out of the box, which is what actually grants full control — the cert just proves membership.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Docs - Authentication</a>
**Tags:** k8s::kcna src::session topic::certificates topic::rbac topic::security topic::tls

---

<!-- note:1793913972242 model:Many -->
**Domain:** TLS Certificates
**Question:** Which identity mappings do Kubernetes component certificates require? (Select all that apply)
**Options:** A. kube-proxy cert must carry <code>CN=system:kube-proxy</code><br>B. Each kubelet cert must carry <code>CN=system:node:&lt;nodename&gt;</code> with <code>O=system:nodes</code><br>C. Admin users need <code>O=system:masters</code> in their cert<br>D. Any CN works — RBAC ignores certificate subjects
**Answer:** A, B, C – <code>system:kube-proxy</code> for kube-proxy, <code>system:node:&lt;nodename&gt;</code>+<code>O=system:nodes</code> for each kubelet, <code>O=system:masters</code> for admin users
**Explanation:** Component identities are fixed names the control plane expects: kube-proxy authenticates as <code>system:kube-proxy</code> (CN), each kubelet as <code>system:node:&lt;nodeName&gt;</code> (CN) plus group <code>system:nodes</code> (O) — Node authorizer relies on that mapping; an admin user is 'kube-admin' (or any CN) in group <code>system:masters</code>. Certificates without the right CN/O authenticate as someone else entirely and get rejected by authorization.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Docs - Authentication</a>
**Tags:** k8s::kcna src::session topic::certificates topic::control-plane topic::security topic::tls

---

<!-- note:1793913972243 model:Many -->
**Domain:** TLS Certificates
**Question:** Why does the kube-apiserver certificate need an openssl.cnf with an [alt_names] section?
**Options:** A. openssl.cnf encrypts the private key<br>B. alt_names lists every DNS name and IP clients use to reach the apiserver — required or hostname verification fails<br>C. It's only needed to set the certificate expiry date<br>D. SANs are for encrypting etcd at rest
**Answer:** B – SANs let one cert be valid for every name/IP clients dial the apiserver by (kubernetes, .svc FQDNs, internal + external IPs)
**Explanation:** The apiserver is reachable under several names: the 'kubernetes' Service name (kubernetes, kubernetes.default, kubernetes.default.svc, kubernetes.default.svc.cluster.local), plus node/public IPs. TLS hostname verification fails if the dialed name isn't in the cert — so the openssl.cnf used to generate the apiserver cert carries an [alt_names] section listing every DNS name and IP (internal + external) that will reach it.
**Sources:** <a href="https://kubernetes.io/docs/setup/best-practices/certificates/" target="_blank">Kubernetes Docs - PKI certificates and requirements</a>
**Tags:** k8s::kcna src::session topic::api topic::certificates topic::security topic::tls

---

<!-- note:1793913972244 model:Many -->
**Domain:** TLS Certificates
**Question:** How is TLS handled between etcd cluster members?
**Options:** A. etcd doesn't support TLS — it relies on NetworkPolicies<br>B. Peer certs authenticate etcd members to each other; client certs authenticate the apiserver — both set via etcd config flags<br>C. etcd certs are stored as Kubernetes Secrets and mounted at runtime<br>D. Peer certs are only for etcd backups
**Answer:** B – etcd members authenticate each other with peer certificates; apiserver↔etcd uses client certs, all configured via etcd flags
**Explanation:** etcd runs its own PKI within the cluster's: member-to-member (peer) traffic uses <code>--peer-cert-file</code>/<code>--peer-key-file</code>/<code>--peer-trusted-ca-file</code>, and clients (kube-apiserver) use <code>--cert-file</code>/<code>--key-file</code>/<code>--trusted-ca-file</code>. These paths are set in the etcd static pod manifest (/etc/kubernetes/manifests/etcd.yaml on kubeadm) — usually under /etc/kubernetes/pki/etcd/.
**Sources:** <a href="https://kubernetes.io/docs/setup/best-practices/certificates/" target="_blank">Kubernetes Docs - PKI certificates and requirements</a>
**Tags:** k8s::kcna src::session topic::certificates topic::etcd topic::security topic::tls

---

<!-- note:1793913972245 model:Many -->
**Domain:** TLS Certificates
**Question:** Who needs the CA certificate, and who needs the CA private key?
**Options:** A. Distribute ca.crt to every component for verification; keep ca.key private on the signing host<br>B. Distribute ca.key so components can verify certs<br>C. Copy both key and cert everywhere — they're a pair<br>D. Neither — verification uses the etcd root
**Answer:** A – everyone gets a COPY of the CA certificate to verify peers; ca.key never leaves the signing host
**Explanation:** Verification is asymmetric: to trust a peer's certificate you only need the CA's public cert — so ca.crt is distributed to every node, component config, and kubeconfig (certificate-authority field). The ca.key is what mints identities, so it stays private on the control-plane/signing host: whoever holds it can forge any identity in the cluster.
**Sources:** <a href="https://kubernetes.io/docs/setup/best-practices/certificates/" target="_blank">Kubernetes Docs - PKI certificates and requirements</a>
**Tags:** k8s::kcna src::session topic::certificates topic::security topic::tls

---

<!-- note:1793914089195 model:Many -->
**Domain:** TLS Certificates - Kubelet
**Question:** How does each kubelet authenticate to the kube-apiserver?
**Options:** A. One shared cluster cert copied to every node<br>B. A per-node client cert: <code>CN=system:node:&lt;nodeName&gt;</code>, <code>O=system:nodes</code><br>C. A ServiceAccount token mounted at /var/lib/kubelet<br>D. The node's SSH host key
**Answer:** B – a per-node client cert with <code>CN=system:node:&lt;nodeName&gt;</code> and <code>O=system:nodes</code>, unique to that machine
**Explanation:** Every kubelet talks to the apiserver as its OWN node identity: the client cert's CN must be <code>system:node:&lt;nodeName&gt;</code> and <code>O=system:nodes</code> — one cert per node, minted with that node's name. kubeadm keeps it under <code>/var/lib/kubelet/pki/</code> and references it in <code>kubelet.conf</code>; with TLS bootstrap the kubelet even requests the cert itself via the certificates.k8s.io CSR API using a bootstrap token.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Docs - Authentication</a>
**Tags:** k8s::kcna src::session topic::control-plane topic::security topic::tls

---

<!-- note:1793914089196 model:Many -->
**Domain:** Node Authorization
**Question:** What ties a kubelet's access to only its own node's objects?
**Options:** A. RBAC RoleBindings per node<br>B. The Node authorizer matches the cert's <code>system:node:&lt;name&gt;</code> to scope kubelet to its own node's objects<br>C. NetworkPolicy blocks cross-node API calls<br>D. kube-proxy filters kubelet traffic
**Answer:** B – Node authorization uses the cert's <code>system:node:&lt;name&gt;</code> to restrict each kubelet to objects belonging to its own node
**Explanation:** The Node authorizer + NodeRestriction admission gate kubelet requests against the node name baked into its cert: 'system:node:worker-2' may only read pods scheduled to worker-2 and update its own node/secrets — it cannot list other nodes' pods or secrets. The name match is why node certs are per-node: a stolen kubelet cert only grants that one node's reach.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/node/" target="_blank">Kubernetes Docs - Node Authorization</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security

---

<!-- note:1793914866144 model:Many -->
**Domain:** Health Probes
**Question:** The purpose of the Readiness probe is to:
**Options:** A. Encrypt traffic<br>B. Decide if Pod receives Service traffic<br>C. Restart container<br>D. Reserve CPU
**Answer:** B – decide if Pod receives Service traffic
**Explanation:** Readiness gates traffic; liveness restarts. A failing readiness probe removes the Pod from Service endpoints so no traffic is routed to it — the container keeps running and is NOT restarted (that's the liveness probe's job). Encryption is TLS/mesh; CPU reservation is resource requests — neither involves probes.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/" target="_blank">Kubernetes Docs - Liveness, Readiness, and Startup Probes</a>
**Tags:** k8s::kcna src::session topic::probes topic::services

---

<!-- note:1793915613866 model:Many -->
**Domain:** NetworkPolicy - isolation
**Question:** If a Pod is selected by at least one NetworkPolicy for ingress, what's the default behavior for ingress traffic?
**Options:** A. Ignore all NetworkPolicies<br>B. Only allow NodePort<br>C. Allow all<br>D. Deny all ingress except what policies allow
**Answer:** D – deny all ingress except what policies allow
**Explanation:** Selection triggers default-deny for that direction, then allow rules apply. Pods selected by NO NetworkPolicy are fully open (allow-all); the moment ≥1 policy's podSelector matches, that direction flips to isolated and ONLY traffic matching the policy's ingress rules passes — everything else is dropped. Three nuances: isolation is per-direction (ingress selection leaves egress open unless a policy also lists egress); policies are additive — multiple selecting policies OR their rules together (union, not strictest-wins); and enforcement depends on the CNI plugin supporting NetworkPolicy — unsupported CNIs silently ignore policies, leaving the pod open.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Docs - Network Policies</a>
**Tags:** k8s::kcna src::session topic::networking topic::networkpolicy topic::security

---

<!-- note:1793915613867 model:Many -->
**Domain:** Scheduling - nodeSelector syntax
**Question:** The correct nodeSelector format is:
**Options:** A. <code>nodeSelector: { disk: ssd }</code><br>B. <code>nodeSelector: ["disk=ssd"]</code><br>C. <code>nodeSelector: (disk=ssd)</code><br>D. <code>nodeSelector: "disk=ssd"</code>
**Answer:** A – nodeSelector: { disk: ssd }
**Explanation:** nodeSelector is a key/value map, not a query string: under spec.nodeSelector you write YAML labels as key: value pairs — <code>nodeSelector: { disk: ssd }</code> (or block form with each pair on its own line) pins the pod to nodes carrying disk=ssd, with ALL pairs required (AND). The 'disk=ssd' expression style is kubectl's -l/<code>--selector</code> flag syntax (e.g. <code>kubectl get pods -l disk=ssd</code>), NOT pod-spec field syntax — a common mix-up. nodeSelector only does equality; for operators like In/NotIn use nodeAffinity matchExpressions.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Docs - Assign Pods to Nodes</a>
**Tags:** k8s::kcna src::session topic::nodeselector topic::scheduling topic::yaml

---

<!-- note:1793920105315 model:Many -->
**Domain:** Health Probes - ordering
**Question:** Probe relationship: which starts first?
**Options:** A. liveness always first<br>B. readiness always first<br>C. startup→readiness→liveness strict loop<br>D. startup first; while failing, readiness/liveness is suppressed; after success, readiness/liveness is independent
**Answer:** D (4) – startup first; while failing, readiness/liveness is suppressed; after success, readiness/liveness is independent
**Explanation:** The startup probe exists for slow-booting apps: while it keeps failing, BOTH liveness and readiness are disabled — so a container that takes 5 minutes to start isn't killed by liveness or kept out of rotation complaints. Once startup succeeds it never runs again, and liveness + readiness take over independently: readiness can fail (pull from Service endpoints) while liveness stays green, and vice versa. There's no strict startup→readiness→liveness pipeline — readiness and liveness are peers, not stages.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/" target="_blank">Kubernetes Docs - Liveness, Readiness, and Startup Probes</a>
**Tags:** k8s::kcna src::session topic::pods topic::probes

---

<!-- note:1793920650504 model:Many -->
**Domain:** Service Communication
**Question:** Why use certificates between services?
**Options:** A. Encrypt + authenticate (TLS/mTLS)<br>B. Increase CPU<br>C. Replace DNS<br>D. Stop restarts
**Answer:** A (1) – encrypt + authenticate (TLS/mTLS)
**Explanation:** Certificates between services buy TWO things at once: encryption in transit (pod-to-pod traffic crosses node networks where cleartext HTTP would expose credentials and data) AND identity verification — with mTLS BOTH sides present certs, so each service proves who it is, not just that the channel is private. That's the security layer service meshes like Istio/Linkerd automate at scale. The distractors are nonsense or other systems' jobs: certificates don't speed anything up (mTLS costs CPU for handshake/crypto), DNS is CoreDNS, and restart behavior belongs to liveness probes and controllers.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/" target="_blank">Kubernetes Docs - Security</a>
**Tags:** k8s::kcna src::session topic::mtls topic::security topic::tls

---

<!-- note:1793921208832 model:Many -->
**Domain:** Ingress - API versions
**Question:** Which is a valid Ingress apiVersion/kind in modern Kubernetes?
**Options:** A. extensions/v1beta1 / Ingress<br>B. v1 / Ingress<br>C. networking.k8s.io/v2 / Ingress<br>D. networking.k8s.io/v1 / Ingress
**Answer:** D (4) – networking.k8s.io/v1 / Ingress
**Explanation:** networking.k8s.io/v1 has been the stable Ingress API since Kubernetes 1.19 — extensions/v1beta1 and networking.k8s.io/v1beta1 were removed in 1.22. The v1beta1→v1 jump had real breaking changes: pathType became required on every path, backend.service.port.name was dropped (number only), and ingressClassName became a spec field. The 'something different' to know: the Ingress API is FROZEN — generally available but no longer developed, no new features. Kubernetes officially recommends the Gateway API (gateway.networking.k8s.io/v1, GA since Oct 2023, v1.4 Oct 2025) as its successor — same job (HTTP routing to Services), richer model: Gateway + GatewayClass + HTTPRoute objects instead of one Ingress.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/ingress/" target="_blank">Kubernetes Docs - Ingress</a><br><a href="https://gateway-api.sigs.k8s.io/guides/getting-started/migrating-from-ingress/" target="_blank">Gateway API - Migrating from Ingress</a>
**Tags:** k8s::kcna src::session topic::ingress topic::networking

---

<!-- note:1793921403923 model:Many -->
**Domain:** RBAC - additive model
**Question:** Kubernetes RBAC "deny" behavior:
**Options:** A. ClusterRole overrides to remove<br>B. RBAC is additive; reduce by removing/changing bindings/roles<br>C. Roles can explicitly deny<br>D. Empty Role cancels other grants
**Answer:** B (2) – RBAC is additive; reduce access by removing or narrowing bindings/roles
**Explanation:** RBAC has NO deny mechanism: there is no 'deny' verb, a Role cannot express 'allow everything except X', and an empty Role grants nothing rather than cancelling other grants. Permissions only accumulate — effective access is the UNION of every Role/ClusterRole bound to you (and across authz modes, an allow from ANY enabled mode wins). Wildcards (*) in rules only expand grants, never subtract. The only ways to reduce someone's access are removing the RoleBinding/ClusterRoleBinding, or editing the Role's rules to narrow verbs/resources. This differs from firewalls/SELinux where explicit deny rules exist — RBAC can't do default-deny-with-exceptions.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security

---

<!-- note:1793921403924 model:Many -->
**Domain:** ServiceAccounts - token mount
**Question:** Which setting prevents a Pod from auto-mounting a ServiceAccount token?
**Options:** A. runAsNonRoot: true<br>B. automountServiceAccountToken: false<br>C. readOnlyRootFilesystem: true<br>D. serviceAccountName: ""
**Answer:** B (2) – automountServiceAccountToken: false
**Explanation:** Every pod gets a ServiceAccount token auto-mounted at /var/run/secrets/kubernetes.io/serviceaccount/ — a projected volume holding the SA's JWT plus the cluster CA cert — because the default is automountServiceAccountToken: true. Setting it false (on the pod spec or on the ServiceAccount itself) skips the mount entirely. It exists for least privilege: any process in the pod can read that token and authenticate to the API server AS that ServiceAccount, so mounting it everywhere means every container carries a live credential it may never need — a stolen token = stolen API access. Pods that don't call the K8s API shouldn't get one; pair it with an RBAC-scoped SA so even mounted tokens can only do what's needed. Distractors: runAsNonRoot and readOnlyRootFilesystem are pod securityContext hardening (UID/filesystem), and serviceAccountName only selects WHICH account — an empty value still mounts the default SA's token.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/" target="_blank">Kubernetes Docs - Configure Service Accounts for Pods</a>
**Tags:** k8s::kcna src::session topic::pods topic::security topic::serviceaccounts

---

<!-- note:1793921727121 model:Many -->
**Domain:** Pod Security Standards
**Question:** Pod Security Standards levels, ordered least → most restrictive:
**Options:** A. Restricted → Baseline → Privileged<br>B. Privileged → Baseline → Restricted<br>C. Baseline → Restricted → Privileged<br>D. Baseline → Privileged → Restricted
**Answer:** B (2) – Privileged → Baseline → Restricted
**Explanation:** Least → most restrictive: Privileged → Baseline → Restricted. The levels are cumulative — Restricted includes ALL Baseline rules plus hardened requirements (runAsNonRoot, drop ALL capabilities, seccomp profile, no privilege escalation). Privileged is unrestricted (the effective default for unlabeled namespaces). Baseline blocks only the obviously dangerous: privileged containers, host namespaces/PID/IPC, hostPath volumes, host ports, dangerous capabilities. Restricted enforces current pod-hardening best practices. Enforcement is via namespace labels like pod-security.kubernetes.io/enforce=restricted, with audit and warn modes for rollout — Pod Security Admission replaced the deprecated PodSecurityPolicy.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/pod-security-standards/" target="_blank">Kubernetes Docs - Pod Security Standards</a>
**Tags:** k8s::kcna src::session topic::pods topic::podsecurity topic::security

---

<!-- note:1793931248497 model:Many -->
**Domain:** Kubeconfig - purpose
**Question:** Why use a kubeconfig file instead of passing --server, --client-key, --client-certificate, --certificate-authority to every kubectl command?
**Options:** A. kubectl can't accept those flags at all<br>B. the kubeconfig stores cluster address + auth material once; kubectl reads it automatically<br>C. the kubeconfig encrypts credentials better than flags<br>D. those flags only work with kubectl exec
**Answer:** B – the kubeconfig stores cluster address + auth material once; kubectl reads it automatically
**Explanation:** The flags DO exist and work per-command — kubectl accepts --server, --client-key, --client-certificate, --certificate-authority, --token etc. on every invocation — but repeating the server URL and credential paths on every call is impractical. The kubeconfig file (default ~/./.kube/config) stores named clusters, users, and contexts once, and kubectl loads it automatically. When both are present, command-line flags still win over file values (flag > kubeconfig precedence). The KUBECONFIG env var points kubectl at a different file or a list of files to merge.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/" target="_blank">Kubernetes Docs - Organizing Cluster Access Using kubeconfig Files</a>
**Tags:** k8s::kcna src::session topic::kubeconfig topic::kubectl

---

<!-- note:1793931248498 model:Many -->
**Domain:** Kubeconfig - context
**Question:** In a kubeconfig file, which element groups a cluster, user, and namespace under one switchable name?
**Options:** A. cluster<br>B. user<br>C. context<br>D. preferences
**Answer:** C – context
**Explanation:** A context is the convenience binding: it groups three parameters under one switchable name — cluster (WHERE: server URL + CA trust material like certificate-authority or certificate-authority-data, or insecure-skip-tls-verify), user (WHO: client-certificate+client-key, token, username/password, or exec credential plugins), and namespace (default namespace for that pairing). The current-context field selects which context kubectl uses; kubectl config use-context switches it. This is why one kubeconfig can hold many clusters/users — you switch contexts instead of editing flags.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/" target="_blank">Kubernetes Docs - Organizing Cluster Access Using kubeconfig Files</a>
**Tags:** k8s::kcna src::session topic::kubeconfig topic::kubectl

---

<!-- note:1793931248499 model:Many -->
**Domain:** Kubeconfig - kubectl config commands
**Question:** Which command switches kubectl to a different context?
**Options:** A. kubectl config get-contexts<br>B. kubectl config use-context <name><br>C. kubectl config current-context<br>D. kubectl config set-context <name>
**Answer:** B – kubectl config use-context <name>
**Explanation:** kubectl config use-context <name> sets current-context — the * in get-contexts output moves to that context. The family: get-contexts lists all contexts (* = current), current-context prints just the active name, set-context creates or edits a context's cluster/user/namespace fields, and kubectl config unset contexts.<name> deletes one. To change only the namespace of the current context: kubectl config set-context --current --namespace=<ns>. View the whole merged file with kubectl config view.
**Sources:** <a href="https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/" target="_blank">Kubernetes Docs - Configure Access to Multiple Clusters</a>
**Tags:** k8s::kcna src::session topic::kubeconfig topic::kubectl

---

<!-- note:1793931248500 model:Many -->
**Domain:** Kubeconfig - defaults
**Question:** Where does kubectl get the default namespace for namespaced resources?
**Options:** A. always "default" — hardcoded<br>B. the namespace field of the current context (falls back to "default" if unset)<br>C. the cluster's namespace setting<br>D. the KUBECONFIG environment variable
**Answer:** B – the namespace field of the current context (falls back to "default" if unset)
**Explanation:** Namespace is a property of the CONTEXT, not the cluster or the user — each context can pin a different namespace, so switching contexts can silently change your default namespace. If the context has no namespace field, kubectl uses "default". A per-command --namespace flag always overrides the context's value for that invocation. The same pattern applies to identity: the user kubectl authenticates as comes from the context's user field unless --user is passed.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/" target="_blank">Kubernetes Docs - Organizing Cluster Access Using kubeconfig Files</a>
**Tags:** k8s::kcna src::session topic::kubeconfig topic::kubectl topic::namespaces

---

<!-- note:1793931248507 model:Cloze -->
**Text:** By default kubectl reads its kubeconfig from {{c1::$HOME/.kube/config}}. The {{c2::KUBECONFIG}} environment variable holds a {{c3::list}} of files that kubectl {{c4::merges}} (first file to set a value wins per key), while the {{c5::--kubeconfig}} flag points at exactly {{c6::one}} file with {{c7::no}} merging.
**Back Extra:** Precedence: --kubeconfig flag > KUBECONFIG env var > default file. When KUBECONFIG lists multiple files, kubectl merges them — the first file to set a value or map key wins and later duplicates are discarded. Relative file paths inside a kubeconfig resolve relative to that kubeconfig's location.
**Tags:** k8s::kcna src::session topic::kubeconfig topic::kubectl

---

<!-- note:1793931250748 model:Basic -->
**Front:** What are the top-level sections of a kubeconfig file (kind: Config)?
**Back:** apiVersion: v1 / kind: Config, then three named lists plus current-context. clusters: WHERE — each has name + server URL + trust material (certificate-authority file, certificate-authority-data base64, or insecure-skip-tls-verify: true, optional proxy-url). users: WHO — name + auth material (client-certificate + client-key, token, username + password, auth-provider, or exec credential plugins). contexts: the binding — name + cluster + user + optional namespace. current-context: which context kubectl uses by default. preferences: {} is normally empty. kubectl config view prints the effective (possibly merged) file.
**Tags:** k8s::kcna src::session topic::kubeconfig topic::kubectl topic::yaml

---

<!-- note:1793931644489 model:Many -->
**Domain:** API Groups - core vs named
**Question:** How do the core API group and named API groups differ?
**Options:** A. Core serves at REST path /api/v1 with apiVersion: v1; named groups at /apis/$GROUP/$VERSION with apiVersion: $GROUP/$VERSION<br>B. The core group is deprecated — all resources moved to named groups<br>C. Named groups use /api/v1 too but with kind prefixes<br>D. The core group has no REST path — it exists only at compile time
**Answer:** A – core serves at /api/v1 with apiVersion: v1; named groups at /apis/$GROUP/$VERSION with apiVersion: $GROUP/$VERSION
**Explanation:** Every object declares group+version in its apiVersion field, which mirrors the REST path. The core (legacy) group is /api/v1 and is written as just apiVersion: v1 — no group name, because it's the original unnamed group holding pods, services, namespaces, nodes, secrets… Named groups live at /apis/<group>/<version> and write apiVersion: <group>/<version> — apps/v1 → /apis/apps/v1, networking.k8s.io/v1 → /apis/networking.k8s.io/v1, batch/v1 → /apis/batch/v1. Named groups exist so the API can grow: new features land in named groups without destabilizing the stable core API.
**Sources:** <a href="https://kubernetes.io/docs/reference/using-api/" target="_blank">Kubernetes Docs - API Overview</a>
**Tags:** k8s::kcna src::session topic::api topic::yaml

---

<!-- note:1793931644490 model:Many -->
**Domain:** API Groups - core resources
**Question:** Which resources are served by the core v1 API group? (Select all that apply)
**Options:** A. Pods<br>B. Namespaces<br>C. Nodes<br>D. Events<br>E. Endpoints<br>F. Secrets<br>G. Deployments<br>H. NetworkPolicies<br>I. CronJobs<br>J. ClusterRoles
**Answer:** A, B, C, D, E, F – Pods, Namespaces, Nodes, Events, Endpoints, Secrets
**Explanation:** The core v1 group holds the ORIGINAL API: pods, services, namespaces, nodes, configmaps, secrets, serviceaccounts, endpoints, events, persistentvolumes/claims, resourcequotas, limitranges, replicationcontrollers, podtemplates. Everything newer lives in named groups — Deployments/StatefulSets/DaemonSets/ReplicaSets → apps/v1; Jobs/CronJobs → batch/v1; Ingresses/NetworkPolicies → networking.k8s.io/v1; Roles/ClusterRoles → rbac.authorization.k8s.io/v1; StorageClasses → storage.k8s.io/v1; CRDs → apiextensions.k8s.io/v1. Rule of thumb: apiVersion: v1 (bare) = core group.
**Sources:** <a href="https://kubernetes.io/docs/reference/using-api/" target="_blank">Kubernetes Docs - API Overview</a>
**Tags:** k8s::kcna src::session topic::api topic::resources

---

<!-- note:1793931644491 model:Many -->
**Domain:** API Groups - named groups
**Question:** Which apiVersion serves Deployment objects in modern Kubernetes?
**Options:** A. v1<br>B. extensions/v1beta1<br>C. apps/v1<br>D. batch/v1
**Answer:** C (3) – apps/v1
**Explanation:** apps/v1 serves Deployments, ReplicaSets, DaemonSets, StatefulSets and ControllerRevisions. extensions/v1beta1 was their ORIGINAL home but was emptied and removed — Ingresses moved to networking.k8s.io/v1, workloads to apps/v1. batch/v1 = Jobs + CronJobs. This is exactly why named groups exist: related resources version and evolve together, and new features land in named groups instead of churning the stable core API.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/deployment-v1/" target="_blank">Kubernetes API Reference - Deployment v1</a>
**Tags:** k8s::kcna src::session topic::api topic::workloads

---

<!-- note:1793931644492 model:Many -->
**Domain:** API Groups - verbs
**Question:** Which of these are valid Kubernetes API verbs? (Select all that apply)
**Options:** A. get<br>B. list<br>C. watch<br>D. create<br>E. update<br>F. patch<br>G. delete<br>H. deletecollection<br>I. read<br>J. write<br>K. query<br>L. fetch
**Answer:** A, B, C, D, E, F, G, H – get, list, watch, create, update, patch, delete, deletecollection
**Explanation:** Verbs are the actions the API server exposes on resources: get, list, watch (reads) and create, update, patch, delete, deletecollection (writes) — these are exactly what RBAC rules grant per resource. They map to HTTP methods: GET → get/list/watch, POST → create, PUT → update, PATCH → patch, DELETE → delete. Extra RBAC verbs exist for special cases: proxy, impersonate, bind, escalate. 'read', 'write', 'query', 'fetch' are NOT API verbs — generic programming words, not part of the API surface.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna src::session topic::api topic::rbac

---

<!-- note:1793931644493 model:Many -->
**Domain:** API Groups - kubectl proxy
**Question:** What does kubectl proxy do?
**Options:** A. Forwards a local port into a pod (like port-forward)<br>B. Starts a localhost proxy to the API server using your kubeconfig credentials, so you can query the REST API directly<br>C. Proxies traffic between cluster Services<br>D. Opens an encrypted tunnel to etcd
**Answer:** B – starts a localhost proxy to the API server using your kubeconfig credentials so you can hit the REST API directly
**Explanation:** kubectl proxy runs a local proxy (default 127.0.0.1:8001; change with --port, --address, --accept-hosts) that forwards to the API server with your kubeconfig's TLS + auth already handled — so curl http://localhost:8001/api/v1/namespaces or /apis/apps/v1/deployments.default works with zero cert juggling. It's a debugging/exploration tool for the raw REST API. It is NOT pod port-forwarding (kubectl port-forward), NOT service-to-service traffic, and NOT etcd access.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/generated/kubectl_proxy/" target="_blank">Kubernetes Docs - kubectl proxy</a>
**Tags:** k8s::kcna src::session topic::api topic::kubectl

---

<!-- note:1793931644494 model:Many -->
**Domain:** API Groups - discovery
**Question:** Which kubectl command lists the API resources available on the cluster together with their API groups?
**Options:** A. kubectl api-versions<br>B. kubectl api-resources<br>C. kubectl get --raw /version<br>D. kubectl config view
**Answer:** B (2) – kubectl api-resources
**Explanation:** kubectl api-resources lists every resource on the cluster (deployments, pods, networkpolicies…) together with its API group/version, kind, and short names. kubectl api-versions lists only the group/version strings. For raw discovery endpoints, kubectl get --raw /apis or /api/v1 queries the same discovery API the server exposes. kubectl config view shows your kubeconfig — unrelated to cluster API discovery.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/generated/kubectl_api-resources/" target="_blank">Kubernetes Docs - kubectl api-resources</a>
**Tags:** k8s::kcna src::session topic::api topic::kubectl

---

<!-- note:1793931644496 model:Cloze -->
**Text:** REST paths — core group: {{c1::/api/v1}} (apiVersion: {{c2::v1}}, no group name); named groups: {{c3::/apis/$GROUP_NAME/$VERSION}} (e.g. apiVersion: {{c4::apps/v1}} → /apis/apps/v1).
**Back Extra:** The apiVersion field mirrors the REST path: bare 'v1' = core group; 'group/version' = named group. So apiVersion: apps/v1 means REST path /apis/apps/v1. kubectl api-resources prints this mapping for every resource your cluster serves.
**Tags:** k8s::kcna src::session topic::api topic::yaml

---

<!-- note:1793931644545 model:Basic (and reversed card) -->
**Front:** What is a Kubernetes API group?
**Back:** A logical grouping of related API resources served together at a REST path. The core (legacy) group lives at /api/v1 and holds the original resources (pods, services, namespaces, nodes, secrets…); named groups live at /apis/<group>/<version> (apps, batch, networking.k8s.io, rbac.authorization.k8s.io, storage.k8s.io, apiextensions.k8s.io…) and host newer features. The group is declared in each object's apiVersion field, and groups make the API extensible — new resource families arrive as new groups without changing core.
**Tags:** k8s::kcna src::session topic::api topic::architecture

---

<!-- note:1793932055033 model:Many -->
**Domain:** kubectl - api-resources flags
**Question:** Which command would you use to see a full list of non-namespaced resources in Kubernetes?
**Options:** A. kubectl api-resources --namespaced=false<br>B. kubectl api-resources --all<br>C. kubectl api-resources<br>D. kubectl api-resources --namespaced=true
**Answer:** A (1) – kubectl api-resources --namespaced=false
**Explanation:** api-resources --namespaced=false filters the output to CLUSTER-scoped resources only — nodes, namespaces, persistentvolumes, clusterroles, storageclasses, priorityclasses… (things not bound to a namespace). --namespaced=true does the opposite (namespaced only). With no flag, api-resources shows everything and a NAMESPACED column tells you which is which. There is no --all flag on api-resources — that's kubectl get territory (-A/--all-namespaces). Other useful filters: --api-group=<group> and --verbs=<verb>.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/generated/kubectl_api-resources/" target="_blank">Kubernetes Docs - kubectl api-resources</a>
**Tags:** k8s::kcna src::session topic::api topic::kubectl

---

<!-- note:1793932206940 model:Many -->
**Domain:** Node Authorization - permitted identities
**Question:** Who is authorized by the node authorizers to make requests to kube-apiserver?
**Options:** A. Only the kubelet running on the master node<br>B. Any user with system administrator privileges<br>C. Any user that is part of the Kubernetes cluster<br>D. Any request from a user named system:node:<name> in the system:nodes group
**Answer:** D (4) – requests from a user named system:node:<name> in the system:nodes group
**Explanation:** The Node authorizer is a special mode built for kubelets: it only authorizes requests authenticated as system:node:<nodeName> belonging to group system:nodes — the identity kubelets get from their client certs (CN=system:node:<name>, O=system:nodes). It then scopes WHAT they may touch: pods bound to their node, node objects/status, mirrored EndpointSlices, leases, and CSRs for their node's certs — tightened further by NodeRestriction. It's identity-based, not role-based: cluster membership or OS admin rights mean nothing here; regular users are denied even though they're 'part of the cluster'. Runs alongside RBAC (--authorization-mode=Node,RBAC) — Node handles kubelet traffic, RBAC handles everything else.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/node/" target="_blank">Kubernetes Docs - Node authorizer</a>
**Tags:** k8s::kcna src::session topic::kubelet topic::rbac topic::security

---

<!-- note:1793932282196 model:Many -->
**Domain:** NetworkPolicy - pod selection
**Question:** Where do we specify the pod labels in a Kubernetes network policy definition file?
**Options:** A. spec.podSelector<br>B. spec.egress<br>C. spec.ingress<br>D. spec.matchLabels
**Answer:** A (1) – spec.podSelector
**Explanation:** spec.podSelector selects WHICH pods the policy applies to — the labels themselves go under spec.podSelector.matchLabels (or matchExpressions for operators). An empty podSelector: {} selects ALL pods in the policy's namespace. spec.ingress and spec.egress are the traffic RULE lists (from/to peers + ports), not selectors — spec.matchLabels isn't a NetworkPolicy field at all (that's the style used inside podSelector and in workload selectors like a Deployment's spec.selector.matchLabels).
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Docs - Network Policies</a>
**Tags:** k8s::kcna src::session topic::networking topic::networkpolicy topic::yaml

---

<!-- note:1793932382562 model:Many -->
**Domain:** kube-proxy - purpose
**Question:** What is the purpose of Kube Proxy in a Kubernetes cluster?
**Options:** A. It is used to monitor the health of the Kubernetes cluster.<br>B. It is used to create and manage Kubernetes objects like Pods and Services.<br>C. It is used to manage the storage resources in a Kubernetes cluster.<br>D. It is used to enable connectivity between pods and services across different nodes in the cluster.
**Answer:** D (4) – enable connectivity between pods and services across different nodes in the cluster
**Explanation:** kube-proxy runs on EVERY node (workers AND control plane — it's not a control-plane component) and implements Services at the node level: it watches Service and EndpointSlice objects through the API server and programs per-node packet rules — iptables, IPVS, nftables, or eBPF depending on proxy mode — that DNAT traffic destined for a ClusterIP to a ready pod IP, and that catch NodePort traffic arriving on the node. So 'pod → Service ClusterIP → some pod, possibly on another node' works transparently. It's not monitoring (that's kubelet probes/metrics-server), not object management (that's controllers), not storage. kube-proxy itself doesn't health-check pods — EndpointSlices only contain ready endpoints, maintained by the endpointslice mirroring controller.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/kube-proxy/" target="_blank">Kubernetes Docs - kube-proxy</a>
**Tags:** k8s::kcna src::session topic::networking topic::services

---

<!-- note:1793932581200 model:Many -->
**Domain:** ServiceAccounts - immutability
**Question:** What statement/s is/are true about the service account of an existing pod in Kubernetes?
**Options:** A. You can change the service account by running kubectl edit pod and modifying the service account field.<br>B. The service account of a pod can be changed by directly modifying the service account field in the running pod using kubectl apply without modifying the pod definition file.<br>C. The service account is set when the pod is created and cannot be changed afterwards.<br>D. You can change the service account by modifying the pod definition file and updating the service account name field.
**Answer:** C (3) – the service account is set when the pod is created and cannot be changed afterwards
**Explanation:** spec.serviceAccountName is immutable after pod creation — same pattern as spec.nodeName: it's fixed at admission and the API server rejects kubectl edit/patch/apply attempts on a live pod (that's why A, B and D all fail — D would work for a NEW pod via the definition file, but applying it to an existing pod errors on the immutable field). To change a pod's SA you must delete and recreate it — for Deployments that's updating the pod template and letting the rollout create new pods. Note the distinction: you CAN change what an SA is allowed to do (edit its RBAC bindings) — that changes permissions of the identity, not which identity the pod uses. The mounted token is also projected at creation, so the pod's credential can't be swapped in place either.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/" target="_blank">Kubernetes Docs - Configure Service Accounts for Pods</a>
**Tags:** k8s::kcna src::session topic::pods topic::security topic::serviceaccounts

---

<!-- note:1793932659732 model:Many -->
**Domain:** Node Authorization - role
**Question:** What is the role of the node authoriser in Kubernetes cluster?
**Options:** A. Handles requests from the kubelets on nodes to the kube-apiserver<br>B. Handles requests from human users to the kube-apiserver<br>C. Deploys and manages nodes within the Kubernetes cluster<br>D. Manages access control policies for the Kubernetes cluster
**Answer:** A (1) – handles requests from the kubelets on nodes to the kube-apiserver
**Explanation:** The Node authorizer is a specialized authorization module that handles ONLY kubelet→apiserver requests: it verifies the caller is authenticated as system:node:<nodeName> in group system:nodes, then decides what that kubelet may read/write for its own node — pods bound to it, node objects/status, mirrored EndpointSlices, leases, and certificate-signing requests for its serving certs (tightened by NodeRestriction). Human users never pass through it — they go through RBAC/Webhook/etc. It doesn't deploy or manage nodes (that's the kubelet executing instructions, and cluster autoscaler/node lifecycle controllers), and it doesn't manage access policies generally — that's RBAC's job; Node,RBAC run side by side in --authorization-mode.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/node/" target="_blank">Kubernetes Docs - Node authorizer</a>
**Tags:** k8s::kcna src::session topic::kubelet topic::rbac topic::security

---

<!-- note:1793932923824 model:Many -->
**Domain:** NetworkPolicy - CNI support
**Question:** Which of the following solutions support Kubernetes network policies?
**Options:** A. Flannel, weave-net, and kube-proxy<br>B. Calico, weave-net, and flannel<br>C. Kube router, calico, and flannel<br>D. Kube router, calico, and weave-net
**Answer:** D (4) – kube-router, calico, and weave-net
**Explanation:** NetworkPolicy is just an API — the CNI plugin must actually ENFORCE it, so support is entirely CNI-dependent. Calico, weave-net and kube-router all ship NetworkPolicy controllers (kube-router even has an official Kubernetes docs page for it; Cilium and Antrea do too). Flannel is the classic 'no' — flanneld only does overlay networking/routing and is policy-unaware (newer flannel charts can bundle a separate policy controller, but that's an add-on, not flannel itself). kube-proxy isn't a CNI at all — it programs Service ClusterIP/NodePort rules on each node; it has nothing to do with pod ingress/egress policy.
**Sources:** <a href="https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/kube-router-network-policy/" target="_blank">Kubernetes Docs - Use Kube-router for NetworkPolicy</a>
**Tags:** k8s::kcna src::session topic::cni topic::networking topic::networkpolicy

---

<!-- note:1793933047097 model:Many -->
**Domain:** NetworkPolicy - policyTypes
**Question:** If you have only the ingress in the policyTypes, what does it mean?
**Options:** A. Only the ingress traffic is isolated, and all egress traffic is unaffected.<br>B. Only the egress traffic is isolated, and all ingress traffic is unaffected.<br>C. Both ingress and egress traffic are isolated.<br>D. There is no network policy applied.
**Answer:** A (1) – only the ingress traffic is isolated, and all egress traffic is unaffected
**Explanation:** policyTypes declares which traffic DIRECTIONS the policy governs. Listing only Ingress means: selected pods get default-deny on inbound traffic, then the policy's ingress rules carve out exceptions — while egress is completely untouched, pods can still initiate any outbound connection. policyTypes: [Egress] does the reverse. The subtle default: if you OMIT policyTypes, Kubernetes infers it — an ingress: rules section implies Ingress, an egress: section implies Egress; and a policy with podSelector but NO rule lists at all defaults to BOTH directions (full isolation). Also note: NetworkPolicy never filters traffic to/from the node itself (hostNetwork/kubelet traffic is exempt).
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Docs - Network Policies</a>
**Tags:** k8s::kcna src::session topic::networking topic::networkpolicy topic::yaml

---

<!-- note:1793933351049 model:Many -->
**Domain:** ServiceAccounts - bound tokens
**Question:** What are the characteristics of tokens generated by the Kubernetes Token Request API?
**Options:** A. Audience bound, time bound, and object bound<br>B. Time bound, cluster bound, and namespace bound<br>C. Audience bound, object bound, and cluster bound<br>D. Time bound, object bound, and namespace bound
**Answer:** A (1) – audience bound, time bound, and object bound
**Explanation:** TokenRequest API tokens (authentication.k8s.io/v1 — also what kubectl create token and projected serviceAccountToken volumes use) carry three bindings: AUDIENCE-bound — spec.audiences becomes the JWT aud claim; a recipient must match one of them or reject the token (default: the API server). TIME-bound — spec.expirationSeconds sets exp/nbf/iat claims; kubelet auto-rotates projected tokens before expiry (~80% of TTL, default ~1h). OBJECT-bound (optional) — spec.boundObjectRef embeds the target object's name+UID as private claims; the token only works while that object exists AND the request comes from it (Pod/Secret, Node since v1.33). 'Cluster bound' and 'namespace bound' aren't TokenRequest concepts — this API replaced the legacy never-expiring Secret-mounted SA tokens.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/" target="_blank">Kubernetes Docs - Managing Service Accounts: Bound service account tokens</a>
**Tags:** k8s::kcna src::session topic::authentication topic::security topic::serviceaccounts

---

<!-- note:1793933689164 model:Many -->
**Domain:** Pods - imagePullSecrets
**Question:** How can we specify the secret to our private registry inside our pod definition file?
**Options:** A. By setting the environment variable in the container definition<br>B. By using the annotations in the pod definition file<br>C. By specifying the secret under the imagePullSecrets section in the pod definition file<br>D. By using the command line and specifying the secret name and registry URL
**Answer:** C (3) – specifying the secret under the imagePullSecrets section in the pod definition file
**Explanation:** spec.imagePullSecrets is the pod-spec field that tells the kubelet which Secret to use when pulling images from a private registry: spec.imagePullSecrets: [{name: regcred}] where regcred is a Secret of type kubernetes.io/dockerconfigjson holding .dockerconfigjson auth (created via kubectl create secret docker-registry). It works at PULL time — before the container starts — so env vars (runtime only) and annotations (metadata, not pull logic) can't do it, and there's no kubectl flag that attaches pull secrets to a pod. You can also set imagePullSecrets on a ServiceAccount so every pod using that SA inherits them. Older kubernetes.io/dockercfg secrets work too.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/" target="_blank">Kubernetes Docs - Pull an Image from a Private Registry</a>
**Tags:** k8s::kcna src::session topic::pods topic::secrets

---

<!-- note:1793933768337 model:Many -->
**Domain:** RBAC - RoleBinding structure
**Question:** What are the two sections of the RoleBinding object?
**Options:** A. Subjects and RoleRef<br>B. Users and Permissions<br>C. Role and User<br>D. APIGroups and Resources
**Answer:** A (1) – Subjects and RoleRef
**Explanation:** A RoleBinding has two functional sections: subjects — WHO gets the permissions (a list of kind: User/Group/ServiceAccount entries with name and namespace) — and roleRef — WHAT they get (a pointer with apiGroup, kind, and name referencing either a Role or a ClusterRole). roleRef is IMMUTABLE: you can't repoint an existing binding to a different role — delete and recreate it instead. A namespaced RoleBinding may reference a ClusterRole, but the granted permissions then apply only within the binding's namespace; ClusterRoleBinding is the cluster-wide variant with the same two fields.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security topic::yaml

---

<!-- note:1793934056843 model:Many -->
**Domain:** ServiceAccounts - token secrets
**Question:** Which of the following statements is true regarding service accounts in Kubernetes version 1.24?
**Options:** A. When a service account is created, it only creates a token access secret but not a regular secret.<br>B. When a service account is created, it only creates a secret but not a token access secret.<br>C. When a service account is created, it no longer automatically creates a secret or a token access secret.<br>D. When a service account is created, it automatically creates a secret and a token access secret.
**Answer:** C (3) – when a service account is created, it no longer automatically creates a secret or a token access secret
**Explanation:** Since Kubernetes 1.24 (KEP-2799), creating a ServiceAccount creates ONLY the SA object — no Secret is auto-generated. Before 1.24, kubectl create sa / a pod referencing an SA triggered creation of a kubernetes.io/service-account-token Secret holding a never-expiring JWT mounted into pods. That mechanism was removed because those tokens never expired and couldn't be rotated — pods now get short-lived, audience/time/object-bound tokens via the TokenRequest API and projected serviceAccountToken volumes instead. Legacy auto-created Secrets that already exist are NOT deleted, but they aren't refreshed either — migration path is to delete them and switch workloads to projected tokens.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/" target="_blank">Kubernetes Docs - Managing Service Accounts</a>
**Tags:** k8s::kcna src::session topic::secrets topic::security topic::serviceaccounts

---

<!-- note:1793934323616 model:Many -->
**Domain:** Kubeconfig - alternate file
**Question:** How do you make kubectl use a kubeconfig file other than the default ~/.kube/config?
**Options:** A. kubectl config use-context my-config<br>B. kubectl --kubeconfig=my-config <command> (global flag) or KUBECONFIG=my-config env var<br>C. kubectl config switch my-config<br>D. kubectl config edit my-config
**Answer:** B (2) – the --kubeconfig global flag on any kubectl command, or the KUBECONFIG environment variable
**Explanation:** --kubeconfig is a GLOBAL kubectl flag — it goes before the subcommand: kubectl --kubeconfig=my-config get pods — and points kubectl at exactly one file (no merging). KUBECONFIG=my-config does the same via env var, and accepts a LIST of files that get merged (first-set wins per key). Precedence: --kubeconfig flag > KUBECONFIG env > default ~/.kube/config. The distractors fail because: 'use-context'/'config use' switch contexts WITHIN a file, not files; 'config view --kubeconfig=' and 'config edit --kubeconfig=' only display/edit that file — they don't make kubectl use it for commands; 'config switch' isn't a real subcommand.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/" target="_blank">Kubernetes Docs - Organizing Cluster Access Using kubeconfig Files</a>
**Tags:** k8s::kcna src::session topic::kubeconfig topic::kubectl

---

<!-- note:1793934915989 model:Many -->
**Domain:** Authorization - AlwaysDeny
**Question:** What is the behavior of the AlwaysDeny authorisation mode in Kubernetes?
**Options:** A. Allows all requests without performing any authorisation checks<br>B. Allows requests based on a policy file with a set of policies defined in a JSON format<br>C. Denies all requests<br>D. Authorises requests coming from a user with the name system node and part of the system nodes group
**Answer:** C (3) – denies all requests
**Explanation:** AlwaysDeny is an --authorization-mode that rejects EVERY API request with 403 Forbidden — yes, literally nothing works while it's the only/first effective mode: no reads, no writes, kubectl dead. It's not for production; it's a deliberate kill-switch and testing tool: emergency lockdown of a compromised or misbehaving cluster, negative testing (prove your RBAC actually blocks things — if requests still succeed under AlwaysDeny, something upstream is wrong), and mode-ordering experiments. Its opposite pole is AlwaysAllow (permits everything after authentication — useful in dev/training clusters). Modes in --authorization-mode are evaluated in order and the first ALLOW wins — AlwaysDeny exists precisely so you can append it as a final 'deny everything else' backstop after real modes like Node,RBAC.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authorization/" target="_blank">Kubernetes Docs - Authorization</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security

---

<!-- note:1793935100778 model:Many -->
**Domain:** Secrets - SA token link
**Question:** What is the relationship between the secret object and the service account in Kubernetes?
**Options:** A. The service account is used to authenticate the secret object.<br>B. The secret object is linked to the service account and stores the service account token.<br>C. The service account is linked to the secret object and stores the API server endpoint.<br>D. The secret object is used to authenticate the service account.
**Answer:** B (2) – the secret object is linked to the service account and stores the service account token
**Explanation:** LEGACY model (pre-1.24, and still true for manually created token secrets): an SA's token lived in a Secret of type kubernetes.io/service-account-token — the Secret was linked to the SA (via annotation kubernetes.io/service-account.name) and stored its JWT, which pods mounted at /var/run/secrets/kubernetes.io/serviceaccount/. The Secret doesn't authenticate the SA — the SA IS the identity, the token just proves it; and the SA doesn't store the API endpoint (that's kubeconfig's job). MODERN model (1.24+): NO Secret is created — pods get short-lived audience/time/object-bound tokens via the TokenRequest API in a projected volume. That's why YOUR cluster lists SAs but no matching secrets: kubectl get secrets shows nothing of type service-account-token on a post-1.24 cluster.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/secret/" target="_blank">Kubernetes Docs - Secrets</a><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/" target="_blank">Kubernetes Docs - Managing Service Accounts</a>
**Tags:** k8s::kcna src::session topic::secrets topic::security topic::serviceaccounts

---

<!-- note:1793994897834 model:Many -->
**Domain:** Authorization - concept
**Question:** After a request is authenticated, what does Kubernetes authorization decide?
**Options:** A. Whether the authenticated identity is allowed to perform the requested action on the requested resource<br>B. Who the caller is — their username and groups<br>C. Whether the connection to the API server is TLS-encrypted<br>D. Which node the pod should be scheduled onto
**Answer:** A (1) – whether the authenticated identity is allowed to perform the requested action on the requested resource
**Explanation:** Authorization answers WHAT an authenticated caller may do: for each API request it evaluates the caller's identity (user + groups) against the request's attributes — verb (get/list/create/update/delete…), resource type, namespace, API path — and returns allow, deny, or no-opinion. Deny-by-default: if NO authorizer approves the request it's rejected 403 Forbidden. Authentication already answered WHO upstream in the request pipeline; authorization is the permission gate before admission control and etcd.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authorization/" target="_blank">Kubernetes Docs - Authorization</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security

---

<!-- note:1793994897835 model:Many -->
**Domain:** Authorization - vs authentication
**Question:** Which statement correctly contrasts authentication and authorization in Kubernetes?
**Options:** A. Authentication proves WHO the caller is; authorization decides WHAT that identity may do<br>B. Authentication decides permissions; authorization proves the caller's identity<br>C. They are the same pipeline stage with two names<br>D. Authorization only applies to pod-to-pod traffic, not API requests
**Answer:** A (1) – authentication proves WHO the caller is; authorization decides WHAT that identity may do
**Explanation:** Two separate pipeline stages with separate plugins. Authentication answers WHO: it turns a cert/token/password into an identity — username plus groups (cert CN→user, O→groups; SA→system:serviceaccount:<ns>:<name>). Authorization answers WHAT: given that identity + the request's verb/resource/namespace attributes, an authorizer (RBAC, Node, Webhook…) allows or denies. Key consequence: you can be fully authenticated and still completely denied — authenticated ≠ authorized. Common misconception: people treat them as one step; they're distinct stages, and RBAC bindings only matter AFTER authentication produces the identity they reference.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/controlling-access/" target="_blank">Kubernetes Docs - Controlling Access to the API</a>
**Tags:** k8s::kcna src::session topic::authentication topic::security

---

<!-- note:1793994897836 model:Many -->
**Domain:** Authorization - why
**Question:** Why does Kubernetes need authorization as a separate layer from authentication?
**Options:** A. Authenticated users need different permissions: admins get full access, developers get scoped-down rights, teams get namespace-limited access<br>B. Authentication is too slow, so authorization shortcuts it<br>C. Authorization is what encrypts Secrets at rest<br>D. The API server refuses to start without an authorization layer
**Answer:** A (1) – authenticated users need different permissions: admins get full access, developers get scoped-down rights, teams get namespace-limited access
**Explanation:** Authentication only answers 'are you who you claim' — without authorization, EVERY valid credential would have equal power over the cluster. Authorization implements least privilege: cluster admins need unrestricted access, developers need only their namespaces and workloads, CI bots need narrow verb sets. It's what lets one cluster safely serve many tenants/teams — the same API server, wildly different effective permissions per identity. Without it, a leaked developer kubeconfig = full cluster compromise.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/controlling-access/" target="_blank">Kubernetes Docs - Controlling Access to the API</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security

---

<!-- note:1793994897837 model:Many -->
**Domain:** Authorization - Webhook
**Question:** What does Webhook authorization mode do?
**Options:** A. Makes a synchronous HTTP callout to an external service that returns the allow/deny verdict<br>B. Reads permission rules from a local JSON policy file on the API server<br>C. Checks the requesting kubelet's node client certificate<br>D. Evaluates Role and ClusterRole objects like RBAC does
**Answer:** A (1) – makes a synchronous HTTP callout to an external service that returns the allow/deny verdict
**Explanation:** Webhook mode delegates the authorization decision entirely: the API server sends a SubjectAccessReview (user, groups, verb, resource, namespace) to your external endpoint and BLOCKS until it responds with allowed/denied — you can run your own logic or use ecosystem solutions like Open Policy Agent. Current clusters can chain MULTIPLE webhooks with matchConditions and failurePolicy via the structured --authorization-config file (the modern replacement for scattered --authorization-webhook-* flags). The failurePolicy matters: if your webhook is down, the config decides whether requests fail open (NoOpinion → next authorizer) or closed (deny).
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authorization/" target="_blank">Kubernetes Docs - Authorization</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security topic::webhook

---

<!-- note:1793994897838 model:Many -->
**Domain:** Authorization - AlwaysAllow
**Question:** What does AlwaysAllow authorization mode do — and when is it the default?
**Options:** A. Permits every request that passed authentication; it is the default when --authorization-mode is not set<br>B. Permits requests only from system:node identities<br>C. Denies every request except health checks<br>D. Delegates all decisions to an external webhook service
**Answer:** A (1) – permits every request that passed authentication; it is the default when --authorization-mode is not set
**Explanation:** AlwaysAllow is the 'no authorization' mode: any request that survived authentication is permitted — authentication becomes the only gate. It IS the default: if --authorization-mode isn't configured on the API server, AlwaysAllow applies (that's why fresh/kind/minikube clusters let your admin cert do anything). The docs warn explicitly: don't run it where the API server is reachable by clients you don't fully trust — every valid credential gets full power. It's for learning/testing clusters; real clusters set --authorization-mode=Node,RBAC (kubeadm default). Pairs with AlwaysDeny — together they bracket the authz spectrum.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authorization/" target="_blank">Kubernetes Docs - Authorization</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security

---

<!-- note:1793994897839 model:Many -->
**Domain:** Authorization - mode ordering
**Question:** With --authorization-mode=Node,RBAC, how are requests evaluated?
**Options:** A. Evaluated in order; the first authorizer to return allow OR deny wins immediately; if ALL return no-opinion the request is denied<br>B. Every configured authorizer must approve the request<br>C. RBAC always gets the final say regardless of order<br>D. The order is randomized on each API server restart
**Answer:** A (1) – evaluated in order; the first authorizer to return allow OR deny wins immediately; if ALL return no-opinion the request is denied
**Explanation:** Each configured authorizer returns one of three verdicts: allow, deny, or no-opinion. The chain evaluates in --authorization-mode order and the FIRST definitive verdict (allow or deny) is returned immediately — later modes aren't consulted. If every mode abstains (no opinion), the request is DENIED with 403 — deny-by-default. The trap: AlwaysAllow/AlwaysDeny always have an opinion, so position is everything — --authorization-mode=AlwaysAllow,RBAC behaves identically to AlwaysAllow alone (RBAC never gets asked). That's why production uses Node,RBAC: kubelets get Node-authorized first, humans fall through to RBAC.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authorization/" target="_blank">Kubernetes Docs - Authorization</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security

---

<!-- note:1793994897840 model:Many -->
**Domain:** Authorization - system:masters
**Question:** What is special about the system:masters group?
**Options:** A. A built-in group granting unrestricted API access that bypasses RBAC and Webhook authorization restrictions<br>B. A read-only group for monitoring tools<br>C. The group kubelets belong to for node authorization<br>D. A deprecated group kept only for backwards compatibility
**Answer:** A (1) – a built-in group granting unrestricted API access that bypasses RBAC and Webhook authorization restrictions
**Explanation:** system:masters is Kubernetes's break-glass group: any identity belonging to it gets full cluster-admin privileges regardless of what RBAC Roles/Bindings or webhooks say — authorization restrictions are bypassed entirely. That's why admin certs carry O=system:masters in their subject (the cert→group mapping you know) and why kubeadm's default admin kubeconfig works instantly. The docs warn against adding users to it: prefer a ClusterRoleBinding to the built-in cluster-admin ClusterRole instead — same power but visible/auditable in RBAC objects rather than a hidden group claim.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authorization/" target="_blank">Kubernetes Docs - Authorization</a>
**Tags:** k8s::kcna src::session topic::authentication topic::rbac topic::security

---

<!-- note:1793994897843 model:Cloze -->
**Text:** ABAC authorization: permission policies live in a {{c1::JSON policy file}} passed to the API server via {{c2::--authorization-policy-file}}; changing them requires {{c3::editing the file and restarting the API server}} — the operational pain that made {{c4::RBAC}} the standard instead.
**Back Extra:** ABAC = Attribute-Based Access Control: policies combine user attributes + resource attributes + environment attributes into allow rules. It predates RBAC and lost because every policy change meant editing the file AND restarting the API server — no dynamic updates, no kubectl management. RBAC replaced it by making permissions Kubernetes API objects editable live. Avoid ABAC in new clusters.
**Tags:** k8s::kcna src::session topic::abac topic::rbac topic::security

---

<!-- note:1793995451562 model:Many -->
**Domain:** RBAC - Role apiVersion
**Question:** Which apiVersion/kind defines a namespaced RBAC Role?
**Options:** A. apiVersion: rbac.authorization.k8s.io/v1, kind: Role<br>B. apiVersion: v1, kind: Role<br>C. apiVersion: rbac.authorization.k8s.io/v1, kind: ClusterRole<br>D. apiVersion: apps/v1, kind: Role
**Answer:** A (1) – rbac.authorization.k8s.io/v1, kind Role
**Explanation:** RBAC objects live in the rbac.authorization.k8s.io API group at v1: apiVersion: rbac.authorization.k8s.io/v1, kind: Role for namespaced roles (metadata.namespace required) or kind: ClusterRole for cluster-scoped ones (no namespace field — ClusterRoles can grant cluster-scoped resources like nodes, non-resource URLs like /healthz, and namespaced resources across ALL namespaces). Inside rules, apiGroups refers to the RESOURCE's API group — apiGroups: [""] means the core/v1 group (pods, secrets, configmaps…).
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security topic::yaml

---

<!-- note:1793995451563 model:Many -->
**Domain:** RBAC - rules structure
**Question:** What three fields define what a Role rule permits?
**Options:** A. apiGroups, resources, and verbs<br>B. subjects, roleRef, and namespace<br>C. name, labels, and annotations<br>D. apiVersion, kind, and metadata
**Answer:** A (1) – apiGroups, resources, and verbs
**Explanation:** Each entry in spec.rules is one permission set with three required dimensions — apiGroups (which API group the resources belong to; [""] = core), resources (plural resource names like pods, secrets, or subresources like pods/log, pods/exec), and verbs (get, list, watch, create, update, patch, delete, deletecollection — plus special verbs impersonate, bind, escalate). A request must match ALL dimensions of a rule to be allowed; multiple rules union together (additive — consistent with RBAC having no deny). Optional fields: resourceNames (restrict to named instances) and nonResourceURLs (for /healthz-style endpoints, ClusterRole only).
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security topic::yaml

---

<!-- note:1793995451564 model:Many -->
**Domain:** RBAC - linking
**Question:** What object links a user, group, or ServiceAccount to a Role's permissions?
**Options:** A. A RoleBinding (its subjects say WHO, its roleRef says WHAT)<br>B. A ClusterRole with a users field<br>C. An annotation on the user's kubeconfig<br>D. A LabelSelector on the Role object
**Answer:** A (1) – a RoleBinding (its subjects say WHO, its roleRef says WHAT)
**Explanation:** The RoleBinding is the link object: subjects[] lists WHO gets access (kind: User, Group, or ServiceAccount + name — names are case-sensitive) and roleRef points to WHAT they get (kind: Role or ClusterRole + name + apiGroup: rbac.authorization.k8s.io). A RoleBinding lives in a namespace and grants the role's permissions within THAT namespace only — even when roleRef points to a ClusterRole. ClusterRoleBinding is the cluster-wide variant. And remember roleRef is immutable — to change what a binding grants you delete and recreate it.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security topic::yaml

---

<!-- note:1793995451565 model:Many -->
**Domain:** RBAC - namespace scope
**Question:** A RoleBinding in namespace 'dev' references a ClusterRole. Where do the permissions apply?
**Options:** A. Only within the 'dev' namespace — the RoleBinding's own namespace sets the scope<br>B. Cluster-wide, because ClusterRoles are cluster-scoped<br>C. Only to user 'jane', cluster-wide<br>D. Nowhere — ClusterRoles can't be bound by RoleBindings
**Answer:** A (1) – only within the 'dev' namespace — the RoleBinding's own namespace sets the scope
**Explanation:** The RoleBinding's metadata.namespace decides WHERE permissions apply — NOT the roleRef's scope. A RoleBinding in namespace 'dev' referencing a ClusterRole grants those ClusterRole permissions ONLY inside 'dev'. This is the doc's own pattern: define ClusterRoles once (secret-reader) and reuse them across namespaces by creating a RoleBinding per namespace — 'dave' bound in 'development' reads secrets only there, not cluster-wide. To grant across ALL namespaces you need a ClusterRoleBinding instead. Role (namespaced) + RoleBinding (same ns) is the tightest scope.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna src::session topic::namespaces topic::rbac topic::security

---

<!-- note:1793995451566 model:Many -->
**Domain:** RBAC - kubectl create
**Question:** Which kubectl command creates a Role granting get/list/watch on pods in namespace 'default'?
**Options:** A. kubectl create role pod-reader --verb=get,list,watch --resource=pods --namespace=default<br>B. kubectl create clusterrole pod-reader --verb=get --resource=pods<br>C. kubectl create rolebinding pod-reader --role=pod-reader --user=jane<br>D. kubectl auth can-i get pods --as jane
**Answer:** A (1) – kubectl create role pod-reader --verb=get,list,watch --resource=pods --namespace=default
**Explanation:** kubectl create role builds a Role imperatively: --verb (repeatable or comma-separated), --resource (plural names), --api-group, and --namespace. Its sibling kubectl create rolebinding links subjects to it: kubectl create rolebinding read-pods --role=pod-reader --user=jane -n default (also --group= and --serviceaccount=ns:name subjects). Equivalent declarative path: kubectl apply -f role.yaml. Verify the result with kubectl auth can-i or kubectl get role,rolebinding -n default.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_role/" target="_blank">Kubernetes Docs - kubectl create role</a>
**Tags:** k8s::kcna src::session topic::kubectl topic::rbac

---

<!-- note:1793995451567 model:Many -->
**Domain:** RBAC - auth can-i
**Question:** Which command checks whether user 'jane' can get pods in namespace 'default'?
**Options:** A. kubectl auth can-i get pods --as jane -n default<br>B. kubectl get rolebindings -n default<br>C. kubectl describe clusterrole pod-reader<br>D. kubectl auth reconcile jane
**Answer:** A (1) – kubectl auth can-i get pods --as jane -n default
**Explanation:** kubectl auth can-i performs a live SubjectAccessReview against the cluster's actual authorization chain — it answers 'could this identity do this?' without changing anything. Flags: --as=<user> simulates an identity, --as-group=<group> adds groups, -n/--namespace scopes it, and --list shows EVERYTHING the (simulated) identity can do. It's the debugging tool for 'why can't X do Y' — check the effective answer instead of reading bindings by hand. auth can-i also verifies your own permissions: kubectl auth can-i create deployments.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_can-i/" target="_blank">Kubernetes Docs - kubectl auth can-i</a>
**Tags:** k8s::kcna src::session topic::kubectl topic::rbac

---

<!-- note:1793995451568 model:Many -->
**Domain:** RBAC - impersonation
**Question:** How do you act as another user or group with kubectl?
**Options:** A. kubectl --as=alice --as-group=devs get pods<br>B. kubectl sudo get pods<br>C. kubectl config set-credentials alice --token=x<br>D. kubectl exec -it alice -- whoami
**Answer:** A (1) – kubectl --as=alice --as-group=devs <command>
**Explanation:** kubectl's --as and --as-group flags make the API server treat the request as a different identity — kubectl --as=alice --as-group=devs get pods acts AS alice in group devs. It only works if YOUR identity has the impersonate verb (RBAC grants it on users/groups/serviceaccounts resources — e.g. system:masters or an impersonator ClusterRole). This is how you test 'what would X see/do' safely. Combine with kubectl auth can-i --as for pure checks without executing the action. Related flags: --as-uid for service-account UIDs.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/user-impersonation/" target="_blank">Kubernetes Docs - User Impersonation</a>
**Tags:** k8s::kcna src::session topic::kubectl topic::rbac

---

<!-- note:1793995451569 model:Many -->
**Domain:** RBAC - resourceNames
**Question:** What does resourceNames do in a Role rule?
**Options:** A. It restricts the rule to specific named resource instances<br>B. It encrypts the named resources at rest<br>C. It assigns resource quotas to the role<br>D. It namespaces the rule to a single namespace
**Answer:** A (1) – it restricts the rule to specific named resource instances
**Explanation:** resourceNames narrows a rule from 'all pods' to named instances: resources: [configmaps], resourceNames: [my-configmap], verbs: [get, update] lets the subject touch ONLY that one ConfigMap. Hard limits (doc-verified): you CANNOT restrict top-level create (the name doesn't exist at authz time) or deletecollection by resourceName; list/watch restricted by resourceName require the client to send a matching field-selector (kubectl get configmaps --field-selector=metadata.name=my-configmap); it DOES work on subresources like pods/exec. An empty resourceNames list means everything is allowed.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security topic::yaml

---

<!-- note:1793995451571 model:Cloze -->
**Text:** Minimal Role manifest (pod-reader in 'default'):<br><br><code>apiVersion: {{c1::rbac.authorization.k8s.io/v1}}<br>kind: {{c2::Role}}<br>metadata:<br>  namespace: {{c3::default}}<br>  name: pod-reader<br>rules:<br>- apiGroups: [{{c4::""}}]  # "" = core API group<br>  resources: [{{c5::pods}}]<br>  verbs: [{{c6::get, watch, list}}]</code>
**Back Extra:** rules is a LIST — each entry is one permission set where apiGroups + resources + verbs must all match a request. apiGroups: [""] = core/v1 resources. Multiple rules union (RBAC is additive — no deny). Verbs come from the API verb set; special verbs impersonate/bind/escalate gate RBAC-escalation itself. Same skeleton with kind: ClusterRole + no namespace grants cluster-wide.
**Tags:** k8s::kcna src::session topic::rbac topic::yaml

---

<!-- note:1793995451572 model:Cloze -->
**Text:** RoleBinding manifest linking user 'jane' to Role 'pod-reader':<br><br><code>apiVersion: {{c1::rbac.authorization.k8s.io/v1}}<br>kind: {{c2::RoleBinding}}<br>metadata:<br>  name: read-pods<br>  namespace: {{c3::default}}<br>subjects:<br>- kind: {{c4::User}}<br>  name: {{c5::jane}}<br>  apiGroup: rbac.authorization.k8s.io<br>roleRef:<br>  kind: {{c6::Role}}<br>  name: pod-reader<br>  apiGroup: rbac.authorization.k8s.io</code>
**Back Extra:** subjects = WHO gets it (kind User/Group/ServiceAccount + case-sensitive name + apiGroup); roleRef = WHAT (kind Role|ClusterRole + name + apiGroup — immutable, recreate to change). The binding's namespace sets scope: RoleBinding in 'dev' + ClusterRole ref = perms only in 'dev'. ClusterRoleBinding = cluster-wide. Create imperatively: kubectl create rolebinding read-pods --role=pod-reader --user=jane -n default.
**Tags:** k8s::kcna src::session topic::rbac topic::yaml

---

<!-- note:1794001609836 model:Many -->
**Domain:** ClusterRoles - cluster-scoped resources
**Question:** A Role in namespace 'prod' grants get/list/watch on 'nodes'. Why doesn't it work?
**Options:** A. Nodes are cluster-scoped — the rule must be in a ClusterRole bound by a ClusterRoleBinding<br>B. Nodes require resourceNames to be set<br>C. The apiGroup should be 'nodes' instead of ''<br>D. Roles cannot contain rules — only ClusterRoles can
**Answer:** A (1) – Nodes are cluster-scoped — the rule must be in a ClusterRole bound by a ClusterRoleBinding
**Explanation:** Cluster-scoped resources have no namespace, so namespaced RBAC can't reach them. kubectl api-resources --namespaced=false lists them: nodes, namespaces, persistentvolumes, clusterroles, storageclasses, CSRs and more. The doc is explicit: a nodes rule 'must be in a ClusterRole bound with a ClusterRoleBinding to be effective.' Role + RoleBinding only covers namespaced resources inside one namespace — for cluster-wide objects you need the Cluster* pair.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security

---

<!-- note:1794001609837 model:Many -->
**Domain:** ClusterRoles - apiVersion
**Question:** Which apiVersion/kind defines a cluster-wide RBAC role?
**Options:** A. apiVersion: rbac.authorization.k8s.io/v1, kind: ClusterRole<br>B. apiVersion: v1, kind: ClusterRole<br>C. apiVersion: rbac.authorization.k8s.io/v1, kind: Role<br>D. apiVersion: rbac.authorization.k8s.io/v1, kind: ClusterRoleBinding
**Answer:** A (1) – apiVersion: rbac.authorization.k8s.io/v1, kind: ClusterRole
**Explanation:** ClusterRoles live in the same rbac.authorization.k8s.io/v1 API group as Role/RoleBinding/ClusterRoleBinding. kind: ClusterRole is cluster-scoped — metadata has NO namespace field (a Role requires one). A ClusterRole's rules can cover three things: cluster-scoped resources (nodes, namespaces, PVs), non-resource URLs (/healthz — via nonResourceURLs), and namespaced resources across ALL namespaces when bound cluster-wide. Note ClusterRoleBinding is the binding object — it links subjects to a role, it doesn't define permissions itself.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security topic::yaml

---

<!-- note:1794001609838 model:Many -->
**Domain:** ClusterRoles - binding matrix
**Question:** Which statement about what bindings can reference is correct?
**Options:** A. A ClusterRoleBinding can only reference a ClusterRole; a RoleBinding can reference a Role or ClusterRole<br>B. A ClusterRoleBinding can reference Roles and ClusterRoles<br>C. A RoleBinding can only reference Roles<br>D. Bindings can reference any RBAC object
**Answer:** A (1) – A ClusterRoleBinding can only reference a ClusterRole; a RoleBinding can reference a Role or ClusterRole
**Explanation:** The scope matrix: RoleBinding→Role = permissions within the binding's namespace only. RoleBinding→ClusterRole = the ClusterRole's rules but ONLY inside that one namespace (the 'dave reads secrets in development' pattern — reuse one ClusterRole across namespaces). ClusterRoleBinding→ClusterRole = permissions across ALL namespaces plus cluster-scoped resources. ClusterRoleBinding→Role is invalid — a namespaced Role can't grant cluster-wide access. Memorize: binding type picks the SCOPE, roleRef.kind picks which role object.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security

---

<!-- note:1794001609839 model:Many -->
**Domain:** ClusterRoles - default roles
**Question:** Which built-in ClusterRole grants unrestricted super-user access and is bound to system:masters?
**Options:** A. cluster-admin<br>B. admin<br>C. edit<br>D. view
**Answer:** A (1) – cluster-admin
**Explanation:** cluster-admin is the super-user ClusterRole — any action on any resource; bound to the system:masters group (the O= field in admin kubeconfigs). The other user-facing defaults are the namespace trio, intended for RoleBindings: admin = read/write most resources + manage roles/rolebindings in the namespace; edit = read/write most objects but no RBAC objects; view = read-only, no roles/rolebindings and NO Secrets. User-facing ClusterRoles support aggregation: label a ClusterRole rbac.authorization.k8s.io/aggregate-to-admin/edit/view to inject rules into the defaults.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security

---

<!-- note:1794001609840 model:Many -->
**Domain:** ClusterRoles - admin edit view
**Question:** What is true about the default 'edit' ClusterRole?
**Options:** A. It allows reading Secrets and running Pods as any ServiceAccount in the namespace — a privilege-escalation path<br>B. It forbids access to Secrets entirely<br>C. It grants cluster-wide read/write access<br>D. It can modify RoleBindings
**Answer:** A (1) – It allows reading Secrets and running Pods as any ServiceAccount in the namespace — a privilege-escalation path
**Explanation:** Doc-verified distinctions: edit = read/write most objects in a namespace but NOT roles/rolebindings — yet it CAN access Secrets and run pods as any ServiceAccount, handing the user that SA's API access (escalation). view = read-only, and deliberately excludes Secrets because secret contents contain SA tokens → privesc. admin = edit + role/rolebinding management. None of the trio has a default binding — you create the RoleBinding yourself to grant them.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security

---

<!-- note:1794001609841 model:Many -->
**Domain:** ClusterRoles - kubectl create
**Question:** Which commands create a ClusterRole 'node-admin' and bind group 'ops' to it cluster-wide?
**Options:** A. kubectl create clusterrole node-admin --verb=get,list,watch,create,update,patch,delete --resource=nodes ; kubectl create clusterrolebinding node-admin --clusterrole=node-admin --group=ops<br>B. kubectl create role node-admin --verb=get --resource=nodes ; kubectl create rolebinding node-admin --role=node-admin --group=ops<br>C. kubectl create clusterrolebinding node-admin --role=node-admin --group=ops<br>D. kubectl auth can-i create nodes --as ops
**Answer:** A (1) – kubectl create clusterrole node-admin --verb=... --resource=nodes ; kubectl create clusterrolebinding node-admin --clusterrole=node-admin --group=ops
**Explanation:** kubectl create clusterrole mirrors create role (--verb, --resource, --api-group — no namespace needed since it's cluster-scoped). kubectl create clusterrolebinding links subjects cluster-wide using --clusterrole= (NOT --role=) plus --user=, --group=, or --serviceaccount=ns:name subjects. Doc example: kubectl create clusterrolebinding root-cluster-admin-binding --clusterrole=cluster-admin --user=root. Inspect with kubectl get clusterrole,clusterrolebinding -o yaml.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/" target="_blank">Kubernetes Docs - kubectl create clusterrole / clusterrolebinding</a>
**Tags:** k8s::kcna src::session topic::kubectl topic::rbac

---

<!-- note:1794001609842 model:Many -->
**Domain:** ClusterRoles - nonResourceURLs
**Question:** How does a ClusterRole grant access to endpoints like /healthz or /metrics that aren't Kubernetes resources?
**Options:** A. With the nonResourceURLs field — e.g. nonResourceURLs: ["/healthz", "/healthz/*"] with verbs<br>B. By listing them under resources as "healthz"<br>C. Via a special apiGroup called "nonresource"<br>D. It can't — only admission webhooks reach those endpoints
**Answer:** A (1) – With the nonResourceURLs field — e.g. nonResourceURLs: ["/healthz", "/healthz/*"] with verbs
**Explanation:** nonResourceURLs is a ClusterRole-only rules field for API endpoints that aren't Kubernetes resources: /healthz, /metrics, /version, /api, /apis. Format: nonResourceURLs: ["/healthz", "/healthz/*"] with verbs — '*' works as a suffix glob. These rules only take effect in a ClusterRole bound by a ClusterRoleBinding. Listing 'healthz' under resources won't work — it's not a resource type at all.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna src::session topic::api topic::rbac topic::security

---

<!-- note:1794001609843 model:Many -->
**Domain:** ClusterRoles - system roles
**Question:** You manually edit the rules of the system:discovery ClusterRole. What happens?
**Options:** A. The API server overwrites your changes at startup via auto-reconciliation<br>B. Nothing — manual edits to ClusterRoles are permanent<br>C. The cluster breaks immediately<br>D. Your changes merge permanently with the defaults
**Answer:** A (1) – The API server overwrites your changes at startup via auto-reconciliation
**Explanation:** system:-prefixed ClusterRoles and ClusterRoleBindings are control-plane managed (labeled kubernetes.io/bootstrapping=rbac-defaults). At EVERY apiserver start it re-adds missing permissions and subjects — auto-reconciliation repairs accidental edits and picks up new permissions each Kubernetes release. Opt out per-object with annotation rbac.authorization.kubernetes.io/autoupdate: "false", but missing defaults can leave the cluster non-functional. Never hand-edit system: roles — extend them instead via aggregate-to-* labels on your own ClusterRoles.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security

---

<!-- note:1794001609859 model:Cloze -->
**Text:** ClusterRole manifest granting full node management cluster-wide:<br><br><code>apiVersion: {{c1::rbac.authorization.k8s.io/v1}}<br>kind: {{c2::ClusterRole}}<br>metadata:<br>  name: node-admin<br>rules:<br>- apiGroups: [{{c3::""}}]<br>  resources: [{{c4::nodes}}]<br>  verbs: [{{c5::get, list, watch, create, update, patch, delete}}]</code>
**Back Extra:** No namespace field — ClusterRoles are cluster-scoped (Role requires metadata.namespace). nodes is a core-group resource so apiGroups: [""]. A ClusterRole alone grants nothing — it needs a ClusterRoleBinding to attach subjects. Same skeleton works for namespaces, persistentvolumes, clusterroles, storageclasses (all cluster-scoped).
**Tags:** k8s::kcna src::session topic::rbac topic::yaml

---

<!-- note:1794001609860 model:Cloze -->
**Text:** ClusterRoleBinding manifest granting group 'manager' secret read access in EVERY namespace:<br><br><code>apiVersion: {{c1::rbac.authorization.k8s.io/v1}}<br>kind: {{c2::ClusterRoleBinding}}<br>metadata:<br>  name: read-secrets-global<br>subjects:<br>- kind: {{c3::Group}}<br>  name: {{c4::manager}}<br>  apiGroup: rbac.authorization.k8s.io<br>roleRef:<br>  kind: {{c5::ClusterRole}}<br>  name: secret-reader<br>  apiGroup: rbac.authorization.k8s.io</code>
**Back Extra:** No namespace — the binding grants across ALL namespaces cluster-wide. roleRef.kind must be ClusterRole (can't point at a namespaced Role). roleRef is immutable — delete/recreate to change. subjects support User/Group/ServiceAccount kinds, names case-sensitive. Imperative equivalent: kubectl create clusterrolebinding read-secrets-global --clusterrole=secret-reader --group=manager.
**Tags:** k8s::kcna src::session topic::rbac topic::yaml

---

<!-- note:1794003812816 model:Many -->
**Domain:** ServiceAccounts - purpose
**Question:** What is the purpose of a ServiceAccount?
**Options:** A. It provides an identity for processes running in Pods to authenticate to the API server<br>B. It stores sensitive credentials for applications<br>C. It defines network access policies for pods<br>D. It groups human users for permission assignment
**Answer:** A (1) – It provides an identity for processes running in Pods to authenticate to the API server
**Explanation:** A ServiceAccount gives in-cluster workloads (pods) an identity — requests authenticate as system:serviceaccount:<namespace>:<name>, then RBAC decides what that identity may do. Kubernetes deliberately has NO User API object: SAs are the only first-class identity Kubernetes manages itself. Human access is a separate path entirely (client certs, tokens, OIDC).
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/" target="_blank">Kubernetes Docs - Configure Service Accounts for Pods</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security

---

<!-- note:1794003812817 model:Many -->
**Domain:** ServiceAccounts - users vs SAs
**Question:** How do human users get access to a Kubernetes cluster? (ServiceAccounts are NOT the mechanism)
**Options:** A. Client certificates, bearer tokens, or OIDC — they authenticate as User identities<br>B. By creating a ServiceAccount for each person<br>C. Via the serviceAccountName field in their kubeconfig<br>D. Through the default ServiceAccount in each namespace
**Answer:** A (1) – Client certificates, bearer tokens, or OIDC — they authenticate as User identities
**Explanation:** ServiceAccounts are for pod workloads, NOT people. Humans get cluster access by authenticating with client certificates (admin.conf kubeconfig), bearer tokens, or OIDC — becoming User identities with groups (e.g. system:masters) that RBAC then authorizes. SA identities look like system:serviceaccount:<ns>:<name> and belong to groups system:serviceaccounts and system:serviceaccounts:<ns>. If you need per-person access, issue certs/tokens — don't mint SAs.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/" target="_blank">Kubernetes Docs - Configure Service Accounts for Pods</a>
**Tags:** k8s::kcna src::session topic::authentication topic::rbac

---

<!-- note:1794003812818 model:Many -->
**Domain:** ServiceAccounts - kubectl create
**Question:** Which command creates a ServiceAccount named build-robot?
**Options:** A. kubectl create serviceaccount build-robot<br>B. kubectl create role build-robot<br>C. kubectl create secret build-robot<br>D. kubectl create token build-robot
**Answer:** A (1) – kubectl create serviceaccount build-robot
**Explanation:** kubectl create serviceaccount NAME makes one imperatively (equivalent: kubectl apply -f sa.yaml with apiVersion: v1, kind: ServiceAccount). The name must be a valid DNS subdomain. Related commands: kubectl get serviceaccounts lists them (NAME/SECRETS/AGE — the SECRETS column is a legacy artifact, mostly 0 since 1.24), kubectl describe serviceaccount <name>, kubectl delete serviceaccount <name>. A ServiceAccount alone grants nothing — pair it with RBAC RoleBindings to give it API permissions.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/" target="_blank">Kubernetes Docs - Configure Service Accounts for Pods</a>
**Tags:** k8s::kcna src::session topic::kubectl topic::rbac

---

<!-- note:1794003812819 model:Many -->
**Domain:** ServiceAccounts - default
**Question:** What happens when you create a Pod without spec.serviceAccountName?
**Options:** A. It is automatically assigned the 'default' ServiceAccount of its namespace<br>B. It gets no API credentials mounted at all<br>C. It uses a cluster-wide admin ServiceAccount<br>D. Pod creation fails validation without the field
**Answer:** A (1) – It is automatically assigned the 'default' ServiceAccount of its namespace
**Explanation:** Every namespace contains at least one SA — 'default'. If spec.serviceAccountName is unset, the API server assigns it at admission (visible in kubectl get pod <name> -o yaml). The default SA still gets its token mounted, so pods that never call the API should set automountServiceAccountToken: false. Best practice: create a dedicated SA per workload and bind only the RBAC it needs — never build apps on 'default'.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/" target="_blank">Kubernetes Docs - Configure Service Accounts for Pods</a>
**Tags:** k8s::kcna src::session topic::rbac topic::security

---

<!-- note:1794003812820 model:Many -->
**Domain:** ServiceAccounts - automount precedence
**Question:** Where can automountServiceAccountToken: false be set, and which wins if both are set?
**Options:** A. On the ServiceAccount OR in the Pod spec — the Pod spec takes precedence<br>B. Only on the Pod spec<br>C. Only on the ServiceAccount<br>D. On the Namespace — it cascades to all pods
**Answer:** A (1) – On the ServiceAccount OR in the Pod spec — the Pod spec takes precedence
**Explanation:** Two opt-out points for token mounting: set automountServiceAccountToken: false in the ServiceAccount manifest (covers every pod using it) OR spec.automountServiceAccountToken: false in the Pod (covers just that pod). Doc-verified: if BOTH specify a value, the POD SPEC wins. Either way the kubelet skips mounting token + CA cert at /var/run/secrets/kubernetes.io/serviceaccount/ — the pod simply can't authenticate to the API.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/" target="_blank">Kubernetes Docs - Configure Service Accounts for Pods</a>
**Tags:** k8s::kcna src::session topic::pods topic::rbac topic::security

---

<!-- note:1794003812821 model:Many -->
**Domain:** ServiceAccounts - create token
**Question:** What does kubectl create token build-robot do?
**Options:** A. It calls the TokenRequest API, prints a JWT to stdout, and stores nothing in the cluster<br>B. It creates a Secret containing a never-expiring token<br>C. It generates a token valid for 30 days by default<br>D. It requires a --save flag to persist the token
**Answer:** A (1) – It calls the TokenRequest API, prints a JWT to stdout, and stores nothing in the cluster
**Explanation:** kubectl create token NAME performs a TokenRequest for that SA and prints the signed JWT — nothing is persisted. Default lifetime is server-decided (~1h); --duration requests a lifetime but the server may return shorter OR longer. --audience sets the intended recipient (default: the API server). --bound-object-kind/name/uid (Pod/Secret/Node kinds) binds the token to an object — it dies when that object or the SA is deleted. Feature is Stable since v1.33.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_token/" target="_blank">Kubernetes Docs - kubectl create token</a>
**Tags:** k8s::kcna src::session topic::authentication topic::kubectl topic::rbac

---

<!-- note:1794003812822 model:Many -->
**Domain:** ServiceAccounts - long-lived token
**Question:** Can you get a ServiceAccount token that stays valid as long as the SA exists?
**Options:** A. Yes — create a Secret of type kubernetes.io/service-account-token annotated kubernetes.io/service-account.name: <sa>; the control plane fills in a token valid until the SA is deleted<br>B. No — all SA tokens expire within hours<br>C. Yes — kubectl create token --forever<br>D. Yes — set expirationSeconds: 0 in the pod spec
**Answer:** A (1) – Yes — create a Secret of type kubernetes.io/service-account-token annotated kubernetes.io/service-account.name: <sa>
**Explanation:** The manual legacy path still works: kubectl apply a Secret with annotation kubernetes.io/service-account.name: build-robot and type kubernetes.io/service-account-token — the control plane generates a token into .data.token that stays valid until the SA is deleted (auto-cleaned). Pre-1.24 this happened automatically for every SA; now it's opt-in. Docs recommend TokenRequest instead — never-expiring tokens are what 1.24 moved away from. Caution: never display the token field where screens can be seen.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/" target="_blank">Kubernetes Docs - Configure Service Accounts for Pods</a>
**Tags:** k8s::kcna src::session topic::rbac topic::secrets topic::security

---

<!-- note:1794003812823 model:Many -->
**Domain:** ServiceAccounts - imagePullSecrets
**Question:** How can all Pods using a ServiceAccount pull from a private registry without per-pod config?
**Options:** A. Add imagePullSecrets to the ServiceAccount object — pods using it inherit the registry credentials<br>B. Mount the dockerconfigjson Secret as a volume in each pod<br>C. Store registry credentials in a ConfigMap referenced by env vars<br>D. It is not possible — imagePullSecrets must be set per-pod
**Answer:** A (1) – Add imagePullSecrets to the ServiceAccount object — pods using it inherit the registry credentials
**Explanation:** ServiceAccount objects carry an imagePullSecrets field: kubectl patch serviceaccount default -p '{"imagePullSecrets":[{"name":"myregistrykey"}]}' (or kubectl edit serviceaccount/default). Every pod created with that SA inherits the dockerconfigjson credentials — much cleaner than repeating imagePullSecrets in each pod spec for registries many workloads share.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/" target="_blank">Kubernetes Docs - Configure Service Accounts for Pods</a>
**Tags:** k8s::kcna src::session topic::images topic::rbac

---

<!-- note:1794003812840 model:Cloze -->
**Text:** Pod spec binding to ServiceAccount 'build-robot' with token mounting disabled:<br><br><code>apiVersion: v1<br>kind: Pod<br>metadata:<br>  name: my-pod<br>spec:<br>  serviceAccountName: {{c1::build-robot}}<br>  automountServiceAccountToken: {{c2::false}}<br>  containers:<br>  - name: app<br>    image: nginx</code>
**Back Extra:** Set ONLY at pod creation (or in a workload's pod template) — serviceAccountName is immutable on existing pods, like nodeName. Deprecated alias: spec.serviceAccount (set both to empty to remove). The SA must exist in the pod's namespace. Omit the field → 'default' SA auto-assigned. Pod-level automountServiceAccountToken overrides the SA's own setting.
**Tags:** k8s::kcna src::session topic::rbac topic::yaml

---

<!-- note:1794003812841 model:Cloze -->
**Text:** Long-lived SA token via manually created Secret:<br><br><code>apiVersion: v1<br>kind: Secret<br>metadata:<br>  name: build-robot-secret<br>  annotations:<br>    kubernetes.io/service-account.name: {{c1::build-robot}}<br>type: {{c2::kubernetes.io/service-account-token}}</code>
**Back Extra:** The annotation is what triggers token generation — control plane writes the JWT into .data.token; valid until the SA is deleted, then auto-cleaned. This is the manual form of the pre-1.24 automatic behavior. kubectl get secret <name> -o yaml reveals it; kubectl describe shows the annotation. Prefer kubectl create token / TokenRequest for anything new.
**Tags:** k8s::kcna src::session topic::rbac topic::secrets topic::yaml

---

<!-- note:1794004823829 model:Many -->
**Domain:** User Access - CSR API
**Question:** How do you get the cluster to sign a client certificate for a new user?
**Options:** A. Create a CertificateSigningRequest, get it approved, then read the signed cert from .status.certificate<br>B. Run kubeadm certs sign on the control-plane node<br>C. Ask the kubelet to sign it via TLS bootstrap<br>D. kubectl create secret tls automatically issues client certs
**Answer:** A (1) – Create a CertificateSigningRequest, get it approved, then read the signed cert from .status.certificate
**Explanation:** The cluster-native signing path: kubectl apply a certificates.k8s.io/v1 CertificateSigningRequest (signerName: kubernetes.io/kube-apiserver-client, usages: [client auth]) → an admin runs kubectl certificate approve <name> → the signed cert appears in the CSR's .status.certificate (base64 — decode it). The control plane's csrsigning controller stamps it with the cluster CA. Requires RBAC rights on certificatesigningrequests — typically only admins can request/approve.
**Sources:** <a href="https://kubernetes.io/docs/setup/best-practices/certificates/" target="_blank">Kubernetes Docs - PKI certificates and requirements</a>
**Tags:** k8s::kcna src::session topic::authentication topic::certificates topic::tls

---

<!-- note:1794004823830 model:Many -->
**Domain:** User Access - CA signing
**Question:** Where do you get the CA cert and key needed to manually sign a user's client certificate?
**Options:** A. On a control-plane node under /etc/kubernetes/pki/ — ca.crt + ca.key on kubeadm clusters<br>B. Inside the etcd database under the /registry/certs key<br>C. In the user's kubeconfig under certificate-authority-data<br>D. Distributed to every node via the kubelet's serving cert
**Answer:** A (1) – On a control-plane node under /etc/kubernetes/pki/ — ca.crt + ca.key on kubeadm clusters
**Explanation:** To sign a user CSR yourself you need the cluster CA's private key. On kubeadm clusters it lives on control-plane nodes: /etc/kubernetes/pki/ca.crt (public, distributed everywhere) and /etc/kubernetes/pki/ca.key (the crown jewels — whoever holds it can mint any identity). Then: openssl x509 -req -in user.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out user.crt -days 365. The CSR API path avoids touching ca.key directly.
**Sources:** <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/" target="_blank">Kubernetes Docs - kubeadm certificate management</a>
**Tags:** k8s::kcna src::session topic::authentication topic::certificates topic::tls

---

<!-- note:1794004823831 model:Many -->
**Domain:** User Access - kubeconfig build
**Question:** Which commands assemble a kubeconfig file for a new user?
**Options:** A. kubectl config set-cluster + set-credentials + set-context + use-context, with --embed-certs=true<br>B. kubectl create kubeconfig --user=dev1 --sign<br>C. kubectl get --raw /api/v1/namespaces/default/serviceaccount/default/token<br>D. Copy /var/lib/kubelet/pki/kubelet.conf to the user
**Answer:** A (1) – kubectl config set-cluster + set-credentials + set-context + use-context, with --embed-certs=true
**Explanation:** Assemble the file with kubectl config subcommands: set-cluster <name> --server=https://... --certificate-authority=ca.crt --embed-certs=true (inlines the CA cert so the file is portable); set-credentials <user> --client-certificate=user.crt --client-key=user.key --embed-certs=true (inlines cert+key); set-context <ctx> --cluster=<name> --user=<user>; use-context <ctx> to activate. Send the resulting ~/.kube/config — it contains everything needed, no external file refs.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/" target="_blank">Kubernetes Docs - Organize Cluster Access Using Kubeconfig Files</a>
**Tags:** k8s::kcna src::session topic::authentication topic::certificates topic::kubectl

---

<!-- note:1794004823832 model:Many -->
**Domain:** User Access - admin.conf
**Question:** What is the fastest way to give someone full admin access to a kubeadm cluster?
**Options:** A. Copy /etc/kubernetes/admin.conf from a control-plane node — it already embeds client certs, server, and context<br>B. Run kubectl create serviceaccount admin -n kube-system<br>C. Export the KUBECONFIG env var on the user's laptop<br>D. kubectl cp the kubelet.conf from any worker node
**Answer:** A (1) – Copy /etc/kubernetes/admin.conf from a control-plane node — it already embeds client certs, server, and context
**Explanation:** admin.conf is a ready-made kubeconfig kubeadm generates on control-plane nodes: server URL + cluster CA + an admin client cert/key (CN=kubernetes-admin, O=system:masters) all embedded. Copy it to the person's ~/.kube/config and they have full cluster-admin immediately — no CSR, no RBAC binding needed since system:masters bypasses authorization. It's the fast path for a second cluster admin; wrong choice for developers (way over-privileged).
**Sources:** <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/" target="_blank">Kubernetes Docs - kubeadm certificate management</a>
**Tags:** k8s::kcna src::session topic::authentication topic::certificates topic::rbac

---

<!-- note:1794004823833 model:Many -->
**Domain:** User Access - RBAC gate
**Question:** You hand someone a valid client-cert kubeconfig but they get 403 on everything. Why?
**Options:** A. Authentication succeeded (cert is valid) but no RBAC binding grants their identity permissions — cert proves WHO, RBAC decides WHAT<br>B. The certificate lacks a SAN entry for the API server<br>C. kubectl requires the --insecure-skip-tls-verify flag<br>D. The user's kubeconfig context points at the wrong cluster
**Answer:** A (1) – Authentication succeeded (cert is valid) but no RBAC binding grants their identity permissions — cert proves WHO, RBAC decides WHAT
**Explanation:** A valid client cert only gets you authenticated — the API server then runs authorization and with no Role/ClusterRoleBinding matching their CN or O group, every request returns 403. The workflow is always two steps: (1) issue identity (cert/token/OIDC), (2) bind permissions (kubectl create rolebinding dev1-edit --role=edit --user=dev1 -n dev). Test with kubectl auth can-i --as=dev1 to verify what their identity can actually do.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Docs - Authentication</a>
**Tags:** k8s::kcna src::session topic::authentication topic::certificates topic::rbac

---

<!-- note:1794004823834 model:Many -->
**Domain:** User Access - OIDC
**Question:** How do organizations provide cluster access without distributing certificates?
**Options:** A. An OIDC issuer + exec credential plugin (e.g. kubelogin) in the kubeconfig — groups come from IdP claims<br>B. A shared admin.conf copied to every developer<br>C. Long-lived SA token Secrets distributed via email<br>D. Client certs signed by a public certificate authority
**Answer:** A (1) – An OIDC issuer + exec credential plugin (e.g. kubelogin) in the kubeconfig — groups come from IdP claims
**Explanation:** Production clusters skip cert distribution: the API server is configured with an OIDC issuer, and users' kubeconfigs use an exec credential plugin (kubelogin for Azure AD, kubectl-oidc-login, etc.) that fetches a fresh token from the IdP on each call. Identity + group claims come from the IdP → RBAC binds those groups. Revoking access = disable the IdP account — nothing long-lived sits on the user's machine to leak.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Docs - Authentication</a>
**Tags:** k8s::kcna src::session topic::authentication topic::rbac

---

<!-- note:1794004823835 model:Many -->
**Domain:** User Access - revocation
**Question:** How do you cut off a user's cluster access after you've issued them a client certificate?
**Options:** A. Delete their RBAC bindings — access ends immediately even though the cert remains cryptographically valid<br>B. Revoke the cert through the cluster CA's CRL<br>C. kubectl delete secret containing the client cert<br>D. Restart the kube-apiserver to flush the auth cache
**Answer:** A (1) – Delete their RBAC bindings — access ends immediately even though the cert remains cryptographically valid
**Explanation:** Two layers, two revocation speeds: RBAC bindings take effect instantly — delete the RoleBinding/ClusterRoleBinding and the identity can do nothing (cert still valid but authorized for zero actions). Certificate revocation is the slow path: there's no CRL/OCSP in K8s client auth, so you wait for cert expiry or rotate the CA. Practical rule: grant access via GROUPS bound in RBAC — removing someone from the IdP group or deleting bindings cuts access without touching their cert.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Docs - Authentication</a>
**Tags:** k8s::kcna src::session topic::authentication topic::rbac

---

<!-- note:1794004823845 model:Cloze -->
**Text:** CertificateSigningRequest manifest for user 'dev1':<br><br><code>apiVersion: {{c1::certificates.k8s.io/v1}}<br>kind: {{c2::CertificateSigningRequest}}<br>metadata:<br>  name: dev1<br>spec:<br>  request: &lt;base64 CSR&gt;<br>  signerName: {{c3::kubernetes.io/kube-apiserver-client}}<br>  usages: [{{c4::"client auth"}}]</code>
**Back Extra:** spec.request holds the base64-encoded CSR (openssl req -new -key user.key -out user.csr, then base64 -w0). After kubectl certificate approve dev1, the signed cert lands in .status.certificate — decode with base64 -d. Requires RBAC rights to create+approve CSRs. usages must include 'client auth' for kubeconfig use.
**Tags:** k8s::kcna src::session topic::authentication topic::certificates topic::yaml

---

<!-- note:1794004823846 model:Cloze -->
**Text:** Assemble a kubeconfig for user 'dev1' — the four kubectl config commands:<br><br>{{c1::<code>kubectl config set-cluster prod --server=https://API:6443 --certificate-authority=ca.crt --embed-certs=true</code>}}<br>{{c2::<code>kubectl config set-credentials dev1 --client-certificate=dev1.crt --client-key=dev1.key --embed-certs=true</code>}}<br>{{c3::<code>kubectl config set-context dev1@prod --cluster=prod --user=dev1</code>}}<br>{{c4::<code>kubectl config use-context dev1@prod</code>}}
**Back Extra:** --embed-certs=true base64-inlines the CA into certificate-authority-data and cert+key into the user stanza — the file becomes fully self-contained/portable (that's what you email someone). Without it, kubectl looks for the referenced files on disk. Order: set-cluster → set-credentials → set-context → use-context. current-context in the file decides what plain 'kubectl get pods' uses.
**Tags:** k8s::kcna src::session topic::authentication topic::kubectl

---

<!-- note:1794006447942 model:Many -->
**Domain:** Registry Auth - secret type
**Question:** What Secret type stores container-registry credentials for image pulls?
**Options:** A. kubernetes.io/dockerconfigjson — a Secret holding a .dockerconfigjson key with the registry auths<br>B. kubernetes.io/tls — a TLS cert/key pair for the registry<br>C. Opaque — any Secret type works for registry auth<br>D. kubernetes.io/service-account-token
**Answer:** A (1) – kubernetes.io/dockerconfigjson — a Secret holding a .dockerconfigjson key with the registry auths
**Explanation:** Registry credentials live in a Secret of type kubernetes.io/dockerconfigjson. Its data key .dockerconfigjson holds a base64'd docker config.json: {"auths":{"registry.example.com":{"username":..,"password":..,"auth":"base64(user:pass)"}}}. The legacy type kubernetes.io/dockercfg used the older ~/.dockercfg format — prefer dockerconfigjson. The kubelet reads this Secret at image-pull time and authenticates to the matching registry.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/" target="_blank">Kubernetes Docs - Pull an Image from a Private Registry</a>
**Tags:** k8s::kcna src::session topic::images topic::secrets topic::security

---

<!-- note:1794006447944 model:Many -->
**Domain:** Registry Auth - pull flow
**Question:** How does a Pod authenticate to a private image registry?
**Options:** A. Create the dockerconfigjson Secret in the pod's namespace, then reference it in spec.imagePullSecrets — the kubelet uses it at pull time<br>B. Add registry credentials to the pod's env vars<br>C. kubectl login inside the pod before the image pulls<br>D. Annotate the pod with the registry password
**Answer:** A (1) – Create the dockerconfigjson Secret in the pod's namespace, then reference it in spec.imagePullSecrets — the kubelet uses it at pull time
**Explanation:** End-to-end: (1) kubectl create secret docker-registry regcred ... in the SAME namespace as the pod — namespace mismatch is the #1 failure; (2) pod spec gets imagePullSecrets: [{name: regcred}]; (3) kubelet pulls the image using those creds before the container starts. If the Secret is missing the pod sits in ImagePullBackOff and kubectl describe pod shows FailedToRetrieveImagePullSecret. The Secret can also live on a ServiceAccount so all its pods inherit it.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/" target="_blank">Kubernetes Docs - Pull an Image from a Private Registry</a>
**Tags:** k8s::kcna src::session topic::images topic::pods topic::secrets

---

<!-- note:1794006447946 model:Many -->
**Domain:** Registry Auth - multiple registries
**Question:** A Pod has containers from quay.io AND a private ECR registry — how do you supply credentials for both?
**Options:** A. Multiple imagePullSecrets per pod, each holding credentials for multiple registries — the kubelet tries the credential matching the image's registry<br>B. Only one imagePullSecret is allowed per pod<br>C. The registry must be listed in the pod's image field<br>D. A single Secret can only hold one registry's credentials
**Answer:** A (1) – Multiple imagePullSecrets per pod, each holding credentials for multiple registries — the kubelet tries the credential matching the image's registry
**Explanation:** A pod with containers from different registries can list several imagePullSecrets, and each Secret's .dockerconfigjson can hold auths for multiple registries. At pull time the kubelet selects the credential matching that image's registry; if none matches it attempts the pull unauthenticated (or via runtime-specific config). imagePullSecrets is a pod-level list — order doesn't matter, matching is by registry hostname.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/" target="_blank">Kubernetes Docs - Pull an Image from a Private Registry</a>
**Tags:** k8s::kcna src::session topic::images topic::pods topic::secrets

---

<!-- note:1794006447949 model:Cloze -->
**Text:** Pod manifest pulling from a private registry via Secret 'regcred':<br><br><code>apiVersion: v1<br>kind: Pod<br>metadata:<br>  name: private-reg<br>spec:<br>  containers:<br>  - name: app<br>    image: your.private.registry.example.com/janedoe/app:v1<br>  {{c1::imagePullSecrets}}:<br>  - name: {{c2::regcred}}</code>
**Back Extra:** imagePullSecrets is a LIST under spec — each entry references a Secret of type kubernetes.io/dockerconfigjson that must exist in the pod's namespace. The kubelet uses these credentials when pulling <private.registry>/app before the container starts. Same field exists on a ServiceAccount to cover all its pods.
**Tags:** k8s::kcna src::session topic::images topic::secrets topic::yaml

---

<!-- note:1794006612602 model:Many -->
**Domain:** SecurityContext - concept
**Question:** What is securityContext and why does it exist?
**Options:** A. Privilege and access-control settings for a Pod or Container — UID/GID, capabilities, seccomp, AppArmor, SELinux, read-only rootfs<br>B. Network rules controlling which pods can talk to each other<br>C. Resource quotas limiting CPU and memory per pod<br>D. TLS certificates used to encrypt pod-to-pod traffic
**Answer:** A (1) – Privilege and access-control settings for a Pod or Container — UID/GID, capabilities, seccomp, AppArmor, SELinux, read-only rootfs
**Explanation:** securityContext defines privilege and access control for pods/containers: runAsUser/runAsGroup (UID/GID), capabilities (Linux privileges), privileged mode, allowPrivilegeEscalation (blocks setuid gains), readOnlyRootFilesystem, seccompProfile, appArmorProfile, seLinuxOptions. It exists because containers share the host kernel — isolation is weaker than a VM, so these settings are the per-workload hardening layer that Pod Security Standards then enforce cluster-wide.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes Docs - Configure a Security Context for a Pod or Container</a>
**Tags:** k8s::kcna src::session topic::pods topic::podsecurity topic::security

---

<!-- note:1794006612603 model:Many -->
**Domain:** SecurityContext - pod vs container
**Question:** Where do pod-level and container-level securityContext fields live in the spec?
**Options:** A. spec.securityContext = PodSecurityContext for ALL containers (+ volumes); spec.containers[].securityContext = SecurityContext for ONE container<br>B. spec.securityContext is for containers, spec.podSecurityContext is for the pod<br>C. Both fields are identical — placement doesn't matter<br>D. spec.securityContext only works on Deployments, not bare Pods
**Answer:** A (1) – spec.securityContext = PodSecurityContext for ALL containers (+ volumes); spec.containers[].securityContext = SecurityContext for ONE container
**Explanation:** Two different objects at two levels: spec.securityContext is a PodSecurityContext applying to every container in the pod (and volumes — fsGroup controls volume ownership); spec.containers[].securityContext is a SecurityContext applying to just that one container. The Pod object is the broader default; the container object is the per-workload override.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes Docs - Configure a Security Context for a Pod or Container</a>
**Tags:** k8s::kcna src::session topic::podsecurity topic::security topic::yaml

---

<!-- note:1794006612604 model:Many -->
**Domain:** SecurityContext - override
**Question:** A Pod sets spec.securityContext.runAsUser: 1000 but its container sets securityContext.runAsUser: 2000. What UID does the process run as?
**Options:** A. The container runs as UID 2000 — container-level securityContext overrides pod-level on overlap<br>B. The container runs as UID 1000 — pod-level always wins<br>C. Pod creation is rejected — conflicting UIDs<br>D. The container runs as root — container settings are ignored
**Answer:** A (1) – The container runs as UID 2000 — container-level securityContext overrides pod-level on overlap
**Explanation:** Doc example: pod sets securityContext.runAsUser: 1000 but the container sets securityContext.runAsUser: 2000 → the process runs as 2000. Container settings override pod settings wherever they overlap; pod settings are the defaults for everything not overridden. One asymmetry: container settings do NOT affect the pod's volumes — fsGroup and friends only exist at pod level.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes Docs - Configure a Security Context for a Pod or Container</a>
**Tags:** k8s::kcna src::session topic::podsecurity topic::security

---

<!-- note:1794006612606 model:Many -->
**Domain:** SecurityContext - allowPrivilegeEscalation
**Question:** What does allowPrivilegeEscalation: false do, and what is its default?
**Options:** A. It defaults to true; setting false blocks setuid-based privilege gains and is incompatible with privileged:true or CAP_SYS_ADMIN<br>B. It defaults to false; set true to allow setuid binaries<br>C. It only applies at pod level, not container level<br>D. It controls whether the container can escalate to host root via nsenter
**Answer:** A (1) – It defaults to true; setting false blocks setuid-based privilege gains and is incompatible with privileged:true or CAP_SYS_ADMIN
**Explanation:** allowPrivilegeEscalation controls whether a process can gain MORE privileges than its parent — e.g. by executing a setuid binary. It maps to the kernel's no_new_privs flag (inverted: allowPrivilegeEscalation: false sets no_new_privs). If undefined it DEFAULTS TO TRUE — so you must opt out explicitly. It's inconsistent with privileged: true or CAP_SYS_ADMIN and can't be combined with them. This is the field Pod Security Standards 'restricted' requires.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes Docs - Configure a Security Context for a Pod or Container</a>
**Tags:** k8s::kcna src::session topic::pods topic::podsecurity topic::security

---

<!-- note:1794006612607 model:Many -->
**Domain:** SecurityContext - capabilities
**Question:** How do you apply least privilege with Linux capabilities in a container securityContext?
**Options:** A. capabilities.drop: ["ALL"] then add back only what's needed — least privilege; privileged:true grants everything<br>B. Capabilities can only be added, never dropped<br>C. privileged:true is required for any container to function<br>D. capabilities are set at pod level only, never per-container
**Answer:** A (1) – capabilities.drop: ["ALL"] then add back only what's needed — least privilege; privileged:true grants everything
**Explanation:** Linux capabilities are the granular privileges root normally holds (NET_ADMIN, SYS_ADMIN, DAC_OVERRIDE…). Hardened containers drop ALL capabilities then add back only required ones: securityContext.capabilities.drop: ["ALL"], add: ["NET_BIND_SERVICE"]. privileged: true is the nuclear option — ALL capabilities plus host device access — required for things like CNI plugins but a massive risk in multi-tenant clusters; Pod Security Standards 'baseline' forbids it.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes Docs - Configure a Security Context for a Pod or Container</a>
**Tags:** k8s::kcna src::session topic::pods topic::podsecurity topic::security

---

<!-- note:1794006612610 model:Cloze -->
**Text:** Pod-level securityContext manifest (from the docs):<br><br><code>apiVersion: v1<br>kind: Pod<br>metadata:<br>  name: security-context-demo<br>spec:<br>  securityContext:<br>    runAsUser: {{c1::1000}}<br>    runAsGroup: {{c2::3000}}<br>    fsGroup: {{c3::2000}}<br>    supplementalGroups: [{{c4::4000}}]<br>  containers:<br>  - name: sec-ctx-demo<br>    image: busybox<br>    securityContext:<br>      allowPrivilegeEscalation: {{c5::false}}</code>
**Back Extra:** Pod-level fields seen here: runAsUser/runAsGroup (UID/GID for all containers), fsGroup (volume group ownership), supplementalGroups (extra groups). Container-level adds per-container overrides like allowPrivilegeEscalation: false and capabilities. The id output would be uid=1000 gid=3000 groups=2000,3000,4000 — pod settings apply to every container unless overridden.
**Tags:** k8s::kcna src::session topic::podsecurity topic::security topic::yaml

---

<!-- note:1794006612611 model:Cloze -->
**Text:** Container-level override example — pod says 1000, container says 2000:<br><br><code>spec:<br>  securityContext:<br>    runAsUser: {{c1::1000}}        # pod default for all containers<br>  containers:<br>  - name: sec-ctx-demo-2<br>    securityContext:<br>      runAsUser: {{c2::2000}}      # overrides pod → runs as 2000<br>      allowPrivilegeEscalation: {{c3::false}}</code>
**Back Extra:** securityContext-2.yaml verbatim: pod-level runAsUser: 1000, container-level runAsUser: 2000 → process runs as 2000 (container wins on overlap). Container settings apply ONLY to that container and never affect pod volumes. kubectl exec -it <pod> -- id confirms the effective UID/GID/groups.
**Tags:** k8s::kcna src::session topic::podsecurity topic::security topic::yaml

---

<!-- note:1794006990743 model:Many -->
**Domain:** Networking - ingress egress
**Question:** What do ingress and egress mean for a Pod's network traffic?
**Options:** A. Ingress = traffic INTO the pod; egress = traffic OUT of the pod — each direction is isolated independently<br>B. Ingress = pod-to-pod traffic; egress = pod-to-internet traffic<br>C. Ingress is enforced by kube-proxy; egress by the CNI<br>D. Ingress applies to Services; egress applies to Pods
**Answer:** A (1) – Ingress = traffic INTO the pod; egress = traffic OUT of the pod — each direction is isolated independently
**Explanation:** Ingress is inbound traffic to a pod (who may connect to it); egress is outbound traffic from a pod (where it may connect to). Isolation is declared per-direction and independently: a pod can be isolated for ingress while fully open for egress, or vice versa. 'Isolated' doesn't mean blocked — it means only explicitly allowed connections pass; 'non-isolated' means no restrictions. By default pods are non-isolated BOTH ways — the flat pod network lets any pod reach any pod or namespace.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Docs - Network Policies</a>
**Tags:** k8s::kcna src::session topic::networking topic::networkpolicy

---

<!-- note:1794006990744 model:Many -->
**Domain:** NetworkPolicy - apiVersion
**Question:** Which apiVersion/kind defines a Kubernetes NetworkPolicy?
**Options:** A. apiVersion: networking.k8s.io/v1, kind: NetworkPolicy<br>B. apiVersion: v1, kind: NetworkPolicy<br>C. apiVersion: networking.k8s.io/v1, kind: NetworkPolicyList<br>D. apiVersion: policy/v1, kind: NetworkPolicy
**Answer:** A (1) – apiVersion: networking.k8s.io/v1, kind: NetworkPolicy
**Explanation:** NetworkPolicy lives in the networking.k8s.io API group at v1: apiVersion: networking.k8s.io/v1, kind: NetworkPolicy — namespaced, so metadata.namespace matters (a policy only selects pods in its own namespace). Mandatory fields beyond the usual apiVersion/kind/metadata: spec.podSelector (which pods it applies to — empty {} selects ALL pods in the namespace), spec.policyTypes (Ingress/Egress/both), and spec.ingress/spec.egress rule lists. Without a CNI that enforces NetworkPolicy, the object is accepted but does NOTHING.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Docs - Network Policies</a>
**Tags:** k8s::kcna src::session topic::networking topic::networkpolicy topic::yaml

---

<!-- note:1794006990745 model:Many -->
**Domain:** Networking - both sides
**Question:** For a connection from pod A to pod B to be allowed by NetworkPolicies, what must be true?
**Options:** A. BOTH — the source pod's egress policy AND the destination pod's ingress policy must allow it<br>B. Only the destination's ingress policy matters<br>C. Only the source's egress policy matters<br>D. Whichever policy was created first
**Answer:** A (1) – BOTH — the source pod's egress policy AND the destination pod's ingress policy must allow it
**Explanation:** A NetworkPolicy connection requires consent from BOTH ends: the source pod's egress rules must allow the destination, AND the destination pod's ingress rules must allow the source. If either side doesn't permit it, the connection never happens — you can't open egress on the client and expect it to reach an isolated server. This is why 'default deny ingress' on a backend forces you to also think about what clients are allowed to initiate.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Docs - Network Policies</a>
**Tags:** k8s::kcna src::session topic::networking topic::networkpolicy

---

<!-- note:1794006990746 model:Many -->
**Domain:** Networking - selectors
**Question:** What are the selector types you can use in a NetworkPolicy's ingress.from / egress.to?
**Options:** A. podSelector (pods in same namespace), namespaceSelector (whole namespaces), ipBlock (external CIDR ranges)<br>B. podSelector, serviceSelector, and nodeSelector<br>C. matchLabels, matchExpressions, and fieldSelector<br>D. ingressSelector, egressSelector, and cidrSelector
**Answer:** A (1) – podSelector (pods in same namespace), namespaceSelector (whole namespaces), ipBlock (external CIDR ranges)
**Explanation:** from/to entries accept three selector types: podSelector picks pods in the policy's OWN namespace by labels; namespaceSelector picks entire namespaces by labels (all their pods); ipBlock picks cluster-external CIDR ranges — pod IPs are ephemeral so ipBlock is for outside-the-cluster sources like load balancers. A single entry can combine namespaceSelector + podSelector to mean 'these labeled pods within these labeled namespaces'. kubectl describe shows how the CNI actually interpreted the policy.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Docs - Network Policies</a>
**Tags:** k8s::kcna src::session topic::labels topic::networking topic::networkpolicy

---

<!-- note:1794006990747 model:Many -->
**Domain:** Networking - selector AND OR
**Question:** namespaceSelector + podSelector in ONE map vs as separate list items — what's the difference?
**Options:** A. One map with both selectors = AND (labeled pods inside labeled namespaces); two separate list items = OR<br>B. They always AND together regardless of YAML structure<br>C. They always OR together regardless of YAML structure<br>D. podSelector can't be combined with namespaceSelector at all
**Answer:** A (1) – One map with both selectors = AND (labeled pods inside labeled namespaces); two separate list items = OR
**Explanation:** The classic YAML gotcha: namespaceSelector and podSelector in the SAME map element are ANDed — 'pods labeled role=client in namespaces labeled user=alice'. As SEPARATE elements of the from/to list they're ORed — 'pods labeled role=client in ANY namespace, OR any pod in namespaces labeled user=alice'. Same labels, wildly different policy. When in doubt: kubectl describe networkpolicy shows the CNI's interpretation.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Docs - Network Policies</a>
**Tags:** k8s::kcna src::session topic::networking topic::networkpolicy topic::yaml

---

<!-- note:1794006990748 model:Many -->
**Domain:** Networking - additive
**Question:** Which statements about Kubernetes NetworkPolicy behavior are true? (Select all that apply)
**Options:** A. When multiple policies select the same pod, their allowed rules combine additively<br>B. Both the source's egress and the destination's ingress must allow a connection<br>C. Reply traffic for allowed connections is implicitly permitted<br>D. Policies are evaluated in creation order — first match wins<br>E. Traffic between a pod and its own node is always allowed
**Answer:** A, B, C, E – policies union additively; both ends must allow; reply traffic is implicit; node traffic always allowed
**Explanation:** (Select all that apply) NetworkPolicies never conflict — when several select the same pod+direction, the allowed connections are the UNION of all their rules; evaluation order is irrelevant. Both ends of a connection must permit it (source egress + dest ingress). Reply traffic for allowed connections is implicitly permitted — you don't write return-path rules. Edge cases: a pod can't block traffic to itself, and traffic to/from the pod's own node is always allowed regardless of policy.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Docs - Network Policies</a>
**Tags:** k8s::kcna src::session topic::networking topic::networkpolicy

---

<!-- note:1794006990752 model:Cloze -->
**Text:** NetworkPolicy manifest — isolate role=db pods, allow redis traffic:<br><br><code>apiVersion: {{c1::networking.k8s.io/v1}}<br>kind: {{c2::NetworkPolicy}}<br>metadata:<br>  name: test-network-policy<br>  namespace: default<br>spec:<br>  podSelector:<br>    matchLabels:<br>      role: {{c3::db}}<br>  policyTypes: [{{c4::Ingress, Egress}}]<br>  ingress:<br>  - from:<br>    - podSelector:<br>        matchLabels:<br>          role: frontend<br>    ports:<br>    - port: {{c5::6379}}<br>  egress:<br>  - to:<br>    - ipBlock:<br>        cidr: 10.0.0.0/24</code>
**Back Extra:** The doc's example isolates role=db pods for BOTH directions: ingress allows TCP 6379 from role=frontend pods (same ns), any pod in project=myproject namespaces, and 172.17.0.0/16 minus 172.17.1.0/24; egress allows TCP 5978 to 10.0.0.0/24. Apply with kubectl apply -f — but only works if your CNI enforces NetworkPolicy.
**Tags:** k8s::kcna src::session topic::networking topic::networkpolicy topic::yaml

---

<!-- note:1794007966270 model:Many -->
**Domain:** Cluster Networking - apiserver port
**Question:** Which port does the Kubernetes API server listen on by default?
**Options:** A. TCP 6443<br>B. TCP 443<br>C. TCP 2379<br>D. TCP 10250
**Answer:** A (1) – TCP 6443 — the Kubernetes API server, the port EVERY component talks through
**Explanation:** kube-apiserver listens on TCP 6443 inbound by default — it's the single front door: kubelets, kube-proxy, controllers, scheduler, kubectl, and every Pod's ServiceAccount token all authenticate to it. In firewall-restricted environments (on-prem DCs, VPC security groups) 6443 is the one port that must be reachable by everything. It's a default, not a law — teams often put the API server behind a load balancer on 443 and route to 6443 internally.
**Sources:** <a href="https://kubernetes.io/docs/reference/networking/ports-and-protocols/" target="_blank">Kubernetes Docs - Ports and Protocols</a>
**Tags:** k8s::kcna src::session topic::control-plane topic::networking

---

<!-- note:1794007966271 model:Many -->
**Domain:** Cluster Networking - control plane ports
**Question:** Which ports must be open on control plane nodes? (Select all that apply)
**Options:** A. 6443 — kube-apiserver<br>B. 2379-2380 — etcd client API<br>C. 10257 — kube-controller-manager<br>D. 10259 — kube-scheduler<br>E. 10255 — kubelet read-only API
**Answer:** A, B, C, D – 6443 apiserver, 2379-2380 etcd, 10257 controller-manager, 10259 scheduler
**Explanation:** (Select all that apply) Control plane inbound TCP ports: 6443 kube-apiserver (all components), 2379-2380 etcd client API (apiserver↔etcd), 10257 kube-controller-manager (self only — its secure endpoint), 10259 kube-scheduler (self only). NOT on the list: 10255 is the long-deprecated kubelet read-only port, 10256 is kube-proxy (worker-side health endpoint), and 443 is only there if you override the API server port.
**Sources:** <a href="https://kubernetes.io/docs/reference/networking/ports-and-protocols/" target="_blank">Kubernetes Docs - Ports and Protocols</a>
**Tags:** k8s::kcna src::session topic::control-plane topic::networking

---

<!-- note:1794007966272 model:Many -->
**Domain:** Cluster Networking - etcd ports
**Question:** Which ports does etcd need open, and who talks to it?
**Options:** A. TCP 2379-2380 — etcd's client API range; 2379 for client traffic, 2380 for peer replication<br>B. TCP 6443-6444 — etcd mirrors the API server ports<br>C. TCP 10250 — etcd shares the kubelet port<br>D. UDP 2379 — etcd uses UDP for replication
**Answer:** A (1) – TCP 2379-2380 — etcd's client API range; 2379 for client traffic, 2380 for peer replication
**Explanation:** etcd listens on TCP 2379-2380 inbound: 2379 serves the client API (kube-apiserver is the client — it's the only regular consumer), 2380 handles peer-to-peer replication between etcd members. etcd stores ALL cluster state so these ports matter for quorum. The doc notes etcd can also run EXTERNAL to the control plane or on custom ports — then only the apiserver↔etcd path needs opening, not the whole range everywhere.
**Sources:** <a href="https://kubernetes.io/docs/reference/networking/ports-and-protocols/" target="_blank">Kubernetes Docs - Ports and Protocols</a>
**Tags:** k8s::kcna src::session topic::control-plane topic::etcd topic::networking

---

<!-- note:1794007966273 model:Many -->
**Domain:** Cluster Networking - kubelet port
**Question:** Which port does the kubelet serve its API on?
**Options:** A. TCP 10250 — the kubelet API: self plus the control plane (logs, exec, metrics, probes)<br>B. TCP 10257 — kubelets share the controller-manager port<br>C. TCP 4194 — the kubelet's flannel VXLAN port<br>D. TCP 6782-6784 — kubelet metrics ports
**Answer:** A (1) – TCP 10250 — the kubelet API: self plus the control plane (logs, exec, metrics, probes)
**Explanation:** kubelet serves its API on TCP 10250 inbound — used by the kubelet itself AND the control plane, which reaches in for kubectl logs/exec, metrics scraping, and probe results. On worker nodes this is THE port that must be open to the control plane subnet. (Historical note: 10255 was the old read-only kubelet port — deprecated and gone from the docs because it leaked pod specs without auth.)
**Sources:** <a href="https://kubernetes.io/docs/reference/networking/ports-and-protocols/" target="_blank">Kubernetes Docs - Ports and Protocols</a>
**Tags:** k8s::kcna src::session topic::kubelet topic::networking

---

<!-- note:1794007966274 model:Many -->
**Domain:** Cluster Networking - kube-proxy port
**Question:** What is TCP 10256 for?
**Options:** A. TCP 10256 — kube-proxy's healthz/metrics endpoint, used by itself and load balancers<br>B. TCP 10250 — kube-proxy shares the kubelet port<br>C. TCP 30000-32767 — kube-proxy's own management range<br>D. UDP 10256 — kube-proxy uses UDP for service traffic
**Answer:** A (1) – TCP 10256 — kube-proxy's healthz/metrics endpoint, used by itself and load balancers
**Explanation:** kube-proxy opens TCP 10256 inbound — it's NOT the port that carries Service traffic (that's whatever NodePort/hostPort the Service uses); 10256 is kube-proxy's own health/metrics endpoint so load balancers and monitoring can check whether the proxy is alive on each node. If you health-check kube-proxy through an LB or scrape its metrics, this is the port to allow.
**Sources:** <a href="https://kubernetes.io/docs/reference/networking/ports-and-protocols/" target="_blank">Kubernetes Docs - Ports and Protocols</a>
**Tags:** k8s::kcna src::session topic::networking topic::services

---

<!-- note:1794007966275 model:Many -->
**Domain:** Cluster Networking - NodePort range
**Question:** Which port range must be open on worker nodes for NodePort Services?
**Options:** A. TCP and UDP 30000-32767 — the default NodePort range, open on every worker node<br>B. TCP 3000-3010 — the default HTTP service range<br>C. TCP 8080-8090 — the kube-proxy forwarding range<br>D. UDP 53 only — NodePort uses DNS ports
**Answer:** A (1) – TCP and UDP 30000-32767 — the default NodePort range, open on every worker node
**Explanation:** NodePort Services get a port in the default range 30000-32767 on EVERY node — both TCP and UDP are listed because the Service protocol decides which. kube-proxy on each node catches traffic arriving at nodeIP:nodePort and forwards it to a ready pod. The range is customizable (--service-node-port-range on the API server) — if you change it, open the NEW range instead. This is why NodePort is 'expose on all nodes': any node's IP works as an entry point.
**Sources:** <a href="https://kubernetes.io/docs/reference/networking/ports-and-protocols/" target="_blank">Kubernetes Docs - Ports and Protocols</a>
**Tags:** k8s::kcna src::session topic::networking topic::services

---

<!-- note:1794007966276 model:Many -->
**Domain:** Cluster Networking - port overrides
**Question:** Can the default component ports be changed?
**Options:** A. All of them are defaults — e.g. API server is often moved behind a 443 load balancer<br>B. Only the API server port can be changed<br>C. Ports are compiled into the kubelet binary<br>D. Changing ports requires recompiling Kubernetes
**Answer:** A (1) – All of them are defaults — e.g. API server is often moved behind a 443 load balancer
**Explanation:** Every port in the table is a default, not fixed: --secure-port on kube-apiserver, --etcd-servers for etcd placement, kubelet's --port, kube-proxy's --healthz-port/metrics-port, and --service-node-port-range for NodePort. The classic pattern: keep the API server on 6443 internally but front it with a load balancer listening on 443 that routes to it — external clients hit 443, internal traffic stays on 6443.
**Sources:** <a href="https://kubernetes.io/docs/reference/networking/ports-and-protocols/" target="_blank">Kubernetes Docs - Ports and Protocols</a>
**Tags:** k8s::kcna src::session topic::control-plane topic::networking

---

<!-- note:1794007966277 model:Many -->
**Domain:** Cluster Networking - node prereqs
**Question:** What network prerequisites must every node in a Kubernetes cluster satisfy?
**Options:** A. Each node needs ≥1 networked interface with an IP, a unique hostname, a unique MAC, and the documented ports open<br>B. All nodes must share one flat L2 broadcast domain<br>C. Each node needs a public IP address<br>D. Hostnames must match pod names exactly
**Answer:** A (1) – Each node needs ≥1 networked interface with an IP, a unique hostname, a unique MAC, and the documented ports open
**Explanation:** Cluster networking prerequisites per node: at least one interface connected to a network, each interface has an IP address, and the host has a unique hostname and unique MAC address — pod networking overlays (VXLAN etc.) and kubelet identity assume no two nodes look alike at L2. On top of that, the firewall must allow the documented component ports (6443, 2379-2380, 10250, 10256, 10257, 10259, NodePort range). Break any of these and you get subtle failures: duplicate hostnames confuse node identity, missing ports show up as probe/metrics timeouts.
**Sources:** <a href="https://kubernetes.io/docs/reference/networking/ports-and-protocols/" target="_blank">Kubernetes Docs - Ports and Protocols</a>
**Tags:** k8s::kcna src::session topic::cluster-setup topic::networking

---

<!-- note:1794007966278 model:Cloze -->
**Text:** Default Kubernetes ports — control plane then workers:<br><br>Control plane (all TCP inbound):<br>{{c1::kube-apiserver}} → {{c2::6443}} (all components)<br>{{c3::etcd}} → {{c4::2379-2380}} (client API)<br>{{c5::kube-controller-manager}} → {{c6::10257}} (self)<br>{{c7::kube-scheduler}} → {{c8::10259}} (self)<br><br>Worker nodes:<br>{{c9::kubelet}} → {{c10::10250}}<br>kube-proxy → {{c11::10256}} (healthz)<br>NodePort Services → {{c12::30000-32767}} TCP+UDP
**Back Extra:** Direction is always INBOUND to the listed component. kubelet 10250 appears on BOTH control plane and workers (control plane reaches in for logs/exec/metrics). etcd can live externally or on custom ports. NodePort range is a default — change it and open the new range instead. kube-proxy 10256 is health/metrics only, NOT service traffic.
**Tags:** k8s::kcna src::session topic::control-plane topic::networking

---

<!-- note:1794008796228 model:Many -->
**Domain:** Services - pod access
**Question:** How can a pod within a Kubernetes cluster reach a service?
**Options:** A. By using the service's DNS record<br>B. By using the service name<br>C. By using the cluster's DNS server<br>D. By using the pod's IP address
**Answer:** B (2) – By using the service name
**Explanation:** A pod reaches a Service by connecting to its NAME (my-service or my-service.ns.svc.cluster.local) — the stable identifier you configure in the app. CoreDNS then resolves that name to the ClusterIP, and kube-proxy forwards ClusterIP traffic to a ready pod. Why not the others: the DNS record and DNS server are the RESOLUTION MECHANISM that makes the name work — they describe how the name is looked up, not what the pod connects to (and resolv.conf already points at CoreDNS automatically). Pod IP bypasses the Service completely — no ClusterIP, no load balancing, and pod IPs are ephemeral. Name vs IP is the real distinction: stable vs unstable.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/service/" target="_blank">Kubernetes Docs - Service</a><br><a href="https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/" target="_blank">Kubernetes Docs - DNS for Services and Pods</a>
**Tags:** k8s::kcna src::session topic::dns topic::networking topic::services

---

<!-- note:1794009611473 model:Many -->
**Domain:** CNI - disabling masquerade
**Question:** When would you set ipMasquerade/ipMasq to false in a CNI configuration? (Select all that apply)
**Options:** A. Pod CIDRs are routable outside the cluster and you need end-to-end pod addressing<br>B. External systems must see real pod source IPs for whitelists or audit<br>C. Pods never need external connectivity — internal-only or air-gapped<br>D. Pods need outbound internet access
**Answer:** A, B, C – routable pod CIDR / source-IP preservation / internal-only clusters
**Explanation:** (Select all that apply) Masquerade trades source-IP fidelity for reachability — disable it (ipMasq/ipMasquerade/natOutgoing=false) when: pod CIDRs are externally routable and you want end-to-end pod addressing (routed/BGP networks); external systems must see REAL pod source IPs for whitelisting or audit (masquerade hides every pod behind its node's IP); or pods never need external connectivity (air-gapped/internal-only) so NAT is pure overhead. NOT a reason: pods needing internet access — that's exactly when masquerade must stay ON.
**Sources:** <a href="https://kubernetes.io/docs/concepts/cluster-administration/networking/" target="_blank">Kubernetes Docs - Cluster Networking</a>
**Tags:** k8s::kcna src::session topic::cni topic::networking

---

<!-- note:1794016331742 model:Many -->
**Domain:** Pod Networking - requirements
**Question:** What does the Kubernetes network model require of pod networking? (Select all that apply)
**Options:** A. Every Pod gets its own IP address<br>B. Pods on the same node can communicate with each other<br>C. Pods on different nodes can communicate without NAT<br>D. Pods must communicate with each other through a NAT gateway<br>E. Every Pod must have a unique MAC address cluster-wide
**Answer:** A, B, C – every pod gets an IP; same-node pods reach each other; cross-node pods reach each other WITHOUT NAT
**Explanation:** (Select all that apply) The Kubernetes network model's core requirements: every Pod gets its own routable IP address; Pods on the same node communicate (localhost/bridge); Pods on DIFFERENT nodes communicate directly — WITHOUT NAT, meaning pod IPs are end-to-end routable across the cluster network. 'Without NAT' is the key constraint — it forbids hiding pod IPs behind node IPs for in-cluster traffic (that's what masquerade does only for EXTERNAL egress).
**Sources:** <a href="https://kubernetes.io/docs/concepts/cluster-administration/networking/" target="_blank">Kubernetes Docs - Cluster Networking</a>
**Tags:** k8s::kcna src::session topic::networking topic::podnetwork

---

<!-- note:1794016331743 model:Many -->
**Domain:** Pod Networking - who implements
**Question:** Kubernetes does not solve pod networking itself — what actually implements it?
**Options:** A. CNI plugins via the container runtime — Kubernetes only defines the requirements<br>B. kube-proxy alone handles all pod networking<br>C. The kube-apiserver assigns pod IPs directly<br>D. kubelet writes iptables rules for pod traffic
**Answer:** A (1) – CNI plugins via the container runtime — Kubernetes only defines the requirements
**Explanation:** Kubernetes deliberately does NOT implement pod networking — it specifies what must be true (IP per pod, NAT-free pod-to-pod) and lets CNIs satisfy it. The container runtime on each node invokes CNI plugins (bridge, Calico, Cilium, flannel…) which actually create interfaces, assign IPs, and wire routes. Many vendor CNIs exist offering different features — basic interface management up to integrated NetworkPolicy, advanced IPAM, multi-plugin chaining.
**Sources:** <a href="https://kubernetes.io/docs/concepts/cluster-administration/networking/" target="_blank">Kubernetes Docs - Cluster Networking</a>
**Tags:** k8s::kcna src::session topic::cni topic::networking

---

<!-- note:1794016331744 model:Many -->
**Domain:** Pod Networking - IP allocation
**Question:** Who assigns IP addresses to Pods, Services, and Nodes respectively?
**Options:** A. Network plugin assigns Pod IPs, kube-apiserver assigns Service IPs, kubelet/cloud-controller-manager assigns Node IPs<br>B. kube-apiserver assigns all three types<br>C. kubelet assigns Pod and Node IPs, network plugin assigns Service IPs<br>D. The CNI plugin assigns Service IPs too
**Answer:** A (1) – Network plugin assigns Pod IPs, kube-apiserver assigns Service IPs, kubelet/cloud-controller-manager assigns Node IPs
**Explanation:** Three different allocators for three object types, all from non-overlapping configured ranges: the NETWORK PLUGIN (CNI/IPAM) assigns Pod IPs; the kube-APISERVER assigns Service ClusterIPs; the KUBELET or cloud-controller-manager assigns Node IPs (cloud provider reports them). Knowing who owns which range matters for debugging IP conflicts and understanding why pod IPs and service IPs live in different CIDRs.
**Sources:** <a href="https://kubernetes.io/docs/concepts/cluster-administration/networking/" target="_blank">Kubernetes Docs - Cluster Networking</a>
**Tags:** k8s::kcna src::session topic::networking topic::services

---

<!-- note:1794016331745 model:Many -->
**Domain:** Pod Networking - NAT-free
**Question:** Why does the Kubernetes network model require pod-to-pod communication WITHOUT NAT?
**Options:** A. Pod IPs must be end-to-end routable — NAT would hide the real pod IP and break the return path/identity<br>B. NAT is faster than direct routing for pod traffic<br>C. Kubernetes requires NAT for pod-to-pod encryption<br>D. NAT is only needed on Windows nodes
**Answer:** A (1) – Pod IPs must be end-to-end routable — NAT would hide the real pod IP and break the return path/identity
**Explanation:** 'Without NAT' means pod-to-pod packets keep their real pod IPs all the way across nodes — the cluster network routes them directly. NAT is only acceptable for traffic LEAVING the cluster (that's what CNI masquerade/ipMasq does for external egress). If pod-to-pod used NAT, source identity would collapse to node IPs, conntrack state would multiply, and asymmetric paths could break replies — the model forbids it so pods have stable, meaningful IPs everywhere in the cluster.
**Sources:** <a href="https://kubernetes.io/docs/concepts/cluster-administration/networking/" target="_blank">Kubernetes Docs - Cluster Networking</a>
**Tags:** k8s::kcna src::session topic::cni topic::networking

---

<!-- note:1794016331748 model:Many -->
**Domain:** Pod Networking - who solves what
**Question:** Which component solves which networking problem?
**Options:** A. pod-to-pod is CNI's job; pod-to-Service and external-to-Service are Services' job<br>B. CNI handles everything including Service load balancing<br>C. kube-proxy handles pod-to-pod; CNI handles Services<br>D. The kube-apiserver routes all four types
**Answer:** A (1) – pod-to-pod is CNI's job; pod-to-Service and external-to-Service are Services' job
**Explanation:** The docs split cluster networking into 4 problems with different owners: container-to-container on one pod = localhost (free); POD-TO-POD = CNI plugins (the network model — IPs, interfaces, routes); POD-TO-SERVICE and EXTERNAL-TO-SERVICE = Services (ClusterIP, kube-proxy, Ingress). This is why kube-proxy doesn't assign pod IPs (CNI does) and CNI doesn't load-balance service names (Services do) — complementary layers, not competing ones.
**Sources:** <a href="https://kubernetes.io/docs/concepts/cluster-administration/networking/" target="_blank">Kubernetes Docs - Cluster Networking</a>
**Tags:** k8s::kcna src::session topic::cni topic::networking topic::services

---

<!-- note:1794016331749 model:Many -->
**Domain:** Pod Networking - IP families
**Question:** How are Kubernetes clusters categorized by IP family?
**Options:** A. IPv4-only, IPv6-only, or dual-stack — and all components must agree on the primary IP family<br>B. Only IPv4 is supported for pod networking<br>C. Dual-stack requires a special CNI license<br>D. Each node can independently choose its IP family
**Answer:** A (1) – IPv4-only, IPv6-only, or dual-stack — and all components must agree on the primary IP family
**Explanation:** Clusters are categorized by configured IP families: IPv4-only, IPv6-only, or dual-stack (IPv4/IPv6 or IPv6/IPv4). For dual-stack ALL components must agree — network plugin assigns both families to pods, kube-apiserver assigns both to services, kubelet/CCM assigns node IPs, and they must agree on which family is PRIMARY. Only IPs in pod.status.ips/node.status.addresses count for the model — extra interface IPs are ignored.
**Sources:** <a href="https://kubernetes.io/docs/concepts/cluster-administration/networking/" target="_blank">Kubernetes Docs - Cluster Networking</a>
**Tags:** k8s::kcna src::session topic::cluster-setup topic::networking

---

<!-- note:1794016331753 model:Cloze -->
**Text:** Kubernetes pod networking model — the requirements and who implements them:<br><br>K8s requires: every Pod gets {{c1::its own IP address}}; Pods on the same node can {{c2::communicate}}; Pods on different nodes can communicate {{c3::without NAT}}.<br><br>K8s does NOT implement this — the {{c4::container runtime}} invokes {{c5::CNI plugins}} on each node.<br><br>IP allocation: {{c6::network plugin}} → Pod IPs; {{c7::kube-apiserver}} → Service IPs; {{c8::kubelet/cloud-controller-manager}} → Node IPs.
**Back Extra:** K8s defines the WHAT, CNIs provide the HOW — the container runtime invokes CNI plugins per node. IP owners: network plugin→Pods, kube-apiserver→Services, kubelet/CCM→Nodes (all non-overlapping). Pod-to-pod = CNI; pod/service/external-to-service = Services. Runtime reads .conflist from --cni-conf-dir, executes plugin from --cni-bin-dir with ADD/DEL commands.
**Tags:** k8s::kcna src::session topic::cni topic::networking topic::podnetwork

---

<!-- note:1794077951412 model:Many -->
**Domain:** Pod Phases - Pending triage
**Question:** A pod is in 'Pending' state for a long time. Which is the most likely cause?
**Options:** A. The pod's liveness probe is failing<br>B. No node has enough CPU or memory to meet the pod's requests<br>C. The pod's readiness probe is not configured<br>D. The container image does not exist
**Answer:** B (2) – No node has enough CPU or memory to meet the pod's requests
**Explanation:** Pending means the pod never got SCHEDULED — it exists in the API but no kube-scheduler bound it to a node, almost always because every node's allocatable CPU/memory minus existing requests can't fit this pod's requests. The distractors all fail at a LATER stage: a failing liveness probe crashes a RUNNING container (restarts, not Pending); a missing image fails in ContainerCreating (ErrImagePull/ImagePullBackOff); a missing readiness probe doesn't block scheduling. Triage rule: Pending = scheduling problem; check 'kubectl describe pod' events for 'Insufficient cpu/memory'.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/" target="_blank">Kubernetes Docs - Pod Lifecycle</a>
**Tags:** k8s::kcna src::session topic::pods topic::resources topic::scheduling

---

<!-- note:1794078127990 model:Many -->
**Domain:** Resiliency Patterns - circuit breaker
**Question:** A payment API dependency keeps failing. Which pattern makes callers fail fast instead of waiting for it, then probes for recovery?
**Options:** A. Bulkhead<br>B. Circuit breaker<br>C. Timeout<br>D. Retry
**Answer:** B (2) – Circuit breaker
**Explanation:** Circuit breaker monitors calls to a dependency and, after a failure threshold, 'opens' — callers fail fast instead of waiting on a dead service, typically returning a FALLBACK response (stale/cached data, default value) so the app keeps working while the dependency recovers. After a cool-down it 'half-opens' to probe recovery. It's about STOPPING traffic to a failing dependency, not partitioning resources (that's bulkhead) or retrying (that's retry's job — dangerous combined with a breaker since retries amplify load).
**Sources:** <a href="https://microservices.io/patterns/reliability/circuit-breaker.html" target="_blank">microservices.io - Circuit Breaker</a>
**Tags:** k8s::kcna src::session topic::architecture topic::resiliency

---

<!-- note:1794078127998 model:Cloze -->
**Text:** Resiliency pattern family — purpose of each:<br><br>{{c1::Retry}} — re-attempt a failed call (transient errors)<br>{{c2::Timeout}} — cap how long a caller waits<br>{{c3::Circuit breaker}} — stop calling a failing dependency, probe for recovery<br>{{c4::Bulkhead}} — isolate resources so one component's failure can't cascade
**Back Extra:** Full mapping: Retry = re-attempt transient failures (watch for retry storms amplifying load); Timeout = cap caller wait (frees threads but doesn't isolate); Circuit breaker = fail-fast + probe recovery on a failing dependency; Bulkhead = partition resources so one failure can't cascade. In Kubernetes these are app-level patterns — the platform gives you probes/replicas, but the code implements the patterns.
**Tags:** k8s::kcna src::session topic::architecture topic::resiliency

---

<!-- note:1794080037340 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which Kubernetes control plane component is responsible for persisting the cluster’s desired state and configuration?
**Options:** A. kube-scheduler<br>B. kube-apiserver<br>C. etcd<br>D. kubelet<br>E. controller-manager
**Answer:** C – etcd
**Explanation:** etcd is a distributed key-value store that reliably stores<br>all Kubernetes cluster data, serving as the single source of truth for the<br>cluster’s state.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037341 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** A developer needs to expose a web application running in a set of Pods within the cluster using a stable internal IP address. Which Kubernetes resource <b>is most</b> appropriate?
**Options:** A. Ingress<br>B. NodePort Service<br>C. ClusterIP Service<br>D. ExternalName Service<br>E. ReplicaSet
**Answer:** C – ClusterIP Service
**Explanation:** A ClusterIP Service provides a stable internal IP address<br>and DNS name for accessing Pods, only reachable from within the cluster.<br>NodePort exposes on nodes, Ingress is for external HTTP/S.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037342 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is <b>the primary purpose</b> of the Kubernetes API server in the control plane architecture?
**Options:** A. To run containerized applications directly<br>B. To schedule Pods onto available worker nodes<br>C. To validate and process REST requests for API objects<br>D. To manage network traffic between Pods<br>E. To store cluster state in a time-series database
**Answer:** C – To validate and process REST requests for API objects
**Explanation:** The kube-apiserver is the frontend of the control plane,<br>exposing the Kubernetes API. It processes and validates API requests,<br>and updates the corresponding objects in etcd.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037343 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** When a Pod is scheduled, what is <b>the primary factor</b> the kubescheduler considers from the Pod’s specification?
**Options:** A. Container image version<br>B. restartPolicy<br>C. Resource requests and limits<br>D. serviceAccountName<br>E. labels
**Answer:** C – Resource requests and limits
**Explanation:** The kube-scheduler filters nodes based on whether they<br>can satisfy the Pod’s resource requests (CPU, memory) and then ranks<br>them based on various priority functions.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037344 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which component is NOT part of the Kubernetes control plane?
**Options:** A. kube-apiserver<br>B. etcd<br>C. kube-scheduler<br>D. kube-proxy<br>E. kube-controller-manager
**Answer:** D – kube-proxy
**Explanation:** kube-proxy runs on every node in the cluster and is responsible for maintaining network rules on nodes, enabling network communication to Pods from network sessions inside or outside of the cluster.<br>It’s a node component, not control plane.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037345 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is the main advantage of using a declarative approach (e.g., YAML manifests) to manage Kubernetes resources?
**Options:** A. It allows for more complex scripting logic<br>B. It enables direct manipulation of etcd data<br>C. It focuses on what desired state, not how to achieve it<br>D. It provides faster API response times<br>E. It simplifies single-container Pod deployments only
**Answer:** C – It focuses on what desired state, not how to achieve it
**Explanation:** Declarative configurations define the desired state, and<br>Kubernetes controllers work to reconcile the current state to this desired<br>state. This is more robust and idempotent than imperative commands.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037346 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** In Kubernetes, what is the <b>primary role</b> of Role-Based Access Control (RBAC)?
**Options:** A. To define network traffic flow between Pods<br>B. To manage secure storage of sensitive data like passwords<br>C. To control user and service account access to API resources<br>D. To assign static IP addresses to Services<br>E. To encrypt container images at rest
**Answer:** C – To control user and service account access to API resources
**Explanation:** RBAC regulates access to Kubernetes API resources based<br>on the roles of individual users or service accounts within the cluster,<br>ensuring users only perform actions they are authorized for.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037347 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is the function of a NetworkPolicy in Kubernetes?
**Options:** A. To provide a stable DNS name for a set of Pods<br>B. To manage external access to services via HTTP/S routing<br>C. To define how Pods are allowed to communicate with each other<br>D. To assign IP addresses to newly created Pods<br>E. To encrypt traffic between services in a mesh
**Answer:** C – To define how Pods are allowed to communicate with each other
**Explanation:** NetworkPolicy resources specify how groups of Pods are<br>allowed to communicate with each other and other network endpoints,<br>acting as a firewall at the Pod level.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037348 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which security mechanism in Kubernetes is best suited for providing an identity to processes running in Pods to interact with the API server?
**Options:** A. NetworkPolicy<br>B. SecurityContext<br>C. ServiceAccount<br>D. PodSecurityPolicy (deprecated) / PodSecurityAdmission<br>E. TLS Certificates for etcd
**Answer:** C – ServiceAccount
**Explanation:** ServiceAccounts provide an identity for processes that run<br>in a Pod, which can then be granted permissions to API resources via<br>RBAC Roles and RoleBindings.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037349 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is <b>the primary goal</b> of Horizontal Pod Autoscaling (HPA) in Kubernetes?
**Options:** A. To increase the resource limits of existing Pods<br>B. To adjust the number of Pod replicas based on metrics<br>C. To add or remove Nodes from the cluster<br>D. To automatically update container images<br>E. To manage storage capacity for stateful sets
**Answer:** B – To adjust the number of Pod replicas based on metrics
**Explanation:** HPA automatically scales the number of Pod replicas in<br>a workload resource (like a Deployment or StatefulSet) up or down based<br>on observed CPU utilization, custom metrics, or external metrics.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037350 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What does a ReplicaSet ensure in Kubernetes?
**Options:** A. That a Pod runs on every node<br>B. That a certain number of Pod replicas are running<br>C. That Pods have stable network identifiers<br>D. That external traffic can reach the Pods<br>E. That Pods are scheduled according to affinity rules
**Answer:** B – That a certain number of Pod replicas are running
**Explanation:** A ReplicaSet’s primary purpose is to maintain a stable set<br>of replica Pods running at any given time, ensuring the desired number of<br>instances of an application are available. Deployments manage ReplicaSets.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037351 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is the main purpose of a ServiceAccount in Kubernetes when interacting with the API server?
**Options:** A. To define network access policies for Pods<br>B. To provide an identity for Pods to authenticate to the API<br>C. To store sensitive credentials for applications<br>D. To group users for applying permissions<br>E. To manage DNS records for services
**Answer:** B – To provide an identity for Pods to authenticate to the API
**Explanation:** ServiceAccounts provide an identity for processes running<br>within Pods. This identity can be used to authenticate to the Kubernetes<br>API server, and RBAC rules can grant it specific permissions.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037352 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** If you need to run a batch job that completes and then terminates, which Kubernetes workload resource is most suitable?
**Options:** A. Deployment<br>B. StatefulSet<br>C. DaemonSet<br>D. Job<br>E. Service
**Answer:** D – Job
**Explanation:** Explanation: A Job creates one or more Pods and ensures that a specified number of them successfully terminate. It’s ideal for batch tasks,<br>while CronJob is for scheduled Jobs.<br><br>Domain: Kubernetes Fundamentals<br><br>Competency: Kubernetes Resources
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037353 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is a key difference between kubectl apply -f and kubectl create -f ?
**Options:** A. apply is declarative, create is imperative<br>B. create can update existing resources, apply cannot<br>C. apply ignores existing resources, create fails if they exist<br>D. apply stores last-applied-configuration, create does not<br>E. create is idempotent, apply is not
**Answer:** D – apply stores last-applied-configuration, create does not
**Explanation:** kubectl apply records the applied configuration in an annotation on the resource. This allows it to calculate a patch between the<br>previous, current, and new desired state, making it suitable for declarative<br>updates. create will fail if the resource exists.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037354 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is <b>the primary function</b> of kube-proxy when a Service of type ClusterIP is created?
**Options:** A. It assigns an IP address from the cluster’s Pod CIDR.<br>B. It modifies iptables or IPVS rules on nodes to route traffic.<br>C. It creates a DNS A record for the Service.<br>D. It terminates TLS connections for the Service.<br>E. It exposes the Service on a port on each Node.
**Answer:** B – It modifies iptables or IPVS rules on nodes to route traffic.
**Explanation:** kube-proxy watches the API server for new Services and<br>Endpoints. For ClusterIP Services, it configures network rules (e.g., iptables, IPVS) on each node to capture traffic destined for the Service’s IP<br>and load balance it to the backend Pods.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037355 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What core benefit does a StatefulSet provide over a Deployment for applications like databases?
**Options:** A. Automatic rolling updates by default<br>B. Simpler YAML configuration for Pod templates<br>C. Stable, unique network identifiers and persistent storage<br>D. Support for hostNetwork: true<br>E. Higher number of allowed replicas
**Answer:** C – Stable, unique network identifiers and persistent storage
**Explanation:** StatefulSets are designed for stateful applications, providing stable, persistent identifiers (e.g., my-app-0, my-app-1) and perinstance persistent storage that follows the Pod identity.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037356 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is <b>the primary role </b>of the ”Controller Manager” in Kubernetes?
**Options:** A. Manages user authentication and authorization<br>B. Exposes the Kubernetes API to external clients<br>C. Runs various controllers that regulate cluster state<br>D. Schedules Pods onto appropriate Nodes<br>E. Stores all cluster configuration data
**Answer:** C – Runs various controllers that regulate cluster state
**Explanation:** The kube-controller-manager runs multiple controller processes (e.g., Node controller, Replication controller, Endpoints controller)<br>that watch for changes and work to drive the actual cluster state towards<br>the desired state.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037357 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What Kubernetes feature allows you to define constraints on which Nodes your Pods can run, based on Node labels?
**Options:** A. NetworkPolicy<br>B. ResourceQuota<br>C. nodeSelector / nodeAffinity<br>D. PodDisruptionBudget<br>E. LimitRange
**Answer:** C – nodeSelector / nodeAffinity
**Explanation:** nodeSelector provides a simple way to constrain Pods to<br>Nodes with specific labels. nodeAffinity offers more expressive rules, including ”preferred” and ”required” constraints.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037358 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is the role of an "Ingress Controller" in a Kubernetes cluster?
**Options:** A. It assigns IP addresses to Pods.<br>B. It manages storage volumes for stateful applications.<br>C. It implements the rules defined in Ingress resources.<br>D. It monitors the health of Nodes in the cluster.<br>E. It encrypts communication between control plane components.
**Answer:** C – It implements the rules defined in Ingress resources.
**Explanation:** An Ingress resource defines HTTP/S routing rules, but an<br>Ingress Controller (e.g., Nginx, Traefik) is the actual reverse proxy/load<br>balancer that reads these rules and routes external traffic accordingly.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037359 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is the core difference between ”authentication” and ”authorization” in Kubernetes security?
**Options:** A. Authentication is for users, authorization for service accounts.<br>B. Authentication verifies identity, authorization verifies permissions.<br>C. Authorization happens before authentication in the API request flow.<br>D. Authentication uses Roles, authorization uses RoleBindings.<br>E. Authorization uses client certificates, authentication uses tokens.
**Answer:** B – Authentication verifies identity, authorization verifies permissions.
**Explanation:** Authentication is the process of determining who a user<br>or service is. Authorization is the process of determining what an authenticated user or service is allowed to do (i.e., which API resources they can<br>access and what actions they can perform).
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037360 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** How can you securely store sensitive information like <b>passwords</b> or <b>API keys</b> in Kubernetes?
**Options:** A. ConfigMap<br>B. Annotation<br>C. Label<br>D. Secret<br>E. nan
**Answer:** D – Secret
**Explanation:** Secrets are Kubernetes objects specifically designed to hold small amounts of sensitive data.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037361 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which Kubernetes component is responsible for watching for newly created Pods and assigning them to Nodes?
**Options:** A. kube-apiserver<br>B. etcd<br>C. kube-scheduler<br>D. kubelet
**Answer:** C – kube-scheduler
**Explanation:** The kube-scheduler is the control plane component that decides which Node a Pod should run on based on constraints and availability.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037363 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which component acts as the central control plane and exposes the Kubernetes API?
**Options:** A. kube-proxy<br>B. kube-apiserver<br>C. etcd<br>D. controller-manager
**Answer:** B – kube-apiserver
**Explanation:** The kube-apiserver validates and configures data for API objects (Pods, Services, etc.) and is the frontend for the control plane.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037364 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is <b>the primary role </b>of etcd in a Kubernetes cluster?
**Options:** A. Running application containers<br>B. Scheduling workloads<br>C. Storing the cluster state<br>D. Managing network policies
**Answer:** C – Storing the cluster state
**Explanation:** etcd is a consistent and highly-available key-value store used as Kubernetes’ backing store for all cluster data.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037365 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which Kubernetes resource is typically used to manage stateless applications by ensuring a specified number of Pod replicas are running?
**Options:** A. StatefulSet<br>B. DaemonSet<br>C. Deployment<br>D. Job
**Answer:** C – Deployment
**Explanation:** Deployments manage ReplicaSets, providing declarative updates and scaling for stateless applications.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037366 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** In Kubernetes, what is the process of assigning Pods to Nodes called?
**Options:** A. Replication<br>B. Orchestration<br>C. Scheduling<br>D. Deployment
**Answer:** C – Scheduling
**Explanation:** Scheduling is the core function of the kube-scheduler, selecting appropriate Nodes for Pods based on resource requests and other factors.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037367 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What Kubernetes object provides a stable IP address and DNS name for accessing a set of Pods?
**Options:** A. Ingress<br>B. Service<br>C. EndpointSlice<br>D. NetworkPolicy
**Answer:** B – Service
**Explanation:** A Service defines a logical set of Pods and a policy by which to access them, providing load balancing and service discovery.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037368 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** How can you securely store sensitive information like passwords or API keys in Kubernetes?
**Options:** A. ConfigMap<br>B. Annotation<br>C. Label<br>D. Secret
**Answer:** D – Secret
**Explanation:** Secrets are Kubernetes objects specifically designed to hold small amounts of sensitive data.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037369 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which Kubernetes object defines rules about how Pods are allowed to communicate with each other and network endpoints?
**Options:** A. Service<br>B. Ingress<br>C. NetworkPolicy<br>D. SecurityContext
**Answer:** C – NetworkPolicy
**Explanation:** NetworkPolicies allow specifying traffic flow rules at the IP address or port level (OSI layer 3 or 4).
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037370 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is <b>the primary goa</b>l of the Cluster Autoscaler?
**Options:** A. Scale Pod replicas<br>B. Scale cluster Nodes<br>C. Scale Persistent Volumes<br>D. Scale Service endpoints
**Answer:** B – Scale cluster Nodes
**Explanation:** The Cluster Autoscaler adjusts the number of Nodes in the cluster based on pending Pods that cannot be scheduled due to resource limits.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037371 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** In Kubernetes RBAC (Role-Based Access Control), what defines a set of permissions?
**Options:** A. Role / ClusterRole<br>B. ServiceAccount<br>C. RoleBinding / ClusterRoleBinding<br>D. User
**Answer:** A – Role / ClusterRole
**Explanation:** Explanation: A Role (namespace-scoped) or ClusterRole (cluster-scoped) contains rules that represent a set of permissions on resources.<br><br>Domain: Container Orchestration<br><br>Competency: Security
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037372 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What object binds a Role or ClusterRole to a user, group, or ServiceAccount?
**Options:** A. Secret<br>B. ConfigMap<br>C. NetworkPolicy<br>D. RoleBinding / ClusterRoleBinding
**Answer:** D – RoleBinding / ClusterRoleBinding
**Explanation:** A RoleBinding (namespace-scoped) or ClusterRoleBinding (cluster-scoped) grants the permissions defined in a Role/ClusterRole to subjects.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037373 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** If you need a Pod to run on every single Node in the cluster (or a subset), which controller is most suitable?
**Options:** A. Deployment<br>B. StatefulSet<br>C. DaemonSet<br>D. Job
**Answer:** C – DaemonSet
**Explanation:** DaemonSets ensure that all (or some) Nodes run a copy of a Pod, useful for cluster services like log collectors or node monitors.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037374 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is a primary difference between a Deployment and a StatefulSet?
**Options:** A. StatefulSets manage Pods<br>B. Deployments are for databases<br>C. StatefulSets provide stable IDs<br>D. Deployments use PVs
**Answer:** C – StatefulSets provide stable IDs
**Explanation:** StatefulSets provide guarantees about the ordering and uniqueness of Pods, including stable network identifiers and persistent storage.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037375 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which Kubernetes API object is used to manage external access to services in a cluster, typically HTTP/S?
**Options:** A. Service (LoadBalancer type)<br>B. NodePort Service<br>C. Ingress<br>D. ExternalName Service
**Answer:** C – Ingress
**Explanation:** Ingress provides HTTP/S routing rules to manage external users’ access to services within the cluster based on hostnames or paths.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037376 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What design pattern involves running an additional container within a Pod to provide auxiliary functions (like logging or monitoring) to the main application container?
**Options:** A. Init Container<br>B. Sidecar Container<br>C. Ephemeral Container<br>D. Job Container
**Answer:** B – Sidecar Container
**Explanation:** The Sidecar pattern adds helper containers alongside the main application container within the same Pod network/storage namespace.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037377 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What <b>fundamental concept</b> allows Kubernetes to maintain the desired state declared by the user?
**Options:** A. Imperative Commands<br>B. Control Loop / Reconciliation<br>C. Manual Scaling<br>D. Direct Node Access
**Answer:** B – Control Loop / Reconciliation
**Explanation:** Kubernetes controllers operate on control loops, constantly comparing the desired state (from API objects) with the actual cluster state.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037378 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which architectural component ensures that the actual state of cluster resources converges towards the desired state defined in their specifications?
**Options:** A. kube-apiserver<br>B. kube-scheduler<br>C. Controllers (within kube-controller-manager)<br>D. kubelet<br>E. etcd
**Answer:** C – Controllers (within kube-controller-manager)
**Explanation:** Controllers implement reconciliation loops. They watch the desired state via the API server and interact with resources to make the current state match the desired state (e.g., ReplicaSet controller ensuring the right number of Pods exist).
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037379 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** A Pod specification includes two containers: one web server and one log shipper. How do these containers communicate efficiently over the network within the Pod?
**Options:** A. Via a Kubernetes Service<br>B. Via the node’s primary IP address<br>C. Via localhost and shared network namespace<br>D. Via an automatically created NetworkPolicy<br>E. Via distinct Pod IP addresses assigned to each container
**Answer:** C – Via localhost and shared network namespace
**Explanation:** Containers within the same Pod share the same network namespace, meaning they can communicate using localhost and standard inter-process communication mechanisms as if they were on the same machine.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037380 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is <b>the primary role</b> of kubelet on a worker node?
**Options:** A. To schedule Pods onto the node<br>B. To store the state of Pods running on the node<br>C. To ensure containers described in PodSpecs assigned to its node are running<br>D. To manage network routing rules for Services<br>E. To authenticate API requests originating from the node
**Answer:** C – To ensure containers described in PodSpecs assigned to its node are running
**Explanation:** The kubelet is the primary node agent. It receives Pod-Specs from the API server and interacts with the container runtime (e.g., containerd) to start, stop, and manage the containers defined in those Pods, reporting their status back to the control plane.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037381 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which Kubernetes resource provides a mechanism for grouping API objects and providing a scope for names?
**Options:** A. Label<br>B. Annotation<br>C. Namespace<br>D. Deployment<br>E. ServiceAccount
**Answer:** C – Namespace
**Explanation:** Namespaces create logical partitions within a cluster, allowing teams or applications to operate independently. Resource names must be unique within a Namespace, but not necessarily across the entire cluster.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037382 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** When interacting with the Kubernetes API server using kubectl, what is the typical format used for defining resource manifests?
**Options:** A. JSON<br>B. XML<br>C. YAML<br>D. Protocol Buffers<br>E. Plain Text
**Answer:** C – YAML
**Explanation:** While the API server can accept JSON, YAML is the overwhelmingly conventional and human-readable format used in configuration files (manifests) passed to kubectl for creating or updating resources.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037383 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What core Kubernetes concept allows Deployments to perform rolling updates with zero downtime?
**Options:** A. Managing StatefulSets<br>B. Utilizing PersistentVolumes<br>C. Incrementally replacing Pods managed by ReplicaSets<br>D. Direct communication with the kube-scheduler<br>E. Modifying NetworkPolicy rules dynamically
**Answer:** C – Incrementally replacing Pods managed by ReplicaSets
**Explanation:** Deployments manage ReplicaSets. During a rolling update, a Deployment creates a new ReplicaSet with the updated Pod template and gradually scales it up while scaling down the old ReplicaSet, ensuring service availability throughout the process.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037384 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which component is responsible for making the ultimate decision about which node a newly created Pod should run on?
**Options:** A. kubelet<br>B. kube-apiserver<br>C. kube-scheduler<br>D. kube-controller-manager<br>E. The Pod’s ServiceAccount
**Answer:** C – kube-scheduler
**Explanation:** The kube-scheduler watches for Pods without an assigned node and selects the most suitable node based on filtering (resource requests, affinity rules, etc.) and scoring algorithms.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037385 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** How does Kubernetes typically handle the failure of a container within a Pod?
**Options:** A. By deleting the entire Pod immediately<br>B. By restarting the failed container based on the Pod’s restartPolicy<br>C. By scheduling a new Pod on a different node<br>D. By marking the Node as unschedulable<br>E. By alerting the kube-scheduler to find a replacement container
**Answer:** B – By restarting the failed container based on the Pod’s restartPolicy
**Explanation:** The kubelet monitors container health. If a container fails, the kubelet restarts it according to the Pod’s restartPolicy (Always, OnFailure, Never). The Pod itself continues to exist on the same node.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037386 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What distinguishes a Kubernetes Secret from a ConfigMap?
**Options:** A. Secrets are namespaced, ConfigMaps are not<br>B. ConfigMaps store configuration data, Secrets store sensitive data (base64 encoded)<br>C. Secrets can only be mounted as environment variables, ConfigMaps as files<br>D. ConfigMaps are automatically encrypted at rest, Secrets are not<br>E. Secrets are immutable once created, ConfigMaps are mutable
**Answer:** B – ConfigMaps store configuration data, Secrets store sensitive data (base64 encoded)
**Explanation:** Both are used for configuration, but Secrets are intended for sensitive information (passwords, keys) and are stored base64 encoded (not truly encrypted by default in etcd, though). ConfigMaps are for nonsensitive configuration data. Both are namespaced and can be mounted in multiple ways.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037387 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which of the following is NOT a standard component of the Kubernetes control plane?
**Options:** A. etcd<br>B. kube-apiserver<br>C. kube-scheduler<br>D. containerd<br>E. kube-controller-manager
**Answer:** D – containerd
**Explanation:** containerd is a container runtime; it typically runs on worker nodes (managed by the kubelet) to handle container execution, not as part of the central control plane.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037388 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is the purpose of labels in Kubernetes?
**Options:** A. To provide detailed descriptive information about a resource<br>B. To define network access rules between resources<br>C. To attach identifying metadata for selection and organization<br>D. To specify resource requests and limits for containers<br>E. To store multi-line configuration data
**Answer:** C – To attach identifying metadata for selection and organization
**Explanation:** Labels are key/value pairs attached to objects (like Pods, Services) used to organize resources and allow users/controllers to select subsets of objects (e.g., a Service selecting Pods with app=backend).
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037389 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** If a Pod needs access to specific hardware features available only on certain nodes, which scheduling mechanism is most suitable?
**Options:** A. ResourceQuota<br>B. NetworkPolicy<br>C. PodDisruptionBudget<br>D. Taints and Tolerations or Node Affinity<br>E. HorizontalPodAutoscaler
**Answer:** D – Taints and Tolerations or Node Affinity
**Explanation:** Taints applied to nodes repel Pods that don’t Tolerate them. Node Affinity allows Pods to express preferences or requirements for nodes based on node labels (which can represent hardware features, location, etc.). Both help ensure Pods land on appropriate nodes.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037390 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which API object represents a single point of access to a set of Pods providing the same functionality, acting as an internal load balancer?
**Options:** A. Ingress<br>B. EndpointSlice<br>C. Service<br>D. ReplicaSet<br>E. NetworkPolicy
**Answer:** C – Service
**Explanation:** A Service defines a logical set of Pods (usually selected by labels) and provides a stable IP address and DNS name. kube-proxy ensures traffic to the Service IP is load-balanced across the healthy backend Pods.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037391 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is the relationship between a Deployment and a ReplicaSet?
**Options:** A. A ReplicaSet manages multiple Deployments<br>B. A Deployment watches ReplicaSets for scaling signals<br>C. A Deployment declaratively manages ReplicaSets to orchestrate Pod updates<br>D. ReplicaSets are used only for stateful applications, Deployments for stateless<br>E. They are independent controllers managing Pod lifecycles
**Answer:** C – A Deployment declaratively manages ReplicaSets to orchestrate Pod updates
**Explanation:** A Deployment provides declarative updates for Pods and ReplicaSets. It creates and manages ReplicaSets, handling rolling updates or rollbacks by manipulating the desired replica count of underlying ReplicaSets. You typically interact with Deployments, not ReplicaSets directly.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037392 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** The Kubernetes API server performs several actions when receiving a request. Which action verifies if the authenticated user is allowed to perform the requested operation?
**Options:** A. Authentication<br>B. Admission Control<br>C. Authorization<br>D. Rate Limiting<br>E. Validation
**Answer:** C – Authorization
**Explanation:** After Authentication (who are you?), Authorization (e.g., via RBAC) checks if the identified user has the necessary permissions (Role/ClusterRole bindings) to perform the action (e.g., create, get, delete) on the specific resource (e.g., pods) in the target namespace.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037393 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is <b>the primary function </b>of etcd within the Kubernetes architecture?
**Options:** A. To run the container runtime interface<br>B. To schedule Pods across available nodes<br>C. To provide reliable, distributed storage for cluster state and configuration<br>D. To manage network policies and ingress rules<br>E. To execute health checks against running containers
**Answer:** C – To provide reliable, distributed storage for cluster state and configuration
**Explanation:** Explanation: etcd is the consistent key-value store that acts as the source of truth for the entire cluster. All configuration, state, and metadata are persisted here, ensuring consistency across the control plane.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037394 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which field in a Pod’s specification is crucial for the kubescheduler to determine if a node has sufficient resources?
**Options:** A. spec.nodeName<br>B. spec.containers[].ports<br>C. spec.containers[].resources.requests<br>D. spec.serviceAccountName<br>E. spec.restartPolicy
**Answer:** C – spec.containers[].resources.requests
**Explanation:** The resources.requests field (for CPU and memory) indicates the minimum amount of resources the container needs. The scheduler uses this to filter out nodes that cannot meet these requests.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037395 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What fundamental concept allows Kubernetes controllers to operate effectively without needing constant instructions?
**Options:** A. Imperative command execution<br>B. The reconciliation loop (Control Loop)<br>C. Direct manipulation of etcd<br>D. Event-driven webhooks<br>E. Stateful session management
**Answer:** B – The reconciliation loop (Control Loop)
**Explanation:** Controllers continuously watch the desired state (from the API server) and the current state (observed in the cluster), taking actions (via the API server) to make the current state match the desired state. This is the core principle of Kubernetes automation.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037396 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** You need to provide non-sensitive configuration data (like a URL endpoint or logging level) to a Pod. Which resource is most appropriate?
**Options:** A. Secret<br>B. ConfigMap<br>C. Annotation<br>D. ResourceQuota<br>E. DownwardAPI
**Answer:** B – ConfigMap
**Explanation:** ConfigMaps are designed specifically for decoupling nonsensitive configuration artifacts from container images, allowing configurations to be managed independently.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037397 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** If you want a specific Pod to run on every node in the cluster (or a subset matching certain criteria), which workload resource should you use?
**Options:** A. Deployment<br>B. StatefulSet<br>C. DaemonSet<br>D. Job<br>E. ReplicaSet
**Answer:** C – DaemonSet
**Explanation:** A DaemonSet ensures that a copy of a Pod runs on all (or some specified) nodes. This is useful for node-level agents like log collectors, monitoring agents, or CNI plugins.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037398 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What does it mean for the Kubernetes API to be ”declarative”?
**Options:** A. API calls must be made sequentially<br>B. Users specify the desired end state, not the steps to reach it<br>C. The API only accepts YAML formatted requests<br>D. API responses always include the full resource specification<br>E. The API can only create resources, not update or delete them
**Answer:** B – Users specify the desired end state, not the steps to reach it
**Explanation:** Users declare the desired state of resources (e.g., ”I want 3 replicas of this Pod”). Kubernetes controllers then figure out the sequence of actions needed to achieve and maintain that state. Contrast this with imperative approaches (”run container X”, ”scale up by 1”).
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037399 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which mechanism prevents the kube-scheduler from placing Pods on a Node that is undergoing maintenance or is otherwise unsuitable?
**Options:** A. ResourceQuotas<br>B. NetworkPolicies<br>C. Taints on the Node and Tolerations on the Pod<br>D. PodDisruptionBudgets<br>E. PriorityClasses
**Answer:** C – Taints on the Node and Tolerations on the Pod
**Explanation:** Explanation: A Taint applied to a Node repels Pods. Pods can express Tolerations for specific taints, allowing them to be scheduled onto those nodes. This is commonly used to cordon nodes for maintenance or dedicate nodes for specific workloads.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037400 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What part of the Kubernetes system is responsible for managing the lifecycle of EndpointSlice objects, which track Pod IPs for Services?
**Options:** A. kube-proxy<br>B. kubelet<br>C. endpointslice-controller (within kube-controller-manager)<br>D. kube-scheduler<br>E. coredns / kube-dns
**Answer:** C – endpointslice-controller (within kube-controller-manager)
**Explanation:** The endpointslice-controller (part of kube-controller-manager) watches Services and their selector-matched Pods, creating and managing EndpointSlices to store the Pod IP addresses and port information efficiently. kube-proxy consumes this information.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037401 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which component translates a Service’s virtual IP address into actual Pod IP addresses on each node?
**Options:** A. etcd<br>B. kube-apiserver<br>C. coredns / kube-dns<br>D. kube-proxy<br>E. kubelet
**Answer:** D – kube-proxy
**Explanation:** kube-proxy, running on each node, watches Services and Endpoints/EndpointSlices. It programs network rules (e.g., iptables, IPVS) to intercept traffic destined for a Service’s ClusterIP and directs it to one of the healthy backend Pod IPs.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037402 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** A <b>StatefulSet </b>is often preferred over a <b>Deployment </b>for running databases. Why?
**Options:** A. StatefulSets have simpler configuration<br>B. Deployments cannot use Persistent Storage<br>C. StatefulSets provide stable, unique network IDs and persistent storage per Pod<br>D. Deployments automatically handle database schema migrations<br>E. StatefulSets require less CPU and memory resources
**Answer:** C – StatefulSets provide stable, unique network IDs and persistent storage per Pod
**Explanation:** StatefulSets provide guarantees crucial for stateful apps: stable network identifiers (e.g., db-0, db-1), stable persistent storage linked to each identity, and ordered, graceful deployment and scaling.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037403 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which kubectl command is used to view the logs of a running container within a Pod?
**Options:** A. kubectl get pod &lt;pod-name&gt; –logs<br>B. kubectl describe pod &lt;pod-name&gt;<br>C. kubectl logs &lt;pod-name&gt; [-c &lt;container-name&gt;]<br>D. kubectl attach &lt;pod-name&gt; -c &lt;container-name&gt;<br>E. kubectl exec &lt;pod-name&gt; – tail /var/log/messages
**Answer:** C – kubectl logs &lt;pod-name&gt; [-c &lt;container-name&gt;]
**Explanation:** kubectl logs fetches the logs (stdout/stderr) from a specified container within a Pod. The -c flag is needed if the Pod has multiple containers.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037404 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is the function of an Admission Controller in the Kubernetes API request lifecycle?
**Options:** A. To authenticate the user making the request<br>B. To authorize the requested operation<br>C. To mutate or validate API objects before they are persisted in etcd<br>D. To schedule the Pod onto a suitable node<br>E. To route network traffic to the correct Pod
**Answer:** C – To mutate or validate API objects before they are persisted in etcd
**Explanation:** Admission Controllers intercept API requests after authentication and authorization but before persistence. They can mutate objects (e.g., inject sidecars, set default values) or validate them (e.g., enforce security policies, check resource quotas).
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037405 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which resource defines constraints on the total amount of compute resources (CPU, memory) that can be consumed within a specific Namespace?
**Options:** A. LimitRange<br>B. ResourceQuota<br>C. NetworkPolicy<br>D. PodSecurityPolicy / PodSecurityAdmission<br>E. PriorityClass
**Answer:** B – ResourceQuota
**Explanation:** A ResourceQuota limits the aggregate resource consumption (CPU, memory, storage, object counts) within a Namespace, preventing overuse and ensuring fair sharing among users or teams.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037406 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Consider a Pod that needs to perform a <b>one-time initialization task</b> before its main application container starts. Which container type is best suited for this?
**Options:** A. Sidecar Container<br>B. Ephemeral Container<br>C. Init Container<br>D. Main Application Container<br>E. Job Container
**Answer:** C – Init Container
**Explanation:** Init Containers run sequentially before the main application containers in a Pod start. They must complete successfully for the main containers to launch, making them ideal for setup tasks like database schema migration, fetching configuration, or waiting for dependencies.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037407 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is the purpose of the metadata.ownerReferences field in a Kubernetes object?
**Options:** A. To specify the user who created the object<br>B. To link the object to its managing controller (e.g., ReplicaSet to Deployment)<br>C. To list labels used for selecting the object<br>D. To store annotations related to the object’s owner<br>E. To define the Namespace the object belongs to
**Answer:** B – To link the object to its managing controller (e.g., ReplicaSet to Deployment)
**Explanation:** ownerReferences create parent-child relationships between objects. This enables cascading deletion (deleting the owner deletes dependents) and helps controllers identify the objects they manage. For example, a ReplicaSet Pod will have an ownerReference pointing to the ReplicaSet.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037408 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which control plane component is primarily responsible for running controllers like the Node Controller, Deployment Controller, and Service Controller?
**Options:** A. etcd<br>B. kube-apiserver<br>C. kube-scheduler<br>D. kube-controller-manager<br>E. cloud-controller-manager
**Answer:** D – kube-controller-manager
**Explanation:** The kube-controller-manager bundles core Kubernetes controllers into a single binary. It runs controllers that handle node lifecycle, workload management (Deployments, ReplicaSets), service endpoints, namespace creation, etc.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037409 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is the purpose of a LimitRange object within a Namespace?
**Options:** A. To limit the total resource usage of the entire Namespace<br>B. To set default resource requests/limits for containers and validate min/max bounds<br>C. To restrict network traffic between Pods in the Namespace<br>D. To control which users can create resources in the Namespace<br>E. To define storage quotas for PersistentVolumeClaims
**Answer:** B – To set default resource requests/limits for containers and validate min/max bounds
**Explanation:** A LimitRange operates at the container/Pod level within a Namespace. It can enforce minimum/maximum resource constraints and specify default request/limit values if they aren’t explicitly set in the Pod spec. ResourceQuota limits the Namespace total.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037410 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which kubectl command would you use to apply a configuration defined in my-app.yaml declaratively?
**Options:** A. kubectl create -f my-app.yaml<br>B. kubectl replace -f my-app.yaml<br>C. kubectl apply -f my-app.yaml<br>D. kubectl patch -f my-app.yaml<br>E. kubectl run -f my-app.yaml
**Answer:** C – kubectl apply -f my-app.yaml
**Explanation:** kubectl apply is the standard command for declarative resource management. It creates resources if they don’t exist or calculates and applies necessary changes if they do, based on the definition in the file.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037411 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** How does the kube-scheduler handle Pods with defined affinity rules?
**Options:** A. It ignores affinity rules if resource requests cannot be met.<br>B. It uses affinity rules as the primary factor for node selection.<br>C. It considers affinity/anti-affinity rules during the filtering and scoring phases.<br>D. It delegates affinity processing to the kubelet.<br>E. It only processes podAffinity, not nodeAffinity.
**Answer:** C – It considers affinity/anti-affinity rules during the filtering and scoring phases.
**Explanation:** Affinity rules (node and inter-pod) influence scheduling decisions. Required affinity rules act as filters (nodes must match). Preferred affinity rules contribute to the scoring phase (nodes matching preferred rules get higher scores).
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037412 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which of the following is a built-in Kubernetes resource for scheduling pods on nodes?
**Options:** A. Deployment<br>B. Ingress<br>C. Service<br>D. DaemonSet
**Answer:** D – DaemonSet
**Explanation:** A DaemonSet ensures that a copy of a Pod runs on all (or selected) nodes in the cluster, commonly used for system-level workloads like logging or monitoring agents.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037413 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What Kubernetes resource is used to expose an application running on a set of pods as a network service
**Options:** A. ReplicaSet<br>B. Job<br>C. Service<br>D. CronJob
**Answer:** C – Service
**Explanation:** A Service provides a stable network endpoint and load-balancing for accessing a group of Pods.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037414 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is the primary component of a Kubernetes control plane that manages API requests?
**Options:** A. Kube-scheduler<br>B. Kube-controller-manager<br>C. Etcd<br>D. Kube-apiserver
**Answer:** D – Kube-apiserver
**Explanation:** The kube-apiserver is the central component that exposes the Kubernetes API and handles all API requests.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037415 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which component of a Kubernetes node <b>is responsible for</b> managing network rules and IP addresses?
**Options:** A. Kubelet<br>B. Kubectl<br>C. Kube-proxy<br>D. Container runtime
**Answer:** C – Kube-proxy
**Explanation:** Kube-proxy manages networking rules and enables service-to-pod communication within the cluster.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037416 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which component of the Kubernetes control plane exposes the RESTful API for managing the cluster?
**Options:** A. kube-scheduler<br>B. kube-controller-manager<br>C. kube-apiserver<br>D. etcd
**Answer:** C – kube-apiserver
**Explanation:** The kube-apiserver exposes the REST API and acts as the primary entry point for all cluster operations.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037417 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is the primary advantage of using containers in application deployment?
**Options:** A. Higher hardware efficiency<br>B. Isolation of applications and dependencies<br>C. Larger application size<br>D. Conversion into virtual machines
**Answer:** B – Isolation of applications and dependencies
**Explanation:** Containers package applications with their dependencies, ensuring isolation and consistency across environments.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037418 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which component determines which nodes can run a pod?
**Options:** A. Kubelet<br>B. Kube-scheduler<br>C. Pod controller<br>D. Node selector
**Answer:** B – Kube-scheduler
**Explanation:** The kube-scheduler selects the most suitable node for a Pod based on scheduling policies and constraints.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037419 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What role does a node’s taint play in scheduling?
**Options:** A. Allows pods with matching tolerations<br>B. Prevents all pods from running<br>C. Improves node performance<br>D. Limits pod resources
**Answer:** A – Allows pods with matching tolerations
**Explanation:** Taints repel Pods unless they have matching tolerations, controlling which Pods can be scheduled on a node.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037420 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which component maintains the desired state of applications?
**Options:** A. Controller Manager<br>B. Kubelet<br>C. Etcd<br>D. Docker Daemon
**Answer:** A – Controller Manager
**Explanation:** Controllers continuously reconcile the desired state with the actual cluster state.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037421 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is the purpose of Pod Security Policies?
**Options:** A. Network traffic control<br>B. Enforce pod execution rules<br>C. Auto-scale pods<br>D. Manage storage
**Answer:** B – Enforce pod execution rules
**Explanation:** Pod Security Policies define security constraints for pod execution (deprecated but relevant conceptually).
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037422 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which resource exposes services to external traffic?
**Options:** A. DaemonSet<br>B. ConfigMap<br>C. Ingress<br>D. PersistentVolume
**Answer:** C – Ingress
**Explanation:** Ingress manages external HTTP/HTTPS access to services.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037423 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is the purpose of HPA?
**Options:** A. Scale nodes<br>B. Scale pods<br>C. Upgrade API server<br>D. Provide storage
**Answer:** B – Scale pods
**Explanation:** HPA automatically adjusts the number of Pods based on metrics like CPU usage.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---

<!-- note:1794080037425 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is the concept of "desired state reconciliation" fundamental to Kubernetes?
**Options:** A. Users manually reconcile cluster state using kubectl.<br>B. Controllers continuously observe and work to match actual state to declared state.<br>C. etcd automatically corrects discrepancies between desired and actual state.<br>D. kubelet reconciles container state based solely on node health.<br>E. The API server rejects any configuration that deviates from the current state.
**Answer:** B – Controllers continuously observe and work to match actual state to declared state.
**Explanation:** Controllers continuously observe the actual state of the cluster and take action to make it match the declared/desired state. This reconciliation loop is the core of Kubernetes: controllers (deployment, replicaset, etc.) watch the API server and correct drift automatically.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---
<!-- note:1794080455329 model:Many -->
**Domain:** Services - troubleshooting
**Question:** A user reports that a web application is not accessible via its Service. The Service is of type ClusterIP. Which TWO steps should be taken to troubleshoot?
**Options:** A. Verify that the kube-proxy is running on the node<br>B. Check that the container runtime is working<br>C. Check the kube-apiserver status<br>D. Check if the Service has any endpoints using 'kubectl get endpoints'<br>E. Restart all nodes in the cluster
**Answer:** A, D – verify kube-proxy is running on the node AND check the Service has endpoints via kubectl get endpoints
**Explanation:** (Select TWO) ClusterIP traffic flows: client -> ClusterIP -> kube-proxy iptables/IPVS rules -> ready Pod IPs. Two failure points to check first: (A) kube-proxy down on the node = no DNAT rules programmed, ClusterIP goes nowhere; (D) empty endpoints = the Service selector matches no READY pods — the most common cause (pods crashed, labels changed, readiness failing). Distractors: container runtime failure breaks pods broadly, not Service-specific; kube-apiserver down breaks kubectl itself; restarting all nodes is disruptive non-diagnostic.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/service/" target="_blank">Kubernetes Docs - Service</a>
**Tags:** k8s::kcna topic::services topic::endpoints src::session

---

<!-- note:1794080455330 model:Many -->
**Domain:** Services - endpoints empty
**Question:** kubectl get endpoints <service-name> shows no addresses for a ClusterIP Service. What is the most likely cause?
**Options:** A. The selector matches no ready pods — Endpoints only lists pods that are Running AND Ready<br>B. The ClusterIP was never allocated by the apiserver<br>C. kube-proxy hasn't synced yet — wait 24 hours<br>D. Endpoints only populate for NodePort services
**Answer:** A (1) – The selector matches no ready pods — Endpoints only lists pods that are Running AND Ready
**Explanation:** The Endpoints object is auto-populated by the control plane with the IPs of pods matching the Service's selector that are Ready. Empty endpoints = kube-proxy has nothing to DNAT to, so the ClusterIP accepts nothing. Causes: selector/label mismatch, pods CrashLoopBackOff, readiness probe failing, or pods in wrong namespace. Inspect with 'kubectl get endpoints <svc>' or 'kubectl describe svc <svc>' (shows Endpoints: field). Note: modern clusters use EndpointSlices internally, but 'kubectl get endpoints' still works.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/service/" target="_blank">Kubernetes Docs - Service</a>
**Tags:** k8s::kcna topic::services topic::endpoints src::session

---

<!-- note:1794081107268 model:Many -->
**Domain:** Labels Selectors - quiz
**Question:** Which THREE statements about Labels and Selectors are correct?
**Options:** A. Services use selectors to determine which Pods receive traffic<br>B. Selectors are used by Deployments to identify the Pods they manage<br>C. Labels can be used to organize and select subsets of objects<br>D. Labels must be unique within a namespace<br>E. Annotations are used for identification and selection
**Answer:** A, B, C – Services select pods for traffic, Deployments select pods they manage, labels organize/select subsets
**Explanation:** (Select THREE) Labels are arbitrary key/value metadata on objects; SELECTORS are the query mechanism that consumes them. True statements: (A) Service spec.selector matches pod labels → those pods receive traffic; (B) Deployment/ReplicaSet spec.selector.matchLabels determines which pods it OWNS and manages (adoption, not just traffic); (C) labels group objects and enable subset selection via equality- or set-based selectors. Distractors: (D) labels need NOT be unique in a namespace — many objects share labels, that's the point of grouping; (E) annotations are non-identifying metadata and CANNOT be used by selectors — only labels are queryable.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/" target="_blank">Kubernetes Docs - Labels and Selectors</a>
**Tags:** k8s::kcna topic::labels topic::selectors src::session

---

<!-- note:1794081107269 model:Many -->
**Domain:** Selectors - workload ownership
**Question:** Which field does a Deployment use to determine which Pods it owns and manages?
**Options:** A. spec.template.metadata.labels — the labels it stamps on new pods<br>B. spec.selector.matchLabels — the Deployment's selector determines which pods it owns and manages<br>C. spec.selector — a flat map like a Service uses<br>D. Annotations on the pod template
**Answer:** B (2) – spec.selector.matchLabels — the Deployment's selector determines which pods it owns and manages
**Explanation:** Workload controllers (Deployment, ReplicaSet, StatefulSet, DaemonSet) use spec.selector.matchLabels (or matchExpressions for set-based) to determine which pods they OWN — the controller adopts matching pods and manages their lifecycle. Two traps: spec.template.metadata.labels is where the controller SETS labels on pods it creates (the producer side, not the selector); and the selector is IMMUTABLE after creation — changing it requires recreating the workload. Services use a different field (spec.selector) purely for traffic routing.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/deployment/" target="_blank">Kubernetes Docs - Deployments</a>
**Tags:** k8s::kcna topic::labels topic::selectors topic::deployments src::session

---

<!-- note:1794081509520 model:Many -->
**Domain:** Pod States - CrashLoopBackOff
**Question:** A container in a pod has been restarted multiple times with 'CrashLoopBackOff' state. What does this indicate?
**Options:** A. The container is using too much memory<br>B. The container exits with a non-zero exit code soon after starting<br>C. The container is running but not responding to health checks<br>D. The container image cannot be pulled
**Answer:** B (2) – The container exits with a non-zero exit code soon after starting
**Explanation:** CrashLoopBackOff = the container STARTS, exits non-zero almost immediately, kubelet restarts it, repeat — with exponential backoff between attempts. The process itself is failing (bad command, missing file, crash on startup, failed liveness probe). Distractors map to OTHER states: unpullable image → ImagePullBackOff/ErrImagePull (never starts); running-but-unhealthy → liveness probe restarts (which CAUSES CrashLoopBackOff but the state itself means exit); memory → OOMKilled. Triage: kubectl logs --previous + kubectl describe pod.
**Sources:** <a href="https://kubernetes.io/docs/tasks/debug/debug-application/determine-reason-pod-failure/" target="_blank">Kubernetes Docs - Determine Reason for Pod Failure</a>
**Tags:** k8s::kcna topic::pods topic::troubleshooting src::session

---

<!-- note:1794081509521 model:Many -->
**Domain:** Pod States - backoff
**Question:** What does the 'BackOff' part of CrashLoopBackOff mean?
**Options:** A. Exponential backoff — the kubelet waits progressively longer between restart attempts to avoid hammering a failing container<br>B. The container is backed off from scheduling onto any node<br>C. Kubernetes has given up and will never restart it again<br>D. The container's CPU is throttled to zero
**Answer:** A (1) – Exponential backoff — the kubelet waits progressively longer between restart attempts to avoid hammering a failing container
**Explanation:** The 'BackOff' suffix means the restart delay grows exponentially (10s, 20s, 40s, up to 5min cap) — kubelet won't hot-loop a crash-looping container forever. You see it in events as 'Back-off restarting failed container'. The loop only breaks when the container stays up past the failure window or the pod is fixed/deleted. To debug the ACTUAL cause use 'kubectl logs <pod> --previous' (last crashed instance) — current logs may be empty if it's mid-backoff.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/" target="_blank">Kubernetes Docs - Pod Lifecycle</a>
**Tags:** k8s::kcna topic::pods topic::troubleshooting src::session

---

<!-- note:1794081542009 model:Many -->
**Domain:** Kubectl - logs container
**Question:** You want to view the logs of a container named 'app' inside a pod named 'web-pod-7d4f8'. Which kubectl command should you use?
**Options:** A. kubectl exec web-pod-7d4f8 -c app -- logs<br>B. kubectl log web-pod-7d4f8 --container app<br>C. kubectl logs web-pod-7d4f8 -c app<br>D. kubectl logs web-pod-7d4f8 app
**Answer:** C (3) – kubectl logs web-pod-7d4f8 -c app
**Explanation:** kubectl logs is the verb (always plural — 'log' doesn't exist); the pod name is positional; -c/--container selects WHICH container when the pod has several (default = first container). Distractors: A uses exec — exec runs a NEW command inside the container, it doesn't fetch logs; B has the nonexistent 'log' verb; D passes 'app' as a second positional arg which kubectl rejects. Related flags worth knowing: --previous (logs of the last crashed instance — the CrashLoopBackOff debugging tool), -f/--follow, --tail=N, --since.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/generated/kubectl_logs/" target="_blank">kubectl logs reference</a>
**Tags:** k8s::kcna topic::kubectl topic::logging src::session

---

<!-- note:1794081542018 model:Cloze -->
**Text:** kubectl logs cheatsheet:<br><br>Basic: <code>kubectl logs {{c1::pod-name}}</code><br>Specific container: <code>-c {{c2::container-name}}</code><br>Last crashed instance: <code>--{{c3::previous}}</code><br>Follow live: <code>-{{c4::f}}</code> / <code>--follow</code><br>Last N lines: <code>--tail={{c5::N}}</code>
**Back Extra:** Full family: kubectl logs <pod> [-c container] [--previous] [-f] [--tail=N] [--since=...]. -c needed only for multi-container pods. --previous shows the last terminated instance's logs (crash debugging). --timestamps adds timestamps. kubectl logs -f streams live.
**Tags:** k8s::kcna topic::kubectl topic::logging src::session

---

<!-- note:1794082133043 model:Many -->
**Domain:** Pod Events - timeline read
**Question:** A pod 'my-pod' shows repeated 'BackOff' events after the container starts. Which is the most likely cause?
**Options:** A. The image 'myapp:v2' does not exist<br>B. The container exceeds its memory limit<br>C. The liveness probe is failing<br>D. The application crashes shortly after starting
**Answer:** D (4) – The application crashes shortly after starting
**Explanation:** Read events CHRONOLOGICALLY: Pulling → Pulled → Created → Started all succeeded — the image exists and the container RAN. Then BackOff = it exited and kubelet is delaying restart. So the failure is POST-start: app crash (bad config, missing env, port conflict, liveness probe killing it). Distractors fail the timeline test: missing image would show ErrImagePull/ImagePullBackOff INSTEAD of Started; OOMKilled shows reason OOMKilled + exit 137; liveness failure shows 'Unhealthy' probe events before restart. Rule: Started followed by BackOff = runtime crash, not pull/scheduling problem.
**Sources:** <a href="https://kubernetes.io/docs/tasks/debug/debug-application/determine-reason-pod-failure/" target="_blank">Kubernetes Docs - Determine Reason for Pod Failure</a>
**Tags:** k8s::kcna topic::pods topic::troubleshooting topic::kubectl src::session

---

<!-- note:1794082133044 model:Many -->
**Domain:** Kubectl - events command
**Question:** How do you list Kubernetes events for a specific pod named 'my-pod'?
**Options:** A. kubectl logs my-pod --events<br>B. kubectl get events --field-selector involvedObject.name=my-pod<br>C. kubectl describe events my-pod<br>D. kubectl get pods --show-events my-pod
**Answer:** B (2) – kubectl get events --field-selector involvedObject.name=my-pod — filters cluster events to just that pod
**Explanation:** kubectl get events lists cluster events newest-first (LAST SEEN, TYPE, REASON, OBJECT, MESSAGE). --field-selector involvedObject.name=<name> scopes to one object — essential since busy clusters flood the list. TYPE is Normal (info: Pulled, Started, Scheduled) or Warning (problems: BackOff, Failed, Unhealthy, FailedScheduling). Pair with kubectl describe pod <pod> which shows the same events inline plus pod conditions. For a specific reason: --field-selector reason=BackOff.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/generated/kubectl_get/kubectl_get_events/" target="_blank">kubectl get events reference</a>
**Tags:** k8s::kcna topic::kubectl topic::troubleshooting src::session

---

<!-- note:1794082210325 model:Many -->
**Domain:** Cluster Architecture - kubelet reconcile
**Question:** Which component runs on every worker node and is responsible for ensuring that containers are running in a pod according to the pod specification?
**Options:** A. kube-scheduler<br>B. kubelet<br>C. container runtime<br>D. kube-proxy
**Answer:** B (2) – kubelet
**Explanation:** The kubelet is the node agent that runs a reconcile loop: it watches the API server for pods BOUND to its node, compares desired state (pod spec) vs actual state, and drives the container runtime via CRI to start/stop containers, run probes, and report status. The container runtime is tempting — it does launch the container processes — but it only executes what the kubelet asks; it never reads pod specs itself. kube-scheduler assigns pods (control plane); kube-proxy manages Service network rules, not pod lifecycle.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/components/#kubelet" target="_blank">Kubernetes Docs - kubelet</a>
**Tags:** k8s::kcna topic::architecture topic::kubelet src::session

---

<!-- note:1794082210326 model:Many -->
**Domain:** Cluster Architecture - kubelet duties
**Question:** Which of the following are responsibilities of the kubelet? (Select all that apply)
**Options:** A. Watches for pods assigned to its node and starts/stops their containers<br>B. Runs liveness and readiness probes against containers<br>C. Assigns pods to nodes based on resource availability<br>D. Maintains iptables/IPVS rules for Service traffic<br>E. Registers the node and reports pod/node status to the API server
**Answer:** A, B, E – watches pod specs & drives containers; runs probes; registers node & reports status
**Explanation:** Kubelet duties (select all): (A) watches API server for pods bound to its node and starts/stops containers via the runtime — YES; (B) executes liveness/readiness/startup probes — YES; (E) registers the node and reports pod/node status back — YES. NOT kubelet: (C) pod-to-node assignment is the kube-scheduler (control plane); (D) Service traffic rules are kube-proxy. Division of labor: kubelet decides WHAT should run; container runtime (containerd/CRI-O) does the actual container mechanics via CRI.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/components/#kubelet" target="_blank">Kubernetes Docs - kubelet</a>
**Tags:** k8s::kcna topic::architecture topic::kubelet src::session

---

<!-- note:1794082761997 model:Many -->
**Domain:** Storage - emptyDir lifecycle
**Question:** A developer creates a Pod with a container that writes logs to a file in an emptyDir volume. The Pod is then deleted, and a new Pod is created with the same emptyDir volume definition. What happens to the data in the emptyDir volume?
**Options:** A. The data is preserved because emptyDir volumes persist across Pod deletions<br>B. The data is lost because emptyDir volumes are deleted when the Pod is deleted<br>C. The data is preserved if the emptyDir volume is mounted with a persistentVolumeClaim<br>D. The data is preserved if the new Pod is scheduled to the same node
**Answer:** B (2) – The data is lost because emptyDir volumes are deleted when the Pod is deleted
**Explanation:** emptyDir lifetime = the POD's lifetime, not the node's. Created when the pod is scheduled, deleted when the pod is deleted — a replacement pod gets a FRESH emptyDir even on the same node. It CAN'T be backed by a PVC (that's not how volume types compose — PVC backs a PersistentVolume directly). For data that must survive pod deletion you need PVC→PV, or accept loss. emptyDir's real jobs: scratch space and sharing files BETWEEN CONTAINERS of the same pod.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/volumes/#emptydir" target="_blank">Kubernetes Docs - emptyDir volume</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794082761998 model:Many -->
**Domain:** Storage - emptyDir use case
**Question:** Which scenario is the BEST fit for an emptyDir volume?
**Options:** A. Storing a database that must survive pod restarts<br>B. Persisting user uploads across deployments<br>C. Sharing a scratch/cache directory between an app container and a sidecar in the same pod<br>D. Keeping logs after the pod is deleted for later debugging
**Answer:** C (3) – Sharing a scratch/cache directory between an app container and a sidecar in the same pod
**Explanation:** emptyDir = pod-scoped temporary storage: exists only while THAT pod runs, deleted with it. Perfect for: scratch space, build caches, and sharing files between containers IN THE SAME POD (e.g. app writes to emptyDir, sidecar ships the logs). WRONG for anything surviving pod deletion — pod logs you want to keep, databases, user uploads → PVC/PV. Same-node scheduling doesn't help: the volume is bound to the pod, not the node.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/volumes/#emptydir" target="_blank">Kubernetes Docs - emptyDir volume</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---
<!-- note:1794103862156 model:Many -->
**Domain:** Sidecars - purpose
**Question:** Why was the sidecar container pattern introduced in Kubernetes?
**Options:** A. To run multiple replicas of the same application inside one Pod for higher availability<br>B. To attach supporting functionality — logging, monitoring, proxying — to an application without modifying its code or image<br>C. To give each container in a Pod its own IP address and network namespace<br>D. To replace Kubernetes Services for east-west traffic<br>E. To enforce security isolation between the app and the host kernel
**Answer:** B (2) – To attach supporting functionality — logging, monitoring, proxying — to an application without modifying its code or image
**Explanation:** Sidecars decouple cross-cutting concerns from business logic: the app image stays focused on its function while helper containers (log shipper, metrics agent, service-mesh proxy like Envoy, config/secret syncer) run alongside in the same Pod. Because helpers are separate containers they can be updated, swapped, or written in different languages without rebuilding or redeploying the app — e.g. Istio injects an Envoy sidecar to add mTLS without touching application code. Note what sidecars do NOT provide: each container still shares the Pod's single network namespace (no per-container IP), and the Pod — not the sidecar — is the isolation/security boundary.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/" target="_blank">Kubernetes Docs - Sidecar Containers</a>
**Tags:** k8s::kcna topic::sidecars topic::pods src::session

---

<!-- note:1794103862157 model:Many -->
**Domain:** Sidecars - shared resources
**Question:** Which resources does a sidecar container share with the app container in the same Pod? (Select all that apply)
**Options:** A. Network namespace — same IP address, localhost, and port space<br>B. Process (PID) namespace — the same visible process list<br>C. Pod volumes — can mount the same filesystems to exchange files<br>D. The node's root filesystem<br>E. The app container's writable filesystem layer
**Answer:** A, C – Network namespace and Pod volumes
**Explanation:** Sidecars share the Pod's NETWORK namespace — that is why app and sidecar talk to each other over localhost with no Service or DNS needed. They can also share VOLUMES (e.g. emptyDir) so a log shipper can tail files the app writes. They do NOT share the process namespace (each container has its own PID namespace and cannot see the other's processes), the node's filesystem, or the app container's writable layer — file sharing requires an explicitly mounted Pod volume.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/" target="_blank">Kubernetes Docs - Sidecar Containers</a>
**Tags:** k8s::kcna topic::sidecars topic::pods src::session

---

<!-- note:1794103862158 model:Many -->
**Domain:** Sidecars - vs init containers
**Question:** How does a sidecar container differ from a regular init container?
**Options:** A. Init containers run concurrently with app containers; sidecars run only during Pod startup<br>B. Init containers run to completion before app containers start and cannot send data back; sidecars run for the Pod's whole lifetime, support probes, and communicate bidirectionally over localhost<br>C. Init containers can share Pod volumes; sidecars cannot access volumes at all<br>D. Sidecars are controlled by a separate controller; init containers are controlled by the kubelet
**Answer:** B (2) – Init containers run to completion before app containers start and cannot send data back; sidecars run for the Pod's whole lifetime, support probes, and communicate bidirectionally over localhost
**Explanation:** Regular init containers execute SEQUENTIALLY TO COMPLETION before any app container starts — data flow is one-way (init writes to a volume, app reads it later). A native sidecar is declared as an initContainer with restartPolicy: Always: it starts in init order but KEEPS RUNNING for the Pod's lifetime, supports liveness/readiness probes, and shares the network namespace so it can talk to the app bidirectionally via localhost (e.g. a log shipper tailing a shared file while the app runs).
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/" target="_blank">Kubernetes Docs - Sidecar Containers</a>
**Tags:** k8s::kcna topic::sidecars topic::pods src::session

---

<!-- note:1794103862159 model:Many -->
**Domain:** Sidecars - native declaration
**Question:** How is a native sidecar container declared in a Pod spec?
**Options:** A. Add `sidecar: true` to a regular entry under spec.containers<br>B. List it under spec.initContainers with restartPolicy: Always — it starts before later init and app containers but keeps running for the Pod's lifetime<br>C. Deploy it as a custom resource of kind: Sidecar<br>D. Set restartPolicy: OnFailure on an init container
**Answer:** B (2) – List it under spec.initContainers with restartPolicy: Always — it starts before later init and app containers but keeps running for the Pod's lifetime
**Explanation:** Native sidecars (Kubernetes 1.28+, feature gate enabled by default since 1.29 and locked/always-on since 1.33) are a special case of init containers: restartPolicy: Always under initContainers. The kubelet marks the sidecar 'started' once its process runs, then proceeds through remaining init containers to the app containers — giving startup ORDERING — but unlike regular init containers the sidecar never exits. There is no `sidecar: true` field and no Sidecar CRD in core Kubernetes; before 1.28 the pattern relied on a plain second container in spec.containers with no startup ordering.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/" target="_blank">Kubernetes Docs - Sidecar Containers</a>
**Tags:** k8s::kcna topic::sidecars topic::pods src::session

---

<!-- note:1794103862160 model:Many -->
**Domain:** Sidecars - termination order
**Question:** When a Pod is terminated, how does the kubelet order container shutdown?
**Options:** A. All containers receive SIGTERM simultaneously<br>B. Sidecars are terminated first so the app can drain quickly<br>C. App containers are terminated first; sidecars stop LAST in reverse order of their spec position, so they keep supporting (e.g. flushing logs) until the end<br>D. Init containers are terminated last
**Answer:** C (3) – App containers are terminated first; sidecars stop LAST in reverse order of their spec position, so they keep supporting (e.g. flushing logs) until the end
**Explanation:** On Pod termination the kubelet postpones stopping sidecar containers until the main app containers have fully stopped, then shuts the sidecars down in REVERSE order of their appearance in the Pod spec. This keeps helpers operational while the app winds down — a log shipper can flush remaining entries, a mesh proxy can drain connections — instead of vanishing at the first SIGTERM. Related gotcha: sidecar containers often exit non-zero during termination because they may not get graceful-shutdown time; that is normal and should be ignored by tooling.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/" target="_blank">Kubernetes Docs - Sidecar Containers</a>
**Tags:** k8s::kcna topic::sidecars topic::pods src::session

---

<!-- note:1794103862161 model:Many -->
**Domain:** Sidecars - use cases
**Question:** Which are typical responsibilities of a sidecar container? (Select all that apply)
**Options:** A. Shipping the app's logs to a centralized logging backend (e.g. Fluent Bit)<br>B. Proxying and encrypting service-to-service traffic (e.g. an Istio/Envoy mesh sidecar)<br>C. Syncing secrets or configuration into a shared volume<br>D. Implementing the application's core business logic<br>E. Load-balancing traffic across Pods in the cluster
**Answer:** A, B, C – Log shipping, mesh proxying, and config/secret syncing
**Explanation:** Sidecars provide SUPPORTING services around the app: log collection/forwarding (Fluent Bit), metrics/observability agents, service-mesh proxies (Istio's Envoy sidecar adds mTLS, retries, traffic splitting without app changes), config/secret syncers, and file generators writing into shared volumes. They explicitly do NOT run the app's business logic (that is the app container's job) and do NOT do cluster-level traffic management — that is the Service/Ingress/Gateway layer.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/" target="_blank">Kubernetes Docs - Sidecar Containers</a>
**Tags:** k8s::kcna topic::sidecars topic::pods src::session

---

<!-- note:1794103864955 model:Basic -->
**Front:** When should a helper container be declared as a native sidecar (spec.initContainers + restartPolicy: Always) rather than just added to spec.containers?
**Back:** When you need startup ORDERING plus sidecar lifecycle semantics: a native sidecar is guaranteed to be running before the next init container and before the app containers start — the kubelet proceeds once its 'started' status is true — and it then keeps running for the Pod's whole lifetime with its own restart/probe behavior. A plain second container under spec.containers gets no ordering guarantee: all regular containers start together and none is treated as a prerequisite for the others.
**Tags:** k8s::kcna topic::sidecars topic::pods src::session

---

<!-- note:1794103864961 model:Cloze -->
**Text:** spec:
  initContainers:
    - name: logshipper
      image: fluent/fluent-bit:latest
      restartPolicy: {{c1::Always}}
  containers:
    - name: app
      image: nginx
**Back Extra:** restartPolicy: Always inside initContainers makes this a NATIVE SIDECAR (Kubernetes 1.28+, always-on since 1.33): it launches in init order before the app container but keeps running for the Pod's entire lifetime, and is terminated only after the app containers stop.
**Tags:** k8s::kcna topic::sidecars topic::yaml src::session

---

<!-- note:1794263352986 model:Many -->
**Domain:** Docker Storage - data root
**Question:** On a Linux host, where does the Docker daemon store images, container filesystems, and volumes?
**Options:** A. /var/lib/containers<br>B. /var/lib/docker — Docker's data root holding images, containers, volumes, and storage-driver layers<br>C. ~/.docker/config.json<br>D. /etc/docker/daemon.json
**Answer:** B (2) – /var/lib/docker — Docker's data root holding images, containers, volumes, and storage-driver layers
**Explanation:** /var/lib/docker is Docker's data root on Linux: it contains subdirectories for containers/, image/, volumes/, overlay2/ (the storage driver layers), build cache, swarm state, and more — EVERYTHING Docker persists lives under it. Distractors: /var/lib/containers is Podman's root (different runtime!), ~/.docker only holds client config (config.json auth, CLI settings), /etc/docker holds daemon.json configuration — not image/container data.
**Sources:** <a href="https://docs.docker.com/engine/storage/drivers/" target="_blank">Docker Docs - Storage drivers</a>
**Tags:** k8s::kcna topic::docker topic::storage src::session

---

<!-- note:1794263352987 model:Many -->
**Domain:** Docker Storage - image layers
**Question:** What is a 'layer' in a Docker image?
**Options:** A. Each Dockerfile instruction copies the entire filesystem into a new layer<br>B. Each Dockerfile instruction creates a layer containing ONLY the changes/diff relative to the previous layer<br>C. Layers are writable so containers can modify them directly<br>D. Only RUN instructions create layers — COPY reuses the base layer
**Answer:** B (2) – Each Dockerfile instruction creates a layer containing ONLY the changes/diff relative to the previous layer
**Explanation:** A Docker image is a stack of read-only layers: FROM provides the base, then each instruction (RUN, COPY, ADD…) produces ONE new layer holding just what that instruction changed — e.g. 'apt-get install nginx' adds nginx's files as a layer, not a whole new filesystem. Layers are content-addressed and shareable. Nuance: metadata instructions (ENV, LABEL, EXPOSE) also create thin layers; ENTRYPOINT/CMD only set config — they don't add file layers.
**Sources:** <a href="https://docs.docker.com/engine/storage/drivers/" target="_blank">Docker Docs - Storage drivers</a>
**Tags:** k8s::kcna topic::docker topic::storage topic::images src::session

---

<!-- note:1794263352988 model:Many -->
**Domain:** Docker Storage - layer caching
**Question:** What are the benefits of Docker's layered image architecture? (Select all that apply)
**Options:** A. Identical base layers are stored once and shared across images — saves disk<br>B. On rebuild, cached layers are reused until a changed instruction — faster builds, no unnecessary rebuilds<br>C. Only the layers whose instructions changed get rebuilt on top of the cache<br>D. Layers can be edited in place after the image is built
**Answer:** A, B, C – shared base layers save disk, the layer cache speeds rebuilds, and unchanged layers aren't rebuilt; D is wrong — layers are read-only
**Explanation:** Layer caching is the layered architecture's superpower: (A) identical base layers (e.g. the ubuntu base) are stored ONCE and shared by every image built FROM it — massive disk savings; (B) on rebuild, Docker reuses cached layers until it hits an instruction whose inputs changed, then rebuilds only from there down — updating app code doesn't re-run apt-get; (C) the registry also stores/pushes layers once and dedupes across images. D is the trap: image layers are READ-ONLY — you cannot edit them after build; runtime writes go to the container's separate writable layer (copy-on-write).
**Sources:** <a href="https://docs.docker.com/build/cache/" target="_blank">Docker Docs - Build cache</a>
**Tags:** k8s::kcna topic::docker topic::storage topic::images src::session

---

<!-- note:1794263352989 model:Many -->
**Domain:** Docker Storage - container layer
**Question:** What filesystem layers make up a running Docker container?
**Options:** A. A full copy of the image filesystem made writable for each container<br>B. Read-only image layers (the built image) plus ONE writable 'container layer' on top for runtime changes<br>C. The image layers become writable once a container starts<br>D. A shared writable layer common to all containers from the same image
**Answer:** B (2) – Read-only image layers (the built image) plus ONE writable 'container layer' on top for runtime changes
**Explanation:** Every running container's filesystem = the image's read-only layers (shared, immutable) + a single writable layer unique to that container. Everything the app writes — new files, logs, overwrites of image files — lands in the container layer. The image layers are never modified, which is exactly why one image can safely back many containers. The writable layer is per-container and dies with the container — nothing in it persists.
**Sources:** <a href="https://docs.docker.com/engine/storage/" target="_blank">Docker Docs - Storage</a>
**Tags:** k8s::kcna topic::docker topic::storage src::session

---

<!-- note:1794263352990 model:Many -->
**Domain:** Docker Storage - copy-on-write
**Question:** A container process modifies /etc/nginx/nginx.conf, which exists in the read-only image layers. What does Docker do?
**Options:** A. Docker edits the file directly in the shared image layer<br>B. Docker copies the file up into the writable container layer; all edits hit the copy — the read-only image layer stays untouched<br>C. The container gets a full copy of every file it might modify<br>D. The write fails because image layers are read-only
**Answer:** B (2) – Docker copies the file up into the writable container layer; all edits hit the copy — the read-only image layer stays untouched
**Explanation:** Copy-on-write (CoW): image layers are shared read-only, so when a container modifies a file that lives in a lower layer, Docker doesn't edit it in place — it COPIES the file up to the container's writable layer and applies changes there. Result: the image layer remains pristine and shareable across all containers; each container sees its own modified version. This is why 'docker commit' snapshots are possible and why images stay immutable. Storage drivers (overlay2 etc.) implement this efficiently — only changed files consume new disk.
**Sources:** <a href="https://docs.docker.com/engine/storage/drivers/" target="_blank">Docker Docs - Storage drivers</a>
**Tags:** k8s::kcna topic::docker topic::storage src::session

---

<!-- note:1794263352991 model:Many -->
**Domain:** Docker Storage - volumes
**Question:** How do you persist data written by a Docker container using a named volume?
**Options:** A. docker volume create makes a directory on the host you mount with -v /host/path:/data<br>B. docker volume create data_volume — stored under /var/lib/docker/volumes on the host, mounted into the container at a path like /data; survives container deletion<br>C. Volumes are stored inside the image's read-only layers<br>D. Volumes must be created inside the container before use
**Answer:** B (2) – docker volume create data_volume — stored under /var/lib/docker/volumes on the host, mounted into the container at a path like /data; survives container deletion
**Explanation:** Named volumes are Docker-managed persistent storage: <code>docker volume create data_volume</code> creates it under /var/lib/docker/volumes/data_volume/_data on the host (location managed by the daemon — don't touch it directly). Mount at runtime: <code>docker run -v data_volume:/data myimage</code> — inside the container it appears as a normal directory. When the container is removed, the VOLUME survives (unlike the writable layer). Volumes live outside the image layer stack entirely, so they're immune to image changes and CoW.
**Sources:** <a href="https://docs.docker.com/engine/storage/volumes/" target="_blank">Docker Docs - Volumes</a>
**Tags:** k8s::kcna topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794263352992 model:Many -->
**Domain:** Docker Storage - storage drivers
**Question:** How does Docker handle storage drivers for its layered filesystem?
**Options:** A. You must pick the storage driver manually at install time<br>B. overlay2 is the default on modern Linux; aufs/zfs/btrfs/devicemapper are alternatives chosen automatically based on the host OS and backing filesystem<br>C. overlay2 is the only supported storage driver<br>D. The storage driver is selected per-container, not per-host
**Answer:** B (2) – overlay2 is the default on modern Linux; aufs/zfs/btrfs/devicemapper are alternatives chosen automatically based on the host OS and backing filesystem
**Explanation:** Storage drivers implement the layered + copy-on-write machinery on disk. overlay2 is the default on all modern Linux distros (uses the kernel's overlay filesystem — fast, low overhead). Legacy/alternative drivers: aufs (older Ubuntu default), zfs and btrfs (used when the host filesystem IS zfs/btrfs — CoW-native, snapshots for free), devicemapper (old RHEL/CentOS, largely deprecated), vfs (no layering, testing only). Docker AUTO-SELECTS the best driver at install based on OS + filesystem — you rarely choose manually; check with <code>docker info | grep 'Storage Driver'</code>.
**Sources:** <a href="https://docs.docker.com/engine/storage/drivers/" target="_blank">Docker Docs - Storage drivers</a>
**Tags:** k8s::kcna topic::docker topic::storage src::session

---

<!-- note:1794263352993 model:Many -->
**Domain:** Docker Storage - volumes vs binds
**Question:** What is the difference between a Docker volume and a bind mount? (Select all that apply)
**Options:** A. Named volumes live under /var/lib/docker/volumes while bind mounts link a host path — both survive container deletion equally<br>B. Named volumes are daemon-managed under /var/lib/docker/volumes and persist independently; bind mounts link any host path directly with no Docker management<br>C. Bind mounts require docker volume create first; named volumes mount arbitrary host paths<br>D. Volumes are per-container only; bind mounts are shared across all containers
**Answer:** B, C – docker volume create data_volume stored under /var/lib/docker/volumes, and bind mounts link any host path directly; A describes neither correctly and D is wrong
**Explanation:** Two mount types differ in WHO manages the host side: NAMED VOLUME — created by <code>docker volume create</code>, lives under /var/lib/docker/volumes (daemon-managed location), survives container deletion, portable across hosts via volume drivers; ideal for persistent app data (databases). BIND MOUNT — <code>-v /host/path:/container/path</code> links ANY host path directly into the container; the host path is YOUR choice, both host processes and the container can modify it simultaneously; great for dev (mount source code) or accessing host files. tmpfs (bonus third type) = memory-only, dies with the container.
**Sources:** <a href="https://docs.docker.com/engine/storage/" target="_blank">Docker Docs - Storage</a>
**Tags:** k8s::kcna topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794263356975 model:Basic -->
**Front:** What does ENTRYPOINT do in a Dockerfile, and how does it differ from CMD?
**Back:** ENTRYPOINT defines the executable the container RUNS when it starts — the fixed 'main' process. Difference from CMD: CMD sets default ARGUMENTS and is fully overridable (<code>docker run image other-cmd</code>); ENTRYPOINT is not replaced — extra args from docker run get APPENDED to it. The idiomatic combo: <code>ENTRYPOINT ["python"] + CMD ["app.py"]</code> lets you swap the script without changing the interpreter. ENTRYPOINT affects only container startup — it creates no filesystem layer (it's config, like ENV/LABEL).
**Tags:** k8s::kcna topic::docker topic::images src::session

---

<!-- note:1794263356976 model:Basic -->
**Front:** Why does data written inside a running container disappear when the container is removed — and what's the fix?
**Back:** The writable container layer is unique per container and exists ONLY while the container runs — docker rm destroys it and everything written there is gone (logs, generated files, database files written without a mount). That's why the layer can't be your persistence story: the image layers are shared read-only, the container layer is disposable. The fixes are the mount types — named volumes (daemon-managed, /var/lib/docker/volumes), bind mounts (direct host path), tmpfs (memory-only, also dies with the container). For databases and anything you can't regenerate, mount a volume.
**Tags:** k8s::kcna topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794263359749 model:Cloze -->
**Text:** Persist container data with a named volume:<br><br>{{c1::<code>docker volume create data_volume</code>}}  # creates /var/lib/docker/volumes/data_volume<br>{{c2::<code>docker run -v data_volume:/data myimage</code>}}  # mount volume at /data<br><br>Bind mount — direct host path into the container:<br>{{c3::<code>docker run -v /home/me/code:/app myimage</code>}}
**Back Extra:** -v <host>:<container> covers BOTH: named volume (left side is a volume NAME → /var/lib/docker/volumes) and bind mount (left side is a host PATH like /home/me/code → /app). --mount is the explicit alternative: --mount type=volume,source=data_volume,target=/data or type=bind,source=/host/path,target=/app — clearer, validates options better.
**Tags:** k8s::kcna topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794263701180 model:Many -->
**Domain:** Docker Storage - drivers vs plugins
**Question:** What is the difference between a Docker storage driver and a volume driver?
**Options:** A. They are two names for the same plugin system<br>B. Storage drivers manage the layered image filesystem (CoW); volume drivers manage named-volume lifecycle and where volume data actually lives<br>C. Volume drivers are just faster versions of storage drivers<br>D. Storage drivers were replaced by volume drivers in modern Docker
**Answer:** B (2) – Storage drivers manage the layered image filesystem (CoW); volume drivers manage named-volume lifecycle and where volume data actually lives
**Explanation:** Two different plugin systems, easy to confuse: STORAGE DRIVERS (overlay2, aufs, zfs…) implement the layered read-only-image + writable-container-layer filesystem — they know nothing about volumes. VOLUME DRIVERS/plugins handle the lifecycle of NAMED volumes (create/mount/unmount/remove) and decide WHERE the bytes live — local disk by default, or remote/cloud storage via plugins. Rule: storage driver = image/container filesystem machinery; volume driver = the -v volume backend.
**Sources:** <a href="https://docs.docker.com/engine/extend/plugins_volume/" target="_blank">Docker Docs - Volume plugins</a>
**Tags:** k8s::kcna topic::docker topic::storage src::session

---

<!-- note:1794263701181 model:Many -->
**Domain:** Docker Storage - local driver
**Question:** What does the 'local' volume driver do?
**Options:** A. local is a plugin you must install separately<br>B. The 'local' driver is the default — stores volume data under /var/lib/docker/volumes on the host<br>C. local stores volumes inside the container image layers<br>D. local only works for bind mounts, not named volumes
**Answer:** B (2) – The 'local' driver is the default — stores volume data under /var/lib/docker/volumes on the host
**Explanation:** The 'local' volume driver is built in and is the DEFAULT for every docker volume create — it stores data on the host filesystem under /var/lib/docker/volumes/<name>/_data. If you never pass --driver, you get 'local'. It's the volume-side equivalent of overlay2 for layers: zero-config, host-disk-backed, dies with the host. Other drivers must be installed as plugins first (docker plugin install) before --driver can use them.
**Sources:** <a href="https://docs.docker.com/engine/storage/volumes/" target="_blank">Docker Docs - Volumes</a>
**Tags:** k8s::kcna topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794263701182 model:Many -->
**Domain:** Docker Storage - volume plugins
**Question:** Which of these are Docker VOLUME driver plugins? (Select all that apply)
**Options:** A. amazon-ebs — creates AWS EBS volumes for containers<br>B. azurefile — mounts Azure Files SMB shares<br>C. overlay2 — provides copy-on-write image layers<br>D. flocker — manages volumes across a cluster of hosts
**Answer:** A, B, D – amazon-ebs (AWS block storage), azurefile (Azure Files SMB), and flocker (cluster volume management); overlay2 and aufs are STORAGE drivers, not volume drivers
**Explanation:** Volume plugins put named volumes on EXTERNAL storage: amazon-ebs → AWS EBS volumes, azurefile → Azure Files (SMB), google-persistent-disk → GCP PD, flocker → cluster-aware volume placement, rexray → multi-cloud, longhorn/portworx → Kubernetes-native distributed storage. The distractors are the trap: overlay2 and aufs are STORAGE drivers — they manage image layers, not volumes. Telling the two plugin families apart is exactly what this lesson is about.
**Sources:** <a href="https://docs.docker.com/engine/extend/plugins_volume/" target="_blank">Docker Docs - Volume plugins</a>
**Tags:** k8s::kcna topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794263701183 model:Many -->
**Domain:** Docker Storage - plugin usage
**Question:** How do you create and use a volume backed by a third-party plugin like amazon-ebs?
**Options:** A. docker run --driver=amazon-ebs -v /data<br>B. docker volume create --driver=<plugin> <name>, then mount normally with -v <name>:<path> — the driver is chosen at volume-creation time<br>C. Volume plugins replace docker run entirely<br>D. You edit /etc/docker/daemon.json to switch drivers per container
**Answer:** B (2) – docker volume create --driver=<plugin> <name>, then mount normally with -v <name>:<path> — the driver is chosen at volume-creation time
**Explanation:** Using a volume plugin is two steps: (1) install the plugin (docker plugin install <name> or it ships configured), (2) create the volume WITH the driver: <code>docker volume create --driver=amazon-ebs --opt size=10 gb_vol</code> — driver-specific options go in --opt. Then use it like any volume: <code>docker run -v gb_vol:/data app</code>. The --volume-driver flag on docker run sets a default driver for anonymous volumes; --mount type=volume,volume-driver=X selects per-volume. The driver choice sticks to the volume — it was decided at create time.
**Sources:** <a href="https://docs.docker.com/engine/extend/plugins_volume/" target="_blank">Docker Docs - Volume plugins</a>
**Tags:** k8s::kcna topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794263701184 model:Many -->
**Domain:** Docker Storage - plugin lifecycle
**Question:** How does a Docker volume plugin actually deliver storage to a container?
**Options:** A. The plugin copies volume data into the container's writable layer<br>B. The plugin API (Create/Mount/Unmount/Remove/Get/List/Path) lets external systems manage volume lifecycle; daemon bind-mounts the returned path into the container<br>C. Plugins run inside the container and manage its filesystem directly<br>D. The daemon proxies all volume I/O through the plugin on every read/write
**Answer:** B (2) – The plugin API (Create/Mount/Unmount/Remove/Get/List/Path) lets external systems manage volume lifecycle; daemon bind-mounts the returned path into the container
**Explanation:** A volume plugin implements the VolumeDriver API over HTTP-ish endpoints: Create (register name), Mount (called per container start — returns a host path where data lives), Unmount (per stop), Remove (on docker rm -v / volume rm), plus Get/List/Path/Capabilities. KEY: the plugin doesn't stream data to the container — it returns a MOUNTPOINT path, and the Docker daemon bind-mounts that path into the container. Capabilities.Scope matters for clusters: 'global' = create once for the whole cluster; 'local' = per-host. This plugin indirection is the ancestor of Kubernetes CSI drivers.
**Sources:** <a href="https://docs.docker.com/engine/extend/plugins_volume/" target="_blank">Docker Docs - Volume plugins</a>
**Tags:** k8s::kcna topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794263701185 model:Many -->
**Domain:** Docker Storage - CSI bridge
**Question:** How do Docker volume plugins relate to Kubernetes CSI drivers?
**Options:** A. CSI replaced Docker volumes entirely — they are unrelated systems<br>B. Volume plugins are Docker's version of the same idea — decouple the volume API from where bytes physically live (local disk vs EBS/Azure Files/PD)<br>C. CSI is a Docker storage driver for image layers<br>D. Kubernetes cannot use cloud storage — only local disk
**Answer:** B (2) – Volume plugins are Docker's version of the same idea — decouple the volume API from where bytes physically live (local disk vs EBS/Azure Files/PD)
**Explanation:** Docker volume plugins and Kubernetes CSI (Container Storage Interface) solve the same architectural problem: the orchestrator asks for 'a volume', a pluggable driver decides WHERE it lives. Docker: volume drivers (local, amazon-ebs, azurefile, flocker…) behind docker volume create/-v. Kubernetes: CSI drivers (ebs.csi.aws.com, efs.csi.aws.com, pd.csi.storage.gke.io…) behind PersistentVolumes/StorageClasses. Same mental model — when you meet PV/PVC/StorageClass in the K8s storage lesson, read them as 'Kubernetes' version of docker volume + volume driver.
**Sources:** <a href="https://kubernetes-csi.github.io/docs/" target="_blank">Kubernetes CSI Docs</a>
**Tags:** k8s::kcna topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794263704051 model:Cloze -->
**Text:** Create a volume on third-party storage via a volume plugin, then mount it:<br><br>{{c1::<code>docker volume create --driver=amazon-ebs --opt size=10 gb_vol</code>}}<br>{{c2::<code>docker run -v gb_vol:/data myapp</code>}}<br><br>Default local volume (no plugin):<br>{{c3::<code>docker volume create data_volume</code>}} → stored under {{c4::<code>/var/lib/docker/volumes</code>}}
**Back Extra:** Driver is chosen at CREATE time and sticks to the volume. --driver=<name> picks the plugin; --opt passes driver-specific settings (size, iops, type). Default (no --driver) = local → /var/lib/docker/volumes. Check installed drivers: docker info | grep -i volume or docker plugin ls.
**Tags:** k8s::kcna topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794266469476 model:Many -->
**Domain:** CSI - overview
**Question:** Why was the Container Storage Interface (CSI) created?
**Options:** A. CSI makes container images smaller and faster to pull<br>B. Same pluggable-interface pattern as CRI (runtimes) and CNI (networks): decouple the orchestrator from vendor-specific implementations<br>C. CSI is Kubernetes' built-in local disk manager<br>D. CSI replaced PersistentVolumes and StorageClasses
**Answer:** B (2) – Same pluggable-interface pattern as CRI (runtimes) and CNI (networks): decouple the orchestrator from vendor-specific implementations
**Explanation:** Cloud-native converged on pluggable interfaces: CRI lets any container runtime plug into the kubelet; CNI lets any network plugin plug into pod networking; CSI does the same for STORAGE — any storage vendor writes one CSI plugin and every orchestrator can use it, no core-code changes. Before CSI, storage integrations were bespoke per-vendor code inside each orchestrator — adding EBS vs Azure Disk vs Ceph meant orchestrator-specific work every time. CSI standardizes the API so storage became a plugin like runtimes and networks already were.
**Sources:** <a href="https://kubernetes-csi.github.io/docs/" target="_blank">Kubernetes CSI Docs</a>
**Tags:** k8s::kcna topic::storage topic::csi src::session

---

<!-- note:1794266469477 model:Many -->
**Domain:** CSI - universality
**Question:** Is CSI specific to Kubernetes?
**Options:** A. CSI is a Kubernetes-only API like PersistentVolume<br>B. CSI is a vendor-neutral industry spec (CNCF) — any container orchestration system can consume any vendor's CSI plugin<br>C. CSI only works with AWS EBS storage<br>D. CSI is a Docker volume driver renamed
**Answer:** B (2) – CSI is a vendor-neutral industry spec (CNCF) — any container orchestration system can consume any vendor's CSI plugin
**Explanation:** CSI is NOT a Kubernetes API or K8s-specific standard — it's an open spec maintained by the container-storage-interface project (CNCF ecosystem). The same plugin works with Kubernetes, Mesos, Cloud Foundry, or any CO that implements the CSI client side. Vendor neutrality cuts both ways: storage vendors implement the spec once and reach every orchestrator; orchestrators implement the client once and reach every storage backend. Kubernetes merely adopted CSI as its standard storage plugin mechanism (GA since v1.13, in-tree plugins removed in 1.20+).
**Sources:** <a href="https://github.com/container-storage-interface/spec" target="_blank">CSI Spec</a>
**Tags:** k8s::kcna topic::storage topic::csi src::session

---

<!-- note:1794266469478 model:Many -->
**Domain:** CSI - services
**Question:** What are the three CSI services a storage plugin can implement? (Select all that apply)
**Options:** A. Identity — plugin info and capabilities<br>B. Controller — cluster-level ops: create/delete volumes, attach/detach, expand<br>C. Scheduler — decides which node a volume lands on<br>D. Node — per-node ops: stage, publish into pod, unpublish, stats
**Answer:** A, B, D – Identity (plugin info/capabilities), Controller (cluster-level create/delete/attach/expand), and Node (per-node stage/publish/unpublish/stats); E is wrong — CSI has no 'Scheduler' service
**Explanation:** The CSI spec defines three gRPC services a plugin may implement: IDENTITY — GetPluginInfo/GetPluginCapabilities/Probe: 'who are you, what can you do'; CONTROLLER — cluster-scoped ops usually run once: CreateVolume, DeleteVolume, ControllerPublishVolume (attach to node), ControllerUnpublishVolume, ControllerExpandVolume; NODE — per-node ops run on every node that mounts the volume: NodeStageVolume (format + global mount), NodePublishVolume (bind into pod path), NodeUnpublish/Unstage, NodeGetVolumeStats. A driver can implement all three or only node (for pre-provisioned local volumes).
**Sources:** <a href="https://github.com/container-storage-interface/spec/blob/master/spec.md" target="_blank">CSI Spec</a>
**Tags:** k8s::kcna topic::storage topic::csi src::session

---

<!-- note:1794266469479 model:Many -->
**Domain:** CSI - RPCs
**Question:** Which of these are actual CSI RPCs called by the orchestrator? (Select all that apply)
**Options:** A. CreateVolume — provision a new volume<br>B. RunPodSandbox — start a pod's isolation environment<br>C. ControllerPublishVolume — attach a volume to a node<br>D. NodeStageVolume — format and globally mount the volume on a node
**Answer:** A, C, D – CreateVolume, ControllerPublishVolume, and NodeStageVolume are all CSI RPCs; RunPodSandbox is a CRI call, not CSI
**Explanation:** CSI RPCs the orchestrator calls: CONTROLLER side — CreateVolume, DeleteVolume, ControllerPublishVolume (attach volume to node), ControllerUnpublishVolume, ControllerExpandVolume, ValidateVolumeCapabilities; NODE side — NodeStageVolume, NodeUnstageVolume, NodePublishVolume, NodeUnpublishVolume, NodeGetVolumeStats, NodeExpandVolume; IDENTITY — GetPluginInfo, GetPluginCapabilities, Probe. Distractors test interface confusion: RunPodSandbox/CreateContainer are CRI (runtime) calls; ADD/DEL are CNI (network) calls. Each interface has its own RPC vocabulary — mixing them is the classic exam trap.
**Sources:** <a href="https://github.com/container-storage-interface/spec/blob/master/spec.md" target="_blank">CSI Spec</a>
**Tags:** k8s::kcna topic::storage topic::csi src::session

---

<!-- note:1794266469480 model:Many -->
**Domain:** CSI - callers
**Question:** Who calls the CSI RPCs like CreateVolume or NodePublishVolume?
**Options:** A. The application container calls CSI RPCs to get storage<br>B. The orchestrator/CO side calls them — kubelet invokes node RPCs via Unix socket; master-side sidecars watch the K8s API and trigger controller RPCs<br>C. etcd calls CSI RPCs to persist volume metadata<br>D. CSI drivers call kubelet RPCs to request mounts
**Answer:** B (2) – The orchestrator/CO side calls them — kubelet invokes node RPCs via Unix socket; master-side sidecars watch the K8s API and trigger controller RPCs
**Explanation:** CSI RPCs are called BY the container orchestrator, never by the application (apps just see a mounted filesystem). In Kubernetes specifically: KUBELET calls NODE-service RPCs (NodeStageVolume/NodePublishVolume) directly over a Unix Domain Socket — it discovers drivers via kubelet plugin registration. Master components NEVER talk to the driver directly — they only see the K8s API; instead sidecar containers in the driver pod (external-provisioner watches PVCs→CreateVolume, external-attacher→ControllerPublishVolume, external-resizer→expand, node-driver-registrar) translate API events into CSI calls. This keeps drivers CO-agnostic.
**Sources:** <a href="https://kubernetes-csi.github.io/docs/" target="_blank">Kubernetes CSI Docs</a>
**Tags:** k8s::kcna topic::storage topic::csi src::session

---

<!-- note:1794266469481 model:Many -->
**Domain:** CSI - Kubernetes wiring
**Question:** How does a CSI driver plug into Kubernetes?
**Options:** A. CSI drivers are compiled into the kubelet binary<br>B. A CSI plugin pod (controller + node DaemonSet) registered via CSIDriver/CSINode objects; StorageClass.provisioner names the driver; PVC binding triggers provisioning<br>C. CSI volumes bypass PVs and PVCs entirely<br>D. You install CSI drivers by patching kubelet flags on each node
**Answer:** B (2) – A CSI plugin pod (controller + node DaemonSet) registered via CSIDriver/CSINode objects; StorageClass.provisioner names the driver; PVC binding triggers provisioning
**Explanation:** How K8s consumes CSI: the driver deploys as pods — a controller plugin (Deployment, for cluster ops) + node plugin (DaemonSet, one per node) + sidecars (external-provisioner/-attacher/-resizer, node-driver-registrar). It registers via CSIDriver and CSINode API objects. The StorageClass's provisioner field holds the driver name (e.g. ebs.csi.aws.com); a PVC referencing that StorageClass triggers external-provisioner → CreateVolume → PV/PVC binding. GA since Kubernetes v1.13; in-tree volume plugins were fully removed by v1.20 — CSI is THE storage mechanism now.
**Sources:** <a href="https://kubernetes-csi.github.io/docs/" target="_blank">Kubernetes CSI Docs</a>
**Tags:** k8s::kcna topic::storage topic::csi src::session

---

<!-- note:1794266469482 model:Many -->
**Domain:** CSI - stage vs publish
**Question:** What is the difference between NodeStageVolume and NodePublishVolume?
**Options:** A. Stage mounts into the pod; Publish prepares the node globally<br>B. NodeStageVolume does the node-wide prep (format, mount to a staging path — once per node); NodePublishVolume bind-mounts the staged volume into each pod's specific path<br>C. Stage and Publish are aliases for the same RPC<br>D. Publish happens on the controller, Stage on the node
**Answer:** B (2) – NodeStageVolume does the node-wide prep (format, mount to a staging path — once per node); NodePublishVolume bind-mounts the staged volume into each pod's specific path
**Explanation:** The node-side mount is deliberately two-phase: STAGE = global per-node operation — NodeStageVolume formats the device if needed and mounts it at a staging/global path (e.g. /var/lib/kubelet/plugins/kubernetes.io/csi/pv-xxx/globalmount); happens ONCE per node per volume regardless of pod count. PUBLISH = per-pod operation — NodePublishVolume bind-mounts (or mounts) the staged volume at the pod's target path (e.g. /var/lib/kubelet/pods/<uid>/volumes/kubernetes.io~csi/pv-xxx/mount). Unpublish/Unstage reverse it on teardown. This split lets one staged volume serve multiple pods and keeps pod-specific paths clean.
**Sources:** <a href="https://github.com/container-storage-interface/spec/blob/master/spec.md" target="_blank">CSI Spec</a>
**Tags:** k8s::kcna topic::storage topic::csi src::session

---

<!-- note:1794266473278 model:Cloze -->
**Text:** Key CSI RPCs the orchestrator calls:<br><br>CONTROLLER service (cluster-scoped):<br>{{c1::<code>CreateVolume</code>}} → {{c2::<code>DeleteVolume</code>}} → {{c3::<code>ControllerPublishVolume</code>}} (attach to node) → {{c4::<code>ControllerUnpublishVolume</code>}} → {{c5::<code>ControllerExpandVolume</code>}}<br><br>NODE service (per-node, kubelet → Unix socket):<br>{{c6::<code>NodeStageVolume</code>}} (format + global mount) → {{c7::<code>NodePublishVolume</code>}} (bind into pod path)
**Back Extra:** CONTROLLER (cluster ops, once): CreateVolume, DeleteVolume, ControllerPublishVolume (attach), ControllerUnpublishVolume (detach), ControllerExpandVolume. NODE (per-node, via kubelet/UDS): NodeStageVolume (format+global mount), NodePublishVolume (bind into pod path), NodeUnpublishVolume, NodeUnstageVolume, NodeGetVolumeStats. IDENTITY: GetPluginInfo, GetPluginCapabilities, Probe. Mnemonic: Controller* = once per volume cluster-wide; Node* = on every node that mounts it.
**Tags:** k8s::kcna topic::storage topic::csi src::session

---

<!-- note:1794272298978 model:Many -->
**Domain:** K8s Volumes - overview
**Question:** Why do Kubernetes pods need volumes?
**Options:** A. Volumes make pods run faster by caching images<br>B. Pods are ephemeral like containers — volume mounts give data persistence beyond pod life and let containers share files<br>C. Volumes replace the need for PersistentVolumes entirely<br>D. Volumes are only needed for Windows pods
**Answer:** B (2) – Pods are ephemeral like containers — volume mounts give data persistence beyond pod life and let containers share files
**Explanation:** Same problem as Docker, one level up: pods are ephemeral — scheduled, run, deleted; container filesystem writes die with them (kubelet restarts crashed containers with a CLEAN state). Kubernetes volumes solve the two core problems: (1) PERSISTENCE — a mounted volume's data survives pod deletion (for persistent types) and container restarts (always); (2) SHARING — multiple containers in one pod can mount the same volume to share files (app + log-shipper sidecar is the classic). A volume is fundamentally just 'a directory, possibly with data, accessible to the pod's containers' — the type decides what backs it.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/volumes/" target="_blank">Kubernetes Docs - Volumes</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794272298979 model:Many -->
**Domain:** K8s Volumes - YAML mechanics
**Question:** How are volumes declared and mounted in a Pod spec?
**Options:** A. Volumes are declared inside each container's spec automatically<br>B. .spec.volumes declares the volumes; .spec.containers[].volumeMounts mounts each into a specific container path — every container mounts independently<br>C. volumeMounts go at pod level, volumes inside containers<br>D. A single volumeMount entry mounts the volume into all containers at once
**Answer:** B (2) – .spec.volumes declares the volumes; .spec.containers[].volumeMounts mounts each into a specific container path — every container mounts independently
**Explanation:** Pod volumes are a TWO-PART declaration: (1) spec.volumes[] — top-level list declaring each volume and its TYPE (emptyDir: {}, hostPath: {path:...}, persistentVolumeClaim: {claimName:...}, secret: {...}…); (2) spec.containers[].volumeMounts[] — per-container list saying mountPath: where inside THAT container + name: which declared volume. Every container that needs the volume must list its own volumeMount — volumes are pod-scoped, mounts are container-scoped. A volume can be mounted by multiple containers (sharing) or just one.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/volumes/" target="_blank">Kubernetes Docs - Volumes</a>
**Tags:** k8s::kcna topic::storage topic::volumes topic::yaml src::session

---

<!-- note:1794272298980 model:Many -->
**Domain:** K8s Volumes - hostPath
**Question:** What does a hostPath volume do in Kubernetes?
**Options:** A. hostPath copies host files into the pod's image at build time<br>B. hostPath mounts a file or directory from the NODE's filesystem into the pod — a powerful escape hatch with real security risks<br>C. hostPath is the recommended way to share data between pods<br>D. hostPath only works on control-plane nodes
**Answer:** B (2) – hostPath mounts a file or directory from the NODE's filesystem into the pod — a powerful escape hatch with real security risks
**Explanation:** hostPath is Kubernetes' version of Docker's bind mount: spec.volumes[].hostPath.path points at a path on the NODE's filesystem, mounted into the pod. It's the 'powerful escape hatch' — needed for node-level access (reading /var/log for log collectors, static pods that can't use ConfigMaps) — but the docs warn heavily: it can expose kubelet credentials or the container runtime socket (container escape!), behavior differs per node (files differ), and hostPath usage does NOT count as ephemeral storage (you monitor disk yourself). Prefer a 'local' PersistentVolume when you can.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/volumes/#hostpath" target="_blank">Kubernetes Docs - Volumes</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794272298981 model:Many -->
**Domain:** K8s Volumes - hostPath types
**Question:** Which hostPath volume 'type' values are valid? (Select all that apply)
**Options:** A. DirectoryOrCreate creates a 0755 directory if the path doesn't exist<br>B. Directory requires the path to already exist as a directory<br>C. FileOrCreate creates a directory with 0755 permissions<br>D. File requires the path to already exist as a file<br>E. Socket requires a UNIX socket at the path<br>F. BlockDeviceOrCreate auto-provisions a block device
**Answer:** B, D, E – DirectoryOrCreate creates a 0755 dir if missing, FileOrCreate creates a 0644 file; the rest either require existence (Directory/File), require special files (Socket/CharDevice/BlockDevice), or skip checks ("")
**Explanation:** hostPath.type controls validation/creation at mount time: "" (empty, default) = NO checks — mounts whatever's there, backward compatible; Directory = must already exist; DirectoryOrCreate = creates empty dir 0755 owned by kubelet if missing; File = must exist; FileOrCreate = creates empty file 0644 if missing; Socket = must be a UNIX socket; CharDevice/BlockDevice = must be device nodes (Linux only). A is wrong — File requires an existing FILE not dir; C mixes them up; F doesn't exist.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/volumes/#hostpath" target="_blank">Kubernetes Docs - Volumes</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794272298982 model:Many -->
**Domain:** K8s Volumes - type survey
**Question:** Which of these are valid Kubernetes pod volume types? (Select all that apply)
**Options:** A. emptyDir<br>B. Service<br>C. configMap<br>D. secret<br>E. persistentVolumeClaim<br>F. downwardAPI
**Answer:** A, C, D, E, F – emptyDir, configMap, secret, downwardAPI, projected, and persistentVolumeClaim are all real pod volume types; Service is a networking object, not a volume
**Explanation:** Kubernetes pod volume types fall into families: POD-SCOPED (die with pod) — emptyDir, hostPath, configMap, secret, downwardAPI, projected, image; CLUSTER-STORAGE — persistentVolumeClaim (the pod-side handle to durable storage), csi, local, nfs, iscsi, azureDisk, awsElasticBlockStore, gcePersistentDisk (in-tree ones deprecated → CSI). A pod can mix ANY number of types simultaneously. Service is a networking abstraction — not a volume. The survey-level skill: recognize the TYPE NAME in a pod spec and know which family it belongs to.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/volumes/" target="_blank">Kubernetes Docs - Volumes</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794272298983 model:Many -->
**Domain:** K8s Volumes - ephemeral vs persistent
**Question:** Which Kubernetes volume types persist data beyond the pod's lifetime?
**Options:** A. All volume types are destroyed when the pod is deleted<br>B. Ephemeral types (emptyDir, hostPath, configMap, secret…) die with the pod; PVC-backed volumes persist beyond pod deletion; container restarts preserve data for ALL types<br>C. PersistentVolumes die with the pod; emptyDir survives pod deletion<br>D. Volume data is lost on every container restart regardless of type
**Answer:** B (2) – Ephemeral types (emptyDir, hostPath, configMap, secret…) die with the pod; PVC-backed volumes persist beyond pod deletion; container restarts preserve data for ALL types
**Explanation:** The lifetime split: EPHEMERAL volumes (emptyDir, hostPath unless on persistent host dir, configMap, secret, downwardAPI, projected, image) are destroyed when the pod is deleted — their lifetime is bound to the pod. PERSISTENT volumes (via persistentVolumeClaim → PV, or CSI) exist beyond any pod's life — delete the pod, the data stays for the next pod to claim. Nuance that trips people: data survives CONTAINER restarts inside a running pod for EVERY volume type — the wipe happens at POD deletion for ephemeral types. hostPath is a gray zone: the mount dies with the pod but the host directory's data persists on the node.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/volumes/" target="_blank">Kubernetes Docs - Volumes</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794272298984 model:Many -->
**Domain:** K8s Volumes - PVC
**Question:** How does a pod get durable (persistent) storage in Kubernetes?
**Options:** A. persistentVolumeClaim creates a new PV on every pod start<br>B. persistentVolumeClaim volume type mounts a PersistentVolume into the pod — the user 'claims' durable storage without knowing cloud details<br>C. PVCs must be defined inside the pod spec itself<br>D. persistentVolumeClaim is only for Windows pods
**Answer:** B (2) – persistentVolumeClaim volume type mounts a PersistentVolume into the pod — the user 'claims' durable storage without knowing cloud details
**Explanation:** In the pod spec, persistentVolumeClaim is the volume type that connects pods to durable cluster storage: volumes[].persistentVolumeClaim.claimName references a PersistentVolumeClaim object; the PVC is bound to a PersistentVolume (provisioned statically or dynamically via StorageClass/CSI). This is the indirection that makes pods portable — the pod says 'give me storage named X', the PVC/PV/StorageClass machinery figures out whether that's EBS, Azure Disk, NFS, or local disk. Without it, pods could only use node-local or pod-scoped volumes.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/volumes/#persistentvolumeclaim" target="_blank">Kubernetes Docs - Volumes</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794272298985 model:Many -->
**Domain:** K8s Volumes - in-tree vs CSI
**Question:** What is the difference between in-tree and CSI (out-of-tree) volume plugins?
**Options:** A. In-tree plugins run as sidecar pods next to kubelet<br>B. In-tree plugins were compiled into the Kubernetes binaries themselves; CSI plugins are out-of-tree and install as extensions — same decoupling idea as Docker volume plugins<br>C. CSI is the replacement for in-tree plugins — vendors ship storage as pods without touching k8s core<br>D. In-tree plugins are faster because they skip the API server
**Answer:** B, C – In-tree plugins were compiled into the Kubernetes binaries themselves; CSI plugins are out-of-tree and install as extensions — same decoupling idea as Docker volume plugins
**Explanation:** Kubernetes volume plugins come in two eras: IN-TREE — built, linked, and shipped inside the core Kubernetes binaries (awsElasticBlockStore, gcePersistentDisk, azureDisk, vsphereVolume, portworxVolume, flexVolume, gitRepo…). Adding a new storage system required code into the k8s repo — slow, vendor-hostile. OUT-OF-TREE — CSI (and formerly FlexVolume) plugins deploy as ordinary pods/extensions, vendor-developed, no core changes. The migration is done: in-tree cloud plugins are DEPRECATED and in v1.37 their operations redirect to CSI drivers — CSI is the only supported path for new storage.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/volumes/" target="_blank">Kubernetes Docs - Volumes</a>
**Tags:** k8s::kcna topic::storage topic::volumes topic::csi src::session

---

<!-- note:1794272305615 model:Basic -->
**Front:** What does subPath do in a volumeMount, and when do you use it?
**Back:** subPath mounts only a SUBDIRECTORY of a volume instead of the whole thing: volumeMounts[].subPath: 'subdir' exposes just <volume>/subdir at mountPath. Use cases: mount one file/dir out of a shared config volume without exposing siblings; give a container write access to only part of a shared volume; mount a single file from a ConfigMap/Secret volume. Caveat: subPath does NOT get updated when the volume's content changes (no live updates for that subtree) — for config that must stay current, mount the whole volume or use env vars.
**Tags:** k8s::kcna topic::storage topic::volumes topic::yaml src::session

---

<!-- note:1794272305616 model:Basic -->
**Front:** What is a projected volume and what problem does it solve?
**Back:** A projected volume merges MULTIPLE volume sources into ONE directory: volumes[].projected.sources[] can combine secret, configMap, downwardAPI, and serviceAccountToken entries — all appear as files in the same mountPath. Classic use: the kubelet itself mounts the pod's service-account token this way (that's why /var/run/secrets/kubernetes.io/serviceaccount/ contains both the token AND ca.crt — different sources, one projected volume). Contrast: a plain secret/configMap volume mounts ONE source; projected stitches several together.
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794272613979 model:Many -->
**Domain:** K8s Storage - PV/PVC binding
**Question:** Can a PVC claim only PART of a PersistentVolume, or must it take the whole thing?
**Options:** A. Yes — multiple PVCs can each claim a portion of one PV<br>B. NO — binding is strictly one-to-one: one PVC claims one WHOLE PV exclusively; PVs cannot be sliced between claims<br>C. Yes — if the PV's capacity is larger than the PVC request<br>D. Only with ReadWriteMany access mode
**Answer:** B (2) – NO — binding is strictly one-to-one: one PVC claims one WHOLE PV exclusively; PVs cannot be sliced between claims
**Explanation:** Your skepticism is correct — the docs are explicit: 'A PVC to PV binding is a one-to-one mapping' and 'Once bound, PersistentVolumeClaim binds are exclusive.' A PVC claims an ENTIRE PV; you cannot split one PV across multiple PVCs. What the lecture meant by 'parts': PVs form a cluster-wide POOL of whole volumes, and each PVC claims one whole PV from that pool — 'give me some of the pool's storage' = 'bind me to one whole PV'. Bonus rule: the bound PV may be LARGER than requested — 'the user will always get at least what they asked for, but the volume may be in excess.'
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/#binding" target="_blank">Kubernetes Docs - PV/PVC Binding</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794272613980 model:Many -->
**Domain:** K8s Storage - PV spec
**Question:** What is a PersistentVolume (PV) in Kubernetes?
**Options:** A. apiVersion: storage.k8s.io/v1, kind: PersistentVolume<br>B. apiVersion: v1, kind: PersistentVolume — a cluster-scoped object describing real storage: capacity, accessModes, reclaimPolicy, storageClassName, claimRef, and the backend spec (csi/nfs/hostPath…)<br>C. PersistentVolumes are namespaced like PVCs<br>D. kind: VolumeClaimTemplate
**Answer:** B (2) – apiVersion: v1, kind: PersistentVolume — a cluster-scoped object describing real storage: capacity, accessModes, reclaimPolicy, storageClassName, claimRef, and the backend spec (csi/nfs/hostPath…)
**Explanation:** A PersistentVolume is a cluster-scoped API object (apiVersion: v1 — core group, NOT a CRD) that represents a piece of real storage in the cluster. Its spec declares: capacity.storage (size), accessModes (RWO/ROX/RWX/RWOP), persistentVolumeReclaimPolicy (what happens after release), storageClassName (which class it belongs to), claimRef (which PVC it's bound to), volumeMode (Filesystem vs Block), and the backend details — csi:, nfs:, hostPath:, local:, etc. Admins create PVs pointing at actual infrastructure (an EBS volume ID, an NFS server export, a node directory).
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/" target="_blank">Kubernetes Docs - Persistent Volumes</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794272613981 model:Many -->
**Domain:** K8s Storage - binding rules
**Question:** What must be true for a PVC to bind to a PV?
**Options:** A. PVC binds to any available PV regardless of size<br>B. PVC must request ≤ PV capacity, a compatible accessMode, and matching storageClass — otherwise it stays Pending/unbound until a fit appears<br>C. PVCs bind to the oldest PV in the cluster first<br>D. A PVC larger than the PV still binds — it just uses less space
**Answer:** B (2) – PVC must request ≤ PV capacity, a compatible accessMode, and matching storageClass — otherwise it stays Pending/unbound until a fit appears
**Explanation:** The control-plane binding loop matches PVCs to PVs on three criteria: SIZE — PVC's requested storage must be ≤ PV's capacity (a 100Gi PVC can't bind a 50Gi PV; it waits for a big enough PV); ACCESS MODE — PVC's requested modes must be satisfiable by the PV's modes; STORAGE CLASS — PVC's storageClassName must match the PV's (empty class '' = no dynamic provisioning, binds only to classless PVs). If nothing matches, the PVC stays UNBOUND indefinitely — 'claims will remain unbound indefinitely if a matching volume does not exist' — until a suitable PV appears or dynamic provisioning creates one.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/#binding" target="_blank">Kubernetes Docs - PV/PVC Binding</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794272613982 model:Many -->
**Domain:** K8s Storage - access modes
**Question:** What are Kubernetes PV/PVC access modes?
**Options:** A. RWO = one pod only, RWX = one node only<br>B. RWO=one node (but multiple pods on that node CAN share!), ROX=read-only many nodes, RWX=read-write many nodes, RWOP=read-write exactly ONE pod (CSI-only, stable since 1.29)<br>C. Access modes enforce filesystem-level read-only protection<br>D. RWOP works with all volume types including hostPath
**Answer:** B (2) – RWO=one node (but multiple pods on that node CAN share!), ROX=read-only many nodes, RWX=read-write many nodes, RWOP=read-write exactly ONE pod (CSI-only, stable since 1.29)
**Explanation:** Four access modes, abbreviated RWO/ROX/RWX/RWOP: ReadWriteOnce — mount read-write on ONE node (nuance: multiple pods ON THAT NODE can still share it — it's node-scoped not pod-scoped!); ReadOnlyMany — read-only on many nodes; ReadWriteMany — read-write on many nodes (NFS/EFS/Azure Files style shared storage); ReadWriteOncePod — read-write by exactly ONE pod cluster-wide, the strictest mode (CSI volumes only, stable v1.29). Two traps: (1) access modes are for MATCHING PVC↔PV and constraining mounts — they do NOT enforce read-only (a ROX volume isn't guaranteed read-only!); (2) a volume mounts with ONE mode at a time.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes" target="_blank">Kubernetes Docs - Access Modes</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794272613983 model:Many -->
**Domain:** K8s Storage - reclaim policy
**Question:** What do PersistentVolume reclaim policies do?
**Options:** A. Retain deletes the backing storage; Delete keeps it<br>B. Retain keeps the PV+data for manual reclaim, Delete removes both PV and backing asset (the default — dynamic PVs inherit the StorageClass policy), Recycle is deprecated<br>C. Recycle is the recommended policy for production<br>D. Reclaim policy only applies to static PVs, not dynamic ones
**Answer:** B (2) – Retain keeps the PV+data for manual reclaim, Delete removes both PV and backing asset (the default — dynamic PVs inherit the StorageClass policy), Recycle is deprecated
**Explanation:** persistentVolumeReclaimPolicy decides what happens to a PV AFTER its PVC is released: RETAIN — PV and data stay; admin manually cleans up (delete PV object, verify asset, clear claimRef, delete asset) — safest for valuable data; DELETE — PV object AND backing storage asset are both removed — the default, and dynamically-provisioned PVs INHERIT their StorageClass's reclaimPolicy (which defaults to Delete — so dynamic volumes self-destruct unless you change the class); RECYCLE — deprecated scrub-and-reuse, replaced by dynamic provisioning. Classic gotcha: PVC deleted → PV with Delete policy → your EBS volume GONE.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/#reclaiming" target="_blank">Kubernetes Docs - Reclaiming</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794272613984 model:Many -->
**Domain:** K8s Storage - provisioning
**Question:** What is the difference between static and dynamic PV provisioning?
**Options:** A. Static provisioning creates PVs automatically on PVC creation<br>B. Static: admin pre-creates PVs; Dynamic: PVC's storageClass triggers a provisioner to create a PV on demand — no admin PV needed<br>C. Dynamic provisioning requires manually creating PVs first<br>D. Static and dynamic are the same thing with different names
**Answer:** B (2) – Static: admin pre-creates PVs; Dynamic: PVC's storageClass triggers a provisioner to create a PV on demand — no admin PV needed
**Explanation:** Two ways PVs come to exist: STATIC — the cluster admin manually creates PersistentVolume objects describing real storage (an NFS export, an EBS volume ID, a node dir); users' PVCs bind to them if criteria match. DYNAMIC — no matching static PV exists → the control plane asks a provisioner (via StorageClass) to CREATE a new PV+backing asset specifically for the PVC; requires the admin to have configured a StorageClass with a provisioner (e.g. ebs.csi.aws.com) and the DefaultStorageClass admission for defaulting. Dynamic is the modern default — users never wait for admin-created PVs.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/#provisioning" target="_blank">Kubernetes Docs - Provisioning</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794272619184 model:Basic -->
**Front:** Why does Kubernetes split storage into admin-managed PVs and user-facing PVCs instead of letting pods declare storage directly?
**Back:** Separation of duties, same pattern as the whole cloud-native design: the ADMIN owns cluster infrastructure — creating PVs that describe real storage (EBS volume IDs, NFS exports, node dirs), setting capacity/access modes/reclaim policy, deciding retention. Users shouldn't need to know (or be allowed to touch) cloud storage details — they just create a PVC saying 'I need 10Gi, ReadWriteOnce' and the binding machinery finds or provisions a match. Result: self-service storage for developers, centralized control + audit for admins, and pods stay portable because they reference claims, not vendor specifics.
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794272619191 model:Cloze -->
**Text:** A PersistentVolume spec — the admin-side storage object:<br><br>{{c1::<code>apiVersion: v1</code>}}<br>{{c2::<code>kind: PersistentVolume</code>}}<br>{{c3::<code>metadata:</code>}}<br>{{c4::<code>spec:</code>}}<br>  capacity:<br>    storage: {{c5::<code>10Gi</code>}}<br>  {{c6::<code>accessModes:</code>}}<br>    - {{c7::<code>ReadWriteOnce</code>}}<br>  {{c8::<code>persistentVolumeReclaimPolicy:</code>}} {{c9::<code>Retain</code>}}<br>  storageClassName: {{c10::<code>standard</code>}}<br>  csi:  # or nfs:/hostPath:/local: — the real backend
**Back Extra:** apiVersion: v1 + kind: PersistentVolume = core API group (not a CRD). Spec fields: capacity.storage (size like 10Gi), accessModes (RWO/ROX/RWX/RWOP), persistentVolumeReclaimPolicy (Retain/Delete/Recycle), storageClassName, claimRef (bound PVC), volumeMode (Filesystem/Block), and the backend: csi:/nfs:/hostPath:/local:. cluster-scoped — no namespace field.
**Tags:** k8s::kcna topic::storage topic::volumes topic::yaml src::session

---

<!-- note:1794273603210 model:Many -->
**Domain:** K8s Storage - PVC spec
**Question:** Which fields belong in a PersistentVolumeClaim spec? (Select all that apply)
**Options:** A. accessModes — how the volume can be mounted (RWO/ROX/RWX/RWOP)<br>B. hostPath — the node directory to mount<br>C. resources.requests.storage — how much storage to claim<br>D. storageClassName — which StorageClass/provisioner to use<br>E. containers — the pod spec to run<br>F. volumeMode — Filesystem or Block device
**Answer:** A, C, D, F – accessModes, resources.requests.storage, storageClassName, and volumeMode; B (selector) and E are also real fields — the trick is which are REQUIRED vs optional
**Explanation:** A PVC spec declares the CLAIM, not the storage: accessModes (how it can be mounted — required), resources.requests.storage (how much — required, e.g. 8Gi), volumeMode (Filesystem vs Block — optional, defaults Filesystem), storageClassName (which class/provisioner — optional but usually set), selector (label filter to pick a specific PV — optional), volumeName (pin to ONE exact PV — optional). Required = accessModes + resources.requests.storage; everything else steers WHICH PV binds. Namespaced object — PVCs live in your namespace, unlike cluster-scoped PVs.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims" target="_blank">Kubernetes Docs - PVCs</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794273603211 model:Many -->
**Domain:** K8s Storage - binding modes
**Question:** How can a PVC control WHICH PersistentVolume it binds to?
**Options:** A. PVCs can only bind automatically — no way to influence which PV<br>B. Three binding paths: automatic criteria matching (size/accessMode/class), selector label-matching to filter candidates, or volumeName to pin one exact PV<br>C. volumeName creates a new PV with that name<br>D. Selector matches PVCs to Pods, not PVs
**Answer:** B (2) – Three binding paths: automatic criteria matching (size/accessMode/class), selector label-matching to filter candidates, or volumeName to pin one exact PV
**Explanation:** A PVC finds its PV three ways: (1) AUTOMATIC — no selector/volumeName: the binding loop matches on capacity, accessModes, volumeMode, storageClassName; (2) SELECTOR — spec.selector.matchLabels/matchExpressions filter PVs by their labels (ANDed with the class requirement — only same-class AND label-matching PVs qualify); (3) VOLUME NAME — spec.volumeName pins the PVC to ONE specific PV (strongest binding; if that PV is already bound, the PVC sits Pending forever). Selector and volumeName are mutually exclusive ways to steer binding — automatic is the default when neither is set.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector" target="_blank">Kubernetes Docs - PVC Selector</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794273603212 model:Many -->
**Domain:** K8s Storage - selector gotcha
**Question:** Can a PVC with a spec.selector get a dynamically provisioned volume?
**Options:** A. Yes — the provisioner copies the selector labels onto the new PV<br>B. NO — a PVC with a non-empty selector cannot get a dynamically provisioned PV; it must bind to an existing matching PV<br>C. Yes — selectors only apply to static provisioning anyway<br>D. The selector is ignored during dynamic provisioning
**Answer:** B (2) – NO — a PVC with a non-empty selector cannot get a dynamically provisioned PV; it must bind to an existing matching PV
**Explanation:** Documented limitation: 'a PVC with a non-empty selector can't have a PV dynamically provisioned for it.' Rationale: dynamic provisioning creates a NEW PV on demand — but a selector says 'only bind me to a PV carrying THESE labels', and a freshly provisioned PV won't carry your custom labels (unless the provisioner supports label propagation via StorageClass parameters). So selector = opt into static/pre-labeled PVs only. If you need dynamic provisioning, leave selector empty and steer via storageClassName instead.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector" target="_blank">Kubernetes Docs - PVC Selector</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794273603213 model:Many -->
**Domain:** K8s Storage - volumeName
**Question:** What happens when a PVC sets volumeName to a PV that's already bound to another PVC?
**Options:** A. It binds to the next available PV automatically<br>B. It stays Pending — volumeName is a hard pin: if that PV is already bound to another PVC, this claim can never bind<br>C. It steals the PV from the other PVC<br>D. It fails immediately with an error event
**Answer:** B (2) – It stays Pending — volumeName is a hard pin: if that PV is already bound to another PVC, this claim can never bind
**Explanation:** spec.volumeName is the explicit-binding escape hatch: 'bind me to PV named X, period.' The docs warn: 'If the specified PV is already bound to another PVC, the binding will be stuck in a pending state' — volumeName doesn't queue or fall back to other PVs, it's a hard reference. Useful for pinning a pod to specific pre-provisioned storage (e.g. a manually created NFS PV), dangerous if you forget the PV is taken — the PVC just sits Pending with no obvious error. Automatic matching (no volumeName) would have found another PV.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/#volume-name" target="_blank">Kubernetes Docs - PVC Volume Name</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794273603214 model:Many -->
**Domain:** K8s Storage - PVC lifecycle
**Question:** What are the phases a PVC/PV pair goes through?
**Options:** A. Pending → Bound → Available → Deleted<br>B. Pending (unbound, searching) → Bound (matched to a PV) → Released (PVC deleted but resource not yet reclaimed) → Failed; Available is the PV's pre-binding state<br>C. Bound → Pending → Retained → Recycled<br>D. PVCs have no phases — only PVs do
**Answer:** B (2) – Pending (unbound, searching) → Bound (matched to a PV) → Released (PVC deleted but resource not yet reclaimed) → Failed; Available is the PV's pre-binding state
**Explanation:** Phase lifecycle: PVC starts PENDING — created but no matching PV yet (waiting for capacity/provisioning); flips BOUND when the control loop binds it to a PV (1:1, exclusive); on PVC deletion the PV enters RELEASED — 'the claim has been deleted, but the associated storage resource is not yet reclaimed' — the reclaim policy then acts (Retain → Available for reuse, Delete → gone); FAILED if something went wrong provisioning/mounting. Don't confuse the actors: these phases describe the CLAIM's view — the PV has its own status (Available/Bound/Released/Failed) tracking the other side of the binding.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/" target="_blank">Kubernetes Docs - PV/PVC Lifecycle</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794273603215 model:Many -->
**Domain:** K8s Storage - delete & reclaim
**Question:** What happens to the PV when you delete a PVC?
**Options:** A. kubectl delete pvc deletes the PV and all data automatically<br>B. kubectl delete pvc removes the CLAIM; the PV's reclaimPolicy decides the volume's fate — and the DEFAULT is Delete, not Retain as the lecture claimed<br>C. The PV always survives PVC deletion with Retain semantics<br>D. kubectl delete pvc --cascade=orphan is required to keep the volume
**Answer:** B (2) – kubectl delete pvc removes the CLAIM; the PV's reclaimPolicy decides the volume's fate — and the DEFAULT is Delete, not Retain as the lecture claimed
**Explanation:** CORRECTION to the lecture: 'by default it is set to retain' is WRONG — the default reclaim policy is DELETE. kubectl delete pvc only removes the claim object; the PV's persistentVolumeReclaimPolicy then acts: DELETE (default — dynamic PVs inherit it from StorageClass which defaults to Delete) removes the PV AND the backing asset (EBS volume gone!); RETAIN keeps PV+data — the PV goes Released, admin can manually reclaim (clear claimRef → PV becomes Available → a NEW PVC can bind it — so yes, others CAN reuse a Retained PV); RECYCLE scrubs contents (deprecated, only nfs/hostPath support it). So deleting a PVC can destroy real cloud storage — check reclaimPolicy first.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/#deleting-a-pvc" target="_blank">Kubernetes Docs - PV/PVC</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794273606342 model:Cloze -->
**Text:** A PersistentVolumeClaim — the user-side storage request:<br><br>{{c1::<code>apiVersion: v1</code>}}<br>{{c2::<code>kind: PersistentVolumeClaim</code>}}<br>{{c3::<code>metadata:</code>}}<br>{{c4::<code>spec:</code>}}<br>  {{c5::<code>accessModes:</code>}}<br>    - {{c6::<code>ReadWriteOnce</code>}}<br>  {{c7::<code>volumeMode:</code>}} {{c8::<code>Filesystem</code>}}<br>  resources:<br>    requests:<br>      storage: {{c9::<code>8Gi</code>}}<br>  storageClassName: {{c10::<code>slow</code>}}<br>  selector:<br>    matchLabels:<br>      release: {{c11::<code>"stable"</code>}}
**Back Extra:** Required: accessModes + resources.requests.storage. volumeMode defaults Filesystem (Block = raw device, no filesystem). selector + storageClassName are ANDed — and a non-empty selector BLOCKS dynamic provisioning. volumeName pins to one exact PV (stuck Pending if taken). storageClassName: "" = explicitly NO class (binds only classless PVs); missing = uses DefaultStorageClass if configured.
**Tags:** k8s::kcna topic::storage topic::volumes topic::yaml src::session

---

<!-- note:1794274357891 model:Many -->
**Domain:** K8s Storage - StorageClass
**Question:** What problem do StorageClasses solve?
**Options:** A. StorageClasses encrypt data at rest in etcd<br>B. StorageClasses enable DYNAMIC provisioning — a PVC's storageClassName triggers a provisioner to create the disk+PV automatically, no manual PV<br>C. StorageClasses replace PVCs with a simpler object<br>D. StorageClasses are only for local node storage
**Answer:** B (2) – StorageClasses enable DYNAMIC provisioning — a PVC's storageClassName triggers a provisioner to create the disk+PV automatically, no manual PV
**Explanation:** Static provisioning (the manual way): admin must create the real disk FIRST (GCP PD, AWS EBS, NFS export), then hand-write a PersistentVolume describing it, then users' PVCs bind to it — slow, error-prone, doesn't scale. StorageClasses solve it via DYNAMIC provisioning: admin defines a StorageClass ONCE naming a provisioner + parameters; a user creates ONLY a PVC with storageClassName + requested size; the external provisioner creates the backing disk AND the PV object automatically, then binds. Users never touch PVs — 'you do not need to write it.'
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/storage-classes/" target="_blank">Kubernetes Docs - Storage Classes</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794274357892 model:Many -->
**Domain:** K8s Storage - StorageClass spec
**Question:** What does a StorageClass object look like at the API level?
**Options:** A. apiVersion: v1, kind: StorageClass — namespaced per team<br>B. apiVersion: storage.k8s.io/v1, kind: StorageClass — a cluster-scoped object (not namespaced, admins define it once for everyone)<br>C. kind: PersistentVolumeClaimTemplate<br>D. apiVersion: storage.k8s.io/v1beta1 only
**Answer:** B (2) – apiVersion: storage.k8s.io/v1, kind: StorageClass — a cluster-scoped object (not namespaced, admins define it once for everyone)
**Explanation:** A StorageClass is apiVersion: storage.k8s.io/v1 (named API group — NOT v1 core, NOT a CRD you write yourself) + kind: StorageClass. It's CLUSTER-SCOPED: admins define classes once ('standard' = fast SSD, 'slow' = cheap HDD, 'encrypted' = encrypted volumes) and every namespace's PVCs can reference them by name via storageClassName. Think of it as a 'storage product catalog' — the class bundles provisioner + parameters + policies into a reusable profile users pick by name.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/storage-classes/" target="_blank">Kubernetes Docs - Storage Classes</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794274357893 model:Many -->
**Domain:** K8s Storage - provisioner
**Question:** What does the 'provisioner' field in a StorageClass do?
**Options:** A. provisioner is the Kubernetes node that hosts the volume<br>B. The provisioner names WHICH volume plugin creates the disks — internal ones (kubernetes.io/gce-pd) or external CSI provisioners (ebs.csi.aws.com, pd.csi.storage.gke.io)<br>C. provisioner specifies the pod that will mount the volume<br>D. provisioner is optional — Kubernetes picks one automatically
**Answer:** B (2) – The provisioner names WHICH volume plugin creates the disks — internal ones (kubernetes.io/gce-pd) or external CSI provisioners (ebs.csi.aws.com, pd.csi.storage.gke.io)
**Explanation:** spec.provisioner is the REQUIRED field — it names the volume plugin that does the actual provisioning. Two flavors: INTERNAL/built-in provisioners named kubernetes.io/<backend> (gce-pd, aws-ebs, azure-disk — legacy in-tree names) and EXTERNAL provisioners — independent programs following the external-provisioner spec, almost always CSI drivers (ebs.csi.aws.com for AWS EBS, pd.csi.storage.gke.io for GCP PD, efs.csi.aws.com…). Third parties can write their own external provisioners — storage vendors ship them as the CSI ecosystem matured; in-tree provisioners are deprecated in favor of CSI.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/storage-classes/" target="_blank">Kubernetes Docs - Storage Classes</a>
**Tags:** k8s::kcna topic::storage topic::volumes topic::csi src::session

---

<!-- note:1794274357894 model:Many -->
**Domain:** K8s Storage - parameters
**Question:** What are 'parameters' in a StorageClass?
**Options:** A. parameters are Kubernetes-wide settings applied to all classes<br>B. Provisioner-specific key-value options passed to the provisioner — e.g. type: pd-ssd, zones, iopsPerGB, fsType, encrypted — max 512 parameters<br>C. parameters must be identical across all StorageClasses<br>D. parameters configure pod resource requests
**Answer:** B (2) – Provisioner-specific key-value options passed to the provisioner — e.g. type: pd-ssd, zones, iopsPerGB, fsType, encrypted — max 512 parameters
**Explanation:** spec.parameters is a free-form map of options handed to the provisioner — each provisioner accepts its own keys: GCP PD takes type (pd-standard/pd-ssd/pd-balanced), zones, iopsPerGB?, fsType; AWS EBS takes type (gp2/gp3/io1/io2), iopsPerGB, encrypted, kmsKeyId, fsType; Azure takes skuName, kind, storageAccount. Omitted params get provisioner defaults. Limits: at most 512 parameters, and they're validated differently per provisioner — a param valid for EBS may be meaningless (or rejected) for PD. This is where 'fast SSD' vs 'cheap HDD' classes actually differ.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/storage-classes/" target="_blank">Kubernetes Docs - Storage Classes</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794274357895 model:Many -->
**Domain:** K8s Storage - class reclaimPolicy
**Question:** How does StorageClass.reclaimPolicy affect dynamically provisioned volumes?
**Options:** A. reclaimPolicy on the class overrides each PV's own setting permanently<br>B. The class's reclaimPolicy is INHERITED by every dynamically provisioned PV — Delete (default) destroys backing storage on PVC delete; Retain preserves it<br>C. reclaimPolicy: Retain is the default for all classes<br>D. reclaimPolicy applies only to static PVs, not dynamic ones
**Answer:** B (2) – The class's reclaimPolicy is INHERITED by every dynamically provisioned PV — Delete (default) destroys backing storage on PVC delete; Retain preserves it
**Explanation:** StorageClass.reclaimPolicy sets the default for all PVs it dynamically provisions: DELETE (the default when unspecified) — PVC deleted → PV + backing disk both destroyed; RETAIN — PVC deleted → PV+data survive for manual reclaim/reuse. This connects directly to the earlier gotcha: a PVC on a default class + kubectl delete pvc = your cloud disk GONE. For anything precious, either set reclaimPolicy: Retain on the class or verify before deleting claims. Only Delete/Retain are valid here — Recycle isn't allowed on classes.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/storage-classes/" target="_blank">Kubernetes Docs - Storage Classes</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794274357896 model:Many -->
**Domain:** K8s Storage - volumeBindingMode
**Question:** What is the difference between Immediate and WaitForFirstConsumer volumeBindingMode?
**Options:** A. Immediate waits for pod scheduling; WaitForFirstConsumer provisions instantly<br>B. Immediate (default) provisions at PVC creation — possibly in the WRONG zone; WaitForFirstConsumer waits until the pod is scheduled, then provisions in the pod's zone/topology<br>C. volumeBindingMode only affects static PVs<br>D. WaitForFirstConsumer requires NFS volumes
**Answer:** B (2) – Immediate (default) provisions at PVC creation — possibly in the WRONG zone; WaitForFirstConsumer waits until the pod is scheduled, then provisions in the pod's zone/topology
**Explanation:** volumeBindingMode controls WHEN provisioning happens: IMMEDIATE (default) — PV is provisioned the moment the PVC is created, BEFORE any pod exists. Problem: a zonal disk (EBS/GCE-PD) provisioned immediately may land in zone A while the pod later schedules in zone B → 'no available volume zone' / multi-attach errors (your earlier card!). WaitForFirstConsumer — the PVC stays Pending until a pod using it is scheduled; the provisioner then creates the volume IN THE POD'S ZONE/topology — the fix for zone-aware storage. Caveats: don't set nodeName in the pod spec (breaks the wait); allowedTopologies can further restrict zones.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/storage-classes/" target="_blank">Kubernetes Docs - Storage Classes</a>
**Tags:** k8s::kcna topic::storage topic::volumes topic::scheduling src::session

---

<!-- note:1794274357897 model:Many -->
**Domain:** K8s Storage - volume expansion
**Question:** What does allowVolumeExpansion do on a StorageClass?
**Options:** A. allowVolumeExpansion lets pods request more CPU<br>B. allowVolumeExpansion: true permits growing the PVC's storage request — the provisioner resizes the backing volume and filesystem online<br>C. Expansion works regardless of the class setting<br>D. allowVolumeExpansion shrinks volumes automatically
**Answer:** B (2) – allowVolumeExpansion: true permits growing the PVC's storage request — the provisioner resizes the backing volume and filesystem online
**Explanation:** allowVolumeExpansion: true on the StorageClass opts the class into PVC RESIZING: edit the PVC's resources.requests.storage upward (or kubectl patch) and Kubernetes asks the provisioner to grow the backing disk, then the node resizes the filesystem — online, no pod restart needed (filesystem must support online growth — ext4/xfs do). Requirements stack: class allows it AND provisioner supports expansion AND the volume plugin handles it. With it false/unset, PVC size is FROZEN at creation — plan capacity upfront or recreate.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/storage-classes/" target="_blank">Kubernetes Docs - Storage Classes</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794274357898 model:Many -->
**Domain:** K8s Storage - user flow
**Question:** What does a user actually create to get dynamically provisioned storage?
**Options:** A. User must create the PV first, then the PVC<br>B. User creates only a PVC naming the class + size — provisioner creates disk+PV, binds, pod mounts it; the PV object exists but was never hand-written<br>C. User creates a Pod with a storageClass field directly<br>D. The admin creates a PV for every expected PVC manually
**Answer:** B (2) – User creates only a PVC naming the class + size — provisioner creates disk+PV, binds, pod mounts it; the PV object exists but was never hand-written
**Explanation:** The dynamic-provisioning user experience: (1) admin defines StorageClass once; (2) user applies a PVC with storageClassName: fast + resources.requests.storage: 10Gi; (3) PVC goes Pending briefly; (4) the external-provisioner sees it, calls the CSI CreateVolume RPC, the cloud disk appears, a PV object is auto-created describing it; (5) binding loop binds PVC↔PV; (6) pod mounts via persistentVolumeClaim.claimName. The user NEVER writes PV YAML — that's the entire point. kubectl get pv shows the auto-created PV with labels like failure-domain.beta.kubernetes.io/zone.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/storage-classes/" target="_blank">Kubernetes Docs - Storage Classes</a>
**Tags:** k8s::kcna topic::storage topic::volumes src::session

---

<!-- note:1794274362470 model:Cloze -->
**Text:** A StorageClass — the admin-side dynamic-provisioning profile:<br><br>{{c1::<code>apiVersion: storage.k8s.io/v1</code>}}<br>{{c2::<code>kind: StorageClass</code>}}<br>{{c3::<code>metadata:</code>}}<br>{{c4::<code>provisioner:</code>}} {{c5::<code>pd.csi.storage.gke.io</code>}}<br>{{c6::<code>parameters:</code>}}<br>  type: {{c7::<code>pd-ssd</code>}}<br>  {{c8::<code>reclaimPolicy:</code>}} {{c9::<code>Delete</code>}}<br>  {{c10::<code>volumeBindingMode:</code>}} {{c11::<code>WaitForFirstConsumer</code>}}<br>  {{c12::<code>allowVolumeExpansion:</code>}} {{c13::<code>true</code>}}
**Back Extra:** provisioner = REQUIRED (which plugin creates disks: kubernetes.io/gce-pd legacy, or CSI like ebs.csi.aws.com/pd.csi.storage.gke.io). parameters = provisioner-specific (type, zones, iopsPerGB, fsType, encrypted — max 512). reclaimPolicy Delete(default)/Retain — inherited by dynamically created PVs. volumeBindingMode Immediate(default)/WaitForFirstConsumer (provision in pod's zone). allowVolumeExpansion true = PVC resizable. mountOptions = filesystem mount flags.
**Tags:** k8s::kcna topic::storage topic::volumes topic::yaml src::session

---
