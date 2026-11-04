# KCNA - Kubernetes and Cloud Native Associate — Kubernetes Fundamentals

> Deck: `KCNA - Kubernetes and Cloud Native Associate` · Group: `Kubernetes Fundamentals` · Notes: 142 · Models: Basic++, Basic+++, Basic, Basic (and reversed card), Cloze, Many

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

<!-- note:1793753105610 model:Many -->
**Domain:** Cluster Architecture - etcd
**Question:** What is the role of etcd in a Kubernetes cluster?
**Options:** A. It implements locks to prevent conflicts between the masters.<br>B. It ensures distributed storage of information across all nodes in the cluster.<br>C. All of the options are correct<br>D. It stores all the data used to manage the cluster.
**Answer:** C (3) – All of the options are correct
**Explanation:** Per the course framing, all three describe etcd: it stores ALL data used to manage the cluster (D), it keeps that data as distributed replicated storage so control-plane nodes share one consistent view (B), and its distributed consensus — leader election/quorum via Raft, described as 'locks' — prevents conflicting writes between the masters (A). Nuance for the real world: etcd members run only on control-plane nodes ('all nodes' is loose phrasing for the etcd members), and 'locks' really means Raft consensus, not literal locking.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/components/" target="_blank">Kubernetes Documentation - Kubernetes Components</a>
**Tags:** k8s::kcna topic::architecture topic::etcd src::session

---

<!-- note:1793754672883 model:Many -->
**Domain:** kubectl explain
**Question:** Which kubectl command shows documentation for a resource's fields, e.g. <code>kubectl explain pod.spec.containers</code>?
**Options:** A. kubectl describe<br>B. kubectl explain<br>C. kubectl doc<br>D. kubectl get -o yaml
**Answer:** B (2) – kubectl explain
**Explanation:** kubectl explain prints the schema/documentation for a resource's fields — e.g. kubectl explain deployment.spec.strategy describes every field, its type and meaning. It's the built-in way to answer 'what does this manifest field do' without leaving the terminal.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/generated/kubectl_explain/" target="_blank">Kubernetes Documentation - kubectl explain</a>
**Tags:** k8s::kcna topic::kubectl topic::yaml src::session

---

<!-- note:1793754672884 model:Many -->
**Domain:** Manifest Structure
**Question:** Which four top-level fields are required in every Kubernetes object manifest?
**Options:** A. name, image, replicas, port<br>B. apiVersion, metadata, spec, status<br>C. apiVersion, kind, metadata and spec<br>D. kind, spec, status, data
**Answer:** C (3) – apiVersion, kind, metadata and spec
**Explanation:** Every manifest needs all four top-level fields: apiVersion (API group+version, e.g. apps/v1), kind (object type → its schema), metadata (name/namespace/labels), spec (the desired state — its contents depend on the kind). status exists too but is written by Kubernetes, not required in your file.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/" target="_blank">Kubernetes Documentation - Objects In Kubernetes</a>
**Tags:** k8s::kcna topic::api topic::yaml src::session

---

<!-- note:1793754672885 model:Many -->
**Domain:** kubectl run
**Question:** Which command creates a pod named 'nginx' running the nginx image?
**Options:** A. kubectl create pod nginx<br>B. kubectl run nginx --image=nginx<br>C. kubectl deploy nginx --image=nginx<br>D. kubectl start nginx --image=nginx
**Answer:** B (2) – kubectl run nginx --image=nginx
**Explanation:** kubectl run creates a single pod; --image names the container image to pull (Docker Hub by default — use a full registry path for private repos). kubectl create pod is also valid; deploy/start are not pod commands. Deployments come from kubectl create deployment.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/pods/" target="_blank">Kubernetes Documentation - Pods</a>
**Tags:** k8s::kcna topic::kubectl topic::pods src::session

---

<!-- note:1793754672890 model:Cloze -->
**Text:** Minimal pod manifest:<br><br><code>apiVersion: {{c1::v1}}<br>kind: {{c2::Pod}}<br>metadata:<br>&nbsp;&nbsp;{{c3::name}}: nginx<br>spec:<br>&nbsp;&nbsp;{{c4::containers}}:<br>&nbsp;&nbsp;- name: nginx<br>&nbsp;&nbsp;&nbsp;&nbsp;{{c5::image}}: nginx</code>
**Back Extra:** v1 = core API group (named groups use group/version, e.g. apps/v1 for Deployments). metadata.name is how you identify the pod; spec.containers is a LIST (note the dash) — even a single-container pod needs the list item.
**Tags:** k8s::kcna topic::pods topic::yaml src::session

---

<!-- note:1793754672900 model:Basic -->
**Front:** How do you list pods with kubectl, and what do the flags <code>-o wide</code>, <code>-A</code> and <code>-w</code> add?
**Back:** <code>kubectl get pods</code> lists pods in the current namespace with status. Useful variants: <code>-o wide</code> (adds pod IPs + which node each runs on), <code>-A</code>/<code>--all-namespaces</code> (every namespace), <code>-w</code> (watch for changes). For detail on one pod incl. events: <code>kubectl describe pod &lt;name&gt;</code>.
**Tags:** k8s::kcna topic::kubectl topic::pods src::session

---

