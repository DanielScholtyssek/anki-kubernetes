# KCNA - Kubernetes and Cloud Native Associate — Kubernetes Fundamentals

> Deck: `KCNA - Kubernetes and Cloud Native Associate` · Group: `Kubernetes Fundamentals` · Notes: 89 · Models: Basic++, Basic+++, Basic, Cloze, Many

<!-- note:1755878800141 model:Basic++ -->
**Front:** Which Kubernetes control plane component is responsible for
persisting the cluster’s desired state and configuration?
<br><br>A. kube-scheduler
<br>B. kube-apiserver
<br>C. etcd
<br>D. kubelet<br>E. controller-manager
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: etcd is a distributed key-value store that reliably stores
all Kubernetes cluster data, serving as the single source of truth for the
cluster’s state.

---

<!-- note:1755879377287 model:Basic++ -->
**Front:** A developer needs to expose a web application running in a set
of Pods within the cluster using a stable internal IP address.
Which Kubernetes resource <b>is most</b> appropriate?<br><br>A. Ingress
<br>B. NodePort Service
<br>C. ClusterIP Service
<br>D. ExternalName Service
<br>E. ReplicaSet
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: A ClusterIP Service provides a stable internal IP address
and DNS name for accessing Pods, only reachable from within the cluster.
NodePort exposes on nodes, Ingress is for external HTTP/S.

---

<!-- note:1755879935690 model:Basic++ -->
**Front:** What is <b>the primary purpose</b> of the Kubernetes API server in
the control plane architecture?<br><br>A. To run containerized applications directly
<br>B. To schedule Pods onto available worker nodes
<br>C. To validate and process REST requests for API objects<br>D. To manage network traffic between Pods
<br>E. To store cluster state in a time-series database
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: The kube-apiserver is the frontend of the control plane,
exposing the Kubernetes API. It processes and validates API requests,
and updates the corresponding objects in etcd.

---

<!-- note:1755879990893 model:Basic++ -->
**Front:** When a Pod is scheduled, what is <b>the primary factor</b> the kubescheduler considers from the Pod’s specification?<br><br>A. Container image version
<br>B. restartPolicy
<br>C. Resource requests and limits
<br>D. serviceAccountName
<br>E. labels
**Back:** Correct Answer: <b>C<br><br>Explanation</b>: The kube-scheduler filters nodes based on whether they
can satisfy the Pod’s resource requests (CPU, memory) and then ranks
them based on various priority functions.

---

<!-- note:1755880042259 model:Basic++ -->
**Front:** Which component is NOT part of the Kubernetes control plane?
<br><br>A. kube-apiserver
<br>B. etcd
<br>C. kube-scheduler
<br>D. kube-proxy
<br>E. kube-controller-manager
**Back:** Correct Answer: <b>D</b>
<br><br><b>Explanation</b>: kube-proxy runs on every node in the cluster and is responsible for maintaining network rules on nodes, enabling network communication to Pods from network sessions inside or outside of the cluster.
It’s a node component, not control plane.

---

<!-- note:1755880144449 model:Basic++ -->
**Front:** What is the main advantage of using a declarative approach (e.g.,
YAML manifests) to manage Kubernetes resources?
<br><br>A. It allows for more complex scripting logic
<br>B. It enables direct manipulation of etcd data
<br>C. It focuses on what desired state, not how to achieve it
<br>D. It provides faster API response times
<br>E. It simplifies single-container Pod deployments only
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: Declarative configurations define the desired state, and
Kubernetes controllers work to reconcile the current state to this desired
state. This is more robust and idempotent than imperative commands.

---

<!-- note:1755880341549 model:Basic++ -->
**Front:** In Kubernetes, what is the <b>primary role</b> of Role-Based Access
Control (RBAC)?
<br><br>A. To define network traffic flow between Pods
<br>B. To manage secure storage of sensitive data like passwords
<br>C. To control user and service account access to API resources
<br>D. To assign static IP addresses to Services
<br>E. To encrypt container images at rest
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: RBAC regulates access to Kubernetes API resources based
on the roles of individual users or service accounts within the cluster,
ensuring users only perform actions they are authorized for.

---

<!-- note:1755880485289 model:Basic++ -->
**Front:** What is the function of a NetworkPolicy in Kubernetes?<br>&nbsp;&nbsp;<br>A. To provide a stable DNS name for a set of Pods
<br>B. To manage external access to services via HTTP/S routing
<br>C. To define how Pods are allowed to communicate with each other
<br>D. To assign IP addresses to newly created Pods
<br>E. To encrypt traffic between services in a mesh
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: NetworkPolicy resources specify how groups of Pods are
allowed to communicate with each other and other network endpoints,
acting as a firewall at the Pod level.

---

<!-- note:1755880642160 model:Basic++ -->
**Front:** Which security mechanism in Kubernetes is best suited for providing an identity to processes running in Pods to interact with
the API server?<br>&nbsp;&nbsp;<br>A. NetworkPolicy
<br>B. SecurityContext
<br>C. ServiceAccount
<br>D. PodSecurityPolicy (deprecated) / PodSecurityAdmission
<br>E. TLS Certificates for etcd
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: ServiceAccounts provide an identity for processes that run
in a Pod, which can then be granted permissions to API resources via
RBAC Roles and RoleBindings.

---

<!-- note:1755880686730 model:Basic++ -->
**Front:** What is <b>the primary goal</b> of Horizontal Pod Autoscaling (HPA)
in Kubernetes?
<br><br>A. To increase the resource limits of existing Pods
<br>B. To adjust the number of Pod replicas based on metrics
<br>C. To add or remove Nodes from the cluster
<br>D. To automatically update container images
<br>E. To manage storage capacity for stateful sets
**Back:** Correct Answer: <b>B</b>
<br><br><b>Explanation</b>: HPA automatically scales the number of Pod replicas in
a workload resource (like a Deployment or StatefulSet) up or down based
on observed CPU utilization, custom metrics, or external metrics.

---

<!-- note:1755881818694 model:Basic++ -->
**Front:** What does a ReplicaSet ensure in Kubernetes?<div>&nbsp;
<br>A. That a Pod runs on every node
<br>B. That a certain number of Pod replicas are running
<br>C. That Pods have stable network identifiers
<br>D. That external traffic can reach the Pods
<br>E. That Pods are scheduled according to affinity rules</div>
**Back:** Correct Answer: <b>B<br></b>
<br><b>Explanation</b>: A ReplicaSet’s primary purpose is to maintain a stable set
of replica Pods running at any given time, ensuring the desired number of
instances of an application are available. Deployments manage ReplicaSets.

