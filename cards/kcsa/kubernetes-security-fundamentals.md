# KCSA - Kubernetes and Cloud Native Security Associate — Kubernetes Security Fundamentals

> Deck: `KCSA - Kubernetes and Cloud Native Security Associate` · Group: `Kubernetes Security Fundamentals` · Notes: 99 · Models: Many

<!-- note:1772101854873 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What was the precursor to the Pod Security Standards (PSS) in Kubernetes?
**Options:** A. Pod Security Admission (PSA)<br>B. Kubernetes Security Policies (KSP)<br>C. PodSecurityPolicy (PSP)<br>D. Network Policies<br>E. Role-Based Access Control (RBAC)
**Answer:** C (3) – PodSecurityPolicy (PSP)
**Explanation:** PodSecurityPolicy (PSP) was the precursor to Pod Security Standards (PSS). PSP was deprecated and replaced by PSS and the PodSecurity admission controller to improve pod security management in Kubernetes clusters.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/pod-security-standards/" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#podsecuritypolicy" target="_blank">PodSecurityPolicy Deprecation</a>

---

<!-- note:1772101854874 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** How do you enable Pod Security Admission (PSA) in a Kubernetes cluster?
**Options:** A. Install the PSA plugin via kubectl<br>B. Add 'PodSecurity' to the '--enable-admission-plugins' flag in the API server<br>C. Apply a custom resource definition for PSA<br>D. Use a third-party tool to enforce PSA<br>E. Enable it in the kubelet configuration
**Answer:** B (2) – Add 'PodSecurity' to the '--enable-admission-plugins' flag in the API server
**Explanation:** To enable Pod Security Admission (PSA), you need to add 'PodSecurity' to the '--enable-admission-plugins' flag when starting the API server. This ensures that the PodSecurity admission controller is active and enforcing pod security standards.
**Sources:** <a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/" target="_blank">Kubernetes API Server Flags</a><br><a href="https://kubernetes.io/docs/concepts/security/pod-security-admission/" target="_blank">Pod Security Admission</a>

---

<!-- note:1772101854875 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Can you enforce more than one Pod Security Admission (PSA) policy level concurrently within a single namespace?
**Options:** A. Yes, by applying multiple labels<br>B. No, only one policy level per namespace<br>C. Yes, but only with custom configurations<br>D. Only if the namespace is partitioned<br>E. It depends on the Kubernetes version
**Answer:** B (2) – No, only one policy level per namespace
**Explanation:** PSA policies are applied at the namespace level. Only one PSA policy level (privileged, baseline, or restricted) can be enforced per namespace for each mode (enforce, audit, or warn). This ensures clear and consistent policy enforcement.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/pod-security-admission/" target="_blank">Kubernetes Documentation</a><br><a href="https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/authentication_and_authorization/understanding-and-managing-pod-security-admission" target="_blank">Red Hat Documentation</a>

---

<!-- note:1772101854876 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which of the following restrictions does the 'baseline' Pod Security Standard enforce? (Select all that apply)
**Options:** A. Disallows privileged containers<br>B. Allows hostPath volumes<br>C. Blocks host networking and ports<br>D. Requires running as non-root<br>E. Allows all Linux capabilities
**Answer:** A, C – Disallows privileged containers; blocks host networking and ports
**Explanation:** The 'baseline' Pod Security Standard disallows privileged containers and blocks host networking and ports. This ensures that pods are less vulnerable to security risks by limiting their capabilities.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/pod-security-standards/" target="_blank">Pod Security Standards</a><br><a href="https://kubernetes.io/docs/concepts/security/security-best-practices/" target="_blank">Kubernetes Security Best Practices</a>

---

<!-- note:1772101854877 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** In Kubernetes RBAC, what does a Role define?
**Options:** A. A set of users and their passwords<br>B. Permissions within a namespace<br>C. Network policies for pods<br>D. Global cluster-wide permissions<br>E. Resource quotas for a project
**Answer:** B (2) – Permissions within a namespace
**Explanation:** A Role in Kubernetes RBAC defines a set of permissions that are applicable within a specific namespace. This allows for fine-grained control over resources within that namespace.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes RBAC Documentation</a><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole" target="_blank">RBAC Roles and RoleBindings</a>

---

<!-- note:1772101854885 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which statement accurately describes how Kubernetes Network Policies control pod-to-pod communication within a cluster?
**Options:** A. By default, they block all traffic between pods.<br>B. They use iptables rules (via the CNI plugin) to control pod communication.<br>C. They are enforced by the kube-scheduler.<br>D. They manage access to the Kubernetes API.<br>E. They control storage access for pods.
**Answer:** B (2) – They use iptables rules (via the CNI plugin) to control pod communication.
**Explanation:** Kubernetes Network Policies define how groups of pods are allowed to communicate with each other and with other network endpoints. These policies are enforced by the Container Network Interface (CNI) plugin used in the cluster. Most CNI plugins implement network policies using iptables or similar mechanisms to control traffic at the network level. By default, if no Network Policy is applied, all pods can communicate freely. Network Policies do not block all traffic by default, nor are they enforced by the kube-scheduler. They do not manage API or storage access.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Network Policies (Official Documentation)</a><br><a href="https://www.mirantis.com/blog/kubernetes-security-best-practices/" target="_blank">Kubernetes Security Best Practices (Mirantis)</a>

---

<!-- note:1772101854888 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Does setting 'privileged: true' on a Kubernetes pod grant it access to Kubernetes Secrets?
**Options:** A. Yes, it grants full access to all Secrets in the cluster<br>B. No, it only elevates the pod's privileges on the host system but does not affect Secrets access<br>C. Yes, but only to Secrets within the same namespace<br>D. No, it explicitly prevents access to Secrets<br>E. Access depends solely on RBAC permissions, regardless of privileged mode
**Answer:** B (2) – No, it only elevates the pod's privileges on the host system but does not affect Secrets access
**Explanation:** Setting 'privileged: true' on a pod grants the container elevated privileges on the host system, such as access to devices and kernel capabilities, but it does not inherently grant access to Kubernetes Secrets. Access to Secrets is controlled by Kubernetes Role-Based Access Control (RBAC) policies and namespace scoping.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes Official Documentation - Security Context</a><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Official Documentation - Using RBAC Authorization</a>

---

<!-- note:1772101854892 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What are the potential impacts of enabling detailed auditing of request responses in a Kubernetes cluster?
**Options:** A. Improved cluster performance due to better monitoring<br>B. Reduced storage requirements for audit logs<br>C. Increased security with no performance or storage drawbacks<br>D. Performance overhead and increased storage usage due to detailed logs<br>E. Disabling of API server logging as a side effect
**Answer:** D (4) – Performance overhead and increased storage usage due to detailed logs
**Explanation:** Enabling detailed auditing of request responses in Kubernetes increases the volume and detail of audit logs generated, leading to higher storage consumption and potential performance overhead on the API server. While detailed auditing improves security visibility, it must be balanced against these resource impacts.
**Sources:** <a href="https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/" target="_blank">Kubernetes Official Documentation - Auditing</a>

---

<!-- note:1772101854902 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Why might a pod retain privileged access even after applying the 'restricted' Pod Security Standard (PSS) or Pod Security Admission (PSA) policy to its namespace? (Select all that apply)
**Options:** A. The Pod Security Standard does not apply retroactively to existing pods<br>B. The namespace labels required for policy enforcement are misconfigured or missing<br>C. The Kubernetes API server does not support Pod Security Standards<br>D. The pod specification explicitly overrides the policy<br>E. Privileged access is always allowed regardless of policy
**Answer:** A, B – the policy doesn't apply retroactively; missing or misconfigured namespace labels disable enforcement
**Explanation:** The 'restricted' Pod Security Standard or Pod Security Admission policy applies only to pods created or updated after the policy is enforced; existing pods are not automatically remediated. Enforcement also depends on correct namespace labeling (e.g., 'pod-security.kubernetes.io/enforce=restricted'). If these labels are missing or misconfigured, the policy will not be enforced on pods in that namespace.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/pod-security-admission/" target="_blank">Kubernetes Official Documentation - Pod Security Admission</a><br><a href="https://kubernetes.io/blog/2021/07/14/pod-security-standards-ga/" target="_blank">Kubernetes Blog - Pod Security Standards</a>

---

<!-- note:1772101854904 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which authentication mechanisms are commonly used by kubeadm during Kubernetes cluster bootstrapping? (Select all that apply)
**Options:** A. TLS certificates<br>B. Token-based authentication<br>C. OAuth tokens<br>D. Static passwords<br>E. Biometric authentication
**Answer:** A, B – TLS certificates and bootstrap tokens
**Explanation:** kubeadm primarily uses TLS certificates and token-based authentication mechanisms to secure communication and authenticate components during cluster bootstrapping. TLS certificates are used for API server and client authentication, while bootstrap tokens facilitate node joining.
**Sources:** <a href="https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/#tls-bootstrap" target="_blank">Kubernetes Official Documentation - kubeadm TLS Bootstrap</a><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/bootstrap-tokens/" target="_blank">Kubernetes Official Documentation - Bootstrap Tokens</a>

---

<!-- note:1772101854906 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Why is a ConfigMap not suitable for storing sensitive information such as secrets in Kubernetes?
**Options:** A. ConfigMaps cannot be mounted as volumes in pods<br>B. ConfigMaps do not support key-value pairs<br>C. Data stored in ConfigMaps is kept in plain text and not encrypted<br>D. ConfigMaps are deprecated in recent Kubernetes versions<br>E. ConfigMaps have strict size limitations that prevent storing secrets
**Answer:** C (3) – Data stored in ConfigMaps is kept in plain text and not encrypted
**Explanation:** ConfigMaps are designed to store non-sensitive configuration data as key-value pairs and store data in plain text within etcd. They do not provide encryption or access controls suitable for sensitive information. Secrets, on the other hand, are specifically designed to store sensitive data and can be encrypted at rest. ConfigMaps can be mounted as volumes and are not deprecated. While ConfigMaps have size limits, the primary reason they are unsuitable for secrets is the lack of security.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/configmap/" target="_blank">Kubernetes Official Documentation - ConfigMaps</a><br><a href="https://kubernetes.io/docs/concepts/configuration/secret/" target="_blank">Kubernetes Official Documentation - Secrets</a>

---

<!-- note:1772101854917 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What is the primary reason why a Kubernetes Network Policy might not be enforced as expected in a cluster?
**Options:** A. Network Policies are enabled by default in all clusters<br>B. The installed CNI plugin does not support Network Policies<br>C. The Network Policy YAML contains syntax errors<br>D. The Kubernetes API server is unavailable<br>E. Network Policies only apply to traffic from outside the cluster
**Answer:** B (2) – The installed CNI plugin does not support Network Policies
**Explanation:** Network Policies in Kubernetes rely on the underlying Container Network Interface (CNI) plugin to enforce rules. If the CNI plugin does not support Network Policies, then the policies will not be enforced regardless of their correctness. While syntax errors in the YAML or API server issues can cause problems, the primary reason Network Policies might not work is lack of CNI support. Also, Network Policies affect pod-to-pod traffic within the cluster, not just external traffic.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Official Documentation - Network Policies</a><br><a href="https://www.cni.dev/plugins/" target="_blank">CNI Plugins and Network Policy Support</a>

---

