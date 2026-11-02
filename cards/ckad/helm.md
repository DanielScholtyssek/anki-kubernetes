# CKAD - Certified Kubernetes Application Developer — helm

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `helm` · Notes: 24 · Models: Basic++++

<!-- note:1781279834552 model:Basic++++ -->
**Front:** What is Helm?
**Back:** A Kubernetes package manager that installs, upgrades, templates, and manages applications packaged as charts.
**Tags:** ckad::helm concept

---

<!-- note:1781279834553 model:Basic++++ -->
**Front:** What is a Helm chart?
**Back:** A package containing Kubernetes templates, default values, and metadata for an application.
**Tags:** ckad::helm concept

---

<!-- note:1781279834554 model:Basic++++ -->
**Front:** What is a Helm release?
**Back:** An installed instance of a chart with chosen values in a namespace.
**Tags:** ckad::helm concept

---

<!-- note:1781279834555 model:Basic++++ -->
**Front:** Command: add a Helm repo.
**Back:** helm repo add &lt;name&gt; &lt;url&gt;
**Tags:** ckad::helm command

---

<!-- note:1781279834556 model:Basic++++ -->
**Front:** Command: update Helm repo indexes.
**Back:** helm repo update
**Tags:** ckad::helm command

---

<!-- note:1781279834557 model:Basic++++ -->
**Front:** Command: search Helm repos for nginx.
**Back:** helm search repo nginx
**Tags:** ckad::helm command

---

<!-- note:1781279834558 model:Basic++++ -->
**Front:** Command: install chart as a release.
**Back:** helm install &lt;release&gt; &lt;repo/chart&gt;
**Tags:** ckad::helm command

---

<!-- note:1781279834559 model:Basic++++ -->
**Front:** Command: install chart into namespace and create namespace.
**Back:** helm install &lt;release&gt; &lt;repo/chart&gt; -n &lt;namespace&gt; --create-namespace
**Tags:** ckad::helm command namespaces

---

<!-- note:1781279834560 model:Basic++++ -->
**Front:** Command: upgrade a Helm release.
**Back:** helm upgrade &lt;release&gt; &lt;repo/chart&gt;
**Tags:** ckad::helm command

---

<!-- note:1781279834561 model:Basic++++ -->
**Front:** Command: install or upgrade in one command.
**Back:** helm upgrade --install &lt;release&gt; &lt;repo/chart&gt;
**Tags:** ckad::helm command

---

<!-- note:1781279834562 model:Basic++++ -->
**Front:** Command: pass one value with Helm.
**Back:** helm install &lt;release&gt; &lt;chart&gt; --set key=value
**Tags:** ckad::helm command

---

<!-- note:1781279834563 model:Basic++++ -->
**Front:** Command: pass values file with Helm.
**Back:** helm install &lt;release&gt; &lt;chart&gt; -f values.yaml
**Tags:** ckad::helm command yaml

---

<!-- note:1781279834564 model:Basic++++ -->
**Front:** Command: render Helm templates without installing.
**Back:** helm template &lt;release&gt; &lt;chart&gt; -f values.yaml
**Tags:** ckad::helm command yaml

---

<!-- note:1781279834565 model:Basic++++ -->
**Front:** Command: lint a Helm chart.
**Back:** helm lint &lt;chart-dir&gt;
**Tags:** ckad::helm command

---

<!-- note:1781279834566 model:Basic++++ -->
**Front:** Command: list Helm releases in all namespaces.
**Back:** helm list -A
**Tags:** ckad::helm command

---

<!-- note:1781279834567 model:Basic++++ -->
**Front:** Command: show Helm release status.
**Back:** helm status &lt;release&gt; -n &lt;namespace&gt;
**Tags:** ckad::helm command

---

<!-- note:1781279834568 model:Basic++++ -->
**Front:** Command: show Helm release history.
**Back:** helm history &lt;release&gt; -n &lt;namespace&gt;
**Tags:** ckad::helm command

---

<!-- note:1781279834569 model:Basic++++ -->
**Front:** Command: rollback Helm release to revision 2.
**Back:** helm rollback &lt;release&gt; 2 -n &lt;namespace&gt;
**Tags:** ckad::helm command

---

<!-- note:1781279834570 model:Basic++++ -->
**Front:** Command: uninstall Helm release.
**Back:** helm uninstall &lt;release&gt; -n &lt;namespace&gt;
**Tags:** ckad::helm command

---

<!-- note:1781279834571 model:Basic++++ -->
**Front:** Command: show default chart values.
**Back:** helm show values &lt;repo/chart&gt;
**Tags:** ckad::helm command

---

<!-- note:1781279834572 model:Basic++++ -->
**Front:** Command: get values used by a release.
**Back:** helm get values &lt;release&gt; -n &lt;namespace&gt;
**Tags:** ckad::helm command

---

<!-- note:1781279834573 model:Basic++++ -->
**Front:** What does Helm --wait do?
**Back:** Waits until Kubernetes resources are ready before marking install/upgrade successful.
**Tags:** ckad::helm command concept

---

<!-- note:1781279834574 model:Basic++++ -->
**Front:** What does Helm --atomic do?
**Back:** Rolls back changes if install/upgrade fails; it implies waiting behavior.
**Tags:** ckad::helm command concept

---

<!-- note:1781279834575 model:Basic++++ -->
**Front:** What should you inspect after a Helm install fails?
**Back:** helm status/history, rendered templates, kubectl get all, describe failing resources, events, values, and namespace.
**Tags:** ckad::helm debugging

---
