# CKS - Certified Kubernetes Security Specialist — Cluster Hardening

> Deck: `CKS - Certified Kubernetes Security Specialist` · Group: `Cluster Hardening` · Notes: 133 · Models: Basic+

<!-- note:1772498091431 model:Basic+ -->
**Front:** What are the two main types of Kubernetes API groups?
**Back:** 1. Core API Group (essential cluster resources like pods, namespaces, services)
2. Named API Group (organizes newer features like apps, networking, storage)
**Tags:** ankidote api-group-types kubernetes-api-groups

---

<!-- note:1772498091433 model:Basic+ -->
**Front:** What verbs are supported by Kubernetes API resources?
**Back:** list, get, create, delete, update, watch
**Tags:** ankidote api-verbs kubernetes-api

---

<!-- note:1772498091434 model:Basic+ -->
**Front:** How do you list available API groups directly from the Kubernetes API server?
**Back:** Use curl http://localhost:6443 to retrieve paths like /api, /apis, /healthz, etc.
**Tags:** ankidote api-groups kubernetes-api-server

---

<!-- note:1772498091436 model:Basic+ -->
**Front:** What is the difference between kube proxy and kubectl proxy?
**Back:** "Kube proxy" manages pod-to-service communication; "kubectl proxy" is an HTTP proxy for secure API access using kubeconfig credentials
**Tags:** ankidote api-access kube-proxy kubectl-proxy

---

<!-- note:1772498091438 model:Basic+ -->
**Front:** What endpoint shows the Kubernetes cluster version?
**Back:** https://kube-master:6443/version (returns major/minor version and git details)
**Tags:** ankidote api-endpoints cluster-version

---

<!-- note:1772498091439 model:Basic+ -->
**Front:** Which API group contains core resources like pods and namespaces?
**Back:** Core API Group (default group at /api/v1)
**Tags:** ankidote core-api-group kubernetes-api

---

<!-- note:1772498091440 model:Basic+ -->
**Front:** What is the purpose of the /metrics endpoint?
**Back:** Provides cluster health metrics for monitoring
**Tags:** ankidote api-endpoints cluster-health

---

<!-- note:1772498091441 model:Basic+ -->
**Front:** Which API group contains resources like deployments and stateful sets?
**Back:** Named API Group (specifically the "apps" sub-group)
**Tags:** ankidote kubernetes-api named-api-group

---

<!-- note:1772498091442 model:Basic+ -->
**Front:** What command starts an HTTP proxy for secure Kubernetes API access?
**Back:** kubectl proxy (uses credentials from kubeconfig file)
**Tags:** ankidote api-access kubectl-proxy

---

<!-- note:1772498091443 model:Basic+ -->
**Front:** What are the core API group resources?
**Back:** Namespaces, pods, replication controllers, events, endpoints, nodes, bindings, persistent volumes, config maps, secrets, services
**Tags:** ankidote core-api-group kubernetes-resources

---

<!-- note:1772498149305 model:Basic+ -->
**Front:** What is the purpose of static password files in Kubernetes authentication?
**Back:** Static password files provide basic authentication by storing user credentials in a CSV format. They are used by kube-apiserver to authenticate requests with username/password pairs.
**Tags:** ankidote basic-auth kubernetes-authentication static-password

---

<!-- note:1772498149319 model:Basic+ -->
**Front:** What columns are required in a static password CSV file?
**Back:** The CSV must include username, password, user ID (UID), and optional group information. Example format: password123,user1,u0001,group1
**Tags:** ankidote csv-format kubernetes-authentication static-password

---

<!-- note:1772498149321 model:Basic+ -->
**Front:** How do you configure kube-apiserver to use a static password file?
**Back:** Add the --basic-auth-file=<filename>.csv flag to the kube-apiserver command. Example: kube-apiserver --basic-auth-file=user-details.csv
**Tags:** ankidote configuration kube-apiserver static-password

---

<!-- note:1772498149322 model:Basic+ -->
**Front:** What is the difference between static password and token files?
**Back:** Static password files use username/password pairs, while token files replace the password column with a token. Both use CSV format but authenticate via different mechanisms.
**Tags:** ankidote authentication-mechanisms static-password static-token

---

<!-- note:1772498149324 model:Basic+ -->
**Front:** How do you use a token from a static token file?
**Back:** Include the token in the Authorization header with 'Bearer' prefix. Example: curl -H 'Authorization: Bearer <token>' https://apiserver/api/v1/pods
**Tags:** ankidote curl-command static-token token-auth

---

<!-- note:1772498149326 model:Basic+ -->
**Front:** What security risk is associated with static password/token files?
**Back:** Storing credentials in plain text exposes them to unauthorized access. Production environments should use certificate-based auth or third-party identity providers.
**Tags:** ankidote authentication-risks security-best-practices static-files

---

<!-- note:1772498149329 model:Basic+ -->
**Front:** How should authentication files be secured in kubeadm clusters?
**Back:** Mount authentication files as volumes with restricted access. Implement role-based authorization policies to prevent unauthorized cluster access.
**Tags:** ankidote kubeadm security volume-mounts

---

