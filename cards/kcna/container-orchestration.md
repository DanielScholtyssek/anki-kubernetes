# KCNA - Kubernetes and Cloud Native Associate — Container Orchestration

> Deck: `KCNA - Kubernetes and Cloud Native Associate` · Group: `Container Orchestration` · Notes: 26 · Models: Basic++, Basic+++

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
