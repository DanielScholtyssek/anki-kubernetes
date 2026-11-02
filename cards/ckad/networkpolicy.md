# CKAD - Certified Kubernetes Application Developer — networkpolicy

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `networkpolicy` · Notes: 19 · Models: Basic++++

<!-- note:1781279834486 model:Basic++++ -->
**Front:** What is a NetworkPolicy?
**Back:** A namespaced resource that controls allowed ingress and/or egress traffic for selected Pods, if the CNI supports policies.
**Tags:** ckad::networkpolicy concept

---

<!-- note:1781279834487 model:Basic++++ -->
**Front:** What does podSelector select in a NetworkPolicy?
**Back:** The Pods the policy applies to, in the same namespace as the NetworkPolicy.
**Tags:** ckad::networkpolicy selectors yaml

---

<!-- note:1781279834488 model:Basic++++ -->
**Front:** What happens to a Pod with no NetworkPolicy selecting it?
**Back:** It is non-isolated for the relevant direction, so traffic is allowed by default.
**Tags:** ckad::networkpolicy concept

---

<!-- note:1781279834489 model:Basic++++ -->
**Front:** What happens when a NetworkPolicy selects a Pod for ingress?
**Back:** The Pod becomes isolated for ingress; only ingress allowed by policies is permitted.
**Tags:** ckad::networkpolicy concept

---

<!-- note:1781279834490 model:Basic++++ -->
**Front:** Are NetworkPolicies additive or ordered?
**Back:** Additive. There is no ordering; traffic is allowed if any policy permits it.
**Tags:** ckad::networkpolicy concept

---

<!-- note:1781279834491 model:Basic++++ -->
**Front:** YAML: default deny all ingress in a namespace.
**Back:** apiVersion: networking.k8s.io/v1<br>kind: NetworkPolicy<br>metadata:<br>  name: default-deny-ingress<br>spec:<br>  podSelector: {}<br>  policyTypes:<br>  - Ingress
**Tags:** ckad::networkpolicy yaml

---

<!-- note:1781279834492 model:Basic++++ -->
**Front:** YAML: default deny ingress and egress.
**Back:** spec:<br>  podSelector: {}<br>  policyTypes:<br>  - Ingress<br>  - Egress
**Tags:** ckad::networkpolicy yaml

---

<!-- note:1781279834493 model:Basic++++ -->
**Front:** YAML: allow ingress to app=api from Pods app=frontend on port 8080.
**Back:** spec:<br>  podSelector:<br>    matchLabels:<br>      app: api<br>  policyTypes: [Ingress]<br>  ingress:<br>  - from:<br>    - podSelector:<br>        matchLabels:<br>          app: frontend<br>    ports:<br>    - protocol: TCP<br>      port: 8080
**Tags:** ckad::networkpolicy yaml

---

<!-- note:1781279834494 model:Basic++++ -->
**Front:** What does an empty ingress list mean in NetworkPolicy?
**Back:** No ingress traffic is allowed for selected Pods, assuming policyTypes includes Ingress.
**Tags:** ckad::networkpolicy yaml

---

<!-- note:1781279834495 model:Basic++++ -->
**Front:** What does ingress: - {} mean?
**Back:** Allow all ingress traffic to selected Pods.
**Tags:** ckad::networkpolicy yaml

---

<!-- note:1781279834496 model:Basic++++ -->
**Front:** What does podSelector: {} mean inside spec?
**Back:** Select all Pods in the NetworkPolicy's namespace.
**Tags:** ckad::networkpolicy selectors yaml

---

<!-- note:1781279834497 model:Basic++++ -->
**Front:** What does namespaceSelector select?
**Back:** Namespaces by labels; it can allow traffic from/to Pods in matching namespaces.
**Tags:** ckad::networkpolicy selectors yaml

---

<!-- note:1781279834498 model:Basic++++ -->
**Front:** YAML: allow from namespace labelled team=blue and Pod labelled role=client.
**Back:** from:<br>- namespaceSelector:<br>    matchLabels:<br>      team: blue<br>  podSelector:<br>    matchLabels:<br>      role: client
**Tags:** ckad::networkpolicy yaml

---

<!-- note:1781279834499 model:Basic++++ -->
**Front:** In NetworkPolicy, what is the difference between two from list items and one item with both namespaceSelector and podSelector?
**Back:** Two list items are OR; one item with both selectors is AND.
**Tags:** ckad::networkpolicy concept selectors

---

<!-- note:1781279834500 model:Basic++++ -->
**Front:** YAML: allow egress DNS to kube-dns.
**Back:** egress:<br>- to:<br>  - namespaceSelector:<br>      matchLabels:<br>        kubernetes.io/metadata.name: kube-system<br>    podSelector:<br>      matchLabels:<br>        k8s-app: kube-dns<br>  ports:<br>  - protocol: UDP<br>    port: 53<br>  - protocol: TCP<br>    port: 53
**Tags:** ckad::networkpolicy egress yaml

---

<!-- note:1781279834501 model:Basic++++ -->
**Front:** YAML: allow egress to CIDR except one range.
**Back:** egress:<br>- to:<br>  - ipBlock:<br>      cidr: 10.0.0.0/8<br>      except:<br>      - 10.1.0.0/16
**Tags:** ckad::networkpolicy egress yaml

---

<!-- note:1781279834502 model:Basic++++ -->
**Front:** Command: list NetworkPolicies.
**Back:** kubectl get networkpolicy
**Tags:** ckad::networkpolicy command

---

<!-- note:1781279834503 model:Basic++++ -->
**Front:** Command: describe NetworkPolicy.
**Back:** kubectl describe networkpolicy &lt;name&gt;
**Tags:** ckad::networkpolicy command debugging

---

<!-- note:1781279834504 model:Basic++++ -->
**Front:** What should you remember when testing NetworkPolicy by Service DNS?
**Back:** DNS itself may need egress allowed, and the Service must have endpoints; otherwise the policy may not be the real issue.
**Tags:** ckad::networkpolicy debugging dns services

---
