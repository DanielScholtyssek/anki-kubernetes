# KCSA - Kubernetes and Cloud Native Security Associate — Kubernetes Cluster Component Security

> Deck: `KCSA - Kubernetes and Cloud Native Security Associate` · Group: `Kubernetes Cluster Component Security` · Notes: 89 · Models: Many

<!-- note:1772101854878 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which Kubernetes admission controller runs first during the admission control process?
**Options:** A. ValidatingAdmissionWebhook<br>B. MutatingAdmissionWebhook<br>C. ResourceQuota<br>D. NamespaceLifecycle<br>E. AlwaysPullImages
**Answer:** B (2) – MutatingAdmissionWebhook
**Explanation:** The MutatingAdmissionWebhook runs first in the Kubernetes admission control process. This is because mutating admission controllers are designed to modify the incoming request before it is validated by validating admission controllers. Other options, such as ValidatingAdmissionWebhook, ResourceQuota, NamespaceLifecycle, and AlwaysPullImages, either run later in the process or serve different purposes.
**Sources:** <a href="https://kubernetes.io/blog/2019/03/21/a-guide-to-kubernetes-admission-controllers/" target="_blank">Kubernetes Official Documentation - Admission Controllers</a><br><a href="https://www.styra.com/blog/what-is-kubernetes-admission-control/" target="_blank">Styra Blog - What Is Kubernetes Admission Control?</a>

---

<!-- note:1772101854881 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the recommended method to restrict access to the Kubernetes kubelet API securely?
**Options:** A. Disable the kubelet service entirely<br>B. Configure kubelet with '--authorization-mode=Webhook' and '--authentication-token-webhook=true' flags<br>C. Remove the kubelet binary from all nodes<br>D. Access kubelet only via SSH tunnels<br>E. Set '--allow-privileged=false' to restrict privileged containers
**Answer:** B (2) – Configure kubelet with '--authorization-mode=Webhook' and '--authentication-token-webhook=true' flags
**Explanation:** The kubelet API should be secured by enabling authentication and authorization mechanisms. Using the '--authorization-mode=Webhook' flag enables authorization via an external webhook, typically the API server, while '--authentication-token-webhook=true' enables token-based authentication against the API server. This combination ensures that only authenticated and authorized requests can access the kubelet API. Disabling the kubelet or removing it is impractical as it is essential for node management. Accessing kubelet only via SSH does not inherently secure the API itself. Setting '--allow-privileged=false' restricts privileged containers but does not control API access.
**Sources:** <a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet-authentication-authorization/" target="_blank">Kubernetes Official Documentation - Kubelet Authentication and Authorization</a><br><a href="https://github.com/cncf/sig-security/blob/main/security-best-practices/kubelet.md" target="_blank">CNCF Kubernetes Security Best Practices</a>

---

<!-- note:1772101854889 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** How can you update the container image of a Kubernetes deployment without modifying other deployment configurations?
**Options:** A. Manually edit the deployment YAML file and apply changes<br>B. Delete the existing deployment and recreate it with the new image<br>C. Use the 'kubectl set image' command to update the image<br>D. Scale the deployment down to zero replicas, update the image, then scale back up<br>E. Update the image directly in the container registry
**Answer:** C (3) – Use the 'kubectl set image' command to update the image
**Explanation:** The 'kubectl set image' command allows you to update the container image of a deployment directly without changing other configuration parameters. This command triggers a rolling update, ensuring minimal downtime. Manually editing the YAML is error-prone and may unintentionally alter other settings. Deleting and recreating the deployment causes downtime and loss of state. Scaling down to zero is unnecessary and disruptive. Updating the image in the container registry alone does not affect running deployments.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#updating-a-deployment" target="_blank">Kubernetes Official Documentation - Updating a Deployment</a><br><a href="https://kubernetes.io/docs/reference/kubectl/cheatsheet/#updating-resources" target="_blank">Kubernetes kubectl Cheat Sheet</a>

---

<!-- note:1772101854893 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** How do you configure Kubernetes to use a specific container runtime, such as containerd, on a node?
**Options:** A. Specify the container runtime in the pod specification<br>B. Set the '--container-runtime-endpoint' flag in the kubelet configuration<br>C. Configure the container runtime in the kube-proxy settings<br>D. Rely on automatic detection; no manual configuration is required<br>E. Set an environment variable on the master node to specify the runtime
**Answer:** B (2) – Set the '--container-runtime-endpoint' flag in the kubelet configuration
**Explanation:** The kubelet is responsible for managing the container runtime on each node. To specify a container runtime like containerd, you configure the kubelet with the '--container-runtime-endpoint' flag, which points to the runtime's socket endpoint. This setting ensures kubelet communicates with the correct container runtime. The pod specification does not control the runtime used by the node. Kube-proxy manages networking and is unrelated to container runtimes. Automatic detection is not reliable for runtime selection. Environment variables on the master node do not affect node-level runtime configuration.
**Sources:** <a href="https://kubernetes.io/docs/setup/production-environment/container-runtimes/" target="_blank">Kubernetes Official Documentation - Container Runtimes</a><br><a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/" target="_blank">Kubernetes Official Documentation - Kubelet Configuration</a>

---

<!-- note:1772101854897 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which of the following best practices are recommended to secure the Kubernetes scheduler (kube-scheduler)? (Select all that apply.)
**Options:** A. Bind the scheduler to 0.0.0.0 to ensure it is accessible from all network interfaces<br>B. Use Role-Based Access Control (RBAC) to restrict access to the scheduler API<br>C. Run the scheduler as a non-root user to minimize privilege escalation risks<br>D. Enable anonymous authentication to simplify access for debugging purposes<br>E. Configure network policies to restrict network access to and from the scheduler
**Answer:** B, C, E – RBAC to restrict scheduler API access; run as non-root; network policies to restrict traffic
**Explanation:** The recommended security measures for securing the kube-scheduler include: using Role-Based Access Control (RBAC) to enforce least privilege, ensuring only authorized entities can interact with the scheduler's API; running the kube-scheduler as a non-root user to reduce potential risks of privilege escalation in case of a compromise; and configuring network policies to restrict unauthorized network access to or from the kube-scheduler, thereby enhancing its security. Binding the scheduler to 0.0.0.0 increases exposure and is not recommended. Similarly, enabling anonymous authentication weakens security by allowing unauthenticated access.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/overview/" target="_blank">Kubernetes Documentation - Security Overview</a><br><a href="https://www.redhat.com/en/blog/12-kubernetes-configuration-best-practices" target="_blank">Red Hat Blog - Kubernetes Configuration Best Practices</a><br><a href="https://www.getambassador.io/blog/kubernetes-rbac-role-based-access-control" target="_blank">Kubernetes RBAC Best Practices</a>

---

<!-- note:1772101854898 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which of the following controllers are included in the Kubernetes kube-controller-manager? (Select all that apply)
**Options:** A. Node Controller<br>B. ReplicaSet Controller<br>C. Ingress Controller<br>D. Cloud Controller Manager<br>E. Service Account Controller
**Answer:** A, B, E – Node, ReplicaSet, and ServiceAccount controllers (Ingress is an add-on; Cloud Controller Manager is separate)
**Explanation:** The kube-controller-manager runs several core controllers including the Node Controller, which manages node status; the ReplicaSet Controller, which ensures the desired number of pod replicas; and the Service Account Controller, which manages service account tokens. The Ingress Controller is typically deployed separately as an add-on and is not part of the kube-controller-manager. The Cloud Controller Manager is a separate component responsible for cloud-specific control loops and is not included in the kube-controller-manager.
**Sources:** <a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/" target="_blank">Kubernetes Official Documentation - Controller Manager</a><br><a href="https://kubernetes.io/docs/concepts/architecture/controller/" target="_blank">Kubernetes Official Documentation - Controllers</a>

---

<!-- note:1772101854901 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which of the following actions can improve the security of the Kubernetes kubelet? (Select all that apply)
**Options:** A. Enable authentication and authorization on the kubelet API<br>B. Disable anonymous access to the kubelet<br>C. Expose the kubelet read-only port to all network interfaces<br>D. Use TLS certificates for kubelet communication<br>E. Run the kubelet process in privileged mode
**Answer:** A, B, D – kubelet API authn/authz, disable anonymous access, TLS for kubelet communication
**Explanation:** Improving kubelet security involves enabling authentication and authorization to ensure only authorized users can access the API, disabling anonymous access to prevent unauthenticated requests, and using TLS certificates to encrypt communication between components. Exposing the read-only port publicly increases attack surface and is discouraged. Running kubelet in privileged mode is not a security best practice and can increase risk.
**Sources:** <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubelet-authentication-authorization/" target="_blank">Kubernetes Official Documentation - Securing the Kubelet</a><br><a href="https://github.com/cncf/sig-security/blob/main/security-best-practices/kubelet.md" target="_blank">CNCF Kubernetes Security Best Practices</a>

---

<!-- note:1772101854905 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which directories on a client machine contain sensitive information related to accessing Kubernetes clusters? (Select all that apply)
**Options:** A. /var/log/<br>B. ~/.kube/config<br>C. /etc/hosts<br>D. ~/.ssh/<br>E. /tmp/
**Answer:** B, D – ~/.kube/config and ~/.ssh/
**Explanation:** The ~/.kube/config file stores Kubernetes cluster access credentials and configuration, making it sensitive. The ~/.ssh/ directory contains SSH keys used for secure access to nodes or clusters. Other directories like /var/log/, /etc/hosts, and /tmp/ do not typically contain sensitive Kubernetes access information.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/" target="_blank">Kubernetes Official Documentation - Configure Access to Multiple Clusters</a><br><a href="https://www.redhat.com/sysadmin/kubernetes-security-best-practices" target="_blank">Kubernetes Security Best Practices - SSH Key Management</a>

