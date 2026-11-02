# CKAD - Certified Kubernetes Application Developer — patterns

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `patterns` · Notes: 18 · Models: Basic++++

<!-- note:1781279834594 model:Basic++++ -->
**Front:** What objects commonly combine to expose a stateless web app externally?
**Back:** Deployment creates Pods, Service selects the Pods, Ingress routes HTTP traffic to the Service.
**Tags:** ckad::patterns deployments ingress services

---

<!-- note:1781279834595 model:Basic++++ -->
**Front:** What objects commonly combine to inject app settings?
**Back:** ConfigMap/Secret provide values; Pod/Deployment consumes them with env, envFrom, or volumes.
**Tags:** ckad::patterns configmaps pods secrets

---

<!-- note:1781279834596 model:Basic++++ -->
**Front:** What objects commonly combine for generated static content?
**Back:** Init container writes files into emptyDir; nginx/main container serves the same emptyDir mount.
**Tags:** ckad::patterns init-containers pods volumes

---

<!-- note:1781279834597 model:Basic++++ -->
**Front:** What objects commonly combine for persistent app data?
**Back:** PVC requests storage; Pod/Deployment mounts the PVC as a volume.
**Tags:** ckad::patterns pods storage

---

<!-- note:1781279834598 model:Basic++++ -->
**Front:** What objects commonly combine for secure API access from a Pod?
**Back:** ServiceAccount gives identity; Role/RoleBinding grants permissions; Pod uses serviceAccountName.
**Tags:** ckad::patterns pods rbac serviceaccounts

---

<!-- note:1781279834599 model:Basic++++ -->
**Front:** What objects commonly combine for network restriction?
**Back:** Labels identify client/server Pods; NetworkPolicy selects protected Pods and allows only required sources/ports.
**Tags:** ckad::patterns labels networkpolicy

---

<!-- note:1781279834600 model:Basic++++ -->
**Front:** Deployment + Service selector rule?
**Back:** Service spec.selector must match labels on Deployment spec.template.metadata.labels.
**Tags:** ckad::patterns deployments selectors services

---

<!-- note:1781279834601 model:Basic++++ -->
**Front:** Deployment + NetworkPolicy selector rule?
**Back:** NetworkPolicy podSelector must match labels on Pods created by the Deployment template.
**Tags:** ckad::patterns deployments networkpolicy selectors

---

<!-- note:1781279834602 model:Basic++++ -->
**Front:** Ingress + Service rule?
**Back:** Ingress backend service.name and service.port must match an existing Service in the same namespace.
**Tags:** ckad::patterns ingress services

---

<!-- note:1781279834603 model:Basic++++ -->
**Front:** Service + readiness probe relationship?
**Back:** Only Ready Pods appear as Service endpoints, so readiness failures can make a Service look broken.
**Tags:** ckad::patterns probes services

---

<!-- note:1781279834604 model:Basic++++ -->
**Front:** ConfigMap env vs ConfigMap volume: when choose env?
**Back:** Use env for simple key-value settings read at process start.
**Tags:** ckad::patterns configmaps env

---

<!-- note:1781279834605 model:Basic++++ -->
**Front:** ConfigMap env vs ConfigMap volume: when choose volume?
**Back:** Use volume for file-based configuration or when the app expects config files.
**Tags:** ckad::patterns configmaps volumes

---

<!-- note:1781279834606 model:Basic++++ -->
**Front:** Secret env vs Secret volume: when choose volume?
**Back:** Use volume for certificates, keys, token files, or when the app expects files.
**Tags:** ckad::patterns secrets volumes

---

<!-- note:1781279834607 model:Basic++++ -->
**Front:** What should a complete web Deployment YAML usually include in CKAD?
**Back:** replicas, selector, template labels, container image, ports, env/config, resources, probes, and optional securityContext.
**Tags:** ckad::patterns deployments yaml

---

<!-- note:1781279834608 model:Basic++++ -->
**Front:** What should a complete Service YAML usually include?
**Back:** type, selector, ports with port and targetPort, and optional named port or nodePort.
**Tags:** ckad::patterns services yaml

---

<!-- note:1781279834609 model:Basic++++ -->
**Front:** What should a complete NetworkPolicy YAML usually include?
**Back:** podSelector, policyTypes, ingress/egress rules, from/to selectors, and ports.
**Tags:** ckad::patterns networkpolicy yaml

---

<!-- note:1781279834610 model:Basic++++ -->
**Front:** What should a complete CronJob YAML usually include?
**Back:** schedule, concurrencyPolicy/suspend if needed, jobTemplate, Pod template, container command, and restartPolicy OnFailure/Never.
**Tags:** ckad::patterns cronjobs yaml

---

<!-- note:1781279834611 model:Basic++++ -->
**Front:** What should a complete probe task answer include?
**Back:** Correct probe type, path/port/command, timing fields, and verification via describe/events/readiness/restarts.
**Tags:** ckad::patterns debugging probes

---