<!-- note:1772498149330 model:Basic+ -->
**Front:** What are the native authentication methods supported by Kubernetes?
**Back:** Kubernetes natively supports service account authentication via the API. External methods include static password/token files, certificates, LDAP, and Kerberos.
**Tags:** ankidote kubernetes native-authentication service-accounts

---

<!-- note:1772498176255 model:Basic+ -->
**Front:** What is the purpose of authorization in Kubernetes?
**Back:** Authorization determines which operations a user can perform within a cluster after authentication. It controls access to cluster resources and actions like creating, reading, updating, or deleting objects.
**Tags:** ankidote authorization-overview kubernetes-security

---

<!-- note:1772498176259 model:Basic+ -->
**Front:** What error occurs when a non-admin user tries to delete a node?
**Back:** Error from server (Forbidden): nodes "worker-2" is forbidden: User "developer" cannot delete resource "nodes"
**Tags:** ankidote authorization-errors rbac

---

<!-- note:1772498176262 model:Basic+ -->
**Front:** What is Node Authorization used for?
**Back:** Node Authorization is used for internal Kubernetes components like kubelets. It grants privileges to users with names prefixed by "system:node" in the "system:nodes" group.
**Tags:** ankidote internal-communication node-authorization

---

<!-- note:1772498176263 model:Basic+ -->
**Front:** What is Attribute-Based Authorization used for?
**Back:** Attribute-Based Authorization associates specific users or groups with permissions via JSON policies. It allows granular control, like letting a developer view/create pods but not modify cluster configurations.
**Tags:** ankidote attribute-based-authorization policy-management

---

<!-- note:1772498176265 model:Basic+ -->
**Front:** What is Role-Based Access Control (RBAC)?
**Back:** RBAC is a scalable authorization mechanism where roles encapsulate permissions (e.g., developer roles vs security roles). Users are assigned roles, and role updates automatically apply to all associated users.
**Tags:** ankidote rbac role-definitions

---

<!-- note:1772498176267 model:Basic+ -->
**Front:** What is Webhook-Based Authorization?
**Back:** Webhook-Based Authorization delegates authorization decisions to external systems like Open Policy Agent. The kube-apiserver forwards requests to these systems for approval or denial.
**Tags:** ankidote external-tools webhook-authorization

---

<!-- note:1772498176269 model:Basic+ -->
**Front:** What does the AlwaysAllow authorization mode do?
**Back:** AlwaysAllow permits all requests without any authorization checks. It is the default mode if not explicitly configured in kube-apiserver.
**Tags:** alwaysallow ankidote authorization-modes

---

<!-- note:1772498176271 model:Basic+ -->
**Front:** What is the order of processing multiple authorization modes?
**Back:** Requests are processed in the order specified: 1) Node authorizer (for node operations), 2) RBAC controller, 3) Webhook authorizer. If any module approves, remaining checks are skipped.
**Tags:** ankidote multi-mode-authorization processing-order

---

<!-- note:1772498176273 model:Basic+ -->
**Front:** What is the default authorization mode in kube-apiserver?
**Back:** The default authorization mode is AlwaysAllow. This allows all requests unless explicitly configured otherwise.
**Tags:** ankidote authorization-modes kube-apiserver

---

<!-- note:1772498176275 model:Basic+ -->
**Front:** What is the purpose of the policy file in Attribute-Based Authorization?
**Back:** The policy file defines JSON rules that associate users, groups, or namespaces with specific resource permissions (e.g., allowing a user to view pods across all namespaces).
**Tags:** ankidote attribute-based-authorization policy-files

---

<!-- note:1772498260536 model:Basic+ -->
**Front:** What is the difference between cluster roles and namespaced roles in Kubernetes?
**Back:** Cluster roles manage cluster-scoped resources (e.g., nodes, persistent volumes), while namespaced roles manage permissions within a specific namespace. Cluster roles apply across all namespaces.
**Tags:** ankidote cluster-roles kubernetes-rbac

---

<!-- note:1772498260538 model:Basic+ -->
**Front:** What are the two categories of Kubernetes resources?
**Back:** 1. Namespaced resources (e.g., pods, services) 2. Cluster-scoped resources (e.g., nodes, persistent volumes).
**Tags:** ankidote kubernetes-resources resource-classification

---

<!-- note:1772498260540 model:Basic+ -->
**Front:** What command lists all namespaced resources in Kubernetes?
**Back:** kubectl api-resources --namespaced=true
**Tags:** ankidote kubernetes-commands resource-classification

---

<!-- note:1772498260542 model:Basic+ -->
**Front:** What is an example YAML for a cluster role that manages nodes?
**Back:** apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: cluster-administrator
rules:
- apiGroups: [""]
  resources: ["nodes"]
  verbs: ["list", "get", "create", "delete"]
**Tags:** ankidote cluster-role yaml-example

---

<!-- note:1772498260543 model:Basic+ -->
**Front:** How do you bind a cluster role to a user?
**Back:** Create a ClusterRoleBinding YAML with:
- User subject
- Reference to the ClusterRole
Example:
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: cluster-admin-role-binding
subjects:
- kind: User
  name: cluster-admin