---

<!-- note:1772101854907 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** In managed Kubernetes services (e.g., EKS, GKE, AKS), who is responsible for managing the etcd cluster?
**Options:** A. The user manages etcd directly<br>B. The cloud provider manages etcd<br>C. etcd is not used in managed services<br>D. A third-party vendor manages etcd<br>E. The Kubernetes community manages etcd
**Answer:** B (2) – The cloud provider manages etcd
**Explanation:** In managed Kubernetes services, the cloud provider is responsible for managing the etcd cluster, including backups, scaling, and availability. Users do not manage etcd directly. etcd is a core component of Kubernetes and is always used, but its management is abstracted away in managed services. The Kubernetes community develops etcd but does not manage individual clusters.
**Sources:** <a href="https://docs.aws.amazon.com/eks/latest/userguide/cluster-architecture.html" target="_blank">Amazon EKS Documentation - Cluster Architecture</a><br><a href="https://cloud.google.com/kubernetes-engine/docs/concepts/control-plane" target="_blank">Google Kubernetes Engine Documentation - Control Plane</a>

---

<!-- note:1772101854908 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What types of data are stored inside the etcd key-value store in a Kubernetes cluster? (Select all that apply)
**Options:** A. Kubernetes cluster state<br>B. Persistent application data<br>C. Pod logs<br>D. Secrets and ConfigMaps<br>E. Container images
**Answer:** A, D – cluster state, including Secrets and ConfigMaps
**Explanation:** etcd stores the entire Kubernetes cluster state, including resource objects such as Secrets and ConfigMaps. It does not store persistent application data (which is stored in volumes), pod logs (which are stored on nodes or centralized logging systems), or container images (stored in container registries).
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/components/#etcd" target="_blank">Kubernetes Official Documentation - etcd</a><br><a href="https://etcd.io/docs/v3.5/what-is-etcd/" target="_blank">CoreOS etcd Documentation - What is etcd?</a>

---

<!-- note:1772101854912 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which of the following statements about static pods in Kubernetes are true? (Select all that apply)
**Options:** A. They are managed directly by the kubelet on a node<br>B. They are defined in the API server and stored in etcd<br>C. They are useful for running critical system components<br>D. They are automatically rescheduled on other nodes if the node fails<br>E. They can be updated using kubectl commands
**Answer:** A, C – managed by kubelet on the node; useful for critical system components
**Explanation:** Static pods are defined by placing pod manifest files directly on a node’s filesystem and are managed by the kubelet on that node, not through the API server or etcd. They are useful for running critical system components that must run on a specific node. Static pods are not rescheduled automatically if the node fails, and they cannot be updated via kubectl since they are not managed through the Kubernetes API.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/" target="_blank">Kubernetes Official Documentation - Static Pods</a><br><a href="https://kubernetes.io/blog/2016/07/static-pods/" target="_blank">Kubernetes Blog - Understanding Static Pods</a>

---

<!-- note:1772101854913 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** When you run the command 'kubectl apply', which Kubernetes component processes the request first?
**Options:** A. etcd<br>B. kube-scheduler<br>C. kube-controller-manager<br>D. kube-apiserver<br>E. kubelet
**Answer:** D (4) – kube-apiserver
**Explanation:** All kubectl commands interact first with the kube-apiserver, which is the central management entity of the Kubernetes control plane. The API server authenticates and validates the request, then persists the desired state in etcd. Other components like the scheduler and controller manager act later based on the updated state.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/overview/" target="_blank">Kubernetes Official Documentation - kubectl Overview</a><br><a href="https://kubernetes.io/docs/concepts/overview/components/#kube-apiserver" target="_blank">Kubernetes Architecture - Control Plane Components</a>

---

<!-- note:1772101854914 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the primary function of the Kubernetes scheduler in a cluster?
**Options:** A. To monitor the overall health of the cluster<br>B. To assign pods to nodes based on resource availability and scheduling policies<br>C. To manage service discovery within the cluster<br>D. To enforce network policies between pods<br>E. To control user access to the Kubernetes API server
**Answer:** B (2) – To assign pods to nodes based on resource availability and scheduling policies
**Explanation:** The Kubernetes scheduler is responsible for selecting the most suitable node for each pod to run on, based on resource availability, constraints, and scheduling policies. It does not monitor cluster health, manage service discovery, enforce network policies, or control API server access. Those responsibilities belong to other components like the kube-controller-manager, CoreDNS, network plugins, and the API server's authentication/authorization mechanisms.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/" target="_blank">Kubernetes Official Documentation - Scheduler</a><br><a href="https://kubernetes.io/docs/concepts/overview/components/" target="_blank">Kubernetes Architecture Overview</a>

---

<!-- note:1772101854915 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the impact on a Kubernetes cluster if the kube-proxy component enters a 'CrashLoopBackOff' state?
**Options:** A. Pods will not be scheduled on any nodes<br>B. Network traffic between services may be disrupted or fail<br>C. The entire Kubernetes cluster will shut down<br>D. The kubelet service on nodes will stop functioning<br>E. Access to Kubernetes Secrets will be blocked
**Answer:** B (2) – Network traffic between services may be disrupted or fail
**Explanation:** kube-proxy manages network rules on each node to enable service communication and load balancing. If kube-proxy crashes repeatedly (CrashLoopBackOff), network traffic between services can be disrupted, causing failures in service discovery and connectivity. However, pod scheduling, kubelet operation, cluster availability, and secret access are not directly affected by kube-proxy failures.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies" target="_blank">Kubernetes Official Documentation - kube-proxy</a><br><a href="https://kubernetes.io/docs/concepts/cluster-administration/networking/" target="_blank">Kubernetes Networking Concepts</a>

---

<!-- note:1772101854924 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the role of the Service Account Controller in Kubernetes?
**Options:** A. Manages the creation and lifecycle of service accounts and their associated authentication tokens<br>B. Controls access permissions to external services from the cluster<br>C. Assigns network policies to service accounts for traffic control<br>D. Manages the lifecycle and scaling of Kubernetes services<br>E. Handles automatic scaling of deployments based on load
**Answer:** A (1) – Manages the creation and lifecycle of service accounts and their associated authentication tokens
**Explanation:** The Service Account Controller, part of the kube-controller-manager, is responsible for creating service accounts and generating the associated authentication tokens used by pods to interact securely with the Kubernetes API. It does not control external service access, assign network policies, manage service lifecycles, or handle deployment scaling.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/" target="_blank">Kubernetes Official Documentation - Service Accounts</a><br><a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/" target="_blank">Kubernetes Controller Manager Overview</a>

---

<!-- note:1772101854925 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which of the following controllers is NOT managed by the kube-controller-manager in Kubernetes?
**Options:** A. Node Controller<br>B. Endpoint Controller<br>C. Ingress Controller<br>D. Deployment Controller<br>E. Service Account Controller
**Answer:** C (3) – Ingress Controller
**Explanation:** The Ingress Controller is not part of the kube-controller-manager; it is typically deployed separately as a pod or set of pods to manage external HTTP/S traffic routing. The kube-controller-manager manages controllers such as Node, Endpoint, Deployment, and Service Account Controllers internally.
**Sources:** <a href="https://kubernetes.io/docs/concepts/architecture/controller/" target="_blank">Kubernetes Official Documentation - Controllers</a><br><a href="https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/" target="_blank">Kubernetes Ingress Controllers</a>

---

<!-- note:1772101854926 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which of the following are best practices for securing etcd in a Kubernetes cluster? (Select all that apply)
**Options:** A. Enable TLS encryption for all communication with etcd<br>B. Limit access to etcd endpoints to trusted networks only<br>C. Use authentication and authorization mechanisms for etcd access<br>D. Expose etcd endpoints publicly to facilitate monitoring<br>E. Store etcd backups in a secure and access-controlled location
**Answer:** A, B, C, E – TLS, trusted-network restriction, authn/authz, and secure backups
**Explanation:** Securing etcd is critical as it stores the cluster state and sensitive data. Best practices include enabling TLS encryption to protect data in transit, restricting access to trusted networks to prevent unauthorized access, implementing authentication and authorization to control who can access etcd, and securely storing backups to prevent data loss or compromise. Exposing etcd endpoints publicly is strongly discouraged as it poses a significant security risk.
**Sources:** <a href="https://kubernetes.io/docs/tasks/administer-cluster/securing-a-cluster/#securing-etcd" target="_blank">Kubernetes Official Documentation - Securing etcd</a><br><a href="https://etcd.io/docs/v3.5/op-guide/security/" target="_blank">etcd Security Best Practices</a>

---

<!-- note:1772101854927 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which Kubernetes component is responsible for persisting the cluster's state?
**Options:** A. kube-scheduler<br>B. etcd<br>C. kube-controller-manager<br>D. kube-proxy<br>E. kubelet
**Answer:** B (2) – etcd
**Explanation:** etcd is a distributed key-value store that persists the Kubernetes cluster's state. It ensures that the cluster's configuration and data are consistent across all nodes.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/components/" target="_blank">Kubernetes Documentation</a><br><a href="https://etcd.io/docs/v3.5/" target="_blank">etcd Documentation</a>

---

