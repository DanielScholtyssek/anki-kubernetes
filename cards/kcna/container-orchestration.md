# KCNA - Kubernetes and Cloud Native Associate — Container Orchestration

> Deck: `KCNA - Kubernetes and Cloud Native Associate` · Group: `Container Orchestration` · Notes: 54 · Models: Basic++, Basic+++, Basic, Basic (and reversed card), Cloze, Many

<!-- note:1755878736894 model:Basic++ -->
**Front:** What is the fundamental reason Kubernetes uses Pods as the
smallest deployable unit, rather than individual containers directly?
<br><br>A. To simplify network configuration for containers<br>B. To enable co-location and shared resources for containers
<br>C. To enforce stricter security boundaries than containers
<br>D. To provide a unique IP address per container
<br>E. To reduce container image size
**Back:** Correct Answer: <b>B
<br><br>Explanation</b>: Pods allow tightly coupled containers to share resources
like network namespace (IP, port space) and storage volumes, facilitating
communication and data sharing for helper or sidecar patterns.

---

<!-- note:1755880094937 model:Basic++ -->
**Front:** What core benefit does containerization (e.g., using Docker or
containerd) provide for application deployment?
<br><br>A. Automatic scaling of applications
<br>B. Abstraction of the underlying operating system and kernel
<br>C. Consistent runtime environment across different machines
<br>D. Built-in service discovery and load balancing
<br>E. Secure by default inter-container communication
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: Containers bundle an application with its dependencies,
ensuring it runs consistently regardless of the host environment, solving
”it works on my machine” problems.

---

<!-- note:1755880279344 model:Basic++ -->
**Front:** Which part of the <b>Container Runtime Interface (CRI)</b> specification is containerd primarily responsible for implementing?
<br><br>A. Image distribution and storage
<br>B. Low-level container execution and lifecycle management
<br>C. Network namespace creation and IP address assignment
<br>D. Defining container image format standards
<br>E. Implementing pod-level resource sharing
**Back:** Correct Answer: <b>B</b>
<br><br><b>Explanation</b>: containerd is a core container runtime that manages the
complete container lifecycle on a single host – image transfer, storage,
container execution, supervision, and network attachments.

---

<!-- note:1755880587012 model:Basic++ -->
**Front:** A stateful application requires storage that persists even if its
Pod is rescheduled to another Node. Which Kubernetes objects
are essential for this?
<br><br>A. ConfigMap and Secret
<br>B. PersistentVolume (PV) and PersistentVolumeClaim (PVC)
<br>C. EphemeralVolume and HostPath volume
<br>D. Service and EndpointSlice
<br>E. Job and CronJob
**Back:** Correct Answer: <b>B</b>
<br><br><b>Explanation</b>: A PersistentVolume (PV) represents a piece of storage,
and a PersistentVolumeClaim (PVC) is a request for that storage by a
user/Pod. This decoupling allows storage to outlive Pods.

---

<!-- note:1755880918790 model:Basic++ -->
**Front:** Why are Open Standards, like those defined by the Open Container Initiative (OCI), critical for the cloud native ecosystem?
<br><br>A. They guarantee better application performance
<br>B. They enforce specific vendor implementations
<br>C. They promote interoperability and prevent vendor lock-in
<br>D. They reduce the need for security patching
<br>E. They simplify the user interface of cloud platforms
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: Open standards (e.g., OCI for container formats/runtimes,
CNI for networking, CRI for runtimes) ensure that different tools and
platforms can work together seamlessly, giving users choice and preventing
vendor lock-in.

---

<!-- note:1755882062504 model:Basic++ -->
**Front:** Which OCI specification defines the format of a container image?<br>&nbsp;<div>A. Runtime Specification
<br>B. Image Specification<br>C. Distribution Specification
<br>D. Network Specification
<br>E. Storage Specification</div>
**Back:** Correct Answer: <b>B</b>
<br><br><b>Explanation</b>: The OCI Image Specification defines how to create and
package a container image, ensuring interoperability across different container tools and runtimes that adhere to the standard.

---

<!-- note:1755882154629 model:Basic++ -->
**Front:** In the context of container security, what does ”least privilege”
primarily refer to?<br>&nbsp;&nbsp;<br>A. Running containers with minimal resource requests
<br>B. Granting containers only the permissions they absolutely need&nbsp;<div>C. Using the smallest possible base container images
<br>D. Limiting network access to containers
<br>E. Encrypting all data within the container</div>
**Back:** Correct Answer: <b>B</b>
<br><br><b>Explanation</b>: The principle of least privilege means that containers (and
their processes) should run with only the capabilities and permissions
essential for their function, reducing the potential impact of a compromise.

---

<!-- note:1756921293694 model:Basic++ -->
**Front:** <div>What is the main benefit of using container orchestration systems like Kubernetes?</div><div><br></div><div>A. Simplifying code writing</div><div>B. Automating deployment scaling</div><div>C. Reducing storage costs</div><div>D. Improving network latency</div>
**Back:** Correct Answer: <b>B</b><br><br><div><div><b>Explanation</b>: Orchestrators automate the deployment, scaling, management, and networking of containerized applications.</div><div>Domain: Container Orchestration</div></div>

---

<!-- note:1756921357835 model:Basic++ -->
**Front:** <div>Which of these is a standard specified by the OCI (Open Container Initiative)?</div><div><br></div><div>A. Docker</div><div>B. Kubernetes</div><div>C. Image Specification</div><div>D. Istio</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: The OCI defines standards for container image formats (Image Specification) and runtime (Runtime Specification).</div>

---

<!-- note:1756921422314 model:Basic++ -->
**Front:** <div>Which container runtime is most commonly associated with Kubernetes and implements the CRI (Container Runtime Interface)?</div><div><br></div><div>A. Docker (dockershim)</div><div>B. containerd</div><div>C. rkt</div><div>D. LXC</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div><div><b>Explanation</b>: containerd is a widely used container runtime focused on simplicity, robustness, and portability, fully implementing the CRI.</div>

---

