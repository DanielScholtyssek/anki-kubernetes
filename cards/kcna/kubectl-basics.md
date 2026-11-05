<!-- note:1793754672883 model:Many -->
**Domain:** kubectl explain
**Question:** Which kubectl command shows documentation for a resource's fields, e.g. <code>kubectl explain pod.spec.containers</code>?
**Options:** A. kubectl describe<br>B. kubectl explain<br>C. kubectl doc<br>D. kubectl get -o yaml
**Answer:** B (2) – kubectl explain
**Explanation:** kubectl explain prints the schema/documentation for a resource's fields — e.g. kubectl explain deployment.spec.strategy describes every field, its type and meaning. It's the built-in way to answer 'what does this manifest field do' without leaving the terminal.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/generated/kubectl_explain/" target="_blank">Kubernetes Documentation - kubectl explain</a>
**Tags:** k8s::kcna topic::kubectl topic::yaml src::session

---

<!-- note:1793754672884 model:Many -->
**Domain:** Manifest Structure
**Question:** Which four top-level fields are required in every Kubernetes object manifest?
**Options:** A. name, image, replicas, port<br>B. apiVersion, metadata, spec, status<br>C. apiVersion, kind, metadata and spec<br>D. kind, spec, status, data
**Answer:** C (3) – apiVersion, kind, metadata and spec
**Explanation:** Every manifest needs all four top-level fields: apiVersion (API group+version, e.g. apps/v1), kind (object type → its schema), metadata (name/namespace/labels), spec (the desired state — its contents depend on the kind). status exists too but is written by Kubernetes, not required in your file.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/" target="_blank">Kubernetes Documentation - Objects In Kubernetes</a>
**Tags:** k8s::kcna topic::api topic::yaml src::session

---

<!-- note:1793754672885 model:Many -->
**Domain:** kubectl run
**Question:** Which command creates a pod named 'nginx' running the nginx image?
**Options:** A. kubectl create pod nginx<br>B. kubectl run nginx --image=nginx<br>C. kubectl deploy nginx --image=nginx<br>D. kubectl start nginx --image=nginx
**Answer:** B (2) – kubectl run nginx --image=nginx
**Explanation:** kubectl run creates a single pod; --image names the container image to pull (Docker Hub by default — use a full registry path for private repos). Note: kubectl create has NO pod subcommand (only deployment, service, job, etc.) — pods are created via kubectl run or a manifest with kubectl create/apply -f. deploy/start are not pod commands.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/pods/" target="_blank">Kubernetes Documentation - Pods</a>
**Tags:** k8s::kcna topic::kubectl topic::pods src::session

---

<!-- note:1793754672890 model:Cloze -->
**Text:** Minimal pod manifest:<br><br><code>apiVersion: {{c1::v1}}<br>kind: {{c2::Pod}}<br>metadata:<br>&nbsp;&nbsp;{{c3::name}}: nginx<br>spec:<br>&nbsp;&nbsp;{{c4::containers}}:<br>&nbsp;&nbsp;- name: nginx<br>&nbsp;&nbsp;&nbsp;&nbsp;{{c5::image}}: nginx</code>
**Back Extra:** v1 = core API group (named groups use group/version, e.g. apps/v1 for Deployments). metadata.name is how you identify the pod; spec.containers is a LIST (note the dash) — even a single-container pod needs the list item.
**Tags:** k8s::kcna topic::pods topic::yaml src::session

---

<!-- note:1793754672900 model:Basic -->
**Front:** How do you list pods with kubectl, and what do the flags <code>-o wide</code>, <code>-A</code> and <code>-w</code> add?
**Back:** <code>kubectl get pods</code> lists pods in the current namespace with status. Useful variants: <code>-o wide</code> (adds pod IPs + which node each runs on), <code>-A</code>/<code>--all-namespaces</code> (every namespace), <code>-w</code> (watch for changes). For detail on one pod incl. events: <code>kubectl describe pod &lt;name&gt;</code>.
**Tags:** k8s::kcna topic::kubectl topic::pods src::session

