# CKAD - Certified Kubernetes Application Developer — downward-api

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `downward-api` · Notes: 6 · Models: Basic++++

<!-- note:1781279834284 model:Basic++++ -->
**Front:** What is the Downward API used for?
**Back:** Expose Pod/container metadata and resource info to containers as environment variables or files.
**Tags:** ckad::downward-api concept

---

<!-- note:1781279834285 model:Basic++++ -->
**Front:** YAML: env var from Pod name using Downward API.
**Back:** env:<br>- name: POD_NAME<br>  valueFrom:<br>    fieldRef:<br>      fieldPath: metadata.name
**Tags:** ckad::downward-api yaml

---

<!-- note:1781279834286 model:Basic++++ -->
**Front:** YAML: env var from Pod namespace using Downward API.
**Back:** env:<br>- name: POD_NAMESPACE<br>  valueFrom:<br>    fieldRef:<br>      fieldPath: metadata.namespace
**Tags:** ckad::downward-api yaml

---

<!-- note:1781279834287 model:Basic++++ -->
**Front:** YAML: env var from Pod IP using Downward API.
**Back:** env:<br>- name: POD_IP<br>  valueFrom:<br>    fieldRef:<br>      fieldPath: status.podIP
**Tags:** ckad::downward-api yaml

---

<!-- note:1781279834288 model:Basic++++ -->
**Front:** YAML: env var from resource limit CPU.
**Back:** env:<br>- name: CPU_LIMIT<br>  valueFrom:<br>    resourceFieldRef:<br>      resource: limits.cpu
**Tags:** ckad::downward-api resources yaml

---

<!-- note:1781279834289 model:Basic++++ -->
**Front:** YAML: mount labels through Downward API volume.
**Back:** volumes:<br>- name: podinfo<br>  downwardAPI:<br>    items:<br>    - path: labels<br>      fieldRef:<br>        fieldPath: metadata.labels
**Tags:** ckad::downward-api volumes yaml

---
