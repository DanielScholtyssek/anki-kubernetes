# CKAD - Certified Kubernetes Application Developer — securitycontext

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `securitycontext` · Notes: 8 · Models: Basic++++

<!-- note:1781279834338 model:Basic++++ -->
**Front:** What is securityContext used for?
**Back:** It controls Linux/security settings at Pod or container level, such as user IDs, capabilities, privilege escalation, seccomp, and filesystem permissions.
**Tags:** ckad::securitycontext concept

---

<!-- note:1781279834339 model:Basic++++ -->
**Front:** YAML: Pod-level runAsUser and fsGroup.
**Back:** spec:<br>  securityContext:<br>    runAsUser: 1000<br>    runAsGroup: 3000<br>    fsGroup: 2000
**Tags:** ckad::securitycontext yaml

---

<!-- note:1781279834340 model:Basic++++ -->
**Front:** YAML: container-level securityContext preventing privilege escalation.
**Back:** securityContext:<br>  allowPrivilegeEscalation: false
**Tags:** ckad::securitycontext yaml

---

<!-- note:1781279834341 model:Basic++++ -->
**Front:** YAML: container read-only root filesystem.
**Back:** securityContext:<br>  readOnlyRootFilesystem: true
**Tags:** ckad::securitycontext yaml

---

<!-- note:1781279834342 model:Basic++++ -->
**Front:** YAML: drop all Linux capabilities.
**Back:** securityContext:<br>  capabilities:<br>    drop:<br>    - ALL
**Tags:** ckad::securitycontext yaml

---

<!-- note:1781279834343 model:Basic++++ -->
**Front:** YAML: add NET_ADMIN capability.
**Back:** securityContext:<br>  capabilities:<br>    add:<br>    - NET_ADMIN
**Tags:** ckad::securitycontext yaml

---

<!-- note:1781279834344 model:Basic++++ -->
**Front:** YAML: seccomp RuntimeDefault.
**Back:** securityContext:<br>  seccompProfile:<br>    type: RuntimeDefault
**Tags:** ckad::securitycontext yaml

---

<!-- note:1781279834345 model:Basic++++ -->
**Front:** What is the difference between Pod securityContext and container securityContext?
**Back:** Pod securityContext applies to all containers where relevant; container securityContext overrides/adds settings for one container.
**Tags:** ckad::securitycontext concept

---
