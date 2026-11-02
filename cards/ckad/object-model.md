# CKAD - Certified Kubernetes Application Developer — object-model

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `object-model` · Notes: 9 · Models: Basic++++

<!-- note:1781279834169 model:Basic++++ -->
**Front:** What are the five common top-level fields in Kubernetes YAML?
**Back:** apiVersion, kind, metadata, spec, status.
**Tags:** ckad::object-model yaml

---

<!-- note:1781279834170 model:Basic++++ -->
**Front:** What does apiVersion define?
**Back:** The API group and version for the object, such as v1, apps/v1, batch/v1, networking.k8s.io/v1.
**Tags:** ckad::object-model yaml

---

<!-- note:1781279834171 model:Basic++++ -->
**Front:** What does kind define?
**Back:** The type of Kubernetes object, such as Pod, Deployment, Service, Job, or NetworkPolicy.
**Tags:** ckad::object-model yaml

---

<!-- note:1781279834172 model:Basic++++ -->
**Front:** What does metadata define?
**Back:** Object identity and organisation: name, namespace, labels, annotations, ownerReferences, and similar metadata.
**Tags:** ckad::object-model yaml

---

<!-- note:1781279834173 model:Basic++++ -->
**Front:** What does spec define?
**Back:** The desired state you want Kubernetes to maintain.
**Tags:** ckad::object-model yaml

---

<!-- note:1781279834174 model:Basic++++ -->
**Front:** What does status define?
**Back:** The current observed state written by Kubernetes controllers; usually do not write it in exam manifests.
**Tags:** ckad::object-model yaml

---

<!-- note:1781279834175 model:Basic++++ -->
**Front:** Minimal YAML skeleton for any Kubernetes object?
**Back:** apiVersion: &lt;version&gt;<br>kind: &lt;Kind&gt;<br>metadata:<br>  name: &lt;name&gt;<br>spec:<br>  ...
**Tags:** ckad::object-model yaml

---

<!-- note:1781279834176 model:Basic++++ -->
**Front:** What is the difference between desired state and observed state?
**Back:** Desired state is spec; observed state is status. Controllers continuously try to make status match spec.
**Tags:** ckad::object-model concept

---

<!-- note:1781279834177 model:Basic++++ -->
**Front:** What is a controller in Kubernetes?
**Back:** A control loop that watches objects and reconciles actual state toward desired state, e.g. Deployment controller creates ReplicaSets and Pods.
**Tags:** ckad::object-model concept

---