---

<!-- note:1755881921335 model:Basic++ -->
**Front:** What is the main purpose of a ServiceAccount in Kubernetes
when interacting with the API server?<div>&nbsp;
<br>A. To define network access policies for Pods
<br>B. To provide an identity for Pods to authenticate to the API
<br>C. To store sensitive credentials for applications
<br>D. To group users for applying permissions
<br>E. To manage DNS records for services</div>
**Back:** Correct Answer: <b>B</b>
<br><br><b>Explanation</b>: ServiceAccounts provide an identity for processes running
within Pods. This identity can be used to authenticate to the Kubernetes
API server, and RBAC rules can grant it specific permissions.

---

<!-- note:1755881957364 model:Basic++ -->
**Front:** If you need to run a batch job that completes and then terminates, which Kubernetes workload resource is most suitable?
<br><br>A. Deployment
<br>B. StatefulSet
<br>C. DaemonSet
<br>D. Job
<br>E. Service
**Back:** Correct Answer: D
<br>Explanation: A Job creates one or more Pods and ensures that a specified number of them successfully terminate. It’s ideal for batch tasks,
while CronJob is for scheduled Jobs.
<br>Domain: Kubernetes Fundamentals
<br>Competency: Kubernetes Resources

---

<!-- note:1755882113362 model:Basic++ -->
**Front:** What is a key difference between kubectl apply -f 
and kubectl create -f ?<div>&nbsp;
<br>A. apply is declarative, create is imperative
<br>B. create can update existing resources, apply cannot
<br>C. apply ignores existing resources, create fails if they exist
<br>D. apply stores last-applied-configuration, create does not
<br>E. create is idempotent, apply is not</div>
**Back:** Correct Answer: <b>D</b>
<br><br><b>Explanation</b>: kubectl apply records the applied configuration in an annotation on the resource. This allows it to calculate a patch between the
previous, current, and new desired state, making it suitable for declarative
updates. create will fail if the resource exists.

---

<!-- note:1755882194354 model:Basic++ -->
**Front:** What is <b>the primary function</b> of kube-proxy when a Service of
type ClusterIP is created?<div><br>A. It assigns an IP address from the cluster’s Pod CIDR.
<br>B. It modifies iptables or IPVS rules on nodes to route traffic.
<br>C. It creates a DNS A record for the Service.
<br>D. It terminates TLS connections for the Service.
<br>E. It exposes the Service on a port on each Node.</div>
**Back:** Correct Answer: <b>B</b>
<br><br><b>Explanation</b>: kube-proxy watches the API server for new Services and
Endpoints. For ClusterIP Services, it configures network rules (e.g., iptables, IPVS) on each node to capture traffic destined for the Service’s IP
and load balance it to the backend Pods.

---

<!-- note:1755882257285 model:Basic++ -->
**Front:** What core benefit does a StatefulSet provide over a Deployment
for applications like databases?
<br><br>A. Automatic rolling updates by default
<br>B. Simpler YAML configuration for Pod templates
<br>C. Stable, unique network identifiers and persistent storage<br>D. Support for hostNetwork: true
<br>E. Higher number of allowed replicas
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: StatefulSets are designed for stateful applications, providing stable, persistent identifiers (e.g., my-app-0, my-app-1) and perinstance persistent storage that follows the Pod identity.

---

<!-- note:1755882436165 model:Basic++ -->
**Front:** What is <b>the primary role </b>of the ”Controller Manager” in Kubernetes?&nbsp;<div><br></div><div>A. Manages user authentication and authorization&nbsp;</div><div>B. Exposes the Kubernetes API to external clients&nbsp;</div><div>C. Runs various controllers that regulate cluster state&nbsp;</div><div>D. Schedules Pods onto appropriate Nodes&nbsp;</div><div>E. Stores all cluster configuration data</div>
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: The kube-controller-manager runs multiple controller processes (e.g., Node controller, Replication controller, Endpoints controller)
that watch for changes and work to drive the actual cluster state towards
the desired state.

---

<!-- note:1755882790818 model:Basic++ -->
**Front:** What Kubernetes feature allows you to define constraints on
which Nodes your Pods can run, based on Node labels?
<br><br>A. NetworkPolicy
<br>B. ResourceQuota
<br>C. nodeSelector / nodeAffinity
<br>D. PodDisruptionBudget<br>E. LimitRange
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: nodeSelector provides a simple way to constrain Pods to
Nodes with specific labels. nodeAffinity offers more expressive rules, including ”preferred” and ”required” constraints.

---

<!-- note:1755883018446 model:Basic++ -->
**Front:** What is the role of an "Ingress Controller" in a Kubernetes
cluster?&nbsp;<div>A. It assigns IP addresses to Pods.</div><div>&nbsp;
<br>B. It manages storage volumes for stateful applications.
<br>C. It implements the rules defined in Ingress resources.
<br>D. It monitors the health of Nodes in the cluster.
<br>E. It encrypts communication between control plane components.</div>
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: An Ingress resource defines HTTP/S routing rules, but an
Ingress Controller (e.g., Nginx, Traefik) is the actual reverse proxy/load
balancer that reads these rules and routes external traffic accordingly.

---

<!-- note:1755883176652 model:Basic++ -->
**Front:** What is the core difference between ”authentication” and ”authorization” in Kubernetes security?
<br><br>A. Authentication is for users, authorization for service accounts.
<br>B. Authentication verifies identity, authorization verifies permissions.
<br>C. Authorization happens before authentication in the API request flow.
<br>D. Authentication uses Roles, authorization uses RoleBindings.
<br>E. Authorization uses client certificates, authentication uses tokens.
**Back:** Correct Answer: <b>B</b>
<br><br><b>Explanation</b>: Authentication is the process of determining who a user
or service is. Authorization is the process of determining what an authenticated user or service is allowed to do (i.e., which API resources they can
access and what actions they can perform).

---

