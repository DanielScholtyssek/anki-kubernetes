# CKAD - Certified Kubernetes Application Developer — selectors

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `selectors` · Notes: 4 · Models: Basic++++

<!-- note:1781279834632 model:Basic++++ -->
**Front:** Why are selectors the biggest CKAD gap?
**Back:** Many resources look correct individually but fail because labels/selectors do not connect Pods, Services, Deployments, and NetworkPolicies.
**Tags:** ckad::selectors concept labs

---

<!-- note:1781279834633 model:Basic++++ -->
**Front:** What is the fastest selector debugging command for Services?
**Back:** kubectl get endpoints &lt;service&gt; and compare Service selector with Pod labels using kubectl get pods --show-labels.
**Tags:** ckad::selectors debugging services

---

<!-- note:1781279834634 model:Basic++++ -->
**Front:** What is the fastest selector debugging command for Deployments?
**Back:** kubectl get deploy &lt;name&gt; -o yaml and compare spec.selector.matchLabels to spec.template.metadata.labels.
**Tags:** ckad::selectors debugging deployments

---

<!-- note:1781279834635 model:Basic++++ -->
**Front:** What is the fastest selector debugging command for NetworkPolicy?
**Back:** kubectl describe netpol &lt;name&gt; and compare podSelector/from/to selectors with Pod and namespace labels.
**Tags:** ckad::selectors debugging networkpolicy

---
