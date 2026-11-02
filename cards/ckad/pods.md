# CKAD - Certified Kubernetes Application Developer — pods

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `pods` · Notes: 39 · Models: Basic++++

<!-- note:1781279834144 model:Basic++++ -->
**Front:** Command: list Pods in all namespaces.
**Back:** kubectl get pods -A
**Tags:** ckad::pods command namespaces

---

<!-- note:1781279834147 model:Basic++++ -->
**Front:** Command: generate Pod YAML for an nginx Pod without creating it.
**Back:** kubectl run nginx --image=nginx --dry-run=client -o yaml
**Tags:** ckad::pods command yaml

---

<!-- note:1781279834160 model:Basic++++ -->
**Front:** Command: wait for a Pod to become Ready.
**Back:** kubectl wait --for=condition=Ready pod/&lt;pod-name&gt; --timeout=60s
**Tags:** ckad::pods command debugging

---

<!-- note:1781279834164 model:Basic++++ -->
**Front:** Command: extract a Pod IP with jsonpath.
**Back:** kubectl get pod &lt;pod&gt; -o jsonpath='{.status.podIP}'
**Tags:** ckad::pods command jsonpath

---

<!-- note:1781279834196 model:Basic++++ -->
**Front:** What is a Pod?
**Back:** The smallest deployable Kubernetes unit: one or more containers sharing network namespace, volumes, and lifecycle.
**Tags:** ckad::pods concept

---

<!-- note:1781279834197 model:Basic++++ -->
**Front:** When should you create a bare Pod directly in CKAD?
**Back:** For simple one-off tasks, test clients, debug Pods, or when the question explicitly asks for a Pod.
**Tags:** ckad::pods concept

---

<!-- note:1781279834199 model:Basic++++ -->
**Front:** What do containers in the same Pod share?
**Back:** They share the same Pod IP, localhost network namespace, and any volumes mounted into both containers.
**Tags:** ckad::pods concept

---

<!-- note:1781279834200 model:Basic++++ -->
**Front:** Can two containers in the same Pod talk via localhost?
**Back:** Yes, because containers in a Pod share the same network namespace.
**Tags:** ckad::pods concept networking

---

<!-- note:1781279834201 model:Basic++++ -->
**Front:** Minimal Pod YAML?
**Back:** apiVersion: v1<br>kind: Pod<br>metadata:<br>  name: nginx<br>spec:<br>  containers:<br>  - name: nginx<br>    image: nginx
**Tags:** ckad::pods yaml

---

<!-- note:1781279834202 model:Basic++++ -->
**Front:** Command: create a bare nginx Pod.
**Back:** kubectl run nginx --image=nginx --restart=Never
**Tags:** ckad::pods command

---

<!-- note:1781279834203 model:Basic++++ -->
**Front:** Command: create a Pod with containerPort 80.
**Back:** kubectl run nginx --image=nginx --restart=Never --port=80
**Tags:** ckad::pods command

---

<!-- note:1781279834204 model:Basic++++ -->
**Front:** Does containerPort expose a Pod outside the cluster?
**Back:** No. containerPort documents/listens inside the Pod spec; use a Service or port-forward to access it.
**Tags:** ckad::pods concept services

---

<!-- note:1781279834205 model:Basic++++ -->
**Front:** YAML: set a container image in a Pod.
**Back:** spec:<br>  containers:<br>  - name: app<br>    image: nginx:1.25
**Tags:** ckad::pods yaml

---

<!-- note:1781279834206 model:Basic++++ -->
**Front:** YAML: set containerPort 8080.
**Back:** ports:<br>- containerPort: 8080
**Tags:** ckad::pods networking yaml

---

<!-- note:1781279834207 model:Basic++++ -->
**Front:** YAML: set restartPolicy Never on a Pod.
**Back:** spec:<br>  restartPolicy: Never
**Tags:** ckad::pods yaml

---

<!-- note:1781279834208 model:Basic++++ -->
**Front:** What are valid Pod restartPolicy values?
**Back:** Always, OnFailure, Never.
**Tags:** ckad::pods yaml

---

<!-- note:1781279834209 model:Basic++++ -->
**Front:** Default Pod restartPolicy?
**Back:** Always.
**Tags:** ckad::pods yaml

---

<!-- note:1781279834211 model:Basic++++ -->
**Front:** Docker ENTRYPOINT maps to which Kubernetes field?
**Back:** command.
**Tags:** ckad::pods command yaml

---

<!-- note:1781279834212 model:Basic++++ -->
**Front:** Docker CMD maps to which Kubernetes field?
**Back:** args.
**Tags:** ckad::pods command yaml

---

<!-- note:1781279834213 model:Basic++++ -->
**Front:** YAML: run command sleep 3600 in a container.
**Back:** command: ["sleep"]<br>args: ["3600"]
**Tags:** ckad::pods command yaml