<!-- note:1756745107509 model:Basic++ -->
**Front:** How can you securely store sensitive information like <b>passwords</b> or <b>API keys</b> in Kubernetes?<br><br>A. ConfigMap<br>B. Annotation<br>C. Label<br>D. Secret<br>E. nan
**Back:** Correct Answer: <b>D<br><br>Explanation</b>: Secrets are Kubernetes objects specifically designed to hold small amounts of sensitive data.

---

<!-- note:1756920369275 model:Basic++ -->
**Front:** <div>Which Kubernetes component is responsible for watching for newly created Pods and assigning them to Nodes?</div><div><br></div><div>A. kube-apiserver</div><div>B. etcd</div><div>C. kube-scheduler</div><div>D. kubelet</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: The kube-scheduler is the control plane component that decides which Node a Pod should run on based on constraints and availability.</div>

---

<!-- note:1756920413222 model:Basic++ -->
**Front:** <div>What is <b>the primary function</b> of the kubelet component?</div><div><br></div><div>A. Storing cluster state</div><div>B. Scheduling Pods onto Nodes</div><div>C. Managing the container runtime</div><div>D. Exposing the Kubernetes API</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><b><br></b></div><div><b>Explanation</b>: The kubelet runs on each Node and ensures that containers described in PodSpecs are running and healthy. It interacts with the container runtime.</div>

---

<!-- note:1756920442062 model:Basic++ -->
**Front:** <div>Which component acts as the central control plane and exposes the Kubernetes API?</div><div><br></div><div>A. kube-proxy</div><div>B. kube-apiserver</div><div>C. etcd</div><div>D. controller-manager</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div><div><b>Explanation</b>: The kube-apiserver validates and configures data for API objects (Pods, Services, etc.) and is the frontend for the control plane.</div>

---

<!-- note:1756920489375 model:Basic++ -->
**Front:** <div>What is <b>the primary role </b>of etcd in a Kubernetes cluster?</div><div><br></div><div>A. Running application containers</div><div>B. Scheduling workloads</div><div>C. Storing the cluster state</div><div>D. Managing network policies</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: etcd is a consistent and highly-available key-value store used as Kubernetes’ backing store for all cluster data.</div>

---

<!-- note:1756920536474 model:Basic++ -->
**Front:** <div>Which Kubernetes resource is typically used to manage stateless applications by ensuring a specified number of Pod replicas are running?</div><div><br></div><div>A. StatefulSet</div><div>B. DaemonSet</div><div>C. Deployment</div><div>D. Job</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: Deployments manage ReplicaSets, providing declarative updates and scaling for stateless applications.</div>

---

<!-- note:1756921223162 model:Basic++ -->
**Front:** <div>In Kubernetes, what is the process of assigning Pods to Nodes called?</div><div><br></div><div>A. Replication</div><div>B. Orchestration</div><div>C. Scheduling</div><div>D. Deployment</div>
**Back:** <div>Correct Answer: <b>C</b><br><br></div><div><b>Explanation</b>: Scheduling is the core function of the kube-scheduler, selecting appropriate Nodes for Pods based on resource requests and other factors.</div>

---

<!-- note:1756921467274 model:Basic++ -->
**Front:** <div>What Kubernetes object provides a stable IP address and DNS name for accessing a set of Pods?</div><div><br></div><div>A. Ingress</div><div>B. Service</div><div>C. EndpointSlice</div><div>D. NetworkPolicy</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div><div><b>Explanation</b>: A Service defines a logical set of Pods and a policy by which to access them, providing load balancing and service discovery.</div>

---

<!-- note:1756921506797 model:Basic++ -->
**Front:** <div>How can you securely store sensitive information like passwords or API keys in Kubernetes?</div><div><br></div><div>A. ConfigMap</div><div>B. Annotation</div><div>C. Label</div><div>D. Secret</div>
**Back:** <div>Correct Answer: <b>D</b></div><div><br></div><div><b>Explanation</b>: Secrets are Kubernetes objects specifically designed to hold small amounts of sensitive data.</div>

---

<!-- note:1756921609953 model:Basic++ -->
**Front:** <div>Which Kubernetes object defines rules about how Pods are allowed to communicate with each other and network endpoints?</div><div><br></div><div>A. Service</div><div>B. Ingress</div><div>C. NetworkPolicy</div><div>D. SecurityContext</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: NetworkPolicies allow specifying traffic flow rules at the IP address or port level (OSI layer 3 or 4).</div>

---

<!-- note:1756922999185 model:Basic++ -->
**Front:** <div>What is <b>the primary goa</b>l of the Cluster Autoscaler?</div><div><br></div><div>A. Scale Pod replicas</div><div>B. Scale cluster Nodes</div><div>C. Scale Persistent Volumes</div><div>D. Scale Service endpoints</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div><div><b>Explanation</b>: The Cluster Autoscaler adjusts the number of Nodes in the cluster based on pending Pods that cannot be scheduled due to resource limits.</div>

---

<!-- note:1756924376134 model:Basic++ -->
**Front:** <div>In Kubernetes RBAC (Role-Based Access Control), what defines a set of permissions?</div><div><br></div><div>A. Role / ClusterRole</div><div>B. ServiceAccount</div><div>C. RoleBinding / ClusterRoleBinding</div><div>D. User</div>
**Back:** <div>Correct Answer: A</div><div>Explanation: A Role (namespace-scoped) or ClusterRole (cluster-scoped) contains rules that represent a set of permissions on resources.</div><div>Domain: Container Orchestration</div><div>Competency: Security</div>

---

<!-- note:1756924421834 model:Basic++ -->
**Front:** <div>What object binds a Role or ClusterRole to a user, group, or ServiceAccount?</div><div><br></div><div>A. Secret</div><div>B. ConfigMap</div><div>C. NetworkPolicy</div><div>D. RoleBinding / ClusterRoleBinding</div>
**Back:** <div>Correct Answer: <b>D</b></div><div><br></div><div><b>Explanation</b>: A RoleBinding (namespace-scoped) or ClusterRoleBinding (cluster-scoped) grants the permissions defined in a Role/ClusterRole to subjects.</div>

---

<!-- note:1756924454765 model:Basic++ -->
**Front:** <div>If you need a Pod to run on every single Node in the cluster (or a subset), which controller is most suitable?</div><div><br></div><div>A. Deployment</div><div>B. StatefulSet</div><div>C. DaemonSet</div><div>D. Job</div>
**Back:** <div>Correct Answer: <b>C</b><br><br></div><div><b>Explanation</b>: DaemonSets ensure that all (or some) Nodes run a copy of a Pod, useful for cluster services like log collectors or node monitors.</div>

