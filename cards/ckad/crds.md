# CKAD - Certified Kubernetes Application Developer — crds

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `crds` · Notes: 7 · Models: Basic++++

<!-- note:1781279834544 model:Basic++++ -->
**Front:** What is a CRD?
**Back:** A CustomResourceDefinition adds a new Kubernetes API resource type to the cluster.
**Tags:** ckad::crds concept

---

<!-- note:1781279834545 model:Basic++++ -->
**Front:** What is a custom resource?
**Back:** An instance of a resource type defined by a CRD.
**Tags:** ckad::crds concept

---

<!-- note:1781279834547 model:Basic++++ -->
**Front:** Command: list CRDs.
**Back:** kubectl get crd
**Tags:** ckad::crds command

---

<!-- note:1781279834548 model:Basic++++ -->
**Front:** Command: list API resources.
**Back:** kubectl api-resources
**Tags:** ckad::crds command

---

<!-- note:1781279834549 model:Basic++++ -->
**Front:** Command: list API versions.
**Back:** kubectl api-versions
**Tags:** ckad::crds command

---

<!-- note:1781279834550 model:Basic++++ -->
**Front:** Command: explain a custom resource if installed.
**Back:** kubectl explain &lt;custom-resource-kind&gt;.spec
**Tags:** ckad::crds command yaml

---

<!-- note:1781279834551 model:Basic++++ -->
**Front:** How should you approach an unfamiliar custom resource in CKAD?
**Back:** Use kubectl api-resources, kubectl explain, existing examples, and describe/events; treat it like normal Kubernetes YAML.
**Tags:** ckad::crds debugging

---
