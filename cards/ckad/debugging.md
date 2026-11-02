# CKAD - Certified Kubernetes Application Developer — debugging

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `debugging` · Notes: 31 · Models: Basic++++

<!-- note:1781279834167 model:Basic++++ -->
**Front:** Command: show events sorted by time.
**Back:** kubectl get events --sort-by=.metadata.creationTimestamp
**Tags:** ckad::debugging command

---

<!-- note:1781279834216 model:Basic++++ -->
**Front:** Command: run temporary curl Pod to test a URL.
**Back:** kubectl run tmp --image=curlimages/curl --restart=Never -it --rm -- curl -s http://&lt;service&gt;:&lt;port&gt;
**Tags:** ckad::debugging command networking

---

<!-- note:1781279834229 model:Basic++++ -->
**Front:** What does ImagePullBackOff usually mean?
**Back:** Kubernetes cannot pull the image, commonly due to wrong image name/tag, registry auth, or network issue.
**Tags:** ckad::debugging pods

---

<!-- note:1781279834230 model:Basic++++ -->
**Front:** What does CrashLoopBackOff usually mean?
**Back:** The container starts then exits repeatedly; inspect logs, command/args, env, config, probes, and dependencies.
**Tags:** ckad::debugging pods

---

<!-- note:1781279834231 model:Basic++++ -->
**Front:** What does Pending usually mean for a Pod?
**Back:** The Pod has not been scheduled or cannot start due to resources, PVCs, selectors, taints, or admission issues.
**Tags:** ckad::debugging pods scheduling

---

<!-- note:1781279834232 model:Basic++++ -->
**Front:** What does Running but not Ready usually suggest?
**Back:** The container is running but readiness probe or readiness condition is failing; Service endpoints may not include it.
**Tags:** ckad::debugging pods probes services

---

<!-- note:1781279834252 model:Basic++++ -->
**Front:** What is an ephemeral debug container?
**Back:** A temporary container added to an existing Pod for debugging, often when the app image lacks a shell or tools.
**Tags:** ckad::debugging concept pods

---

<!-- note:1781279834253 model:Basic++++ -->
**Front:** Command: add an ephemeral debug container to a Pod.
**Back:** kubectl debug -it &lt;pod&gt; --image=busybox --target=&lt;container&gt; -- /bin/sh
**Tags:** ckad::debugging command pods

---

<!-- note:1781279834254 model:Basic++++ -->
**Front:** Do ephemeral containers restart or define normal app workload?
**Back:** No. They are for debugging and are not normal restartable app containers.
**Tags:** ckad::debugging concept pods

---

<!-- note:1781279834522 model:Basic++++ -->
**Front:** What is the universal first debugging command for a broken resource?
**Back:** kubectl describe &lt;resource&gt; &lt;name&gt;
**Tags:** ckad::debugging command

---

<!-- note:1781279834523 model:Basic++++ -->
**Front:** Command: list Pods with status and node details.
**Back:** kubectl get pods -o wide
**Tags:** ckad::debugging command pods

---

<!-- note:1781279834524 model:Basic++++ -->
**Front:** Command: show all resources in namespace.
**Back:** kubectl get all
**Tags:** ckad::debugging command

---

<!-- note:1781279834525 model:Basic++++ -->
**Front:** Command: show logs from all containers in a Pod.
**Back:** kubectl logs &lt;pod&gt; --all-containers=true
**Tags:** ckad::debugging command logs

---

<!-- note:1781279834526 model:Basic++++ -->
**Front:** Command: stream logs from a Pod.
**Back:** kubectl logs -f &lt;pod&gt;
**Tags:** ckad::debugging command logs

---

<!-- note:1781279834527 model:Basic++++ -->
**Front:** Command: show logs for Pods matching a label.
**Back:** kubectl logs -l app=web
**Tags:** ckad::debugging command labels logs

---

<!-- note:1781279834528 model:Basic++++ -->
**Front:** Command: execute env inside a Pod.
**Back:** kubectl exec &lt;pod&gt; -- env
**Tags:** ckad::debugging command env

---

