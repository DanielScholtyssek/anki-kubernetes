# CKAD - Certified Kubernetes Application Developer — services

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `services` · Notes: 30 · Models: Basic++++

<!-- note:1781279834149 model:Basic++++ -->
**Front:** Command: generate Service YAML exposing a Deployment without creating it.
**Back:** kubectl expose deployment web --port=80 --target-port=8080 --dry-run=client -o yaml
**Tags:** ckad::services command yaml

---

<!-- note:1781279834441 model:Basic++++ -->
**Front:** What is a Service?
**Back:** A stable virtual network endpoint that routes traffic to matching ready Pods using selectors and endpoints.
**Tags:** ckad::services concept

---

<!-- note:1781279834442 model:Basic++++ -->
**Front:** Why do Pods need Services?
**Back:** Pod IPs are ephemeral; Services provide stable DNS/name/IP and load-balancing across matching Pods.
**Tags:** ckad::services concept pods

---

<!-- note:1781279834443 model:Basic++++ -->
**Front:** What field connects a Service to Pods?
**Back:** spec.selector, matching Pod labels.
**Tags:** ckad::services selectors yaml

---

<!-- note:1781279834444 model:Basic++++ -->
**Front:** What resource shows the actual backend Pods for a Service?
**Back:** Endpoints or EndpointSlices.
**Tags:** ckad::services concept endpoints

---

<!-- note:1781279834445 model:Basic++++ -->
**Front:** Command: expose Deployment web as ClusterIP Service on port 80 to targetPort 8080.
**Back:** kubectl expose deployment web --name=web --port=80 --target-port=8080
**Tags:** ckad::services command

---

<!-- note:1781279834446 model:Basic++++ -->
**Front:** Command: create Service YAML without applying it.
**Back:** kubectl expose deployment web --port=80 --target-port=8080 --dry-run=client -o yaml
**Tags:** ckad::services command yaml

---

<!-- note:1781279834447 model:Basic++++ -->
**Front:** YAML: ClusterIP Service selecting app=web.
**Back:** apiVersion: v1<br>kind: Service<br>metadata:<br>  name: web<br>spec:<br>  type: ClusterIP<br>  selector:<br>    app: web<br>  ports:<br>  - port: 80<br>    targetPort: 8080
**Tags:** ckad::services yaml

---

<!-- note:1781279834448 model:Basic++++ -->
**Front:** In Service ports, what is port?
**Back:** The port exposed by the Service inside the cluster.
**Tags:** ckad::services yaml

---

<!-- note:1781279834449 model:Basic++++ -->
**Front:** In Service ports, what is targetPort?
**Back:** The port on the selected Pods/containers that traffic is forwarded to.
**Tags:** ckad::services yaml

---

<!-- note:1781279834450 model:Basic++++ -->
**Front:** In Service ports, what is nodePort?
**Back:** The external port opened on each node for a NodePort Service.
**Tags:** ckad::services yaml

---

<!-- note:1781279834451 model:Basic++++ -->
**Front:** What is the default Service type?
**Back:** ClusterIP.
**Tags:** ckad::services concept

---

<!-- note:1781279834452 model:Basic++++ -->
**Front:** What is a ClusterIP Service used for?
**Back:** Internal stable access within the cluster.
**Tags:** ckad::services concept

---

<!-- note:1781279834453 model:Basic++++ -->
**Front:** What is a NodePort Service used for?
**Back:** Expose a Service on a port across cluster nodes, usually for external/simple lab access.
**Tags:** ckad::services concept

---

<!-- note:1781279834454 model:Basic++++ -->
**Front:** What is a LoadBalancer Service used for?
**Back:** Request an external load balancer from cloud/provider integration.
**Tags:** ckad::services concept

---

<!-- note:1781279834455 model:Basic++++ -->
**Front:** YAML: NodePort Service.
**Back:** spec:<br>  type: NodePort<br>  ports:<br>  - port: 80<br>    targetPort: 8080<br>    nodePort: 30080
**Tags:** ckad::services yaml

---

<!-- note:1781279834456 model:Basic++++ -->
**Front:** What is the usual NodePort range?
**Back:** 30000-32767, unless the cluster is configured differently.
**Tags:** ckad::services concept

---

<!-- note:1781279834457 model:Basic++++ -->
**Front:** YAML: Service using a named targetPort.
**Back:** ports:<br>- port: 80<br>  targetPort: http
**Tags:** ckad::services yaml

---

<!-- note:1781279834459 model:Basic++++ -->
**Front:** Command: check Service endpoints.
**Back:** kubectl get endpoints &lt;service-name&gt;
**Tags:** ckad::services command debugging endpoints

---

<!-- note:1781279834460 model:Basic++++ -->
**Front:** Command: check EndpointSlices.
**Back:** kubectl get endpointslices
**Tags:** ckad::services command debugging endpoints

---

<!-- note:1781279834461 model:Basic++++ -->
**Front:** What does a Service with no endpoints usually mean?
**Back:** The Service selector does not match Ready Pods, Pods are not Ready, target labels are wrong, or Pods are in a different namespace.
**Tags:** ckad::services debugging selectors

---

<!-- note:1781279834462 model:Basic++++ -->
**Front:** What DNS name can a Pod use for a Service in the same namespace?
**Back:** &lt;service-name&gt;
**Tags:** ckad::services concept dns

---

<!-- note:1781279834463 model:Basic++++ -->
**Front:** What DNS name can a Pod use for a Service in another namespace?
**Back:** &lt;service-name&gt;.&lt;namespace&gt;.svc.cluster.local
**Tags:** ckad::services concept dns

---

<!-- note:1781279834464 model:Basic++++ -->
**Front:** Command: port-forward local 8080 to Service port 80.
**Back:** kubectl port-forward service/&lt;service-name&gt; 8080:80
**Tags:** ckad::services command debugging

---

<!-- note:1781279834466 model:Basic++++ -->
**Front:** What is a headless Service?
**Back:** A Service with clusterIP: None, often used for direct Pod DNS records, especially StatefulSets.
**Tags:** ckad::services concept statefulsets

---

<!-- note:1781279834467 model:Basic++++ -->
**Front:** YAML: headless Service.
**Back:** spec:<br>  clusterIP: None
**Tags:** ckad::services yaml

---

<!-- note:1781279834468 model:Basic++++ -->
**Front:** What is a Service without selector used for?
**Back:** Manually mapping a Service to external/custom endpoints by creating Endpoints or EndpointSlice objects.
**Tags:** ckad::services concept endpoints

---

<!-- note:1781279834469 model:Basic++++ -->
**Front:** YAML: Service without selector.
**Back:** apiVersion: v1<br>kind: Service<br>metadata:<br>  name: external-db<br>spec:<br>  ports:<br>  - port: 5432<br>    targetPort: 5432
**Tags:** ckad::services yaml

---

<!-- note:1781279834470 model:Basic++++ -->
**Front:** What is ExternalName Service?
**Back:** A Service that maps to an external DNS name using CNAME-style DNS, with no Pod endpoints.
**Tags:** ckad::services concept

---

<!-- note:1781279834471 model:Basic++++ -->
**Front:** YAML: ExternalName Service.
**Back:** spec:<br>  type: ExternalName<br>  externalName: example.com
**Tags:** ckad::services yaml

---
