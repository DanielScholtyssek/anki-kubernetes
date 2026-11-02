# CKAD - Certified Kubernetes Application Developer — namespaces

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `namespaces` · Notes: 12 · Models: Basic++++

<!-- note:1781279834143 model:Basic++++ -->
**Front:** Command: list namespaces.
**Back:** kubectl get ns
**Tags:** ckad::namespaces command

---

<!-- note:1781279834185 model:Basic++++ -->
**Front:** What is a Namespace used for?
**Back:** A namespace partitions namespaced resources inside a cluster so tasks, apps, and teams can be isolated logically.
**Tags:** ckad::namespaces concept

---

<!-- note:1781279834186 model:Basic++++ -->
**Front:** Are Nodes namespaced?
**Back:** No. Nodes are cluster-scoped.
**Tags:** ckad::namespaces concept

---

<!-- note:1781279834187 model:Basic++++ -->
**Front:** Are Pods namespaced?
**Back:** Yes. Pods are namespaced resources.
**Tags:** ckad::namespaces concept pods

---

<!-- note:1781279834188 model:Basic++++ -->
**Front:** Are Services namespaced?
**Back:** Yes. Services are namespaced resources.
**Tags:** ckad::namespaces concept services

---

<!-- note:1781279834189 model:Basic++++ -->
**Front:** Are PersistentVolumes namespaced?
**Back:** No. PersistentVolumes are cluster-scoped; PersistentVolumeClaims are namespaced.
**Tags:** ckad::namespaces concept storage

---

<!-- note:1781279834190 model:Basic++++ -->
**Front:** Command: create namespace dev.
**Back:** kubectl create namespace dev
**Tags:** ckad::namespaces command

---

<!-- note:1781279834191 model:Basic++++ -->
**Front:** Command: generate namespace YAML without creating it.
**Back:** kubectl create namespace dev --dry-run=client -o yaml
**Tags:** ckad::namespaces command yaml

---

<!-- note:1781279834192 model:Basic++++ -->
**Front:** YAML: namespace field location for a Pod.
**Back:** metadata:<br>  namespace: dev
**Tags:** ckad::namespaces yaml

---

<!-- note:1781279834193 model:Basic++++ -->
**Front:** Command: get Pods from namespace dev.
**Back:** kubectl get pods -n dev
**Tags:** ckad::namespaces command pods

---

<!-- note:1781279834194 model:Basic++++ -->
**Front:** Command: delete namespace dev.
**Back:** kubectl delete namespace dev
**Tags:** ckad::namespaces command

---

<!-- note:1781279834195 model:Basic++++ -->
**Front:** What happens when you delete a namespace?
**Back:** Namespaced resources inside it are deleted as part of namespace cleanup.
**Tags:** ckad::namespaces concept

---
