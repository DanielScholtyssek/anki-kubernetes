# Kubernetes for Beginners — replicasets

> Deck: `Kubernetes for Beginners` · Group: `replicasets` · Notes: 14 · Models: Basic, Basic (and reversed card), Cloze, Many

<!-- note:1793721354687 model:Basic -->
**Front:** What problem does a ReplicaSet solve — why not just create Pods directly?
**Back:** It guarantees that a specified number of pod replicas are running at any given time. Without it, a pod that crashes or is deleted is just gone; the ReplicaSet controller continuously compares desired count (<code>spec.replicas</code>) with actual pods and creates replacements from its pod template — or removes extras if there are too many.
**Tags:** k8s::beginners topic::pods topic::replicasets src::session

---

<!-- note:1793721354688 model:Basic -->
**Front:** How does a ReplicaSet provide high availability for an application?
**Back:** High availability = the app keeps serving even when individual pods or nodes fail. A ReplicaSet delivers this by keeping N identical pods running and replacing any that die — the scheduler places replacement pods on surviving nodes, so losing one node doesn't take the application down while replicas remain elsewhere.
**Tags:** k8s::beginners topic::ha topic::replicasets src::session

---

<!-- note:1793721354689 model:Basic -->
**Front:** How do ReplicaSets enable scaling and load balancing of pods?
**Back:** Scaling: raising <code>spec.replicas</code> (e.g. <code>kubectl scale rs/name --replicas=5</code>) makes the controller create more pod copies, spread across cluster nodes. Load balancing: a Service in front of those pods distributes traffic across all matching replicas. The ReplicaSet keeps the pool at the right size; the Service spreads the load.
**Tags:** k8s::beginners topic::pods topic::replicasets src::session

---

<!-- note:1793721354690 model:Basic -->
**Front:** What is the difference between a ReplicationController and a ReplicaSet?
**Back:** Same purpose — keep N pod replicas running — but ReplicationController is the legacy predecessor, superseded by ReplicaSet (and Deployment on top). Practical difference: ReplicationController selectors are equality-based only, while ReplicaSet supports set-based selectors (<code>matchExpressions</code>, e.g. <code>tier in (frontend, backend)</code>) in addition to <code>matchLabels</code>. New work uses ReplicaSet — usually indirectly via Deployment.
**Tags:** k8s::beginners topic::pods topic::replicasets src::session

---

<!-- note:1793721354691 model:Basic -->
**Front:** Can a ReplicaSet manage pods it did not create itself?
**Back:** Yes — a ReplicaSet counts every pod matching its <code>spec.selector</code>, not only pods from its template. An unowned pod (no controller in <code>metadata.ownerReferences</code>) with matching labels gets adopted and counted toward the replica total; if that pushes the count above <code>spec.replicas</code>, the ReplicaSet terminates the extras.
**Tags:** k8s::beginners topic::pods topic::replicasets src::session

---

<!-- note:1793721354698 model:Basic (and reversed card) -->
**Front:** In Kubernetes, what is a replica?
**Back:** One of several identical copies of a pod running the same application. Replicas give an app redundancy (one can die without outage) and capacity (traffic spreads across many copies).
**Tags:** k8s::beginners topic::pods topic::replicasets src::session

---

<!-- note:1793721354699 model:Basic (and reversed card) -->
**Front:** What does <code>spec.selector</code> do in a ReplicaSet, and what must it match?
**Back:** The required label selector (usually <code>spec.selector.matchLabels</code>) that identifies which pods the ReplicaSet counts and owns. Rule: the labels in <code>spec.template.metadata.labels</code> must match the selector, or the API rejects the manifest.
**Tags:** k8s::beginners topic::pods topic::replicasets src::session

---

<!-- note:1793721354707 model:Cloze -->
**Text:** Minimal ReplicaSet manifest:<br><br><code>apiVersion: {{c1::apps/v1}}<br>kind: {{c2::ReplicaSet}}<br>metadata:<br>&nbsp;&nbsp;name: frontend<br>spec:<br>&nbsp;&nbsp;{{c3::replicas}}: 3<br>&nbsp;&nbsp;{{c4::selector}}:<br>&nbsp;&nbsp;&nbsp;&nbsp;matchLabels:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tier: frontend<br>&nbsp;&nbsp;template: &lt;pod template&gt;</code>
**Back Extra:** ReplicaSet lives in the named API group 'apps' (hence apps/v1). replicas = desired count; selector.matchLabels links it to pods; template is the pod blueprint it stamps out when the actual count is low.
**Tags:** k8s::beginners topic::replicasets topic::yaml src::session