<!-- note:1772101854918 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** If a user is granted the 'cluster-admin' ClusterRole through a RoleBinding, what level of access will they have?
**Options:** A. Full administrative privileges limited to the namespace where the RoleBinding is applied<br>B. Full cluster-wide administrative privileges<br>C. Read-only access to all resources in the cluster<br>D. No permissions; ClusterRoles require ClusterRoleBindings to take effect<br>E. Access only to service accounts within the namespace
**Answer:** A (1) – Full administrative privileges limited to the namespace where the RoleBinding is applied
**Explanation:** When a ClusterRole, such as 'cluster-admin', is assigned using a RoleBinding, it grants full administrative privileges but only within the namespace where the RoleBinding is applied. This is because RoleBindings are namespace-scoped, meaning they cannot grant cluster-wide permissions even if the associated role is a ClusterRole. To grant cluster-wide permissions, a ClusterRoleBinding must be used. Incorrect options: (1) Full cluster-wide privileges require a ClusterRoleBinding, not a RoleBinding. (2) Read-only access is not tied to this scenario. (3) The statement about 'no permissions' is incorrect because RoleBindings do apply within their namespace. (4) Access to service accounts is not exclusive in this context.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Official Documentation - RBAC</a><br><a href="https://www.strongdm.com/blog/kubernetes-rbac-role-based-access-control" target="_blank">StrongDM Blog - Kubernetes RBAC Explained</a>

---

<!-- note:1772101854921 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** How can you enable Pod Security Admission (PSA) in a Kubernetes cluster to enforce pod security standards?
**Options:** A. By applying security labels directly to pods<br>B. By configuring the API server to enable the PodSecurity admission controller<br>C. By setting environment variables on cluster nodes<br>D. By deploying a third-party admission webhook<br>E. By updating kubelet configurations on nodes
**Answer:** B (2) – By configuring the API server to enable the PodSecurity admission controller
**Explanation:** Pod Security Admission (PSA) is enabled by configuring the Kubernetes API server to include the 'PodSecurity' admission controller in its '--enable-admission-plugins' flag. This admission controller enforces pod security standards based on namespace labels. Applying labels to pods or setting environment variables on nodes does not enable PSA. While third-party admission webhooks can enforce policies, PSA is a built-in admission controller. Kubelet configurations do not control PSA.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/pod-security-admission/" target="_blank">Kubernetes Official Documentation - Pod Security Admission</a><br><a href="https://github.com/kubernetes/enhancements/tree/master/keps/sig-auth/2571-pod-security-admission" target="_blank">Kubernetes Enhancement Proposal (KEP) - Pod Security Admission</a>

---

<!-- note:1772101854922 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** In Kubernetes Role-Based Access Control (RBAC), what is the purpose of a RoleBinding?
**Options:** A. Defines permissions within a namespace<br>B. Associates a Role with users, groups, or service accounts within a namespace<br>C. Creates a new role with cluster-wide permissions<br>D. Manages network policies for a namespace<br>E. Sets resource quotas for a project
**Answer:** B (2) – Associates a Role with users, groups, or service accounts within a namespace
**Explanation:** A RoleBinding in Kubernetes RBAC binds a Role to one or more subjects (users, groups, or service accounts) within a specific namespace, granting them the permissions defined in that Role. Roles themselves define permissions, but RoleBindings associate those permissions with subjects. ClusterRoles and ClusterRoleBindings are used for cluster-wide permissions. Network policies and resource quotas are managed by different Kubernetes objects unrelated to RoleBindings.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Official Documentation - Using RBAC Authorization</a><br><a href="https://kubernetes.io/docs/concepts/security/authorization/#role-based-access-control-rbac" target="_blank">Kubernetes RBAC Concepts</a>

---

<!-- note:1772101854928 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What is the primary function of Resource Quotas in a Kubernetes namespace?
**Options:** A. Limit the number of namespaces in the cluster<br>B. Restrict access to the Kubernetes API server<br>C. Control the amount of resources consumed within a namespace<br>D. Schedule pods to specific nodes<br>E. Enforce network policies
**Answer:** C (3) – Control the amount of resources consumed within a namespace
**Explanation:** Resource Quotas in Kubernetes are used to limit the total amount of compute resources (such as CPU, memory, and object counts) that can be consumed within a namespace. This helps prevent a single namespace from exhausting cluster resources. Resource Quotas do not limit namespaces themselves, control API server access, schedule pods, or enforce network policies, which are handled by other Kubernetes components.
**Sources:** <a href="https://kubernetes.io/docs/concepts/policy/resource-quotas/" target="_blank">Kubernetes Official Documentation - Resource Quotas</a><br><a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/" target="_blank">Kubernetes Resource Management</a>

---

<!-- note:1772101854930 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which Kubernetes object is specifically designed to store sensitive information such as passwords, tokens, or keys?
**Options:** A. ConfigMap<br>B. Secret<br>C. Volume<br>D. Pod Annotation<br>E. Deployment
**Answer:** B (2) – Secret
**Explanation:** Kubernetes Secrets are intended to store sensitive data like passwords, OAuth tokens, and SSH keys securely. Unlike ConfigMaps, which store non-sensitive configuration data, Secrets provide mechanisms to protect this sensitive information, including base64 encoding and integration with encryption at rest. Volumes, Pod Annotations, and Deployments are not designed for securely storing sensitive data.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/secret/" target="_blank">Kubernetes Official Documentation - Secrets</a><br><a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#use-secrets-to-store-sensitive-information" target="_blank">Kubernetes Best Practices - Managing Secrets</a>

---

<!-- note:1772101854932 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which of the following are common CNI plugins that support Network Policies? (Select all that apply)
**Options:** A. Flannel<br>B. Calico<br>C. Weave Net<br>D. AWS VPC CNI<br>E. Cilium
**Answer:** B, C, D, E – Calico, Weave Net, AWS VPC CNI, and Cilium support NetworkPolicies (Flannel does not by default)
**Explanation:** Calico, Weave Net, Cilium, and AWS VPC CNI are CNI plugins that support Network Policies. AWS VPC CNI supports network policies but requires them to be enabled and does not support them for Fargate or Windows containers. Flannel does not support Network Policies by default.
**Sources:** <a href="https://aws.amazon.com/about-aws/whats-new/2023/08/amazon-vpc-cni-kubernetes-networkpolicy-enforcement/" target="_blank">AWS Announcement on VPC CNI Network Policy Support</a><br><a href="https://docs.aws.amazon.com/eks/latest/userguide/cni-network-policy-configure.html#enable-network-policy-parameter" target="_blank">AWS EKS Documentation on Network Policy Configuration</a><br><a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Documentation on Network Policies</a>

---

<!-- note:1772101854935 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which Kubernetes feature enables encryption of Secrets data at rest within the cluster?
**Options:** A. Enabling TLS on the API server<br>B. Using the etcd encryption provider for at-rest encryption<br>C. Storing Secrets in ConfigMaps<br>D. Encrypting data at the application layer<br>E. Using third-party encryption tools outside Kubernetes
**Answer:** B (2) – Using the etcd encryption provider for at-rest encryption
**Explanation:** Kubernetes supports encryption of Secrets at rest by enabling the etcd encryption provider, which encrypts Secret data stored in etcd, the cluster's backing store. This protects sensitive data from unauthorized access if etcd storage is compromised. TLS on the API server secures data in transit, not at rest. ConfigMaps do not provide encryption and are not intended for sensitive data. Application-layer encryption and third-party tools can add security but are not native Kubernetes features for Secrets encryption.
**Sources:** <a href="https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/" target="_blank">Kubernetes Official Documentation - Encrypting Secret Data at Rest</a><br><a href="https://github.com/cncf/sig-security/blob/main/security-whitepaper.md#kubernetes-secrets" target="_blank">CNCF Security Whitepaper - Kubernetes Secrets Management</a>

---

<!-- note:1772101854936 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What is the default behavior of Kubernetes network traffic when no Network Policies are applied to a namespace?
**Options:** A. All ingress and egress traffic is denied<br>B. All ingress traffic is denied; egress traffic is allowed<br>C. All ingress and egress traffic is allowed<br>D. All egress traffic is denied; ingress traffic is allowed<br>E. Traffic is allowed only within the namespace
**Answer:** C (3) – All ingress and egress traffic is allowed
**Explanation:** By default, Kubernetes allows all ingress and egress traffic to pods if no Network Policies are applied. Network Policies are opt-in and must be explicitly created to restrict traffic. Without any policies, pods can send and receive traffic unrestricted. The other options describe behaviors that occur only when specific Network Policies are configured.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Official Documentation - Network Policies</a><br><a href="https://github.com/cncf/sig-security/blob/main/security-best-practices.md#network-policies" target="_blank">CNCF Kubernetes Security Best Practices</a>

---

<!-- note:1772101854937 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** How do Kubernetes Secrets provide improved security compared to ConfigMaps?
**Options:** A. Secrets are encrypted by default in etcd<br>B. Secrets are stored in a separate database from ConfigMaps<br>C. Secrets are base64-encoded and can be encrypted at rest, whereas ConfigMaps are stored in plain text<br>D. Secrets provide built-in versioning<br>E. Secrets can only be accessed by cluster administrators
**Answer:** C (3) – Secrets are base64-encoded and can be encrypted at rest, whereas ConfigMaps are stored in plain text
**Explanation:** Kubernetes Secrets are base64-encoded and can be configured to be encrypted at rest in etcd, providing better protection for sensitive data than ConfigMaps, which are stored as plain text in etcd. Secrets are not encrypted by default unless encryption at rest is enabled. They do not provide built-in versioning, and access controls depend on RBAC policies rather than restricting access solely to cluster admins.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/secret/" target="_blank">Kubernetes Official Documentation - Secrets</a><br><a href="https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/" target="_blank">Kubernetes Official Documentation - Encrypting Secret Data at Rest</a>

---

<!-- note:1772101854938 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which Kubernetes component is responsible for enforcing Pod Security Standards through admission control?
**Options:** A. kube-scheduler<br>B. kube-apiserver with the PodSecurity admission plugin<br>C. kube-controller-manager<br>D. kubelet<br>E. etcd
**Answer:** B (2) – kube-apiserver with the PodSecurity admission plugin
**Explanation:** The kube-apiserver enforces Pod Security Standards by using the PodSecurity admission plugin, which validates and enforces security policies on pods during creation or update. The kube-scheduler schedules pods to nodes, kube-controller-manager manages controllers, kubelet runs on nodes to manage pods, and etcd is the cluster data store; none of these enforce Pod Security Standards directly.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/pod-security-admission/" target="_blank">Kubernetes Official Documentation - Pod Security Admission</a><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/" target="_blank">Kubernetes Official Documentation - Admission Controllers</a>

---

<!-- note:1772101854939 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What is the purpose of the '--allow-privileged' flag in the Kubernetes API server configuration?
**Options:** A. Allows pods to run privileged containers with elevated permissions<br>B. Enables unauthenticated access to the API server<br>C. Grants cluster-admin rights to all users<br>D. Disables security contexts on pods<br>E. Controls enforcement of network policies
**Answer:** A (1) – Allows pods to run privileged containers with elevated permissions
**Explanation:** The '--allow-privileged' flag on the Kubernetes API server enables or disables the ability to create privileged containers, which have elevated permissions on the host and can perform sensitive operations. This flag does not affect authentication, user permissions, security contexts broadly, or network policy enforcement. Running privileged containers increases security risks and should be carefully controlled.
**Sources:** <a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/" target="_blank">Kubernetes Official Documentation - API Server Flags</a><br><a href="https://kubernetes.io/docs/concepts/policy/pod-security-policy/#privileged" target="_blank">Kubernetes Official Documentation - Privileged Containers</a>