---

<!-- note:1756924504285 model:Basic++ -->
**Front:** <div>What is a primary difference between a Deployment and a StatefulSet?</div><div><br></div><div>A. StatefulSets manage Pods</div><div>B. Deployments are for databases</div><div>C. StatefulSets provide stable IDs</div><div>D. Deployments use PVs</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: StatefulSets provide guarantees about the ordering and uniqueness of Pods, including stable network identifiers and persistent storage.</div>

---

<!-- note:1756924565456 model:Basic++ -->
**Front:** <div>Which Kubernetes API object is used to manage external access to services in a cluster, typically HTTP/S?</div><div><br></div><div>A. Service (LoadBalancer type)</div><div>B. NodePort Service</div><div>C. Ingress</div><div>D. ExternalName Service</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: Ingress provides HTTP/S routing rules to manage external users’ access to services within the cluster based on hostnames or paths.</div>

---

<!-- note:1756924924815 model:Basic++ -->
**Front:** <div>What design pattern involves running an additional container within a Pod to provide auxiliary functions (like logging or monitoring) to the main application container?</div><div><br></div><div>A. Init Container</div><div>B. Sidecar Container</div><div>C. Ephemeral Container</div><div>D. Job Container</div>
**Back:** <div>Correct Answer:<b> B</b></div><div><br></div><div><b>Explanation</b>: The Sidecar pattern adds helper containers alongside the main application container within the same Pod network/storage namespace.</div>

---

<!-- note:1756924968415 model:Basic++ -->
**Front:** <div>What <b>fundamental concept</b> allows Kubernetes to maintain the desired state declared by the user?</div><div><br></div><div>A. Imperative Commands</div><div>B. Control Loop / Reconciliation</div><div>C. Manual Scaling</div><div>D. Direct Node Access</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div><div><b>Explanation</b>: Kubernetes controllers operate on control loops, constantly comparing the desired state (from API objects) with the actual cluster state.</div>

---

<!-- note:1756925071592 model:Basic++ -->
**Front:** <div>Which architectural component ensures that the actual state of cluster resources converges towards the desired state defined in their specifications?</div><div><br></div><div>A. kube-apiserver</div><div>B. kube-scheduler</div><div>C. Controllers (within kube-controller-manager)</div><div>D. kubelet</div><div>E. etcd</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: Controllers implement reconciliation loops. They watch the desired state via the API server and interact with resources to make the current state match the desired state (e.g., ReplicaSet controller ensuring the right number of Pods exist).</div>

---

<!-- note:1756925176676 model:Basic++ -->
**Front:** <div>A Pod specification includes two containers: one web server and one log shipper. How do these containers communicate efficiently over the network within the Pod?</div><div><br></div><div>A. Via a Kubernetes Service</div><div>B. Via the node’s primary IP address</div><div>C. Via localhost and shared network namespace</div><div>D. Via an automatically created NetworkPolicy</div><div>E. Via distinct Pod IP addresses assigned to each container</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: Containers within the same Pod share the same network namespace, meaning they can communicate using localhost and standard inter-process communication mechanisms as if they were on the same machine.</div>

---

<!-- note:1756925241301 model:Basic++ -->
**Front:** <div>What is <b>the primary role</b> of kubelet on a worker node?</div><div><br></div><div>A. To schedule Pods onto the node</div><div>B. To store the state of Pods running on the node</div><div>C. To ensure containers described in PodSpecs assigned to its node are running</div><div>D. To manage network routing rules for Services</div><div>E. To authenticate API requests originating from the node</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: The kubelet is the primary node agent. It receives Pod-Specs from the API server and interacts with the container runtime (e.g., containerd) to start, stop, and manage the containers defined in those Pods, reporting their status back to the control plane.</div>

---

<!-- note:1756925435597 model:Basic++ -->
**Front:** <div>Which Kubernetes resource provides a mechanism for grouping API objects and providing a scope for names?</div><div><br></div><div>A. Label</div><div>B. Annotation</div><div>C. Namespace</div><div>D. Deployment</div><div>E. ServiceAccount</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: Namespaces create logical partitions within a cluster, allowing teams or applications to operate independently. Resource names must be unique within a Namespace, but not necessarily across the entire cluster.</div>

---

<!-- note:1756925508788 model:Basic++ -->
**Front:** <div>When interacting with the Kubernetes API server using kubectl, what is the typical format used for defining resource manifests?</div><div><br></div><div>A. JSON</div><div>B. XML</div><div>C. YAML</div><div>D. Protocol Buffers</div><div>E. Plain Text</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: While the API server can accept JSON, YAML is the overwhelmingly conventional and human-readable format used in configuration files (manifests) passed to kubectl for creating or updating resources.</div>

---

<!-- note:1756925566796 model:Basic++ -->
**Front:** <div>What core Kubernetes concept allows Deployments to perform rolling updates with zero downtime?</div><div><br></div><div>A. Managing StatefulSets</div><div>B. Utilizing PersistentVolumes</div><div>C. Incrementally replacing Pods managed by ReplicaSets</div><div>D. Direct communication with the kube-scheduler</div><div>E. Modifying NetworkPolicy rules dynamically</div>
**Back:** Correct Answer: <b>C<br><br></b><div><div><b>Explanation</b>: Deployments manage ReplicaSets. During a rolling update, a Deployment creates a new ReplicaSet with the updated Pod template and gradually scales it up while scaling down the old ReplicaSet, ensuring service availability throughout the process.</div></div>

---

<!-- note:1756926055697 model:Basic++ -->
**Front:** <div>Which component is responsible for making the ultimate decision about which node a newly created Pod should run on?</div><div><br></div><div>A. kubelet</div><div>B. kube-apiserver</div><div>C. kube-scheduler</div><div>D. kube-controller-manager</div><div>E. The Pod’s ServiceAccount</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: The kube-scheduler watches for Pods without an assigned node and selects the most suitable node based on filtering (resource requests, affinity rules, etc.) and scoring algorithms.</div>

---