---

<!-- note:1793755549227 model:Many -->
**Domain:** Imperative vs Declarative - apply
**Question:** Which of these is the DECLARATIVE object-management approach in Kubernetes?
**Options:** A. kubectl create deployment web --image=nginx<br>B. kubectl replace -f deployment.yaml<br>C. kubectl apply -f deployment.yaml<br>D. kubectl edit deployment web
**Answer:** C (3) – kubectl apply -f deployment.yaml
**Explanation:** apply -f is the DECLARATIVE path: it merges the file's desired state into the live object and records last-applied-configuration to compute future diffs. create/replace -f are the middle tier ('imperative object configuration' — file-driven but verb-led: create fails if it exists, replace swaps the whole object). create/edit/run/expose are pure imperative commands.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna topic::kubectl topic::yaml src::session

---

<!-- note:1793755549228 model:Many -->
**Domain:** Imperative vs Declarative - commands
**Question:** Which group contains ONLY imperative commands (no manifest file involved)?
**Options:** A. kubectl run, kubectl create deployment, kubectl expose<br>B. kubectl apply -f, kubectl diff<br>C. kubectl create -f, kubectl replace -f<br>D. kubectl get, kubectl describe
**Answer:** A (1) – kubectl run, kubectl create deployment, kubectl expose
**Explanation:** Imperative commands tell the cluster WHAT to do right now: run, create deployment, expose, scale, delete — no file, no recorded desired state. The -f variants of create/replace are imperative object configuration (middle tier); apply -f is the declarative tier. get/describe are read-only, not management.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna topic::kubectl topic::yaml src::session

---

<!-- note:1793755549229 model:Many -->
**Domain:** Imperative vs Declarative - why
**Question:** Why is the declarative approach preferred for production and GitOps workflows?
**Options:** A. It executes faster than imperative commands<br>B. Manifests live in Git as a reviewable source of truth, and apply is idempotent and detects drift via last-applied-configuration<br>C. Imperative commands cannot create objects<br>D. The API server only accepts YAML
**Answer:** B (2) – Manifests live in Git as a reviewable source of truth, and apply is idempotent and detects drift via last-applied-configuration
**Explanation:** Declarative YAML can be versioned, reviewed and audited in Git (the GitOps model), re-applied safely (idempotent), and apply's last-applied annotation reveals drift. Imperative commands leave no record — nothing to diff, review or re-converge from.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna topic::gitops topic::kubectl src::session

---

<!-- note:1793756257574 model:Basic (and reversed card) -->
**Front:** What is the IMPERATIVE approach to managing infrastructure or Kubernetes objects?
**Back:** The approach where you spell out WHAT you want AND HOW to get there — every step explicitly, in order (<code>run this</code>, <code>create that</code>, <code>scale this to 5</code>). The tool executes commands; it doesn't reason about an end state. Examples: kubectl run/create/expose/scale/edit/set image — and shell scripts in the DevOps world.
**Tags:** k8s::kcna topic::declarative topic::kubectl src::session

---

<!-- note:1793756257575 model:Basic (and reversed card) -->
**Front:** What is the DECLARATIVE approach to managing infrastructure or Kubernetes objects?
**Back:** The approach where you describe only WHAT the end state should look like — a manifest of desired state — and the system works out the HOW itself (diff, plan, reconcile). Examples: <code>kubectl apply -f</code>, Terraform plans, Kubernetes controllers converging actual→desired state.
**Tags:** k8s::kcna topic::declarative topic::kubectl src::session

---

