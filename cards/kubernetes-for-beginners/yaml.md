# Kubernetes for Beginners — yaml

> Deck: `Kubernetes for Beginners` · Group: `yaml` · Notes: 10 · Models: Basic, Basic (and reversed card), Cloze, Many

<!-- note:1793718827409 model:Basic -->
**Front:** What is a manifest file in Kubernetes and what is it used for?
**Back:** A manifest is a YAML file (JSON is also accepted) that declaratively describes a Kubernetes object — such as a Pod, Service, or Deployment — and its desired state. You submit it with <code>kubectl apply -f file.yaml</code> and the control plane continuously works to make the cluster match what the file describes.
**Tags:** k8s::beginners topic::api topic::yaml src::session

---

<!-- note:1793718827410 model:Basic -->
**Front:** What does the <code>apiVersion</code> field in a manifest specify, and how does it map to core vs named API groups?
**Back:** <code>apiVersion</code> names which version of the Kubernetes API is used to create the object, written <code>&lt;group&gt;/&lt;version&gt;</code> for named API groups or just <code>&lt;version&gt;</code> for the core group (which has no name). So <code>apiVersion: v1</code> = core API group (Pod, Service); <code>apiVersion: apps/v1</code> = named group 'apps', version v1 (Deployment, ReplicaSet); <code>batch/v1</code> = group 'batch' (Job).
**Tags:** k8s::beginners topic::api topic::yaml src::session

---

<!-- note:1793718827411 model:Basic -->
**Front:** What goes into the <code>metadata</code> field of a Kubernetes manifest?
**Back:** Data that uniquely identifies the object: at minimum <code>metadata.name</code>; optionally <code>namespace</code>, <code>labels</code> and <code>annotations</code>. The cluster also fills in a <code>uid</code>. Metadata is about the object's identity — not its behavior (that's <code>spec</code>).
**Tags:** k8s::beginners topic::api topic::yaml src::session

---

<!-- note:1793718827412 model:Basic -->
**Front:** What kind of information goes into the <code>spec</code> field of a manifest?
**Back:** <code>spec</code> holds the object's desired state — its full configuration. What lands there depends on the kind: a Pod spec lists <code>containers</code> (image, ports, env, resources); a Deployment spec has <code>replicas</code>, <code>selector</code> and a pod <code>template</code>; a Service spec has <code>selector</code> and <code>ports</code>. The control plane continuously works to make the object's <code>status</code> (current state, written by the cluster) match this spec.
**Tags:** k8s::beginners topic::api topic::yaml src::session

---

<!-- note:1793718827413 model:Basic -->
**Front:** Why do the fields under <code>spec</code> differ between a Pod manifest and a Deployment manifest?
**Back:** Because the spec schema is defined per <code>kind</code> — each object type has its own set of allowed fields under <code>spec</code>. There is no universal spec format; you look up the valid fields for the specific kind in the Kubernetes API reference (e.g. the Pod spec page vs the StatefulSet spec page).
**Tags:** k8s::beginners topic::api topic::yaml src::session

---

<!-- note:1793718827420 model:Basic (and reversed card) -->
**Front:** Which four top-level fields must every Kubernetes object manifest contain?
**Back:** <code>apiVersion</code>, <code>kind</code>, <code>metadata</code> and <code>spec</code>. (<code>status</code> also appears on live objects, but the cluster writes it — it is not required in the file you submit.)
**Tags:** k8s::beginners topic::api topic::yaml src::session

---

<!-- note:1793718827421 model:Basic (and reversed card) -->
**Front:** In a Kubernetes manifest, what does the <code>kind</code> field specify?
**Back:** The type of object you want to create — e.g. <code>Pod</code>, <code>Service</code>, <code>Deployment</code>, <code>StatefulSet</code>, <code>Job</code>. The kind also determines which fields are valid under <code>spec</code>, since each kind has its own spec schema.
**Tags:** k8s::beginners topic::api topic::yaml src::session

---

<!-- note:1793718827429 model:Cloze -->
**Text:** A minimal Pod manifest:<br><br><code>apiVersion: {{c1::v1}}<br>kind: {{c2::Pod}}<br>{{c3::metadata}}:<br>&nbsp;&nbsp;name: nginx<br>{{c4::spec}}:<br>&nbsp;&nbsp;containers:</code>
**Back Extra:** apiVersion + kind say what to create and through which API (Pods are in the core group, hence plain <code>v1</code>); metadata identifies the object; spec is the desired state, with a schema specific to the kind.
**Tags:** k8s::beginners topic::pods topic::yaml src::session

---

<!-- note:1793718827443 model:Many -->
**Domain:** Object Model
**Question:** Which of these is NOT one of the four required top-level fields of a Kubernetes manifest?
**Options:** A. apiVersion<br>B. kind<br>C. status<br>D. spec
**Answer:** C (3) – status
**Explanation:** The four required top-level fields are apiVersion, kind, metadata and spec. status does exist on live objects, but it is supplied and updated by the Kubernetes control plane to record the object's current state — you never write it into the manifest you submit.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/" target="_blank">Kubernetes Documentation - Objects In Kubernetes</a>
**Tags:** k8s::beginners topic::api topic::yaml src::session

---

<!-- note:1793718827444 model:Many -->
**Domain:** Object Model
**Question:** A manifest starts with <code>apiVersion: apps/v1</code>. What does this value encode?
**Options:** A. The object is version 1 of an application<br>B. The named API group 'apps', version v1<br>C. The object belongs to the core API group<br>D. The cluster must run Kubernetes version 1
**Answer:** B (2) – The named API group 'apps', version v1
**Explanation:** apiVersion encodes <group>/<version> for named API groups and just <version> (v1) for the core API group, which has no name. 'apps' is the named group that holds Deployments, ReplicaSets, StatefulSets and DaemonSets; core-group kinds like Pod and Service use plain apiVersion: v1. It selects the API endpoint — it has nothing to do with application versioning.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/" target="_blank">Kubernetes Documentation - Objects In Kubernetes</a>
**Tags:** k8s::beginners topic::api topic::yaml src::session

---