roleRef:
  kind: ClusterRole
  name: cluster-administrator
**Tags:** ankidote cluster-role-binding role-binding

---

<!-- note:1772498260544 model:Basic+ -->
**Front:** What command applies a cluster role and its binding?
**Back:** kubectl create -f cluster-admin-role.yaml
kubectl create -f cluster-admin-role-binding.yaml
**Tags:** ankidote kubernetes-commands role-binding

---

<!-- note:1772498260545 model:Basic+ -->
**Front:** Can cluster roles be used for namespaced resources? If so, how does it differ?
**Back:** Yes. When applied to namespaced resources, cluster roles grant permissions across all namespaces, unlike namespaced roles which are restricted to specific namespaces.
**Tags:** ankidote cluster-roles kubernetes-rbac

---

<!-- note:1772498260547 model:Basic+ -->
**Front:** What are default cluster roles created by Kubernetes?
**Back:** Kubernetes automatically creates several default cluster roles during setup. These roles may appear in practice tests and configurations.
**Tags:** ankidote default-roles kubernetes-rbac

---

<!-- note:1772498307262 model:Basic+ -->
**Front:** What is the maximum version skew allowed between kube-apiserver and other control plane components?
**Back:** The kube-apiserver must be equal to or higher than other components. Controller manager and scheduler can lag by one minor version, kubelet and kube-proxy can lag by two minor versions. Kubectl can be one minor version ahead, equal, or one behind.
**Tags:** ankidote control-plane kubernetes-upgrade versioning

---

<!-- note:1772498307266 model:Basic+ -->
**Front:** What is the recommended approach for upgrading Kubernetes clusters to minimize downtime?
**Back:** Upgrade one minor version at a time. Direct upgrades from version 1.x to 1.x+2 are not recommended. Supported versions are always the three most recent minor versions.
**Tags:** ankidote downtime kubernetes-upgrade versioning

---

<!-- note:1772498307268 model:Basic+ -->
**Front:** What happens during a master node upgrade in Kubernetes?
**Back:** The control plane components (API server, scheduler, controller manager) experience brief downtime. Management functions like kubectl access are temporarily unavailable, but worker node workloads continue serving users.
**Tags:** ankidote control-plane downtime kubernetes-upgrade

---

<!-- note:1772498307270 model:Basic+ -->
**Front:** What are the three worker node upgrade strategies?
**Back:** 1. Upgrade all worker nodes simultaneously (causes downtime)
2. Upgrade one node at a time (minimizes downtime)
3. Add new worker nodes with updated version, migrate workloads, then decommission old nodes
**Tags:** ankidote kubernetes-upgrade strategies worker-nodes

---

<!-- note:1772498307274 model:Basic+ -->
**Front:** What does the kubeadm upgrade plan command show?
**Back:** It shows current cluster version, kubeadm tool version, latest stable version in the current series, and components requiring manual upgrades after control plane upgrade (typically kubelet).
**Tags:** ankidote kubeadm kubernetes-upgrade upgrade-plan

---

<!-- note:1772498307276 model:Basic+ -->
**Front:** What is the correct sequence for upgrading from Kubernetes v1.11 to v1.13 using kubeadm?
**Back:** 1. Update kubeadm tool to target version
2. Upgrade control plane to v1.12
3. Upgrade kubelets
4. Upgrade control plane to v1.13
**Tags:** ankidote kubeadm kubernetes-upgrade upgrade-steps

---

<!-- note:1772498307279 model:Basic+ -->
**Front:** What command upgrades the control plane with kubeadm?
**Back:** kubeadm upgrade apply <target-version> (e.g., kubeadm upgrade apply v1.12.0)
**Tags:** ankidote control-plane kubeadm kubernetes-upgrade

---

<!-- note:1772498307281 model:Basic+ -->
**Front:** What is the purpose of draining a node before upgrade?
**Back:** Draining evicts pods and marks the node as unschedulable to safely prepare it for upgrade without impacting running applications.
**Tags:** ankidote kubernetes-upgrade node-drain pre-upgrade

---

<!-- note:1772498307283 model:Basic+ -->
**Front:** What command upgrades kubelet on a worker node?
**Back:** kubectl drain <node-name> (to drain), followed by apt-get upgrade kubelet and systemctl restart kubelet
**Tags:** ankidote kubelet kubernetes-upgrade worker-nodes

---

<!-- note:1772498307284 model:Basic+ -->
**Front:** What is the maximum allowed version skew between kube-apiserver and kubelet?
**Back:** Kubelet can lag by two minor versions from kube-apiserver. For example, if apiserver is v1.10, kubelet can be v1.8.
**Tags:** ankidote kubelet kubernetes-upgrade versioning

---

<!-- note:1772498377214 model:Basic+ -->
**Front:** What is the new package repository URL for Kubernetes tools?
**Back:** The new repository URL is https://pkgs.k8s.io/core/stable/v1.29/deb for Debian/Ubuntu systems.
**Tags:** ankidote kubeadm repository upgrade

---

<!-- note:1772498377217 model:Basic+ -->
**Front:** How do you check the operating system distribution on a Kubernetes node?
**Back:** Run `cat /etc/*release` to identify the OS distribution.
**Tags:** ankidote distribution kubeadm os

