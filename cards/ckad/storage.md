# CKAD - Certified Kubernetes Application Developer — storage

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `storage` · Notes: 12 · Models: Basic++++

<!-- note:1781279834301 model:Basic++++ -->
**Front:** What is a PersistentVolumeClaim?
**Back:** A namespaced request for persistent storage that a Pod can mount through the cluster storage system.
**Tags:** ckad::storage concept pvc

---

<!-- note:1781279834302 model:Basic++++ -->
**Front:** What is the relationship between PV and PVC?
**Back:** A PersistentVolume is cluster storage; a PersistentVolumeClaim is a namespaced request that binds to suitable storage.
**Tags:** ckad::storage concept pvc

---

<!-- note:1781279834303 model:Basic++++ -->
**Front:** Minimal PVC YAML.
**Back:** apiVersion: v1<br>kind: PersistentVolumeClaim<br>metadata:<br>  name: data<br>spec:<br>  accessModes: ["ReadWriteOnce"]<br>  resources:<br>    requests:<br>      storage: 1Gi
**Tags:** ckad::storage pvc yaml

---

<!-- note:1781279834304 model:Basic++++ -->
**Front:** YAML: mount a PVC in a Pod.
**Back:** volumes:<br>- name: data<br>  persistentVolumeClaim:<br>    claimName: data<br>containers:<br>- name: app<br>  volumeMounts:<br>  - name: data<br>    mountPath: /data
**Tags:** ckad::storage pvc volumes yaml

---

<!-- note:1781279834305 model:Basic++++ -->
**Front:** Common PVC access mode: ReadWriteOnce means what?
**Back:** The volume can be mounted as read-write by a single node.
**Tags:** ckad::storage concept pvc

---

<!-- note:1781279834306 model:Basic++++ -->
**Front:** Common PVC access mode: ReadOnlyMany means what?
**Back:** The volume can be mounted read-only by many nodes.
**Tags:** ckad::storage concept pvc

---

<!-- note:1781279834307 model:Basic++++ -->
**Front:** Common PVC access mode: ReadWriteMany means what?
**Back:** The volume can be mounted read-write by many nodes if the storage class supports it.
**Tags:** ckad::storage concept pvc

---

<!-- note:1781279834308 model:Basic++++ -->
**Front:** What does storageClassName do in a PVC?
**Back:** Selects the StorageClass used for dynamic provisioning or binding.
**Tags:** ckad::storage pvc yaml

---

<!-- note:1781279834309 model:Basic++++ -->
**Front:** YAML: PVC with storageClassName fast.
**Back:** spec:<br>  storageClassName: fast
**Tags:** ckad::storage pvc yaml

---

<!-- note:1781279834310 model:Basic++++ -->
**Front:** What does a Pending PVC usually mean?
**Back:** No matching storage is available/provisioned, storage class is wrong/missing, or dynamic provisioner cannot satisfy the claim.
**Tags:** ckad::storage debugging pvc

---

<!-- note:1781279834311 model:Basic++++ -->
**Front:** Command: list PVCs.
**Back:** kubectl get pvc
**Tags:** ckad::storage command pvc

---

<!-- note:1781279834312 model:Basic++++ -->
**Front:** Command: describe a PVC.
**Back:** kubectl describe pvc &lt;name&gt;
**Tags:** ckad::storage command debugging pvc

---