<!-- note:1793755549227 model:Many -->
**Domain:** Imperative vs Declarative - apply
**Question:** Which of these is the DECLARATIVE object-management approach in Kubernetes?
**Options:** A. kubectl create deployment web --image=nginx<br>B. kubectl replace -f deployment.yaml<br>C. kubectl apply -f deployment.yaml<br>D. kubectl edit deployment web
**Answer:** C (3) – kubectl apply -f deployment.yaml
**Explanation:** apply -f is the DECLARATIVE path: it merges the file's desired state into the live object and records last-applied-configuration to compute future diffs. create/replace -f are the middle tier ('imperative object configuration' — file-driven but verb-led: create fails if it exists, replace swaps the whole object). create/edit/run/expose are pure imperative commands.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna topic::kubectl topic::yaml src::session

---

<!-- note:1793755549228 model:Many -->
**Domain:** Imperative vs Declarative - commands
**Question:** Which group contains ONLY imperative commands (no manifest file involved)?
**Options:** A. kubectl run, kubectl create deployment, kubectl expose<br>B. kubectl apply -f, kubectl diff<br>C. kubectl create -f, kubectl replace -f<br>D. kubectl get, kubectl describe
**Answer:** A (1) – kubectl run, kubectl create deployment, kubectl expose
**Explanation:** Imperative commands tell the cluster WHAT to do right now: run, create deployment, expose, scale, delete — no file, no recorded desired state. The -f variants of create/replace are imperative object configuration (middle tier); apply -f is the declarative tier. get/describe are read-only, not management.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna topic::kubectl topic::yaml src::session

---

<!-- note:1793755549229 model:Many -->
**Domain:** Imperative vs Declarative - why
**Question:** Why is the declarative approach preferred for production and GitOps workflows?
**Options:** A. It executes faster than imperative commands<br>B. Manifests live in Git as a reviewable source of truth, and apply is idempotent and detects drift via last-applied-configuration<br>C. Imperative commands cannot create objects<br>D. The API server only accepts YAML
**Answer:** B (2) – Manifests live in Git as a reviewable source of truth, and apply is idempotent and detects drift via last-applied-configuration
**Explanation:** Declarative YAML can be versioned, reviewed and audited in Git (the GitOps model), re-applied safely (idempotent), and apply's last-applied annotation reveals drift. Imperative commands leave no record — nothing to diff, review or re-converge from.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna topic::gitops topic::kubectl src::session

---

<!-- note:1793756257574 model:Basic (and reversed card) -->
**Front:** What is the IMPERATIVE approach to managing infrastructure or Kubernetes objects?
**Back:** The approach where you spell out WHAT you want AND HOW to get there — every step explicitly, in order (<code>run this</code>, <code>create that</code>, <code>scale this to 5</code>). The tool executes commands; it doesn't reason about an end state. Examples: kubectl run/create/expose/scale/edit/set image — and shell scripts in the DevOps world.
**Tags:** k8s::kcna topic::declarative topic::kubectl src::session

---

<!-- note:1793756257575 model:Basic (and reversed card) -->
**Front:** What is the DECLARATIVE approach to managing infrastructure or Kubernetes objects?
**Back:** The approach where you describe only WHAT the end state should look like — a manifest of desired state — and the system works out the HOW itself (diff, plan, reconcile). Examples: <code>kubectl apply -f</code>, Terraform plans, Kubernetes controllers converging actual→desired state.
**Tags:** k8s::kcna topic::declarative topic::kubectl src::session

---

<!-- note:1793756257583 model:Many -->
**Domain:** Imperative vs Declarative - DevOps
**Question:** You write a Terraform config describing what infrastructure SHOULD exist, and Terraform works out the steps to reach it. Which approach is this?
**Options:** A. Imperative<br>B. Declarative<br>C. Procedural<br>D. Manual
**Answer:** B (2) – Declarative
**Explanation:** Terraform is the classic declarative IaC tool: you write config describing the END state (which resources should exist), and Terraform's engine computes the plan — what to create/change/destroy to get there. Same model as kubectl apply. Imperative tools/scripts instead encode each step to execute.
**Sources:** <a href="https://developer.hashicorp.com/terraform/intro" target="_blank">HashiCorp Documentation - What is Terraform</a>
**Tags:** k8s::kcna topic::declarative topic::gitops src::session

---

<!-- note:1793756257584 model:Many -->
**Domain:** Imperative vs Declarative - set image
**Question:** <code>kubectl set image deployment/web nginx=nginx:2.0</code> — which management approach is this?
**Options:** A. A declarative update<br>B. Imperative object configuration<br>C. An imperative command — it directly instructs the cluster to change the image NOW, with no declared desired state<br>D. A GitOps operation
**Answer:** C (3) – An imperative command — it directly instructs the cluster to change the image NOW, with no declared desired state
**Explanation:** set image, like run/create/expose/scale/edit/delete, is imperative: one-shot instruction, nothing recorded to converge against. The declarative equivalent is editing the image in the manifest and re-running kubectl apply -f.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna topic::declarative topic::kubectl src::session

---