---

<!-- note:1772101854942 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What is a significant security risk associated with not restricting egress traffic in a Kubernetes cluster?
**Options:** A. It complicates the debugging process for network-related issues.<br>B. It leads to reduced latency in network communications within the cluster.<br>C. It creates a potential pathway for data exfiltration from compromised pods to external, unauthorized destinations.<br>D. It enhances and simplifies pod-to-pod communication within the cluster.<br>E. It simplifies network configuration, reducing the complexity of network policies.
**Answer:** C (3) – It creates a potential pathway for data exfiltration from compromised pods to external, unauthorized destinations.
**Explanation:** Failing to restrict egress traffic in Kubernetes can expose the cluster to significant security risks, most notably data exfiltration. Without proper egress controls, a compromised pod can freely communicate with external servers, potentially leaking sensitive data to attackers. While unrestricted egress might simplify initial network configurations, the security implications far outweigh any convenience gained. Restricting egress traffic is a critical security measure to limit the attack surface and prevent unauthorized communication from within the cluster.
**Sources:** <a href="https://www.tigera.io/blog/prevent-data-exfiltration-in-kubernetes-the-critical-role-of-egress-access-controls/" target="_blank">Tigera: Prevent Data Exfiltration in Kubernetes</a><br><a href="https://www.redhat.com/en/blog/guide-to-kubernetes-egress-network-policies" target="_blank">Red Hat: Guide to Kubernetes Egress Network Policies</a>

---

<!-- note:1772101854943 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** How can you verify that Pod Security Admission (PSA) is actively enforcing security policies within a specific Kubernetes namespace?
**Options:** A. Check the API server logs for PSA-related entries<br>B. Attempt to create a pod that violates the PSA policy and observe the outcome<br>C. Inspect the kubelet configuration on the nodes<br>D. Review the scheduler's event logs for pod scheduling issues<br>E. Use the command 'kubectl get psa' to check enforcement status
**Answer:** B (2) – Attempt to create a pod that violates the PSA policy and observe the outcome
**Explanation:** The most direct way to verify that Pod Security Admission is enforcing policies is to try creating a pod that violates the defined PSA policy in the target namespace. If the pod creation is denied, it confirms that PSA is active and enforcing the policies. Checking API server logs or scheduler events may provide indirect clues but are less reliable for verification. The kubelet configuration does not control PSA enforcement, and 'kubectl get psa' is not a valid command for checking PSA status.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/pod-security-admission/" target="_blank">Kubernetes Official Documentation - Pod Security Admission</a><br><a href="https://kubernetes.io/blog/2021/04/06/pod-security-admission-beta/" target="_blank">Kubernetes Blog - Pod Security Admission Controller</a>

---

<!-- note:1772101854944 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What is the effect of applying a Kubernetes NetworkPolicy that does not select any pods in the cluster?
**Options:** A. It has no effect on network traffic within the cluster<br>B. It denies all network traffic to and from all pods<br>C. It allows all network traffic by default<br>D. It causes an error in the network plugin<br>E. It only affects newly created pods after the policy is applied
**Answer:** A (1) – It has no effect on network traffic within the cluster
**Explanation:** A NetworkPolicy that does not select any pods effectively applies to no pods and therefore has no impact on network traffic. It neither denies nor allows traffic beyond the cluster's default behavior. It does not cause errors in the network plugin, nor does it selectively affect only new pods. NetworkPolicies only affect pods that they select.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Official Documentation - Network Policies</a><br><a href="https://www.cncf.io/blog/2020/07/15/understanding-kubernetes-network-policies/" target="_blank">CNCF - Kubernetes Network Policy Explained</a>

---

<!-- note:1772101854950 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** How can you restrict a Kubernetes user to create resources only within a specific namespace?
**Options:** A. Assign the user the cluster-admin role<br>B. Create a Role and RoleBinding scoped to that namespace for the user<br>C. Modify the kube-apiserver configuration to limit user access<br>D. Create a NetworkPolicy that restricts user actions<br>E. Set a resource quota on the namespace to limit resource creation
**Answer:** B (2) – Create a Role and RoleBinding scoped to that namespace for the user
**Explanation:** To restrict a user to create resources only within a specific namespace, you create a Role that defines the allowed permissions within that namespace and bind it to the user via a RoleBinding. Assigning cluster-admin grants full cluster-wide permissions, which is too broad. Modifying kube-apiserver configuration is not practical for per-user namespace restrictions. NetworkPolicies control pod network traffic, not user permissions. Resource quotas limit resource consumption but do not restrict user actions.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Official Documentation - Using RBAC Authorization</a><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole" target="_blank">Kubernetes Official Documentation - Roles and RoleBindings</a>

---

<!-- note:1772101854954 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What measures can you take to prevent a container from running as the root user in Kubernetes?
**Options:** A. Set 'runAsUser: 0' in the security context<br>B. Use a Pod Security Admission to enforce non-root user requirements<br>C. It is not possible to prevent this<br>D. Modify the container image to exclude root user privileges<br>E. Set 'allowPrivilegeEscalation: true' in the security context
**Answer:** B (2) – Use a Pod Security Admission to enforce non-root user requirements
**Explanation:** To enhance security, you can use Pod Security Admission to enforce that containers run as non-root users. This prevents potential privilege escalation attacks. Option 1 ('runAsUser: 0') explicitly allows running as root, which is insecure. Option 3 is incorrect because Kubernetes provides mechanisms to enforce non-root users. Option 4 may reduce root privileges but does not enforce non-root execution. Option 5 ('allowPrivilegeEscalation: true') enables privilege escalation, which contradicts the goal of preventing root access.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/pod-security-standards/" target="_blank">Kubernetes Official Documentation - Pod Security Standards</a><br><a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes Official Documentation - Security Contexts</a>

---

<!-- note:1772101854955 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What is the primary purpose of Role-Based Access Control (RBAC) in Kubernetes?
**Options:** A. To manage network policies for pods<br>B. To control user and process access to Kubernetes resources<br>C. To schedule pods efficiently across nodes<br>D. To monitor cluster performance metrics<br>E. To provide logging and audit capabilities
**Answer:** B (2) – To control user and process access to Kubernetes resources
**Explanation:** RBAC in Kubernetes is designed to control and manage access permissions for users and processes to Kubernetes resources, ensuring that only authorized entities can perform specific actions. It does not manage network policies, scheduling, monitoring, or logging directly, although these areas may have their own mechanisms.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Official Documentation - RBAC Authorization</a><br><a href="https://www.redhat.com/sysadmin/kubernetes-rbac" target="_blank">Red Hat - Introduction to Kubernetes RBAC</a>

---

<!-- note:1772101854956 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which Kubernetes object is used to define a set of network access rules that control traffic to and from pods?
**Options:** A. Service<br>B. Deployment<br>C. Ingress<br>D. NetworkPolicy<br>E. ConfigMap
**Answer:** D (4) – NetworkPolicy
**Explanation:** NetworkPolicy objects in Kubernetes are used to specify rules that control the ingress and egress traffic to and from pods. Services manage access at a different layer, Ingress manages external access, Deployments manage pod lifecycle, and ConfigMaps store configuration data, none of which control pod-level network access rules.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Official Documentation - Network Policies</a><br><a href="https://www.cncf.io/blog/2020/07/15/understanding-kubernetes-network-policies/" target="_blank">CNCF - Kubernetes Network Policy Explained</a>

---

<!-- note:1772101854968 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What is the primary function of Kubernetes labels in organizing resources?
**Options:** A. To provide human-readable names for resources<br>B. To organize and select groups of objects<br>C. To store configuration data<br>D. To set permissions on resources<br>E. To define network policies
**Answer:** B (2) – To organize and select groups of objects
**Explanation:** Kubernetes labels are key-value pairs attached to objects, such as pods or services, to facilitate identification and selection. They enable users to organize and filter resources based on specific criteria, making it easier to manage complex environments.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors" target="_blank">Kubernetes Labels and Selectors</a>

---

<!-- note:1772101854972 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** How can you create a ConfigMap from a file in Kubernetes?
**Options:** A. kubectl create configmap my-config --file=config.yaml<br>B. kubectl apply configmap my-config --from-file=config.yaml<br>C. kubectl create configmap my-config --from-file=config.yaml<br>D. kubectl generate configmap my-config config.yaml<br>E. kubectl configmap my-config --import=config.yaml
**Answer:** C (3) – kubectl create configmap my-config --from-file=config.yaml
**Explanation:** To create a ConfigMap from a file, you use the command `kubectl create configmap my-config --from-file=config.yaml`. This command allows you to import configuration data from a file into a ConfigMap, which can then be used by applications running in Kubernetes.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/configmap/" target="_blank">Kubernetes ConfigMaps Documentation</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#-em-create-em-configmap" target="_blank">Kubernetes CLI Reference</a>

---

<!-- note:1772101855005 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** How do you create a Secret from literal values in Kubernetes?
**Options:** A. kubectl create secret generic my-secret --from-literal=key1=value1<br>B. kubectl create secret generic my-secret key1=value1<br>C. kubectl create secret my-secret --literal key1=value1<br>D. kubectl create secret tls my-secret --key1 value1<br>E. kubectl secret create my-secret key1=value1
**Answer:** A (1) – kubectl create secret generic my-secret --from-literal=key1=value1
**Explanation:** To create a Secret from literal values, you use the command `kubectl create secret generic my-secret --from-literal=key1=value1`. This command allows you to define key-value pairs directly in the command line, which are then stored as a Secret in Kubernetes.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/secret/" target="_blank">Kubernetes Secrets Documentation</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#-em-create-em-secret" target="_blank">Kubernetes CLI Reference</a>

---

<!-- note:1772101855006 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What is the role of the 'cluster-admin' ClusterRole?
**Options:** A. Read-only access to cluster resources<br>B. Admin access limited to one namespace<br>C. Full control over all resources in the cluster<br>D. Access to manage nodes but not pods<br>E. Limited to managing storage resources
**Answer:** C (3) – Full control over all resources in the cluster
**Explanation:** The 'cluster-admin' ClusterRole grants full cluster-wide administrative permissions. When bound via a ClusterRoleBinding, it provides full control over all resources in the cluster. When bound via a RoleBinding, its permissions are limited to the namespace specified in the binding.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Documentation - Role-Based Access Control (RBAC)</a><br><a href="https://kubernetes.io/docs/concepts/security/controlling-access/" target="_blank">Kubernetes Documentation - Controlling Access to the Kubernetes API</a>

---

<!-- note:1772101855007 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which command is used to apply a label to a pod in Kubernetes?
**Options:** A. kubectl label pods <pod-name> key=value<br>B. kubectl annotate pods <pod-name> key=value<br>C. kubectl tag pods <pod-name> key=value<br>D. kubectl set label pods <pod-name> key=value<br>E. kubectl edit pods <pod-name> --label key=value
**Answer:** A (1) – kubectl label pods <pod-name> key=value
**Explanation:** The command `kubectl label pods <pod-name> key=value` is used to apply a label to a pod. This command updates the metadata of the pod with the specified key-value pair, allowing for easier management and filtering of resources.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/" target="_blank">Kubernetes Labels Documentation</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#-em-label-em" target="_blank">Kubernetes CLI Reference</a>

---