---

<!-- note:1772498377218 model:Basic+ -->
**Front:** What command updates the Kubernetes repository configuration for Debian/Ubuntu?
**Back:** Use `echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.29/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list`
**Tags:** ankidote kubeadm repo upgrade

---

<!-- note:1772498377221 model:Basic+ -->
**Front:** How do you determine the latest available Kubernetes version in the 1.29 series?
**Back:** Run `sudo apt-cache madison kubeadm` to list available versions.
**Tags:** ankidote kubeadm upgrade version

---

<!-- note:1772498377224 model:Basic+ -->
**Front:** What command upgrades kubeadm on the control plane node?
**Back:** Use `sudo apt-mark unhold kubeadm && sudo apt-get install -y kubeadm='1.29.3-1.1' && sudo apt-mark hold kubeadm`
**Tags:** ankidote control-plane kubeadm upgrade

---

<!-- note:1772498377225 model:Basic+ -->
**Front:** What command checks the upgrade plan for Kubernetes?
**Back:** Run `sudo kubeadm upgrade plan` to see available upgrade options.
**Tags:** ankidote kubeadm upgrade-plan

---

<!-- note:1772498377227 model:Basic+ -->
**Front:** What command applies the Kubernetes upgrade to the control plane?
**Back:** Execute `sudo kubeadm upgrade apply v1.29.3` to initiate the upgrade.
**Tags:** ankidote apply kubeadm upgrade

---

<!-- note:1772498377229 model:Basic+ -->
**Front:** What command drains a node before upgrading kubelet?
**Back:** Use `kubectl drain controlplane --ignore-daemonsets` to drain the node.
**Tags:** ankidote drain node upgrade

---

<!-- note:1772498377232 model:Basic+ -->
**Front:** How do you upgrade kubelet and kubectl on a control plane node?
**Back:** Run `sudo apt-mark unhold kubelet kubectl && sudo apt-get install -y kubelet='1.29.3-1.1' kubectl='1.29.3-1.1' && sudo apt-mark hold kubelet kubectl`
**Tags:** ankidote kubectl kubelet upgrade

---

<!-- note:1772498377234 model:Basic+ -->
**Front:** What command uncords a node after upgrading kubelet?
**Back:** Use `kubectl uncordon controlplane` to resume scheduling on the node.
**Tags:** ankidote node uncordon upgrade

---

<!-- note:1772498377235 model:Basic+ -->
**Front:** What command upgrades a worker node using kubeadm?
**Back:** Run `sudo kubeadm upgrade node` to upgrade the worker node.
**Tags:** ankidote kubeadm upgrade worker-node

---

<!-- note:1772498377237 model:Basic+ -->
**Front:** What is the final verification step after upgrading all nodes?
**Back:** Check `kubectl get nodes` to confirm all nodes show version v1.29.3.
**Tags:** ankidote kubeadm upgrade verification

---

<!-- note:1772498377240 model:Basic+ -->
**Front:** What are the key steps in upgrading a Kubernetes cluster with kubeadm?
**Back:** 1. Update package repositories to packages.k8s.io
2. Determine target version
3. Upgrade control plane
4. Drain and upgrade kubelet/kubectl
5. Repeat for worker nodes
**Tags:** ankidote kubeadm summary upgrade

---

<!-- note:1772498711389 model:Basic+ -->
**Front:** What is the purpose of kubectl proxy?
**Back:** The kubectl proxy command provides a local proxy service to securely access the Kubernetes API server and internal cluster services without manually specifying authentication credentials. It uses the kubeconfig file for authentication.
**Tags:** ankidote kubectl-proxy kubernetes-api

---

<!-- note:1772498711392 model:Basic+ -->
**Front:** What is the default port for kubectl proxy?
**Back:** The kubectl proxy runs by default on port 8001. You can verify this with: `kubectl proxy`
**Tags:** ankidote kubectl-proxy ports

---

<!-- note:1772498711394 model:Basic+ -->
**Front:** How to start kubectl proxy?
**Back:** Run the command: `kubectl proxy` to start the proxy service. It will output: `Starting to serve on 127.0.0.1:8001`
**Tags:** ankidote commands kubectl-proxy

---

<!-- note:1772498711397 model:Basic+ -->
**Front:** What does the kubectl proxy output indicate?
**Back:** The output confirms the proxy is running and listening on `127.0.0.1:8001`, forwarding requests to the Kubernetes API server using credentials from the kubeconfig file.
**Tags:** ankidote kubectl-proxy output

---

<!-- note:1772498711401 model:Basic+ -->
**Front:** How to access cluster services via kubectl proxy?
**Back:** Use the proxy to access internal services by constructing URLs like: `curl http://localhost:8001/api/v1/namespaces/default/services/nginx/proxy/`
**Tags:** ankidote kubectl-proxy services

---

<!-- note:1772498711404 model:Basic+ -->
**Front:** What is the command to port-forward a service?
**Back:** Use `kubectl port-forward service/nginx 28080:80` to forward local port 28080 to the service's port 80. Access it with: `curl http://localhost:28080/`
**Tags:** ankidote commands port-forwarding