<!-- note:1793756257585 model:Many -->
**Domain:** Imperative vs Declarative - apply mechanics
**Question:** You run <code>kubectl apply -f app.yaml</code> on an object that already exists. What does apply do?
**Options:** A. It fails because the resource already exists<br>B. It compares the manifest, the live object AND last-applied-configuration, then applies only the needed changes (create or patch)<br>C. It deletes and recreates the object from scratch<br>D. It replaces the whole object, losing unmanaged fields
**Answer:** B (2) – It compares the manifest, the live object AND last-applied-configuration, then applies only the needed changes (create or patch)
**Explanation:** apply is a three-way merge: file's desired state vs the object's live state vs the recorded last-applied-configuration. Object missing → created; exists → patched to match the declaration. That's why the same file can be applied repeatedly and why it's the declarative workflow.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna topic::declarative topic::kubectl src::session

---

<!-- note:1793756257586 model:Many -->
**Domain:** Imperative vs Declarative - contrast
**Question:** Which statement correctly contrasts the imperative and declarative approaches?
**Options:** A. Imperative describes the end state; declarative lists the steps<br>B. Imperative = you specify WHAT you want AND HOW (the steps); declarative = you specify only WHAT the result should be<br>C. They are two names for the same workflow<br>D. Declarative requires typing more commands
**Answer:** B (2) – Imperative = you specify WHAT you want AND HOW (the steps); declarative = you specify only WHAT the result should be
**Explanation:** Imperative: the operator encodes the path — every command/step explicitly. Declarative: the operator encodes the destination — the system derives the path (diff + reconcile). Kubernetes manifests+apply and Terraform are declarative; ad-hoc kubectl commands and shell scripts are imperative.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna topic::declarative topic::kubectl src::session

---

<!-- note:1793756656941 model:Many -->
**Domain:** kubectl apply - last-applied
**Question:** What does the <code>kubectl.kubernetes.io/last-applied-configuration</code> annotation on an object store?
**Options:** A. The object's current live spec<br>B. The JSON of the manifest most recently applied via kubectl apply<br>C. The default values the API server filled in<br>D. The object's original creation manifest from any tool
**Answer:** B (2) – The JSON of the manifest most recently applied via kubectl apply
**Explanation:** Each apply writes the applied manifest (as JSON) into the kubectl.kubernetes.io/last-applied-configuration annotation on the object. It's the third leg of apply's three-way merge — file vs live vs last-applied — letting kubectl compute diffs, detect drift, and delete fields removed from the file. kubectl get -o yaml shows LIVE state; this annotation remembers what YOU declared.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/" target="_blank">Kubernetes Documentation - Kubernetes Object Management</a>
**Tags:** k8s::kcna topic::declarative topic::kubectl topic::yaml src::session

---

