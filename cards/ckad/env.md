# CKAD - Certified Kubernetes Application Developer — env

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `env` · Notes: 2 · Models: Basic++++

<!-- note:1781279834262 model:Basic++++ -->
**Front:** YAML: set a literal environment variable in a container.
**Back:** env:<br>- name: MODE<br>  value: prod
**Tags:** ckad::env yaml

---

<!-- note:1781279834263 model:Basic++++ -->
**Front:** Command: create Pod with env var MODE=prod.
**Back:** kubectl run app --image=nginx --env=MODE=prod
**Tags:** ckad::env command pods

---
