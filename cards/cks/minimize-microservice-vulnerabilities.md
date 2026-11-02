# CKS - Certified Kubernetes Security Specialist — Minimize Microservice Vulnerabilities

> Deck: `CKS - Certified Kubernetes Security Specialist` · Group: `Minimize Microservice Vulnerabilities` · Notes: 256 · Models: Basic+

<!-- note:1772499457963 model:Basic+ -->
**Front:** What are admission controllers in Kubernetes?
**Back:** Admission controllers are components in Kubernetes that validate, mutate, or reject API requests before they are persisted to etcd. They provide an additional security layer beyond authentication and authorization.
**Tags:** admission-controllers ankidote kubernetes-security

---

<!-- note:1772499457966 model:Basic+ -->
**Front:** What is the role of admission controllers in the Kubernetes request lifecycle?
**Back:** Admission controllers examine, modify, or reject API requests after authentication and authorization. They enforce policies like image registry restrictions, security context changes, or metadata labeling.
**Tags:** ankidote kubernetes-security request-lifecycle

---

<!-- note:1772499457969 model:Basic+ -->
**Front:** What is the purpose of the 'Namespace Exists' admission controller?
**Back:** The Namespace Exists controller rejects requests to create resources in non-existent namespaces. It ensures operations only occur within valid namespaces.
**Tags:** admission-controllers ankidote namespace-controllers

---

<!-- note:1772499457971 model:Basic+ -->
**Front:** How does the 'Namespace Auto-Provision' controller differ from 'Namespace Exists'?
**Back:** Namespace Auto-Provision automatically creates missing namespaces, while Namespace Exists rejects requests for non-existent namespaces. Auto-Provision is deprecated in favor of Namespace Lifecycle.
**Tags:** ankidote deprecation namespace-controllers

---

<!-- note:1772499457972 model:Basic+ -->
**Front:** What is the function of the 'Always Pull Images' admission controller?
**Back:** This controller ensures that images are pulled from a registry on each pod creation, enforcing consistent image versions across clusters.
**Tags:** ankidote built-in-controllers image-policies

---

<!-- note:1772499457973 model:Basic+ -->
**Front:** How can you enable additional admission controllers in Kubernetes?
**Back:** Update the `--enable-admission-plugins` flag in the kube-apiserver configuration. For kubeadm, modify the kube-apiserver manifest file to include the desired plugins.
**Tags:** admission-controllers ankidote configuration

---

<!-- note:1772499457976 model:Basic+ -->
**Front:** What command checks enabled admission controllers in a Kubernetes cluster?
**Back:** Run `kube-apiserver -h | grep enable-admission-plugins` on the control plane node. For kubeadm clusters, use `kubectl exec kube-apiserver-controlplane -n kube-system -- kube-apiserver -h | grep enable-admission-plugins`.
**Tags:** admission-controllers ankidote configuration

---

<!-- note:1772499457977 model:Basic+ -->
**Front:** What is the impact of disabling an admission controller?
**Back:** Disabling an admission controller removes its validation or modification rules from the API request lifecycle, potentially allowing unsafe operations or policy violations.
**Tags:** ankidote configuration security

---

<!-- note:1772499457978 model:Basic+ -->
**Front:** Provide an example of a pod manifest that admission controllers might modify.
**Back:** A pod manifest with security context settings like `runAsUser: 0` or `capabilities: add: ["MAC_ADMIN"]` would be modified by admission controllers to enforce security policies.
**Tags:** ankidote pod-manifests security-policies

---

<!-- note:1772499457980 model:Basic+ -->
**Front:** What is the purpose of the 'Event Rate Limit' admission controller?
**Back:** This controller restricts the number of concurrent API requests processed by the API server, preventing resource exhaustion and ensuring stable cluster performance.
**Tags:** ankidote built-in-controllers rate-limiting

---

<!-- note:1772499457982 model:Basic+ -->
**Front:** How does the Namespace Lifecycle admission controller improve security?
**Back:** Namespace Lifecycle replaces deprecated controllers by rejecting requests for non-existent namespaces and protecting critical namespaces (e.g., default, kube-system) from deletion.
**Tags:** ankidote deprecation namespace-security

---

<!-- note:1772499457983 model:Basic+ -->
**Front:** What happens when the 'Namespace Auto-Provision' controller is enabled?
**Back:** The controller automatically creates missing namespaces when a pod is deployed to a non-existent namespace, avoiding 'namespace not found' errors.
**Tags:** ankidote auto-provisioning namespace-controllers

---

<!-- note:1772499457985 model:Basic+ -->
**Front:** What is the significance of the 'Default Storage Class' admission controller?
**Back:** This controller automatically assigns a default storage class to persistent volume claims if none is specified, ensuring consistent storage configuration across the cluster.
**Tags:** ankidote built-in-controllers storage

---

<!-- note:1772499457987 model:Basic+ -->
**Front:** What is the primary security benefit of admission controllers?
**Back:** Admission controllers enforce complex security policies, such as restricting root user containers, validating image sources, and applying metadata labels, ensuring cluster compliance with organizational standards.
**Tags:** ankidote policy-enforcement security

---

<!-- note:1772499486548 model:Basic+ -->
**Front:** What is the primary purpose of namespaces in Kubernetes control plane isolation?
**Back:** Namespaces partition cluster resources among users, isolating resources within each namespace and enabling team-specific resource management without name conflicts.
**Tags:** ankidote control-plane-isolation kubernetes-namespaces

---

<!-- note:1772499486551 model:Basic+ -->
**Front:** How do namespaces help with security policies in Kubernetes?
**Back:** Security policies like RBAC and network policies are scoped to individual namespaces, ensuring isolation and preventing cross-namespace resource access.
**Tags:** ankidote namespace-security rbac

---

<!-- note:1772499486554 model:Basic+ -->
**Front:** What command creates a new namespace in Kubernetes?
**Back:** kubectl create namespace <namespace-name>
**Tags:** ankidote kubernetes-commands namespace-creation

---

<!-- note:1772499486565 model:Basic+ -->
**Front:** What principle ensures users have minimal access rights in control plane isolation?
**Back:** The principle of least privilege restricts users to only the namespaces and resources they need, preventing unauthorized modifications.
**Tags:** access-control ankidote least-privilege

---

<!-- note:1772499486568 model:Basic+ -->
**Front:** What Kubernetes object defines permissions for a namespace?
**Back:** A Role object defines permissions (verbs) for specific resources (e.g., pods, services) within a namespace.
**Tags:** ankidote kubernetes-objects rbac

---

<!-- note:1772499486570 model:Basic+ -->
**Front:** What connects a user to a Role in Kubernetes?
**Back:** A RoleBinding links a user or service account to a Role, granting them the defined permissions within a namespace.
**Tags:** ankidote rbac rolebinding

---

<!-- note:1772499486573 model:Basic+ -->
**Front:** What are the permissions granted by the developer-role in the example?
**Back:** The Role grants 'get, list, watch, create, update, delete' permissions on pods and services within the 'development' namespace.
**Tags:** ankidote namespace-permissions rbac-example

---

<!-- note:1772499486575 model:Basic+ -->
**Front:** What is the purpose of the YAML configuration shown?
**Back:** The YAML creates a Role with specific permissions and a RoleBinding that ties the 'pranjal' user to the 'developer-role' in the 'development' namespace.
**Tags:** ankidote kubernetes-security rbac-configuration

---

<!-- note:1772499486577 model:Basic+ -->
**Front:** Which Kubernetes feature enforces strict access control between teams?
**Back:** Role-Based Access Control (RBAC) enforces strict access control by scoping permissions to specific namespaces and resources.
**Tags:** ankidote rbac team-isolation

---

<!-- note:1772499486580 model:Basic+ -->
**Front:** What ensures resources in one namespace don't conflict with another?
**Back:** Namespaces allow resource name overlaps across namespaces, preventing naming conflicts while maintaining isolation.
**Tags:** ankidote namespace-conflict resource-isolation

---

<!-- note:1772499512369 model:Basic+ -->
**Front:** What is the default DNS behavior in Kubernetes for cross-namespace resolution?
**Back:** By default, Kubernetes allows any service or pod to resolve FQDNs across namespaces using formats like backend.namespace-a.svc.cluster.local.
**Tags:** ankidote kubernetes-dns multi-tenant

---

<!-- note:1772499512373 model:Basic+ -->
**Front:** Why is cross-namespace DNS resolution problematic in multi-tenant clusters?
**Back:** It compromises tenant isolation, enabling accidental or malicious discovery of resources across namespaces.
**Tags:** ankidote dns-isolation multi-tenant security

---

<!-- note:1772499512376 model:Basic+ -->
**Front:** What CoreDNS directive enforces namespace-specific DNS resolution?
**Back:** The `fallthrough in-namespace` directive in the Kubernetes block restricts queries to the originating namespace.
**Tags:** ankidote coredns dns-configuration multi-tenant

---

<!-- note:1772499512380 model:Basic+ -->
**Front:** What command edits the CoreDNS ConfigMap in kube-system namespace?
**Back:** kubectl edit configmap coredns -n kube-system
**Tags:** ankidote configmap coredns kubernetes-commands

---

<!-- note:1772499512383 model:Basic+ -->
**Front:** What test verifies DNS isolation between namespaces?
**Back:** Deploy a pod in one namespace and attempt to resolve a service in another using nslookup, e.g., nslookup backend.namespace-b.svc.cluster.local
**Tags:** ankidote dns-isolation multi-tenant testing

---

<!-- note:1772499512386 model:Basic+ -->
**Front:** What is the purpose of the `fallthrough in-namespace` directive?
**Back:** It ensures DNS queries are only resolved for services/pods in the same namespace as the querying pod.
**Tags:** ankidote coredns dns-configuration security

---

<!-- note:1772499512388 model:Basic+ -->
**Front:** What happens after modifying the CoreDNS ConfigMap?
**Back:** CoreDNS automatically reloads the configuration in its running pods without requiring restarts.
**Tags:** ankidote configuration coredns kubernetes

---

<!-- note:1772499512389 model:Basic+ -->
**Front:** What is the primary benefit of restricting cross-namespace DNS?
**Back:** Enhanced security and isolation between tenants sharing the same Kubernetes cluster.
**Tags:** ankidote dns-isolation multi-tenant security

---

