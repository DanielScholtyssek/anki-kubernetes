# CKAD - Certified Kubernetes Application Developer — limitrange

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `limitrange` · Notes: 2 · Models: Basic++++

<!-- note:1781279834331 model:Basic++++ -->
**Front:** What is a LimitRange?
**Back:** A namespace object that sets default, minimum, or maximum resource requests/limits for containers or Pods.
**Tags:** ckad::limitrange concept

---

<!-- note:1781279834332 model:Basic++++ -->
**Front:** YAML: LimitRange default container request/limit.
**Back:** apiVersion: v1<br>kind: LimitRange<br>metadata:<br>  name: limits<br>spec:<br>  limits:<br>  - type: Container<br>    defaultRequest:<br>      cpu: 100m<br>      memory: 128Mi<br>    default:<br>      cpu: 500m<br>      memory: 256Mi
**Tags:** ckad::limitrange yaml

---
