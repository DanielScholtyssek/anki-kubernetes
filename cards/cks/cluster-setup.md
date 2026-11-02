# CKS - Certified Kubernetes Security Specialist — Cluster Setup

> Deck: `CKS - Certified Kubernetes Security Specialist` · Group: `Cluster Setup` · Notes: 129 · Models: Basic+

<!-- note:1772498201184 model:Basic+ -->
**Front:** What is the recommended file permission for the kube-apiserver.yaml file according to CIS Kubernetes Benchmark?
**Back:** The file permissions for the API server pod specification file should be set to 644.
**Tags:** ankidote cis-benchmark file-permissions kubernetes-security

---

<!-- note:1772498201189 model:Basic+ -->
**Front:** What command checks the current file permissions for kube-apiserver.yaml?
**Back:** Use `stat -c %a /etc/kubernetes/manifests/kube-apiserver.yaml` to check permissions.
**Tags:** ankidote cis-benchmark command-line file-permissions

---

<!-- note:1772498201192 model:Basic+ -->
**Front:** What command corrects file permissions for kube-apis,server.yaml?
**Back:** Run `chmod 644 /etc/kubernetes/manifests/kube-apiserver.yaml` to set correct permissions.
**Tags:** ankidote cis-benchmark command-line file-permissions

---

<!-- note:1772498201196 model:Basic+ -->
**Front:** What should be disabled for Kubernetes API server security according to CIS benchmarks?
**Back:** Anonymous authentication should be disabled for the Kube API server.
**Tags:** ankidote api-server cis-benchmark security-config

---

<!-- note:1772498201199 model:Basic+ -->
**Front:** What authentication methods should NOT be specified for Kube API server?
**Back:** Basic and token authentication files should not be specified.
**Tags:** ankidote api-server cis-benchmark security-config

---

<!-- note:1772498201201 model:Basic+ -->
**Front:** What protocol must be enforced for Kube API server security?
**Back:** HTTPS must be required with proper certificate configuration.
**Tags:** ankidote api-server cis-benchmark security-config

---

<!-- note:1772498201204 model:Basic+ -->
**Front:** What is the limitation of the free CIS CAT tool?
**Back:** The free lite version of CIS CAT supports only selected benchmarks (e.g., Windows, Ubuntu, macOS) and does not include Kubernetes.
**Tags:** ankidote benchmarking cis-assessment-tool tool-limitations

---

<!-- note:1772498201206 model:Basic+ -->
**Front:** What is the purpose of the open-source Kubernetes CIS benchmark tool?
**Back:** It performs CIS Benchmark assessments specifically for Kubernetes configurations.
**Tags:** ankidote cis-benchmark kubernetes-tools open-source

---

<!-- note:1772498228085 model:Basic+ -->
**Front:** What is the role of a Certificate Authority (CA) in Kubernetes certificate management?
**Back:** The CA signs certificate signing requests (CSRs) using its private key and root certificate, enabling trusted certificate issuance for the entire cluster.
**Tags:** ankidote ca certificates-api kubernetes

---

<!-- note:1772498228088 model:Basic+ -->
**Front:** What is a CertificateSigningRequest (CSR) in Kubernetes?
**Back:** A CSR is a request submitted to the Kubernetes API for certificate signing, containing the user's public key and requested certificate usages.
**Tags:** ankidote certificates-api csr kubernetes

---

<!-- note:1772498228092 model:Basic+ -->
**Front:** What command reviews pending certificate signing requests?
**Back:** kubectl get csr
**Tags:** ankidote certificates-api csr kubectl

---

<!-- note:1772498228095 model:Basic+ -->
**Front:** How do you approve a CertificateSigningRequest?
**Back:** Use kubectl certificate approve <csr-name> to approve and sign the CSR with the CA's private key.</csr-name>
**Tags:** ankidote certificates-api csr kubectl

---

<!-- note:1772498228098 model:Basic+ -->
**Front:** What command retrieves the signed certificate from a CSR?
**Back:** kubectl get csr <csr-name> -o yaml
**Tags:** ankidote certificates-api csr kubectl

---

<!-- note:1772498228101 model:Basic+ -->
**Front:** What Kubernetes component manages certificate signing and rotation?
**Back:** The controller manager handles CSR approval, signing, and certificate rotation through dedicated controllers.
**Tags:** ankidote certificates-api controller-manager kubernetes

---

<!-- note:1772498228103 model:Basic+ -->
**Front:** Where are the CA's root certificate and private key configured in the controller manager?
**Back:** They are specified via --cluster-signing-cert-file and --cluster-signing-key-file flags in the controller manager's configuration.
**Tags:** ankidote certificates-api configuration controller-manager

---

<!-- note:1772498228105 model:Basic+ -->
**Front:** What OpenSSL commands generate a private key and CSR?
**Back:** openssl genrsa -out jane.key 2048
openssl req -new -key jane.key -subj "/CN=jane" -out jane.csr
**Tags:** ankidote certificates-api csr openssl