---

<!-- note:1781279834214 model:Basic++++ -->
**Front:** YAML: run a shell command in a container.
**Back:** command: ["/bin/sh", "-c"]<br>args: ["echo hello; sleep 3600"]
**Tags:** ckad::pods command yaml

---

<!-- note:1781279834215 model:Basic++++ -->
**Front:** Command: run busybox env and delete Pod afterwards.
**Back:** kubectl run busybox --image=busybox --restart=Never -it --rm -- env
**Tags:** ckad::pods command

---

<!-- note:1781279834217 model:Basic++++ -->
**Front:** Command: show Pod logs.
**Back:** kubectl logs &lt;pod&gt;
**Tags:** ckad::pods command logs

---

<!-- note:1781279834218 model:Basic++++ -->
**Front:** Command: show logs for a specific container in a multi-container Pod.
**Back:** kubectl logs &lt;pod&gt; -c &lt;container&gt;
**Tags:** ckad::pods command logs

---

<!-- note:1781279834219 model:Basic++++ -->
**Front:** Command: show previous crashed container logs.
**Back:** kubectl logs &lt;pod&gt; --previous
**Tags:** ckad::pods command debugging logs

---

<!-- note:1781279834220 model:Basic++++ -->
**Front:** Command: exec into a Pod shell.
**Back:** kubectl exec -it &lt;pod&gt; -- /bin/sh
**Tags:** ckad::pods command exec

---

<!-- note:1781279834221 model:Basic++++ -->
**Front:** Command: exec into a specific container in a Pod.
**Back:** kubectl exec -it &lt;pod&gt; -c &lt;container&gt; -- /bin/sh
**Tags:** ckad::pods command exec

---

<!-- note:1781279834222 model:Basic++++ -->
**Front:** Command: copy a file from local machine into a Pod.
**Back:** kubectl cp ./file.txt &lt;pod&gt;:/tmp/file.txt
**Tags:** ckad::pods command

---

<!-- note:1781279834223 model:Basic++++ -->
**Front:** Command: copy a file from a specific container in a Pod.
**Back:** kubectl cp ./file.txt &lt;pod&gt;:/tmp/file.txt -c &lt;container&gt;
**Tags:** ckad::pods command

---

<!-- note:1781279834224 model:Basic++++ -->
**Front:** Command: describe a Pod for events and detailed state.
**Back:** kubectl describe pod &lt;pod&gt;
**Tags:** ckad::pods command debugging

---

<!-- note:1781279834225 model:Basic++++ -->
**Front:** Command: get Pod YAML.
**Back:** kubectl get pod &lt;pod&gt; -o yaml
**Tags:** ckad::pods command yaml

---

<!-- note:1781279834226 model:Basic++++ -->
**Front:** Command: get Pod wide output including IP and node.
**Back:** kubectl get pods -o wide
**Tags:** ckad::pods command

---

<!-- note:1781279834227 model:Basic++++ -->
**Front:** Command: change a bare Pod container image.
**Back:** kubectl set image pod/&lt;pod&gt; &lt;container&gt;=&lt;image&gt;:&lt;tag&gt;
**Tags:** ckad::pods command

---

<!-- note:1781279834228 model:Basic++++ -->
**Front:** Why is updating a bare Pod image less common than updating a Deployment image?
**Back:** Bare Pods are not rollout-managed; Deployments provide controlled rollout, rollback, and self-healing.
**Tags:** ckad::pods concept deployments

---

<!-- note:1781279834243 model:Basic++++ -->
**Front:** What is a multi-container Pod best used for?
**Back:** Tightly coupled helper containers such as sidecars, adapters, or log shippers that must share lifecycle, localhost, or volumes.
**Tags:** ckad::pods concept

---

<!-- note:1781279834244 model:Basic++++ -->
**Front:** YAML: two containers in one Pod structure.
**Back:** spec:<br>  containers:<br>  - name: app<br>    image: nginx<br>  - name: sidecar<br>    image: busybox<br>    command: ["sh", "-c", "sleep 3600"]
**Tags:** ckad::pods yaml

---

<!-- note:1781279834245 model:Basic++++ -->
**Front:** What is a sidecar container?
**Back:** A helper container in the same Pod that supports the main app, often for logging, proxying, syncing, or file generation.
**Tags:** ckad::pods concept

---

<!-- note:1781279834458 model:Basic++++ -->
**Front:** YAML: container named port http.
**Back:** ports:<br>- name: http<br>  containerPort: 8080
**Tags:** ckad::pods services yaml

---

<!-- note:1781279834465 model:Basic++++ -->
**Front:** Command: port-forward local 8080 to Pod port 80.
**Back:** kubectl port-forward pod/&lt;pod-name&gt; 8080:80
**Tags:** ckad::pods command debugging services

---
