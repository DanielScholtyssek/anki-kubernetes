# CKAD - Certified Kubernetes Application Developer — labs

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `labs` · Notes: 20 · Models: Basic++++

<!-- note:1781279834612 model:Basic++++ -->
**Front:** What is the most important KodeKloud lightning lab skill after YAML basics?
**Back:** Combining multiple objects correctly and verifying the full path, not just creating individual resources.
**Tags:** ckad::labs concept

---

<!-- note:1781279834613 model:Basic++++ -->
**Front:** What should you do if a lab asks for an object you partially remember?
**Back:** Generate a close YAML skeleton with kubectl, then use kubectl explain and edit the missing fields.
**Tags:** ckad::labs workflow

---

<!-- note:1781279834614 model:Basic++++ -->
**Front:** What should you do if a manifest apply error says unknown field?
**Back:** Check indentation and field location with kubectl explain for the exact parent path.
**Tags:** ckad::labs debugging yaml

---

<!-- note:1781279834615 model:Basic++++ -->
**Front:** What should you do if a task has many requirements?
**Back:** Create a minimal working object first, then add requirements one by one and verify.
**Tags:** ckad::labs workflow

---

<!-- note:1781279834616 model:Basic++++ -->
**Front:** What should you do if you are stuck for too long in CKAD?
**Back:** Save partial work if useful, move on, and return later; do not spend excessive time on one low-value task.
**Tags:** ckad::labs exam

---

<!-- note:1781279834617 model:Basic++++ -->
**Front:** Minimum verification for a Pod task?
**Back:** kubectl get pod, kubectl describe pod, kubectl logs if applicable, and check Ready/Completed state based on task.
**Tags:** ckad::labs debugging pods

---

<!-- note:1781279834618 model:Basic++++ -->
**Front:** Minimum verification for a Deployment task?
**Back:** kubectl rollout status deployment/&lt;name&gt;, kubectl get deploy/rs/pods, and inspect image/replicas/labels.
**Tags:** ckad::labs debugging deployments

---

<!-- note:1781279834619 model:Basic++++ -->
**Front:** Minimum verification for a Service task?
**Back:** kubectl get svc, kubectl get endpoints, and test from a temporary Pod or port-forward.
**Tags:** ckad::labs debugging services

---

<!-- note:1781279834620 model:Basic++++ -->
**Front:** Minimum verification for an Ingress task?
**Back:** kubectl get ingress, kubectl describe ingress, check backend Service/endpoints, and test host/path if possible.
**Tags:** ckad::labs debugging ingress

---

<!-- note:1781279834621 model:Basic++++ -->
**Front:** Minimum verification for a NetworkPolicy task?
**Back:** Check selected Pods/labels, describe policy, then test allowed and denied traffic from labelled temporary Pods.
**Tags:** ckad::labs debugging networkpolicy

---

<!-- note:1781279834622 model:Basic++++ -->
**Front:** Minimum verification for ConfigMap/Secret env task?
**Back:** Exec into Pod and run env or print the expected variable; recreate Pod if env changed after creation.
**Tags:** ckad::labs configmaps debugging secrets

---

<!-- note:1781279834623 model:Basic++++ -->
**Front:** Minimum verification for ConfigMap/Secret volume task?
**Back:** Exec into Pod and ls/cat the mount path; check volumeMounts and volumes names match.
**Tags:** ckad::labs configmaps debugging secrets volumes

---

<!-- note:1781279834624 model:Basic++++ -->
**Front:** Minimum verification for Job task?
**Back:** kubectl get job, kubectl get pods --selector=job-name=&lt;job&gt;, and kubectl logs job/&lt;job&gt;.
**Tags:** ckad::labs debugging jobs

---

<!-- note:1781279834625 model:Basic++++ -->
**Front:** Minimum verification for CronJob task?
**Back:** kubectl get cronjob, describe it, optionally create manual Job from CronJob to verify command/template.
**Tags:** ckad::labs cronjobs debugging

---

<!-- note:1781279834626 model:Basic++++ -->
**Front:** What command should you use when asked to create YAML quickly from scratch?
**Back:** kubectl run/create/expose/create job/create cronjob with --dry-run=client -o yaml &gt; file.yaml.
**Tags:** ckad::labs command yaml

---

<!-- note:1781279834627 model:Basic++++ -->
**Front:** What command helps when you know the object but not the field path?
**Back:** kubectl explain &lt;kind&gt;.&lt;path&gt;
**Tags:** ckad::labs command yaml

---

<!-- note:1781279834628 model:Basic++++ -->
**Front:** What is the fastest way to find why Kubernetes rejected your YAML?
**Back:** Read the exact kubectl apply error, then check indentation/apiVersion/kind/field path with kubectl explain.
**Tags:** ckad::labs debugging yaml

---

<!-- note:1781279834629 model:Basic++++ -->
**Front:** What is the fastest way to find why a Pod was rejected or changed by policy?
**Back:** Read the kubectl error and events; admission messages usually say exactly what policy requires.
**Tags:** admission ckad::labs debugging

---

<!-- note:1781279834630 model:Basic++++ -->
**Front:** What should you memorise for CKAD rather than search docs every time?
**Back:** kubectl generation commands, core YAML skeletons, selectors, Service ports, env/volume injection, probes, rollout commands, and NetworkPolicy structure.
**Tags:** ckad::labs exam

---

<!-- note:1781279834631 model:Basic++++ -->
**Front:** What should you rely on docs/kubectl explain for?
**Back:** Exact less-common field paths, advanced affinity, projected volumes, RBAC details, Helm/Kustomize syntax, and unfamiliar CRDs.
**Tags:** ckad::labs exam

---