---

<!-- note:1772498228108 model:Basic+ -->
**Front:** What is the purpose of the CertificateSigningRequest manifest?
**Back:** It defines the user's requested certificate groups, usages, and Base64-encoded CSR for submission to the API.
**Tags:** ankidote certificates-api csr manifest

---

<!-- note:1772498228110 model:Basic+ -->
**Front:** What file stores the CA's root certificate in Kubernetes?
**Back:** The CA's root certificate is stored in /etc/kubernetes/pki/ca.crt on the master node.
**Tags:** ankidote ca certificates-api kubernetes

---

<!-- note:1772498438087 model:Basic+ -->
**Front:** What is the purpose of the podSelector in the basic network policy YAML?
**Back:** The podSelector identifies the target pods (e.g., database pods) by matching labels. In the example, it selects pods labeled 'role: db'.
**Tags:** ankidote network-policy yaml-configuration

---

<!-- note:1772498438092 model:Basic+ -->
**Front:** Which YAML field specifies that only ingress traffic is allowed in a policy?
**Back:** The policyTypes array with '- Ingress' defines that only ingress traffic is controlled by the policy.
**Tags:** ankidote ingress-egress network-policy

---

<!-- note:1772498438094 model:Basic+ -->
**Front:** What is required to allow database pods to initiate outbound connections?
**Back:** An egress rule must be defined in the policyTypes array, and the egress section must specify the allowed destinations.
**Tags:** ankidote egress-rules network-policy

---

<!-- note:1772498438097 model:Basic+ -->
**Front:** How does combining podSelector and namespaceSelector affect traffic matching?
**Back:** Combining them creates an AND condition: traffic must meet both the pod label and namespace label criteria to be allowed.
**Tags:** ankidote network-policy selectors

---

<!-- note:1772498438099 model:Basic+ -->
**Front:** What YAML construct allows traffic from an external IP address?
**Back:** The ipBlock field with a CIDR notation (e.g., '192.168.5.10/32') specifies allowed external IP ranges.
**Tags:** ankidote ip-block network-policy

---

<!-- note:1772498438101 model:Basic+ -->
**Front:** What is the default behavior of Kubernetes network communication?
**Back:** By default, Kubernetes allows all pods to communicate unless explicitly restricted by network policies.
**Tags:** ankidote default-behavior network-policy

---

<!-- note:1772498438102 model:Basic+ -->
**Front:** Why is an egress rule unnecessary for database pods receiving API traffic?
**Back:** Ingress traffic automatically permits the corresponding response traffic, so egress rules are only needed if the database pod initiates connections.
**Tags:** ankidote ingress-egress traffic-flow

---

<!-- note:1772498438105 model:Basic+ -->
**Front:** What is the purpose of the namespaceSelector in the network policy?
**Back:** The namespaceSelector restricts traffic to pods in specific namespaces (e.g., 'prod') by matching namespace labels.
**Tags:** ankidote namespaces selectors

---

<!-- note:1772498438108 model:Basic+ -->
**Front:** How are multiple selectors combined in a single network policy rule?
**Back:** Multiple selectors are combined using an AND condition within the same 'from' block, or as separate entries using an OR condition.
**Tags:** ankidote policy-structure selectors

---

<!-- note:1772498438110 model:Basic+ -->
**Front:** What is the role of the 'ports' section in a network policy?
**Back:** The 'ports' section specifies which ports and protocols (e.g., TCP:3306) are allowed in the policy rules.
**Tags:** ankidote policy-structure ports

---

<!-- note:1772498585343 model:Basic+ -->
**Front:** What is Ingress in Kubernetes?
**Back:** Ingress is a Kubernetes resource that manages external access to applications, providing routing configurations based on URL paths or hostnames. It acts as a layer-7 load balancer, handling SSL termination and consolidating multiple services into a single externally accessible URL.
**Tags:** ankidote ingress-definition kubernetes-networking

---

<!-- note:1772498585346 model:Basic+ -->
**Front:** How does Ingress differ from NodePort/LoadBalancer services?
**Back:** Ingress consolidates multiple services into a single URL with routing rules, while NodePort/LoadBalancer services require separate endpoints. Ingress handles SSL termination and advanced routing, whereas NodePort exposes services on high ports and LoadBalancer creates cloud-specific balancers.
**Tags:** ankidote ingress-vs-nodeport kubernetes-networking

---

<!-- note:1772498585349 model:Basic+ -->
**Front:** What components are required to deploy an NGINX Ingress Controller?
**Back:** A Deployment for the controller, a Service to expose it (NodePort or LoadBalancer), a ConfigMap for configuration, and a ServiceAccount for permissions. These components work together to manage Ingress resources.
**Tags:** ankidote ingress-deployment nginx-ingress

---