<!-- note:1772499667246 model:Basic+ -->
**Front:** How do you create a Kubernetes secret with literal values for keys?
**Back:** Use `kubectl create secret generic <name> --from-literal=key1=value1 --from-literal=key2=value2` to define secrets with explicit key-value pairs.
**Tags:** ankidote kubernetes-secrets secret-creation

---

<!-- note:1772499667250 model:Basic+ -->
**Front:** What encoding format is used for secret data in Kubernetes?
**Back:** Secret data is stored as Base64-encoded strings in etcd. For example, `C3VwZXJzZWNyZQ==` decodes to `supersecret`.
**Tags:** ankidote data-encoding secret-encoding

---

<!-- note:1772499667253 model:Basic+ -->
**Front:** Where are Kubernetes secrets stored in etcd?
**Back:** Secrets are stored under paths like `/registry/secrets/<namespace>/<secret-name>` in etcd.
**Tags:** ankidote etcd-storage secret-location

---

<!-- note:1772499667255 model:Basic+ -->
**Front:** What command retrieves raw etcd data for a secret?
**Back:** Use `ETCDCTL_API=3 etcdctl --cacert=... --cert=... --key=... get /registry/secrets/default/<secret-name>` to view unencrypted data.
**Tags:** ankidote data-inspection etcdctl-usage

---

<!-- note:1772499667258 model:Basic+ -->
**Front:** How do you install etcdctl on Ubuntu?
**Back:** Run `apt-get install etcd-client` to install the etcdctl client tool.
**Tags:** ankidote etcdctl-installation package-management

---

<!-- note:1772499667261 model:Basic+ -->
**Front:** What command verifies encryption of new secrets in etcd?
**Back:** Use `ETCDCTL_API=3 etcdctl --cacert=... --cert=... --key=... get /registry/secrets/default/<secret-name>` to check encrypted data.
**Tags:** ankidote encryption-verification etcd-data-inspection

---

<!-- note:1772499667264 model:Basic+ -->
**Front:** How do you check if encryption at rest is enabled in Kubernetes?
**Back:** Look for the `--encryption-provider-config` flag in the kube-apiserver manifest or process arguments.
**Tags:** ankidote api-server-config encryption-check

---

<!-- note:1772499667267 model:Basic+ -->
**Front:** What is the structure of an encryption configuration file?
**Back:** The file defines `resources` (e.g., secrets) and `providers` (e.g., `aescbc` with keys). Example:
```yaml
resources:
  - resources: [secrets]
providers:
  - aescbc: {keys: [...]}
  - identity: {}
```
**Tags:** ankidote config-file encryption-configuration

---

<!-- note:1772499667270 model:Basic+ -->
**Front:** What are the requirements for an AES-CBC encryption key?
**Back:** The key must be a base64-encoded 32-byte value. Generate it with `head -c 32 /dev/urandom | base64`.
**Tags:** ankidote encryption-provider key-generation

---

<!-- note:1772499667273 model:Basic+ -->
**Front:** What changes are needed in the kube-apiserver manifest for encryption?
**Back:** Add the `--encryption-provider-config` flag and mount the encryption config file via a volume. Example:
```yaml
- --encryption-provider-config=/etc/kubernetes/enc/enc.yaml
volumeMounts: [...]```
```yaml
volumes: [...]```
**Tags:** ankidote api-server-config manifest-updates

---

<!-- note:1772499667277 model:Basic+ -->
**Front:** How do you verify encryption of new secrets after configuration?
**Back:** Create a new secret with `kubectl create secret generic <name> --from-literal=key=value` and inspect etcd data using etcdctl to confirm encryption.
**Tags:** ankidote encryption-testing secret-verification

---

<!-- note:1772499667280 model:Basic+ -->
**Front:** What is the purpose of encryption at rest for Kubernetes secrets?
**Back:** Encryption at rest protects secret data stored in etcd, preventing unauthorized access to plaintext values.
**Tags:** ankidote data-protection encryption-purpose

---

<!-- note:1772499700075 model:Basic+ -->
**Front:** What is multi-team tenancy in Kubernetes?
**Back:** Multi-team tenancy refers to managing and isolating resources for different internal teams within a single Kubernetes cluster, using namespaces and role-based access control (RBAC) to ensure logical separation and fair resource allocation.
**Tags:** ankidote kubernetes-security multi-team-tenancy

---

<!-- note:1772499700080 model:Basic+ -->
**Front:** What is multi-customer tenancy in Kubernetes?
**Back:** Multi-customer tenancy involves hosting and segregating applications for external customers in a shared Kubernetes cluster, requiring strict security measures to isolate data and meet regulatory standards like GDPR or HIPAA.
**Tags:** ankidote kubernetes-security multi-customer-tenancy

---

<!-- note:1772499700083 model:Basic+ -->
**Front:** What are the key differences between multi-team and multi-customer tenancy?
**Back:** Multi-team tenancy focuses on internal teams with direct cluster access, while multi-customer tenancy targets external clients with no direct access. Both use namespaces, but multi-customer requires stricter security and compliance.
**Tags:** ankidote kubernetes-tenancy multi-tenancy-differences

---

<!-- note:1772499700086 model:Basic+ -->
**Front:** How does isolation differ between multi-team and multi-customer tenancy?
**Back:** Both models use Kubernetes namespaces for isolation, but multi-customer tenancy demands stricter separation and security measures due to regulatory requirements and data sensitivity.
**Tags:** ankidote isolation-security kubernetes-tenancy

---

<!-- note:1772499700089 model:Basic+ -->
**Front:** What access control mechanisms are critical for multi-team tenancy?
**Back:** Role-based access control (RBAC) and namespace quotas are critical for multi-team tenancy to ensure secure resource allocation and prevent unauthorized access.
**Tags:** access-control ankidote multi-team-tenancy

---

<!-- note:1772499700091 model:Basic+ -->
**Front:** What security protocols are essential for multi-customer tenancy?
**Back:** Multi-customer tenancy requires adherence to stringent security protocols such as GDPR, HIPAA, or other regulatory standards to ensure data isolation and compliance.
**Tags:** ankidote multi-customer-tenancy security-protocols

---

<!-- note:1772499700094 model:Basic+ -->
**Front:** Which tenancy model is suitable for internal team collaboration?
**Back:** Multi-team tenancy is designed for managing internal organizational teams, enabling shared infrastructure with logical separation and direct cluster access.
**Tags:** ankidote kubernetes-tenancy multi-team-tenancy

---

<!-- note:1772499700096 model:Basic+ -->
**Front:** Why is direct cluster access important in multi-team tenancy?
**Back:** Direct cluster access via tools like kubectl or GitOps controllers allows internal teams to manage their resources efficiently while maintaining control over their namespaces and quotas.
**Tags:** access-control ankidote multi-team-tenancy

---

<!-- note:1772499743875 model:Basic+ -->
**Front:** Why is encryption important for pod-to-pod communication in Kubernetes?
**Back:** Encryption protects sensitive data transmitted between pods, preventing data breaches and unauthorized access. Without encryption, data like customer phone numbers or addresses could be intercepted in plain text.
**Tags:** ankidote kubernetes-encryption mtls-necessity

---

<!-- note:1772499743877 model:Basic+ -->
**Front:** What are the steps involved in establishing a secure connection between two pods using mTLS?
**Back:** 1. Pod A requests Pod B's certificate.
2. Pod B responds with its certificate and requests Pod A's certificate.
3. Pod A validates Pod B's certificate and sends its public certificate with a symmetric key.
4. Pod B validates Pod A's certificate, then both use the symmetric key for encrypted communication.
**Tags:** ankidote mtls-process pod-communication

---

<!-- note:1772499743879 model:Basic+ -->
**Front:** What is the primary challenge of managing encryption across a Kubernetes cluster with hundreds of pods?
**Back:** Managing encryption across a cluster is complex due to varying encryption algorithms used by different applications, leading to potential security gaps and inconsistencies.
**Tags:** ankidote cluster-encryption mtls-challenges

---

<!-- note:1772499743881 model:Basic+ -->
**Front:** Which tools enable mTLS at the network layer in Kubernetes?
**Back:** Popular tools include Istio and Linkerd. These service meshes abstract encryption from applications, providing centralized policy management and consistent security across heterogeneous workloads.
**Tags:** ankidote mtls-tools service-mesh

---

<!-- note:1772499743882 model:Basic+ -->
**Front:** What is the difference between Istio's permissive and strict mTLS modes?
**Back:** Permissive mode encrypts traffic when possible but allows unencrypted communication with external services. Strict mode requires all traffic to use mTLS, enforcing encryption but requiring full mTLS compatibility across services.
**Tags:** ankidote istio-modes mtls-configuration

---

<!-- note:1772499743885 model:Basic+ -->
**Front:** How does Istio implement mTLS for pod communication?
**Back:** Istio uses sidecar containers to intercept and encrypt outbound traffic. The sidecar decrypts messages upon receipt, ensuring secure communication without modifying application code.
**Tags:** ankidote istio-implementation sidecar-containers

---

<!-- note:1772499743888 model:Basic+ -->
**Front:** What are the benefits of using mTLS with service meshes like Istio?
**Back:** Benefits include offloading encryption from applications, centralized policy management, consistent security across diverse workloads, and automatic sidecar deployment for seamless encryption.
**Tags:** ankidote mtls-advantages service-mesh-benefits

---

<!-- note:1772499743890 model:Basic+ -->
**Front:** What is a critical consideration before enabling strict mTLS mode in Istio?
**Back:** All services must be mTLS-compatible to avoid connectivity issues, as strict mode requires every service-to-service communication to use encrypted channels.
**Tags:** ankidote istio-strict-mode mtls-compatibility

---

<!-- note:1772499790002 model:Basic+ -->
**Front:** What is Cilium used for in Kubernetes environments?
**Back:** Cilium secures network connectivity between containerized applications using eBPF to enforce advanced network security policies, including Pod-to-Pod encryption.
**Tags:** ankidote cilium-purpose kubernetes-security

---

<!-- note:1772499790008 model:Basic+ -->
**Front:** What technology does Cilium use for efficient data processing?
**Back:** Cilium leverages eBPF (Extended Berkeley Packet Filter) for highly efficient data processing with minimal performance overhead.
**Tags:** ankidote cilium-technology ebpf

---