<!-- note:1772101855018 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What is the purpose of the 'allowPrivilegeEscalation' field in a Kubernetes pod's security context?
**Options:** A. Allows the container to run as root<br>B. Controls whether a process can gain more privileges than its parent process<br>C. Enables privileged mode for the container<br>D. Allows mounting of host directories<br>E. Disables all capabilities for the container
**Answer:** B (2) – Controls whether a process can gain more privileges than its parent process
**Explanation:** The 'allowPrivilegeEscalation' field in a Kubernetes pod's security context controls whether a process can gain more privileges than its parent process. This setting is crucial for security as it prevents potential privilege escalation attacks by limiting the capabilities of processes within a container.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes Security Context Documentation</a><br><a href="https://kubernetes.io/docs/concepts/security/pod-security-standards/" target="_blank">Kubernetes Pod Security Standards</a>

---

<!-- note:1772101855019 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which Kubernetes object specifically controls inbound/outbound network traffic between Pods at the IP address and port level?
**Options:** A. NetworkPolicy<br>B. Ingress<br>C. Service<br>D. Endpoint<br>E. FirewallRule
**Answer:** A (1) – NetworkPolicy
**Explanation:** NetworkPolicy objects define granular rules for Pod-to-Pod communication, including allowed ingress/egress traffic. While Services enable network access to Pods and Ingress manages external HTTP(S) routing, NetworkPolicy provides critical microsegmentation capabilities for zero-trust security architectures.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Network Policies Documentation</a><br><a href="https://www.cisecurity.org/benchmark/kubernetes/" target="_blank">CIS Kubernetes Benchmark v1.8</a>

---

<!-- note:1772101855021 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What is the correct kubectl command syntax to create a Role named 'pod-reader' with get/watch/list permissions on Pods in the current namespace?
**Options:** A. kubectl apply role<br>B. kubectl create role pod-reader --verb=get,list,watch --resource=pods<br>C. kubectl generate role<br>D. kubectl new role<br>E. kubectl init role
**Answer:** B (2) – kubectl create role pod-reader --verb=get,list,watch --resource=pods
**Explanation:** The 'kubectl create role' command with proper flags creates RBAC Roles. The full syntax requires specifying verbs (--verb) and resources (--resource). This command creates non-namespaced Roles; for cluster-wide permissions, use 'kubectl create clusterrole' instead.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes RBAC Documentation</a><br><a href="https://www.manning.com/books/kubernetes-in-action" target="_blank">Kubernetes in Action (Manning Publications)</a>

---

<!-- note:1772101855022 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which RBAC component links a ClusterRole to all authenticated users across the entire Kubernetes cluster?
**Options:** A. ClusterRoleBinding<br>B. RoleBinding<br>C. ClusterRole<br>D. ServiceAccount<br>E. GroupBinding
**Answer:** A (1) – ClusterRoleBinding
**Explanation:** ClusterRoleBinding associates ClusterRoles with subjects (users/groups/serviceaccounts) cluster-wide. This is critical for security as it affects all namespaces. Best practice recommends using RoleBinding with namespaced Roles for least-privilege access.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/rbac-good-practices/" target="_blank">Kubernetes RBAC Good Practices</a><br><a href="https://www.cisecurity.org/benchmark/kubernetes/" target="_blank">CIS Kubernetes Benchmark v1.8</a>

---

<!-- note:1772101855023 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What is the correct command to base64-encode the string 'admin' for Kubernetes Secret creation, including proper newline handling?
**Options:** A. echo -n 'admin' | base64<br>B. echo 'admin' | base64<br>C. echo 'admin' | base64encode<br>D. base64 'admin'<br>E. encode --base64 'admin'
**Answer:** A (1) – echo -n 'admin' | base64
**Explanation:** The '-n' flag prevents adding a trailing newline character, which is critical for accurate encoding. Kubernetes Secrets require precise base64 encoding without unexpected characters. The resulting output can be used in Secret manifests' data field.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/secret/" target="_blank">Kubernetes Secrets Documentation</a><br><a href="https://man7.org/linux/man-pages/man1/base64.1.html" target="_blank">Linux man-pages project</a>

---

<!-- note:1772101855025 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which Kubernetes Secret type is required when configuring TLS termination for an Ingress resource?
**Options:** A. Opaque<br>B. kubernetes.io/tls<br>C. Docker Registry<br>D. Basic Auth<br>E. SSH Key
**Answer:** B (2) – kubernetes.io/tls
**Explanation:** For configuring TLS termination in an Ingress resource, a Secret of type 'kubernetes.io/tls' is required. This type of Secret must contain 'tls.crt' and 'tls.key' entries with PEM-encoded certificates.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/ingress/#tls" target="_blank">Kubernetes Ingress TLS Documentation</a><br><a href="https://kubernetes.io/docs/concepts/configuration/secret/#secret-types" target="_blank">Kubernetes Secret Types Reference</a>

---

<!-- note:1772101855026 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which kubectl command correctly creates a TLS secret named 'tls-secret' using the certificate file 'tls.crt' and the key file 'tls.key'?
**Options:** A. kubectl create secret generic tls-secret --from-file=tls.crt --from-file=tls.key<br>B. kubectl create secret tls tls-secret --cert=tls.crt --key=tls.key<br>C. kubectl create secret docker-registry tls-secret --docker-server=tls.crt --docker-username=tls.key<br>D. kubectl create tls-secret tls-secret --cert=tls.crt --key=tls.key<br>E. kubectl create secret tls-secret --type=tls --cert=tls.crt --key=tls.key
**Answer:** B (2) – kubectl create secret tls tls-secret --cert=tls.crt --key=tls.key
**Explanation:** The correct command to create a TLS secret in Kubernetes is 'kubectl create secret tls' followed by the secret name and the paths to the certificate and key files using the --cert and --key flags.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/secret/#tls-secrets" target="_blank">Kubernetes Official Documentation - Secrets</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#create-secret" target="_blank">Kubernetes CLI Reference - kubectl create secret</a>

---

<!-- note:1772101855028 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** In a Kubernetes Pod specification, which field is used to define Linux capabilities for an individual container?
**Options:** A. securityContext.capabilities<br>B. spec.capabilities<br>C. container.securityContext.capabilities<br>D. podSecurityContext.capabilities<br>E. linuxOptions.capabilities
**Answer:** A (1) – securityContext.capabilities
**Explanation:** Linux capabilities for containers are specified under the 'securityContext.capabilities' field within the container's specification. This allows fine-grained control over the capabilities added or dropped for that specific container.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes Official Documentation - Security Context</a><br><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#securitycontext-v1-core" target="_blank">Kubernetes API Reference - PodSpec</a>

---

<!-- note:1772101855029 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which configuration in a Kubernetes container's securityContext is used to drop all Linux capabilities, effectively removing extra privileges?
**Options:** A. capabilities: {drop: ['ALL']}<br>B. capabilities: {add: ['NONE']}<br>C. privileged: false<br>D. allowPrivilegeEscalation: false<br>E. runAsNonRoot: true
**Answer:** A (1) – capabilities: {drop: ['ALL']}
**Explanation:** To remove all Linux capabilities from a container, the 'capabilities' field under the container's securityContext should specify 'drop: ['ALL']'. This explicitly drops all added capabilities, minimizing the container's privileges.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-capabilities-for-a-container" target="_blank">Kubernetes Official Documentation - Security Context</a><br><a href="https://www.redhat.com/sysadmin/linux-capabilities-kubernetes" target="_blank">Red Hat - Understanding Linux Capabilities in Kubernetes</a>

---

<!-- note:1772101855031 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What is the role of the 'namespaceSelector' field in a Kubernetes NetworkPolicy?
**Options:** A. To select namespaces where the policy is applied<br>B. To select Pods in specific namespaces for ingress or egress rules<br>C. To label namespaces<br>D. To deny traffic to certain namespaces<br>E. To enforce policies across all namespaces
**Answer:** B (2) – To select Pods in specific namespaces for ingress or egress rules
**Explanation:** The 'namespaceSelector' in a NetworkPolicy is used to select Pods in specific namespaces as sources or destinations for ingress or egress traffic rules. It does not select the namespaces where the policy itself is applied; NetworkPolicies are always applied within the namespace they are defined. It also does not label namespaces, deny traffic directly, or enforce policies cluster-wide.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/#networkpolicy-resource" target="_blank">Kubernetes Official Documentation - Network Policies</a><br><a href="https://docs.projectcalico.org/security/network-policy#namespace-selector" target="_blank">Calico Docs - NetworkPolicy namespaceSelector</a>

---

<!-- note:1772101855032 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** If Kubernetes audit logs are stored at '/var/log/kubernetes/audit.log', which command can you use to view these logs in real time?
**Options:** A. kubectl logs audit<br>B. sudo tail -f /var/log/kubernetes/audit.log<br>C. kubectl get events --audit<br>D. journalctl -u kube-apiserver<br>E. kubectl describe audit-logs
**Answer:** B (2) – sudo tail -f /var/log/kubernetes/audit.log
**Explanation:** Audit logs written to a file such as '/var/log/kubernetes/audit.log' can be viewed in real time using the 'tail -f' command with appropriate permissions, hence 'sudo tail -f /var/log/kubernetes/audit.log'. The 'kubectl logs' command is used for container logs, not audit logs stored on the host. 'kubectl get events --audit' and 'kubectl describe audit-logs' are invalid commands. 'journalctl -u kube-apiserver' shows the kube-apiserver service logs but may not include audit logs if they are configured to a separate file.
**Sources:** <a href="https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/" target="_blank">Kubernetes Official Documentation - Auditing</a><br><a href="https://access.redhat.com/documentation/en-us/openshift_container_platform/4.7/html/security_hardening/monitoring-audit-logs_security-hardening" target="_blank">Red Hat - Viewing Kubernetes Audit Logs</a>

---

<!-- note:1772101855036 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** In a Kubernetes container's securityContext, which field prevents processes from gaining elevated privileges through privilege escalation?
**Options:** A. runAsUser: 0<br>B. privileged: false<br>C. allowPrivilegeEscalation: false<br>D. runAsNonRoot: false<br>E. readOnlyRootFilesystem: true
**Answer:** C (3) – allowPrivilegeEscalation: false
**Explanation:** The 'allowPrivilegeEscalation' field, when set to false, prevents a process from gaining more privileges than its parent process, effectively blocking privilege escalation attacks. Setting 'privileged' to false disables privileged mode but does not specifically prevent privilege escalation. 'runAsUser: 0' runs the container as root, which does not prevent privilege escalation. 'runAsNonRoot: false' allows running as root, so it doesn't prevent privilege escalation. 'readOnlyRootFilesystem: true' restricts filesystem writes but does not control privilege escalation.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes Official Documentation - Security Context</a><br><a href="https://kubernetes.io/docs/concepts/security/pod-security-standards/" target="_blank">Kubernetes Pod Security Standards</a>

---

<!-- note:1772101855037 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which Kubernetes resources, if compromised, could lead to significant security breaches and should be audited carefully? (Select all that apply)
**Options:** A. Secrets<br>B. ConfigMaps<br>C. Pods<br>D. ServiceAccounts<br>E. PersistentVolumes
**Answer:** A, D – Secrets and ServiceAccounts
**Explanation:** Secrets and ServiceAccounts are considered sensitive Kubernetes resources because they often contain confidential information such as credentials, API keys, and tokens. If compromised, these resources can lead to unauthorized access, privilege escalation, or data breaches. ConfigMaps generally contain non-sensitive configuration data and are less critical from a security perspective. While Pods and PersistentVolumes are important, they are not typically audited for sensitive information unless they handle sensitive data explicitly.
**Sources:** <a href="https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/" target="_blank">Kubernetes Official Documentation - Auditing</a><br><a href="https://kubernetes.io/docs/concepts/configuration/secret/" target="_blank">Kubernetes Official Documentation - Secrets</a>