<!-- note:1756921545261 model:Basic++ -->
**Front:** <div>What is the role of a CNI (Container Network Interface) plugin in Kubernetes?</div><div><br></div><div>A. Managing storage volumes</div><div>B. Providing container networking</div><div>C. Scheduling Pods</div><div>D. Securing the API server</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div><div>Explanation: CNI plugins are responsible for configuring network interfaces for containers and managing IP address allocation within the cluster.</div>

---

<!-- note:1756921718413 model:Basic++ -->
**Front:** <div>What Kubernetes object represents a piece of storage in the cluster, provisioned by an administrator or dynamically?</div><div><br></div><div>A. PersistentVolumeClaim (PVC)</div><div>B. StorageClass</div><div>C. PersistentVolume (PV)</div><div>D. Volume</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: A PersistentVolume (PV) is a piece of storage provisioned for use in the cluster, independent of any individual Pod.</div>

---

<!-- note:1756922839040 model:Basic++ -->
**Front:** <div>What does a PersistentVolumeClaim (PVC) represent in Kubernetes?</div><div><br></div><div>A. A request for storage by a user</div><div>B. A type of storage backend</div><div>C. A node’s local storage</div><div>D. A backup of a volume</div>
**Back:** Correct Answer: <b>A</b><br><br><div><div><b>Explanation</b>: A PVC is a request made by a user (or Pod) for storage resources defined by a PV.</div></div>

---

<!-- note:1756922916665 model:Basic++ -->
**Front:** What is the function of a StorageClass in Kubernetes?<br><br><div><div>A. To define types of storage</div><div>B. To claim a specific PV</div><div>C. To attach storage to a Pod</div><div>D. To backup volume data</div></div>
**Back:** <div>Correct Answer: <b>A</b></div><div><br></div><div><b>Explanation</b>: StorageClasses allow administrators to define different ”classes” of storage (e.g., ’fast-ssd’, ’cheap-hdd’) for dynamic provisioning.</div>

---

<!-- note:1756926441386 model:Basic++ -->
**Front:** <div>When defining a Pod, what does the <i>spec.containers[].image</i> field specify?<br><br></div><div>A. The base operating system for the container</div><div>B. The specific container image (and tag) to run</div><div>C. The command to execute inside the container</div><div>D. The resource limits for the container</div><div>E. The network port the container will listen on</div>
**Back:** <div>Correct Answer: <b>B</b><br><br></div><div><b>Explanation</b>: This field tells the container runtime which image (e.g., nginx:1.21 or myrepo/myapp:v2.5) to pull from a registry and use to create the container process.</div>

---

<!-- note:1756927136838 model:Basic++ -->
**Front:** <div>Which OCI (Open Container Initiative) specification defines how container runtimes should execute containers?</div><div><br></div><div>A. Image Specification</div><div>B. Distribution Specification</div><div>C. Runtime Specification (CRI is Kubernetes’ interface to this)</div><div>D. Network Specification (CNI is related)</div><div>E. Storage Specification</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: The OCI Runtime Specification outlines how to run a container filesystem bundle. Kubernetes uses the Container Runtime Interface (CRI) as an abstraction layer over runtimes like containerd or CRI-O that implement this standard.</div>

---

<!-- note:1756928234534 model:Basic++ -->
**Front:** <div>What is the primary goal of the Open Container Initiative (OCI)?</div><div><br></div><div>A. To create a commercial container platform</div><div>B. To define open standards around container formats and runtime</div><div>C. To manage the Kubernetes source code repository</div><div>D. To develop container networking plugins (CNI)</div><div>E. To provide free container image hosting</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div><div><b>Explanation</b>: OCI aims to establish common, open, minimal standards for container image formats and container runtime execution to ensure interoperability and prevent fragmentation in the container ecosystem.</div>

---

<!-- note:1756928733069 model:Basic++ -->
**Front:** <div>Which statement best describes the relationship between Kubernetes and Docker (as of 2025)?</div><div><br></div><div>A. Kubernetes requires Docker to be installed on all nodes.</div><div>B. Docker is the only container runtime supported by Kubernetes.</div><div>C. Kubernetes primarily interacts with container runtimes via CRI (e.g., containerd, CRI-O), abstracting Docker.</div><div>D. Docker manages the Kubernetes control plane components.</div><div>E. Kubernetes is a component within the Docker Enterprise platform.</div>
**Back:** <div>Correct Answer: C</div><div><br></div><div>Explanation: Kubernetes deprecated the direct Docker integration (dockershim). It now interacts with OCI-compliant runtimes like containerd (which Docker itself uses) or CRI-O via the Container Runtime Interface (CRI). While Docker might be installed, K8s doesn’t use it directly in the same way.</div>

---

<!-- note:1756928790353 model:Basic++ -->
**Front:** <div>If multiple Pods need to share persistent data, which volume type allows simultaneous mounting by multiple Pods (potentially with read/write access)?</div><div><br></div><div>A. hostPath</div><div>B. emptyDir</div><div>C. A PersistentVolume with an accessMode like ReadWriteMany (RWX)</div><div>D. secret volume</div><div>E. configMap volume</div>
**Back:** <div>Correct Answer: <b>C</b><br><br></div><div><b>Explanation</b>: PersistentVolumes (PVs) represent external storage. Their accessModes define how they can be mounted. ReadWriteOnce (RWO) allows mounting by a single node, while ReadWriteMany (RWX) allows simultaneous read/write mounting by multiple nodes (requires a capable storage backend like NFS).</div>

---

<!-- note:1767559867265 model:Basic+++ -->
**Front:** Which statement about containers is true? <br><br><div>A. Require a specific OS<br> B. Run consistently across environments<br> C. Are the same as virtual machines<br> D. Only support monolithic apps</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div> <div><b>Explanation</b>: Containers provide portability, allowing applications to run consistently across different environments.</div>

---

<!-- note:1767559967952 model:Basic+++ -->
**Front:** What is the primary function of Kubernetes? <br><br><div>A. Network security<br> B. Managing container lifecycle<br> C. Code compilation<br> D. Cloud storage</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div> <div><b>Explanation</b>: Kubernetes manages deployment, scaling, and operation of containerized applications.</div>

---

<!-- note:1767560021237 model:Basic+++ -->
**Front:** What is the primary role of a container runtime? <br><br><div>A. Build images<br> B. Run containers<br> C. Schedule pods<br> D. Monitor nodes</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div> <div><b>Explanation</b>: The container runtime is responsible for executing containers on cluster nodes.</div>

