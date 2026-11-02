# CKAD - Certified Kubernetes Application Developer — probes

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `probes` · Notes: 17 · Models: Basic++++

<!-- note:1781279834505 model:Basic++++ -->
**Front:** What is a liveness probe?
**Back:** A health check that restarts the container when it fails repeatedly.
**Tags:** ckad::probes concept liveness

---

<!-- note:1781279834506 model:Basic++++ -->
**Front:** What is a readiness probe?
**Back:** A health check that controls whether the Pod is considered ready to receive Service traffic.
**Tags:** ckad::probes concept readiness

---

<!-- note:1781279834507 model:Basic++++ -->
**Front:** What is a startup probe?
**Back:** A probe for slow-starting apps; liveness/readiness are disabled until startup succeeds.
**Tags:** ckad::probes concept startup

---

<!-- note:1781279834508 model:Basic++++ -->
**Front:** When should you use startupProbe?
**Back:** When an app has a long initial startup and liveness might otherwise kill it too early.
**Tags:** ckad::probes concept startup

---

<!-- note:1781279834509 model:Basic++++ -->
**Front:** YAML: HTTP liveness probe.
**Back:** livenessProbe:<br>  httpGet:<br>    path: /healthz<br>    port: 8080<br>  initialDelaySeconds: 10<br>  periodSeconds: 5
**Tags:** ckad::probes liveness yaml

---

<!-- note:1781279834510 model:Basic++++ -->
**Front:** YAML: TCP readiness probe.
**Back:** readinessProbe:<br>  tcpSocket:<br>    port: 8080<br>  initialDelaySeconds: 5<br>  periodSeconds: 10
**Tags:** ckad::probes readiness yaml

---

<!-- note:1781279834511 model:Basic++++ -->
**Front:** YAML: exec probe.
**Back:** livenessProbe:<br>  exec:<br>    command: ["cat", "/tmp/healthy"]<br>  periodSeconds: 5
**Tags:** ckad::probes yaml

---

<!-- note:1781279834512 model:Basic++++ -->
**Front:** YAML: startup probe using HTTP.
**Back:** startupProbe:<br>  httpGet:<br>    path: /startup<br>    port: 8080<br>  failureThreshold: 30<br>  periodSeconds: 10
**Tags:** ckad::probes startup yaml

---

<!-- note:1781279834513 model:Basic++++ -->
**Front:** What does initialDelaySeconds do?
**Back:** Waits that many seconds after container start before beginning probe checks.
**Tags:** ckad::probes yaml

---

<!-- note:1781279834514 model:Basic++++ -->
**Front:** What does periodSeconds do in a probe?
**Back:** How often the probe runs.
**Tags:** ckad::probes yaml

---

<!-- note:1781279834515 model:Basic++++ -->
**Front:** What does timeoutSeconds do in a probe?
**Back:** How long Kubernetes waits for a probe response before treating it as failed.
**Tags:** ckad::probes yaml

---

<!-- note:1781279834516 model:Basic++++ -->
**Front:** What does failureThreshold do in a probe?
**Back:** Number of consecutive failures before Kubernetes takes the failure action.
**Tags:** ckad::probes yaml

---

<!-- note:1781279834517 model:Basic++++ -->
**Front:** What does successThreshold do in a readiness probe?
**Back:** Number of consecutive successes needed to mark the container ready after failure; for liveness/startup it must be 1.
**Tags:** ckad::probes yaml

---

<!-- note:1781279834518 model:Basic++++ -->
**Front:** Can probes use named ports?
**Back:** Yes for HTTP/TCP probes; use the container port name.
**Tags:** ckad::probes services yaml

---

<!-- note:1781279834519 model:Basic++++ -->
**Front:** What is the Service impact of a failing readiness probe?
**Back:** The Pod is removed from Service endpoints and stops receiving Service traffic.
**Tags:** ckad::probes concept services

---

<!-- note:1781279834520 model:Basic++++ -->
**Front:** What is the impact of a failing liveness probe?
**Back:** The kubelet restarts the container.
**Tags:** ckad::probes concept liveness

---

<!-- note:1781279834521 model:Basic++++ -->
**Front:** What should you inspect if a Pod repeatedly restarts after adding a liveness probe?
**Back:** Probe path/port/scheme, initialDelaySeconds, app startup time, logs, and events from kubectl describe pod.
**Tags:** ckad::probes debugging

---