<!-- note:1772499790012 model:Basic+ -->
**Front:** What are the key features of Cilium's Pod-to-Pod encryption?
**Back:** Key features include flexible encryption options, end-to-end security, and policy-driven control for precise security management.
**Tags:** ankidote cilium-features pod-to-pod-encryption

---

<!-- note:1772499790016 model:Basic+ -->
**Front:** What is the first step in setting up Cilium for encryption?
**Back:** The first step is deploying Cilium on your Kubernetes cluster via Helm or standard manifests.
**Tags:** ankidote cilium-setup installation

---

<!-- note:1772499790019 model:Basic+ -->
**Front:** What is required for key management in Cilium?
**Back:** Cilium uses its native key management system or integrates with existing infrastructure for encryption key management.
**Tags:** ankidote cilium-key-management encryption

---

<!-- note:1772499790022 model:Basic+ -->
**Front:** What benefits does Cilium provide for monitoring and performance?
**Back:** Cilium offers minimal performance overhead through eBPF, along with encryption, identity management, and policy enforcement.
**Tags:** ankidote cilium-benefits performance

---

<!-- note:1772499790025 model:Basic+ -->
**Front:** What ensures continuous encryption in Cilium?
**Back:** End-to-end security ensures data remains encrypted throughout its network journey between pods.
**Tags:** ankidote cilium-encryption security

---

<!-- note:1772499790027 model:Basic+ -->
**Front:** How does Cilium enable policy-driven encryption?
**Back:** Cilium allows customizable encryption policies based on namespaces or labels to control encryption application.
**Tags:** ankidote cilium-policies policy-enforcement

---

<!-- note:1772499908799 model:Basic+ -->
**Front:** What is namespace isolation in Kubernetes?
**Back:** Namespace isolation divides a Kubernetes cluster into logical sections, allowing teams or projects to manage resources independently. It uses namespaces and RBAC to enforce access controls and resource separation.
**Tags:** ankidote kubernetes-isolation namespace-isolation

---

<!-- note:1772499908801 model:Basic+ -->
**Front:** How does pod isolation work in Kubernetes?
**Back:** Pod isolation ensures pods are isolated from each other while sharing resources within the same namespace. Containers in a pod share resources but remain isolated from other pods to prevent interference.
**Tags:** ankidote kubernetes-isolation pod-isolation

---

<!-- note:1772499908805 model:Basic+ -->
**Front:** What is network isolation in Kubernetes?
**Back:** Network isolation restricts communication between pods using network policies. These policies define rules to allow or deny traffic between pods, ensuring secure internal network boundaries.
**Tags:** ankidote kubernetes-isolation network-isolation

---

<!-- note:1772499908808 model:Basic+ -->
**Front:** What is node isolation in Kubernetes?
**Back:** Node isolation enforces infrastructure-level separation by dedicating nodes to specific teams or isolating them with access policies. Nodes can host multiple teams under strict controls or be dedicated to single teams.
**Tags:** ankidote kubernetes-isolation node-isolation

---

<!-- note:1772499908812 model:Basic+ -->
**Front:** What are the two main isolation levels in Kubernetes?
**Back:** Kubernetes provides control plane isolation (namespaces, RBAC) and data plane isolation (network policies, storage, node isolation) to separate workloads across the cluster's control and data planes.
**Tags:** ankidote control-plane data-plane kubernetes-isolation

---

<!-- note:1772499908814 model:Basic+ -->
**Front:** What is the difference between hard and soft isolation in Kubernetes?
**Back:** Hard isolation dedicates physical/virtual infrastructure to tenants for complete resource segregation. Soft isolation shares infrastructure but uses namespaces, quotas, and network policies for logical separation.
**Tags:** ankidote hard-isolation kubernetes-isolation soft-isolation

---

<!-- note:1772500077302 model:Basic+ -->
**Front:** What is the purpose of Kubernetes Secrets?
**Back:** Kubernetes Secrets securely store sensitive data like passwords, keys, and tokens in encoded format, preventing hardcoded credentials in application code.
**Tags:** ankidote kubernetes-secrets security-best-practices

---

<!-- note:1772500077306 model:Basic+ -->
**Front:** How do you encode plain text values for Kubernetes Secrets?
**Back:** Use base64 encoding. Example: echo -n 'mysql' | base64 outputs bXlzcWw=.
**Tags:** ankidote base64-encoding secret-creation

---

<!-- note:1772500077308 model:Basic+ -->
**Front:** What command creates a Secret using the imperative method?
**Back:** kubectl create secret generic app-secret --from-literal=DB_Host=mysql --from-literal=DB_User=root --from-literal=DB_Password=paswrd
**Tags:** ankidote imperative-method secret-creation

---

<!-- note:1772500077310 model:Basic+ -->
**Front:** What YAML structure defines a Kubernetes Secret declaratively?
**Back:** apiVersion: v1
kind: Secret
metadata:
  name: app-secret
data:
  DB_Host: bXlzcWw=
  DB_User: cm9vdA==
  DB_Password: cGFzd3Jk
**Tags:** ankidote declarative-method yaml-structure

---

<!-- note:1772500077314 model:Basic+ -->
**Front:** How do you inject Secrets into a Pod as environment variables?
**Back:** Use envFrom in the Pod specification: envFrom: - secretRef: name: app-secret
**Tags:** ankidote environment-variables secret-injection

---

<!-- note:1772500077316 model:Basic+ -->
**Front:** What command decodes a base64 encoded Secret value?
**Back:** echo -n 'bXlzcWw=' | base64 --decode outputs mysql
**Tags:** ankidote base64-decoding secret-viewing

---

<!-- note:1772500077323 model:Basic+ -->
**Front:** What is the difference between ConfigMaps and Secrets?
**Back:** ConfigMaps store non-sensitive data as plain text, while Secrets encode sensitive data using base64 for secure storage.
**Tags:** ankidote configmap-vs-secret security-considerations

---

<!-- note:1772500077325 model:Basic+ -->
**Front:** How do you mount a Secret as a volume in a Pod?
**Back:** Define a volume with secretName: app-secret and mount it into the container's filesystem, e.g., /opt/app-secret-volumes.
**Tags:** ankidote secret-injection volume-mounting

---

<!-- note:1772500077331 model:Basic+ -->
**Front:** What command lists all Secrets in a namespace?
**Back:** kubectl get secrets
**Tags:** ankidote kubectl-commands secret-management

---

<!-- note:1772500077333 model:Basic+ -->
**Front:** What security best practice is recommended for Kubernetes Secrets?
**Back:** Avoid storing Secret definitions in version control systems like GitHub, as they are not encrypted by default.
**Tags:** ankidote etcd-encryption security-best-practices

---

<!-- note:1772500077335 model:Basic+ -->
**Front:** How do you enable encryption at rest for Kubernetes Secrets?
**Back:** Configure the kube-apiserver with an encryption-provider-config file specifying encryption algorithms and keys, then mount the config file in the apiserver Pod.
**Tags:** ankidote encryption-at-rest security-configuration

---

<!-- note:1772500077338 model:Basic+ -->
**Front:** What are three third-party secret providers mentioned in the text?
**Back:** AWS Provider, Azure Provider, GCP Provider, and Vault Provider.
**Tags:** ankidote secret-management third-party-providers

---

<!-- note:1772500077341 model:Basic+ -->
**Front:** What command displays a Secret's encoded data in YAML format?
**Back:** kubectl get secret app-secret -o yaml
**Tags:** ankidote secret-viewing yaml-output

---

<!-- note:1772500077343 model:Basic+ -->
**Front:** What is the risk of storing Secrets in etcd without encryption?
**Back:** Anyone with access to etcd can decode Secrets using base64, exposing sensitive data.
**Tags:** ankidote data-encryption etcd-security

---

<!-- note:1772500077345 model:Basic+ -->
**Front:** How do you prevent unauthorized access to Secrets in Kubernetes?
**Back:** Implement Role-Based Access Control (RBAC) to restrict Pod and Deployment creation permissions in the same namespace.
**Tags:** access-control ankidote rbac

---

<!-- note:1772500116703 model:Basic+ -->
**Front:** What is the purpose of integrating OPA with Kubernetes using Gatekeeper?
**Back:** To enforce policies via the OPA Constraint Framework and Kubernetes admission controllers, enabling governance and policy enforcement through CRD-based policies.
**Tags:** ankidote constraint-framework gatekeeper kubernetes opa

---

<!-- note:1772500116706 model:Basic+ -->
**Front:** What command deploys OPA Gatekeeper in Kubernetes?
**Back:** kubectl apply -f https://raw.githubusercontent.com/open-policy-agent/gatekeeper/v3.14.0/deploy/gatekeeper
**Tags:** ankidote gatekeeper installation opa

---

<!-- note:1772500116707 model:Basic+ -->
**Front:** How to verify OPA Gatekeeper deployment?
**Back:** Run kubectl get all -n gatekeeper-system to check running components and expected output includes pods, services, and deployments in the gatekeeper-system namespace.
**Tags:** ankidote gatekeeper opa verification

---

<!-- note:1772500116709 model:Basic+ -->
**Front:** What is the role of the OPA Constraint Framework?
**Back:** It allows declaring policies with required conditions, enforcing them via Kubernetes admission controllers, and defining checks for policy compliance.
**Tags:** ankidote constraint-framework opa policy-enforcement

---

<!-- note:1772500116710 model:Basic+ -->
**Front:** What does the Rego code in Example 1 validate?
**Back:** It ensures pods in a namespace include the 'billing' label by comparing provided labels against a fixed required set.
**Tags:** ankidote label-validation policy-enforcement rego

---

<!-- note:1772500116712 model:Basic+ -->
**Front:** What are the key components in Rego policy validation?
**Back:** The 'provided' variable extracts labels from the pod, 'required' defines mandatory labels, and 'missing' identifies absent labels to trigger violations.
**Tags:** ankidote policy-validation rego variables

---

<!-- note:1772500116716 model:Basic+ -->
**Front:** How to make OPA policies dynamic with parameters?
**Back:** Use Constraint Templates to define CRDs that accept parameters (e.g., required labels) instead of hardcoding values in Rego policies.
**Tags:** ankidote constraint-templates dynamic-policies parameterization

---

<!-- note:1772500116719 model:Basic+ -->
**Front:** What is the structure of a Constraint Template YAML?
**Back:** It defines a CRD with a 'rego' block containing the policy logic and targets admission controllers, e.g., the provided requiredlabels-template.yaml example.
**Tags:** ankidote constraint-templates gatekeeper yaml