---

<!-- note:1772101855038 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which Kubernetes Admission Controller was deprecated and replaced by Pod Security Admission in Kubernetes version 1.25?
**Options:** A. PodSecurityPolicy<br>B. NodeRestriction<br>C. AlwaysPullImages<br>D. NamespaceLifecycle<br>E. LimitRanger
**Answer:** A (1) – PodSecurityPolicy
**Explanation:** PodSecurityPolicy was deprecated in Kubernetes version 1.25 and replaced by the Pod Security Admission (PSA) controller. The PSA controller provides a simpler and more flexible way to enforce pod security standards, aligning with Kubernetes' evolving security model. Other options, such as NodeRestriction, AlwaysPullImages, NamespaceLifecycle, and LimitRanger, are not related to this deprecation.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/pod-security-admission/" target="_blank">Kubernetes Official Documentation - Pod Security Admission</a><br><a href="https://kubernetes.io/blog/2021/04/06/podsecuritypolicy-deprecation-past-present-and-future/" target="_blank">Kubernetes Blog - Deprecation of PodSecurityPolicy</a>

---

<!-- note:1772101855039 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Select all that apply: Which Kubernetes object(s) allow you to define a set of rules for validating or mutating admission requests?
**Options:** A. ValidatingWebhookConfiguration<br>B. MutatingWebhookConfiguration<br>C. AdmissionController<br>D. CustomResourceDefinition<br>E. WebhookPolicy
**Answer:** A, B – ValidatingWebhookConfiguration and MutatingWebhookConfiguration
**Explanation:** `ValidatingWebhookConfiguration` and `MutatingWebhookConfiguration` are used to integrate admission webhooks that validate or mutate admission requests. Option 2 (`AdmissionController`) is a general term for the mechanism but not a specific Kubernetes object. Option 3 (`CustomResourceDefinition`) is used to define custom resources, and Option 4 (`WebhookPolicy`) is not a valid Kubernetes object.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/" target="_blank">Kubernetes Admission Webhooks Documentation</a><br><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#validatingwebhookconfiguration-v1-admissionregistration-k8s-io" target="_blank">Kubernetes API Reference</a>

---

<!-- note:1772101855040 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which field in the Pod spec can you use to disable privilege escalation for all containers in the Pod?
**Options:** A. securityContext.allowPrivilegeEscalation: false<br>B. spec.containers.securityContext.allowPrivilegeEscalation: false<br>C. podSecurityContext.allowPrivilegeEscalation: false<br>D. spec.securityContext.allowPrivilegeEscalation: false<br>E. metadata.securityContext.allowPrivilegeEscalation: false
**Answer:** B (2) – spec.containers.securityContext.allowPrivilegeEscalation: false
**Explanation:** The correct field to disable privilege escalation for all containers in a Pod is 'spec.containers.securityContext.allowPrivilegeEscalation: false'. This must be set individually for each container within the Pod, as there is no global 'allowPrivilegeEscalation' setting at the Pod level.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes Documentation on Security Context</a><br><a href="https://www.wiz.io/academy/kubernetes-security-context-best-practices" target="_blank">Wiz Kubernetes Security Context Best Practices</a><br><a href="https://www.redhat.com/en/blog/guide-to-kubernetes-security-context-pod-security-policy-psp" target="_blank">Red Hat Guide to Kubernetes Security Context</a>

---

<!-- note:1772101855042 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** In a Kubernetes NetworkPolicy, which selector is used to specify the Pods to which the policy applies?
**Options:** A. podSelector<br>B. namespaceSelector<br>C. policySelector<br>D. matchLabels<br>E. appSelector
**Answer:** A (1) – podSelector
**Explanation:** The 'podSelector' field in a NetworkPolicy defines the set of Pods that the policy applies to by selecting Pods based on labels. 'namespaceSelector' selects namespaces, not Pods. 'policySelector' is not a valid field in NetworkPolicy. 'matchLabels' is a label selector syntax used inside 'podSelector' but is not itself a selector field. 'appSelector' is not a standard Kubernetes selector field.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Official Documentation - Network Policies</a><br><a href="https://github.com/kubernetes/community/blob/master/contributors/design-proposals/network/networkpolicy.md" target="_blank">CNCF Network Policy Specification</a>

---

<!-- note:1772101855043 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** In a Kubernetes NetworkPolicy specification, which field defines the allowed egress destinations for Pods?
**Options:** A. ingress<br>B. egress<br>C. to<br>D. from<br>E. destinations
**Answer:** B (2) – egress
**Explanation:** The 'egress' field in a NetworkPolicy spec specifies the rules that allow outbound traffic from selected Pods to specified destinations. The 'ingress' field defines allowed inbound traffic. 'to' is a subfield inside 'egress' rules specifying destination peers but is not the top-level field defining egress rules. 'from' is used in ingress rules to specify source peers. 'destinations' is not a valid field in NetworkPolicy.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Official Documentation - Network Policies</a><br><a href="https://github.com/kubernetes/community/blob/master/contributors/design-proposals/network/networkpolicy.md" target="_blank">CNCF Network Policy Specification</a>

---

<!-- note:1772101855044 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which of the following are valid components of a Kubernetes audit policy? (Select all that apply)
**Options:** A. Rules<br>B. Levels<br>C. Stages<br>D. Users<br>E. Verbs
**Answer:** A, C, D, E – rules, stages, users, and verbs (levels is a field inside rules, not a component)
**Explanation:** A Kubernetes audit policy is composed of 'Rules' that define what events to capture. Each rule can specify 'Stages' of the request lifecycle (such as RequestReceived, ResponseStarted). 'Users' can be specified to filter audit events by user identity. 'Verbs' define the types of API operations (e.g., get, create) to audit. 'Levels' is not a component of the policy structure but rather a field inside rules specifying the detail level of logging (e.g., None, Metadata).
**Sources:** <a href="https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/" target="_blank">Kubernetes Official Documentation - Auditing</a><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#audit" target="_blank">Kubernetes Audit Policy Documentation</a>

---

<!-- note:1772101855045 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** In a Kubernetes audit policy, which 'level' setting logs only metadata about requests but excludes the request and response bodies?
**Options:** A. None<br>B. Metadata<br>C. Request<br>D. RequestResponse<br>E. Minimal
**Answer:** B (2) – Metadata
**Explanation:** The 'Metadata' audit level records request metadata such as request method, resource, user, and timestamp but does not log the request or response bodies. 'None' disables logging. 'Request' logs the request body but not the response. 'RequestResponse' logs both request and response bodies. 'Minimal' is not a standard audit level in Kubernetes.
**Sources:** <a href="https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/" target="_blank">Kubernetes Official Documentation - Auditing</a><br><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#auditpolicy-v1beta1-auditregistration-k8s-io" target="_blank">Kubernetes Audit Policy Levels</a>

---

<!-- note:1772101855048 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** In Kubernetes, which securityContext setting ensures that a container runs as a non-root user to enhance security?
**Options:** A. runAsUser: 0<br>B. runAsNonRoot: true<br>C. runAsGroup: 0<br>D. allowPrivilegeEscalation: false<br>E. privileged: false
**Answer:** B (2) – runAsNonRoot: true
**Explanation:** The 'runAsNonRoot: true' setting enforces that the container must run as a non-root user, preventing it from running with UID 0 (root). This enhances security by limiting container privileges. 'runAsUser: 0' explicitly sets the user to root, which is insecure. 'runAsGroup: 0' sets the group ID but doesn't enforce non-root user. 'allowPrivilegeEscalation: false' prevents privilege escalation but does not enforce non-root user. 'privileged: false' disables privileged mode but does not guarantee a non-root user.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes Official Documentation - Security Context</a><br><a href="https://www.cncf.io/blog/2020/07/15/kubernetes-security-best-practices/" target="_blank">CNCF - Kubernetes Security Best Practices</a>

---

<!-- note:1772101855049 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Select all that apply: Which command(s) can be used to list all ServiceAccounts in the 'dev' namespace?
**Options:** A. kubectl get sa -n dev<br>B. kubectl get serviceaccount -A<br>C. kubectl get serviceaccounts --namespace=dev<br>D. kubectl describe serviceaccounts -n dev<br>E. kubectl list sa dev
**Answer:** A, C, D – kubectl get sa -n dev; kubectl get serviceaccounts --namespace=dev; kubectl describe serviceaccounts -n dev
**Explanation:** The commands `kubectl get sa -n dev`, `kubectl get serviceaccounts --namespace=dev`, and `kubectl describe serviceaccounts -n dev` all list ServiceAccounts in the 'dev' namespace. The first two provide a summary list, while `kubectl describe` provides detailed information about each ServiceAccount. Option 1 (`kubectl get serviceaccount -A`) lists ServiceAccounts across all namespaces, and Option 4 (`kubectl list sa dev`) is not a valid `kubectl` command.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/overview/" target="_blank">Kubernetes Official Documentation</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands/" target="_blank">Kubernetes kubectl Command Reference</a>

---

<!-- note:1772101855050 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** In a Kubernetes Pod specification, which field is used to specify the ServiceAccount under which the Pod should run?
**Options:** A. serviceAccount<br>B. serviceAccountName<br>C. accountName<br>D. saName<br>E. serviceAccountSpec
**Answer:** B (2) – serviceAccountName
**Explanation:** The correct field is 'serviceAccountName', which defines the name of the ServiceAccount that the Pod uses for authentication and authorization. The other options are incorrect as they are not valid Pod spec fields. 'serviceAccount' and 'accountName' do not exist in the Pod spec. 'saName' and 'serviceAccountSpec' are not recognized fields.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/" target="_blank">Kubernetes Official Documentation - Service Accounts</a><br><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#podspec-v1-core" target="_blank">Kubernetes API Reference - PodSpec</a>

---

<!-- note:1772101855051 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which Kubernetes object defines cluster-wide permissions and roles that can be assigned to users or service accounts?
**Options:** A. Role<br>B. ClusterRole<br>C. RoleBinding<br>D. ClusterRoleBinding<br>E. ServiceAccount
**Answer:** B (2) – ClusterRole
**Explanation:** 'ClusterRole' defines permissions that apply across the entire Kubernetes cluster, allowing for cluster-wide access control. In contrast, 'Role' defines permissions scoped to a specific namespace. 'RoleBinding' and 'ClusterRoleBinding' are used to assign Roles or ClusterRoles to users or service accounts but do not define permissions themselves. 'ServiceAccount' represents an identity for processes running in Pods, not permissions.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Official Documentation - RBAC Authorization</a><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole" target="_blank">Kubernetes Official Documentation - Roles and ClusterRoles</a>

---

<!-- note:1772101855053 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which of the following securityContext fields are commonly applied at the Pod level in Kubernetes? (Select all that apply)
**Options:** A. runAsUser<br>B. fsGroup<br>C. privileged<br>D. capabilities<br>E. seLinuxOptions
**Answer:** A, B, E – runAsUser, fsGroup, and seLinuxOptions (privileged and capabilities are container-level)
**Explanation:** At the Pod level, 'runAsUser' specifies the user ID for all containers in the Pod, 'fsGroup' sets the group ID for mounted volumes, and 'seLinuxOptions' configures SELinux labels for the Pod. 'privileged' and 'capabilities' are container-level settings and cannot be set at the Pod level. Therefore, only 'runAsUser', 'fsGroup', and 'seLinuxOptions' are valid Pod-level securityContext fields.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes Official Documentation - Security Context</a><br><a href="https://www.redhat.com/sysadmin/kubernetes-security-contexts" target="_blank">Red Hat - Understanding Kubernetes Security Contexts</a>