---

<!-- note:1767560057447 model:Basic+++ -->
**Front:** Which container runtime option is supported by Kubernetes? <br><br><div>A. Docker Engine<br> B. CRI-compliant runtimes<br> C. Hyper-V<br> D. VMware vSphere</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div> <div><b>Explanation</b>: Kubernetes natively supports runtimes that implement the Container Runtime Interface (CRI), such as containerd and CRI-O.</div>

---

<!-- note:1767560112595 model:Basic+++ -->
**Front:** Which networking model does Kubernetes use? <br><br><div>A. NAT<br> B. VPN<br> C. Flat networking<br> D. Peer-to-peer</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div> <div><b>Explanation</b>: Kubernetes uses a flat network model where all Pods can communicate without NAT.</div>

---

<!-- note:1767561126861 model:Basic+++ -->
**Front:** Which resource manages persistent data? <br><br><div>A. Node<br> B. PersistentVolume<br> C. ServiceAccount<br> D. ConfigMap</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div> <div><b>Explanation</b>: PersistentVolumes represent storage resources in the cluster.</div>

---

<!-- note:1767561150983 model:Basic+++ -->
**Front:** What is true about a PersistentVolumeClaim? <br><br><div>A. Deletes the PV automatically<br> B. Is a storage request<br> C. Requires admin attachment<br> D. Describes access methods</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div> <div><b>Explanation</b>: A PVC is a user request for storage resources.</div>

---

<!-- note:1793752347323 model:Basic -->
**Front:** Which kubectl command exposes a Deployment named <code>web</code> as a NodePort Service on port 80?
**Back:** <code>kubectl expose deployment web --type=NodePort --port=80</code> — <code>--port</code> is the port the Service listens on; <code>--type=NodePort</code> makes it open a 30000-32767 port on every node. Alternative: <code>kubectl create service nodeport web --tcp=80:8080</code> (servicePort:targetPort). To convert an existing service: <code>kubectl patch svc web -p '{"spec":{"type":"NodePort"}}'</code>.
**Tags:** k8s::kcna topic::kubectl topic::services src::session

---

<!-- note:1793752347334 model:Cloze -->
**Text:** A Service named <code>backend</code> in namespace <code>prod</code> gets the in-cluster DNS name<br><br><code>{{c1::backend}}.{{c2::prod}}.{{c3::svc}}.{{c4::cluster.local}}</code><br><br>resolving to the Service's {{c5::clusterIP}}.
**Back Extra:** CoreDNS publishes &lt;service&gt;.&lt;namespace&gt;.svc.cluster.local for every Service; it resolves to the clusterIP. Inside the same namespace the short name (backend) is enough; from another namespace you need backend.&lt;ns&gt;.
**Tags:** k8s::kcna topic::dns topic::services src::session

---

<!-- note:1793752354576 model:Many -->
**Domain:** Service Types - ClusterIP
**Question:** Which Service type is the default when <code>spec.type</code> is not specified, and is reachable only inside the cluster?
**Options:** A. NodePort<br>B. ClusterIP<br>C. LoadBalancer<br>D. ExternalName
**Answer:** B (2) – ClusterIP
**Explanation:** ClusterIP is the default Service type: a stable virtual IP reachable only inside the cluster — used for internal pod-to-pod / microservice traffic. NodePort and LoadBalancer build on it to expose traffic externally; ExternalName is pure DNS.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/service/" target="_blank">Kubernetes Documentation - Service</a>
**Tags:** k8s::kcna topic::networking topic::services src::session

---

<!-- note:1793752354577 model:Many -->
**Domain:** Service Types - NodePort
**Question:** Which Service type opens the same port (e.g. 30080) on EVERY node's IP so external clients can reach the service?
**Options:** A. ClusterIP<br>B. ExternalName<br>C. NodePort<br>D. Ingress
**Answer:** C (3) – NodePort
**Explanation:** A NodePort Service allocates the same static port (default range 30000-32767) on EVERY node — each node proxies &lt;node-IP&gt;:&lt;nodePort&gt; into the Service, which forwards to a ready backend pod. It's the simplest built-in way to accept outside traffic.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/service/" target="_blank">Kubernetes Documentation - Service</a>
**Tags:** k8s::kcna topic::networking topic::services src::session

---

<!-- note:1793752354578 model:Many -->
**Domain:** Service Types - LoadBalancer
**Question:** Which Service type asks the cloud provider (or an LB implementation like MetalLB/Cilium) to provision an external load balancer with a public IP?
**Options:** A. NodePort<br>B. LoadBalancer<br>C. ClusterIP<br>D. ExternalName
**Answer:** B (2) – LoadBalancer
**Explanation:** type: LoadBalancer delegates to an external implementation — the cloud-controller-manager on AWS/GCP/Azure, or tools like MetalLB/Cilium LB IPAM on bare metal. The provisioned IP lands in .status.loadBalancer.ingress. With no implementation, EXTERNAL-IP stays &lt;pending&gt;.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/service/" target="_blank">Kubernetes Documentation - Service</a>
**Tags:** k8s::kcna topic::networking topic::services src::session

---

<!-- note:1793752354579 model:Many -->
**Domain:** Service Port Fields
**Question:** In a Service manifest, which field specifies the port ON THE BACKEND PODS that traffic is forwarded to?
**Options:** A. port<br>B. nodePort<br>C. targetPort<br>D. hostPort
**Answer:** C (3) – targetPort
**Explanation:** port = what the Service itself listens on (clients connect to clusterIP:port); targetPort = the port on the backend pods traffic is forwarded to (defaults to the port value); nodePort = the per-node external port for NodePort Services.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/service/" target="_blank">Kubernetes Documentation - Service</a>
**Tags:** k8s::kcna topic::networking topic::services topic::yaml src::session

---