<!-- note:1772101854929 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the effect of disabling anonymous authentication on the kubelet?
**Options:** A. Increased security by requiring authentication<br>B. Nodes cannot join the cluster<br>C. Pods fail to start<br>D. kube-proxy stops working<br>E. No effect; kubelet does not support anonymous access
**Answer:** A (1) – Increased security by requiring authentication
**Explanation:** Disabling anonymous authentication on the kubelet enhances security by ensuring that only authenticated requests are accepted. This prevents unauthorized access and reduces the risk of attacks.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/security-best-practices/" target="_blank">Kubernetes Security Best Practices</a><br><a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/" target="_blank">Kubelet Documentation</a>

---

<!-- note:1772101854933 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What does the '--anonymous-auth=false' flag do when set on the kube-apiserver?
**Options:** A. Disables anonymous requests to the API server<br>B. Disables authentication entirely<br>C. Allows all requests without authentication<br>D. Enables anonymous authentication<br>E. Forces all clients to use tokens
**Answer:** A (1) – Disables anonymous requests to the API server
**Explanation:** Setting '--anonymous-auth=false' on the kube-apiserver ensures that all requests to the API server must be authenticated. This enhances security by preventing unauthorized access.
**Sources:** <a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/" target="_blank">Kubernetes API Server Documentation</a><br><a href="https://kubernetes.io/docs/concepts/security/controlling-access/" target="_blank">Kubernetes Security Configuration</a>

---

<!-- note:1772101854945 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Is there a Kubernetes object specifically designed to limit the number of concurrent requests to the API server?
**Options:** A. ResourceQuota<br>B. LimitRange<br>C. PodDisruptionBudget<br>D. PriorityClass<br>E. There is no such object
**Answer:** E (5) – There is no such object
**Explanation:** Kubernetes does not have an object specifically for limiting concurrent API server requests. Instead, this is typically controlled through API server configuration flags.
**Sources:** <a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/" target="_blank">Kubernetes API Server Configuration</a><br><a href="https://kubernetes.io/docs/concepts/policy/resource-quotas/" target="_blank">Kubernetes Resource Management</a>

---

<!-- note:1772101854947 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the primary role of the kube-proxy component in Kubernetes?
**Options:** A. Managing network policies<br>B. Providing service discovery and routing<br>C. Scheduling pods to nodes<br>D. Storing cluster state<br>E. Monitoring node health
**Answer:** B (2) – Providing service discovery and routing
**Explanation:** kube-proxy is responsible for maintaining network rules on each node to ensure service discovery and routing. It does not manage network policies or schedule pods.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/service/" target="_blank">Kubernetes Networking Documentation</a><br><a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/" target="_blank">kube-proxy Documentation</a>

---

<!-- note:1772101854948 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What command is used to check the version of the Kubernetes API server?
**Options:** A. 'kubectl version'<br>B. 'kubectl get apiserver'<br>C. 'kube-apiserver --version'<br>D. 'kubectl cluster-info'<br>E. 'kubectl describe componentstatus'
**Answer:** A (1) – 'kubectl version'
**Explanation:** The `kubectl version` command is used to display the client and server versions of Kubernetes. This is useful for ensuring compatibility and identifying potential version mismatches.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/overview/" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/" target="_blank">Kubernetes API Server</a>

---

<!-- note:1772101854949 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the default service type in Kubernetes if not explicitly specified?
**Options:** A. ClusterIP<br>B. NodePort<br>C. LoadBalancer<br>D. ExternalName<br>E. Ingress
**Answer:** A (1) – ClusterIP
**Explanation:** If not specified, the default service type in Kubernetes is ClusterIP. This means the service is only accessible within the cluster. Other types like NodePort or LoadBalancer are used for external access.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types" target="_blank">Kubernetes Service Types</a><br><a href="https://kubernetes.io/docs/concepts/cluster-administration/networking/" target="_blank">Kubernetes Networking</a>

---

<!-- note:1772101854951 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the primary purpose of a PodDisruptionBudget in Kubernetes?
**Options:** A. To prevent pods from being evicted during maintenance<br>B. To limit the number of pods in a namespace<br>C. To allocate CPU and memory resources<br>D. To define pod scheduling constraints<br>E. To enforce network policies
**Answer:** A (1) – To prevent pods from being evicted during maintenance
**Explanation:** A PodDisruptionBudget ensures that a specified number of replicas of a pod are available at any time, preventing disruptions during maintenance or other events that might cause pod eviction.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/pods/disruptions/" target="_blank">Kubernetes PodDisruptionBudget</a><br><a href="https://kubernetes.io/docs/concepts/workloads/pods/" target="_blank">Kubernetes Pod Management</a>

---

<!-- note:1772101854953 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the main function of the kubelet in a Kubernetes node?
**Options:** A. Managing pod networking<br>B. Running containers on each node<br>C. Storing cluster configuration<br>D. Scheduling pods to nodes<br>E. Managing the control plane
**Answer:** B (2) – Running containers on each node
**Explanation:** The kubelet is responsible for running and managing containers on each node in a Kubernetes cluster. It ensures that the pods are running as expected and reports back to the control plane.
**Sources:** <a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/" target="_blank">Kubernetes Kubelet</a><br><a href="https://kubernetes.io/docs/concepts/architecture/nodes/" target="_blank">Kubernetes Node Management</a>

---

<!-- note:1772101854959 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** How does Kubernetes ensure that a Deployment maintains the desired number of replicas?
**Options:** A. Through the kube-scheduler<br>B. Using the ReplicaSet controller<br>C. Via the kubelet on each node<br>D. By the API server checking periodically<br>E. It does not ensure this automatically
**Answer:** B (2) – Using the ReplicaSet controller
**Explanation:** Kubernetes Deployments use ReplicaSets to ensure that the desired number of pod replicas is maintained. ReplicaSets automatically adjust the number of replicas if any discrepancies are detected.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/deployment/" target="_blank">Kubernetes Deployments</a><br><a href="https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/" target="_blank">Kubernetes ReplicaSets</a>

---

<!-- note:1772101854960 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which of the following is NOT a valid Kubernetes Service type?
**Options:** A. ClusterIP<br>B. NodePort<br>C. LoadBalancer<br>D. ExternalName<br>E. InternalPort
**Answer:** E (5) – InternalPort
**Explanation:** Kubernetes defines several Service types to expose applications: ClusterIP, NodePort, LoadBalancer, and ExternalName are valid types. 'InternalPort' is not a recognized Service type in Kubernetes and does not exist in the official API. ClusterIP exposes the service on a cluster-internal IP, NodePort exposes the service on each node's IP at a static port, LoadBalancer provisions an external load balancer, and ExternalName maps the service to a DNS name. Therefore, 'InternalPort' is invalid.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/service/" target="_blank">Kubernetes Official Documentation - Services</a><br><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#service-v1-core" target="_blank">Kubernetes API Reference - Service Spec</a>

---

<!-- note:1772101854961 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the purpose of the '--service-account-key-file' flag in the kube-apiserver?
**Options:** A. To specify the private key file used to sign service account tokens<br>B. To define the service account used by the API server<br>C. To store service account credentials<br>D. To encrypt service account Secrets<br>E. To disable service accounts
**Answer:** A (1) – To specify the private key file used to sign service account tokens
**Explanation:** The '--service-account-key-file' flag in the kube-apiserver specifies the path to the private key file used to sign service account tokens. This key is critical for token authentication and validation. The API server uses this key to cryptographically sign tokens issued to service accounts, ensuring their authenticity. Other options are incorrect: the flag does not define which service account the API server uses, nor does it store credentials or encrypt Secrets. It also does not disable service accounts.
**Sources:** <a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/" target="_blank">Kubernetes Official Documentation - Service Accounts</a><br><a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/" target="_blank">Kubernetes Security Best Practices - Service Accounts</a>

---

<!-- note:1772101854962 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which statement best describes the Kubernetes Ingress resource?
**Options:** A. It defines internal networking rules between pods<br>B. It manages external HTTP and HTTPS access to services<br>C. It is used for storing configuration data<br>D. It schedules pods to nodes<br>E. It provides persistent storage to pods
**Answer:** B (2) – It manages external HTTP and HTTPS access to services
**Explanation:** Kubernetes Ingress is a resource that manages external access to services, typically HTTP and HTTPS traffic. It provides routing rules to direct external requests to the appropriate backend services within the cluster. It does not define internal pod networking (that is handled by Services and network plugins), nor is it used for storing configuration data (ConfigMaps/Secrets), scheduling pods (handled by the scheduler), or providing persistent storage (handled by PersistentVolumes).
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/ingress/" target="_blank">Kubernetes Official Documentation - Ingress</a><br><a href="https://kubernetes.io/docs/concepts/cluster-administration/networking/" target="_blank">Kubernetes Networking Concepts</a>

---

<!-- note:1772101854963 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** How can you force delete a Kubernetes pod that is stuck in the 'Terminating' state?
**Options:** A. Run 'kubectl delete pod <pod-name>' normally<br>B. Restart the kubelet service on the node<br>C. Run 'kubectl delete pod <pod-name> --force --grace-period=0'<br>D. Delete the node where the pod is running<br>E. Edit the pod's YAML to remove finalizers
**Answer:** C (3) – Run 'kubectl delete pod <pod-name> --force --grace-period=0'
**Explanation:** A pod stuck in 'Terminating' state can be force deleted using the command 'kubectl delete pod <pod-name> --force --grace-period=0'. This command bypasses the graceful termination period and forcibly removes the pod from the API server, even if the pod's containers are still running. Restarting the kubelet or deleting the node can be disruptive and are not recommended first steps. Editing the pod's YAML to remove finalizers can help if finalizers are blocking deletion, but the force delete command is the standard immediate solution.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination" target="_blank">Kubernetes Official Documentation - Deleting Pods</a><br><a href="https://github.com/kubernetes/kubernetes/issues/40682" target="_blank">Kubernetes GitHub Issue - Pod stuck in Terminating</a>