---

<!-- note:1772500116723 model:Basic+ -->
**Front:** How to enforce namespace-specific labels with OPA?
**Back:** Define constraints that match specific namespaces and pass parameters via 'input.parameters.labels' to dynamically set required labels in Rego.
**Tags:** ankidote constraints namespaces parameters

---

<!-- note:1772500116725 model:Basic+ -->
**Front:** What is the first step in integrating OPA with Kubernetes?
**Back:** Install OPA Gatekeeper using kubectl apply with the Gatekeeper deployment manifest from the official repository.
**Tags:** ankidote installation integration-steps

---

<!-- note:1772500116730 model:Basic+ -->
**Front:** What command checks Gatekeeper components post-deployment?
**Back:** kubectl get all -n gatekeeper-system to verify pods, services, and deployments are running in the gatekeeper-system namespace.
**Tags:** ankidote deployment gatekeeper verification

---

<!-- note:1772500116732 model:Basic+ -->
**Front:** What RBAC permissions are required for Gatekeeper deployment?
**Back:** Ensure the user has sufficient RBAC permissions to deploy and manage resources in the target Kubernetes namespace.
**Tags:** ankidote deployment permissions rbac

---

<!-- note:1772500116735 model:Basic+ -->
**Front:** What is the structure of a Constraint Template for label validation?
**Back:** A YAML file with 'apiVersion', 'kind', 'metadata', and 'spec' sections defining the CRD, targets, and Rego policy logic as shown in requiredlabels-template.yaml.
**Tags:** ankidote constraint-templates gatekeeper yaml

---

<!-- note:1772500116738 model:Basic+ -->
**Front:** What commands apply the OPA Constraint Template and Constraint?
**Back:** kubectl apply -f requiredlabels-template.yaml && kubectl apply -f require-label-billing.yaml to deploy the template and namespace-specific constraint.
**Tags:** ankidote application commands deployment

---

<!-- note:1772500214823 model:Basic+ -->
**Front:** What is the purpose of Open Policy Agent (OPA) in the described scenario?
**Back:** OPA provides a centralized policy decision point for managing authorization, allowing services to query policies via an API to determine access permissions.
**Tags:** ankidote authorization opa-architecture

---

<!-- note:1772500214826 model:Basic+ -->
**Front:** What is the default port used by the OPA server?
**Back:** The OPA server listens on port 8181 by default.
**Tags:** ankidote networking opa-deployment

---

<!-- note:1772500214827 model:Basic+ -->
**Front:** How do you start the OPA server with the `-s` flag?
**Back:** Run `./opa run -s` to start the server in standalone mode.
**Tags:** ankidote command-line opa-deployment

---

<!-- note:1772500214829 model:Basic+ -->
**Front:** What is the structure of a basic Rego policy for authorization?
**Back:** A Rego policy defines a `package` and uses `import input` to evaluate conditions. Example:

```rego
package httpapi.authz
import input
default allow = false
allow { input.path == "home"; input.user == "john" }
```
**Tags:** ankidote policy-authoring rego-syntax

---

<!-- note:1772500214831 model:Basic+ -->
**Front:** How do you load a Rego policy into OPA?
**Back:** Use a PUT request:
```bash
curl -X PUT --data-binary @example.rego http://localhost:8181/v1/policies/example1
```
**Tags:** ankidote opa-api policy-loading

---

<!-- note:1772500214833 model:Basic+ -->
**Front:** What input format does the Flask app send to OPA for authorization checks?
**Back:** A JSON dictionary with `input` containing `user` and `path` fields:
```python
input_dict = {"input": {"user": user, "path": "home"}}
```
**Tags:** ankidote flask-integration opa-api

---

<!-- note:1772500214834 model:Basic+ -->
**Front:** What is the purpose of OPA's testing framework?
**Back:** The testing framework runs Rego test files to validate policy behavior before deployment. Example tests check allow/deny rules for different inputs.
**Tags:** ankidote opa-testing policy-validation

---

<!-- note:1772500214835 model:Basic+ -->
**Front:** How do you execute OPA tests?
**Back:** Run `opa test -v` to execute tests and display results. Example output shows PASS/FAIL status for each test case.
**Tags:** ankidote command-line opa-testing

---

<!-- note:1772500214836 model:Basic+ -->
**Front:** What is the role of the Rego playground?
**Back:** The Rego playground at [play.openpolicyagent.org](https://play.openpolicyagent.org) allows users to experiment with policy writing, test inputs, and refine policies interactively.
**Tags:** ankidote policy-debugging rego-playground

---

<!-- note:1772500214837 model:Basic+ -->
**Front:** What is the default behavior of OPA's API?
**Back:** By default, OPA's API is open and unauthenticated. Proper network security measures are recommended for production environments.
**Tags:** ankidote api-configuration opa-security

---

<!-- note:1772500247151 model:Basic+ -->
**Front:** What is Kubernetes multi-tenancy?
**Back:** Multi-tenancy in Kubernetes refers to sharing a single cluster among multiple users, teams, or customers while maintaining isolation, security, and efficient resource management through mechanisms like namespaces, RBAC, and network policies.
**Tags:** ankidote kubernetes-multi-tenancy resource-management

---

<!-- note:1772500247155 model:Basic+ -->
**Front:** What are the key benefits of Kubernetes multi-tenancy?
**Back:** Benefits include cost efficiency (reduced hardware/operational costs), enhanced resource usage, simplified management through centralized control, and robust security via isolation mechanisms.
**Tags:** ankidote benefits kubernetes-multi-tenancy

---

<!-- note:1772500247159 model:Basic+ -->
**Front:** What is an example of namespace isolation in Kubernetes?
**Back:** Namespaces act like isolated environments (e.g., different floors in a building), separating resources and access controls while sharing the same cluster infrastructure.
**Tags:** ankidote kubernetes-multi-tenancy namespace-isolation

---

<!-- note:1772500247162 model:Basic+ -->
**Front:** What is the anti-pattern mentioned in the article?
**Back:** Provisioning a separate cluster for each tenant or application, which becomes unsustainable due to complexity and operational overhead as tenant count grows.
**Tags:** ankidote anti-patterns kubernetes-multi-tenancy

---

<!-- note:1772500247166 model:Basic+ -->
**Front:** What mechanisms ensure security in Kubernetes multi-tenancy?
**Back:** Security is enforced through Kubernetes RBAC (access control), network policies (isolating traffic), and storage isolation to prevent data leakage between tenants.
**Tags:** ankidote kubernetes-multi-tenancy security

---

<!-- note:1772500247169 model:Basic+ -->
**Front:** What are the main approaches to resource management in multi-tenancy?
**Back:** Approaches include namespace isolation, resource quotas (limiting CPU/memory), network policies (controlling traffic), and storage isolation to ensure fair resource sharing.
**Tags:** ankidote kubernetes-multi-tenancy resource-management

---

<!-- note:1772500247176 model:Basic+ -->
**Front:** Why is shared infrastructure management critical in multi-tenancy?
**Back:** Shared resources like networking, storage, and nodes require careful management to prevent resource contention, overconsumption, and ensure system stability and performance.
**Tags:** ankidote kubernetes-multi-tenancy shared-infrastructure

---

<!-- note:1772500247179 model:Basic+ -->
**Front:** What is the role of RBAC in Kubernetes multi-tenancy?
**Back:** RBAC (Role-Based Access Control) enforces access restrictions, ensuring tenants can only interact with resources and systems they are authorized to use.
**Tags:** ankidote kubernetes-multi-tenancy rbac

---

<!-- note:1772500247183 model:Basic+ -->
**Front:** What is the primary challenge of scaling multi-tenancy?
**Back:** Managing increasing complexity in security policies, access controls, and resource allocations while maintaining compliance, data privacy, and system performance.
**Tags:** ankidote kubernetes-multi-tenancy scaling-challenges

---

<!-- note:1772500247186 model:Basic+ -->
**Front:** How does the building metaphor explain Kubernetes multi-tenancy?
**Back:** The cluster is likened to a building, with namespaces as floors (isolated environments), shared resources as common areas (networking/storage), and RBAC as access badges controlling tenant interactions.
**Tags:** ankidote kubernetes-multi-tenancy metaphor

---

<!-- note:1772500284928 model:Basic+ -->
**Front:** What is Pod Security Admission (PSA) in Kubernetes?
**Back:** Pod Security Admission (PSA) is an admission controller that replaces Pod Security Policies (PSP) in Kubernetes. It provides a safer, easier-to-use, and more extensible solution for enforcing pod security standards across clusters.
**Tags:** ankidote kubernetes-security pod-security-admission

---

<!-- note:1772500284930 model:Basic+ -->
**Front:** What are the three built-in Pod Security Profiles?
**Back:** The three built-in profiles are: 1) Privileged (minimal restrictions), 2) Baseline (balanced security for most applications), and 3) Restricted (strict security with potential compatibility trade-offs).
**Tags:** ankidote kubernetes-security pod-security-profiles

---

<!-- note:1772500284932 model:Basic+ -->
**Front:** What is the purpose of the 'enforce' mode in PSA?
**Back:** The 'enforce' mode rejects pod creation requests that violate the specified security policy, ensuring strict compliance with the configured profile.
**Tags:** ankidote kubernetes-security pod-security-modes

---

<!-- note:1772500284935 model:Basic+ -->
**Front:** How do you verify PSA is enabled in a Kubernetes cluster?
**Back:** Run `kubectl exec -n kube-system kube-apiserver-controlplane -it -- kube-apiserver -h | grep enable-admission-plugins` to check if 'PodSecurity' is listed in the enabled admission plugins.
**Tags:** ankidote kubernetes-apiserver pod-security-verification

---

<!-- note:1772500284937 model:Basic+ -->
**Front:** What command labels a namespace with the 'restricted' profile and 'enforce' mode?
**Back:** Use `kubectl label ns <namespace> pod-security.kubernetes.io/enforce=restricted` to apply the restricted profile with enforce mode to a namespace.
**Tags:** ankidote kubernetes-namespace pod-security-configuration

---

<!-- note:1772500284939 model:Basic+ -->
**Front:** What is the key difference between Baseline and Restricted profiles?
**Back:** The Baseline profile prevents unauthorized privilege escalation while supporting most containerized apps, whereas the Restricted profile enforces strict security best practices, potentially limiting compatibility.
**Tags:** ankidote kubernetes-security pod-security-profiles

