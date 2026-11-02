# CKAD - Certified Kubernetes Application Developer — annotations

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `annotations` · Notes: 5 · Models: Basic++++

<!-- note:1781279834180 model:Basic++++ -->
**Front:** What is an annotation?
**Back:** A key-value metadata entry for non-selector information such as descriptions, checksums, owners, or tool metadata.
**Tags:** ckad::annotations concept

---

<!-- note:1781279834181 model:Basic++++ -->
**Front:** Should annotations be used for Service or Deployment selectors?
**Back:** No. Selectors use labels, not annotations.
**Tags:** ckad::annotations concept

---

<!-- note:1781279834240 model:Basic++++ -->
**Front:** Command: annotate a Pod owner=team-a.
**Back:** kubectl annotate pod &lt;pod&gt; owner=team-a
**Tags:** ckad::annotations command pods

---

<!-- note:1781279834241 model:Basic++++ -->
**Front:** Command: remove annotation owner from a Pod.
**Back:** kubectl annotate pod &lt;pod&gt; owner-
**Tags:** ckad::annotations command pods

---

<!-- note:1781279834242 model:Basic++++ -->
**Front:** Command: list annotations on a Pod.
**Back:** kubectl annotate pod &lt;pod&gt; --list
**Tags:** ckad::annotations command pods

---