<!-- note:1756926105669 model:Basic++ -->
**Front:** <div>How does Kubernetes typically handle the failure of a container within a Pod?</div><div><br></div><div>A. By deleting the entire Pod immediately</div><div>B. By restarting the failed container based on the Pod’s restartPolicy</div><div>C. By scheduling a new Pod on a different node</div><div>D. By marking the Node as unschedulable</div><div>E. By alerting the kube-scheduler to find a replacement container</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><b><br></b></div><div><b>Explanation</b>: The kubelet monitors container health. If a container fails, the kubelet restarts it according to the Pod’s restartPolicy (Always, OnFailure, Never). The Pod itself continues to exist on the same node.</div>

---

<!-- note:1756926212662 model:Basic++ -->
**Front:** <div>What distinguishes a Kubernetes Secret from a ConfigMap?</div><div><br></div><div>A. Secrets are namespaced, ConfigMaps are not</div><div>B. ConfigMaps store configuration data, Secrets store sensitive data (base64 encoded)</div><div>C. Secrets can only be mounted as environment variables, ConfigMaps as files</div><div>D. ConfigMaps are automatically encrypted at rest, Secrets are not</div><div>E. Secrets are immutable once created, ConfigMaps are mutable</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div><div><b>Explanation</b>: Both are used for configuration, but Secrets are intended for sensitive information (passwords, keys) and are stored base64 encoded (not truly encrypted by default in etcd, though). ConfigMaps are for nonsensitive configuration data. Both are namespaced and can be mounted in multiple ways.</div>

---

<!-- note:1756926291465 model:Basic++ -->
**Front:** <div>Which of the following is NOT a standard component of the Kubernetes control plane?</div><div><br></div><div>A. etcd</div><div>B. kube-apiserver</div><div>C. kube-scheduler</div><div>D. containerd</div><div>E. kube-controller-manager</div>
**Back:** <div>Correct Answer: <b>D</b></div><div><br></div><div><b>Explanation</b>: containerd is a container runtime; it typically runs on worker nodes (managed by the kubelet) to handle container execution, not as part of the central control plane.</div>

---

<!-- note:1756926351473 model:Basic++ -->
**Front:** <div>What is the purpose of labels in Kubernetes?</div><div><br></div><div>A. To provide detailed descriptive information about a resource</div><div>B. To define network access rules between resources</div><div>C. To attach identifying metadata for selection and organization</div><div>D. To specify resource requests and limits for containers</div><div>E. To store multi-line configuration data</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: Labels are key/value pairs attached to objects (like Pods, Services) used to organize resources and allow users/controllers to select subsets of objects (e.g., a Service selecting Pods with app=backend).</div>

---

<!-- note:1756926597995 model:Basic++ -->
**Front:** <div>If a Pod needs access to specific hardware features available only on certain nodes, which scheduling mechanism is most suitable?</div><div><br></div><div>A. ResourceQuota</div><div>B. NetworkPolicy</div><div>C. PodDisruptionBudget</div><div>D. Taints and Tolerations or Node Affinity</div><div>E. HorizontalPodAutoscaler</div>
**Back:** <div>Correct Answer: <b>D</b><br><br></div><div><b>Explanation</b>: Taints applied to nodes repel Pods that don’t Tolerate them. Node Affinity allows Pods to express preferences or requirements for nodes based on node labels (which can represent hardware features, location, etc.). Both help ensure Pods land on appropriate nodes.</div>

---

<!-- note:1756926659613 model:Basic++ -->
**Front:** <div>Which API object represents a single point of access to a set of Pods providing the same functionality, acting as an internal load balancer?</div><div><br></div><div>A. Ingress</div><div>B. EndpointSlice</div><div>C. Service</div><div>D. ReplicaSet</div><div>E. NetworkPolicy</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: A Service defines a logical set of Pods (usually selected by labels) and provides a stable IP address and DNS name. kube-proxy ensures traffic to the Service IP is load-balanced across the healthy backend Pods.</div>

---

<!-- note:1756926793331 model:Basic++ -->
**Front:** <div>What is the relationship between a Deployment and a ReplicaSet?</div><div><br></div><div>A. A ReplicaSet manages multiple Deployments</div><div>B. A Deployment watches ReplicaSets for scaling signals</div><div>C. A Deployment declaratively manages ReplicaSets to orchestrate Pod updates</div><div>D. ReplicaSets are used only for stateful applications, Deployments for stateless</div><div>E. They are independent controllers managing Pod lifecycles</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: A Deployment provides declarative updates for Pods and ReplicaSets. It creates and manages ReplicaSets, handling rolling updates or rollbacks by manipulating the desired replica count of underlying ReplicaSets. You typically interact with Deployments, not ReplicaSets directly.</div>

---

<!-- note:1756926869853 model:Basic++ -->
**Front:** <div>The Kubernetes API server performs several actions when receiving a request. Which action verifies if the authenticated user is allowed to perform the requested operation?</div><div><br></div><div>A. Authentication</div><div>B. Admission Control</div><div>C. Authorization</div><div>D. Rate Limiting</div><div>E. Validation</div>
**Back:** <div>Correct Answer: <b>C</b><br><br></div><div><b>Explanation</b>: After Authentication (who are you?), Authorization (e.g., via RBAC) checks if the identified user has the necessary permissions (Role/ClusterRole bindings) to perform the action (e.g., create, get, delete) on the specific resource (e.g., pods) in the target namespace.</div>

---

<!-- note:1756926940156 model:Basic++ -->
**Front:** <div>What is <b>the primary function </b>of etcd within the Kubernetes architecture?</div><div><br></div><div>A. To run the container runtime interface</div><div>B. To schedule Pods across available nodes</div><div>C. To provide reliable, distributed storage for cluster state and configuration</div><div><div>D. To manage network policies and ingress rules</div><div>E. To execute health checks against running containers</div></div>
**Back:** <div>Correct Answer: <b>C</b></div><div><b><br></b></div><div>Explanation: etcd is the consistent key-value store that acts as the source of truth for the entire cluster. All configuration, state, and metadata are persisted here, ensuring consistency across the control plane.</div>

---

<!-- note:1756926999351 model:Basic++ -->
**Front:** <div>Which field in a Pod’s specification is crucial for the kubescheduler to determine if a node has sufficient resources?</div><div><br></div><div>A. spec.nodeName</div><div>B. spec.containers[].ports</div><div>C. spec.containers[].resources.requests</div><div>D. spec.serviceAccountName</div><div>E. spec.restartPolicy</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: The resources.requests field (for CPU and memory) indicates the minimum amount of resources the container needs. The scheduler uses this to filter out nodes that cannot meet these requests.</div>

