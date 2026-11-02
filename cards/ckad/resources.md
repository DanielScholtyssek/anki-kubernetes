# CKAD - Certified Kubernetes Application Developer — resources

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `resources` · Notes: 10 · Models: Basic++++

<!-- note:1781279834317 model:Basic++++ -->
**Front:** What are resource requests?
**Back:** Minimum CPU/memory Kubernetes uses for scheduling decisions.
**Tags:** ckad::resources concept

---

<!-- note:1781279834318 model:Basic++++ -->
**Front:** What are resource limits?
**Back:** Maximum CPU/memory a container is allowed to use; memory over limit can cause OOMKilled.
**Tags:** ckad::resources concept

---

<!-- note:1781279834319 model:Basic++++ -->
**Front:** YAML: set CPU and memory requests/limits.
**Back:** resources:<br>  requests:<br>    cpu: 100m<br>    memory: 128Mi<br>  limits:<br>    cpu: 500m<br>    memory: 256Mi
**Tags:** ckad::resources yaml

---

<!-- note:1781279834320 model:Basic++++ -->
**Front:** What does CPU unit 500m mean?
**Back:** Half of one CPU core.
**Tags:** ckad::resources concept

---

<!-- note:1781279834321 model:Basic++++ -->
**Front:** What does memory unit Mi mean?
**Back:** Mebibytes, e.g. 128Mi is 128 × 2^20 bytes.
**Tags:** ckad::resources concept

---

<!-- note:1781279834322 model:Basic++++ -->
**Front:** What happens if a container exceeds memory limit?
**Back:** It can be killed with OOMKilled.
**Tags:** ckad::resources debugging

---

<!-- note:1781279834323 model:Basic++++ -->
**Front:** What happens if a container exceeds CPU limit?
**Back:** It is throttled rather than killed.
**Tags:** ckad::resources concept

---

<!-- note:1781279834324 model:Basic++++ -->
**Front:** What causes a Pod to remain Pending due to resources?
**Back:** No node has enough allocatable CPU/memory to satisfy its requests.
**Tags:** ckad::resources debugging scheduling

---

<!-- note:1781279834325 model:Basic++++ -->
**Front:** Command: show node resource usage if metrics are available.
**Back:** kubectl top nodes
**Tags:** ckad::resources command observability

---

<!-- note:1781279834326 model:Basic++++ -->
**Front:** Command: show Pod resource usage if metrics are available.
**Back:** kubectl top pods
**Tags:** ckad::resources command observability

---