---

<!-- note:1772500284942 model:Basic+ -->
**Front:** What action does the 'warn' mode take for policy violations?
**Back:** The 'warn' mode allows pod creation but issues a warning to the user about the policy violation without blocking the request.
**Tags:** ankidote kubernetes-security pod-security-modes

---

<!-- note:1772500284944 model:Basic+ -->
**Front:** What is the primary benefit of using Pod Security Standards?
**Back:** Pod Security Standards provide a unified, extensible framework to enforce security best practices across namespaces, reducing risks from misconfigured pods.
**Tags:** ankidote kubernetes-security pod-security-standards

---

<!-- note:1772500284946 model:Basic+ -->
**Front:** Which profile enforces strict security measures based on pod hardening best practices?
**Back:** The Restricted profile implements strict security measures based on pod hardening best practices, prioritizing high security over compatibility.
**Tags:** ankidote kubernetes-security pod-security-profiles

---

<!-- note:1772500284948 model:Basic+ -->
**Front:** What is the role of third-party tools like Kyverno or OPA Gatekeeper with PSA?
**Back:** Third-party tools like Kyverno or OPA Gatekeeper manage advanced/custom configurations that PSA does not handle, providing additional policy enforcement capabilities.
**Tags:** ankidote kubernetes-tools pod-security-extensions

---

<!-- note:1772500336749 model:Basic+ -->
**Front:** What security settings are present in the sample pod definition?
**Back:** The sample pod has: privileged: True, runs as root (runAsUser: 0), adds CAP_SYS_BOOT capability, and uses a HostPath volume exposing the host's filesystem.
**Tags:** ankidote kubernetes-security pod-security-policies

---

<!-- note:1772500336753 model:Basic+ -->
**Front:** What is the primary purpose of Pod Security Policies (PSPs)?
**Back:** PSPs validate pod creation requests against security rules and reject insecure configurations by intercepting and enforcing policy compliance.
**Tags:** ankidote kubernetes-admission pod-security-policies

---

<!-- note:1772500336756 model:Basic+ -->
**Front:** How do you enable PSP as an admission controller?
**Back:** Add 'PodSecurityPolicy' to the API server's --enable-admission-plugins parameter, e.g., --enable-admission-plugins=PodSecurityPolicy.
**Tags:** ankidote kubernetes-admission pod-security-policies

---

<!-- note:1772500336757 model:Basic+ -->
**Front:** What YAML creates a PSP that disallows privileged containers?
**Back:** apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: example-psp
spec:
  privileged: false
**Tags:** ankidote kubernetes-policies pod-security-policies

---

<!-- note:1772500336759 model:Basic+ -->
**Front:** What happens when a pod violates PSP rules?
**Back:** The PSP admission controller rejects the pod creation request with an error message, preventing insecure configurations from running.
**Tags:** ankidote kubernetes-admission pod-security-policies

---

<!-- note:1772500336763 model:Basic+ -->
**Front:** What RBAC configuration is needed for PSP access?
**Back:** Create a Role with 'use' verb on the PSP and a RoleBinding linking it to the default ServiceAccount: 

Role:
  apiGroups: ["policy"]
  resources: ["podsecuritypolicies"]
  resourceNames: ["example-psp"]
  verbs: ["use"]

RoleBinding:
  subjects: [ServiceAccount: default]
  roleRef: Role: psp-example-role
**Tags:** ankidote kubernetes-rbac pod-security-policies

---

<!-- note:1772500336766 model:Basic+ -->
**Front:** When were Pod Security Policies deprecated and removed?
**Back:** PSPs were deprecated in Kubernetes 1.21 and completely removed in 1.25, replaced by Pod Security Admission and Pod Security Standards.
**Tags:** ankidote kubernetes-deprecation pod-security-policies

---

<!-- note:1772500381328 model:Basic+ -->
**Front:** What is pod-to-pod encryption in Kubernetes?
**Back:** Pod-to-pod encryption secures communication between Kubernetes pods, ensuring data confidentiality and integrity. It encrypts traffic between pods, whether in the same namespace or across namespaces, protecting against interception and tampering.
**Tags:** ankidote kubernetes-security pod-to-pod-encryption

---

<!-- note:1772500381332 model:Basic+ -->
**Front:** Why is pod-to-pod encryption critical in multi-tenant environments?
**Back:** It protects sensitive data flowing between services in shared infrastructure, preventing unauthorized access and ensuring compliance with standards like GDPR and HIPAA. It also mitigates insider threats and supports zero-trust security models.
**Tags:** ankidote compliance data-security multi-tenant

---

<!-- note:1772500381336 model:Basic+ -->
**Front:** What are the primary benefits of pod-to-pod encryption?
**Back:** It prevents eavesdropping, meets regulatory requirements, secures internal communications, and reduces risks from MITM attacks. It also enhances overall cluster security without significant operational complexity.
**Tags:** ankidote encryption-benefits mitm-prevention security-posture

---

<!-- note:1772500381339 model:Basic+ -->
**Front:** What scenario demonstrates the need for pod-to-pod encryption?
**Back:** An e-commerce application's front-end pod sending credit card details to a back-end pod: unencrypted communication risks data breaches via man-in-the-middle attacks.
**Tags:** ankidote data-breach example use-case

---

<!-- note:1772500381341 model:Basic+ -->
**Front:** What methods implement pod-to-pod encryption?
**Back:** Common methods include Mutual TLS (via service meshes like Istio/Linkerd), Cilium Encryption (using IPsec/WireGuard), and Calico Encryption (leveraging IPsec).
**Tags:** ankidote cilium implementation-methods mTLS

---

<!-- note:1772500381342 model:Basic+ -->
**Front:** What does automated key management in Kubernetes enable?
**Back:** It simplifies encryption setup and management, making it feasible for multi-tenant environments sharing network infrastructure while maintaining secure communication.
**Tags:** ankidote automation key-management multi-tenant

---

<!-- note:1772500381346 model:Basic+ -->
**Front:** How does pod-to-pod encryption support zero-trust security?
**Back:** By treating all connections as untrusted, encryption ensures data remains secure even if network boundaries are blurred in cloud-native environments, verifying trust through encrypted communication.
**Tags:** ankidote cloud-native security-model zero-trust

---

<!-- note:1772500381349 model:Basic+ -->
**Front:** What compliance standards benefit from pod-to-pod encryption?
**Back:** Standards like GDPR and HIPAA require data protection in transit, which pod-to-pod encryption achieves by securing internal communications and preventing unauthorized access.
**Tags:** ankidote compliance GDPR HIPAA

---

<!-- note:1772500459801 model:Basic+ -->
**Front:** What conditions must be met for a pod to be classified as Guaranteed QoS?
**Back:** A pod is Guaranteed if both CPU and memory requests and limits are set to identical values. This ensures resource guarantees and prevents eviction unless the node is unstable.
**Tags:** ankidote guaranteed kubernetes-qos

---

<!-- note:1772500459804 model:Basic+ -->
**Front:** What defines the Burstable QoS class in Kubernetes?
**Back:** Pods with resource requests lower than their limits belong to Burstable. They guarantee a minimum resource level but can burst beyond it if resources are available.
**Tags:** ankidote burstable kubernetes-qos

---

<!-- note:1772500459806 model:Basic+ -->
**Front:** What happens to Best-Effort QoS pods under resource pressure?
**Back:** Best-Effort pods receive no resource guarantees and are the first to be evicted when the cluster faces resource contention.
**Tags:** ankidote best-effort kubernetes-qos

---

<!-- note:1772500459810 model:Basic+ -->
**Front:** How does Kubernetes handle network QoS?
**Back:** Kubernetes does not directly manage network QoS. It relies on CNI plugins like Calico or Linux traffic control for bandwidth limiting and traffic shaping.
**Tags:** ankidote kubernetes-qos network-qos

---

<!-- note:1772500459813 model:Basic+ -->
**Front:** What governs storage QoS in Kubernetes?
**Back:** Storage QoS is managed via storage classes and underlying platform features. For example, AWS io1 disks with high IOPS can be configured for performance-critical workloads.
**Tags:** ankidote kubernetes-qos storage-qos

---

<!-- note:1772500459817 model:Basic+ -->
**Front:** What is the purpose of Kubernetes QoS classes?
**Back:** Kubernetes QoS classes (Guaranteed, Burstable, Best-Effort) ensure fair resource distribution in multi-tenant environments by prioritizing critical workloads and managing resource allocation efficiently.
**Tags:** ankidote kubernetes-qos summary

---

<!-- note:1772500459820 model:Basic+ -->
**Front:** What YAML configuration ensures a Guaranteed QoS class?
**Back:** Set identical CPU and memory requests and limits:
```yaml
resources:
  requests:
    memory: "500Mi"
    cpu: "500m"
  limits:
    memory: "500Mi"
    cpu: "500m"
```
**Tags:** ankidote guaranteed kubernetes-qos yaml

---

<!-- note:1772500459822 model:Basic+ -->
**Front:** What YAML configuration exemplifies a Burstable QoS class?
**Back:** Set requests lower than limits:
```yaml
resources:
  requests:
    memory: "200Mi"
    cpu: "200m"
  limits:
    memory: "16Gi"
    cpu: "1"
```
**Tags:** ankidote burstable kubernetes-qos yaml

---

<!-- note:1772500459825 model:Basic+ -->
**Front:** What YAML configuration represents a Best-Effort QoS class?
**Back:** Omit resource requests and limits entirely:
```yaml
resources: {}
```
**Tags:** ankidote best-effort kubernetes-qos yaml

---

<!-- note:1772500459829 model:Basic+ -->
**Front:** What YAML example demonstrates a Network QoS policy with Calico?
**Back:** Use a Calico NetworkPolicy with bandwidth limits:
```yaml
spec:
  ingress:
    - action: Allow
      protocol: TCP
      destination:
        ports: [80]
      limits:
        rate: 10Mbps
```
**Tags:** ankidote kubernetes-qos network-qos yaml

---

<!-- note:1772500459832 model:Basic+ -->
**Front:** What YAML example shows a Storage QoS configuration for high IOPS?
**Back:** Configure a StorageClass with high IOPS settings:
```yaml
parameters:
  type: io1
  iopsPerGB: "50"
  fsType: ext4
```
**Tags:** ankidote kubernetes-qos storage-qos yaml