<!-- note:1793756257583 model:Many -->
**Domain:** Imperative vs Declarative - DevOps
**Question:** You write a Terraform config describing what infrastructure SHOULD exist, and Terraform works out the steps to reach it. Which approach is this?
**Options:** A. Imperative<br>B. Declarative<br>C. Procedural<br>D. Manual
**Answer:** B (2) – Declarative
**Explanation:** Terraform is the classic declarative IaC tool: you write config describing the END state (which resources should exist), and Terraform's engine computes the plan — what to create/change/destroy to get there. Same model as kubectl apply. Imperative tools/scripts instead encode each step to execute.
**Sources:** <a href="https://developer.hashicorp.com/terraform/intro" target="_blank">HashiCorp Documentation - What is Terraform</a>
**Tags:** k8s::kcna topic::declarative topic::gitops src::session

---

<!-- note:1793756257584 model:Many -->
**Domain:** Imperative vs Declarative - set image
**Question:** <code>kubectl set image deployment/web nginx=nginx:2.0</code> — which management approach is this?
**Options:** A. A declarative update<br>B. Imperative object configuration<br>C. An imperative command — it directly instructs the cluster to change the image NOW, with no declared desired state<br>D. A GitOps operation
**Answer:** C (3) – An imperative command — it directly instructs the cluster to change the image NOW, with no declared desired state
**Explanation:** set image, like run/create/expose/scale/edit/delete, is imperative: one-shot instruction, nothing recorded to converge against. The declarative equivalent is editing the image in the manifest and re-running kubectl apply -f.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna topic::declarative topic::kubectl src::session

---

<!-- note:1793756257585 model:Many -->
**Domain:** Imperative vs Declarative - apply mechanics
**Question:** You run <code>kubectl apply -f app.yaml</code> on an object that already exists. What does apply do?
**Options:** A. It fails because the resource already exists<br>B. It compares the manifest, the live object AND last-applied-configuration, then applies only the needed changes (create or patch)<br>C. It deletes and recreates the object from scratch<br>D. It replaces the whole object, losing unmanaged fields
**Answer:** B (2) – It compares the manifest, the live object AND last-applied-configuration, then applies only the needed changes (create or patch)
**Explanation:** apply is a three-way merge: file's desired state vs the object's live state vs the recorded last-applied-configuration. Object missing → created; exists → patched to match the declaration. That's why the same file can be applied repeatedly and why it's the declarative workflow.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna topic::declarative topic::kubectl src::session

---

<!-- note:1793756257586 model:Many -->
**Domain:** Imperative vs Declarative - contrast
**Question:** Which statement correctly contrasts the imperative and declarative approaches?
**Options:** A. Imperative describes the end state; declarative lists the steps<br>B. Imperative = you specify WHAT you want AND HOW (the steps); declarative = you specify only WHAT the result should be<br>C. They are two names for the same workflow<br>D. Declarative requires typing more commands
**Answer:** B (2) – Imperative = you specify WHAT you want AND HOW (the steps); declarative = you specify only WHAT the result should be
**Explanation:** Imperative: the operator encodes the path — every command/step explicitly. Declarative: the operator encodes the destination — the system derives the path (diff + reconcile). Kubernetes manifests+apply and Terraform are declarative; ad-hoc kubectl commands and shell scripts are imperative.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna topic::declarative topic::kubectl src::session

---

<!-- note:1793756656941 model:Many -->
**Domain:** kubectl apply - last-applied
**Question:** What does the <code>kubectl.kubernetes.io/last-applied-configuration</code> annotation on an object store?
**Options:** A. The object's current live spec<br>B. The JSON of the manifest most recently applied via kubectl apply<br>C. The default values the API server filled in<br>D. The object's original creation manifest from any tool
**Answer:** B (2) – The JSON of the manifest most recently applied via kubectl apply
**Explanation:** Each apply writes the applied manifest (as JSON) into the kubectl.kubernetes.io/last-applied-configuration annotation on the object. It's the third leg of apply's three-way merge — file vs live vs last-applied — letting kubectl compute diffs, detect drift, and delete fields removed from the file. kubectl get -o yaml shows LIVE state; this annotation remembers what YOU declared.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna topic::declarative topic::kubectl topic::yaml src::session

---