---

<!-- note:1772101855058 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** In a Kubernetes container's securityContext, which field allows you to add specific Linux capabilities to the container?
**Options:** A. addCapabilities<br>B. linuxCapabilities<br>C. capabilities.add<br>D. securityOptions<br>E. privilegedCaps
**Answer:** C (3) – capabilities.add
**Explanation:** The correct field is 'capabilities.add', which is a list under the container's securityContext that specifies which Linux capabilities to add to the container's default set. 'addCapabilities' and 'linuxCapabilities' are incorrect field names. 'securityOptions' and 'privilegedCaps' are not valid Kubernetes securityContext fields.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-capabilities-for-a-container" target="_blank">Kubernetes Official Documentation - Security Context</a><br><a href="https://www.redhat.com/sysadmin/linux-capabilities-kubernetes" target="_blank">Red Hat - Linux Capabilities in Kubernetes</a>

---

<!-- note:1772101855061 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** To enable audit logging in Kubernetes, which flag must be added to the API server configuration to specify the log file path?
**Options:** A. --audit-log-path<br>B. --audit-policy-file<br>C. --enable-audit<br>D. --audit-log-maxage<br>E. --audit-log-format
**Answer:** A (1) – --audit-log-path
**Explanation:** The '--audit-log-path' flag is crucial for enabling audit logging by specifying the path where audit logs will be stored. This allows for the collection and analysis of API requests and responses, which is essential for security auditing and compliance.
**Sources:** <a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/tasks/debug-application-cluster/audit/" target="_blank">Kubernetes Audit Logging</a>

---

<!-- note:1772101855062 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which of the following steps are necessary to enable audit logging in Kubernetes? (Select all that apply)
**Options:** A. Create an audit policy file<br>B. Configure the kubelet with audit flags<br>C. Add '--audit-policy-file' flag to API server<br>D. Restart the kube-controller-manager<br>E. Specify '--audit-log-path' in the API server configuration
**Answer:** A, C, E – create audit policy file, --audit-policy-file, and --audit-log-path on the API server
**Explanation:** To enable audit logging in Kubernetes, you must create an audit policy file, specify this file using the '--audit-policy-file' flag in the API server configuration, and define the log path using '--audit-log-path'. These steps ensure that audit logs are properly configured and stored.
**Sources:** <a href="https://kubernetes.io/docs/tasks/debug-application-cluster/audit/#audit-policy" target="_blank">Kubernetes Audit Policy</a><br><a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/" target="_blank">Kubernetes API Server Configuration</a>

---

<!-- note:1772101855071 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which Kubernetes resource is used to assign permissions within a namespace to a user or group?
**Options:** A. ClusterRole<br>B. Role<br>C. ClusterRoleBinding<br>D. RoleBinding<br>E. ServiceAccount
**Answer:** D (4) – RoleBinding
**Explanation:** A RoleBinding is used to grant permissions defined in a Role to users or groups within a specific namespace. This is essential for fine-grained access control in Kubernetes.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/#rolebinding-and-clusterrolebinding" target="_blank">Kubernetes RoleBinding</a><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/authorization/" target="_blank">Kubernetes Authorization</a>

---

<!-- note:1772101855072 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What is the correct 'kind' value for an object that associates a Role with a user or group?
**Options:** A. RoleBinding<br>B. ClusterRole<br>C. User<br>D. Group<br>E. RoleAssignment
**Answer:** A (1) – RoleBinding
**Explanation:** A RoleBinding is the Kubernetes object that binds a Role to a user or group within a namespace, enabling them to perform specific actions.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/#rolebinding-and-clusterrolebinding" target="_blank">Kubernetes RoleBinding</a><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes RBAC</a>

---

<!-- note:1772101855077 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which securityContext field makes a container's root filesystem read-only to prevent modifications?
**Options:** A. readOnlyFileSystem<br>B. readOnlyRootFilesystem<br>C. immutableRoot<br>D. filesystemReadonly<br>E. noWriteFilesystem
**Answer:** B (2) – readOnlyRootFilesystem
**Explanation:** The 'readOnlyRootFilesystem' field in a container's securityContext makes the root filesystem read-only, preventing any modifications and enhancing container security.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes SecurityContext</a><br><a href="https://kubernetes.io/docs/concepts/security/pod-security-standards/" target="_blank">Kubernetes Pod Security</a>

---

<!-- note:1772101855078 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** In Kubernetes security best practices, what is the primary security benefit of configuring a container's root filesystem as read-only?
**Options:** A. Improved container startup performance<br>B. Reduced container image storage requirements<br>C. Enhanced security by preventing malicious filesystem modifications<br>D. Enables cross-container file sharing capabilities<br>E. Simplifies rolling updates for containerized applications
**Answer:** C (3) – Enhanced security by preventing malicious filesystem modifications
**Explanation:** A read-only root filesystem (configured via securityContext.readOnlyRootFilesystem) prevents attackers from modifying system files, installing malware, or writing to sensitive directories, even if they gain shell access. This security hardening measure is recommended by CIS Kubernetes Benchmarks and Kubernetes security best practices.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes Documentation - Security Contexts</a><br><a href="https://www.cisecurity.org/benchmark/kubernetes" target="_blank">CIS Kubernetes Benchmark v1.8</a>

---

<!-- note:1772101855081 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** When creating a NetworkPolicy to implement default deny egress traffic for Kubernetes pods, which policyTypes value must be specified?
**Options:** A. Ingress only<br>B. Egress only<br>C. Both Ingress and Egress<br>D. DenyAll policy type<br>E. Egress with explicit deny rules
**Answer:** B (2) – Egress only
**Explanation:** To create default deny egress, policyTypes must include Egress, and no egress rules should be defined. This combination blocks all outgoing traffic while allowing explicit exceptions through subsequent allow rules. The Kubernetes NetworkPolicy documentation emphasizes this pattern for implementing zero-trust network policies.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes NetworkPolicy Documentation</a><br><a href="https://docs.cilium.io/en/stable/security/policy/" target="_blank">Cilium Network Policy Guide</a>

---

<!-- note:1772101855082 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** In Kubernetes NetworkPolicy configuration, what podSelector configuration creates a default-deny-all policy that applies to all pods in a namespace?
**Options:** A. Empty selector: {}<br>B. Wildcard selector: '*'<br>C. Omitted podSelector field<br>D. Null value: podSelector: null<br>E. Label-based exclusion selector
**Answer:** A (1) – Empty selector: {}
**Explanation:** An empty podSelector ({}) matches all pods in the namespace, while omitting the field would make the policy ineffective. This configuration is critical for implementing namespace-wide default-deny policies, as documented in Kubernetes network policy best practices and the CIS Kubernetes Benchmark.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/#default-deny-all-ingress-and-all-egress-traffic" target="_blank">Kubernetes NetworkPolicy Best Practices</a><br><a href="https://blog.aquasec.com/kubernetes-network-policy-best-practices" target="_blank">Aqua Security Kubernetes Network Policy Guide</a>

---

<!-- note:1772101855083 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which securityContext configuration field enables privileged container mode in Kubernetes pods?
**Options:** A. allowPrivilegeEscalation: true<br>B. runAsPrivileged: true<br>C. privileged: true<br>D. capabilities.add: ["ALL"]<br>E. securityContext.privilegedMode: enabled
**Answer:** C (3) – privileged: true
**Explanation:** The privileged: true setting gives the container full access to host devices and capabilities, equivalent to root privileges on the host. This dangerous configuration should be avoided in production, as emphasized in Kubernetes security documentation and CIS Benchmarks. Privileged containers bypass most security controls and namespace restrictions.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes Security Context Documentation</a><br><a href="https://www.cisecurity.org/benchmark/kubernetes" target="_blank">CIS Kubernetes Benchmark v1.8 - 5.2.1</a>

---

<!-- note:1772101855085 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which Kubernetes pod specification field prevents automatic mounting of the default ServiceAccount token?
**Options:** A. mountServiceAccountToken: false<br>B. automountServiceAccountToken: false<br>C. serviceAccountToken: disabled<br>D. disableServiceAccountMount: true<br>E. serviceAccountMountPolicy: none
**Answer:** B (2) – automountServiceAccountToken: false
**Explanation:** automountServiceAccountToken: false in the pod spec prevents automatic mounting of the service account token, reducing attack surface. This security hardening measure is recommended when pods don't need Kubernetes API access, as noted in the Kubernetes service account documentation and security best practices guides.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/" target="_blank">Kubernetes Service Accounts Documentation</a><br><a href="https://kubernetes.io/docs/concepts/security/overview/" target="_blank">Kubernetes Security Best Practices</a>

---

<!-- note:1772101855086 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Why would you disable automounting of ServiceAccount tokens in a Kubernetes Pod?
**Options:** A. To reduce memory usage of the Pod<br>B. To prevent the Pod from having unnecessary or unauthorized access to the Kubernetes API<br>C. To improve the application's runtime performance<br>D. To enable network policies enforcement<br>E. To allow the Pod to use multiple ServiceAccounts simultaneously
**Answer:** B (2) – To prevent the Pod from having unnecessary or unauthorized access to the Kubernetes API
**Explanation:** Disabling automounting of ServiceAccount tokens prevents the Pod from automatically receiving credentials that grant access to the Kubernetes API. This reduces the attack surface by limiting the Pod's ability to interact with the cluster unless explicitly required. The other options are incorrect because automounting tokens does not significantly affect memory usage or application performance, does not directly enable network policies, and Pods cannot use multiple ServiceAccounts simultaneously.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/" target="_blank">Kubernetes Official Documentation - Service Accounts</a><br><a href="https://kubernetes.io/docs/concepts/security/pod-security-standards/" target="_blank">Kubernetes Official Documentation - Pod Security Standards</a>

---

<!-- note:1772101855088 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What is the primary function of the ImagePolicyWebhook admission controller in Kubernetes?
**Options:** A. To scan container images for vulnerabilities during runtime<br>B. To enforce custom policies on container images during admission to the cluster<br>C. To cache container images locally for faster deployment<br>D. To automatically update container images to the latest version<br>E. To log all image pull requests for auditing purposes
**Answer:** B (2) – To enforce custom policies on container images during admission to the cluster
**Explanation:** The ImagePolicyWebhook admission controller intercepts Pod creation requests and enforces policies on container images before they are admitted into the cluster, such as validating image signatures or restricting images from untrusted registries. It does not perform runtime vulnerability scanning, caching, automatic updates, or logging image pulls, which are handled by other tools or controllers.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#imagepolicywebhook" target="_blank">Kubernetes Official Documentation - Admission Controllers</a><br><a href="https://kubernetes.io/blog/2019/03/21/image-policy-webhook/" target="_blank">Kubernetes Blog - Using ImagePolicyWebhook for Image Validation</a>

---

<!-- note:1772101855089 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** In a Kubernetes audit policy, which log level should be set to capture the full content of both requests and responses?
**Options:** A. None<br>B. Metadata<br>C. Request<br>D. RequestResponse<br>E. Content
**Answer:** D (4) – RequestResponse
**Explanation:** The 'RequestResponse' audit log level records both the metadata and the full content of requests and responses, providing comprehensive audit information. 'None' disables logging, 'Metadata' logs only metadata without content, 'Request' logs request content but not responses, and 'Content' is not a valid audit log level in Kubernetes.
**Sources:** <a href="https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/" target="_blank">Kubernetes Official Documentation - Auditing</a><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/audit/#audit-levels" target="_blank">Kubernetes Official Documentation - Audit Policy</a>