---

<!-- note:1772500607201 model:Basic+ -->
**Front:** What security settings can be configured using Kubernetes security contexts?
**Back:** Security contexts in Kubernetes allow setting user IDs (runAsUser), Linux capabilities (capabilities.add), and other security parameters at both Pod and container levels.
**Tags:** ankidote kubernetes pod-security security-contexts

---

<!-- note:1772500607206 model:Basic+ -->
**Front:** How do Pod-level and container-level security contexts interact?
**Back:** Pod-level security context settings propagate to all containers in the Pod, but container-level security context overrides these settings for individual containers.
**Tags:** ankidote kubernetes pod-vs-container security-contexts

---

<!-- note:1772500607208 model:Basic+ -->
**Front:** What does the runAsUser parameter do in a security context?
**Back:** The runAsUser parameter specifies the user ID that the container process will run as, overriding the default root user.
**Tags:** ankidote kubernetes runasuser security-contexts

---

<!-- note:1772500607212 model:Basic+ -->
**Front:** What is the purpose of security contexts in Kubernetes?
**Back:** Security contexts in Kubernetes standardize user privileges across containerized environments and provide enhanced protection by restricting container capabilities and user permissions.
**Tags:** ankidote kubernetes security-contexts security-purposes

---

<!-- note:1772500646080 model:Basic+ -->
**Front:** What technology does Cilium leverage for efficient Kubernetes networking and security?
**Back:** Cilium leverages eBPF (Extended Berkeley Packet Filter) technology to run directly within the Linux kernel, enabling high-performance networking with minimal overhead.
**Tags:** ankidote cilium-architecture e-bpf kubernetes-networking

---

<!-- note:1772500646084 model:Basic+ -->
**Front:** What is Cil's core responsibility in Kubernetes networking?
**Back:** Cilium manages pod networking using the Container Network Interface (CNI), ensuring seamless communication among pods while enforcing strict security policies.
**Tags:** ankidote cilium-architecture cni pod-networking

---

<!-- note:1772500646089 model:Basic+ -->
**Front:** What feature allows Cilium to enforce secure pod-to-pod communication?
**Back:** Network Policies enable Cilium to secure pod-to-pod communications by preventing unauthorized access through policy enforcement.
**Tags:** ankidote cilium-features kubernetes-security network-policies

---

<!-- note:1772500646092 model:Basic+ -->
**Front:** What capability does Cilium provide for traffic management in Kubernetes?
**Back:** Cilium offers Services and Load Balancing to efficiently route traffic and distribute loads evenly among pods, ensuring high availability.
**Tags:** ankidote cilium-features load-balancing traffic-management

---

<!-- note:1772500646097 model:Basic+ -->
**Front:** Which Cilium feature helps prevent network congestion in Kubernetes clusters?
**Back:** Bandwidth Management regulates traffic consumption per pod to prevent network congestion and ensure fair resource allocation.
**Tags:** ankidote bandwidth-management cilium-features network-optimization

---

<!-- note:1772500646099 model:Basic+ -->
**Front:** What functionality enables real-time monitoring of network traffic in Cilium?
**Back:** Flow and Policy Logging provides real-time monitoring of network traffic and insights into policy enforcement across the Kubernetes cluster.
**Tags:** ankidote cilium-features network-logging policy-enforcement

---

<!-- note:1772500646101 model:Basic+ -->
**Front:** What does Cilium provide for security and operational visibility?
**Back:** Cilium offers Security and Operational Metrics to provide deep visibility into the cluster's security posture and overall performance.
**Tags:** ankidote cilium-features operational-insights security-metrics

---

<!-- note:1772500646105 model:Basic+ -->
**Front:** How does eBPF integration benefit Cilium's performance?
**Back:** eBPF integration allows Cilium to achieve high-performance networking with minimal overhead, making it ideal for efficient Kubernetes networking.
**Tags:** ankidote e-bpf kernel-integration performance-optimization

---

<!-- note:1772500707030 model:Basic+ -->
**Front:** What is node isolation using taints and tolerations?
**Back:** Node isolation using taints and tolerations prevents unauthorized pods from being scheduled on nodes reserved for specific tenants, ensuring workload separation and avoiding noisy neighbor issues.
**Tags:** ankidote multi-tenancy node-isolation taints-tolerations

---

<!-- note:1772500707035 model:Basic+ -->
**Front:** What command applies a taint to a node for tenant isolation?
**Back:** kubectl taint nodes nodeA customer=customerA:NoSchedule
**Tags:** ankidote node-isolation node-pools taints

---

<!-- note:1772500707038 model:Basic+ -->
**Front:** What YAML configuration enables pod scheduling on a tainted node?
**Back:** A pod's spec must include tolerations matching the node's taint, e.g.: tolerations: - key: "customer" operator: "Equal" value: "customerA" effect: "NoSchedule"
**Tags:** ankidote node-isolation pod-definitions tolerations

---

<!-- note:1772500707042 model:Basic+ -->
**Front:** What is the purpose of taints and tolerations in multi-tenancy?
**Back:** They enable dedicating nodes to specific tenants by restricting pod scheduling to nodes with matching tolerations, preventing workload interference.
**Tags:** ankidote multi-tenancy node-isolation taints-tolerations

---

<!-- note:1772500744777 model:Basic+ -->
**Front:** What must be created to use gVisor with Kubernetes?
**Back:** A RuntimeClass object with a valid handler field (e.g., `runsc` for gVisor).
**Tags:** ankidote gvisor-configuration kubernetes-runtime runtimeclass

---

<!-- note:1772500744780 model:Basic+ -->
**Front:** What is the required handler value for gVisor in a RuntimeClass?
**Back:** The handler must be set to `runsc` to use the gVisor runtime.
**Tags:** ankidote gvisor kubernetes-runtime runtimeclass-handler

---

<!-- note:1772500744783 model:Basic+ -->
**Front:** How do you specify a runtime for a Kubernetes pod?
**Back:** Add the `runtimeClassName` field to the pod's spec with the desired RuntimeClass name.
**Tags:** ankidote gvisor kubernetes-pod runtimeclass-usage

---

<!-- note:1772500744786 model:Basic+ -->
**Front:** What command creates a RuntimeClass from a YAML file?
**Back:** Use `kubectl create -f <filename>.yaml` to apply the RuntimeClass definition.
**Tags:** ankidote kubernetes-commands runtimeclass-creation yaml

---

<!-- note:1772500744788 model:Basic+ -->
**Front:** How to verify gVisor sandboxing is active?
**Back:** Run `pgrep -a nginx` on the node; no output indicates successful sandboxing.
**Tags:** ankidote gvisor-verification kubernetes-verification sandboxing

---

<!-- note:1772500744793 model:Basic+ -->
**Front:** What process confirms the gVisor runtime is running?
**Back:** Check for a `runsc` process on the node, indicating the runtime is active.
**Tags:** ankidote gvisor-process kubernetes-verification runtime-check

---

<!-- note:1772500744795 model:Basic+ -->
**Front:** What YAML fields define a RuntimeClass?
**Back:** The `metadata.name` (identifier) and `handler` (runtime name like `runsc`)
**Tags:** ankidote kubernetes runtimeclass-fields yaml-structure

---

<!-- note:1772500744797 model:Basic+ -->
**Front:** What is the purpose of a RuntimeClass in Kubernetes?
**Back:** To define and configure a specific container runtime (e.g., gVisor) for pods.
**Tags:** ankidote container-runtime kubernetes-runtime runtimeclass-purpose

---

<!-- note:1772500799054 model:Basic+ -->
**Front:** What is the primary function of Validating Admission Controllers?
**Back:** They check incoming requests and either allow or deny them based on predefined rules without modifying the request.
**Tags:** admission-controllers ankidote validating-controllers

---

<!-- note:1772500799059 model:Basic+ -->
**Front:** What is the primary function of Mutating Admission Controllers?
**Back:** They modify requests by adjusting the object before it is persisted to the cluster.
**Tags:** admission-controllers ankidote mutating-controllers

---

<!-- note:1772500799063 model:Basic+ -->
**Front:** Which controller ensures a namespace exists before allowing a request?
**Back:** The namespace existence (namespace lifecycle) validating admission controller.
**Tags:** ankidote namespace-controller validating-controllers

---

<!-- note:1772500799068 model:Basic+ -->
**Front:** What does the DefaultStorageClass controller do?
**Back:** It automatically adds a default storage class to PVCs that don't specify one.
**Tags:** ankidote mutating-controllers storage-class

---

<!-- note:1772500799070 model:Basic+ -->
**Front:** What is the processing order of admission controllers?
**Back:** Mutating controllers run before validating controllers to ensure modifications are validated.
**Tags:** admission-process ankidote controller-order

---

<!-- note:1772500799071 model:Basic+ -->
**Front:** What is an Admission Review JSON object used for?
**Back:** It contains details about the request sent to a webhook server, including the user, operation, and object involved.
**Tags:** admission-review ankidote webhooks

---

<!-- note:1772500799073 model:Basic+ -->
**Front:** What does a Validating Webhook Response include?
**Back:** It includes an 'allowed' field indicating whether the request is approved, along with optional status messages.
**Tags:** ankidote validating-webhook webhooks

---

<!-- note:1772500799075 model:Basic+ -->
**Front:** What does a Mutating Webhook Response include?
**Back:** It includes an 'allowed' field, a 'patch' field with JSON Patch instructions, and a 'patchType' indicating the format.
**Tags:** ankidote mutating-webhook webhooks

---

<!-- note:1772500799077 model:Basic+ -->
**Front:** What is the purpose of the 'caBundle' in webhook configurations?
**Back:** It provides the certificate authority bundle for secure TLS communication between the API server and the webhook server.
**Tags:** ankidote tls-security webhook-config

---

<!-- note:1772500799078 model:Basic+ -->
**Front:** How does the Python webhook example handle validation?
**Back:** The '/validate' route rejects requests where the object's name matches the user name, returning a status of false.
**Tags:** ankidote python-webhook webhook-examples

---

<!-- note:1772500799079 model:Basic+ -->
**Front:** How does the Python webhook example handle mutation?
**Back:** The '/mutate' route adds a label with the username using a JSON patch and returns the encoded patch.
**Tags:** ankidote python-webhook webhook-examples

---