<!-- note:1793756864965 model:Many -->
**Domain:** Namespaces - defaults
**Question:** Which namespaces exist in a fresh Kubernetes cluster by default?
**Options:** A. only 'default'<br>B. default, prod, staging<br>C. default, kube-system, kube-public, kube-node-lease<br>D. master, worker, default
**Answer:** C (3) – default, kube-system, kube-public, kube-node-lease
**Explanation:** Every cluster starts with four: 'default' (objects with no namespace set), 'kube-system' (the cluster's own infrastructure — CoreDNS, kube-proxy, control-plane pods in kubeadm clusters), 'kube-public' (publicly readable info, mostly unused), 'kube-node-lease' (node heartbeat Lease objects). Create your own for teams/apps via kubectl create ns.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Documentation - Namespaces</a>
**Tags:** k8s::kcna topic::architecture topic::namespaces src::session

---

<!-- note:1793756864966 model:Many -->
**Domain:** Namespaces - kubectl
**Question:** Which kubectl command makes 'dev' your DEFAULT namespace for all subsequent commands?
**Options:** A. kubectl use namespace dev<br>B. kubectl config set-context --current --namespace=dev<br>C. kubectl set namespace dev<br>D. kubectl switch-context dev
**Answer:** B (2) – kubectl config set-context --current --namespace=dev
**Explanation:** set-context --current --namespace=dev writes 'dev' into your kubeconfig's current context — every subsequent kubectl command defaults to it, no -n flag needed. The alternative is passing -n dev (or --namespace=dev) on each command. kubectl get ns lists namespaces; create ns makes one.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Documentation - Namespaces</a>
**Tags:** k8s::kcna topic::kubectl topic::namespaces src::session

---

<!-- note:1793756864967 model:Many -->
**Domain:** Namespaces - scoping
**Question:** Which of these resources is cluster-scoped — i.e. does NOT live inside a namespace?
**Options:** A. Pod<br>B. Service<br>C. Deployment<br>D. Node
**Answer:** D (4) – Node
**Explanation:** Nodes, PersistentVolumes, ClusterRoles — and Namespaces themselves — are cluster-scoped: they live outside any namespace (metadata.namespace must be empty). Pods, Services, Deployments, Secrets, ConfigMaps are namespaced. Discover which is which with kubectl api-resources --namespaced=true/false.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Documentation - Namespaces</a>
**Tags:** k8s::kcna topic::api topic::namespaces src::session

---

<!-- note:1793756864968 model:Many -->
**Domain:** Namespaces - isolation
**Question:** Do namespaces on their own provide hard isolation between workloads?
**Options:** A. Yes — namespaces fully isolate workloads from each other<br>B. No — namespaces are logical grouping; real isolation needs NetworkPolicy, RBAC and quotas on top<br>C. Yes — pods cannot communicate across namespaces<br>D. Only if ResourceQuota is configured
**Answer:** B (2) – No — namespaces are logical grouping; real isolation needs NetworkPolicy, RBAC and quotas on top
**Explanation:** Namespaces partition names and org ownership — but the pod network stays flat by default: a pod in ns 'dev' can still reach a pod in ns 'prod'. Hard isolation is layered on: NetworkPolicies for traffic, RBAC for API access, ResourceQuota/LimitRange for resources. Namespaces are the boundary those features scope to, not the isolation itself.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Documentation - Namespaces</a>
**Tags:** k8s::kcna topic::namespaces topic::networking src::session

---

<!-- note:1793757640845 model:Many -->
**Domain:** Namespaces - kube-system
**Question:** A fresh cluster's DNS pods (CoreDNS) and kube-proxy land in which namespace — deliberately separated from user workloads so they can't be accidentally deleted?
**Options:** A. default<br>B. kube-system<br>C. kube-public<br>D. kube-node-lease
**Answer:** B (2) – kube-system
**Explanation:** kube-system holds the cluster's own objects — CoreDNS, kube-proxy, and (in kubeadm clusters) the control-plane static pods. Putting them in their own namespace keeps them out of your 'kubectl get all' view and protects them from accidental deletion — you have to explicitly target -n kube-system. kube-public is for data readable by ALL users; kube-node-lease holds node heartbeats.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Documentation - Namespaces</a>
**Tags:** k8s::kcna topic::architecture topic::namespaces src::session

---

<!-- note:1793757640846 model:Many -->
**Domain:** Namespaces - DNS
**Question:** A pod in namespace 'dev' must reach the Service 'api' living in namespace 'prod'. Which DNS name works?
**Options:** A. api<br>B. api.prod<br>C. api.prod.svc.cluster.local<br>D. api.dev.svc.cluster.local
**Answer:** C (3) – api.prod.svc.cluster.local
**Explanation:** Services are registered in CoreDNS as <service>.<namespace>.svc.cluster.local. The SHORT name (api) only resolves inside the caller's own namespace — a dev pod asking for 'api' gets dev's api (or NXDOMAIN). Cross-namespace calls need the namespace in the name: api.prod.svc.cluster.local.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/" target="_blank">Kubernetes Documentation - DNS for Services and Pods</a>
**Tags:** k8s::kcna topic::dns topic::namespaces src::session

---

<!-- note:1793757640855 model:Basic (and reversed card) -->
**Front:** In Service DNS names like <code>api.prod.svc.cluster.local</code>, what is the final domain component?
**Back:** <code>cluster.local</code> — it completes the Service FQDN <code>&lt;svc&gt;.&lt;ns&gt;.svc.cluster.local</code>. It's the cluster's default DNS domain (the 'base domain' CoreDNS serves); kubelet hands it to pods via <code>clusterDomain</code>/resolv.conf. Custom clusters can change it, but stock installs use cluster.local.
**Tags:** k8s::kcna topic::dns topic::namespaces src::session

---

<!-- note:1793757640856 model:Basic (and reversed card) -->
**Front:** How do you place a new object into namespace 'dev' instead of 'default' when creating it?
**Back:** Set its <code>metadata.namespace</code> field (e.g. <code>namespace: dev</code>) — or pass <code>-n dev</code> at creation with an imperative command. If you omit it, the object lands in your current context's namespace (usually <code>default</code>).
**Tags:** k8s::kcna topic::namespaces topic::yaml src::session

---

<!-- note:1793807595536 model:Many -->
**Domain:** Scheduling - pod selection
**Question:** Which pods does the kube-scheduler pick up and try to place?
**Options:** A. Pods whose spec.nodeName is still unset<br>B. Pods that failed health checks<br>C. Pods on overloaded nodes<br>D. All newly created pods regardless of fields
**Answer:** A (1) – pods whose spec.nodeName is still unset (unassigned)
**Explanation:** The scheduler watches for newly created pods that have no node assigned — i.e. spec.nodeName is empty. For each it runs filtering (which nodes are feasible) then scoring (which is best), then binds the pod. Pods already carrying a nodeName never reach the scheduler — that's why manually setting it bypasses scheduling entirely.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/" target="_blank">Kubernetes Documentation - kube-scheduler</a>
**Tags:** k8s::kcna topic::pods topic::scheduling src::session

---

<!-- note:1793807595537 model:Many -->
**Domain:** Scheduling - nodeName immutability
**Question:** Can you change spec.nodeName on an already-created pod to move it to another node?
**Options:** A. Yes — kubectl patch pod --type merge works<br>B. Yes — kubectl edit pod and update the field<br>C. No — nodeName is immutable after creation; recreate the pod to move it<br>D. Only if the pod is restarted first
**Answer:** C (3) – no — nodeName is immutable after creation; recreate the pod to move it
**Explanation:** spec.nodeName can only be written at two moments: by you at pod creation, or by the scheduler via a Binding while the pod is still unassigned. Once set it's read-only — kubectl patch/edit on it is rejected. To move a scheduled pod you must delete and recreate it (or let a Deployment do the rollout).
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/" target="_blank">Kubernetes Documentation - kube-scheduler</a>
**Tags:** k8s::kcna topic::pods topic::scheduling src::session

---

<!-- note:1793807595538 model:Many -->
**Domain:** Scheduling - manual binding
**Question:** Without kube-scheduler, how do you assign an already-created pod that has no nodeName to a node?
**Options:** A. kubectl annotate the pod with the target node<br>B. Create a Binding object (POST JSON to the pod's binding subresource naming the target node)<br>C. Patch spec.nodeName directly<br>D. Add the node's name to metadata.labels
**Answer:** B (2) – create a Binding object (POST JSON to the pod's binding subresource naming the target node)
**Explanation:** The Binding object is what the scheduler itself creates after picking a node. Doing it manually: POST to /api/v1/namespaces/<ns>/pods/<pod>/binding with a body like {"target": {"kind": "Node", "name": "node2"}} — the API server then writes nodeName and the kubelet takes over. It only works while nodeName is still empty.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/" target="_blank">Kubernetes Documentation - kube-scheduler</a>
**Tags:** k8s::kcna topic::api topic::scheduling src::session

---

<!-- note:1793807595548 model:Basic (and reversed card) -->
**Front:** What is the <code>spec.nodeName</code> field on a pod?
**Back:** It holds the name of the node the pod is bound to run on. It's empty when you submit the pod — the scheduler fills it (via a Binding) after choosing a node. If you set <code>spec.nodeName</code> yourself at creation time, the pod skips the scheduler entirely: manual scheduling. Immutable afterwards.
**Tags:** k8s::kcna topic::pods topic::scheduling src::session

---

<!-- note:1793807595549 model:Basic (and reversed card) -->
**Front:** Mechanically, what does the kube-scheduler DO once it picks a node for a pod?
**Back:** The scheduler creates a <code>Binding</code> object — a POST to the pod's <code>binding</code> subresource naming the chosen node. The API server records the decision by writing <code>spec.nodeName</code> on the pod; the kubelet on that node then sees the pod is assigned to it and starts the containers.
**Tags:** k8s::kcna topic::architecture topic::scheduling src::session

---

<!-- note:1793808319432 model:Many -->
**Domain:** Labels - multi-criteria
**Question:** What does <code>kubectl get pods -l 'app=web,env=prod'</code> return?
**Options:** A. Pods matching ANY of the criteria<br>B. Only pods matching ALL criteria — multiple -l requirements are ANDed<br>C. Pods matching the first criterion only<br>D. Pods in the 'prod' namespace labelled web
**Answer:** B (2) – only pods matching ALL criteria — multiple -l requirements are ANDed
**Explanation:** Comma-separated selector requirements must ALL be satisfied — it's an AND, not OR. Equality selectors match exact values (app=web, env!=dev); set-based selectors match membership (env in (prod,qa), tier notin (cache), !key = absence). Everything from kubectl -l to NetworkPolicy podSelector uses the same requirement logic.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/" target="_blank">Kubernetes Documentation - Labels and Selectors</a>
**Tags:** k8s::kcna topic::kubectl topic::labels src::session

---

<!-- note:1793808319433 model:Many -->
**Domain:** Labels - manifest placement
**Question:** Where in a pod/Deployment manifest do an object's OWN labels always go?
**Options:** A. spec.labels<br>B. spec.selector.labels<br>C. metadata.labels<br>D. status.labels
**Answer:** C (3) – metadata.labels — the object's own label set
**Explanation:** Labels always go under metadata.labels on the object itself: metadata: {labels: {app: web, tier: frontend}}. The consumers live elsewhere in OTHER objects' specs: Service spec.selector, ReplicaSet/Deployment spec.selector.matchLabels, NetworkPolicy podSelector. 'Label everything, select from outside' is the pattern.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/" target="_blank">Kubernetes Documentation - Labels and Selectors</a>
**Tags:** k8s::kcna topic::labels topic::yaml src::session

---

<!-- note:1793808323513 model:Cloze -->
**Text:** List only pods labelled <code>app=web</code>:<br><br><code>kubectl get pods {{c1::-l}} {{c2::app=web}}</code><br><br>(<code>-l</code> is short for <code>{{c3::--selector}}</code>)
**Back Extra:** The flag works on most list commands (get pods, get svc, get all, delete). Multiple requirements AND together: -l 'app=web,env=prod'. Set-based form: -l 'env in (prod,qa)'. Combine with --show-labels to see each object's full label set.
**Tags:** k8s::kcna topic::kubectl topic::labels src::session

---

<!-- note:1793808319514 model:Basic (and reversed card) -->
**Front:** Labels vs selectors — which side does what?
**Back:** Labels are key-value pairs ATTACHED to objects under <code>metadata.labels</code> — the grouping side (tag by app, tier, env, version…). Selectors are QUERIES that filter objects by their labels — the selection side (<code>kubectl -l</code>, Service <code>spec.selector</code>, ReplicaSet <code>matchLabels</code>, NetworkPolicy). Labels tag things; selectors find them.
**Tags:** k8s::kcna topic::api topic::labels src::session

---

<!-- note:1793808422503 model:Many -->
**Domain:** Annotations - purpose
**Question:** You want to record build version, release notes and owner contact on Deployments — purely for humans and tooling to READ, never to filter on. What should you attach?
**Options:** A. Labels — key-value pairs under metadata.labels<br>B. Annotations — informational metadata not meant for selecting objects<br>C. ConfigMaps — dedicated configuration storage<br>D. Environment variables on the container spec
**Answer:** B (2) – annotations — informational metadata not meant for selecting objects
**Explanation:** Annotations record non-identifying, informational metadata — build versions, release notes, owner/contact info, doc links, tool config. Labels would technically hold short strings too, but labels exist to be SELECTED on (Services, ReplicaSets, -l flags). Rule of thumb: if controllers need to filter on it → label; if humans/tools just need to read it → annotation.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/" target="_blank">Kubernetes Documentation - Annotations</a>
**Tags:** k8s::kcna topic::annotations topic::labels src::session

---

<!-- note:1793808422504 model:Many -->
**Domain:** Annotations - limitations
**Question:** Which statement about annotations is TRUE?
**Options:** A. They can be selected with kubectl get -l just like labels<br>B. They're required on every object<br>C. They cannot be used in selectors — no -l flag or matchExpressions can filter on annotations<br>D. They can only hold values under 63 characters like labels
**Answer:** C (3) – they cannot be used in selectors — no -l flag or matchExpressions can filter on annotations
**Explanation:** The annotation API has no selector mechanism: kubectl -l doesn't see them, spec.selector/matchExpressions ignore them, Services can't pick pods by them. They're write-and-read metadata only (get -o yaml / describe shows them). Also unlike labels they aren't size-constrained the same way — they can hold larger structured blobs (that's how last-applied fits a whole manifest).
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/" target="_blank">Kubernetes Documentation - Annotations</a>
**Tags:** k8s::kcna topic::annotations topic::api src::session

---

<!-- note:1793808422514 model:Basic (and reversed card) -->
**Front:** What are annotations in Kubernetes — and a few typical examples?
**Back:** Key-value string metadata for informational purposes — recording details that identify nothing and select nothing: build/release version, git commit, owner contact, docs links, or config for tools and controllers (e.g. <code>kubectl.kubernetes.io/last-applied-configuration</code>, Prometheus <code>scrape</code> hints). They live under <code>metadata.annotations</code>, beside <code>metadata.labels</code>.
**Tags:** k8s::kcna topic::annotations topic::api src::session

---

<!-- note:1793808422523 model:Cloze -->
**Text:** Record a build version on a pod imperatively:<br><br><code>kubectl {{c1::annotate}} pod web {{c2::build-version}}={{c3::v1.4.2}}</code>
**Back Extra:** Same shape as kubectl label: <resource> <name> <key>=<value>. Re-running with an existing key fails unless you add --overwrite. Remove with a trailing minus: kubectl annotate pod web build-version-. In YAML the same data sits under metadata.annotations.
**Tags:** k8s::kcna topic::annotations topic::kubectl src::session

---

<!-- note:1793809412430 model:Many -->
**Domain:** Taints - effects
**Question:** Which taint effect removes ALREADY-RUNNING pods from a node if they don't tolerate it?
**Options:** A. NoSchedule<br>B. PreferNoSchedule<br>C. NoExecute<br>D. Evict
**Answer:** C (3) – NoExecute
**Explanation:** NoSchedule: no new pods without a matching toleration (existing pods stay). PreferNoSchedule: soft version — scheduler tries to avoid but no guarantee. NoExecute: evicts running pods that don't tolerate it (immediately, or after tolerationSeconds if set) AND blocks new ones.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/" target="_blank">Kubernetes Documentation - Taints and Tolerations</a>
**Tags:** k8s::kcna topic::scheduling topic::taints src::session

---

<!-- note:1793809412431 model:Many -->
**Domain:** Taints - toleration semantics
**Question:** A pod tolerates node1's taint. Is it guaranteed to be scheduled on node1?
**Options:** A. Yes — a matching toleration binds the pod to that node<br>B. No — a toleration only PERMITS placement; nodeAffinity/nodeSelector attracts pods to nodes<br>C. Yes — but only for NoSchedule taints<br>D. No — tolerations and taints are unrelated
**Answer:** B (2) – no — a toleration only PERMITS placement; nodeAffinity/nodeSelector attracts pods to nodes
**Explanation:** Tolerations are a pass, not a magnet: the scheduler may still place the pod on any node — tainted or untainted. Taints REPEL (set on nodes); affinity/nodeSelector ATTRACT (set on pods). For 'must run on node X' you combine them: taint the node to keep others out + nodeAffinity on the pod to pin it there.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/" target="_blank">Kubernetes Documentation - Taints and Tolerations</a>
**Tags:** k8s::kcna topic::scheduling topic::taints src::session

---

<!-- note:1793809412432 model:Many -->
**Domain:** Taints - control plane
**Question:** Why don't regular workload pods land on the control-plane node by default?
**Options:** A. Pods can't reach the control-plane network<br>B. kubelet refuses to run user pods on it<br>C. The control-plane node carries a default taint (node-role.kubernetes.io/control-plane:NoSchedule) that user pods don't tolerate<br>D. Control-plane nodes only accept static pods
**Answer:** C (3) – the control-plane node carries a default taint (node-role.kubernetes.io/control-plane:NoSchedule) that user pods don't tolerate
**Explanation:** kubeadm clusters taint control-plane nodes by default (node-role.kubernetes.io/control-plane:NoSchedule) so workloads stay off them — protection, not magic. DaemonSets and system pods carry matching tolerations. You CAN remove the taint (kubectl taint nodes <cp> node-role.kubernetes.io/control-plane:NoSchedule-) e.g. on single-node labs like minikube — it's just not done on real clusters.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/" target="_blank">Kubernetes Documentation - Taints and Tolerations</a>
**Tags:** k8s::kcna topic::architecture topic::taints src::session

---

<!-- note:1793809412438 model:Basic (and reversed card) -->
**Front:** Taints vs tolerations — which object gets which, and what's the pair for?
**Back:** A scheduling restriction pair: <b>taints on NODES repel</b> pods (the node says 'stay away unless allowed'); <b>tolerations on PODS</b> let them bypass a matching taint. Effect: keeps pods off unsuitable nodes — dedicated hardware, control plane, special workloads. Tolerations permit but never attract — pods can still land anywhere.
**Tags:** k8s::kcna topic::scheduling topic::taints src::session

---

<!-- note:1793809412490 model:Cloze -->
**Text:** Taint node1 so only pods tolerating <code>dedicated=gpu</code> may schedule:<br><br><code>kubectl taint nodes node1 {{c1::dedicated=gpu}}:{{c2::NoSchedule}}</code>
**Back Extra:** Format: kubectl taint nodes <node> <key>=<value>:<effect>. Remove a taint by appending a minus: kubectl taint nodes node1 dedicated=gpu:NoSchedule-. Effects: NoSchedule / PreferNoSchedule / NoExecute.
**Tags:** k8s::kcna topic::kubectl topic::taints src::session

---

<!-- note:1793809412491 model:Cloze -->
**Text:** Pod spec tolerating a <code>dedicated=gpu:NoSchedule</code> taint — fields under <code>{{c1::spec.tolerations}}</code>:<br><br><code>tolerations:<br>- key: {{c2::"dedicated"}}<br>  operator: {{c3::"Equal"}}<br>  value: {{c4::"gpu"}}<br>  effect: {{c5::"NoSchedule"}}</code>
**Back Extra:** operator defaults to Equal (needs a matching value); Exists matches the key regardless of value (omit 'value'). Effect must equal the taint's effect. Add tolerationSeconds: 3600 under a NoExecute toleration to survive the taint for one hour before eviction.
**Tags:** k8s::kcna topic::taints topic::yaml src::session

---

<!-- note:1793810135656 model:Many -->
**Domain:** NodeSelector - limitations
**Question:** Can spec.nodeSelector express 'run on nodes labelled size=large OR size=medium'?
**Options:** A. Yes — separate values with commas<br>B. No — nodeSelector only does equality-AND on labels; OR/prefer logic needs nodeAffinity/nodeAntiAffinity<br>C. Yes — use a YAML list under nodeSelector<br>D. Yes — use two nodeSelector blocks
**Answer:** B (2) – no — nodeSelector only does equality-AND on labels; OR/prefer logic needs nodeAffinity/nodeAntiAffinity
**Explanation:** nodeSelector accepts only exact key=value pairs, ANDed together — you can't say 'large OR medium', 'not small', or 'prefer fast'. Node affinity adds expressive rules: the In operator (size In [large, medium]), NotIn, plus requiredDuringScheduling (hard) vs preferredDuringScheduling (soft) terms. Anti-affinity is the inverse — keep pods OFF matching nodes (or spread them).
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Documentation - Assign Pods to Nodes</a>
**Tags:** k8s::kcna topic::nodeselector topic::scheduling src::session

---

<!-- note:1793810135657 model:Many -->
**Domain:** NodeSelector - hard requirement
**Question:** A pod has spec.nodeSelector {size: large} but NO node carries that label. What happens?
**Options:** A. It schedules anyway on a random node<br>B. It's deleted after a timeout<br>C. It stays Pending/unschedulable until a node with matching labels appears<br>D. kubelet runs it on the control-plane node
**Answer:** C (3) – it stays Pending/unschedulable until a node with matching labels appears
**Explanation:** nodeSelector is a HARD constraint — the scheduler won't place the pod anywhere else and won't retry-error; the pod just sits unscheduled. Events show '0/N nodes are available'. Fixes: label a node, relax the selector, or switch to nodeAffinity preferredDuringScheduling for a soft preference.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Documentation - Assign Pods to Nodes</a>
**Tags:** k8s::kcna topic::nodeselector topic::scheduling src::session

---

<!-- note:1793810135666 model:Basic (and reversed card) -->
**Front:** What is <code>spec.nodeSelector</code> on a pod?
**Back:** A pod-spec field holding key-value pairs that constrain WHERE the pod may run: the scheduler only picks nodes whose labels satisfy ALL listed pairs. <code>spec.nodeSelector: {size: large}</code> = 'nodes labelled size=large only'. It's the simplest node-constraint mechanism — hard equality matching only, no OR/preferences.
**Tags:** k8s::kcna topic::nodeselector topic::scheduling src::session

---

<!-- note:1793810135683 model:Basic -->
**Front:** Recipe: pin a pod to SSD nodes using nodeSelector
**Back:** Two steps, in order: 1) LABEL the node — <code>kubectl label nodes node1 disktype=ssd</code>. 2) Add the selector in the pod spec — <code>spec.nodeSelector: {disktype: ssd}</code>. The nodeSelector never labels anything itself; it only matches labels nodes already carry. Labels on the node, selector on the pod.
**Tags:** k8s::kcna topic::nodeselector topic::scheduling src::session

---

<!-- note:1793810943058 model:Many -->
**Domain:** NodeAffinity - types
**Question:** Which node affinity type schedules the pod ANYWAY when no node satisfies the rule?
**Options:** A. requiredDuringSchedulingIgnoredDuringExecution<br>B. preferredDuringSchedulingIgnoredDuringExecution<br>C. requiredDuringSchedulingRequiredDuringExecution<br>D. softDuringScheduling
**Answer:** B (2) – preferredDuringSchedulingIgnoredDuringExecution
**Explanation:** requiredDuringSchedulingIgnoredDuringExecution is the HARD type: no matching node = pod stays Pending (like nodeSelector but expressive). preferredDuringSchedulingIgnoredDuringExecution is SOFT: scheduler scores matching nodes higher using weight 1-100, but schedules anyway if none match. The 'IgnoredDuringExecution' suffix on BOTH means label changes after scheduling don't evict the pod.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Documentation - Assign Pods to Nodes</a>
**Tags:** k8s::kcna topic::affinity topic::scheduling src::session

---

<!-- note:1793810943059 model:Many -->
**Domain:** NodeAffinity - IgnoredDuringExecution
**Question:** A pod required a node label via nodeAffinity, gets scheduled, then the node's label is REMOVED. What does 'IgnoredDuringExecution' mean happens?
**Options:** A. The pod is evicted when the label changes<br>B. The pod reschedules to a compliant node<br>C. Nothing — node label changes after scheduling don't evict the pod<br>D. The pod enters a failed state
**Answer:** C (3) – nothing — node label changes after scheduling don't evict the pod
**Explanation:** Affinity rules are evaluated only at SCHEDULING time. Once bound, the pod is immune to node-label changes: if the node loses its 'size=large' label later, the pod keeps running. (Contrast: NoExecute taints DO evict.) The never-implemented RequiredDuringExecution variant would have evicted — hence the verbose naming.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Documentation - Assign Pods to Nodes</a>
**Tags:** k8s::kcna topic::affinity topic::scheduling src::session

---

<!-- note:1793810943060 model:Many -->
**Domain:** NodeAffinity - match logic
**Question:** How are nodeSelectorTerms and the matchExpressions inside them logically combined?
**Options:** A. Both ORed<br>B. Terms ORed, expressions ANDed — pod needs any ONE term fully satisfied<br>C. Both ANDed<br>D. Terms ANDed, expressions ORed
**Answer:** B (2) – terms ORed, expressions ANDed — pod needs any ONE term fully satisfied
**Explanation:** Two levels of logic inside requiredDuringScheduling...: the list nodeSelectorTerms[] is ORed (match ANY term); the matchExpressions[] inside ONE term are ANDed (ALL expressions in that term must match). Bonus: if both nodeSelector AND nodeAffinity are set on a pod, BOTH must be satisfied.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Documentation - Assign Pods to Nodes</a>
**Tags:** k8s::kcna topic::affinity topic::scheduling src::session

---

<!-- note:1793810943061 model:Many -->
**Domain:** NodeAffinity - operators
**Question:** With nodeAffinity matchExpressions, how do you require a pod to avoid nodes labelled zone=east?
**Options:** A. operator: NotIn (or DoesNotExist for 'label absent' — anti-affinity behavior)<br>B. operator: Exclude<br>C. operator: NotEqual<br>D. operator: Neq
**Answer:** A (1) – operator: NotIn (or DoesNotExist for 'label absent' — anti-affinity behavior)
**Explanation:** matchExpressions operators: In (value in list — this gives the OR nodeSelector lacks: size In [large, medium]), NotIn (value NOT in list), Exists (key present, any value), DoesNotExist (key absent), Gt/Lt (integer compare). NotIn and DoesNotExist are how you express node ANTI-affinity — keep pods off matching nodes.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Documentation - Assign Pods to Nodes</a>
**Tags:** k8s::kcna topic::affinity topic::scheduling src::session

---

<!-- note:1793810943068 model:Basic (and reversed card) -->
**Front:** What is node affinity — and what does it add over nodeSelector?
**Back:** The expressive version of nodeSelector — pod-specified rules under <code>spec.affinity.nodeAffinity</code> that attract pods to (or repel from) nodes based on node labels. Adds what nodeSelector lacks: OR logic (values lists, multiple terms), NOT operators (NotIn/DoesNotExist = anti-affinity), and SOFT preferences (preferredDuringScheduling... with weights). Exists purely to control pod placement.
**Tags:** k8s::kcna topic::affinity topic::scheduling src::session

---

<!-- note:1793810943076 model:Cloze -->
**Text:** Require the pod on large-or-medium nodes via affinity:<br><br><code>spec:<br>  affinity:<br>    {{c1::nodeAffinity}}:<br>      {{c2::requiredDuringSchedulingIgnoredDuringExecution}}:<br>        {{c3::nodeSelectorTerms}}:<br>        - {{c4::matchExpressions}}:<br>          - {key: size, operator: {{c5::In}}, values: [large, medium]}</code>
**Back Extra:** Hierarchy: spec.affinity.nodeAffinity.<type>.nodeSelectorTerms[].matchExpressions[] — each expression is {key, operator, values[]}. values is a LIST (In = OR across values). Preferred type uses - weight: N / preference: matchExpressions instead of plain terms.
**Tags:** k8s::kcna topic::affinity topic::yaml src::session

---