<!-- note:1793752354580 model:Many -->
**Domain:** ReplicaSet Selectors
**Question:** How does a ReplicaSet identify which pods it manages and counts toward spec.replicas?
**Options:** A. Pods register themselves with the ReplicaSet via the API<br>B. Its spec.selector.matchLabels must match the labels in spec.template.metadata.labels<br>C. The kubelet reports pod names to the ReplicaSet<br>D. Namespaces define which pods belong to a ReplicaSet
**Answer:** B (2) – Its spec.selector.matchLabels must match the labels in spec.template.metadata.labels
**Explanation:** A ReplicaSet counts and manages every pod whose labels satisfy spec.selector.matchLabels — the selector must equal the pod template's labels or the API rejects the object. It can even adopt pre-existing matching pods that have no controller ownerReference.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/" target="_blank">Kubernetes Documentation - ReplicaSet</a>
**Tags:** k8s::kcna topic::labels topic::replicasets src::session

---

<!-- note:1793752906095 model:Many -->
**Domain:** Docker vs containerd - dockershim
**Question:** Why did Kubernetes remove dockershim in v1.24?
**Options:** A. Docker Inc. changed its license, forcing removal<br>B. Docker Engine is not CRI-compatible; the kubelet-internal dockershim shim was vendor-specific complexity, so Kubernetes standardized on CRI runtimes (containerd, CRI-O)<br>C. Containers were deprecated in favor of VMs<br>D. containerd can only run images built by containerd
**Answer:** B (2) – Docker Engine is not CRI-compatible; the kubelet-internal dockershim shim was vendor-specific complexity, so Kubernetes standardized on CRI runtimes (containerd, CRI-O)
**Explanation:** Dockershim let the kubelet talk to Docker Engine, which predates and never implemented the CRI. It was removed in v1.24 to cut maintenance burden and align with open standards. Docker images still work — they follow OCI specs — and Docker Engine can still be used via the cri-dockerd shim.
**Sources:** <a href="https://kubernetes.io/blog/2022/05/03/dockershim-historical-context/" target="_blank">Kubernetes Blog - Dockershim: The Historical Context</a>
**Tags:** k8s::kcna topic::cri-oci topic::docker src::session

---

<!-- note:1793752906096 model:Many -->
**Domain:** Docker vs containerd - cri-dockerd
**Question:** Can a cluster still use Docker Engine as its container runtime today?
**Options:** A. No — Docker cannot run containers in Kubernetes anymore<br>B. Yes — natively, because Docker implements CRI<br>C. Yes — via cri-dockerd, a CRI shim maintained by Docker/Mirantis; though most clusters use containerd or CRI-O directly<br>D. Only if containerd is also installed
**Answer:** C (3) – Yes — via cri-dockerd, a CRI shim maintained by Docker/Mirantis; though most clusters use containerd or CRI-O directly
**Explanation:** Dockershim removal ended the BUILT-IN Docker path, not Docker itself. cri-dockerd re-adds the CRI bridge outside the kubelet. In practice, managed clusters run containerd or CRI-O — and note Docker Engine itself uses containerd under the hood.
**Sources:** <a href="https://kubernetes.io/blog/2022/05/03/dockershim-historical-context/" target="_blank">Kubernetes Blog - Dockershim: The Historical Context</a>
**Tags:** k8s::kcna topic::cri-oci topic::docker src::session

---

<!-- note:1793752906097 model:Many -->
**Domain:** OCI Image Portability
**Question:** Why can an image built with Docker run on a different runtime like containerd?
**Options:** A. Kubernetes converts the image at pull time<br>B. Both follow OCI standards: the image conforms to the image-spec format and containerd follows the runtime-spec<br>C. Docker must be installed on the node<br>D. containerd embeds a Docker engine
**Answer:** B (2) – Both follow OCI standards: the image conforms to the image-spec format and containerd follows the runtime-spec
**Explanation:** OCI image-spec standardizes how an image is packaged (manifest, config, layers); runtime-spec standardizes how it's executed. Any OCI-compliant runtime can run any OCI-compliant image — that's why Docker-built images run on containerd, CRI-O, etc. No conversion needed.
**Sources:** <a href="https://opencontainers.org/" target="_blank">Open Container Initiative</a>
**Tags:** k8s::kcna topic::cri-oci topic::docker src::session

---

<!-- note:1793752906098 model:Many -->
**Domain:** Containers vs VMs
**Question:** How do containers fundamentally differ from virtual machines?
**Options:** A. Each container boots its own guest OS kernel<br>B. Containers share the host OS kernel (isolated via namespaces/cgroups) with no guest OS — much lighter and faster than VMs<br>C. Containers require a hypervisor while VMs don't<br>D. VMs are lighter because they don't need isolation
**Answer:** B (2) – Containers share the host OS kernel (isolated via namespaces/cgroups) with no guest OS — much lighter and faster than VMs
**Explanation:** A VM runs a full guest OS on a hypervisor — heavyweight, slow to boot. A container is just an isolated process set on the host: it shares the host kernel and gets its own view of processes/network/filesystems. That's why containers start in milliseconds and pack denser.
**Sources:** <a href="https://docs.docker.com/get-started/docker-overview/" target="_blank">Docker Official Documentation - Docker Overview</a>
**Tags:** k8s::kcna topic::container-orchestration topic::docker src::session

---

<!-- note:1793752906099 model:Many -->
**Domain:** Image vs Container
**Question:** What is the difference between a container image and a container?
**Options:** A. The image is the read-only template/package; the container is a running instance of it<br>B. The container is the template; the image is the running process<br>C. They are two names for the same thing<br>D. Images run on VMs; containers run on bare metal
**Answer:** A (1) – The image is the read-only template/package; the container is a running instance of it
**Explanation:** An image packages the app + dependencies as a sharable, versioned artifact (built once, stored in a registry). A container is what runs when you instantiate the image — the live isolated environment with its own processes, network and filesystem. One image → many containers.
**Sources:** <a href="https://docs.docker.com/get-started/docker-overview/" target="_blank">Docker Official Documentation - Docker Overview</a>
**Tags:** k8s::kcna topic::cri-oci topic::docker src::session

---

<!-- note:1793752918686 model:Basic (and reversed card) -->
**Front:** What is the Container Runtime Interface (CRI)?
**Back:** The standard gRPC plugin interface between the kubelet and the container runtime on each node. Any runtime implementing CRI (containerd, CRI-O) can run containers under Kubernetes — that's what makes runtimes swappable. The CRI-compliant runtimes in turn follow OCI standards (image-spec, runtime-spec).
**Tags:** k8s::kcna topic::container-orchestration topic::cri-oci src::session

