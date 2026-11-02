# CKAD - Certified Kubernetes Application Developer — volumes

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `volumes` · Notes: 15 · Models: Basic++++

<!-- note:1781279834290 model:Basic++++ -->
**Front:** What is a Kubernetes volume?
**Back:** Storage attached to a Pod and mounted into containers; its lifecycle depends on the volume type.
**Tags:** ckad::volumes concept

---

<!-- note:1781279834291 model:Basic++++ -->
**Front:** What is emptyDir used for?
**Back:** Temporary storage shared by containers in the same Pod, created when the Pod is assigned to a node and deleted when the Pod is removed.
**Tags:** ckad::volumes concept emptydir

---

<!-- note:1781279834292 model:Basic++++ -->
**Front:** YAML: define emptyDir volume.
**Back:** volumes:<br>- name: work<br>  emptyDir: {}
**Tags:** ckad::volumes emptydir yaml

---

<!-- note:1781279834293 model:Basic++++ -->
**Front:** YAML: mount a volume into a container.
**Back:** volumeMounts:<br>- name: work<br>  mountPath: /work
**Tags:** ckad::volumes yaml

---

<!-- note:1781279834294 model:Basic++++ -->
**Front:** What is emptyDir commonly combined with?
**Back:** Init containers or sidecars that generate files for the main container.
**Tags:** ckad::volumes concept emptydir init-containers

---

<!-- note:1781279834295 model:Basic++++ -->
**Front:** What happens to emptyDir data when a container restarts?
**Back:** The data remains as long as the Pod remains on the node.
**Tags:** ckad::volumes concept emptydir

---

<!-- note:1781279834296 model:Basic++++ -->
**Front:** What happens to emptyDir data when the Pod is deleted?
**Back:** The data is deleted.
**Tags:** ckad::volumes concept emptydir

---

<!-- note:1781279834297 model:Basic++++ -->
**Front:** YAML: emptyDir backed by memory.
**Back:** volumes:<br>- name: cache<br>  emptyDir:<br>    medium: Memory
**Tags:** ckad::volumes emptydir yaml

---

<!-- note:1781279834298 model:Basic++++ -->
**Front:** What is hostPath used for?
**Back:** Mounting a path from the node filesystem into a Pod; useful for node-level access but risky and node-dependent.
**Tags:** ckad::volumes concept hostpath

---

<!-- note:1781279834299 model:Basic++++ -->
**Front:** YAML: hostPath volume.
**Back:** volumes:<br>- name: host<br>  hostPath:<br>    path: /data<br>    type: DirectoryOrCreate
**Tags:** ckad::volumes hostpath yaml

---

<!-- note:1781279834300 model:Basic++++ -->
**Front:** Why is hostPath usually not ideal for portable apps?
**Back:** It ties the Pod to files on a particular node and can create security risks.
**Tags:** ckad::volumes concept hostpath

---

<!-- note:1781279834313 model:Basic++++ -->
**Front:** What is subPath used for in a volumeMount?
**Back:** Mount one file or subdirectory from a volume instead of mounting the whole volume path.
**Tags:** ckad::volumes yaml

---

<!-- note:1781279834314 model:Basic++++ -->
**Front:** YAML: mount a single ConfigMap key with subPath.
**Back:** volumeMounts:<br>- name: config<br>  mountPath: /etc/app/config.yaml<br>  subPath: config.yaml
**Tags:** ckad::volumes configmaps yaml

---

<!-- note:1781279834315 model:Basic++++ -->
**Front:** What is a projected volume?
**Back:** A volume that combines multiple sources such as Secret, ConfigMap, Downward API, or service account token into one mount.
**Tags:** ckad::volumes concept projected

---

<!-- note:1781279834316 model:Basic++++ -->
**Front:** YAML: projected volume with ConfigMap and Secret sources.
**Back:** volumes:<br>- name: projected<br>  projected:<br>    sources:<br>    - configMap:<br>        name: app-config<br>    - secret:<br>        name: app-secret
**Tags:** ckad::volumes projected yaml

---