---

<!-- note:1772498711407 model:Basic+ -->
**Front:** How does port-forwarding work?
**Back:** Port forwarding maps a local port to a port on a cluster service, pod, or resource. It provides secure, direct access to remote services as if they were running locally.
**Tags:** ankidote mechanism port-forwarding

---

<!-- note:1772498711410 model:Basic+ -->
**Front:** What is the benefit of using port-forwarding?
**Back:** Port forwarding allows secure, direct access to remote cluster services without exposing them externally. It is ideal for testing and troubleshooting.
**Tags:** ankidote port-forwarding security

---

<!-- note:1772498711412 model:Basic+ -->
**Front:** What is the purpose of kubectl port-forward?
**Back:** The kubectl port-forward command enables local access to remote cluster resources by forwarding traffic from a local port to a service, pod, or API endpoint.
**Tags:** ankidote kubernetes port-forwarding

---

<!-- note:1772498711415 model:Basic+ -->
**Front:** What happens when using curl with the Kubernetes API directly?
**Back:** Curling the API server directly (e.g., `curl http://<kube-api-server-ip>:6443 -k`) returns a 403 Forbidden error because no authentication credentials are provided.
**Tags:** ankidote authentication kubectl-proxy

---

<!-- note:1772498755164 model:Basic+ -->
**Front:** What security risk arises if an impersonator masquerades as the master in Kubelet communication?
**Back:** It could expose sensitive information about cargo (container details, quantity, destination).
**Tags:** ankidote authentication kubelet-security

---

<!-- note:1772498755167 model:Basic+ -->
**Front:** How is the Kubelet typically installed manually on worker nodes?
**Back:** Download the binary using wget and configure it via a service file with ExecStart flags.
**Tags:** ankidote configuration kubelet-installation

---

<!-- note:1772498755170 model:Basic+ -->
**Front:** What are the two main ports used by Kubelet and their access levels?
**Back:** Port 10250 provides full API access; port 10255 offers unauthenticated read-only access.
**Tags:** ankidote kubelet-ports security

---

<!-- note:1772498755172 model:Basic+ -->
**Front:** How do you disable anonymous authentication for Kubelet?
**Back:** Use --anonymous-auth=false in the service file or set authentication.anonymous.enabled: false in the YAML config.
**Tags:** ankidote authentication kubelet-security

---

<!-- note:1772498755174 model:Basic+ -->
**Front:** What parameter configures certificate-based authentication for Kubelet?
**Back:** The --client-ca-file flag in the service file or clientCAFile in the YAML configuration.
**Tags:** ankidote certificate-auth kubelet-security

---

<!-- note:1772498755177 model:Basic+ -->
**Front:** What authorization mode should be used to secure Kubelet requests?
**Back:** Webhook mode, which validates requests against the API server.
**Tags:** ankidote authorization kubelet-authorization

---

<!-- note:1772498755179 model:Basic+ -->
**Front:** How do you disable the read-only port (10255) in Kubelet?
**Back:** Set --read-only-port=0 in the service file or readOnlyPort: 0 in the YAML config.
**Tags:** ankidote kubelet-configuration port-security

---

<!-- note:1772498755182 model:Basic+ -->
**Front:** What are the four key security measures for Kubelet?
**Back:** 1. Disable anonymous auth. 2. Use certificate-based auth. 3. Enable Webhook authorization. 4. Disable read-only port 10255.
**Tags:** ankidote kubelet-security summary

---

<!-- note:1772498822864 model:Basic+ -->
**Front:** What are the steps to secure cluster hosts?
**Back:** Disable root access, disable password-based authentication, enable SSH key-based authentication, and implement additional security measures for the underlying infrastructure.
**Tags:** ankidote cluster-hosts kubernetes-security

---

<!-- note:1772498822867 model:Basic+ -->
**Front:** What are the authentication methods for the Kubernetes API server?
**Back:** Static files (user/password), tokens, certificates, LDAP integration, and service accounts for machine-to-machine communication.
**Tags:** ankidote api-server authentication

---

<!-- note:1772498822869 model:Basic+ -->
**Front:** What authorization mechanisms does Kubernetes use?
**Back:** Role-Based Access Control (RBAC), Attribute-Based Access Control (ABAC), Node Authorization, and Webhook-based authorization.
**Tags:** ankidote api-server authorization

---

<!-- note:1772498822871 model:Basic+ -->
**Front:** How are intra-cluster communications secured?
**Back:** All component communications (etcd, kubelet, kube-proxy, etc.) use TLS encryption for secure data transmission.
**Tags:** ankidote intra-cluster-communications tls

---

<!-- note:1772498822872 model:Basic+ -->
**Front:** What is the purpose of network policies in Kubernetes?
**Back:** To restrict pod-to-pod communication by controlling traffic flow between pods and preventing unauthorized access.
**Tags:** ankidote network-policies pod-communication

---

<!-- note:1772498845089 model:Basic+ -->
**Front:** How do you check the Kubernetes version on each node in a cluster?
**Back:** Use the command `kubectl get nodes` to view version information for all nodes. The VERSION column shows the Kubernetes version running on each node.
**Tags:** ankidote cluster-management kubernetes-versions