<!-- note:1772498585353 model:Basic+ -->
**Front:** What YAML arguments configure the NGINX Ingress Controller?
**Back:** The controller uses `--configmap=$(POD_NAMESPACE)/nginx-configuration` to reference a ConfigMap, and environment variables `POD_NAME`/`POD_NAMESPACE` for metadata. It exposes ports 80 (HTTP) and 443 (HTTPS).
**Tags:** ankidote ingress-configuration nginx-ingress

---

<!-- note:1772498585354 model:Basic+ -->
**Front:** How to configure Ingress for URL path-based routing?
**Back:** Define an Ingress resource with `rules` and `paths` specifying URL paths. Example:
```yaml
rules:
- http:
    paths:
    - path: /wear
      backend: serviceName: wear-service, servicePort: 80
```
**Tags:** ankidote ingress-rules url-routing

---

<!-- note:1772498585356 model:Basic+ -->
**Front:** How to configure Ingress for domain-based routing?
**Back:** Use `host` fields in Ingress rules to split traffic by domain. Example:
```yaml
rules:
- host: wear.my-online-store.com
  http:
    paths:
    - backend: serviceName: wear-service, servicePort: 80
```
**Tags:** ankidote host-routing ingress-rules

---

<!-- note:1772498585362 model:Basic+ -->
**Front:** What is a default backend in Ingress?
**Back:** A default backend handles unmatched URLs (e.g., myonlinestore.com/listen) by returning a custom 404 page or message. It ensures all traffic is managed even if no rules match.
**Tags:** ankidote error-handling ingress-default-backend

---

<!-- note:1772498585364 model:Basic+ -->
**Front:** What are supported Ingress controllers in Kubernetes?
**Back:** Supported controllers include NGINX, GCE (Google Cloud), Contour, HAProxy, Traefik, and Istio. These controllers implement routing rules defined in Ingress resources.
**Tags:** ankidote ingress-controllers kubernetes-networking

---

<!-- note:1772498585366 model:Basic+ -->
**Front:** What is the purpose of the ConfigMap in Ingress deployment?
**Back:** The ConfigMap decouples configuration data (like log paths and SSL settings) from the container image, allowing flexible customization of the Ingress controller's behavior.
**Tags:** ankidote configmap ingress-configuration

---

<!-- note:1772498585368 model:Basic+ -->
**Front:** How does Ingress simplify production-grade applications?
**Back:** Ingress consolidates multiple services into a single URL, handles SSL termination, and provides centralized routing rules. This reduces complexity compared to managing multiple LoadBalancer services.
**Tags:** ankidote ingress-benefits kubernetes-networking

---

<!-- note:1772498626390 model:Basic+ -->
**Front:** What is Kube-Bench?
**Back:** Kube-Bench is an open-source tool developed by Aqua Security for verifying Kubernetes security configurations against CIS Benchmarks.
**Tags:** ankidote cis-benchmarks kube-bench security-tools

---

<!-- note:1772498626392 model:Basic+ -->
**Front:** What is the primary purpose of Kube-Bench?
**Back:** To assess Kubernetes security configurations for compliance with CIS Benchmarks and identify potential security issues.
**Tags:** ankidote cis-benchmarks kube-bench security-assessment

---

<!-- note:1772498626395 model:Basic+ -->
**Front:** What are the three deployment methods for Kube-Bench?
**Back:** 1. Docker Container
2. Kubernetes Job
3. Binaries or Source Compilation
**Tags:** ankidote deployment-methods kube-bench kubernetes

---

<!-- note:1772498626398 model:Basic+ -->
**Front:** What is the first step in using Kube-Bench?
**Back:** Identify a stable Kube-Bench version compatible with your Kubernetes cluster from its GitHub repository.
**Tags:** ankidote cis-benchmarks kube-bench step-by-step

---

<!-- note:1772498626400 model:Basic+ -->
**Front:** What is the purpose of running Kube-Bench?
**Back:** To evaluate Kubernetes configurations against CIS Benchmarks and generate a pass/fail report for each check.
**Tags:** ankidote cis-benchmarks kube-bench security-assessment

---

<!-- note:1772498626402 model:Basic+ -->
**Front:** What should be done after reviewing Kube-Bench results?
**Back:** Remediate identified security issues and re-run the assessment to confirm compliance.
**Tags:** ankidote kube-bench remediation security-compliance

---

<!-- note:1772498626404 model:Basic+ -->
**Front:** How does Kube-Bench align with CIS Benchmarks?
**Back:** It performs checks corresponding to each CIS recommendation to systematically identify security configuration issues.
**Tags:** ankidote best-practices cis-benchmarks kube-bench

---

<!-- note:1772498626406 model:Basic+ -->
**Front:** Why is regular Kube-Bench updates important?
**Back:** To maintain compliance as Kubernetes and security best practices evolve, ensuring ongoing security validation.
**Tags:** ankidote kube-bench security-compliance updates

---

<!-- note:1772498626408 model:Basic+ -->
**Front:** What is a recommended deployment method for scheduled compliance checks?
**Back:** Running Kube-Bench as a Kubernetes Job simplifies automated, scheduled security assessments.
**Tags:** ankidote automation deployment-methods kube-bench

