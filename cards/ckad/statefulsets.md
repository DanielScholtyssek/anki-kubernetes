# CKAD - Certified Kubernetes Application Developer — statefulsets

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `statefulsets` · Notes: 4 · Models: Basic++++

<!-- note:1781279834437 model:Basic++++ -->
**Front:** What is a StatefulSet?
**Back:** A controller for stateful apps needing stable network identity, ordered rollout, and stable per-Pod storage.
**Tags:** ckad::statefulsets concept

---

<!-- note:1781279834438 model:Basic++++ -->
**Front:** What naming pattern do StatefulSet Pods use?
**Back:** &lt;statefulset-name&gt;-0, &lt;statefulset-name&gt;-1, etc.
**Tags:** ckad::statefulsets concept

---

<!-- note:1781279834439 model:Basic++++ -->
**Front:** What is serviceName used for in a StatefulSet?
**Back:** It links the StatefulSet to a headless Service for stable network identity.
**Tags:** ckad::statefulsets concept services

---

<!-- note:1781279834440 model:Basic++++ -->
**Front:** Command: list StatefulSets.
**Back:** kubectl get statefulsets
**Tags:** ckad::statefulsets command

---
