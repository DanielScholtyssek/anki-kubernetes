# CKAD - Certified Kubernetes Application Developer — commands

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `commands` · Notes: 20 · Models: Basic++++

<!-- note:1781279834636 model:Basic++++ -->
**Front:** Command: create a namespace and run nginx Pod in it.
**Back:** kubectl create ns mynamespace<br>kubectl run nginx --image=nginx --restart=Never -n mynamespace
**Tags:** ckad::commands namespaces pods

---

<!-- note:1781279834637 model:Basic++++ -->
**Front:** Command: run nginx Pod and expose it immediately as Service?
**Back:** kubectl run nginx --image=nginx --port=80 --expose
**Tags:** ckad::commands pods services

---

<!-- note:1781279834638 model:Basic++++ -->
**Front:** Command: create Deployment YAML and save to file.
**Back:** kubectl create deploy web --image=nginx --dry-run=client -o yaml &gt; deploy.yaml
**Tags:** ckad::commands deployments yaml

---

<!-- note:1781279834639 model:Basic++++ -->
**Front:** Command: create Service from Deployment and save YAML.
**Back:** kubectl expose deploy web --port=80 --target-port=8080 --dry-run=client -o yaml &gt; svc.yaml
**Tags:** ckad::commands services yaml

---

<!-- note:1781279834640 model:Basic++++ -->
**Front:** Command: create Job YAML and save to file.
**Back:** kubectl create job hello --image=busybox --dry-run=client -o yaml -- echo hello &gt; job.yaml
**Tags:** ckad::commands jobs yaml

---

<!-- note:1781279834641 model:Basic++++ -->
**Front:** Command: create CronJob YAML and save to file.
**Back:** kubectl create cronjob hello --image=busybox --schedule='* * * * *' --dry-run=client -o yaml -- echo hello &gt; cronjob.yaml
**Tags:** ckad::commands cronjobs yaml

---

<!-- note:1781279834642 model:Basic++++ -->
**Front:** Command: quickly delete a stuck Pod without graceful wait.
**Back:** kubectl delete pod &lt;pod&gt; --grace-period=0 --force
**Tags:** ckad::commands debugging pods

---

<!-- note:1781279834643 model:Basic++++ -->
**Front:** Command: get all resources with a label.
**Back:** kubectl get all -l app=web
**Tags:** ckad::commands labels

---

<!-- note:1781279834644 model:Basic++++ -->
**Front:** Command: get resources in all namespaces with label app=web.
**Back:** kubectl get all -A -l app=web
**Tags:** ckad::commands labels namespaces

---

<!-- note:1781279834645 model:Basic++++ -->
**Front:** Command: show API resources with short names.
**Back:** kubectl api-resources
**Tags:** ckad::commands crds

---

<!-- note:1781279834646 model:Basic++++ -->
**Front:** Command: show only names of Pods.
**Back:** kubectl get pods -o name
**Tags:** ckad::commands

---

<!-- note:1781279834647 model:Basic++++ -->
**Front:** Command: delete all resources in a manifest directory.
**Back:** kubectl delete -f ./manifests/
**Tags:** ckad::commands yaml

---

<!-- note:1781279834648 model:Basic++++ -->
**Front:** Command: apply every YAML in a directory.
**Back:** kubectl apply -f ./manifests/
**Tags:** ckad::commands yaml

---

<!-- note:1781279834649 model:Basic++++ -->
**Front:** Command: get current namespace from context.
**Back:** kubectl config view --minify --output 'jsonpath={..namespace}'
**Tags:** ckad::commands jsonpath namespaces

---

<!-- note:1781279834650 model:Basic++++ -->
**Front:** Command: create a temporary debug Pod with sleep.
**Back:** kubectl run debug --image=busybox:1.36 --restart=Never -- sleep 3600
**Tags:** ckad::commands debugging pods

---

<!-- note:1781279834651 model:Basic++++ -->
**Front:** Command: enter the temporary debug Pod.
**Back:** kubectl exec -it debug -- sh
**Tags:** ckad::commands debugging pods

---

<!-- note:1781279834652 model:Basic++++ -->
**Front:** Command: delete all completed Pods in current namespace.
**Back:** kubectl delete pod --field-selector=status.phase=Succeeded
**Tags:** ckad::commands debugging pods

---

<!-- note:1781279834653 model:Basic++++ -->
**Front:** Command: list failed Pods.
**Back:** kubectl get pods --field-selector=status.phase=Failed
**Tags:** ckad::commands debugging pods

---

<!-- note:1781279834654 model:Basic++++ -->
**Front:** Command: get Pods on a specific node.
**Back:** kubectl get pods --field-selector=spec.nodeName=&lt;node-name&gt; -A
**Tags:** ckad::commands pods scheduling

---

<!-- note:1781279834655 model:Basic++++ -->
**Front:** Command: get object as JSON and filter with jq if available.
**Back:** kubectl get pod &lt;pod&gt; -o json | jq .status.containerStatuses
**Tags:** ckad::commands debugging jsonpath

---