<!-- note:1781279834529 model:Basic++++ -->
**Front:** Command: test Service DNS from a temporary busybox Pod.
**Back:** kubectl run test --image=busybox:1.36 --restart=Never -it --rm -- wget -O- http://&lt;service&gt;:&lt;port&gt;
**Tags:** ckad::debugging command services

---

<!-- note:1781279834530 model:Basic++++ -->
**Front:** Command: run nslookup in temporary busybox Pod.
**Back:** kubectl run dns --image=busybox:1.36 --restart=Never -it --rm -- nslookup &lt;service&gt;
**Tags:** ckad::debugging command dns services

---

<!-- note:1781279834531 model:Basic++++ -->
**Front:** Command: show container image from Pod with jsonpath.
**Back:** kubectl get pod &lt;pod&gt; -o jsonpath='{.spec.containers[*].image}'
**Tags:** ckad::debugging command jsonpath

---

<!-- note:1781279834532 model:Basic++++ -->
**Front:** Command: show Pod phase with jsonpath.
**Back:** kubectl get pod &lt;pod&gt; -o jsonpath='{.status.phase}'
**Tags:** ckad::debugging command jsonpath

---

<!-- note:1781279834533 model:Basic++++ -->
**Front:** Command: custom columns for Pod name and phase.
**Back:** kubectl get pods -o custom-columns=NAME:.metadata.name,PHASE:.status.phase
**Tags:** ckad::debugging command

---

<!-- note:1781279834534 model:Basic++++ -->
**Front:** Command: delete all Pods with label app=web.
**Back:** kubectl delete pods -l app=web
**Tags:** ckad::debugging command labels

---

<!-- note:1781279834535 model:Basic++++ -->
**Front:** What are the first checks for a Service that does not work?
**Back:** Service selector, Pod labels, Pod readiness, endpoints, targetPort/containerPort, namespace, and NetworkPolicy.
**Tags:** ckad::debugging services

---

<!-- note:1781279834536 model:Basic++++ -->
**Front:** What are the first checks for a ConfigMap/Secret not visible in app?
**Back:** Correct name/key, env vs volume method, namespace, Pod restarted if env var changed, mount path/subPath, and file permissions.
**Tags:** ckad::debugging configmaps secrets

---

<!-- note:1781279834537 model:Basic++++ -->
**Front:** What are the first checks for a failed rollout?
**Back:** Image pull, command/args, probes, resources, config, volume mounts, events, and ReplicaSet/Pod status.
**Tags:** ckad::debugging deployments

---

<!-- note:1781279834538 model:Basic++++ -->
**Front:** What are the first checks for network policy failures?
**Back:** Selected Pods, policyTypes, namespace labels, pod labels, ports, DNS egress, and whether CNI enforces NetworkPolicy.
**Tags:** ckad::debugging networkpolicy

---

<!-- note:1781279834539 model:Basic++++ -->
**Front:** What is the quickest way to fix wrong immutable Pod fields?
**Back:** Regenerate/edit YAML and recreate the Pod if the task permits: kubectl replace --force -f file.yaml.
**Tags:** ckad::debugging pods yaml

---

<!-- note:1781279834540 model:Basic++++ -->
**Front:** What does CreateContainerConfigError often suggest?
**Back:** Invalid/missing ConfigMap, Secret, volume, env reference, or other container configuration problem.
**Tags:** ckad::debugging pods

---

<!-- note:1781279834541 model:Basic++++ -->
**Front:** What does OOMKilled mean?
**Back:** The container exceeded its memory limit and was killed.
**Tags:** ckad::debugging resources

---

<!-- note:1781279834542 model:Basic++++ -->
**Front:** What does ErrImagePull mean?
**Back:** Initial image pull failed; inspect image name, tag, registry, and credentials.
**Tags:** ckad::debugging pods

---

<!-- note:1781279834543 model:Basic++++ -->
**Front:** What does Completed mean for a Pod?
**Back:** The container process exited successfully; expected for one-off Pods/Jobs, not for long-running apps.
**Tags:** ckad::debugging jobs pods

---
