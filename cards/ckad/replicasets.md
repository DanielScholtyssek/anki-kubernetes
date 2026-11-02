# CKAD - Certified Kubernetes Application Developer — replicasets

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `replicasets` · Notes: 3 · Models: Basic++++

<!-- note:1781279834380 model:Basic++++ -->
**Front:** What is a ReplicaSet?
**Back:** A controller that maintains a specified number of matching Pod replicas.
**Tags:** ckad::replicasets concept

---

<!-- note:1781279834381 model:Basic++++ -->
**Front:** Should CKAD usually require you to create ReplicaSets directly?
**Back:** Usually no; create Deployments, which create ReplicaSets automatically.
**Tags:** ckad::replicasets concept deployments

---

<!-- note:1781279834405 model:Basic++++ -->
**Front:** Command: list ReplicaSets for Deployment with app=web.
**Back:** kubectl get rs -l app=web
**Tags:** ckad::replicasets command deployments

---
