# CKAD - Certified Kubernetes Application Developer — ingress

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `ingress` · Notes: 14 · Models: Basic++++

<!-- note:1781279834472 model:Basic++++ -->
**Front:** What is Ingress?
**Back:** An HTTP/HTTPS routing resource that maps external host/path traffic to Services, implemented by an Ingress controller.
**Tags:** ckad::ingress concept

---

<!-- note:1781279834473 model:Basic++++ -->
**Front:** What must exist for Ingress to actually route traffic?
**Back:** An Ingress controller must be installed and running in the cluster.
**Tags:** ckad::ingress concept

---

<!-- note:1781279834474 model:Basic++++ -->
**Front:** What does ingressClassName do?
**Back:** Selects which Ingress controller should handle the Ingress.
**Tags:** ckad::ingress yaml

---

<!-- note:1781279834475 model:Basic++++ -->
**Front:** Command: create Ingress for host example.com path / to service web:80.
**Back:** kubectl create ingress web --rule='example.com/=web:80'
**Tags:** ckad::ingress command

---

<!-- note:1781279834476 model:Basic++++ -->
**Front:** YAML: basic Ingress rule to Service web:80.
**Back:** apiVersion: networking.k8s.io/v1<br>kind: Ingress<br>metadata:<br>  name: web<br>spec:<br>  ingressClassName: nginx<br>  rules:<br>  - host: example.com<br>    http:<br>      paths:<br>      - path: /<br>        pathType: Prefix<br>        backend:<br>          service:<br>            name: web<br>            port:<br>              number: 80
**Tags:** ckad::ingress yaml

---

<!-- note:1781279834477 model:Basic++++ -->
**Front:** What are valid Ingress pathType values?
**Back:** Exact, Prefix, ImplementationSpecific.
**Tags:** ckad::ingress yaml

---

<!-- note:1781279834478 model:Basic++++ -->
**Front:** What does pathType Prefix mean?
**Back:** Matches URL paths by prefix according to Kubernetes path matching rules.
**Tags:** ckad::ingress concept

---

<!-- note:1781279834479 model:Basic++++ -->
**Front:** What does pathType Exact mean?
**Back:** Matches the exact URL path only.
**Tags:** ckad::ingress concept

---

<!-- note:1781279834480 model:Basic++++ -->
**Front:** YAML: Ingress backend by named Service port.
**Back:** backend:<br>  service:<br>    name: web<br>    port:<br>      name: http
**Tags:** ckad::ingress services yaml

---

<!-- note:1781279834481 model:Basic++++ -->
**Front:** YAML: Ingress TLS section.
**Back:** tls:<br>- hosts:<br>  - example.com<br>  secretName: tls-secret
**Tags:** ckad::ingress secrets yaml

---

<!-- note:1781279834482 model:Basic++++ -->
**Front:** What Secret type is commonly used for Ingress TLS?
**Back:** kubernetes.io/tls, usually created with kubectl create secret tls.
**Tags:** ckad::ingress concept secrets

---

<!-- note:1781279834483 model:Basic++++ -->
**Front:** What should you check if Ingress returns no app response?
**Back:** Ingress class/controller, rules/host/path, backend Service name/port, Service endpoints, and app readiness.
**Tags:** ckad::ingress debugging

---

<!-- note:1781279834484 model:Basic++++ -->
**Front:** Command: list Ingress resources.
**Back:** kubectl get ingress
**Tags:** ckad::ingress command

---

<!-- note:1781279834485 model:Basic++++ -->
**Front:** Command: describe an Ingress.
**Back:** kubectl describe ingress &lt;name&gt;
**Tags:** ckad::ingress command debugging

---