---

<!-- note:1772498845092 model:Basic+ -->
**Front:** What are the components of a Kubernetes version number like v1.11.3?
**Back:** A Kubernetes version number consists of three parts: MAJOR (1), MINOR (11), and PATCH (3). Major represents the primary release series, minor introduces new features, and patch focuses on bug fixes.
**Tags:** ankidote kubernetes-architecture versioning

---

<!-- note:1772498845094 model:Basic+ -->
**Front:** What distinguishes alpha, beta, and stable Kubernetes releases?
**Back:** Alpha releases contain experimental features disabled by default. Beta releases are matured features enabled by default with thorough testing. Stable releases are production-ready and fully supported.
**Tags:** ankidote kubernetes-versions release-types

---

<!-- note:1772498845097 model:Basic+ -->
**Front:** Where can you find official Kubernetes release packages and documentation?
**Back:** Official Kubernetes releases are available on the GitHub releases page: https://github.com/kubernetes/kubernetes/releases. Each release includes executables, download links, and checksums.
**Tags:** ankidote kubernetes-resources release-channels

---

<!-- note:1772498946389 model:Basic+ -->
**Front:** What is the purpose of Role-Based Access Control (RBAC) in Kubernetes?
**Back:** RBAC enables defining roles with specific permissions and binding them to users or groups to ensure secure and controlled access within a Kubernetes cluster.
**Tags:** access-control ankidote kubernetes rbac

---

<!-- note:1772498946392 model:Basic+ -->
**Front:** What is the correct apiVersion for a Kubernetes Role?
**Back:** The apiVersion must be set to `rbac.authorization.k8s.io/v1`.
**Tags:** ankidote kubernetes rbac role-creation

---

<!-- note:1772498946396 model:Basic+ -->
**Front:** What YAML fields are required to define a Role in Kubernetes?
**Back:** The required fields are `apiVersion`, `kind`, `metadata.name`, and `rules`.
**Tags:** ankidote kubernetes rbac role-creation

---

<!-- note:1772498946398 model:Basic+ -->
**Front:** What command creates a Role from a YAML file?
**Back:** Use `kubectl create -f <filename>.yaml` to apply the Role definition.
**Tags:** ankidote kubernetes rbac role-creation

---

<!-- note:1772498946401 model:Basic+ -->
**Front:** What is the purpose of a RoleBinding in Kubernetes?
**Back:** A RoleBinding links a user, group, or service account to a Role, granting them the defined permissions.
**Tags:** ankidote kubernetes rbac role-binding

---

<!-- note:1772498946404 model:Basic+ -->
**Front:** What YAML fields are required for a RoleBinding?
**Back:** The required fields are `metadata.name`, `subjects`, and `roleRef`.
**Tags:** ankidote kubernetes rbac role-binding

---

<!-- note:1772498946406 model:Basic+ -->
**Front:** How do you verify a Role was created successfully?
**Back:** Run `kubectl get roles` to list all roles in the current namespace.
**Tags:** ankidote kubernetes rbac verification

---

<!-- note:1772498946409 model:Basic+ -->
**Front:** What command checks if a user can perform an action?
**Back:** Use `kubectl auth can-i <verb> <resource>` to check permissions.
**Tags:** ankidote kubernetes permission-check rbac

---

<!-- note:1772498946415 model:Basic+ -->
**Front:** How do you check permissions for a different user without switching accounts?
**Back:** Use the `--as` flag, e.g., `kubectl auth can-i <action> --as=<username>`.
**Tags:** ankidote kubernetes permission-check rbac

---

<!-- note:1772498946418 model:Basic+ -->
**Front:** How do you restrict a role to specific resources in Kubernetes?
**Back:** Add the `resourceNames` field to the Role's rules, specifying the exact resource names.
**Tags:** ankidote kubernetes rbac resource-restriction

---

<!-- note:1772498946421 model:Basic+ -->
**Front:** What is the purpose of the `resourceNames` field in RBAC rules?
**Back:** The `resourceNames` field limits permissions to specific resources (e.g., pods named 'blue' and 'orange').
**Tags:** ankidote kubernetes rbac resource-restriction

---

<!-- note:1772498946424 model:Basic+ -->
**Front:** What command describes a Role's detailed permissions?
**Back:** Use `kubectl describe role <name>` to view allowed resources and verbs.
**Tags:** ankidote kubernetes rbac verification

---

<!-- note:1772498946428 model:Basic+ -->
**Front:** What is the default namespace for a Role if not specified?
**Back:** Roles are namespaced and created in the default namespace unless explicitly specified in metadata.
**Tags:** ankidote kubernetes namespaces rbac

---

<!-- note:1772499116361 model:Basic+ -->
**Front:** What are the two types of accounts in Kubernetes?
**Back:** User Account (for humans) and Service Account (for applications/machines).
**Tags:** account-types ankidote kubernetes-service-accounts

---

<!-- note:1772499116364 model:Basic+ -->
**Front:** What command creates a service account named 'dashboard-sa'?
**Back:** kubectl create serviceaccount dashboard-sa
**Tags:** ankidote kubectl-commands service-account-creation

