# CKAD - Certified Kubernetes Application Developer — hpa

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `hpa` · Notes: 4 · Models: Basic++++

<!-- note:1781279834406 model:Basic++++ -->
**Front:** Command: autoscale Deployment between 2 and 10 replicas at 80% CPU.
**Back:** kubectl autoscale deployment web --min=2 --max=10 --cpu-percent=80
**Tags:** ckad::hpa command deployments

---

<!-- note:1781279834407 model:Basic++++ -->
**Front:** Command: list HPAs.
**Back:** kubectl get hpa
**Tags:** ckad::hpa command

---

<!-- note:1781279834408 model:Basic++++ -->
**Front:** What object is created by kubectl autoscale deployment?
**Back:** HorizontalPodAutoscaler.
**Tags:** ckad::hpa concept deployments

---

<!-- note:1781279834409 model:Basic++++ -->
**Front:** What does HPA generally require to work with CPU metrics?
**Back:** Metrics Server and containers with CPU requests.
**Tags:** ckad::hpa concept resources

---