---

<!-- note:1793721354720 model:Many -->
**Domain:** Workloads
**Question:** Which field in a ReplicaSet manifest determines which pods it manages?
**Options:** A. metadata.name<br>B. spec.selector (matchLabels)<br>C. spec.replicas<br>D. apiVersion
**Answer:** B (2) – spec.selector (matchLabels)
**Explanation:** The selector is a required field — usually spec.selector.matchLabels — and it must equal spec.template.metadata.labels or the API rejects the manifest. replicas says how many pods to keep; it does not identify which ones. Ownership is recorded on the pod side in metadata.ownerReferences.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/" target="_blank">Kubernetes Documentation - ReplicaSet</a>
**Tags:** k8s::beginners topic::pods topic::replicasets src::session

---

<!-- note:1793721354721 model:Many -->
**Domain:** Workloads
**Question:** A ReplicaSet wants 4 replicas and a node hosting one of them dies. What happens next?
**Options:** A. Nothing — it waits for the node to come back<br>B. It restarts the surviving pods<br>C. The ReplicaSet creates a replacement pod on a surviving node<br>D. kubectl must be run manually to recreate the pod
**Answer:** C (3) – The ReplicaSet creates a replacement pod on a surviving node
**Explanation:** The controller constantly reconciles desired (4) vs actual (now 3) pods and stamps out a new pod from spec.template; the scheduler places it on a healthy node. Meanwhile the 3 surviving replicas keep serving traffic — that is the high-availability role of replication.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/" target="_blank">Kubernetes Documentation - ReplicaSet</a>
**Tags:** k8s::beginners topic::ha topic::replicasets src::session

---

<!-- note:1793722394260 model:Basic -->
**Front:** Why must a ReplicaSet manifest always include <code>spec.template</code>, even if matching pods already exist?
**Back:** Because the template is the pod blueprint the ReplicaSet stamps out whenever actual < desired replicas. Without it the controller wouldn't know what to create — image, ports, labels — so the API requires it even when matching pods already exist. Its <code>template.metadata.labels</code> must also match <code>spec.selector</code>, or creation is rejected.
**Tags:** k8s::beginners topic::pods topic::replicasets src::session

---

<!-- note:1793722394261 model:Basic -->
**Front:** What are the two ways to change a ReplicaSet's replica count, and which is safe for GitOps?
**Back:** Declarative (GitOps-safe): edit <code>spec.replicas</code> in the YAML manifest and <code>kubectl apply -f</code> — git stays the source of truth. Imperative: <code>kubectl scale --replicas=5 rs/frontend</code> (or <code>--replicas=5 -f file.yaml</code>, which overrides the file's count) — changes only the live object, so the manifest drifts and the next apply/sync silently reverts the scale.
**Tags:** k8s::beginners topic::gitops topic::replicasets src::session

---

<!-- note:1793722394308 model:Cloze -->
**Text:** Scale the 'frontend' ReplicaSet to 5 replicas imperatively:<br><br><code>kubectl scale {{c1::--replicas=5}} {{c2::rs}}/frontend</code>
**Back Extra:** Imperative scaling — changes only the live object. rs is the short name for replicaset; <code>-f file.yaml</code> works instead of TYPE/NAME. For GitOps, edit spec.replicas in the manifest and apply instead, or the next sync reverts this.
**Tags:** k8s::beginners topic::gitops topic::replicasets src::session

---

<!-- note:1793722402526 model:Many -->
**Domain:** ReplicaSets
**Question:** Your team stores manifests in git (GitOps). A colleague runs <code>kubectl scale --replicas=8 rs/web</code> for a traffic spike. What's the risk?
**Options:** A. Nothing — the change persists forever<br>B. git still holds the old count, so the next apply/sync reverts it<br>C. kubectl scale cannot target ReplicaSets<br>D. The ReplicaSet gets deleted and recreated
**Answer:** B (2) – git still holds the old count, so the next apply/sync reverts it
**Explanation:** kubectl scale patches the live object only — the manifest in git still says the old spec.replicas. GitOps treats git as the source of truth, so the next apply or controller sync restores the old count. The safe way is to edit spec.replicas in the YAML, commit, and apply.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/generated/kubectl_scale/" target="_blank">Kubernetes Documentation - kubectl scale</a>
**Tags:** k8s::beginners topic::gitops topic::replicasets src::session

---
