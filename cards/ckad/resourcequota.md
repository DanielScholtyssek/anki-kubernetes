# CKAD - Certified Kubernetes Application Developer — resourcequota

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `resourcequota` · Notes: 4 · Models: Basic++++

<!-- note:1781279834327 model:Basic++++ -->
**Front:** What is a ResourceQuota?
**Back:** A namespace-level object that limits aggregate resource usage or object counts in that namespace.
**Tags:** ckad::resourcequota concept

---

<!-- note:1781279834328 model:Basic++++ -->
**Front:** Command: create ResourceQuota for CPU, memory, and Pods.
**Back:** kubectl create quota myrq --hard=cpu=1,memory=1Gi,pods=2
**Tags:** ckad::resourcequota command

---

<!-- note:1781279834329 model:Basic++++ -->
**Front:** YAML: ResourceQuota hard limits.
**Back:** apiVersion: v1<br>kind: ResourceQuota<br>metadata:<br>  name: myrq<br>spec:<br>  hard:<br>    requests.cpu: "1"<br>    requests.memory: 1Gi<br>    pods: "2"
**Tags:** ckad::resourcequota yaml

---

<!-- note:1781279834330 model:Basic++++ -->
**Front:** Command: describe ResourceQuota.
**Back:** kubectl describe quota &lt;name&gt;
**Tags:** ckad::resourcequota command

---