---

<!-- note:1756927077574 model:Basic++ -->
**Front:** <div>What fundamental concept allows Kubernetes controllers to operate effectively without needing constant instructions?</div><div><br></div><div>A. Imperative command execution</div><div>B. The reconciliation loop (Control Loop)</div><div>C. Direct manipulation of etcd</div><div>D. Event-driven webhooks</div><div>E. Stateful session management</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div><div><b>Explanation</b>: Controllers continuously watch the desired state (from the API server) and the current state (observed in the cluster), taking actions (via the API server) to make the current state match the desired state. This is the core principle of Kubernetes automation.</div>

---

<!-- note:1756927666027 model:Basic++ -->
**Front:** <div>You need to provide non-sensitive configuration data (like a URL endpoint or logging level) to a Pod. Which resource is most appropriate?</div><div><br></div><div>A. Secret</div><div>B. ConfigMap</div><div>C. Annotation</div><div><div>D. ResourceQuota</div><div>E. DownwardAPI</div></div>
**Back:** Correct Answer: <b>B</b><br><br><div><div><b>Explanation</b>: ConfigMaps are designed specifically for decoupling nonsensitive configuration artifacts from container images, allowing configurations to be managed independently.</div></div>

---

<!-- note:1756927728581 model:Basic++ -->
**Front:** <div>If you want a specific Pod to run on every node in the cluster (or a subset matching certain criteria), which workload resource should you use?</div><div><br></div><div>A. Deployment</div><div>B. StatefulSet</div><div>C. DaemonSet</div><div>D. Job</div><div>E. ReplicaSet</div>
**Back:** <div>Correct Answer: <b>C</b><br><br></div><div><b>Explanation</b>: A DaemonSet ensures that a copy of a Pod runs on all (or some specified) nodes. This is useful for node-level agents like log collectors, monitoring agents, or CNI plugins.</div>

---

<!-- note:1756927776723 model:Basic++ -->
**Front:** <div>What does it mean for the Kubernetes API to be ”declarative”?</div><div><br></div><div>A. API calls must be made sequentially</div><div>B. Users specify the desired end state, not the steps to reach it</div><div>C. The API only accepts YAML formatted requests</div><div>D. API responses always include the full resource specification</div><div>E. The API can only create resources, not update or delete them</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div><div><b>Explanation</b>: Users declare the desired state of resources (e.g., ”I want 3 replicas of this Pod”). Kubernetes controllers then figure out the sequence of actions needed to achieve and maintain that state. Contrast this with imperative approaches (”run container X”, ”scale up by 1”).</div>

---

<!-- note:1756927897147 model:Basic++ -->
**Front:** <div>Which mechanism prevents the kube-scheduler from placing Pods on a Node that is undergoing maintenance or is otherwise unsuitable?</div><div><br></div><div>A. ResourceQuotas</div><div>B. NetworkPolicies</div><div>C. Taints on the Node and Tolerations on the Pod</div><div>D. PodDisruptionBudgets</div><div>E. PriorityClasses</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div>Explanation: A Taint applied to a Node repels Pods. Pods can express Tolerations for specific taints, allowing them to be scheduled onto those nodes. This is commonly used to cordon nodes for maintenance or dedicate nodes for specific workloads.</div>

---

<!-- note:1756928054009 model:Basic++ -->
**Front:** <div>What part of the Kubernetes system is responsible for managing the lifecycle of EndpointSlice objects, which track Pod IPs for Services?</div><div><br></div><div>A. kube-proxy</div><div>B. kubelet</div><div><div>C. endpointslice-controller (within kube-controller-manager)</div><div>D. kube-scheduler</div><div>E. coredns / kube-dns</div></div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: The endpointslice-controller (part of kube-controller-manager) watches Services and their selector-matched Pods, creating and managing EndpointSlices to store the Pod IP addresses and port information efficiently. kube-proxy consumes this information.</div>

---

<!-- note:1756928114363 model:Basic++ -->
**Front:** <div>Which component translates a Service’s virtual IP address into actual Pod IP addresses on each node?</div><div><br></div><div>A. etcd</div><div>B. kube-apiserver</div><div>C. coredns / kube-dns</div><div>D. kube-proxy</div><div>E. kubelet</div>
**Back:** <div>Correct Answer: <b>D</b></div><div><br></div><div><b>Explanation</b>: kube-proxy, running on each node, watches Services and Endpoints/EndpointSlices. It programs network rules (e.g., iptables, IPVS) to intercept traffic destined for a Service’s ClusterIP and directs it to one of the healthy backend Pod IPs.</div>

---

<!-- note:1756928185613 model:Basic++ -->
**Front:** <div>A <b>StatefulSet </b>is often preferred over a <b>Deployment </b>for running databases. Why?</div><div><br></div><div>A. StatefulSets have simpler configuration</div><div>B. Deployments cannot use Persistent Storage</div><div>C. StatefulSets provide stable, unique network IDs and persistent storage per Pod</div><div>D. Deployments automatically handle database schema migrations</div><div>E. StatefulSets require less CPU and memory resources</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: StatefulSets provide guarantees crucial for stateful apps: stable network identifiers (e.g., db-0, db-1), stable persistent storage linked to each identity, and ordered, graceful deployment and scaling.</div>

---

<!-- note:1756928322133 model:Basic++ -->
**Front:** <div>Which kubectl command is used to view the logs of a running container within a Pod?</div><div><br></div><div>A. kubectl get pod &lt;pod-name&gt; –logs</div><div>B. kubectl describe pod &lt;pod-name&gt;</div><div>C. kubectl logs &lt;pod-name&gt; [-c &lt;container-name&gt;]</div><div><div>D. kubectl attach &lt;pod-name&gt; -c &lt;container-name&gt;</div><div>E. kubectl exec &lt;pod-name&gt; – tail /var/log/messages</div></div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: kubectl logs fetches the logs (stdout/stderr) from a specified container within a Pod. The -c flag is needed if the Pod has multiple containers.</div>

---