---

<!-- note:1772498666362 model:Basic+ -->
**Front:** What is the purpose of a KubeConfig file in Kubernetes?
**Back:** A KubeConfig file consolidates cluster access information, credentials, and contexts to simplify secure communication with the Kubernetes API server.
**Tags:** ankidote kubeconfig kubernetes security

---

<!-- note:1772498666365 model:Basic+ -->
**Front:** What are the three main sections of a KubeConfig file?
**Back:** Clusters (Kubernetes cluster details), Users (credentials), and Contexts (combinations of clusters and users).
**Tags:** ankidote clusters-users-contexts kubeconfig structure

---

<!-- note:1772498666367 model:Basic+ -->
**Front:** What does the 'current-context' field in a KubeConfig file specify?
**Back:** It defines the default context (cluster/user combination) that kubectl uses for operations.
**Tags:** ankidote configuration contexts kubeconfig

---

<!-- note:1772498666368 model:Basic+ -->
**Front:** How do you switch the active context in kubectl?
**Back:** Use `kubectl config use-context <context-name>` to update the current-context field.
**Tags:** ankidote commands contexts kubeconfig

---

<!-- note:1772498666370 model:Basic+ -->
**Front:** How can you set a default namespace in a KubeConfig context?
**Back:** Add the `namespace` field to the context's configuration under the `context` section.
**Tags:** ankidote configuration kubeconfig namespaces

---

<!-- note:1772498666372 model:Basic+ -->
**Front:** What is the default location for the kubeconfig file?
**Back:** The default location is `$HOME/.kube/config` if the file exists there.
**Tags:** ankidote defaults file-location kubeconfig

---

<!-- note:1772498666373 model:Basic+ -->
**Front:** How do you specify a custom kubeconfig file location?
**Back:** Use the `--kubeconfig` flag with kubectl commands, e.g., `kubectl get pods --kubeconfig=my-custom-config`.
**Tags:** ankidote custom-file flags kubeconfig

---

<!-- note:1772498666374 model:Basic+ -->
**Front:** What are the key fields in a KubeConfig YAML file?
**Back:** The file includes `apiVersion`, `kind`, `clusters`, `users`, `contexts`, and `current-context`.
**Tags:** ankidote kubeconfig structure yaml

---

<!-- note:1772498666375 model:Basic+ -->
**Front:** How are clusters defined in a KubeConfig file?
**Back:** Clusters are defined as an array of objects with a `name` and cluster-specific details like `server` and `certificate-authority`.
**Tags:** ankidote clusters configuration kubeconfig

---

<!-- note:1772498666376 model:Basic+ -->
**Front:** What is the recommended practice for handling certificate files in kubeconfig?
**Back:** Use full file paths for certificates or embed base64-encoded certificate data using `certificate-authority-data` for security and portability.
**Tags:** ankidote certificates kubeconfig security

---

<!-- note:1772498803089 model:Basic+ -->
**Front:** What security risks are associated with older versions of the Kubernetes Dashboard?
**Back:** Older versions lacked strict access controls, leading to vulnerabilities like the Tesla cryptojacking incident where unsecured dashboards were exploited for cryptocurrency mining.
**Tags:** ankidote kubernetes-dashboard-security security-risks

---

<!-- note:1772498803093 model:Basic+ -->
**Front:** What namespace is created when deploying the Kubernetes Dashboard?
**Back:** The deployment creates a dedicated namespace called `kubernetes-dashboard`.
**Tags:** ankidote kubernetes-dashboard-deployment namespace-creation

---

<!-- note:1772498803096 model:Basic+ -->
**Front:** What is the purpose of the Kubernetes Dashboard's Service resource?
**Back:** The Service exposes the dashboard internally within the cluster using ClusterIP by default.
**Tags:** ankidote kubernetes-dashboard-service service-configuration

---

<!-- note:1772498803099 model:Basic+ -->
**Front:** How do you securely access the Kubernetes Dashboard from a local machine?
**Back:** Use `kubectl proxy` to create a secure tunnel, then navigate to `http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/`.
**Tags:** ankidote kubectl-proxy secure-access

---

<!-- note:1772498803103 model:Basic+ -->
**Front:** What is the default service type for the Kubernetes Dashboard?
**Back:** The default service type is ClusterIP, restricting access to within the cluster.
**Tags:** ankidote kubernetes-dashboard service-type

---

<!-- note:1772498803106 model:Basic+ -->
**Front:** What are the risks of changing the Kubernetes Dashboard service type to LoadBalancer or NodePort?
**Back:** Exposing the dashboard externally increases security risks, requiring additional network and authentication controls.
**Tags:** ankidote security-risks service-exposure

---

<!-- note:1772498803109 model:Basic+ -->
**Front:** What deployment strategy is demonstrated in the provided YAML example?
**Back:** The example uses a rolling update strategy with `maxUnavailable: 25%` and `maxSurge: 25`.
**Tags:** ankidote deployment-strategy rolling-update