---

<!-- note:1772101854964 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the effect of the 'kubectl config use-context' command in Kubernetes?
**Options:** A. Switches the active namespace in the current context<br>B. Changes the current kubeconfig file being used<br>C. Modifies the cluster configuration in kubeconfig<br>D. Sets the current context to the specified one in kubeconfig<br>E. Updates the API server endpoint in the current context
**Answer:** D (4) – Sets the current context to the specified one in kubeconfig
**Explanation:** The command 'kubectl config use-context <context-name>' sets the current context in the kubeconfig file to the specified context. This changes which cluster, user, and namespace kubectl commands operate against by default. It does not switch namespaces directly (that requires 'kubectl config set-context' or 'kubectl config set-namespace'), nor does it change the kubeconfig file itself or modify cluster details. It simply selects which predefined context is active.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/" target="_blank">Kubernetes Official Documentation - Managing kubeconfig Files</a><br><a href="https://kubernetes.io/docs/reference/kubectl/cheatsheet/" target="_blank">Kubernetes kubectl Cheat Sheet</a>

---

<!-- note:1772101854965 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What command is used to list all pods across all namespaces in a Kubernetes cluster?
**Options:** A. 'kubectl get pods'<br>B. 'kubectl get pods --all'<br>C. 'kubectl get pods -A'<br>D. 'kubectl get pods --namespaces'<br>E. 'kubectl get all-pods'
**Answer:** C (3) – 'kubectl get pods -A'
**Explanation:** The '-A' flag is used with 'kubectl get pods' to list resources in all namespaces. This is a shorthand for '--all-namespaces', which ensures that pods from every namespace are displayed.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/overview/" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/get-pods" target="_blank">Kubernetes CLI Reference</a>

---

<!-- note:1772101854966 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the primary function of a ReplicaSet in Kubernetes?
**Options:** A. To ensure that a specified number of pod replicas are running at all times<br>B. To expose services to external traffic using load balancing<br>C. To store persistent data for applications<br>D. To define and enforce network policies for pods<br>E. To schedule pods to specific nodes based on resource requirements
**Answer:** A (1) – To ensure that a specified number of pod replicas are running at all times
**Explanation:** A ReplicaSet in Kubernetes ensures that a specified number of pod replicas are running at all times. It monitors existing pods and creates or deletes them as needed to maintain the desired state. Incorrect options: (1) Exposing services to external traffic is handled by Services, not ReplicaSets. (2) Persistent data storage is managed by PersistentVolumes and PersistentVolumeClaims. (3) Network policies are defined separately using NetworkPolicy resources. (4) Scheduling pods to specific nodes is handled by the Kubernetes Scheduler.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/" target="_blank">Kubernetes Official Documentation - ReplicaSet</a><br><a href="https://kubernetes.io/docs/concepts/workloads/" target="_blank">Kubernetes Concepts - Workloads and Controllers</a>

---

<!-- note:1772101854969 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** How do you scale a Kubernetes deployment named 'my-deployment' to 5 replicas using the CLI?
**Options:** A. kubectl scale deployment my-deployment --replicas=5<br>B. kubectl update deployment my-deployment --replicas=5<br>C. kubectl set deployment my-deployment replicas=5<br>D. kubectl resize deployment my-deployment 5<br>E. kubectl deploy my-deployment --replicas=5
**Answer:** A (1) – kubectl scale deployment my-deployment --replicas=5
**Explanation:** The 'kubectl scale' command is used to adjust the number of replicas in a deployment. In this case, 'kubectl scale deployment my-deployment --replicas=5' will scale the deployment to 5 replicas.
**Sources:** <a href="https://kubernetes.io/docs/reference/generated/kubectl/scale" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/scale" target="_blank">Kubernetes CLI Reference</a>

---

<!-- note:1772101854970 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which Kubernetes component is responsible for maintaining network rules on nodes for services?
**Options:** A. kubelet<br>B. kube-proxy<br>C. kube-scheduler<br>D. kube-controller-manager<br>E. etcd
**Answer:** B (2) – kube-proxy
**Explanation:** kube-proxy is the component that maintains network rules on nodes for services. It ensures that incoming traffic is properly routed to the correct service endpoints.
**Sources:** <a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/concepts/architecture/" target="_blank">Kubernetes Architecture</a>

---

<!-- note:1772101854971 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the primary function of a DaemonSet in Kubernetes?
**Options:** A. A pod runs on all nodes or a subset of nodes<br>B. Only one pod runs in the cluster<br>C. Pods are automatically scaled based on load<br>D. Services are exposed externally<br>E. ConfigMaps are synchronized across namespaces
**Answer:** A (1) – A pod runs on all nodes or a subset of nodes
**Explanation:** DaemonSets ensure that a copy of a pod runs on each node or a subset of nodes in a Kubernetes cluster. This is useful for running system daemons or monitoring agents.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/concepts/workloads/" target="_blank">Kubernetes Workloads</a>

---

<!-- note:1772101854973 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What happens by default when a container in a Kubernetes pod crashes?
**Options:** A. The pod is deleted<br>B. Kubernetes does nothing<br>C. The kubelet restarts the container<br>D. An alert is sent to the administrator<br>E. The node is drained
**Answer:** C (3) – The kubelet restarts the container
**Explanation:** By default, when a container in a Kubernetes pod crashes, the kubelet will automatically restart it. This behavior can be configured using restart policies.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/" target="_blank">Kubernetes Kubelet</a>

---

<!-- note:1772101854974 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What command is used to update an image in a Kubernetes deployment?
**Options:** A. kubectl set image deployment/my-deployment my-container=my-image:tag<br>B. kubectl update image deployment/my-deployment my-container=my-image:tag<br>C. kubectl replace image deployment/my-deployment my-container=my-image:tag<br>D. kubectl change image deployment/my-deployment my-container=my-image:tag<br>E. kubectl edit deployment my-deployment
**Answer:** A (1) – kubectl set image deployment/my-deployment my-container=my-image:tag
**Explanation:** The `kubectl set image` command is used to update the image for a specified container in a Kubernetes deployment. This command modifies the deployment configuration to use the new image, which triggers a rollout of the updated pods.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/overview/" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/commands/set-image" target="_blank">Kubernetes CLI Reference</a>

---

<!-- note:1772101854975 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** How can you prevent pods from being scheduled on a Kubernetes node? (Select all that apply)
**Options:** A. kubectl cordon <node-name><br>B. kubectl drain <node-name><br>C. kubectl taint nodes <node-name> key=value:NoSchedule<br>D. kubectl label nodes <node-name> unschedulable=true<br>E. kubectl delete node <node-name>
**Answer:** A, C – kubectl cordon; kubectl taint nodes <node> key=value:NoSchedule
**Explanation:** Both cordoning and tainting a node with `kubectl taint nodes <node-name> key=value:NoSchedule` prevents pods without a matching toleration from being scheduled on it. This is a way to mark nodes as unsuitable for certain workloads without completely removing them from the cluster.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/" target="_blank">Kubernetes Taints and Tolerations</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/commands/taint" target="_blank">Kubernetes CLI Reference</a>

---

<!-- note:1772101854976 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the primary function of the 'kubeadm' tool in Kubernetes?
**Options:** A. To manage container images<br>B. To bootstrap Kubernetes clusters<br>C. To monitor cluster health<br>D. To deploy applications to the cluster<br>E. To manage network policies
**Answer:** B (2) – To bootstrap Kubernetes clusters
**Explanation:** The `kubeadm` tool is used to bootstrap a Kubernetes cluster, making it easier to set up and manage clusters. It automates the installation and configuration process, ensuring that all necessary components are properly initialized.
**Sources:** <a href="https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/" target="_blank">Kubernetes kubeadm Documentation</a><br><a href="https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/" target="_blank">Kubernetes kubeadm CLI Reference</a>

---

<!-- note:1772101854978 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** How do you delete a Kubernetes namespace and all its associated resources?
**Options:** A. kubectl delete all --namespace=<namespace><br>B. kubectl delete namespace <namespace><br>C. kubectl remove namespace <namespace><br>D. kubectl clean namespace <namespace><br>E. kubectl purge namespace <namespace>
**Answer:** B (2) – kubectl delete namespace <namespace>
**Explanation:** Deleting a namespace with `kubectl delete namespace <namespace>` removes the namespace and all resources within it. This includes pods, services, deployments, and other objects defined within that namespace.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Namespaces Documentation</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/commands/delete-namespace" target="_blank">Kubernetes CLI Reference</a>

---

<!-- note:1772101854979 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the purpose of the 'kubectl exec' command in Kubernetes?
**Options:** A. Executes a command on the Kubernetes control plane<br>B. Runs a command inside a container in a pod<br>C. Creates a new pod in the cluster<br>D. Updates an existing deployment<br>E. Deletes a Kubernetes resource
**Answer:** B (2) – Runs a command inside a container in a pod
**Explanation:** 'kubectl exec' is used to execute a command inside a running container within a Kubernetes pod. This is particularly useful for debugging or interacting with applications running inside containers. For example, you can use it to access logs or run shell commands within the container. Other options are incorrect because:<br>- Option 0: Commands are not executed on the control plane using 'kubectl exec'.<br>- Option 2: It does not create new pods; 'kubectl run' or deployment manifests are used for that.<br>- Option 3: Updating deployments is done using 'kubectl apply' or 'kubectl set'.<br>- Option 4: Deleting resources is handled by 'kubectl delete'.
**Sources:** <a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#exec" target="_blank">Kubernetes Official Documentation - kubectl exec</a><br><a href="https://kubernetes.io/docs/tutorials/kubernetes-basics/debug-application/" target="_blank">Kubernetes Basics - Debugging Applications</a>