<!-- note:1756928383492 model:Basic++ -->
**Front:** <div>What is the function of an Admission Controller in the Kubernetes API request lifecycle?</div><div><br></div><div>A. To authenticate the user making the request</div><div>B. To authorize the requested operation</div><div>C. To mutate or validate API objects before they are persisted in etcd</div><div>D. To schedule the Pod onto a suitable node</div><div>E. To route network traffic to the correct Pod</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: Admission Controllers intercept API requests after authentication and authorization but before persistence. They can mutate objects (e.g., inject sidecars, set default values) or validate them (e.g., enforce security policies, check resource quotas).</div>

---

<!-- note:1756928499293 model:Basic++ -->
**Front:** <div>Which resource defines constraints on the total amount of compute resources (CPU, memory) that can be consumed within a specific Namespace?</div><div><br></div><div>A. LimitRange</div><div>B. ResourceQuota</div><div>C. NetworkPolicy</div><div>D. PodSecurityPolicy / PodSecurityAdmission</div><div>E. PriorityClass</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div><div><b>Explanation</b>: A ResourceQuota limits the aggregate resource consumption (CPU, memory, storage, object counts) within a Namespace, preventing overuse and ensuring fair sharing among users or teams.</div>

---

<!-- note:1756928551587 model:Basic++ -->
**Front:** <div>Consider a Pod that needs to perform a <b>one-time initialization task</b> before its main application container starts. Which container type is best suited for this?</div><div><br></div><div>A. Sidecar Container</div><div>B. Ephemeral Container</div><div>C. Init Container</div><div>D. Main Application Container</div><div>E. Job Container</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: Init Containers run sequentially before the main application containers in a Pod start. They must complete successfully for the main containers to launch, making them ideal for setup tasks like database schema migration, fetching configuration, or waiting for dependencies.</div>

---

<!-- note:1756928671928 model:Basic++ -->
**Front:** <div>What is the purpose of the metadata.ownerReferences field in a Kubernetes object?</div><div><br></div><div>A. To specify the user who created the object</div><div>B. To link the object to its managing controller (e.g., ReplicaSet to Deployment)</div><div><div>C. To list labels used for selecting the object</div><div>D. To store annotations related to the object’s owner</div><div>E. To define the Namespace the object belongs to</div></div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div><div><b>Explanation</b>: ownerReferences create parent-child relationships between objects. This enables cascading deletion (deleting the owner deletes dependents) and helps controllers identify the objects they manage. For example, a ReplicaSet Pod will have an ownerReference pointing to the ReplicaSet.</div>

---

<!-- note:1756928832974 model:Basic++ -->
**Front:** <div>Which control plane component is primarily responsible for running controllers like the Node Controller, Deployment Controller, and Service Controller?</div><div><br></div><div>A. etcd</div><div>B. kube-apiserver</div><div>C. kube-scheduler</div><div>D. kube-controller-manager</div><div>E. cloud-controller-manager</div>
**Back:** <div>Correct Answer: <b>D</b></div><div><br></div><div><b>Explanation</b>: The kube-controller-manager bundles core Kubernetes controllers into a single binary. It runs controllers that handle node lifecycle, workload management (Deployments, ReplicaSets), service endpoints, namespace creation, etc.</div>

---

<!-- note:1756928902002 model:Basic++ -->
**Front:** <div>What is the purpose of a LimitRange object within a Namespace?</div><div><br></div><div>A. To limit the total resource usage of the entire Namespace</div><div><div>B. To set default resource requests/limits for containers and validate min/max bounds</div><div>C. To restrict network traffic between Pods in the Namespace</div><div>D. To control which users can create resources in the Namespace</div><div>E. To define storage quotas for PersistentVolumeClaims</div></div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div><div><b>Explanation</b>: A LimitRange operates at the container/Pod level within a Namespace. It can enforce minimum/maximum resource constraints and specify default request/limit values if they aren’t explicitly set in the Pod spec. ResourceQuota limits the Namespace total.</div>

---

<!-- note:1756928949262 model:Basic++ -->
**Front:** <div>Which kubectl command would you use to apply a configuration defined in my-app.yaml declaratively?</div><div><br></div><div>A. kubectl create -f my-app.yaml</div><div>B. kubectl replace -f my-app.yaml</div><div>C. kubectl apply -f my-app.yaml</div><div>D. kubectl patch -f my-app.yaml</div><div>E. kubectl run -f my-app.yaml</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: kubectl apply is the standard command for declarative resource management. It creates resources if they don’t exist or calculates and applies necessary changes if they do, based on the definition in the file.</div>

---

<!-- note:1756928999786 model:Basic++ -->
**Front:** <div>How does the kube-scheduler handle Pods with defined affinity rules?</div><div><br></div><div>A. It ignores affinity rules if resource requests cannot be met.</div><div>B. It uses affinity rules as the primary factor for node selection.</div><div>C. It considers affinity/anti-affinity rules during the filtering and scoring phases.</div><div>D. It delegates affinity processing to the kubelet.</div><div>E. It only processes podAffinity, not nodeAffinity.</div>
**Back:** <div>Correct Answer: <b>C</b><br><br></div><div><b>Explanation</b>: Affinity rules (node and inter-pod) influence scheduling decisions. Required affinity rules act as filters (nodes must match). Preferred affinity rules contribute to the scoring phase (nodes matching preferred rules get higher scores).</div>

---

<!-- note:1756929672400 model:Basic++ -->
**Front:** <div>What is the concept of "desired state reconciliation" fundamental to Kubernetes?</div><div><br></div><div>A. Users manually reconcile cluster state using kubectl.</div><div>B. Controllers continuously observe and work to match actual state to declared state.</div><div>C. etcd automatically corrects discrepancies between desired and actual state.</div><div>D. kubelet reconciles container state based solely on node health.</div><div>E. The API server rejects any configuration that deviates from the current state.</div>
**Back:** Correct Answer:<br><br>

---

<!-- note:1767559651445 model:Basic+++ -->
**Front:** Which of the following is a built-in Kubernetes resource for scheduling pods on nodes?<br><br>A. Deployment<br>
B. Ingress<br>
C. Service<br>
D. DaemonSet
**Back:** <div>Correct Answer: <b>D</b></div><div><br></div>
<div><b>Explanation</b>: A DaemonSet ensures that a copy of a Pod runs on all (or selected) nodes in the cluster, commonly used for system-level workloads like logging or monitoring agents.</div>

---

