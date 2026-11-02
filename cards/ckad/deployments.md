# CKAD - Certified Kubernetes Application Developer — deployments

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `deployments` · Notes: 31 · Models: Basic++++

<!-- note:1781279834148 model:Basic++++ -->
**Front:** Command: generate Deployment YAML without creating it.
**Back:** kubectl create deployment web --image=nginx --dry-run=client -o yaml
**Tags:** ckad::deployments command yaml

---

<!-- note:1781279834157 model:Basic++++ -->
**Front:** Command: edit a live Deployment.
**Back:** kubectl edit deployment &lt;name&gt;
**Tags:** ckad::deployments command

---

<!-- note:1781279834158 model:Basic++++ -->
**Front:** Command: patch a Deployment replica count to 5.
**Back:** kubectl patch deployment &lt;name&gt; -p &#x27;{&quot;spec&quot;:{&quot;replicas&quot;:5}}&#x27;
**Tags:** ckad::deployments command

---

<!-- note:1781279834182 model:Basic++++ -->
**Front:** Which field usually contains labels used by a Service selector on a Deployment&#x27;s Pods?
**Back:** spec.template.metadata.labels in the Deployment.
**Tags:** ckad::deployments selectors yaml

---

<!-- note:1781279834183 model:Basic++++ -->
**Front:** Why must Deployment selector labels match Pod template labels?
**Back:** The Deployment manages Pods by matching spec.selector to spec.template.metadata.labels; mismatch causes errors or unmanaged Pods.
**Tags:** ckad::deployments selectors yaml

---

<!-- note:1781279834198 model:Basic++++ -->
**Front:** When should you prefer a Deployment over a bare Pod?
**Back:** For long-running replicated applications that need self-healing, rollout, scaling, and updates.
**Tags:** ckad::deployments concept pods

---

<!-- note:1781279834378 model:Basic++++ -->
**Front:** What is a Deployment?
**Back:** A controller for stateless long-running apps that manages ReplicaSets and Pods, supports scaling, rolling updates, and rollbacks.
**Tags:** ckad::deployments concept

---

<!-- note:1781279834379 model:Basic++++ -->
**Front:** What object does a Deployment create to manage Pods?
**Back:** ReplicaSet.
**Tags:** ckad::deployments concept replicasets

---

<!-- note:1781279834382 model:Basic++++ -->
**Front:** Command: create Deployment web with nginx image.
**Back:** kubectl create deployment web --image=nginx
**Tags:** ckad::deployments command

---

<!-- note:1781279834383 model:Basic++++ -->
**Front:** Command: create Deployment web with 3 replicas and port 80.
**Back:** kubectl create deployment web --image=nginx --replicas=3 --port=80
**Tags:** ckad::deployments command

---

<!-- note:1781279834384 model:Basic++++ -->
**Front:** YAML: Deployment required selector/template label relationship.
**Back:** spec:<br>  selector:<br>    matchLabels:<br>      app: web<br>  template:<br>    metadata:<br>      labels:<br>        app: web
**Tags:** ckad::deployments selectors yaml

---

<!-- note:1781279834385 model:Basic++++ -->
**Front:** YAML: Deployment replicas field.
**Back:** spec:<br>  replicas: 3
**Tags:** ckad::deployments yaml

---

<!-- note:1781279834386 model:Basic++++ -->
**Front:** YAML: Deployment Pod template container.
**Back:** spec:<br>  template:<br>    spec:<br>      containers:<br>      - name: nginx<br>        image: nginx
**Tags:** ckad::deployments pods yaml

---

<!-- note:1781279834387 model:Basic++++ -->
**Front:** Which Deployment field is immutable and commonly causes errors if changed?
**Back:** spec.selector.
**Tags:** ckad::deployments debugging yaml

---

<!-- note:1781279834388 model:Basic++++ -->
**Front:** Command: scale Deployment web to 5.
**Back:** kubectl scale deployment web --replicas=5
**Tags:** ckad::deployments command