---

<!-- note:1772101854980 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** How can you expose a Kubernetes deployment as a service?
**Options:** A. kubectl expose deployment my-deployment<br>B. kubectl service deployment my-deployment<br>C. kubectl create service my-deployment<br>D. kubectl generate service my-deployment<br>E. kubectl map service my-deployment
**Answer:** A (1) – kubectl expose deployment my-deployment
**Explanation:** The `kubectl expose` command creates a Service that exposes the deployment, allowing access to the pods within the deployment from outside the cluster.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/service/" target="_blank">Kubernetes Services Documentation</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/commands/expose" target="_blank">Kubernetes CLI Reference</a>

---

<!-- note:1772101854981 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the primary function of a Horizontal Pod Autoscaler (HPA) in Kubernetes?
**Options:** A. Automatically scales nodes<br>B. Scales pods based on CPU utilization<br>C. Schedules pods to nodes<br>D. Balances network traffic<br>E. Manages storage volumes
**Answer:** B (2) – Scales pods based on CPU utilization
**Explanation:** A Horizontal Pod Autoscaler (HPA) in Kubernetes automatically adjusts the number of replicas of a pod based on observed CPU utilization or other custom metrics. This helps ensure that the application has sufficient resources to handle the current workload without over-allocating resources when demand is low.
**Sources:** <a href="https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/concepts/workloads/controllers/horizontal-pod-autoscaler/" target="_blank">Horizontal Pod Autoscaling</a>

---

<!-- note:1772101854982 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the main purpose of an Ingress Controller in Kubernetes?
**Options:** A. To expose services outside the cluster using HTTP/HTTPS<br>B. To manage internal pod communication<br>C. To store and manage secrets<br>D. To schedule pods to nodes<br>E. To provide persistent storage
**Answer:** A (1) – To expose services outside the cluster using HTTP/HTTPS
**Explanation:** Ingress Controllers in Kubernetes manage external access to cluster services via HTTP/HTTPS. They act as entry points for incoming HTTP requests and route them to appropriate services within the cluster, allowing for load balancing, SSL termination, and path-based routing.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/ingress/" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/" target="_blank">Ingress Controllers</a>

---

<!-- note:1772101854983 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** How do you label a Kubernetes node with the key 'env' and value 'production'?
**Options:** A. kubectl label node <node-name> env:production<br>B. kubectl label nodes <node-name> env=production<br>C. kubectl annotate node <node-name> env=production<br>D. kubectl set label node <node-name> env=production<br>E. kubectl tag node <node-name> env=production
**Answer:** B (2) – kubectl label nodes <node-name> env=production
**Explanation:** To label a Kubernetes node with the key 'env' and value 'production', you use the command `kubectl label nodes <node-name> env=production`. This command adds a label to the specified node, which can be used for filtering or selecting nodes for specific tasks.
**Sources:** <a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#label" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#label" target="_blank">Kubectl Label</a>

---

<!-- note:1772101854984 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which Kubernetes resource is used to run a one-time task?
**Options:** A. Deployment<br>B. StatefulSet<br>C. DaemonSet<br>D. Job<br>E. ReplicaSet
**Answer:** D (4) – Job
**Explanation:** In Kubernetes, a Job is used to run a one-time task. Jobs create one or more pods to perform a task and ensure they complete successfully. They are ideal for batch processing or running tasks that need to complete before the pods are terminated.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/job/" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/concepts/workloads/controllers/job/" target="_blank">Jobs</a>

---

<!-- note:1772101854985 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** How can you retrieve a list of all contexts in your kubeconfig file?
**Options:** A. kubectl config get-contexts<br>B. kubectl get contexts<br>C. kubectl config view<br>D. kubectl context list<br>E. kubectl list contexts
**Answer:** A (1) – kubectl config get-contexts
**Explanation:** To list all contexts in your kubeconfig file, you use the command `kubectl config get-contexts`. This command displays all available contexts, which are used to manage different Kubernetes clusters or environments.
**Sources:** <a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#config" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#config" target="_blank">Kubectl Config</a>

---

<!-- note:1772101854986 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What happens when you set 'terminationGracePeriodSeconds' to zero in a Kubernetes pod spec?
**Options:** A. The pod will terminate immediately without a graceful shutdown<br>B. The pod will never terminate<br>C. The pod will have infinite time to terminate<br>D. The setting is ignored by Kubernetes<br>E. The pod will terminate after 30 seconds
**Answer:** A (1) – The pod will terminate immediately without a graceful shutdown
**Explanation:** Setting 'terminationGracePeriodSeconds' to zero forces the pod to terminate immediately without a graceful shutdown. This means any running processes will be forcefully stopped, which can lead to data corruption or other issues if not handled properly.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#podspec-v1-core" target="_blank">Kubernetes Termination Grace Period</a>

---

<!-- note:1772101854987 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which Kubernetes object is used to manage stateful applications that require persistent storage and network identities?
**Options:** A. Deployment<br>B. StatefulSet<br>C. ReplicaSet<br>D. DaemonSet<br>E. Job
**Answer:** B (2) – StatefulSet
**Explanation:** StatefulSets are used to manage stateful applications that require persistent storage and network identities. Unlike Deployments, StatefulSets maintain a stable network identity and storage for each pod, making them suitable for applications like databases.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/" target="_blank">Kubernetes StatefulSets</a><br><a href="https://kubernetes.io/docs/concepts/workloads/controllers/deployment/" target="_blank">Kubernetes Deployments vs StatefulSets</a>

---

<!-- note:1772101854988 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** How do you create a Kubernetes namespace named 'dev'?
**Options:** A. kubectl create namespace dev<br>B. kubectl apply namespace dev<br>C. kubectl generate namespace dev<br>D. kubectl make namespace dev<br>E. kubectl new namespace dev
**Answer:** A (1) – kubectl create namespace dev
**Explanation:** To create a Kubernetes namespace named 'dev', you use the command 'kubectl create namespace dev'. This command directly creates a new namespace in your cluster.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Namespaces</a><br><a href="https://kubernetes.io/docs/reference/kubectl/overview/" target="_blank">Kubernetes CLI Commands</a>

---

<!-- note:1772101854989 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What command can you use to edit a Kubernetes resource directly in your default editor?
**Options:** A. kubectl change <resource><br>B. kubectl update <resource><br>C. kubectl edit <resource><br>D. kubectl modify <resource><br>E. kubectl adjust <resource>
**Answer:** C (3) – kubectl edit <resource>
**Explanation:** The 'kubectl edit' command is used to edit a Kubernetes resource directly in your default editor. This command opens the resource's configuration file in your editor, allowing you to make changes before saving and applying them.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/overview/" target="_blank">Kubernetes CLI Commands</a><br><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/" target="_blank">Kubernetes Resource Management</a>

---

<!-- note:1772101854990 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** How do you port-forward a local port to a port on a Kubernetes pod?
**Options:** A. kubectl port-forward <pod-name> <local-port>:<pod-port><br>B. kubectl forward-port <pod-name> <local-port>:<pod-port><br>C. kubectl tunnel <pod-name> <local-port>:<pod-port><br>D. kubectl proxy <pod-name> --port=<local-port><br>E. kubectl connect <pod-name> --port=<local-port>
**Answer:** A (1) – kubectl port-forward <pod-name> <local-port>:<pod-port>
**Explanation:** To port-forward a local port to a port on a Kubernetes pod, you use the command 'kubectl port-forward <pod-name> <local-port>:<pod-port>'. This command allows you to access the pod's port from your local machine.
**Sources:** <a href="https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/" target="_blank">Kubernetes Port Forwarding</a><br><a href="https://kubernetes.io/docs/reference/kubectl/overview/" target="_blank">Kubernetes CLI Commands</a>

---

<!-- note:1772101854991 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the primary purpose of a PersistentVolumeClaim (PVC) in Kubernetes?
**Options:** A. To request storage resources from the cluster<br>B. To define storage classes<br>C. To monitor disk usage<br>D. To create a new volume<br>E. To delete unused volumes
**Answer:** A (1) – To request storage resources from the cluster
**Explanation:** A PersistentVolumeClaim (PVC) is a request for storage by a user that binds to a PersistentVolume (PV) in the cluster. It abstracts the details of how storage is provided and allows pods to use storage resources without knowing the underlying storage implementation. PVCs do not define storage classes, monitor disk usage, create new volumes directly, or delete volumes; those tasks are handled by other Kubernetes components.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/" target="_blank">Kubernetes Official Documentation - Persistent Volumes</a><br><a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims" target="_blank">Kubernetes Official Documentation - PersistentVolumeClaim</a>

---

<!-- note:1772101854994 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which Kubernetes resource is designed to manage long-running, stateful applications that require stable network identities and persistent storage?
**Options:** A. Deployment<br>B. Job<br>C. StatefulSet<br>D. DaemonSet<br>E. ReplicaSet
**Answer:** C (3) – StatefulSet
**Explanation:** StatefulSets are used to manage stateful applications that require stable, unique network identifiers and persistent storage across pod restarts. Unlike Deployments or ReplicaSets, which are suited for stateless applications, StatefulSets ensure that pods are created in order and maintain persistent identities. Jobs are for batch or finite tasks, and DaemonSets ensure a pod runs on every node but do not provide stable identities or storage.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/" target="_blank">Kubernetes Official Documentation - StatefulSets</a><br><a href="https://kubernetes.io/docs/concepts/workloads/controllers/" target="_blank">Kubernetes Official Documentation - Workloads Overview</a>

---