---

<!-- note:1772498803111 model:Basic+ -->
**Front:** What command deploys the Kubernetes Dashboard using the recommended configuration?
**Back:** Run `kubectl apply -f https://<path-to-Kubernetes-dashboard>/recommended.yaml`.
**Tags:** ankidote deployment-command kubectl-apply

---

<!-- note:1772498803113 model:Basic+ -->
**Front:** What is the role of Secrets in the Kubernetes Dashboard deployment?
**Back:** Secrets store certificates and other sensitive configurations required for secure communication.
**Tags:** ankidote kubernetes-dashboard secrets-management

---

<!-- note:1772498803115 model:Basic+ -->
**Front:** Which tool is recommended for secure, team-wide access to the Kubernetes Dashboard?
**Back:** Implement authentication and authorization measures beyond the default proxy method to control access.
**Tags:** ankidote authentication secure-access

---

<!-- note:1772498803118 model:Basic+ -->
**Front:** What does the `kubectl describe service` command reveal about the Dashboard service?
**Back:** It shows details like the IP address, port mappings, and service type (e.g., ClusterIP).
**Tags:** ankidote kubectl-describe service-diagnosis

---

<!-- note:1772498803121 model:Basic+ -->
**Front:** What are the three alternative methods to expose the Kubernetes Dashboard externally?
**Back:** LoadBalancer, NodePort, and Authentication Proxies (e.g., OAuth2 Proxy).
**Tags:** ankidote exposure-methods security-configuration

---

<!-- note:1772498803122 model:Basic+ -->
**Front:** What is the recommended approach for securing the Kubernetes Dashboard?
**Back:** Use `kubectl proxy` for individual access and implement strict authentication/authorization for team access, avoiding external service types unless necessary.
**Tags:** ankidote kubernetes-dashboard security-best-practices

---

<!-- note:1772498803125 model:Basic+ -->
**Front:** Which resources are created during the Kubernetes Dashboard deployment?
**Back:** Deployment, Service, ConfigMaps, and Secrets are created in the `kubernetes-dashboard` namespace.
**Tags:** ankidote deployment-resources kubernetes-dashboard

---

<!-- note:1772498803128 model:Basic+ -->
**Front:** What is the purpose of the `revisionHistoryLimit` in the Dashboard deployment?
**Back:** It specifies the number of old ReplicaSet versions to retain for rollback purposes.
**Tags:** ankidote deployment-configuration replicaset

---

<!-- note:1772498878713 model:Basic+ -->
**Front:** What is ingress traffic in the context of the web server example?
**Back:** Ingress traffic is incoming traffic, such as user requests to the web server on port 80.
**Tags:** ankidote ingress network-policy

---

<!-- note:1772498878715 model:Basic+ -->
**Front:** What is egress traffic in the web server example?
**Back:** Egress traffic is outgoing traffic, such as the web server forwarding requests to the API server on port 5000.
**Tags:** ankidote egress network-policy

---

<!-- note:1772498878716 model:Basic+ -->
**Front:** What is the default network behavior in Kubernetes clusters?
**Back:** By default, Kubernetes allows unrestricted communication between all pods, services, or IPs within the cluster due to an 'allow all' rule.
**Tags:** ankidote default-policy kubernetes-networking

---

<!-- note:1772498878718 model:Basic+ -->
**Front:** What is the purpose of a Kubernetes NetworkPolicy?
**Back:** A NetworkPolicy defines how pods communicate with each other by restricting traffic based on labels, ports, and directions (ingress/egress).
**Tags:** ankidote kubernetes network-policy

---

<!-- note:1772498878721 model:Basic+ -->
**Front:** What does the YAML example for the db-policy restrict?
**Back:** The YAML restricts ingress traffic to the database pod, allowing only TCP port 3306 from pods labeled with `name: api-pod`.
**Tags:** ankidote network-policy yaml-example

---

<!-- note:1772498878723 model:Basic+ -->
**Front:** Which CNI plugins support Kubernetes network policies?
**Back:** Kube-router, Calico, Romana, and Weave Net support network policies. Flannel does not.
**Tags:** ankidote cni-plugins network-policy

---

<!-- note:1772498878724 model:Basic+ -->
**Front:** What command applies a network policy from a YAML file?
**Back:** Run `kubectl create -f <policy-file-name>.yaml` to apply the policy.
**Tags:** ankidote kubectl network-policy

---

<!-- note:1772498878726 model:Basic+ -->
**Front:** What is required for ingress/egress isolation in NetworkPolicies?
**Back:** PolicyTypes must explicitly define ingress or egress in the spec. Otherwise, traffic is not isolated.
**Tags:** ankidote network-policy policytypes

---

<!-- note:1772498878727 model:Basic+ -->
**Front:** What are the three key components in the web API database example?
**Back:** Web server (port 80), API server (port 5000), and database server (port 3306).
**Tags:** ankidote example network-flow

---