---

<!-- note:1772499116367 model:Basic+ -->
**Front:** Where is the service account token stored?
**Back:** As a Secret object with a name like 'dashboard-sa-token-<random-string>'.
**Tags:** ankidote secret-storage service-account-token

---

<!-- note:1772499116370 model:Basic+ -->
**Front:** What happens if a pod doesn't specify a service account?
**Back:** Kubernetes automatically uses the default service account in the namespace.
**Tags:** ankidote default-service-account pod-configuration

---

<!-- note:1772499116373 model:Basic+ -->
**Front:** What security improvements did Kubernetes v1.22 introduce for service accounts?
**Back:** Tokens are now audience-bound, time-bound, and object-bound with the token request API.
**Tags:** ankidote kubernetes-versions token-request-api

---

<!-- note:1772499116375 model:Basic+ -->
**Front:** What command generates a service account token in Kubernetes v1.24+?
**Back:** kubectl create token <service-account-name>
**Tags:** ankidote kubernetes-1.24 token-generation

---

<!-- note:1772499116378 model:Basic+ -->
**Front:** How are service account tokens mounted in Kubernetes v1.22+?
**Back:** As projected volumes that dynamically interact with the token controller API.
**Tags:** ankidote projected-volume token-mounting

---

<!-- note:1772499116380 model:Basic+ -->
**Front:** What security risks are associated with non-expiring service account tokens?
**Back:** Indefinite validity increases risk of token misuse and exposure to attackers.
**Tags:** ankidote security-risks token-expiration

---

<!-- note:1772499116383 model:Basic+ -->
**Front:** How to create a non-expiring token manually in Kubernetes?
**Back:** Create a Secret with type 'kubernetes.io/service-account-token' and annotation 'kubernetes.io/service-account.name: <sa-name>'.
**Tags:** ankidote manual-secret-creation token-security

---

<!-- note:1772499406488 model:Basic+ -->
**Front:** What is API Priority and Fairness in Kubernetes?
**Back:** API Priority and Fairness ensures critical API requests (e.g., namespace creation, deployment updates) receive higher priority in multi-tenant clusters. It manages concurrency and queuing for API operations to prevent lower-priority traffic from delaying essential operations.
**Tags:** ankidote api-priority fairness kubernetes

---

<!-- note:1772499406491 model:Basic+ -->
**Front:** How do you configure PriorityLevelConfiguration for API priority?
**Back:** Define PriorityLevelConfiguration using `flowcontrol.apiserver.k8s.io/v1beta3` API, specifying `assuredConcurrencyShares` (higher for critical) and `limitResponse` (e.g., Queue). Example:
```yaml
apiVersion: flowcontrol.apiserver.k8s.io/v1beta3
kind: PriorityLevelConfiguration
metadata: name: high-priority
spec: type: Limited
  limited: assuredConcurrencyShares: 10
  limitResponse: type: Queue
```
**Tags:** ankidote api-priority kubernetes priority-level

---

<!-- note:1772499406493 model:Basic+ -->
**Front:** What is the purpose of FlowSchema in API priority configuration?
**Back:** FlowSchema maps priority levels to specific tenant requests by defining rules (e.g., matching ServiceAccounts, namespaces) and linking to PriorityLevelConfigurations. It ensures critical namespaces (like Tenant A) get higher precedence.
**Tags:** ankidote api-priority flowschema kubernetes

---

<!-- note:1772499406494 model:Basic+ -->
**Front:** How does assuredConcurrencyShares affect API priority?
**Back:** Higher `assuredConcurrencyShares` (e.g., 10 for high-priority) guarantees more API concurrency slots, ensuring critical requests are processed faster. Lower values (e.g., 1 for low-priority) limit resource allocation for non-critical traffic.
**Tags:** ankidote api-priority concurrency kubernetes

---

<!-- note:1772499406496 model:Basic+ -->
**Front:** What is Pod Priority and Preemption in Kubernetes?
**Back:** Pod Priority and Preemption manage node resource allocation by prioritizing critical pods. When resources are strained, lower-priority pods are preempted or evicted to ensure critical workloads (e.g., production databases) maintain required resources.
**Tags:** ankidote kubernetes pod-priority preemption

---

<!-- note:1772499406497 model:Basic+ -->
**Front:** How do you define PriorityClasses for Pod Priority?
**Back:** Create PriorityClass objects with `value` (higher for critical) and `globalDefault` (false unless default). Example:
```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata: name: high-priority
value: 1000
description: Critical production workloads.
```
**Tags:** ankidote kubernetes pod-priority priorityclass

---

<!-- note:1772499406500 model:Basic+ -->
**Front:** What role does priorityClassName play in Pod specifications?
**Back:** The `priorityClassName` field in a Pod's spec assigns it to a PriorityClass, ensuring it receives scheduling preferences during resource contention. Critical pods (e.g., in namespace A) use high-priority classes to avoid eviction.
**Tags:** ankidote kubernetes pod-priority priorityclass

---