<!-- note:1772101854995 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the default Kubernetes behavior when a container exceeds its configured memory limit?
**Options:** A. The container is throttled<br>B. The container is terminated<br>C. The pod is moved to another node<br>D. Kubernetes does nothing<br>E. Additional memory is allocated
**Answer:** B (2) – The container is terminated
**Explanation:** When a container exceeds its memory limit, the Kubernetes kubelet kills the container to prevent it from affecting other workloads. This is known as an Out Of Memory (OOM) kill. The container is terminated and may be restarted depending on the pod's restart policy. CPU limits result in throttling, but memory limits cause termination. Kubernetes does not move pods automatically to other nodes or allocate additional memory beyond the specified limit.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/" target="_blank">Kubernetes Official Documentation - Managing Compute Resources for Containers</a><br><a href="https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/" target="_blank">Kubernetes Official Documentation - Pod Lifecycle</a>

---

<!-- note:1772101854996 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which kubectl command lists all resource types within a specific namespace?
**Options:** A. kubectl get all --namespace=<namespace><br>B. kubectl get resources --namespace=<namespace><br>C. kubectl describe namespace <namespace><br>D. kubectl list namespace <namespace><br>E. kubectl get all <namespace>
**Answer:** A (1) – kubectl get all --namespace=<namespace>
**Explanation:** The command 'kubectl get all --namespace=<namespace>' retrieves all resource types (pods, services, deployments, etc.) within the specified namespace. The other options are either invalid commands or do not list all resources. 'kubectl describe namespace' provides details about the namespace itself, not its resources.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/cheatsheet/" target="_blank">Kubernetes Official Documentation - kubectl Cheat Sheet</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get" target="_blank">Kubernetes Official Documentation - kubectl get</a>

---

<!-- note:1772101854997 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the effect of the 'kubectl rollout undo' command on a Kubernetes deployment?
**Options:** A. Deletes the deployment<br>B. Rolls back to the previous revision<br>C. Pauses the deployment<br>D. Scales down the deployment<br>E. Updates the deployment to a new version
**Answer:** B (2) – Rolls back to the previous revision
**Explanation:** The 'kubectl rollout undo' command reverts a deployment to its previous revision, effectively rolling back any changes made in the most recent update. It does not delete, pause, scale, or update the deployment to a new version but restores the last known good state.
**Sources:** <a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#rollout" target="_blank">Kubernetes Official Documentation - kubectl rollout</a><br><a href="https://kubernetes.io/docs/concepts/workloads/controllers/deployment/" target="_blank">Kubernetes Official Documentation - Deployments</a>

---

<!-- note:1772101854999 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is a common use case for a Kubernetes CronJob?
**Options:** A. Running a database<br>B. Serving web traffic<br>C. Scheduling regular, recurring tasks<br>D. Managing network policies<br>E. Providing persistent storage
**Answer:** C (3) – Scheduling regular, recurring tasks
**Explanation:** Kubernetes CronJobs are designed to schedule and run Jobs at specified times or intervals, similar to cron jobs in Unix-like systems. They are ideal for automating repetitive tasks such as backups, report generation, or periodic maintenance. Other options like running a database, serving web traffic, managing network policies, or providing persistent storage are outside the scope of CronJobs' functionality.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/" target="_blank">Kubernetes Official Documentation - CronJobs</a><br><a href="https://kubernetes.io/blog/2019/07/16/welcome-cronjob/" target="_blank">Kubernetes Patterns - CronJob Pattern</a>

---

<!-- note:1772101855001 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which kubectl command is used to delete a deployment named 'my-app' in Kubernetes?
**Options:** A. kubectl remove deployment my-app<br>B. kubectl delete deployment my-app<br>C. kubectl destroy deployment my-app<br>D. kubectl erase deployment my-app<br>E. kubectl terminate deployment my-app
**Answer:** B (2) – kubectl delete deployment my-app
**Explanation:** The correct command to delete a deployment in Kubernetes is 'kubectl delete deployment my-app'. This command removes the deployment resource and all associated pods. The other options are incorrect as they are not valid kubectl commands for deleting resources.
**Sources:** <a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete" target="_blank">Kubernetes Official Documentation - kubectl delete</a><br><a href="https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/" target="_blank">Kubernetes Basics - Deleting a Deployment</a>

---

<!-- note:1772101855002 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the primary function of a Kubernetes Service of type 'NodePort'?
**Options:** A. Exposes the service on a static port on each node's IP address<br>B. Load balances traffic across multiple services<br>C. Exposes the service externally using a cloud provider's load balancer<br>D. Maps the service to an external DNS name<br>E. Provides internal cluster DNS resolution
**Answer:** A (1) – Exposes the service on a static port on each node's IP address
**Explanation:** A Kubernetes Service of type 'NodePort' exposes the service on the same static port across all nodes in the cluster, allowing external traffic to access the service via <NodeIP>:<NodePort>. It does not provide load balancing across multiple services (that is handled by ClusterIP or LoadBalancer types), nor does it map to external DNS names or provide internal DNS resolution. The LoadBalancer type is used to expose services externally via cloud provider load balancers.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/service/#nodeport" target="_blank">Kubernetes Official Documentation - Services</a><br><a href="https://www.cncf.io/blog/2019/04/02/kubernetes-networking-deep-dive/" target="_blank">Kubernetes Networking Deep Dive</a>

---

<!-- note:1772101855003 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which kubectl command displays the Kubernetes client and server versions for the cluster?
**Options:** A. kubectl version<br>B. kubectl get version<br>C. kubectl cluster-info<br>D. kubectl describe cluster<br>E. kubectl info
**Answer:** A (1) – kubectl version
**Explanation:** The command 'kubectl version' shows both the client and server (cluster) Kubernetes versions, which is useful for verifying compatibility and troubleshooting. Other commands like 'kubectl get version' or 'kubectl info' are invalid or do not provide version details. 'kubectl cluster-info' provides cluster endpoint information but not version details.
**Sources:** <a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#version" target="_blank">Kubernetes Official Documentation - kubectl version</a><br><a href="https://kubernetes.io/docs/reference/kubectl/cheatsheet/" target="_blank">Kubernetes CLI Cheat Sheet</a>

---

<!-- note:1772101855004 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the primary purpose of the 'kubectl config' command in Kubernetes?
**Options:** A. To configure Kubernetes cluster settings<br>B. To manage kubeconfig files and contexts<br>C. To update deployment configurations<br>D. To set node configurations<br>E. To modify pod specifications
**Answer:** B (2) – To manage kubeconfig files and contexts
**Explanation:** 'kubectl config' is used to view and modify kubeconfig files, which store cluster connection information, user credentials, and contexts. This command helps manage multiple clusters and user access configurations. It does not directly configure cluster settings, deployments, nodes, or pods.
**Sources:** <a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#config" target="_blank">Kubernetes Official Documentation - kubectl config</a><br><a href="https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/" target="_blank">Kubernetes Basics - Accessing Clusters</a>

---

<!-- note:1772101855009 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the primary function of a Kubernetes Ingress resource in managing network traffic?
**Options:** A. To manage internal cluster networking<br>B. To define rules for routing external HTTP and HTTPS traffic to services<br>C. To provide persistent storage to pods<br>D. To schedule pods onto nodes<br>E. To configure network policies for pod communication
**Answer:** B (2) – To define rules for routing external HTTP and HTTPS traffic to services
**Explanation:** A Kubernetes Ingress resource primarily manages external access to services within a cluster by defining rules for routing HTTP and HTTPS traffic. It acts as an entry point that controls how external clients reach services inside the cluster. Other options are incorrect because internal networking is handled by Services and CNI plugins, storage is managed by PersistentVolumes, pod scheduling is done by the scheduler, and network policies control pod-to-pod communication rather than external traffic.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/ingress/" target="_blank">Kubernetes Official Documentation - Ingress</a><br><a href="https://www.cncf.io/blog/2018/12/19/a-deep-dive-into-kubernetes-networking/" target="_blank">Cloud Native Computing Foundation - Kubernetes Networking</a>

---

<!-- note:1772101855011 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** How can you enable debug-level logging for the Kubernetes kubelet component?
**Options:** A. Set the verbosity level to 4 by adding '--v=4' to the kubelet startup arguments<br>B. Run the command 'kubectl debug kubelet'<br>C. Modify the kubelet configuration file to set 'logLevel: debug'<br>D. Restart the kubelet with the flag '--debug=true'<br>E. Debug logging cannot be enabled for the kubelet
**Answer:** A (1) – Set the verbosity level to 4 by adding '--v=4' to the kubelet startup arguments
**Explanation:** Debug logging in kubelet is enabled by increasing the verbosity level through the '--v' flag, with '--v=4' commonly used to enable debug-level logs. The other options are incorrect: 'kubectl debug kubelet' is not a valid command; kubelet configuration does not use a 'logLevel' field; '--debug=true' is not a recognized flag; and debug logging is indeed possible and commonly used for troubleshooting.
**Sources:** <a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/" target="_blank">Kubernetes Official Documentation - Kubelet Command Line Flags</a><br><a href="https://kubernetes.io/docs/concepts/cluster-administration/logging/" target="_blank">Kubernetes Logging and Monitoring</a>

---

<!-- note:1772101855012 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which kubectl command is used to create a pod directly from a container image?
**Options:** A. kubectl create pod <pod-name> --image=<image><br>B. kubectl run <pod-name> --image=<image><br>C. kubectl new pod <pod-name> --image=<image><br>D. kubectl pod <pod-name> --image=<image><br>E. kubectl deploy pod <pod-name> --image=<image>
**Answer:** B (2) – kubectl run <pod-name> --image=<image>
**Explanation:** The 'kubectl run' command is used to create a pod or deployment from a specified container image. It is the standard way to quickly start a pod with a given image. The other options are invalid commands or syntaxes that do not exist in kubectl.
**Sources:** <a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#run" target="_blank">Kubernetes Official Documentation - kubectl run</a><br><a href="https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-intro/" target="_blank">Kubernetes Basics - Running a Pod</a>

