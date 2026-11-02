# CKAD - Certified Kubernetes Application Developer — workflow

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `workflow` · Notes: 21 · Models: Basic++++

<!-- note:1781279834138 model:Basic++++ -->
**Front:** What is the safest first action in any CKAD task?
**Back:** Check the current context and namespace before creating or modifying resources.
**Tags:** ckad::workflow concept

---

<!-- note:1781279834139 model:Basic++++ -->
**Front:** Command: show current Kubernetes context.
**Back:** kubectl config current-context
**Tags:** ckad::workflow command

---

<!-- note:1781279834140 model:Basic++++ -->
**Front:** Command: list all configured contexts.
**Back:** kubectl config get-contexts
**Tags:** ckad::workflow command

---

<!-- note:1781279834141 model:Basic++++ -->
**Front:** Command: switch to a context.
**Back:** kubectl config use-context &lt;context-name&gt;
**Tags:** ckad::workflow command

---

<!-- note:1781279834142 model:Basic++++ -->
**Front:** Command: set the current namespace for the active context.
**Back:** kubectl config set-context --current --namespace=&lt;namespace&gt;
**Tags:** ckad::workflow command namespaces

---

<!-- note:1781279834145 model:Basic++++ -->
**Front:** Command: list all common workload/network resources in a namespace.
**Back:** kubectl get all -n &lt;namespace&gt;
**Tags:** ckad::workflow command

---

<!-- note:1781279834146 model:Basic++++ -->
**Front:** What does --dry-run=client -o yaml do?
**Back:** It generates the YAML the client would send without creating the resource, useful for fast exam YAML templates.
**Tags:** ckad::workflow command yaml

---

<!-- note:1781279834150 model:Basic++++ -->
**Front:** Command: explain valid fields for Pod spec.
**Back:** kubectl explain pod.spec
**Tags:** ckad::workflow command yaml

---

<!-- note:1781279834151 model:Basic++++ -->
**Front:** Command: recursively explain a field tree.
**Back:** kubectl explain pod.spec.containers --recursive
**Tags:** ckad::workflow command yaml

---

<!-- note:1781279834152 model:Basic++++ -->
**Front:** Command: apply a manifest file.
**Back:** kubectl apply -f file.yaml
**Tags:** ckad::workflow command yaml

---

<!-- note:1781279834153 model:Basic++++ -->
**Front:** Command: create resources from a manifest file.
**Back:** kubectl create -f file.yaml
**Tags:** ckad::workflow command yaml

---

<!-- note:1781279834154 model:Basic++++ -->
**Front:** Command: replace a resource from a manifest file.
**Back:** kubectl replace -f file.yaml
**Tags:** ckad::workflow command yaml

---

<!-- note:1781279834155 model:Basic++++ -->
**Front:** When is kubectl replace --force useful in CKAD?
**Back:** When a field is immutable and the task allows recreation; it deletes and recreates the object from the manifest.
**Tags:** ckad::workflow command yaml

---

<!-- note:1781279834156 model:Basic++++ -->
**Front:** Command: delete resources defined in a manifest file.
**Back:** kubectl delete -f file.yaml
**Tags:** ckad::workflow command yaml

---

<!-- note:1781279834159 model:Basic++++ -->
**Front:** Why should you verify after every CKAD change?
**Back:** Because creating the resource is not enough; you must prove Pods are running, Services have endpoints, rollouts complete, and network paths work.
**Tags:** ckad::workflow concept

---

<!-- note:1781279834161 model:Basic++++ -->
**Front:** Command: watch resources change live.
**Back:** kubectl get pods -w
**Tags:** ckad::workflow command

---

<!-- note:1781279834162 model:Basic++++ -->
**Front:** Command: show output in YAML.
**Back:** kubectl get &lt;resource&gt; &lt;name&gt; -o yaml
**Tags:** ckad::workflow command yaml

---

<!-- note:1781279834163 model:Basic++++ -->
**Front:** Command: show output in JSON.
**Back:** kubectl get &lt;resource&gt; &lt;name&gt; -o json
**Tags:** ckad::workflow command yaml

---

<!-- note:1781279834166 model:Basic++++ -->
**Front:** Command: sort Pods by creation timestamp.
**Back:** kubectl get pods --sort-by=.metadata.creationTimestamp
**Tags:** ckad::workflow command debugging

---

<!-- note:1781279834168 model:Basic++++ -->
**Front:** What is the general CKAD loop?
**Back:** Inspect → generate/edit YAML → apply → verify → debug if needed → move on.
**Tags:** ckad::workflow concept

---

<!-- note:1781279834184 model:Basic++++ -->
**Front:** Which object fields are often immutable and may require recreate?
**Back:** Deployment spec.selector, Service clusterIP/type details in some cases, PVC storageClassName/accessModes, and Pod spec fields after creation.
**Tags:** ckad::workflow yaml

---
