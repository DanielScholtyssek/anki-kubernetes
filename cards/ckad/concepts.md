# CKAD - Certified Kubernetes Application Developer — concepts

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `concepts` · Notes: 10 · Models: Basic++++

<!-- note:1781279834656 model:Basic++++ -->
**Front:** Why is a Deployment&#x27;s Service usually stable through rollouts?
**Back:** The Service selects labels on Pods; as new ReplicaSet Pods get the same labels and become Ready, traffic shifts automatically.
**Tags:** ckad::concepts deployments services

---

<!-- note:1781279834657 model:Basic++++ -->
**Front:** Why can a Service have endpoints even if containerPort is omitted?
**Back:** Services route to Pod IP and targetPort; containerPort is metadata/documentation unless using named ports or tooling that reads it.
**Tags:** ckad::concepts pods services

---

<!-- note:1781279834658 model:Basic++++ -->
**Front:** Why can a Pod be Running but absent from Service endpoints?
**Back:** It may not match the Service selector or may not be Ready.
**Tags:** ckad::concepts probes services

---

<!-- note:1781279834659 model:Basic++++ -->
**Front:** Why can a NetworkPolicy appear to do nothing?
**Back:** The cluster CNI may not enforce NetworkPolicy, or the policy may not select the intended Pods/direction.
**Tags:** ckad::concepts debugging networkpolicy

---

<!-- note:1781279834660 model:Basic++++ -->
**Front:** Why should CKAD answers prefer simple YAML over clever shell pipelines?
**Back:** Simple manifests are easier to verify and fix under time pressure; clever one-liners can hide mistakes.
**Tags:** ckad::concepts labs

---

<!-- note:1781279834661 model:Basic++++ -->
**Front:** What is the strongest sign that your Service selector is correct?
**Back:** kubectl get endpoints &lt;service&gt; shows the expected Pod IPs and ports.
**Tags:** ckad::concepts selectors services

---

<!-- note:1781279834662 model:Basic++++ -->
**Front:** What is the strongest sign that your Deployment is healthy?
**Back:** kubectl rollout status succeeds and desired/current/ready/up-to-date replicas match.
**Tags:** ckad::concepts deployments rollout

---

<!-- note:1781279834663 model:Basic++++ -->
**Front:** What is the strongest sign that your NetworkPolicy allow rule works?
**Back:** A labelled allowed client can connect, while an unlabelled/disallowed client cannot.
**Tags:** ckad::concepts debugging networkpolicy

---

<!-- note:1781279834664 model:Basic++++ -->
**Front:** What is the strongest sign that your ConfigMap volume is correct?
**Back:** Inside the Pod, the expected files exist at the mountPath with expected contents.
**Tags:** ckad::concepts configmaps volumes

---

<!-- note:1781279834665 model:Basic++++ -->
**Front:** What is the strongest sign that your Secret env injection is correct?
**Back:** Inside the Pod, the expected environment variable exists with the expected value, without exposing it unnecessarily in logs.
**Tags:** ckad::concepts env secrets

---
