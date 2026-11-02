# CKAD - Certified Kubernetes Application Developer — init-containers

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `init-containers` · Notes: 6 · Models: Basic++++

<!-- note:1781279834246 model:Basic++++ -->
**Front:** What is an init container?
**Back:** A container that runs to completion before app containers start, often to prepare files, wait for dependencies, or perform setup.
**Tags:** ckad::init-containers concept

---

<!-- note:1781279834247 model:Basic++++ -->
**Front:** How do init containers run?
**Back:** Sequentially, before app containers; each must succeed before the next starts.
**Tags:** ckad::init-containers concept

---

<!-- note:1781279834248 model:Basic++++ -->
**Front:** YAML: initContainers field location.
**Back:** spec:<br>  initContainers:<br>  - name: init<br>    image: busybox<br>    command: ["sh", "-c", "echo init"]<br>  containers:<br>  - name: app<br>    image: nginx
**Tags:** ckad::init-containers yaml

---

<!-- note:1781279834249 model:Basic++++ -->
**Front:** How can an init container pass files to the main container?
**Back:** Mount the same volume, usually emptyDir, into both containers at different paths.
**Tags:** ckad::init-containers concept volumes

---

<!-- note:1781279834250 model:Basic++++ -->
**Front:** Command: view logs from an init container.
**Back:** kubectl logs &lt;pod&gt; -c &lt;init-container-name&gt;
**Tags:** ckad::init-containers command logs

---

<!-- note:1781279834251 model:Basic++++ -->
**Front:** What does Init:CrashLoopBackOff mean?
**Back:** An init container is failing repeatedly, so app containers have not started.
**Tags:** ckad::init-containers debugging

---