---

<!-- note:1772101855013 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the effect of executing the command 'kubectl drain <node-name>' on a Kubernetes node?
**Options:** A. Deletes the node from the cluster<br>B. Marks the node as unschedulable and evicts all pods safely<br>C. Restarts the node<br>D. Upgrades the node's Kubernetes version<br>E. Cleans up unused container images on the node
**Answer:** B (2) – Marks the node as unschedulable and evicts all pods safely
**Explanation:** 'kubectl drain' prepares a node for maintenance by marking it unschedulable to prevent new pods from being scheduled and safely evicting all existing pods. It does not delete the node, restart it, upgrade Kubernetes, or clean images. This ensures workloads are gracefully moved before maintenance.
**Sources:** <a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#drain" target="_blank">Kubernetes Official Documentation - kubectl drain</a><br><a href="https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/" target="_blank">Kubernetes Cluster Administration - Node Maintenance</a>

---

<!-- note:1772101855016 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** When configuring encryption at rest for Kubernetes secrets using etcd, which Kubernetes component's configuration must be updated to enable this encryption?
**Options:** A. kube-scheduler<br>B. kube-controller-manager<br>C. kubelet<br>D. kube-apiserver<br>E. etcd
**Answer:** D (4) – kube-apiserver
**Explanation:** Encryption at rest for Kubernetes secrets is configured by updating the kube-apiserver with an encryption configuration file. The kube-apiserver handles requests and encrypts secrets before storing them in etcd. The other components do not manage encryption configuration for secrets.
**Sources:** <a href="https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/" target="_blank">Kubernetes Official Documentation - Encrypting Secret Data at Rest</a><br><a href="https://kubernetes.io/docs/concepts/configuration/secret/" target="_blank">Kubernetes Security Best Practices - Secrets Management</a>

---

<!-- note:1772101855017 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** In Kubernetes Pod specifications, which field explicitly defines the container runtime class that should be used for pod execution?
**Options:** A. runtime<br>B. runtimeClassName<br>C. containerRuntime<br>D. runtimeClass<br>E. containerRuntimeClass
**Answer:** B (2) – runtimeClassName
**Explanation:** The 'runtimeClassName' field in Pod specifications references a RuntimeClass object that defines container runtime configurations. This allows administrators to control runtime security parameters and isolation mechanisms. Other options like 'runtimeClass' or 'containerRuntimeClass' are invalid field names in the Kubernetes API.
**Sources:** <a href="https://kubernetes.io/docs/concepts/containers/runtime-class/" target="_blank">Kubernetes RuntimeClass Documentation</a><br><a href="https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/" target="_blank">Kubernetes Pod Specification Reference</a>

---

<!-- note:1772101855024 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which Kubernetes resource provides layer 7 (HTTP/HTTPS) routing rules for external access to cluster services while enabling path-based and host-based routing?
**Options:** A. Ingress<br>B. Service<br>C. Endpoint<br>D. NetworkPolicy<br>E. LoadBalancer
**Answer:** A (1) – Ingress
**Explanation:** Ingress resources define HTTP/HTTPS routing rules and integrate with Ingress controllers to expose services. Services (ClusterIP, NodePort, LoadBalancer) operate at layer 4, while NetworkPolicy controls network traffic flow. LoadBalancer is a Service type, not a separate resource.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/ingress/" target="_blank">Kubernetes Ingress Documentation</a><br><a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Networking Best Practices</a>

---

<!-- note:1772101855030 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which Kubernetes admission controller specifically restricts kubelets to only modify their own Node API objects and Pod objects bound to their node?
**Options:** A. NodeRestriction<br>B. LimitRanger<br>C. NamespaceLifecycle<br>D. ResourceQuota<br>E. PodSecurityPolicy
**Answer:** A (1) – NodeRestriction
**Explanation:** The NodeRestriction admission controller limits kubelet permissions to prevent node spoofing and privilege escalation. It ensures kubelets can only modify their own Node API object and Pod objects scheduled on their node, while LimitRanger and ResourceQuota manage resource constraints.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/" target="_blank">Kubernetes Admission Controllers Guide</a><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/node/" target="_blank">Kubernetes Node Authorization</a>

---

<!-- note:1772101855033 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which of the following are critical security hardening measures for the Kubernetes API server? (Select all that apply)
**Options:** A. Disable anonymous authentication<br>B. Enable RBAC authorization<br>C. Allow all admission controllers<br>D. Enable etcd encryption for secrets<br>E. Use insecure port for API communication
**Answer:** A, B, D – disable anonymous auth, RBAC, and etcd encryption for secrets
**Explanation:** Disabling anonymous authentication prevents unauthorized access, RBAC enables granular permissions, and etcd encryption protects sensitive data. Allowing all admission controllers (including deprecated ones) and using insecure ports would reduce security. The insecure port (--insecure-port) is deprecated and should be disabled.
**Sources:** <a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/" target="_blank">Kubernetes API Server Security</a><br><a href="https://www.cisecurity.org/benchmark/kubernetes/" target="_blank">CIS Kubernetes Benchmark</a>

---

<!-- note:1772101855034 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which Kubernetes control plane component is exclusively responsible for evaluating scheduling constraints and binding Pods to appropriate worker nodes?
**Options:** A. kube-controller-manager<br>B. kube-scheduler<br>C. kube-apiserver<br>D. kubelet<br>E. etcd
**Answer:** B (2) – kube-scheduler
**Explanation:** The kube-scheduler evaluates Pod specifications against node resources, taints/tolerations, and affinity/anti-affinity rules to select optimal nodes. The kube-controller-manager handles node lifecycle controllers, while kubelets manage Pod execution on worker nodes.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/" target="_blank">Kubernetes Scheduler Documentation</a><br><a href="https://kubernetes.io/docs/concepts/overview/components/" target="_blank">Kubernetes Components Overview</a>

---

<!-- note:1772101855035 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** In Kubernetes, which resource allows multiple containers to share the same network stack, enabling them to communicate using 'localhost'?
**Options:** A. Deployment<br>B. DaemonSet<br>C. Pod<br>D. Service<br>E. StatefulSet
**Answer:** C (3) – Pod
**Explanation:** A Pod in Kubernetes is the smallest deployable unit that can host one or more containers. Containers within the same Pod share the same network stack, including the same IP address and port space. This allows them to communicate with each other using 'localhost'. Other resources like Deployment, DaemonSet, Service, and StatefulSet are higher-level abstractions that manage Pods but do not define such shared networking behavior directly.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/pods/" target="_blank">Kubernetes Official Documentation - Pods</a><br><a href="https://kubernetes.io/docs/concepts/cluster-administration/networking/" target="_blank">Kubernetes Networking Concepts</a>

---

<!-- note:1772101855041 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the correct command to label a Kubernetes namespace named 'production' with the label 'env=prod'?
**Options:** A. kubectl label namespace env=prod production<br>B. kubectl label namespace production env=prod<br>C. kubectl annotate namespace production env=prod<br>D. kubectl label namespaces env=prod production<br>E. kubectl set label namespace production env=prod
**Answer:** B (2) – kubectl label namespace production env=prod
**Explanation:** To label a Kubernetes namespace, you use the `kubectl label` command. The correct syntax is `kubectl label namespace <namespace_name> <label_key>=<label_value>`. Therefore, to label the 'production' namespace with 'env=prod', you would use `kubectl label namespace production env=prod`. This command updates the namespace with the specified label, which can be useful for organizing and filtering resources within your cluster.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/overview/" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/" target="_blank">Kubernetes Label Documentation</a>

---

<!-- note:1772101855052 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What command should you use to delete all pods within a Kubernetes namespace named 'test'?
**Options:** A. kubectl delete pods --all -n test<br>B. kubectl delete pod -A<br>C. kubectl delete pods -n test<br>D. kubectl remove pods --namespace=test<br>E. kubectl delete pods * -n test
**Answer:** A (1) – kubectl delete pods --all -n test
**Explanation:** To delete all pods in a specific namespace, you use the `kubectl delete pods` command with the `--all` flag to specify all pods, and the `-n` flag to specify the namespace. The correct command is `kubectl delete pods --all -n test`. This command will delete all pods in the 'test' namespace, which can be useful for cleaning up resources or resetting a namespace.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/pods/" target="_blank">Kubernetes Pod Documentation</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/delete" target="_blank">Kubernetes Delete Command Documentation</a>

---

<!-- note:1772101855056 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which Kubernetes object is used to persist data across the lifecycle of a pod?
**Options:** A. PersistentVolume<br>B. ConfigMap<br>C. Secret<br>D. PersistentVolumeClaim<br>E. EmptyDir
**Answer:** A (1) – PersistentVolume
**Explanation:** A PersistentVolume (PV) is a Kubernetes resource that provides persistent storage for data that needs to be preserved across pod lifecycles. Unlike data stored in an EmptyDir or other ephemeral storage, data in a PersistentVolume remains available even if the pod is deleted or recreated. PersistentVolumeClaims (PVCs) are used to request storage resources from PersistentVolumes, but the PV itself is the resource that holds the data.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/" target="_blank">Kubernetes Persistent Volumes Documentation</a><br><a href="https://kubernetes.io/docs/concepts/storage/" target="_blank">Kubernetes Storage Overview</a>

---