<!-- note:1772498878729 model:Basic+ -->
**Front:** Which pod receives ingress traffic on port 3306?
**Back:** The database server receives ingress traffic on port 3306 from the API server.
**Tags:** ankidote network-flow ports

---

<!-- note:1772498902937 model:Basic+ -->
**Front:** How does Kubernetes RBAC mirror hotel access control?
**Back:** Role-based access control (RBAC) in Kubernetes defines roles with specific permissions, ensuring only authorized users can modify node metadata. This mirrors hotel staff access levels where managers have broader access than housekeepers.
**Tags:** access-control ankidote rbac

---

<!-- note:1772498902940 model:Basic+ -->
**Front:** What is node isolation in Kubernetes, and how does it relate to the hotel analogy?
**Back:** Node isolation reserves specific nodes for particular workloads, preventing non-critical applications from running on critical nodes. This is analogous to hotels assigning VIP guests to exclusive rooms and regular guests to standard rooms.
**Tags:** ankidote node-isolation workload-isolation

---

<!-- note:1772498902943 model:Basic+ -->
**Front:** What is the purpose of network policies in Kubernetes, according to the hotel analogy?
**Back:** Network policies control communication between pods/nodes, ensuring only authorized services can interact. This mirrors hotel restrictions like staff-only areas and VIP guest floors that limit access to specific zones.
**Tags:** ankidote communication-control network-policies

---

<!-- note:1772498902948 model:Basic+ -->
**Front:** What role do audit logs play in Kubernetes security, according to the hotel analogy?
**Back:** Audit logs track access and modifications to node metadata, similar to hotel logs that record room access details. They provide critical records for security monitoring, compliance, and incident investigation.
**Tags:** ankidote audit-logs security-monitoring

---

<!-- note:1772498902950 model:Basic+ -->
**Front:** Why are regular updates and patches critical for Kubernetes nodes?
**Back:** Regular updates and patches address vulnerabilities in Kubernetes nodes, just as hotels upgrade security systems. This proactive maintenance ensures timely mitigation of security risks and maintains cluster integrity.
**Tags:** ankidote node-updates vulnerability-management

---

<!-- note:1772499004736 model:Basic+ -->
**Front:** What are CIS Benchmarks?
**Back:** CIS Benchmarks are a set of security best practices for configuring systems to meet security guidelines and reduce vulnerabilities.
**Tags:** ankidote cis-benchmarks security-best-practices

---

<!-- note:1772499004738 model:Basic+ -->
**Front:** What tools are used for Kubernetes security benchmarks?
**Back:** Tools include kube-bench and kube-benchsuite, which validate cluster configurations against CIS benchmarks.
**Tags:** ankidote kube-bench security-tools

---

<!-- note:1772499004740 model:Basic+ -->
**Front:** What are primary Kubernetes authentication mechanisms?
**Back:** Kubernetes uses Service Accounts for pod identity and TLS Certificates for secure API communication.
**Tags:** ankidote authentication tls-certificates

---

<!-- note:1772499004742 model:Basic+ -->
**Front:** How to secure node metadata and endpoints?
**Back:** Protect node metadata via kubelet --read-only flag and secure endpoints with TLS encryption and access controls.
**Tags:** ankidote metadata-protection node-security

---

<!-- note:1772499004744 model:Basic+ -->
**Front:** What methods secure the Kubernetes Dashboard?
**Back:** Secure the dashboard with Role-Based Access Control (RBAC), TLS encryption, and verified platform binaries.
**Tags:** ankidote binary-verification dashboard-security

---

<!-- note:1772499004746 model:Basic+ -->
**Front:** What are strategies for secure Kubernetes cluster upgrades?
**Back:** Use kubeadm with --config for controlled upgrades and apply network policies to restrict ingress traffic.
**Tags:** ankidote cluster-upgrades network-policies

---

<!-- note:1772499076463 model:Basic+ -->
**Front:** Why is securing node metadata critical in Kubernetes?
**Back:** Node metadata contains sensitive information like instance details and credentials. Exposure can lead to security risks such as unauthorized access or infrastructure compromise.
**Tags:** ankidote kubernetes-metadata node-security

---

<!-- note:1772499076467 model:Basic+ -->
**Front:** What analogy is used to explain node metadata?
**Back:** A Kubernetes cluster is compared to a hotel, where nodes are rooms with metadata like room type, occupancy, and service notes.
**Tags:** analogies ankidote kubernetes-metadata

---

<!-- note:1772499076470 model:Basic+ -->
**Front:** What is the purpose of node labels?
**Back:** Labels are key-value pairs used to categorize nodes, such as grouping by geographic region or environment.
**Tags:** ankidote kubernetes-metadata node-labels

---

<!-- note:1772499076473 model:Basic+ -->
**Front:** What are node annotations used for?
**Back:** Annotations provide additional context for debugging, logging, and monitoring, such as Flannel's internal configuration.
**Tags:** ankidote kubernetes-metadata node-annotations

---