---

<!-- note:1772101855090 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** How do you configure a Kubernetes audit policy rule to log events for all resources within a specific namespace?
**Options:** A. Set 'namespace: <namespace>' in the policy rule<br>B. Use 'namespaces: ["<namespace>"]' under the rule's 'namespaces' field<br>C. Add 'resourceNames: ["<namespace>"]' to the rule<br>D. Set 'level: Namespace' in the policy<br>E. Specify 'namespaceSelector: {matchNames: ["<namespace>"]}'
**Answer:** B (2) – Use 'namespaces: ["<namespace>"]' under the rule's 'namespaces' field
**Explanation:** In Kubernetes audit policies, the 'namespaces' field in a rule specifies the namespaces to which the rule applies, allowing you to log events for all resources within those namespaces. The other options are incorrect because 'namespace' is not a valid field, 'resourceNames' filters specific resource names rather than namespaces, 'level' defines log verbosity not scope, and 'namespaceSelector' is not used in audit policies.
**Sources:** <a href="https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/#audit-policy" target="_blank">Kubernetes Official Documentation - Audit Policy Configuration</a><br><a href="https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apiserver/plugin/pkg/audit/policy/testdata/policy.yaml" target="_blank">Kubernetes GitHub - Audit Policy Examples</a>

---

<!-- note:1772101855091 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which kubectl command correctly creates a generic secret named 'db-secret' with a key 'password' and the value 'S3cr3t!'?
**Options:** A. kubectl create secret generic db-secret --password='S3cr3t!'<br>B. kubectl create secret db-secret --from-literal='password=S3cr3t!'<br>C. kubectl create secret generic db-secret --from-literal=password=S3cr3t!<br>D. kubectl create secret tls db-secret --key='S3cr3t!'<br>E. kubectl create secret docker-registry db-secret --password='S3cr3t!'
**Answer:** C (3) – kubectl create secret generic db-secret --from-literal=password=S3cr3t!
**Explanation:** The correct command uses 'kubectl create secret generic' with the '--from-literal' flag to specify a key-value pair for the secret. The syntax is: kubectl create secret generic db-secret --from-literal=password=S3cr3t!. The other options are incorrect because '--password' is not a valid flag for generic secrets, 'kubectl create secret' without 'generic' is incomplete, 'tls' secrets require certificate and key files, and 'docker-registry' secrets are for Docker credentials, not arbitrary key-value pairs.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/secret/#creating-a-secret-manually" target="_blank">Kubernetes Official Documentation - Managing Secrets</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#create-secret" target="_blank">Kubernetes Official Documentation - kubectl create secret</a>

---

<!-- note:1772101855092 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** How can you retrieve the value of a secret key 'username' from the secret 'db-secret' in the namespace 'prod'?
**Options:** A. kubectl get secret db-secret -n prod -o jsonpath='{.data.username}' | base64 --decode<br>B. kubectl describe secret db-secret -n prod<br>C. kubectl get secret db-secret -n prod -o yaml<br>D. kubectl read secret db-secret -n prod --key=username<br>E. kubectl decode secret db-secret -n prod --field=username
**Answer:** A (1) – kubectl get secret db-secret -n prod -o jsonpath='{.data.username}' | base64 --decode
**Explanation:** To extract and decode the secret value, you use `kubectl get` with `jsonpath` to specify the key and then decode the base64 encoded value. This method is efficient for retrieving specific secret values.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/secret/" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/reference/kubectl/overview/" target="_blank">Kubectl Reference</a>

---

<!-- note:1772101855107 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which Kubernetes resource is used to enforce Pod Security Standards within a namespace?
**Options:** A. PodSecurityPolicy<br>B. NetworkPolicy<br>C. LimitRange<br>D. ResourceQuota<br>E. Pod Security Admission Controller
**Answer:** E (5) – Pod Security Admission Controller
**Explanation:** The Pod Security Admission Controller is responsible for enforcing Pod Security Standards in Kubernetes. It ensures that pods comply with predefined security policies, enhancing cluster security.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/pod-security-standards/" target="_blank">Kubernetes Pod Security Standards</a><br><a href="https://kubernetes.io/docs/concepts/security/pod-security-admission/" target="_blank">Pod Security Admission Controller</a>

---

<!-- note:1772101855124 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which built-in Kubernetes authentication method is generally not recommended for production environments?
**Options:** A. Static Token File<br>B. OpenID Connect (OIDC)<br>C. Service Accounts<br>D. Client Certificates<br>E. Integrating with cloud provider IAM
**Answer:** A (1) – Static Token File
**Explanation:** Static Token File authentication is not recommended for production due to security concerns. It lacks the robustness and flexibility of other methods like OIDC or Service Accounts.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Authentication</a><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/#static-token-file" target="_blank">Static Token File Documentation</a>

---

<!-- note:1772101855125 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which Kubernetes resource defines permissions within a specific namespace?
**Options:** A. ClusterRole<br>B. ClusterRoleBinding<br>C. Role<br>D. RoleBinding<br>E. ServiceAccount
**Answer:** C (3) – Role
**Explanation:** A Role in Kubernetes defines permissions within a namespace. It specifies what actions can be performed by users or service accounts within that namespace.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole" target="_blank">Kubernetes Roles</a><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">RBAC Documentation</a>

---

<!-- note:1772101855126 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What is the primary function of a 'RoleBinding' in Kubernetes RBAC?
**Options:** A. Defines cluster-wide permissions<br>B. Binds a ClusterRole to a namespace<br>C. Binds a Role to users or groups within a namespace<br>D. Creates a new ServiceAccount<br>E. Defines network policies
**Answer:** C (3) – Binds a Role to users or groups within a namespace
**Explanation:** A RoleBinding in Kubernetes assigns a Role to specific users or groups within a namespace, granting them the permissions defined by that Role.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/#rolebinding-and-clusterrolebinding" target="_blank">Kubernetes RoleBindings</a><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">RBAC Documentation</a>

---

<!-- note:1772101855127 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What admission controller should be used to enforce Pod Security Standards in Kubernetes versions 1.25 and later?
**Options:** A. PodSecurityPolicy<br>B. Pod Security Admission Controller<br>C. NodeRestriction<br>D. ResourceQuota<br>E. LimitRanger
**Answer:** B (2) – Pod Security Admission Controller
**Explanation:** The Pod Security Admission Controller is the recommended method for enforcing Pod Security Standards in Kubernetes versions 1.25 and above. This controller replaces the deprecated PodSecurityPolicy and provides a more flexible and efficient way to manage pod security.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/pod-security-admission/" target="_blank">Kubernetes Documentation</a><br><a href="https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md" target="_blank">Kubernetes Release Notes</a>

---

<!-- note:1772101855128 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** In Kubernetes, what is the main reason for using namespaces?
**Options:** A. To provide network isolation between different applications.<br>B. To group and logically isolate resources such as deployments, services, and pods.<br>C. To enforce security policies across the entire cluster.<br>D. To manage the lifecycle of persistent storage volumes.<br>E. To monitor the overall health and performance of the Kubernetes cluster.
**Answer:** B (2) – To group and logically isolate resources such as deployments, services, and pods.
**Explanation:** Namespaces in Kubernetes are primarily used to logically divide a cluster into multiple virtual clusters. This allows teams or projects to operate in isolation from one another within the same physical cluster. While namespaces can be used in conjunction with network policies to provide network isolation, their primary purpose is logical grouping and isolation of Kubernetes resources like pods, services, and deployments. They do not inherently enforce security policies or manage storage volumes directly, nor are they primarily for monitoring cluster health.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Documentation: Namespaces</a><br><a href="https://www.aquasec.com/cloud-native-academy/kubernetes-security/kubernetes-namespaces/" target="_blank">Aqua Security: Kubernetes Namespaces</a>

---

<!-- note:1772101855130 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What is the recommended method for storing sensitive data, such as passwords or tokens, in a Kubernetes environment?
**Options:** A. Hardcode them in application code<br>B. Store them in ConfigMaps<br>C. Use Kubernetes Secrets<br>D. Store them in environment variables<br>E. Include them in container images
**Answer:** C (3) – Use Kubernetes Secrets
**Explanation:** Kubernetes Secrets are specifically designed to securely store sensitive data. They provide a secure way to manage and distribute sensitive information to pods, reducing the risk of data exposure compared to other methods like hardcoding or using environment variables.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/secret/" target="_blank">Kubernetes Documentation</a><br><a href="https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_Practices.html" target="_blank">OWASP Secure Coding Practices</a>

---

<!-- note:1772101855131 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which Kubernetes resource is used to enforce network segmentation between pods?
**Options:** A. NetworkPolicy<br>B. PodSecurityPolicy<br>C. ResourceQuota<br>D. LimitRange<br>E. Ingress
**Answer:** A (1) – NetworkPolicy
**Explanation:** NetworkPolicy defines rules that segment network traffic between pods, allowing you to control the flow of traffic and isolate pods from each other. This is essential for securing communication within a Kubernetes cluster.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Documentation</a><br><a href="https://docs.projectcalico.org/security/calico-network-policy" target="_blank">Calico Network Policies</a>

---

<!-- note:1772101855132 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Why is it advisable to avoid running containers with root privileges in a Kubernetes environment?
**Options:** A. It increases resource consumption<br>B. It can lead to security risks by granting unnecessary permissions<br>C. It reduces application performance<br>D. It prevents containers from accessing the network<br>E. It is required by Kubernetes policies
**Answer:** B (2) – It can lead to security risks by granting unnecessary permissions
**Explanation:** Running containers as root increases the risk of privilege escalation and other security attacks. By running containers as non-root users, you reduce the attack surface and improve the overall security posture of your Kubernetes environment.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/pod-security-standards/" target="_blank">Kubernetes Best Practices</a><br><a href="https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_Practices.html" target="_blank">OWASP Secure Coding Practices</a>

---

<!-- note:1772101855133 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which security context setting ensures that a container runs as a non-root user in Kubernetes?
**Options:** A. privileged: false<br>B. allowPrivilegeEscalation: false<br>C. runAsNonRoot: true<br>D. readOnlyRootFilesystem: true<br>E. capabilities: []
**Answer:** C (3) – runAsNonRoot: true
**Explanation:** Setting 'runAsNonRoot: true' in a pod's security context ensures that the container is not run as the root user. This setting helps prevent unnecessary privilege escalation and improves container security.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/concepts/security/pod-security-standards/" target="_blank">Kubernetes Security Best Practices</a>

---

<!-- note:1772101855134 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** In Kubernetes security contexts, what specific security benefit does configuring 'readOnlyRootFilesystem: true' provide to containers?
**Options:** A. Prevents container processes from modifying host network configurations<br>B. Enables root user privileges for container operations<br>C. Restricts container processes from writing to the root filesystem<br>D. Allows containers to bypass filesystem permission checks<br>E. Disables container logging capabilities
**Answer:** C (3) – Restricts container processes from writing to the root filesystem
**Explanation:** Setting readOnlyRootFilesystem to true mounts the container's root filesystem as read-only, preventing malicious processes from writing to or modifying system files. This hardening measure significantly reduces attack surfaces by blocking persistence mechanisms and limiting damage from container escapes. Other options describe unrelated security mechanisms: network restrictions (option 1), privilege escalation (option 2/4), and logging (option 5) require separate configurations.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes Documentation - Security Contexts</a><br><a href="https://www.cisecurity.org/benchmark/kubernetes/" target="_blank">CIS Kubernetes Benchmark v1.8</a>