---

<!-- note:1793753618569 model:Many -->
**Domain:** Container Runtime - CRI benefit
**Question:** What are the benefits of using container runtimes that support the CRI? (Select all that apply)
**Options:** A. It enables automatic scaling of container instances<br>B. It enables container runtimes to be developed independently of Kubernetes<br>C. It provides better compatibility and standardization across container runtimes<br>D. It allows for direct communication between containers
**Answer:** B, C – runtimes implement CRI independently of Kubernetes; the standard interface gives compatibility and standardization across runtimes
**Explanation:** CRI defines one standard interface between the kubelet and any container runtime. That standardization is the core benefit: compliant runtimes (containerd, CRI-O, cri-dockerd) plug in interchangeably, giving better compatibility and standardization across runtimes (C); and runtime developers only need to satisfy the interface, so runtimes can be built and evolved independently of Kubernetes itself (B). A and D are unrelated to CRI — scaling is the orchestrator's job and CNI, not CRI, handles container networking.
**Sources:** <a href="https://kubernetes.io/docs/concepts/architecture/cri/" target="_blank">Kubernetes Documentation - Container Runtime Interface (CRI)</a>
**Tags:** k8s::kcna topic::container-orchestration topic::cri-oci src::session

---

<!-- note:1793754672879 model:Many -->
**Domain:** ReplicaSet Self-healing
**Question:** A pod managed by a ReplicaSet is deleted (or its node fails). What happens?
**Options:** A. Nothing — the pod is gone permanently<br>B. The ReplicaSet controller notices actual < desired and creates a replacement pod to restore the count<br>C. The kubelet restarts the deleted pod's containers<br>D. The Deployment re-creates the ReplicaSet
**Answer:** B (2) – The ReplicaSet controller notices actual < desired and creates a replacement pod to restore the count
**Explanation:** A ReplicaSet's reconcile loop continuously compares spec.replicas to the number of matching pods alive. Delete a pod (or lose a node) and the count drops — the controller immediately creates a new pod from spec.template to restore it. That's the self-healing/HA behavior ReplicaSets provide.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/" target="_blank">Kubernetes Documentation - ReplicaSet</a>
**Tags:** k8s::kcna topic::pods topic::replicasets src::session

---

<!-- note:1793754672880 model:Many -->
**Domain:** Deployment Rolling Update Internals
**Question:** You change a Deployment's pod template (e.g. new image). What happens internally during the rolling update?
**Options:** A. The existing ReplicaSet edits its pods in place<br>B. A new ReplicaSet is created for the new pod template and scaled up while the old one scales down<br>C. All pods are deleted, then recreated<br>D. The Service is re-pointed first, then pods update
**Answer:** B (2) – A new ReplicaSet is created for the new pod template and scaled up while the old one scales down
**Explanation:** Every change to .spec.template creates a new ReplicaSet — during a RollingUpdate the new RS scales up gradually as the old scales down (maxSurge/maxUnavailable control the pace). Old RSs stay at 0 replicas so <code>kubectl rollout undo</code> can scale one back up.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/deployment/" target="_blank">Kubernetes Documentation - Deployment</a>
**Tags:** k8s::kcna topic::deployments topic::rollouts src::session

---

<!-- note:1793754672881 model:Many -->
**Domain:** Rollout & Rollback
**Question:** A Deployment's latest rollout is broken. Which command rolls it back to the previous pod-template version?
**Options:** A. <code>kubectl rollout restart deployment/web</code><br>B. <code>kubectl rollout undo deployment/web</code><br>C. <code>kubectl delete deployment/web</code><br>D. <code>kubectl scale deployment/web --replicas=0</code>
**Answer:** B (2) – <code>kubectl rollout undo deployment/web</code>
**Explanation:** <code>kubectl rollout undo</code> scales an OLD ReplicaSet back up — the pod template returns to the previous revision (<code>kubectl rollout history</code> lists them; <code>--to-revision=N</code> picks a specific one). Only the pod template rolls back; scaling/config changes aren't revisions.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/deployment/" target="_blank">Kubernetes Documentation - Deployment</a>
**Tags:** k8s::kcna topic::deployments topic::kubectl src::session

---

<!-- note:1793754672882 model:Many -->
**Domain:** kubectl create deployment
**Question:** Which command creates a Deployment named web running 3 replicas of nginx?
**Options:** A. <code>kubectl run web --image=nginx --replicas=3</code><br>B. kubectl new deployment web <code>--image=nginx</code><br>C. <code>kubectl create deployment web --image=nginx --replicas=3</code><br>D. <code>kubectl apply deployment web --image=nginx --replicas=3</code>
**Answer:** C (3) – <code>kubectl create deployment web --image=nginx --replicas=3</code>
**Explanation:** <code>kubectl create deployment</code> makes the Deployment object; <code>--image</code> sets the pod template's container image, <code>--replicas</code> sets the desired count (default 1). Imperative equivalent of a YAML Deployment manifest. (<code>kubectl run</code> creates a bare Pod, not a Deployment.)
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_deployment/" target="_blank">Kubernetes Documentation - kubectl create deployment</a>
**Tags:** k8s::kcna topic::deployments topic::kubectl src::session

---

<!-- note:1793822816861 model:Many -->
**Domain:** DaemonSet - scheduling
**Question:** How does a DaemonSet actually get its pods onto each node?
**Options:** A. It sets spec.nodeName directly — no scheduler involved<br>B. The DaemonSet controller creates a pod per node with a nodeAffinity pinning it to that hostname; the default scheduler then binds it<br>C. kubelet on each node pulls the template itself<br>D. The ReplicationController schedules copies to nodes
**Answer:** B (2) – the DaemonSet controller creates a pod per node with a nodeAffinity pinning it to that hostname; the default scheduler then binds it
**Explanation:** DaemonSet pods do NOT bypass the scheduler: the controller creates one Pod per eligible node and injects nodeAffinity (matchFields metadata.name In [node]) — the DEFAULT scheduler then binds each pod to its node via spec.nodeName. You can point DS pods at a custom scheduler with spec.template.spec.schedulerName.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/" target="_blank">Kubernetes Documentation - DaemonSet</a>
**Tags:** k8s::kcna topic::daemonsets topic::scheduling src::session