<!-- note:1772499076477 model:Basic+ -->
**Front:** What does system info in node metadata include?
**Back:** System info includes machine ID, system UUID, boot ID, kernel version, OS details, container runtime, and Kubernetes component versions.
**Tags:** ankidote kubernetes-metadata system-info

---

<!-- note:1772499076481 model:Basic+ -->
**Front:** What components are part of node metadata?
**Back:** Node metadata includes node name, labels, annotations, architecture, system info, addresses, conditions, resource capacities, taints, pod CIDRs, kubelet version, and cloud provider IDs.
**Tags:** ankidote kubernetes-metadata node-components

---

<!-- note:1772499076483 model:Basic+ -->
**Front:** What is the role of node conditions?
**Back:** Node conditions indicate operational status (e.g., Ready, OutOfDisk, MemoryPressure) and help monitor node health.
**Tags:** ankidote kubernetes-metadata node-conditions

---

<!-- note:1772499076487 model:Basic+ -->
**Front:** What are taints and tolerations used for?
**Back:** Taints and tolerations control pod scheduling on nodes, ensuring workloads are placed appropriately based on node characteristics.
**Tags:** ankidote kubernetes-metadata taints-tolerations

---

<!-- note:1772499076489 model:Basic+ -->
**Front:** What is the purpose of pod CIDRs in node metadata?
**Back:** Pod CIDRs define the IP ranges used for pods on a node, ensuring network isolation and addressing within the cluster.
**Tags:** ankidote kubernetes-metadata pod-cidr

---

<!-- note:1772499076492 model:Basic+ -->
**Front:** What are best practices for securing node metadata?
**Back:** Restrict access to metadata, monitor for unauthorized changes, and use Kubernetes security features like IAM roles and network policies to protect sensitive data.
**Tags:** ankidote kubernetes-metadata security-best-practices

---

<!-- note:1772499263637 model:Basic+ -->
**Front:** What command is used to download Kubernetes binaries from the official source?
**Back:** Use `curl https://dl.k8s.io/v1.20.0/kubernetes.tar.gz -L -o kubernetes.tar.gz` to download the binary.
**Tags:** ankidote binary-verification kubernetes-security

---

<!-- note:1772499263639 model:Basic+ -->
**Front:** Which command generates a SHA-512 checksum on macOS/Linux?
**Back:** Use `shasum -a 512 kubernetes.tar.gz` to generate a SHA-512 checksum.
**Tags:** ankidote checksum-command os-specific

---

<!-- note:1772499263641 model:Basic+ -->
**Front:** Why is comparing checksums critical for security?
**Back:** Checksum comparison ensures files haven't been tampered with during transit, as even minor changes alter the hash.
**Tags:** ankidote file-integrity security-checksums

---

<!-- note:1772499263644 model:Basic+ -->
**Front:** What indicates a potential security risk with downloaded binaries?
**Back:** A mismatch between the generated checksum and the release page's hash indicates possible tampering.
**Tags:** ankidote hash-mismatch security-risks

---

<!-- note:1772499263646 model:Basic+ -->
**Front:** Which command is available on both macOS and Linux for SHA-512 verification?
**Back:** The `shasum -a 512 kubernetes.tar.gz` command works on both macOS and Linux systems.
**Tags:** ankidote command-comparison os-commands

---

<!-- note:1772499288135 model:Basic+ -->
**Front:** What is a security benchmark according to the text?
**Back:** A security benchmark is a set of best practices for securing systems by hardening configurations, such as disabling unused USB ports, implementing access controls, and configuring firewalls.
**Tags:** ankidote security-benchmarks system-hardening

---

<!-- note:1772499288138 model:Basic+ -->
**Front:** What does CIS stand for, and what is its mission?
**Back:** CIS stands for Center for Internet Security. Its mission is to create a safer connected world by developing, validating, and promoting actionable cybersecurity best practices through community-driven recommendations.
**Tags:** ankidote cis-organization cybersecurity-mission

---

<!-- note:1772499288140 model:Basic+ -->
**Front:** Which technology categories does CIS cover?
**Back:** CIS covers operating systems (Linux, Windows, macOS), public cloud platforms (AWS, Azure, Google Cloud), mobile platforms (iOS, Android), network devices (Cisco, Palo Alto), desktop software (Zoom, MS Office), server software (Nginx, Tomcat), and virtualization technologies (Kubernetes, Docker).
**Tags:** ankidote cis-categories technology-coverage

---

<!-- note:1772499288142 model:Basic+ -->
**Front:** What are the components of a CIS benchmark?
**Back:** Each CIS benchmark includes: 1) an explanation of risks for non-compliant configurations, 2) step-by-step instructions to verify security risks with commands, and 3) procedures to resolve identified issues.
**Tags:** ankidote benchmark-structure cis-components

---

<!-- note:1772499288143 model:Basic+ -->
**Front:** What is CIS CAT, and what does it do?
**Back:** CIS CAT (Configuration Assessment Tool) is an automated tool that compares a system's configuration against CIS benchmarks, generates an HTML report, and highlights passed/failed security recommendations with scoring percentages.
**Tags:** ankidote automated-assessment cis-cat