<!-- note:1767559707187 model:Basic+++ -->
**Front:** What Kubernetes resource is used to expose an application running on a set of pods as a network service<br><br>A. ReplicaSet<br>
B. Job<br>
C. Service<br>
D. CronJob
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div>
<div><b>Explanation</b>: A Service provides a stable network endpoint and load-balancing for accessing a group of Pods.</div>

---

<!-- note:1767559725017 model:Basic+++ -->
**Front:** What is the primary component of a Kubernetes control plane that manages API requests?<br><br>A. Kube-scheduler<br>
B. Kube-controller-manager<br>
C. Etcd<br>
D. Kube-apiserver
**Back:** <div>Correct Answer: <b>D</b></div><div><br></div>
<div><b>Explanation</b>: The kube-apiserver is the central component that exposes the Kubernetes API and handles all API requests.</div>

---

<!-- note:1767559754902 model:Basic+++ -->
**Front:** Which component of a Kubernetes node <b>is responsible for</b> managing network rules and IP addresses?<br><br>A. Kubelet<br>
B. Kubectl<br>
C. Kube-proxy<br>
D. Container runtime
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div>
<div><b>Explanation</b>: Kube-proxy manages networking rules and enables service-to-pod communication within the cluster.</div>

---

<!-- note:1767559778182 model:Basic+++ -->
**Front:** Which component of the Kubernetes control plane exposes the RESTful API for managing the cluster?<br><br>A. kube-scheduler<br>
B. kube-controller-manager<br>
C. kube-apiserver<br>
D. etcd
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div>
<div><b>Explanation</b>: The kube-apiserver exposes the REST API and acts as the primary entry point for all cluster operations.</div>

---

<!-- note:1767559844816 model:Basic+++ -->
**Front:** What is the primary advantage of using containers in application deployment?<br><br>A. Higher hardware efficiency<br> B. Isolation of applications and dependencies<br> C. Larger application size<br> D. Conversion into virtual machines<div></div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div> <div><b>Explanation</b>: Containers package applications with their dependencies, ensuring isolation and consistency across environments.</div>

---

<!-- note:1767559892668 model:Basic+++ -->
**Front:** Which component determines which nodes can run a pod? <br><br><div>A. Kubelet<br> B. Kube-scheduler<br> C. Pod controller<br> D. Node selector</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div> <div><b>Explanation</b>: The kube-scheduler selects the most suitable node for a Pod based on scheduling policies and constraints.</div>

---

<!-- note:1767559942363 model:Basic+++ -->
**Front:** What role does a node’s taint play in scheduling?<br><br>A. Allows pods with matching tolerations<div> B. Prevents all pods from running<br> C. Improves node performance<br> D. Limits pod resources</div>
**Back:** <div>Correct Answer: <b>A</b></div><div><br></div> <div><b>Explanation</b>: Taints repel Pods unless they have matching tolerations, controlling which Pods can be scheduled on a node.</div>

---

<!-- note:1767559998923 model:Basic+++ -->
**Front:** Which component maintains the desired state of applications? <br><br><div>A. Controller Manager<br> B. Kubelet<br> C. Etcd<br> D. Docker Daemon</div>
**Back:** <div>Correct Answer: <b>A</b></div><div><br></div> <div><b>Explanation</b>: Controllers continuously reconcile the desired state with the actual cluster state.</div>

---

<!-- note:1767560083143 model:Basic+++ -->
**Front:** What is the purpose of Pod Security Policies? <br><br><div>A. Network traffic control<br> B. Enforce pod execution rules<br> C. Auto-scale pods<br> D. Manage storage</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div> <div><b>Explanation</b>: Pod Security Policies define security constraints for pod execution (deprecated but relevant conceptually).</div>

---

<!-- note:1767560140559 model:Basic+++ -->
**Front:** Which resource exposes services to external traffic? <br><br><div>A. DaemonSet<br> B. ConfigMap<br> C. Ingress<br> D. PersistentVolume</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div> <div><b>Explanation</b>: Ingress manages external HTTP/HTTPS access to services.</div>

---

<!-- note:1767561170543 model:Basic+++ -->
**Front:** What is the purpose of HPA? <br><br><div>A. Scale nodes<br> B. Scale pods<br> C. Upgrade API server<br> D. Provide storage</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div> <div><b>Explanation</b>: HPA automatically adjusts the number of Pods based on metrics like CPU usage.</div>

---

<!-- note:1767561230837 model:Basic+++ -->
**Front:** Which component provides metrics for autoscaling? <br><br><div>A. Kube-scheduler<br> B. Controller Manager<br> C. Metrics Server<br> D. Kubelet</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div> <div><b>Explanation</b>: Metrics Server collects resource usage metrics used by HPA.</div>

---

<!-- note:1793752906100 model:Many -->
**Domain:** Cluster Architecture - Control Plane
**Question:** Which of these components runs ONLY on control-plane nodes, not on worker nodes?
**Options:** A. kubelet<br>B. container runtime<br>C. kube-apiserver<br>D. kube-proxy
**Answer:** C (3) – kube-apiserver
**Explanation:** kube-apiserver, etcd, kube-scheduler and kube-controller-manager run only on control-plane nodes — they manage the cluster. kubelet, kube-proxy and the container runtime run on every node (workers AND control plane) so any node can host pods.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/components/" target="_blank">Kubernetes Documentation - Kubernetes Components</a>
**Tags:** k8s::kcna topic::architecture topic::control-plane src::session

---

<!-- note:1793752906116 model:Basic -->
**Front:** What is the difference between a control-plane node and a worker node in Kubernetes?
**Back:** Control-plane nodes run the cluster's management components — kube-apiserver, etcd, kube-scheduler, kube-controller-manager — and normally run no user workloads (protected by a taint). Worker nodes run the application pods: each has kubelet, kube-proxy and a container runtime. Every node needs the per-node components; only control-plane nodes need the management stack.
**Tags:** k8s::kcna topic::architecture topic::control-plane src::session

---

<!-- note:1793752918693 model:Cloze -->
**Text:** Control plane nodes were previously called {{c1::master}} nodes.
**Back Extra:** The old term 'master node' is still common in older courses, books and docs — e.g. 'master components'. Same thing; 'control plane' is the current name.
**Tags:** k8s::kcna topic::architecture topic::control-plane src::session

---
