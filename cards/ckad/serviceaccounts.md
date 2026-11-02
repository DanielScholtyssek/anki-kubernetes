# CKAD - Certified Kubernetes Application Developer — serviceaccounts

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `serviceaccounts` · Notes: 5 · Models: Basic++++

<!-- note:1781279834333 model:Basic++++ -->
**Front:** What is a ServiceAccount used for?
**Back:** It gives Pods an identity for talking to the Kubernetes API or using permissions bound through RBAC.
**Tags:** ckad::serviceaccounts concept

---

<!-- note:1781279834334 model:Basic++++ -->
**Front:** Command: create ServiceAccount app-sa.
**Back:** kubectl create serviceaccount app-sa
**Tags:** ckad::serviceaccounts command

---

<!-- note:1781279834335 model:Basic++++ -->
**Front:** YAML: attach ServiceAccount to Pod.
**Back:** spec:<br>  serviceAccountName: app-sa
**Tags:** ckad::serviceaccounts pods yaml

---

<!-- note:1781279834336 model:Basic++++ -->
**Front:** YAML: disable automatic service account token mount.
**Back:** spec:<br>  automountServiceAccountToken: false
**Tags:** ckad::serviceaccounts security yaml

---

<!-- note:1781279834337 model:Basic++++ -->
**Front:** Command: create a token for a ServiceAccount.
**Back:** kubectl create token app-sa
**Tags:** ckad::serviceaccounts command

---
