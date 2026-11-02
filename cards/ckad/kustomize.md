# CKAD - Certified Kubernetes Application Developer — kustomize

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `kustomize` · Notes: 18 · Models: Basic++++

<!-- note:1781279834576 model:Basic++++ -->
**Front:** What is Kustomize?
**Back:** A manifest customization tool that overlays changes onto base YAML without templating.
**Tags:** ckad::kustomize concept

---

<!-- note:1781279834577 model:Basic++++ -->
**Front:** What file defines a Kustomize package?
**Back:** kustomization.yaml.
**Tags:** ckad::kustomize yaml

---

<!-- note:1781279834578 model:Basic++++ -->
**Front:** Command: build Kustomize manifests.
**Back:** kubectl kustomize &lt;directory&gt;
**Tags:** ckad::kustomize command yaml

---

<!-- note:1781279834579 model:Basic++++ -->
**Front:** Command: apply Kustomize directory.
**Back:** kubectl apply -k &lt;directory&gt;
**Tags:** ckad::kustomize command

---

<!-- note:1781279834580 model:Basic++++ -->
**Front:** YAML: kustomization resources.
**Back:** resources:<br>- deployment.yaml<br>- service.yaml
**Tags:** ckad::kustomize yaml

---

<!-- note:1781279834581 model:Basic++++ -->
**Front:** YAML: set namespace in kustomization.
**Back:** namespace: dev
**Tags:** ckad::kustomize namespaces yaml

---

<!-- note:1781279834582 model:Basic++++ -->
**Front:** YAML: add namePrefix in kustomization.
**Back:** namePrefix: dev-
**Tags:** ckad::kustomize yaml

---

<!-- note:1781279834583 model:Basic++++ -->
**Front:** YAML: add common labels in kustomization.
**Back:** commonLabels:<br>  app: web
**Tags:** ckad::kustomize labels yaml

---

<!-- note:1781279834584 model:Basic++++ -->
**Front:** YAML: configMapGenerator.
**Back:** configMapGenerator:<br>- name: app-config<br>  literals:<br>  - MODE=prod
**Tags:** ckad::kustomize configmaps yaml

---

<!-- note:1781279834585 model:Basic++++ -->
**Front:** YAML: secretGenerator.
**Back:** secretGenerator:<br>- name: app-secret<br>  literals:<br>  - password=s3cr3t
**Tags:** ckad::kustomize secrets yaml

---

<!-- note:1781279834586 model:Basic++++ -->
**Front:** How do generated ConfigMap/Secret names usually change in Kustomize?
**Back:** Kustomize appends a hash suffix by default so workloads roll when content changes.
**Tags:** ckad::kustomize concept configmaps secrets

---

<!-- note:1781279834587 model:Basic++++ -->
**Front:** YAML: disable Kustomize name suffix hash.
**Back:** generatorOptions:<br>  disableNameSuffixHash: true
**Tags:** ckad::kustomize yaml

---

<!-- note:1781279834588 model:Basic++++ -->
**Front:** YAML: update container image with Kustomize.
**Back:** images:<br>- name: nginx<br>  newTag: 1.25
**Tags:** ckad::kustomize deployments yaml

---

<!-- note:1781279834589 model:Basic++++ -->
**Front:** YAML: set replicas with Kustomize.
**Back:** replicas:<br>- name: web<br>  count: 3
**Tags:** ckad::kustomize deployments yaml

---

<!-- note:1781279834590 model:Basic++++ -->
**Front:** YAML: strategic merge patch entry.
**Back:** patches:<br>- path: patch.yaml<br>  target:<br>    kind: Deployment<br>    name: web
**Tags:** ckad::kustomize yaml

---

<!-- note:1781279834591 model:Basic++++ -->
**Front:** What is a base in Kustomize?
**Back:** A reusable set of manifests referenced by overlays.
**Tags:** ckad::kustomize concept

---

<!-- note:1781279834592 model:Basic++++ -->
**Front:** What is an overlay in Kustomize?
**Back:** A directory that references a base and applies environment-specific changes.
**Tags:** ckad::kustomize concept

---

<!-- note:1781279834593 model:Basic++++ -->
**Front:** When should you use kubectl apply -k rather than kubectl apply -f?
**Back:** Use -k for a directory containing kustomization.yaml; use -f for raw manifest files.
**Tags:** ckad::kustomize command

---