---

<!-- note:1781279834389 model:Basic++++ -->
**Front:** Command: set Deployment image.
**Back:** kubectl set image deployment/web nginx=nginx:1.25
**Tags:** ckad::deployments command

---

<!-- note:1781279834390 model:Basic++++ -->
**Front:** Command: check rollout status.
**Back:** kubectl rollout status deployment/web
**Tags:** ckad::deployments command rollout

---

<!-- note:1781279834391 model:Basic++++ -->
**Front:** Command: show rollout history.
**Back:** kubectl rollout history deployment/web
**Tags:** ckad::deployments command rollout

---

<!-- note:1781279834392 model:Basic++++ -->
**Front:** Command: undo latest rollout.
**Back:** kubectl rollout undo deployment/web
**Tags:** ckad::deployments command rollout

---

<!-- note:1781279834393 model:Basic++++ -->
**Front:** Command: undo to a specific revision.
**Back:** kubectl rollout undo deployment/web --to-revision=&lt;revision&gt;
**Tags:** ckad::deployments command rollout

---

<!-- note:1781279834394 model:Basic++++ -->
**Front:** Command: pause Deployment rollout.
**Back:** kubectl rollout pause deployment/web
**Tags:** ckad::deployments command rollout

---

<!-- note:1781279834395 model:Basic++++ -->
**Front:** Command: resume Deployment rollout.
**Back:** kubectl rollout resume deployment/web
**Tags:** ckad::deployments command rollout

---

<!-- note:1781279834396 model:Basic++++ -->
**Front:** Command: restart a Deployment rollout.
**Back:** kubectl rollout restart deployment/web
**Tags:** ckad::deployments command rollout

---

<!-- note:1781279834397 model:Basic++++ -->
**Front:** How do you record a useful change cause for rollout history?
**Back:** Annotate the Deployment, e.g. kubectl annotate deployment web kubernetes.io/change-cause='update image to nginx:1.25' --overwrite
**Tags:** ckad::deployments command rollout

---

<!-- note:1781279834398 model:Basic++++ -->
**Front:** What is RollingUpdate strategy?
**Back:** Default Deployment strategy that gradually creates new Pods and removes old Pods while maintaining availability.
**Tags:** ckad::deployments concept rollout

---

<!-- note:1781279834399 model:Basic++++ -->
**Front:** What is Recreate strategy?
**Back:** Deployment strategy that terminates old Pods before creating new Pods, causing downtime but avoiding overlap.
**Tags:** ckad::deployments concept rollout

---

<!-- note:1781279834400 model:Basic++++ -->
**Front:** YAML: set Deployment strategy Recreate.
**Back:** strategy:<br>  type: Recreate
**Tags:** ckad::deployments rollout yaml

---

<!-- note:1781279834401 model:Basic++++ -->
**Front:** YAML: set RollingUpdate maxSurge and maxUnavailable.
**Back:** strategy:<br>  type: RollingUpdate<br>  rollingUpdate:<br>    maxSurge: 1<br>    maxUnavailable: 0
**Tags:** ckad::deployments rollout yaml

---

<!-- note:1781279834402 model:Basic++++ -->
**Front:** What does maxSurge mean?
**Back:** How many extra Pods above desired replicas can exist during a rolling update.
**Tags:** ckad::deployments concept rollout

---

<!-- note:1781279834403 model:Basic++++ -->
**Front:** What does maxUnavailable mean?
**Back:** How many desired replicas may be unavailable during a rolling update.
**Tags:** ckad::deployments concept rollout

---

<!-- note:1781279834404 model:Basic++++ -->
**Front:** What should you inspect if a Deployment rollout is stuck?
**Back:** kubectl rollout status, kubectl get pods, kubectl describe deployment, describe failing Pods, logs, events, image names, probes, resources, and config.
**Tags:** ckad::deployments debugging

---