<!-- note:1772500799080 model:Basic+ -->
**Front:** What is the structure of a ValidatingWebhookConfiguration?
**Back:** It includes a 'name' for the webhook, 'clientConfig' with service details and TLS settings, and 'rules' specifying which resources and operations trigger the webhook.
**Tags:** ankidote validating-webhook webhook-config

---

<!-- note:1772500799084 model:Basic+ -->
**Front:** What happens if any admission controller rejects a request?
**Back:** The entire operation fails, and an error message is returned to the user.
**Tags:** admission-process ankidote controller-rejection

---

<!-- note:1772500799086 model:Basic+ -->
**Front:** What is the role of the 'storageClassName' in PVC creation?
**Back:** The default storage class controller adds it automatically if not specified, ensuring the PVC uses the preconfigured default class.
**Tags:** ankidote mutating-controllers pvc-creation

---

<!-- note:1772500799089 model:Basic+ -->
**Front:** What is the difference between validating and mutating controllers (per the callout)?
**Back:** Validating controllers only verify requests against policies, while mutating controllers modify requests. Some controllers may perform both actions.
**Tags:** admission-controllers ankidote controller-differences

---

<!-- note:1772500837028 model:Basic+ -->
**Front:** What is the API version used in the Cilium network policy?
**Back:** The API version is "cilium.io/v2".
**Tags:** ankidote cilium-network-policy kubernetes-encryption

---

<!-- note:1772500837032 model:Basic+ -->
**Front:** What is the kind of the Cilium network policy?
**Back:** The kind is "CiliumNetworkPolicy".
**Tags:** ankidote cilium-network-policy kubernetes-encryption

---

<!-- note:1772500837036 model:Basic+ -->
**Front:** What is the name of the Cilium network policy?
**Back:** The policy is named "allow-encrypted-traffic".
**Tags:** ankidote cilium-network-policy kubernetes-encryption

---

<!-- note:1772500837038 model:Basic+ -->
**Front:** Which label selector targets pods for encryption?
**Back:** The endpoint selector matches pods with the label "app: myapp".
**Tags:** ankidote cilium-network-policy kubernetes-encryption

---

<!-- note:1772500837041 model:Basic+ -->
**Front:** What port and protocol does the egress rule allow?
**Back:** The egress rule allows TCP port 80.
**Tags:** ankidote cilium-network-policy kubernetes-encryption

---

<!-- note:1772500837045 model:Basic+ -->
**Front:** What command installs tcpdump in a Kubernetes pod?
**Back:** The command is "apt-get update && apt-get install -y tcpdump".
**Tags:** ankidote encryption-verification network-monitoring

---

<!-- note:1772500837047 model:Basic+ -->
**Front:** Which network interface does tcpdump monitor?
**Back:** Tcpdump monitors the "eth0" interface.
**Tags:** ankidote encryption-verification network-monitoring

---

<!-- note:1772500837051 model:Basic+ -->
**Front:** How do you verify encrypted traffic between pods?
**Back:** Use "tcpdump -i eth0 -nn" to capture and inspect packets.
**Tags:** ankidote encryption-verification network-monitoring

---

<!-- note:1772500837053 model:Basic+ -->
**Front:** What ensures encrypted traffic flows only to designated pods?
**Back:** The egress rules restrict traffic to pods with the same label "app: myapp".
**Tags:** ankidote cilium-network-policy kubernetes-encryption

---

<!-- note:1772500837055 model:Basic+ -->
**Front:** What is the purpose of the Cilium network policy?
**Back:** The policy enforces encryption for Pod-to-Pod communication in Kubernetes.
**Tags:** ankidote cilium-network-policy kubernetes-encryption

---

<!-- note:1772500874404 model:Basic+ -->
**Front:** What is gVisor and how does it enhance container isolation?
**Back:** gVisor is a Google-developed solution that creates an isolation layer between containers and the Linux kernel by intercepting system calls, reducing the attack surface and preventing direct kernel interaction.
**Tags:** ankidote container-isolation gvisor-overview

---

<!-- note:1772500874439 model:Basic+ -->
**Front:** What is the role of Sentry in gVisor's architecture?
**Back:** Sentry is an application-level kernel in gVisor that intercepts and processes system calls from containerized applications, providing a limited feature set to minimize vulnerabilities.
**Tags:** ankidote gvisor-architecture sentry-role

---

<!-- note:1772500874443 model:Basic+ -->
**Front:** What is Gofer's function in gVisor?
**Back:** Gofer acts as a file proxy in gVisor, handling file access requests from containers and acting as a middleman between containers and the Linux kernel to prevent direct system access.
**Tags:** ankidote gofer-role gvisor-architecture

---

<!-- note:1772500874447 model:Basic+ -->
**Front:** How does gVisor handle network operations?
**Back:** gVisor uses its own network stack to isolate containers from the host operating system's network code, preventing direct interaction with the kernel's networking components.
**Tags:** ankidote gvisor-architecture network-isolation

---

<!-- note:1772500874449 model:Basic+ -->
**Front:** What are the benefits of gVisor's container isolation approach?
**Back:** Each container has its own isolated gVisor kernel, reducing the attack surface. A compromised gVisor instance does not affect other containers due to strict isolation.
**Tags:** ankidote container-security gvisor-benefits

---

<!-- note:1772500874452 model:Basic+ -->
**Front:** What are the limitations of using gVisor?
**Back:** gVisor may introduce performance overhead due to system call interception, and not all applications are fully compatible with its architecture. Compatibility testing is required.
**Tags:** ankidote container-compatibility gvisor-limitations

---

<!-- note:1772500874455 model:Basic+ -->
**Front:** Why is the Linux kernel's attack surface a concern for containers?
**Back:** The Linux kernel supports thousands of operations via system calls, creating a large attack surface. Vulnerabilities like Dirty COW can compromise host systems through containers.
**Tags:** ankidote kernel-vulnerabilities linux-security

---

<!-- note:1772500874458 model:Basic+ -->
**Front:** What is the primary security advantage of gVisor over traditional containers?
**Back:** gVisor reduces the attack surface by intercepting system calls and isolating containers from the Linux kernel, preventing direct kernel access and mitigating exploits like Dirty COW.
**Tags:** ankidote container-isolation gvisor-security

---

<!-- note:1772500903178 model:Basic+ -->
**Front:** How does Kata Containers differ from alternatives like gVisor?
**Back:** Kata Containers uses a lightweight virtual machine (VM) for each container, while alternatives like gVisor use user-space sandboxing. This provides stronger isolation by assigning a dedicated kernel to each container.
**Tags:** ankidote container-sandboxing security-isolation

---

<!-- note:1772500903181 model:Basic+ -->
**Front:** What isolation strategy does Kata Containers use?
**Back:** Kata Containers isolates containers by assigning each one a dedicated kernel through lightweight VMs. This prevents system-wide failures as container issues are contained within individual VMs.
**Tags:** ankidote container-isolation kernel-isolation

---

<!-- note:1772500903183 model:Basic+ -->
**Front:** What performance trade-off does Kata Containers have?
**Back:** Kata Containers incurs a slight performance overhead due to additional memory and compute resources for each VM. However, this is balanced by enhanced security and isolation benefits.
**Tags:** ankidote performance-impact security-tradeoffs

---

<!-- note:1772500903186 model:Basic+ -->
**Front:** Which cloud providers support nested virtualization for Kata Containers?
**Back:** Google Cloud supports nested virtualization for Kata Containers, but it requires manual configuration and may not provide optimal performance. Most cloud providers do not support this feature.
**Tags:** ankidote cloud-computing nested-virtualization

---

<!-- note:1772500903188 model:Basic+ -->
**Front:** What environment is optimal for Kata Containers?
**Back:** Kata Containers performs best on dedicated physical or bare metal servers. This avoids the performance limitations of nested virtualization in cloud environments.
**Tags:** ankidote deployment-environment performance-optimization

---

<!-- note:1772500965455 model:Basic+ -->
**Front:** What is one method to enforce a read-only file system in Kubernetes pods?
**Back:** Set `readOnlyRootFilesystem: true` in the container's security context. Example:

```yaml
securityContext:
  readOnlyRootFilesystem: true
```
This prevents writes to the root filesystem but may cause errors if apps require write access (e.g., Nginx needing `/var/run` or `/var/cache/nginx`)
**Tags:** ankidote container-immutability kubernetes security

---

<!-- note:1772500965459 model:Basic+ -->
**Front:** How can you allow limited write access while maintaining immutability?
**Back:** Mount writable volumes (e.g., `emptyDir`) to specific directories requiring writes. Example:

```yaml
volumeMounts:
- name: cache-volume
  mountPath: /var/cache/nginx
- name: runtime-volume
  mountPath: /var/run
volumes:
- name: cache-volume
  emptyDir: {}
- name: runtime-volume
  emptyDir: {}
```
This keeps the root filesystem read-only while allowing writes to mounted volumes.
**Tags:** ankidote container-immutability kubernetes volumes

---

<!-- note:1772500965462 model:Basic+ -->
**Front:** What happens when a container runs in privileged mode with a read-only root filesystem?
**Back:** The container cannot modify the read-only root filesystem, even with privileged access. Example:

```bash
kubectl exec -ti nginx -- apt update
E: List directory /var/lib/apt/lists/partial is missing. - Acquire (30: Read-only file system)
```
Privileged mode does not bypass the read-only restriction.
**Tags:** ankidote container-immutability kubernetes security

---

<!-- note:1772500965465 model:Basic+ -->
**Front:** What is a best practice for ensuring container immutability?
**Back:** Enforce a read-only root filesystem using `readOnlyRootFilesystem: true` in the security context. This prevents in-place modifications to the container's filesystem.
**Tags:** ankidote best-practices container-immutability kubernetes

---

<!-- note:1772500965468 model:Basic+ -->
**Front:** How should write access be managed in immutable containers?
**Back:** Mount writable volumes (e.g., `emptyDir` or persistent volumes) only to directories requiring write access. This allows necessary writes while keeping the root filesystem read-only.
**Tags:** ankidote container-immutability kubernetes volumes

---

<!-- note:1772500965472 model:Basic+ -->
**Front:** Why should privileged mode be avoided in containers?
**Back:** Privileged containers can perform actions affecting the host system, compromising security. They bypass normal restrictions, including read-only filesystems, and should only be used when absolutely necessary.
**Tags:** ankidote container-immutability kubernetes security

