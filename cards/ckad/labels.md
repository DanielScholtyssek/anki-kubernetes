# CKAD - Certified Kubernetes Application Developer — labels

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `labels` · Notes: 10 · Models: Basic++++

<!-- note:1781279834165 model:Basic++++ -->
**Front:** Command: print a custom APP label column for Pods.
**Back:** kubectl get pods -L app
**Tags:** ckad::labels command

---

<!-- note:1781279834178 model:Basic++++ -->
**Front:** What is a selector used for?
**Back:** A selector chooses objects by labels, commonly to connect Deployments to Pods, Services to Pods, or NetworkPolicies to Pods.
**Tags:** ckad::labels concept selectors

---

<!-- note:1781279834179 model:Basic++++ -->
**Front:** What is a label?
**Back:** A key-value pair used for grouping, selecting, and organising Kubernetes objects.
**Tags:** ckad::labels concept

---

<!-- note:1781279834233 model:Basic++++ -->
**Front:** YAML: add labels to a Pod.
**Back:** metadata:<br>  labels:<br>    app: web<br>    tier: frontend
**Tags:** ckad::labels pods yaml

---

<!-- note:1781279834234 model:Basic++++ -->
**Front:** Command: label a Pod app=web.
**Back:** kubectl label pod &lt;pod&gt; app=web
**Tags:** ckad::labels command pods

---

<!-- note:1781279834235 model:Basic++++ -->
**Front:** Command: overwrite a Pod label.
**Back:** kubectl label pod &lt;pod&gt; app=api --overwrite
**Tags:** ckad::labels command pods

---

<!-- note:1781279834236 model:Basic++++ -->
**Front:** Command: remove label app from a Pod.
**Back:** kubectl label pod &lt;pod&gt; app-
**Tags:** ckad::labels command pods

---

<!-- note:1781279834237 model:Basic++++ -->
**Front:** Command: list Pods with labels displayed.
**Back:** kubectl get pods --show-labels
**Tags:** ckad::labels command pods

---

<!-- note:1781279834238 model:Basic++++ -->
**Front:** Command: get Pods with label app=web.
**Back:** kubectl get pods -l app=web
**Tags:** ckad::labels command pods

---

<!-- note:1781279834239 model:Basic++++ -->
**Front:** Command: get Pods where app is v1 or v2.
**Back:** kubectl get pods -l 'app in (v1,v2)'
**Tags:** ckad::labels command pods

---