---

<!-- note:1772101855136 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** When implementing Kubernetes NetworkPolicies, what security implication should administrators consider when using an empty podSelector field?
**Options:** A. Creates a default-allow-all traffic pattern within the namespace<br>B. Applies the policy to all pods in the specified namespace<br>C. Generates validation errors in the policy controller<br>D. Only affects newly created pods in the namespace<br>E. Enforces cross-namespace communication rules
**Answer:** B (2) – Applies the policy to all pods in the specified namespace
**Explanation:** An empty podSelector in a NetworkPolicy selects all pods in the namespace, meaning the policy applies to all pods in that namespace. The effect on traffic depends on the policy's ingress and egress rules; it does not by itself create a default-allow or default-deny behavior. Administrators should carefully design policies with empty podSelectors to avoid unintended broad application. Other options misrepresent NetworkPolicy mechanics: validation errors (option 3) do not occur due to empty selectors, scope is not limited to new pods (option 4), and cross-namespace communication (option 5) requires explicit policy rules.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes NetworkPolicy Documentation</a><br><a href="https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF" target="_blank">NSA/CISA Kubernetes Hardening Guide</a>

---

<!-- note:1772101855140 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What critical security objectives are achieved through regular vulnerability scanning of container images in Kubernetes environments?
**Options:** A. Optimizes container runtime performance metrics<br>B. Reduces container image layer count<br>C. Identifies and remediates known software vulnerabilities<br>D. Ensures compliance with open-source licensing<br>E. Accelerates container deployment pipelines
**Answer:** C (3) – Identifies and remediates known software vulnerabilities
**Explanation:** Regular image scanning detects vulnerabilities in base images and dependencies, enabling remediation before deployment. This practice addresses CVE management and reduces attack surfaces, forming a crucial part of DevSecOps pipelines. Other options describe unrelated benefits: performance (option 1), licensing (option 4), and deployment speed (option 5) require different tooling and processes.
**Sources:** <a href="https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-190.pdf" target="_blank">NIST SP 800-190 Container Security Guide</a><br><a href="https://kubernetes.io/docs/concepts/security/overview/" target="_blank">Kubernetes Security Best Practices</a>

---

<!-- note:1772101855141 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which open-source tool specializes in static security analysis of Kubernetes manifests through vulnerability scanning and policy checks?
**Options:** A. kube-hunter (penetration testing tool)<br>B. kubesec (security risk analysis)<br>C. kubectl (cluster management CLI)<br>D. kubelet (node agent)<br>E. etcdctl (key-value store client)
**Answer:** B (2) – kubesec (security risk analysis)
**Explanation:** Kubesec analyzes Kubernetes manifests for security misconfigurations, providing risk scores and remediation guidance. It checks for common issues like privileged containers, missing security contexts, and insecure capabilities. Other tools serve different purposes: kube-hunter (option 1) tests live clusters, kubectl (option 3) manages resources, kubelet (option 4) runs pods, and etcdctl (option 5) interacts with etcd.
**Sources:** <a href="https://github.com/controlplaneio/kubesec" target="_blank">Kubesec GitHub Repository</a><br><a href="https://landscape.cncf.io/card-mode?category=security-compliance&grouping=category" target="_blank">CNCF Security Tooling Landscape</a>

---

<!-- note:1772101855146 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** How do Kubernetes NetworkPolicies enhance cluster security when properly configured?
**Options:** A. Enable automatic TLS certificate rotation<br>B. Enforce least-privilege communication between pods<br>C. Manage persistent volume encryption<br>D. Provide application auto-scaling capabilities<br>E. Enable cluster-wide logging aggregation
**Answer:** B (2) – Enforce least-privilege communication between pods
**Explanation:** NetworkPolicies implement microsegmentation by controlling pod-to-pod communication through label selectors, effectively enforcing zero-trust networking principles. They prevent lateral movement attacks by restricting traffic flows between services. Other options describe unrelated features: TLS (option 1), storage (option 3), scaling (option 4), and logging (option 5) require different configurations.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/#best-practices" target="_blank">Kubernetes NetworkPolicy Best Practices</a><br><a href="https://www.cisecurity.org/benchmark/kubernetes/" target="_blank">CIS Kubernetes Benchmark Network Policies Section</a>

---

<!-- note:1772101855147 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What is the primary purpose of audit logging in Kubernetes?
**Options:** A. To monitor application performance<br>B. To track and record API server requests for security and compliance auditing<br>C. To manage network policies<br>D. To automatically scale applications based on load<br>E. To store container images
**Answer:** B (2) – To track and record API server requests for security and compliance auditing
**Explanation:** Audit logging in Kubernetes is designed to record all requests made to the API server, capturing details about who did what and when. This information is crucial for security auditing, compliance monitoring, and forensic analysis. It is not intended for monitoring application performance, managing network policies, scaling applications, or storing container images, which are handled by other Kubernetes components or tools.
**Sources:** <a href="https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/" target="_blank">Kubernetes Official Documentation - Auditing</a><br><a href="https://github.com/cncf/sig-security/blob/main/security-whitepaper.md#audit-logging" target="_blank">CNCF Security Whitepaper - Kubernetes Audit Logging</a>

---

<!-- note:1772101855148 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which API server flag is used to specify the audit policy file that defines what events are recorded in Kubernetes audit logs?
**Options:** A. --audit-log-path<br>B. --audit-policy-file<br>C. --enable-audit<br>D. --audit-log-maxage<br>E. --audit-log-format
**Answer:** B (2) – --audit-policy-file
**Explanation:** The '--audit-policy-file' flag is used to specify the path to the audit policy file, which controls the granularity and types of events that are logged by the Kubernetes API server. Other flags like '--audit-log-path' specify where to write the logs, '--audit-log-maxage' controls log retention, and '--audit-log-format' defines the log format. There is no '--enable-audit' flag; audit logging is enabled by configuring these flags properly.
**Sources:** <a href="https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/#audit-policy" target="_blank">Kubernetes Official Documentation - Auditing</a><br><a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/" target="_blank">Kubernetes API Server Command Line Reference</a>

---

<!-- note:1772101855149 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** In Kubernetes, what is the purpose of the Pod Security Standards?
**Options:** A. A deprecated feature replaced by PodSecurityPolicy<br>B. A set of built-in policies that enforce best practices for pod security<br>C. A configuration for network policies<br>D. A type of storage class for pods<br>E. An admission controller for scheduling pods
**Answer:** B (2) – A set of built-in policies that enforce best practices for pod security
**Explanation:** Pod Security Standards (PSS) are predefined policy levels provided by Kubernetes to enforce security best practices for pods. They replace the deprecated PodSecurityPolicy and provide three levels—Privileged, Baseline, and Restricted—to control pod permissions and capabilities. They are not related to network policies, storage classes, or pod scheduling admission controllers.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/pod-security-standards/" target="_blank">Kubernetes Official Documentation - Pod Security Standards</a><br><a href="https://kubernetes.io/blog/2021/04/06/podsecuritypolicy-deprecation-pod-security-admission/" target="_blank">Kubernetes Blog - Deprecation of PodSecurityPolicy</a>

---

<!-- note:1772101855150 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which of the following are the recognized Pod Security Standard levels in Kubernetes? (Select all that apply)
**Options:** A. Privileged<br>B. Baseline<br>C. Restricted<br>D. Unrestricted<br>E. Default
**Answer:** A, B, C – Privileged, Baseline, and Restricted
**Explanation:** The Pod Security Standards define three levels of security enforcement for pods: Privileged, Baseline, and Restricted. 'Privileged' allows the most permissions, 'Baseline' enforces a moderate security posture suitable for most applications, and 'Restricted' enforces the strictest security controls. 'Unrestricted' and 'Default' are not recognized Pod Security Standard levels.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/pod-security-standards/" target="_blank">Kubernetes Official Documentation - Pod Security Standards</a><br><a href="https://kubernetes.io/docs/concepts/security/overview/" target="_blank">Kubernetes Security Best Practices</a>

---

<!-- note:1772101855151 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** Which Kubernetes resource is commonly used to integrate Open Policy Agent (OPA) for policy enforcement through admission control?
**Options:** A. ValidatingWebhookConfiguration<br>B. MutatingWebhookConfiguration<br>C. AdmissionController<br>D. CustomResourceDefinition<br>E. PolicyController
**Answer:** A (1) – ValidatingWebhookConfiguration
**Explanation:** The 'ValidatingWebhookConfiguration' resource is used to register admission webhooks that validate requests to the Kubernetes API server. Open Policy Agent (OPA) leverages this mechanism to enforce custom policies by intercepting and validating API requests. 'MutatingWebhookConfiguration' is used for modifying requests, 'AdmissionController' is a general concept, 'CustomResourceDefinition' defines new resource types, and 'PolicyController' is not a standard Kubernetes resource.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/" target="_blank">Kubernetes Official Documentation - Admission Controllers</a><br><a href="https://www.openpolicyagent.org/docs/latest/kubernetes-admission-control/" target="_blank">Open Policy Agent - Kubernetes Admission Control</a>

---

<!-- note:1772101855152 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What is the primary function of Open Policy Agent (OPA) in Kubernetes?
**Options:** A. To serve as a container runtime<br>B. To enforce policies and make authorization decisions<br>C. To provide logging and monitoring capabilities<br>D. To manage network routing<br>E. To handle storage management
**Answer:** B (2) – To enforce policies and make authorization decisions
**Explanation:** Open Policy Agent (OPA) is a general-purpose policy engine that evaluates inputs against defined policies to make authorization decisions. In Kubernetes, OPA is commonly used to enforce security and compliance policies on cluster resources. Incorrect options, such as serving as a container runtime, logging, or network management, describe functionalities unrelated to OPA's role.
**Sources:** <a href="https://www.cncf.io/blog/2023/10/09/secure-your-kubernetes-environment-with-opa-and-gatekeeper/" target="_blank">CNCF Blog - Secure Your Kubernetes Environment with OPA and Gatekeeper</a><br><a href="https://spacelift.io/blog/opa-kubernetes" target="_blank">Spacelift Blog - Kubernetes with Open Policy Agent (OPA) & Gatekeeper</a>

---

<!-- note:1772101855153 model:Many -->
**Domain:** Kubernetes Security Fundamentals
**Question:** What is a primary benefit of using Namespaces in Kubernetes?
**Options:** A. Improves application performance<br>B. Provides a mechanism for resource isolation and organization<br>C. Simplifies container image management<br>D. Automatically scales applications based on load<br>E. Eliminates the need for Pods
**Answer:** B (2) – Provides a mechanism for resource isolation and organization
**Explanation:** Namespaces in Kubernetes provide a way to logically separate and isolate resources within a cluster, enabling multiple teams or projects to share the same cluster without resource conflicts. They help organize cluster resources and apply resource quotas or policies per namespace. Namespaces do not directly improve application performance, simplify container images, automatically scale applications, or replace Pods, which are fundamental units of deployment in Kubernetes.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Official Documentation - Namespaces</a><br><a href="https://www.cncf.io/blog/2020/06/09/kubernetes-namespaces-demystified/" target="_blank">CNCF - Kubernetes Basics: Namespaces</a>

---