---

<!-- note:1793822816862 model:Many -->
**Domain:** DaemonSet - lifecycle
**Question:** A cluster running a DaemonSet gets a NEW node. What happens?
**Options:** A. Nothing until the next reconcile<br>B. The DaemonSet must be reapplied<br>C. A pod lands on the new node automatically; pods on removed nodes are garbage-collected<br>D. Only if the DS has replicas: N set
**Answer:** C (3) – a pod lands on the new node automatically; pods on removed nodes are garbage-collected
**Explanation:** The DaemonSet controller continuously reconciles: any node joining the cluster that matches the selector gets a pod; nodes leaving take their DS pods with them (garbage collection). That's the whole point vs a Deployment — replica count follows node count, not a fixed number.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/" target="_blank">Kubernetes Documentation - DaemonSet</a>
**Tags:** k8s::kcna topic::daemonsets topic::scheduling src::session

---

<!-- note:1793822816863 model:Many -->
**Domain:** DaemonSet - tolerations
**Question:** Why do DaemonSet pods keep running on nodes that become NotReady or pressure-tainted?
**Options:** A. They get special scheduler priority only<br>B. Automatic tolerations — the controller adds not-ready/unreachable/pressure tolerations so DS pods survive node problems<br>C. Nothing — DS pods are immune by default<br>D. The nodeName field bypasses taints
**Answer:** B (2) – automatic tolerations — the controller adds not-ready/unreachable/pressure tolerations so DS pods survive node problems
**Explanation:** The DaemonSet controller pre-adds tolerations: node.kubernetes.io/not-ready (NoExecute), unreachable (NoExecute), disk/memory/pid-pressure (NoSchedule) — so node agents keep running through failures (when they're needed MOST). To also land on control-plane nodes, the template must tolerate node-role.kubernetes.io/control-plane explicitly.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/" target="_blank">Kubernetes Documentation - DaemonSet</a>
**Tags:** k8s::kcna topic::daemonsets topic::taints src::session

---

<!-- note:1793822816871 model:Basic (and reversed card) -->
**Front:** What is a DaemonSet — and which workloads belong in one?
**Back:** A workload controller that runs ONE copy of a pod on every node (or a subset via nodeSelector/affinity in the template). Replica count follows node count — nodes joining get the pod automatically. Used for node-local agents that must exist everywhere: monitoring exporters, log collectors (fluentd), kube-proxy, CNI plugins like Calico. apiVersion: apps/v1.
**Tags:** k8s::kcna topic::daemonsets topic::workloads src::session

---

<!-- note:1793822816917 model:Cloze -->
**Text:** DaemonSet manifest skeleton (fluentd on every node):<br><br><code>apiVersion: {{c1::apps/v1}}<br>kind: {{c2::DaemonSet}}<br>metadata: {name: fluentd}<br>spec:<br>  {{c3::selector}}:<br>    {{c4::matchLabels}}: {name: fluentd}<br>  {{c5::template}}:<br>    metadata: {labels: {name: fluentd}}<br>    spec: {containers: [...], restartPolicy: {{c6::Always}}}</code>
**Back Extra:** Same skeleton as a Deployment MINUS the replicas field — count is implied (one per node). selector.matchLabels must equal template.metadata.labels and is immutable after creation. Pod template's restartPolicy must be Always (default). Add spec.template.spec.nodeSelector/affinity to cover only a subset of nodes.
**Tags:** k8s::kcna topic::daemonsets topic::yaml src::session

---

<!-- note:1793823868597 model:Many -->
**Domain:** Static Pods - mirror pods
**Question:** <code>kubectl get pods</code> shows 'static-web-my-node1' — you kubectl delete it and it instantly reappears. What is it and how do you actually remove it?
**Options:** A. The pod is stuck terminating<br>B. RBAC is blocking the delete<br>C. It's a mirror of a static pod — the kubelet manages it from a manifest file on the node; delete the file, not the object<br>D. The pod has a finalizer
**Answer:** C (3) – it's a mirror of a static pod — the kubelet manages it from a manifest file on the node; delete the file, not the object
**Explanation:** The kubelet creates a read-only MIRROR of each static pod in the API server (named &lt;pod&gt;-&lt;nodename&gt;) so kubectl visibility works. Deleting the mirror does nothing — kubelet's source of truth is the manifest file in staticPodPath (e.g. /etc/kubernetes/manifests). To change/kill the pod: edit or remove the file ON THE NODE.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/" target="_blank">Kubernetes Documentation - Create static Pods</a>
**Tags:** k8s::kcna topic::pods topic::staticpods src::session

---

<!-- note:1793823868598 model:Many -->
**Domain:** Static Pods - limitations
**Question:** Which object kinds can a kubelet create from the static pod manifest directory?
**Options:** A. Any workload object<br>B. Only Pods — kubelet understands no other kind; no Deployments, ReplicaSets or Services<br>C. Pods and Services only<br>D. Pods and ConfigMaps
**Answer:** B (2) – only Pods — kubelet understands no other kind; no Deployments, ReplicaSets or Services
**Explanation:** Static manifests must be kind: Pod, apiVersion: v1 — nothing else exists without the API server. There's no controller to honor replicas, no scheduler (the pod lands on this node, period), no etcd. The kubelet alone watches the directory, creates the pod, and restarts it on failure — a one-node control loop.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/" target="_blank">Kubernetes Documentation - Create static Pods</a>
**Tags:** k8s::kcna topic::kubelet topic::staticpods src::session

---

<!-- note:1793823868599 model:Many -->
**Domain:** Static Pods - control plane
**Question:** In a kubeadm cluster, how do kube-apiserver, etcd and friends actually run on the control-plane node?
**Options:** A. As a Deployment in kube-system<br>B. As systemd services only<br>C. As static pods — kubelet runs them from manifests in /etc/kubernetes/manifests, no API server dependency<br>D. As DaemonSet pods
**Answer:** C (3) – as static pods — kubelet runs them from manifests in /etc/kubernetes/manifests, no API server dependency
**Explanation:** Kubeadm clusters bootstrap the control plane via static pods: manifests for kube-apiserver, etcd, kube-controller-manager and kube-scheduler sit in /etc/kubernetes/manifests and the kubelet runs them. Elegant because the control plane can't be hosted by the cluster it's bootstrapping — kubelet is the only piece that must exist first.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/" target="_blank">Kubernetes Documentation - Create static Pods</a>
**Tags:** k8s::kcna topic::architecture topic::staticpods src::session

---

<!-- note:1793823868607 model:Basic (and reversed card) -->
**Front:** What is a static pod?
**Back:** A pod created and managed directly by the kubelet — no API server, no scheduler, no controller. The kubelet periodically scans a configured directory (staticPodPath in the KubeletConfiguration, commonly /etc/kubernetes/manifests; deprecated flag: <code>--pod-manifest-path</code>) and runs every pod manifest found there, restarting them on failure. For visibility it mirrors each into the API server as a read-only object.
**Tags:** k8s::kcna topic::pods topic::staticpods src::session

---

<!-- note:1793823868617 model:Cloze -->
**Text:** Enable static pods via kubelet config file:<br><br><code>apiVersion: {{c1::kubelet.config.k8s.io/v1beta1}}<br>kind: {{c2::KubeletConfiguration}}<br>{{c3::staticPodPath}}: {{c4::/etc/kubernetes/manifests}}</code><br><br>then <code>systemctl {{c5::restart}} kubelet</code>
**Back Extra:** staticPodPath points kubelet at a directory it scans periodically — pod YAMLs appearing there get created, files removed get their pods deleted. Deprecated alternative: <code>--pod-manifest-path</code> flag. Web-hosted variant: staticPodURL / <code>--manifest-url</code>. Check the live kubelet's config on the node (e.g. /var/lib/kubelet/config.yaml) or ps aux | grep kubelet for the flag.
**Tags:** k8s::kcna topic::kubelet topic::staticpods src::session

---

<!-- note:1793933689164 model:Many -->
**Domain:** Pods - imagePullSecrets
**Question:** How can we specify the secret to our private registry inside our pod definition file?
**Options:** A. By setting the environment variable in the container definition<br>B. By using the annotations in the pod definition file<br>C. By specifying the secret under the imagePullSecrets section in the pod definition file<br>D. By using the command line and specifying the secret name and registry URL
**Answer:** C (3) – specifying the secret under the imagePullSecrets section in the pod definition file
**Explanation:** spec.imagePullSecrets is the pod-spec field that tells the kubelet which Secret to use when pulling images from a private registry: spec.imagePullSecrets: [{name: regcred}] where regcred is a Secret of type kubernetes.io/dockerconfigjson holding .dockerconfigjson auth (created via kubectl create secret docker-registry). It works at PULL time — before the container starts — so env vars (runtime only) and annotations (metadata, not pull logic) can't do it, and there's no kubectl flag that attaches pull secrets to a pod. You can also set imagePullSecrets on a ServiceAccount so every pod using that SA inherits them. Older kubernetes.io/dockercfg secrets work too.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/" target="_blank">Kubernetes Docs - Pull an Image from a Private Registry</a>
**Tags:** k8s::kcna topic::pods topic::secrets src::session

---

<!-- note:1794006447940 model:Many -->
**Domain:** Images - name expansion
**Question:** In a Pod spec, image: nginx is shorthand for what fully-qualified image?
**Options:** A. docker.io/library/nginx:latest<br>B. nginx.docker.io/library/latest<br>C. docker.io/nginx:library<br>D. index.docker.io/nginx:stable
**Answer:** A (1) – docker.io/library/nginx:latest — registry docker.io, namespace library (official images), tag latest
**Explanation:** An image name is REGISTRY/REPOSITORY:TAG with three independent defaults: no registry → docker.io (Docker Hub); official-library images live under the library/ namespace (docker.io/library/nginx); no tag → latest. So image: nginx is shorthand for docker.io/library/nginx:latest. Your own Docker Hub images resolve to docker.io/<your-username>/<image> — the middle path segment is the namespace/account, not part of the registry.
**Sources:** <a href="https://kubernetes.io/docs/concepts/containers/images/" target="_blank">Kubernetes Docs - Container Images</a>
**Tags:** k8s::kcna topic::images topic::containers src::session

---

<!-- note:1794006447941 model:Many -->
**Domain:** Images - name parts
**Question:** For image: quay.io/myorg/api:v2, which part is the registry?
**Options:** A. quay.io — the registry is the first path segment when it contains a dot or port<br>B. myorg — the first path segment is always the registry<br>C. api — the last segment is the registry<br>D. quay.io/myorg — registry and namespace are one field
**Answer:** A (1) – quay.io — the registry is the first path segment when it contains a dot or port
**Explanation:** Image name anatomy: [registry/][namespace/]repository[:tag]. The registry is identified by a '.' or ':' in the first path segment (quay.io, gcr.io, localhost:5000) or the literal 'localhost' — docker.io is assumed when absent. Everything between registry and repo is the namespace/account (yourorg, library). With your own Docker Hub account 'acme', image: acme/api expands to docker.io/acme/api:latest — registry docker.io, namespace acme, repo api.
**Sources:** <a href="https://kubernetes.io/docs/concepts/containers/images/" target="_blank">Kubernetes Docs - Container Images</a>
**Tags:** k8s::kcna topic::images topic::containers src::session

---

<!-- note:1794006447942 model:Many -->
**Domain:** Registry Auth - secret type
**Question:** What Secret type stores container-registry credentials for image pulls?
**Options:** A. kubernetes.io/dockerconfigjson — a Secret holding a .dockerconfigjson key with the registry auths<br>B. kubernetes.io/tls — a TLS cert/key pair for the registry<br>C. Opaque — any Secret type works for registry auth<br>D. kubernetes.io/service-account-token
**Answer:** A (1) – kubernetes.io/dockerconfigjson — a Secret holding a .dockerconfigjson key with the registry auths
**Explanation:** Registry credentials live in a Secret of type kubernetes.io/dockerconfigjson. Its data key .dockerconfigjson holds a base64'd docker config.json: {"auths":{"registry.example.com":{"username":..,"password":..,"auth":"base64(user:pass)"}}}. The legacy type kubernetes.io/dockercfg used the older ~/.dockercfg format — prefer dockerconfigjson. The kubelet reads this Secret at image-pull time and authenticates to the matching registry.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/" target="_blank">Kubernetes Docs - Pull an Image from a Private Registry</a>
**Tags:** k8s::kcna topic::images topic::secrets topic::security src::session

---

<!-- note:1794006447943 model:Many -->
**Domain:** Registry Auth - create command
**Question:** Which command creates a Secret with Docker registry credentials?
**Options:** A. kubectl create secret docker-registry regcred --docker-server=... --docker-username=... --docker-password=... --docker-email=...<br>B. kubectl create secret tls regcred --cert=... --key=...<br>C. kubectl create configmap regcred --from-literal=auth=...<br>D. kubectl create secret generic regcred --type=kubernetes.io/registry
**Answer:** A (1) – kubectl create secret docker-registry regcred --docker-server=... --docker-username=... --docker-password=... --docker-email=...
**Explanation:** kubectl create secret docker-registry builds the Secret imperatively: --docker-server is the registry FQDN (use https://index.docker.io/v1/ for Docker Hub, or your private registry's address), plus --docker-username/--docker-password/--docker-email. kubectl creates it as type kubernetes.io/dockerconfigjson in your current namespace. Doc warning: passing --docker-password on the CLI can leak it into shell history — prefer the --from-file=.dockerconfigjson variant when you already ran docker login.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/" target="_blank">Kubernetes Docs - Pull an Image from a Private Registry</a>
**Tags:** k8s::kcna topic::images topic::secrets topic::kubectl src::session

---

<!-- note:1794006447944 model:Many -->
**Domain:** Registry Auth - pull flow
**Question:** How does a Pod authenticate to a private image registry?
**Options:** A. Create the dockerconfigjson Secret in the pod's namespace, then reference it in spec.imagePullSecrets — the kubelet uses it at pull time<br>B. Add registry credentials to the pod's env vars<br>C. kubectl login inside the pod before the image pulls<br>D. Annotate the pod with the registry password
**Answer:** A (1) – Create the dockerconfigjson Secret in the pod's namespace, then reference it in spec.imagePullSecrets — the kubelet uses it at pull time
**Explanation:** End-to-end: (1) kubectl create secret docker-registry regcred ... in the SAME namespace as the pod — namespace mismatch is the #1 failure; (2) pod spec gets imagePullSecrets: [{name: regcred}]; (3) kubelet pulls the image using those creds before the container starts. If the Secret is missing the pod sits in ImagePullBackOff and kubectl describe pod shows FailedToRetrieveImagePullSecret. The Secret can also live on a ServiceAccount so all its pods inherit it.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/" target="_blank">Kubernetes Docs - Pull an Image from a Private Registry</a>
**Tags:** k8s::kcna topic::images topic::secrets topic::pods src::session

---

<!-- note:1794006447945 model:Many -->
**Domain:** Registry Auth - from dockerconfigjson
**Question:** You already ran docker login — how do you turn that credential into a cluster Secret?
**Options:** A. kubectl create secret generic regcred --from-file=.dockerconfigjson=~/.docker/config.json --type=kubernetes.io/dockerconfigjson<br>B. kubectl create secret docker-registry regcred --from-file=config.json<br>C. Copy ~/.docker/config.json into the pod as a mounted volume<br>D. kubectl create secret generic regcred --from-literal=.dockerconfigjson=$(cat config.json)
**Answer:** A (1) – kubectl create secret generic regcred --from-file=.dockerconfigjson=~/.docker/config.json --type=kubernetes.io/dockerconfigjson
**Explanation:** If you already ran docker login locally, reuse ~/.docker/config.json directly: kubectl create secret generic regcred --from-file=.dockerconfigjson=<path> --type=kubernetes.io/dockerconfigjson. The critical detail: the data key MUST be named .dockerconfigjson (that's what the kubelet looks for) and type must be kubernetes.io/dockerconfigjson. The file's auths entries carry base64 username:password per registry — same format docker uses.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/" target="_blank">Kubernetes Docs - Pull an Image from a Private Registry</a>
**Tags:** k8s::kcna topic::images topic::secrets topic::kubectl src::session

---

<!-- note:1794006447946 model:Many -->
**Domain:** Registry Auth - multiple registries
**Question:** A Pod has containers from quay.io AND a private ECR registry — how do you supply credentials for both?
**Options:** A. Multiple imagePullSecrets per pod, each holding credentials for multiple registries — the kubelet tries the credential matching the image's registry<br>B. Only one imagePullSecret is allowed per pod<br>C. The registry must be listed in the pod's image field<br>D. A single Secret can only hold one registry's credentials
**Answer:** A (1) – Multiple imagePullSecrets per pod, each holding credentials for multiple registries — the kubelet tries the credential matching the image's registry
**Explanation:** A pod with containers from different registries can list several imagePullSecrets, and each Secret's .dockerconfigjson can hold auths for multiple registries. At pull time the kubelet selects the credential matching that image's registry; if none matches it attempts the pull unauthenticated (or via runtime-specific config). imagePullSecrets is a pod-level list — order doesn't matter, matching is by registry hostname.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/" target="_blank">Kubernetes Docs - Pull an Image from a Private Registry</a>
**Tags:** k8s::kcna topic::images topic::secrets topic::pods src::session

---

<!-- note:1794006447949 model:Cloze -->
**Text:** Pod manifest pulling from a private registry via Secret 'regcred':<br><br><code>apiVersion: v1<br>kind: Pod<br>metadata:<br>  name: private-reg<br>spec:<br>  containers:<br>  - name: app<br>    image: your.private.registry.example.com/janedoe/app:v1<br>  {{c1::imagePullSecrets}}:<br>  - name: {{c2::regcred}}</code>
**Back Extra:** imagePullSecrets is a LIST under spec — each entry references a Secret of type kubernetes.io/dockerconfigjson that must exist in the pod's namespace. The kubelet uses these credentials when pulling <private.registry>/app before the container starts. Same field exists on a ServiceAccount to cover all its pods.
**Tags:** k8s::kcna topic::images topic::yaml topic::secrets src::session

---