<!-- note:1772499406503 model:Basic+ -->
**Front:** How do API Priority and Pod Priority differ?
**Back:** API Priority manages Kubernetes API request flow (e.g., namespace creation), while Pod Priority handles node-level resource allocation for pods. They are distinct mechanisms and cannot replace each other in multi-tenant clusters.
**Tags:** ankidote api-priority comparison pod-priority

---

<!-- note:1772499406506 model:Basic+ -->
**Front:** Why are both API Priority and Pod Priority essential in multi-tenant clusters?
**Back:** API Priority ensures critical control plane operations aren't stalled by low-priority traffic, while Pod Priority guarantees critical workloads receive resources during node-level contention. Together, they maintain cluster stability and service quality.
**Tags:** ankidote api-priority multi-tenant pod-priority

---

<!-- note:1772499406508 model:Basic+ -->
**Front:** What is the purpose of the `matchingPrecedence` field in FlowSchema?
**Back:** The `matchingPrecedence` value (e.g., 1000 for high-priority) determines which FlowSchema rules take priority when multiple rules could apply. Higher values ensure critical namespaces (like Tenant A) are prioritized over others.
**Tags:** ankidote api-priority flowschema kubernetes

---

<!-- note:1772507707611 model:Basic+ -->
**Front:** What command generates the CA private key for Kubernetes certificate creation?
**Back:** openssl genrsa -out ca.key 2048
**Tags:** ankidote ca-certificate kubernetes openssl tls

---

<!-- note:1772507707615 model:Basic+ -->
**Front:** What is the common name used in the CA certificate signing request?
**Back:** KUBERNETES-CA
**Tags:** ankidote ca-certificate certificate-creation kubernetes tls

---

<!-- note:1772507707618 model:Basic+ -->
**Front:** What command signs the admin user certificate using the CA?
**Back:** openssl x509 -req -in admin.csr -CA ca.crt -CAkey ca.key -out admin.crt
**Tags:** ankidote client-certificate kubernetes openssl tls

---

<!-- note:1772507707622 model:Basic+ -->
**Front:** What additional parameter grants admin privileges in a client certificate?
**Back:** Organizational Unit (OU) like 'system:masters'
**Tags:** ankidote client-certificate kubernetes rbac tls

---

<!-- note:1772507707626 model:Basic+ -->
**Front:** What command creates a certificate with Subject Alternative Names (SAN) for the kube API server?
**Back:** openssl req -new -key apiserver.key -subj "/CN=kube-apiserver" -out apiserver.csr
**Tags:** ankidote kubernetes openssl san tls

---

<!-- note:1772507707628 model:Basic+ -->
**Front:** What file defines Subject Alternative Names (SAN) for the kube API server certificate?
**Back:** openssl.cnf (contains DNS and IP entries)
**Tags:** ankidote kubernetes openssl san tls

---

<!-- note:1772507707632 model:Basic+ -->
**Front:** What are the three key components of the kubelet configuration for TLS?
**Back:** ClientCAFile, TLS certificate file, TLS private key file
**Tags:** ankidote configuration kubelet kubernetes tls

---

<!-- note:1772507707635 model:Basic+ -->
**Front:** What command configures the etcd server to use its certificate files?
**Back:** cat etcd.yaml (shows --cert-file, --key-file, --peer-cert-file parameters)
**Tags:** ankidote configuration etcd kubernetes tls

---

<!-- note:1772507707638 model:Basic+ -->
**Front:** What is the purpose of mutual trust between clients and servers in Kubernetes?
**Back:** Ensures certificates are signed by a shared CA root certificate for secure communication
**Tags:** ankidote ca-certificate kubernetes mutual-trust tls

---

<!-- note:1772507707643 model:Basic+ -->
**Front:** What file consolidates API server endpoint and certificate parameters in Kubernetes?
**Back:** KubeConfig file
**Tags:** ankidote certificate-parameters kubeconfig kubernetes tls

---

<!-- note:1772507707646 model:Basic+ -->
**Front:** What command validates a certificate connection to the kube API server?
**Back:** curl https://kube-apiserver:6443/api/v1/pods --key admin.key --cert admin.crt --cacert ca.crt
**Tags:** ankidote certificate-validation curl kubernetes tls

---

<!-- note:1772507707649 model:Basic+ -->
**Front:** What are the three types of certificates created in Kubernetes certificate creation?
**Back:** CA certificate, client certificate, server certificate
**Tags:** ankidote certificate-types kubernetes openssl tls

---

<!-- note:1772507707652 model:Basic+ -->
**Front:** What parameter in the kubelet configuration specifies the CA file for authentication?
**Back:** clientCAFile
**Tags:** ankidote configuration kubelet kubernetes tls

---

<!-- note:1772507707657 model:Basic+ -->
**Front:** What is the naming convention for node-specific kubelet certificates?
**Back:** system:node:<node-name>
**Tags:** ankidote kubelet kubernetes naming-convention tls

---

<!-- note:1772507707659 model:Basic+ -->
**Front:** What command generates a certificate for the etcd peer communication?
**Back:** openssl req -new -key etcdpeer.key -subj "/CN=etcd-peer" -out etcdpeer.csr
**Tags:** ankidote etcd kubernetes peer-certificate tls

---