---

<!-- note:1772499288145 model:Basic+ -->
**Front:** What command checks USB storage configuration in CIS benchmarks?
**Back:** The command `modprobe -n -v usb-storage` checks if USB storage is enabled, helping verify compliance with USB-related security benchmarks.
**Tags:** ankidote cis-command usb-security

---

<!-- note:1772507645338 model:Basic+ -->
**Front:** What is the purpose of securing node metadata in Kubernetes?
**Back:** To ensure correct scheduling of workloads, prevent unauthorized access to cluster information, maintain system integrity, and ensure compliance with regulatory standards.
**Tags:** ankidote kubernetes-security node-metadata workload-scheduling

---

<!-- note:1772507645342 model:Basic+ -->
**Front:** What risk does tampered node metadata pose in Kubernetes?
**Back:** It can lead to sensitive workloads being scheduled on insecure nodes, similar to assigning VIP guests to unsuitable rooms in a hotel analogy.
**Tags:** ankidote kubernetes-security node-metadata workload-scheduling

---

<!-- note:1772507645345 model:Basic+ -->
**Front:** What is an example of improper workload scheduling due to insecure node metadata?
**Back:** Removing a critical taint from a production node might allow non-production workloads to consume resources intended for high-security tasks.
**Tags:** ankidote kubernetes-security node-taints workload-scheduling

---

<!-- note:1772507645349 model:Basic+ -->
**Front:** How can attackers exploit insecure node metadata for data exposure?
**Back:** They can access the Kubernetes API to retrieve Kubelet versions, which may enable version-specific exploits.
**Tags:** ankidote data-exposure kubelet-version kubernetes-security

---

<!-- note:1772507645353 model:Basic+ -->
**Front:** What command reveals Kubelet versions from node metadata?
**Back:** kubectl get nodes -o jsonpath='{.items[*].status.nodeInfo.kubeletVersion}'
**Tags:** ankidote kubelet-version kubernetes-security node-metadata

---

<!-- note:1772507645356 model:Basic+ -->
**Front:** How can attackers use node metadata for network mapping?
**Back:** By listing internal IP addresses of all nodes, they can construct a map of the internal network for targeted attacks like DDoS.
**Tags:** ankidote internal-ips kubernetes-security network-mapping

---

<!-- note:1772507645359 model:Basic+ -->
**Front:** What command retrieves internal IP addresses from node metadata?
**Back:** kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="InternalIP")].address}'
**Tags:** ankidote internal-ips kubernetes-security node-metadata

---

<!-- note:1772507645362 model:Basic+ -->
**Front:** What regulatory standards could be violated by insecure node metadata?
**Back:** GDPR and HIPAA compliance could be breached if unauthorized access reveals kernel versions or other sensitive node details.
**Tags:** ankidote compliance kubernetes-security regulatory-standards

---

<!-- note:1772507645366 model:Basic+ -->
**Front:** What command shows kernel versions from node metadata?
**Back:** kubectl get nodes -o jsonpath='{.items[*].status.nodeInfo.kernelVersion}'
**Tags:** ankidote kernel-version kubernetes-security node-metadata

---

<!-- note:1772507645369 model:Basic+ -->
**Front:** What are the four key benefits of securing node metadata?
**Back:** 1. Correct scheduling of sensitive workloads
2. Prevention of unauthorized access to cluster information
3. Maintenance of system integrity
4. Compliance with regulatory standards
**Tags:** ankidote benefits kubernetes-security node-metadata

---

<!-- note:1772507661991 model:Basic+ -->
**Front:** Where can you find the complete Kubernetes Dashboard documentation index?
**Back:** https://notes.kodekloud.com/llms.txt
**Tags:** ankidote documentation kubernetes-dashboard

---

<!-- note:1772507661995 model:Basic+ -->
**Front:** What are the two authentication methods for Kubernetes Dashboard?
**Back:** Token-based authentication and KubeConfig file authentication
**Tags:** ankidote authentication kubernetes-dashboard

---

<!-- note:1772507661999 model:Basic+ -->
**Front:** What security principle should guide permission assignments in Kubernetes?
**Back:** The principle of least privilege - granting only necessary permissions to minimize security risks
**Tags:** ankidote rbac security-principles

---

<!-- note:1772507662001 model:Basic+ -->
**Front:** How do you retrieve the token secret for a Kubernetes Dashboard user?
**Back:** Use `kubectl describe secret <secret-name>` to view the token, ca.crt, and namespace data
**Tags:** ankidote kubernetes-dashboard token-retrieval

---

<!-- note:1772507662004 model:Basic+ -->
**Front:** What is the purpose of using a KubeConfig file for authentication?
**Back:** To authenticate without using tokens, allowing configuration of access through Kubernetes credentials
**Tags:** ankidote authentication kubeconfig kubernetes-dashboard

---