<!-- note:1772101855059 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** If the Kubernetes API server is not responding, which configuration file should you check for possible misconfigurations?
**Options:** A. /var/log/kube-apiserver.log<br>B. /etc/kubernetes/manifests/kube-scheduler.yaml<br>C. /etc/kubernetes/manifests/kube-apiserver.yaml<br>D. /etc/kubernetes/config/apiserver.conf<br>E. /var/lib/kubelet/config.yaml
**Answer:** C (3) – /etc/kubernetes/manifests/kube-apiserver.yaml
**Explanation:** The Kubernetes API server's configuration is typically defined in its static pod manifest, which is usually located at `/etc/kubernetes/manifests/kube-apiserver.yaml`. This file contains the configuration for the API server, including any custom settings or overrides that might be causing issues. Checking this file can help identify misconfigurations that could be preventing the API server from responding.
**Sources:** <a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/" target="_blank">Kubernetes API Server Documentation</a><br><a href="https://kubernetes.io/docs/concepts/workloads/pods/init-containers/" target="_blank">Kubernetes Manifests Documentation</a>

---

<!-- note:1772101855065 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** According to the CIS Kubernetes Benchmark, which setting should be disabled on the kube-apiserver for security reasons?
**Options:** A. Anonymous authentication<br>B. RBAC authorization<br>C. TLS encryption<br>D. Admission controllers<br>E. Audit logging
**Answer:** A (1) – Anonymous authentication
**Explanation:** Anonymous authentication should be disabled on the kube-apiserver to enhance security, as recommended by the CIS Kubernetes Benchmark. Enabling anonymous authentication allows unauthorized access to cluster resources, which is a significant security risk. Disabling it ensures that all interactions with the API server require proper authentication.
**Sources:** <a href="https://www.cisecurity.org/benchmark/kubernetes/" target="_blank">CIS Kubernetes Benchmark</a><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Authentication Documentation</a>

---

<!-- note:1772101855066 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which kube-apiserver flag must be configured to disable anonymous authentication and prevent unauthenticated requests to the Kubernetes API?
**Options:** A. --disable-anonymous-auth<br>B. --anonymous-auth=false<br>C. --enable-auth=false<br>D. --no-anonymous<br>E. --deny-anonymous
**Answer:** B (2) – --anonymous-auth=false
**Explanation:** The '--anonymous-auth=false' flag explicitly disables anonymous requests to the API server, forcing authentication for all requests. This is critical for production clusters to prevent unauthorized access. The other options are either non-existent flags or use incorrect syntax for authentication configuration.
**Sources:** <a href="https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/" target="_blank">Kubernetes API Server Security Settings</a><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Authentication Documentation</a>

---

<!-- note:1772101855087 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which kube-apiserver configuration flag properly enables the ImagePolicyWebhook admission controller in modern Kubernetes versions (v1.10+)?
**Options:** A. --enable-admission-plugins=ImagePolicyWebhook<br>B. --admission-control=ImagePolicyWebhook<br>C. --admission-plugins=ImagePolicyWebhook<br>D. --enable-image-policy<br>E. --image-policy-webhook=true
**Answer:** A (1) – --enable-admission-plugins=ImagePolicyWebhook
**Explanation:** In Kubernetes v1.10+, admission controllers are enabled using '--enable-admission-plugins'. The '--admission-control' flag was deprecated in favor of this new syntax. The ImagePolicyWebhook controller enables image verification through external webhooks, crucial for enforcing image registry policies.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/" target="_blank">Kubernetes Admission Controllers Guide</a><br><a href="https://kubernetes.io/docs/reference/config-api/apiserver-webhook.v1/" target="_blank">ImagePolicyWebhook Configuration</a>

---

<!-- note:1772101855095 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which Kubernetes resource type allows cluster administrators to define and enforce the use of specific container runtimes like gVisor or Kata Containers?
**Options:** A. Runtime<br>B. RuntimeClass<br>C. PodSecurityPolicy<br>D. SecurityContext<br>E. ContainerRuntime
**Answer:** B (2) – RuntimeClass
**Explanation:** RuntimeClass is a first-class Kubernetes resource that specifies container runtime configurations. It enables security-conscious runtime selection (like gVisor's sandboxed environment) while maintaining portability across different container runtimes. PodSecurityPolicy (deprecated in v1.21) handled security policies but not runtime selection.
**Sources:** <a href="https://kubernetes.io/docs/concepts/containers/runtime-class/" target="_blank">Kubernetes RuntimeClass Documentation</a><br><a href="https://gvisor.dev/docs/user_guide/kubernetes/" target="_blank">gVisor Integration Guide</a>

---

<!-- note:1772101855096 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Where in a Pod specification should you declare the use of a gVisor RuntimeClass to ensure all containers in the Pod use this secure runtime environment?
**Options:** A. Set 'runtime: gvisor'<br>B. Set 'securityContext: {runtimeClassName: "gvisor"}'<br>C. Set 'runtimeClassName: "gvisor"' at the Pod spec level<br>D. Set 'containerRuntime: "gvisor"' in the container spec<br>E. Annotate the Pod with 'runtimeClass: gvisor'
**Answer:** C (3) – Set 'runtimeClassName: "gvisor"' at the Pod spec level
**Explanation:** The 'runtimeClassName' field must be specified directly in the Pod's spec section (pod.spec.runtimeClassName). This ensures all containers in the Pod use the specified runtime. SecurityContext handles security parameters but not runtime selection, and container-level runtime configuration isn't supported in this manner.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/" target="_blank">Kubernetes Pod Specification</a><br><a href="https://kubernetes.io/docs/concepts/containers/runtime-class/#usage" target="_blank">RuntimeClass Usage Guide</a>

---

<!-- note:1772101855120 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which Kubernetes component is responsible for securely storing and managing all cluster data, including Secrets, ConfigMaps, and cluster state?
**Options:** A. kube-apiserver<br>B. kube-scheduler<br>C. kubelet<br>D. etcd<br>E. kube-controller-manager
**Answer:** D (4) – etcd
**Explanation:** etcd is the distributed key-value store that serves as Kubernetes' primary data store. It maintains the cluster's state, configuration data, and Secrets. While the kube-apiserver interacts with etcd, it doesn't store data directly. Proper etcd configuration (encryption, access controls, backups) is critical for cluster security.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/components/#etcd" target="_blank">Kubernetes etcd Documentation</a><br><a href="https://etcd.io/docs/v3.5/op-guide/security/" target="_blank">etcd Security Guide</a>

---

<!-- note:1772101855135 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What command is used to create a Kubernetes namespace named 'production'?
**Options:** A. kubectl create namespace production<br>B. kubectl new namespace production<br>C. kubectl apply namespace production<br>D. kubectl init namespace production<br>E. kubectl generate namespace production
**Answer:** A (1) – kubectl create namespace production
**Explanation:** The command 'kubectl create namespace production' is used to create a new namespace in a Kubernetes cluster. Namespaces provide a way to divide cluster resources between multiple applications or teams. They are essential for organizing and isolating resources within a cluster.
**Sources:** <a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#create" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Namespace Management</a>

---

<!-- note:1772101855137 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** In a Kubernetes cluster, which component is responsible for assigning pods to specific nodes based on resource requirements and constraints?
**Options:** A. kube-apiserver<br>B. kube-scheduler<br>C. kubelet<br>D. kube-controller-manager<br>E. etcd
**Answer:** B (2) – kube-scheduler
**Explanation:** The kube-scheduler is the component in Kubernetes responsible for scheduling pods onto nodes. It evaluates the resource requirements of the pods (e.g., CPU, memory) and matches them with the available resources on nodes. Other components, such as kube-apiserver, handle API requests; kubelet manages node-level operations; kube-controller-manager handles controllers; and etcd is the key-value store for cluster data.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/" target="_blank">Kubernetes Official Documentation - Scheduler</a><br><a href="https://kubernetes.io/docs/concepts/overview/components/" target="_blank">Kubernetes Components Overview</a>

---

<!-- note:1772101855139 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** What is the primary function of the Kubernetes 'LimitRange' resource?
**Options:** A. To limit the number of namespaces<br>B. To set default resource requests and limits for pods in a namespace<br>C. To restrict network access between pods<br>D. To control access to the Kubernetes API<br>E. To define storage classes
**Answer:** B (2) – To set default resource requests and limits for pods in a namespace
**Explanation:** A LimitRange in Kubernetes is used to enforce constraints on resource usage within a namespace. It sets default resource requests and limits for pods, ensuring that they do not exceed specified thresholds. This helps in preventing resource over-allocation and maintaining cluster stability.
**Sources:** <a href="https://kubernetes.io/docs/concepts/policy/limit-range/" target="_blank">Kubernetes LimitRange Documentation</a><br><a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/" target="_blank">Kubernetes Resource Management</a>

---

<!-- note:1772101855145 model:Many -->
**Domain:** Kubernetes Cluster Component Security
**Question:** Which Kubernetes resource is used to request persistent storage for a Pod?
**Options:** A. PersistentVolume<br>B. PersistentVolumeClaim<br>C. StorageClass<br>D. VolumeMount<br>E. ConfigMap
**Answer:** B (2) – PersistentVolumeClaim
**Explanation:** A PersistentVolumeClaim (PVC) is used by a Pod to request persistent storage resources. The PVC is matched with a PersistentVolume (PV), which provides the actual storage. StorageClasses are used to dynamically provision PersistentVolumes.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/" target="_blank">Kubernetes Persistent Volumes Documentation</a><br><a href="https://kubernetes.io/docs/concepts/storage/storage-classes/" target="_blank">Kubernetes Storage Classes Documentation</a>

---