---

<!-- note:1772500965476 model:Basic+ -->
**Front:** What is a recommended user privilege setting for containers?
**Back:** Run containers as non-root users to minimize risks. This prevents potential privilege escalation and reduces the attack surface in case of vulnerabilities.
**Tags:** ankidote container-immutability kubernetes security

---

<!-- note:1772500965480 model:Basic+ -->
**Front:** How can Pod Security Policies (PSPs) enforce immutability?
**Back:** Use PSPs to enforce policies like `readOnlyRootFilesystem: true`, `runAsNonRoot`, and disable `privileged`. Example:

```yaml
spec:
  readOnlyRootFilesystem: true
  runAsUser:
    rule: RunAsNonRoot
  privileged: false
```
This ensures containers are non-privileged, read-only, and run as non-root users.
**Tags:** ankidote container-immutability kubernetes policies

---

<!-- note:1772500965485 model:Basic+ -->
**Front:** Provide an example of a PodSecurityPolicy enforcing immutability.
**Back:** ```yaml
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: example
spec:
  privileged: false
  readOnlyRootFilesystem: true
  runAsUser:
    rule: RunAsNonRoot
  seLinux:
    rule: RunAsAny
  supplementalGroups:
    rule: RunAsAny
  fsGroup:
    rule: RunAsAny
```
This policy enforces non-privileged, read-only containers running as non-root users.
**Tags:** ankidote container-immutability kubernetes policies

---

<!-- note:1772507728267 model:Basic+ -->
**Front:** What is the purpose of network policies in Kubernetes for multi-tenancy?
**Back:** Network policies enforce multi-tenancy by isolating network traffic between different tenants and their applications, ensuring only authorized communications occur.
**Tags:** ankidote kubernetes-network-policies multi-tenancy network-security

---

<!-- note:1772507728270 model:Basic+ -->
**Front:** What is a pod selector in Kubernetes network policies?
**Back:** A pod selector identifies target pods based on their labels, specifying which pods the policy applies to.
**Tags:** ankidote kubernetes-network-policies network-rules pod-selectors

---

<!-- note:1772507728273 model:Basic+ -->
**Front:** What is a namespace selector in Kubernetes network policies?
**Back:** A namespace selector specifies the namespaces to which a network policy applies, controlling traffic across namespaces.
**Tags:** ankidote kubernetes-network-policies namespace-selectors network-rules

---

<!-- note:1772507728276 model:Basic+ -->
**Front:** What does the example YAML network policy allow?
**Back:** It allows pods labeled `app: backend` in the `tenant_a` namespace to receive TCP traffic on port 8080 from any pod in namespaces labeled `tenant_b`.
**Tags:** ankidote inter-tenant-traffic network-policy-example yaml-configuration

---

<!-- note:1772507728280 model:Basic+ -->
**Front:** What benefit does network policy isolation provide in multi-tenant clusters?
**Back:** It ensures granular control over network communications, preventing unauthorized access between tenants and isolating traffic for security.
**Tags:** ankidote multi-tenancy network-isolation security-best-practices

---

<!-- note:1772507728282 model:Basic+ -->
**Front:** What protocol and port does the example policy allow?
**Back:** The policy allows TCP traffic on port 8080.
**Tags:** ankidote network-policy-ports network-rules tcp-protocol

---

<!-- note:1772507767267 model:Basic+ -->
**Front:** What is data-plane isolation in Kubernetes?
**Back:** Data-plane isolation in Kubernetes is a strategy to enhance performance, security, and reliability in multi-tenant environments by segregating workloads to prevent resource contention and unauthorized access.
**Tags:** ankidote kubernetes-data-plane multi-tenant-security

---

<!-- note:1772507767272 model:Basic+ -->
**Front:** What is the purpose of network policies in data-plane isolation?
**Back:** Network policies control traffic flow between pods, ensuring only authorized communications occur and enforcing segmentation within the data plane.
**Tags:** ankidote kubernetes-data-plane network-policies

---

<!-- note:1772507767276 model:Basic+ -->
**Front:** How does storage isolation contribute to data-plane security?
**Back:** Storage isolation segments storage resources to prevent unauthorized access and ensure tenant-specific storage operations do not interfere with others.
**Tags:** ankidote kubernetes-data-plane storage-isolation

---

<!-- note:1772507767279 model:Basic+ -->
**Front:** What role do taints and tolerations play in data-plane isolation?
**Back:** Taints and tolerations prevent pods from being scheduled on inappropriate nodes by requiring pods to have matching tolerations to run on tainted nodes.
**Tags:** ankidote kubernetes-data-plane taints-tolerations

---

<!-- note:1772507787961 model:Basic+ -->
**Front:** What is the role of Admission Controllers in Kubernetes security?
**Back:** Admission Controllers enforce security policies by validating and modifying pod creation requests, working alongside Pod Security Policies to restrict privileged containers and ensure compliance with security baselines.
**Tags:** admission-controllers ankidote kubernetes-security pod-security-policies

---

<!-- note:1772507787966 model:Basic+ -->
**Front:** How does Open Policy Agent (OPA) enhance Kubernetes security?
**Back:** OPA enforces security policies by evaluating requests against customizablerego policies, allowing dynamic, centralized control over access decisions and resource modifications in Kubernetes clusters.
**Tags:** ankidote kubernetes-security open-policy-agent policy-enforcement

---

<!-- note:1772507787969 model:Basic+ -->
**Front:** What is the purpose of container sandboxing in Kubernetes?
**Back:** Container sandboxing technologies like Kata Containers and gVisor isolate workloads by running containers in lightweight VMs or user-space sandboxes, reducing attack surface and preventing privilege escalation.
**Tags:** ankidote container-sandboxing gvisor kata-containers security-isolation

---

<!-- note:1772507787973 model:Basic+ -->
**Front:** How does mTLS secure pod-to-pod communication in microservices?
**Back:** mTLS (mutual TLS) requires双向 certificate authentication between pods, ensuring only trusted services can communicate, thereby preventing eavesdropping and unauthorized access in microservice architectures.
**Tags:** ankidote microservice-security mTLS pod-communication

---

<!-- note:1772507787976 model:Basic+ -->
**Front:** What is a critical security best practice for Kubernetes configurations?
**Back:** Always test security configurations in a staging environment before deploying them in production to avoid unintended disruptions or vulnerabilities.
**Tags:** ankidote kubernetes security-best-practices testing-configurations

---

<!-- note:1772507817011 model:Basic+ -->
**Front:** What is a Kubernetes ResourceQuota?
**Back:** A ResourceQuota is a Kubernetes object that enforces limits on resource consumption (CPU, memory, storage) for pods and containers within a namespace, ensuring fair resource distribution in multi-tenant environments.
**Tags:** ankidote kubernetes multi-tenancy resource-quotas

---

<!-- note:1772507817014 model:Basic+ -->
**Front:** What is the purpose of resource quotas in Kubernetes?
**Back:** Resource quotas prevent resource exhaustion by limiting the total CPU, memory, and storage that can be consumed by pods and containers in a namespace, ensuring cluster stability and fair resource allocation.
**Tags:** ankidote cluster-management kubernetes resource-quotas

---

<!-- note:1772507817017 model:Basic+ -->
**Front:** What fields are defined in the ResourceQuota spec's hard section?
**Back:** The hard section defines hard limits for requests.cpu, requests.memory, limits.cpu, and limits.memory. Example: requests.cpu: "4", requests.memory: 16Gi, limits.cpu: "8", limits.memory: 32Gi.
**Tags:** ankidote kubernetes resource-quotas yaml-configuration

---

<!-- note:1772507817022 model:Basic+ -->
**Front:** How does a Pod adhere to resource quotas?
**Back:** A Pod must define resource requests and limits in its spec.resources section. For example, a Pod in namespace_a specifies requests.cpu: "250m" and limits.cpu: "500m" to stay within the namespace's quota constraints.
**Tags:** ankidote kubernetes pod-resources resource-quotas

---

<!-- note:1772507817025 model:Basic+ -->
**Front:** What is the difference between requests and limits in a ResourceQuota?
**Back:** Requests are the minimum resources a pod can use, while limits are the maximum. ResourceQuotas enforce both to ensure pods do not exceed allocated resources.
**Tags:** ankidote kubernetes resource-management resource-quotas

---

<!-- note:1772507817027 model:Basic+ -->
**Front:** Where is a ResourceQuota applied in Kubernetes?
**Back:** A ResourceQuota is applied to a specific namespace, as indicated by the metadata.namespace field. For example, the quota cpu-memory-quota is applied to namespace_a.
**Tags:** ankidote kubernetes namespace-management resource-quotas

---

<!-- note:1772507817031 model:Basic+ -->
**Front:** What are the resource limits for the example Pod in namespace_a?
**Back:** The Pod has requests.cpu: "250m", requests.memory: "64Mi", limits.cpu: "500m", and limits.memory: "128Mi" to comply with the namespace's quota constraints.
**Tags:** ankidote kubernetes pod-resources resource-quotas

---

<!-- note:1772508097810 model:Basic+ -->
**Front:** What is the purpose of using separate storage classes for tenant isolation?
**Back:** To manage persistent volumes (PVs) and claims (PVCs) with distinct performance requirements for different tenant types, ensuring optimal resource utilization and performance isolation.
**Tags:** ankidote data-plane-isolation kubernetes-storage storage-classes

---

<!-- note:1772508097814 model:Basic+ -->
**Front:** What parameter in the StorageClass YAML config enables high IOPS for AWS EBS?
**Back:** The 'type: io1' parameter specifies AWS io1 disks which support high IOPS. The 'iopsPerGB: "50"' parameter defines high IOPS per GB.
**Tags:** ankidote aws-ebs kubernetes-yaml storage-classes

---

<!-- note:1772508097818 model:Basic+ -->
**Front:** What namespace typically uses a high-performance storage class?
**Back:** Namespace A, dedicated to critical tenants requiring high-performance storage with enhanced IOPS.
**Tags:** ankidote data-plane-isolation namespace-management storage-classes

---

<!-- note:1772508097822 model:Basic+ -->
**Front:** What is the benefit of isolating storage classes for different workloads?
**Back:** Improved resource utilization and better performance isolation, ensuring critical applications receive necessary storage performance while standard workloads use optimized resources.
**Tags:** ankidote data-plane-isolation resource-management storage-optimization

---
