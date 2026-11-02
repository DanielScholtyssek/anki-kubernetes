# KCSA - Kubernetes and Cloud Native Security Associate — Cloud Native Security

> Deck: `KCSA - Kubernetes and Cloud Native Security Associate` · Group: `Cloud Native Security` · Notes: 36 · Models: Many

<!-- note:1772101854879 model:Many -->
**Domain:** Cloud Native Security
**Question:** What is the primary purpose of a Cloud Workload Protection Platform (CWPP)?
**Options:** A. Monitor network traffic<br>B. Secure workloads across various environments<br>C. Manage cloud costs<br>D. Provide identity and access management<br>E. Automate infrastructure provisioning
**Answer:** B (2) – Secure workloads across various environments
**Explanation:** CWPPs are designed to protect workloads in any environment.
**Sources:** 

---

<!-- note:1772101854882 model:Many -->
**Domain:** Cloud Native Security
**Question:** What is the primary purpose of signing container images in a cloud-native environment?
**Options:** A. To reduce the image size for deployment<br>B. To verify the image's integrity and authenticity<br>C. To include metadata for deployment automation<br>D. To enforce runtime security policies<br>E. To speed up image pulling during deployment
**Answer:** B (2) – To verify the image's integrity and authenticity
**Explanation:** The primary purpose of image signing is to ensure that a container image originates from a trusted source and has not been tampered with. This process involves cryptographically signing the image, allowing users to verify its integrity and authenticity before use. Incorrect options such as reducing image size or speeding up deployment do not relate to the security function of signing. Similarly, metadata inclusion and runtime policy enforcement are separate mechanisms unrelated to image signing.
**Sources:** <a href="https://docs.docker.com/engine/security/trust/" target="_blank">Docker Content Trust Documentation</a><br><a href="https://github.com/cncf/tag-security/blob/main/security-whitepaper/cloud-native-security-whitepaper.md" target="_blank">CNCF Cloud Native Security Whitepaper</a>

---

<!-- note:1772101854886 model:Many -->
**Domain:** Cloud Native Security
**Question:** How do multistage builds in Docker reduce image size?
**Options:** A. By running multiple containers within a single image<br>B. By creating images compatible with multiple architectures<br>C. By separating build-time dependencies from runtime components in different stages<br>D. By enabling parallel builds across multiple stages<br>E. By deploying to multiple environments simultaneously
**Answer:** C (3) – By separating build-time dependencies from runtime components in different stages
**Explanation:** Multistage builds in Docker allow developers to separate build-time dependencies (e.g., compilers, libraries) from runtime components by using multiple `FROM` instructions in a single Dockerfile. This ensures that only the necessary artifacts (e.g., binaries) are included in the final image, significantly reducing its size and improving security. While multistage builds can simplify workflows, they do not inherently enable parallel builds or support multi-environment deployments.
**Sources:** <a href="https://docs.docker.com/get-started/docker-concepts/building-images/multi-stage-builds/" target="_blank">Docker Documentation: Multi-Stage Builds</a><br><a href="https://earthly.dev/blog/docker-multistage/" target="_blank">Earthly Blog: Understanding Docker Multistage Builds</a>

---

<!-- note:1772101854890 model:Many -->
**Domain:** Cloud Native Security
**Question:** What are the key characteristics of gVisor and Firecracker? (Select all that apply)
**Options:** A. gVisor is a user-space kernel providing sandboxing<br>B. Firecracker uses lightweight microVMs with KVM<br>C. Both provide full hardware virtualization<br>D. Firecracker is a container runtime interface<br>E. gVisor offers better performance than traditional VMs
**Answer:** A (1) – gVisor is a user-space kernel providing sandboxing
**Explanation:** gVisor provides sandboxing by running in user space and intercepting system calls, which enhances security without the need for full hardware virtualization. Firecracker uses microVMs, leveraging KVM for efficient isolation. gVisor can offer better performance compared to traditional VMs due to its lightweight nature.
**Sources:** <a href="https://gvisor.dev/docs/" target="_blank">gVisor Documentation</a><br><a href="https://firecracker-microvm.github.io/" target="_blank">Firecracker Documentation</a>

---

<!-- note:1772101854891 model:Many -->
**Domain:** Cloud Native Security
**Question:** What is the primary difference between MicroVM and User-Space Kernel approaches in cloud native security?
**Options:** A. MicroVMs are larger in size<br>B. User-space kernels provide hardware virtualization<br>C. MicroVMs run directly on hardware without a host OS<br>D. User-space kernels intercept system calls in user space<br>E. There is no difference; they are the same
**Answer:** D (4) – User-space kernels intercept system calls in user space
**Explanation:** The primary difference lies in how they operate. User-space kernels, like gVisor, run in user space and intercept system calls, providing a lightweight sandboxing mechanism. MicroVMs, on the other hand, are full-fledged virtual machines that run directly on hardware but require a host OS for management.
**Sources:** <a href="https://gvisor.dev/docs/" target="_blank">gVisor Documentation</a><br><a href="https://www.redhat.com/en/topics/virtualization/what-is-microvm" target="_blank">MicroVM Overview</a>

---

<!-- note:1772101854894 model:Many -->
**Domain:** Cloud Native Security
**Question:** What components are necessary to verify the integrity and authenticity of a container image?
**Options:** A. A checksum and the image manifest<br>B. A digital signature, public key, and verification tool<br>C. The Dockerfile used to build the image<br>D. Access to the container registry logs<br>E. The image's pull secret
**Answer:** B (2) – A digital signature, public key, and verification tool
**Explanation:** To verify the integrity and authenticity of a container image, you need a digital signature, a public key to verify the signature, and a verification tool. This ensures that the image has not been tampered with and comes from a trusted source.
**Sources:** <a href="https://docs.docker.com/engine/security/" target="_blank">Docker Security Documentation</a><br><a href="https://www.suse.com/c/suse-best-practices/container-image-security/" target="_blank">Container Image Security Best Practices</a>

---

<!-- note:1772101854900 model:Many -->
**Domain:** Cloud Native Security
**Question:** What are the four key areas of focus for cloud-native security, often referred to as the '4 Cs'?
**Options:** A. Code, Container, Cluster, Cloud<br>B. Compute, Connectivity, Compliance, Cost<br>C. Cloud, Core, Control, Compliance<br>D. Code, Continuous Integration, Cloud, Compliance<br>E. Containerization, Coordination, Configuration, Control
**Answer:** A (1) – Code, Container, Cluster, Cloud
**Explanation:** The '4 Cs' of cloud-native security are Code, Container, Cluster, and Cloud. These represent the layers where security should be applied to ensure comprehensive protection across the entire cloud-native stack.
**Sources:** <a href="https://cloudnativecomputing.dev/" target="_blank">Cloud Native Security Overview</a><br><a href="https://www.cisecurity.org/insights/articles/cloud-security-best-practices/" target="_blank">Cloud Security Best Practices</a>

---

<!-- note:1772101854903 model:Many -->
**Domain:** Cloud Native Security
**Question:** How does the underlying cloud infrastructure impact the security of a Kubernetes cluster?
**Options:** A. No impact, as Kubernetes abstracts infrastructure entirely<br>B. Yes, infrastructure vulnerabilities can compromise cluster security<br>C. Only if using on-premises hardware<br>D. It depends on the Kubernetes version<br>E. Only when running stateful applications
**Answer:** B (2) – Yes, infrastructure vulnerabilities can compromise cluster security
**Explanation:** The security of the underlying cloud infrastructure directly impacts the security of a Kubernetes cluster. Vulnerabilities in the infrastructure can compromise the cluster, making it essential to ensure the infrastructure is secure.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/" target="_blank">Kubernetes Security Documentation</a><br><a href="https://www.cisecurity.org/insights/articles/cloud-security-best-practices/" target="_blank">Cloud Security Best Practices</a>

---

<!-- note:1772101854909 model:Many -->
**Domain:** Cloud Native Security
**Question:** In which scenarios is soft multi-tenancy preferred over hard multi-tenancy in cloud-native environments?
**Options:** A. When strict tenant isolation is mandatory<br>B. For workloads from untrusted tenants requiring strong isolation<br>C. To maximize resource utilization efficiency in trusted tenant environments<br>D. When compliance with strict regulatory requirements is necessary<br>E. When deploying workloads across multiple Kubernetes clusters
**Answer:** C (3) – To maximize resource utilization efficiency in trusted tenant environments
**Explanation:** Soft multi-tenancy is preferred when tenants are trusted and strict isolation is not required, allowing for more efficient sharing of resources. Hard multi-tenancy, by contrast, enforces strict isolation suitable for untrusted tenants or compliance-driven environments. Therefore, soft multi-tenancy optimizes resource usage in trusted settings but is not suitable where strong isolation or regulatory compliance is mandatory.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/multi-tenancy/" target="_blank">Kubernetes Official Documentation - Multi-tenancy</a><br><a href="https://www.cncf.io/blog/2020/05/27/multi-tenancy-in-kubernetes/" target="_blank">CNCF - Multi-tenancy in Kubernetes</a>

---

<!-- note:1772101854910 model:Many -->
**Domain:** Cloud Native Security
**Question:** Which methods can be used to isolate resources effectively in a multi-tenant Kubernetes environment? (Select all that apply)
**Options:** A. Deploying separate Kubernetes clusters for each tenant<br>B. Using Kubernetes namespaces combined with Role-Based Access Control (RBAC)<br>C. Applying Kubernetes Network Policies to restrict traffic<br>D. Sharing service accounts among tenants to simplify access<br>E. Disabling resource quotas to allow unlimited resource usage
**Answer:** A (1) – Deploying separate Kubernetes clusters for each tenant
**Explanation:** Effective resource isolation in multi-tenant Kubernetes environments can be achieved by deploying separate clusters, using namespaces with RBAC to control access, and applying network policies to restrict communication. Sharing service accounts among tenants reduces isolation and is insecure. Disabling resource quotas removes limits on resource consumption, which can lead to resource contention and is not recommended.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/" target="_blank">Kubernetes Official Documentation - Namespaces</a><br><a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Official Documentation - Network Policies</a>

---

<!-- note:1772101854911 model:Many -->
**Domain:** Cloud Native Security
**Question:** What is an effective and consistent approach to enforce policies across multiple Kubernetes clusters?
**Options:** A. Manually applying policies individually on each cluster<br>B. Using policy-as-code tools such as Open Policy Agent (OPA) or Kyverno<br>C. Relying solely on default Kubernetes security settings<br>D. Implementing different policies tailored for each environment<br>E. Enforcing policies only at the application layer
**Answer:** B (2) – Using policy-as-code tools such as Open Policy Agent (OPA) or Kyverno
**Explanation:** Using policy-as-code tools like OPA or Kyverno enables automated, consistent, and scalable enforcement of policies across multiple Kubernetes clusters. Manual application is error-prone and inconsistent. Default Kubernetes settings are minimal and insufficient for comprehensive policy enforcement. Tailoring different policies per environment can lead to inconsistencies. Enforcing policies only at the application layer misses cluster-level security controls.
**Sources:** <a href="https://www.openpolicyagent.org/docs/latest/" target="_blank">Open Policy Agent Documentation</a><br><a href="https://kyverno.io/docs/" target="_blank">Kyverno Policy Management</a>

---

<!-- note:1772101854916 model:Many -->
**Domain:** Cloud Native Security
**Question:** What is a common cause for failing to pull the latest version of a container image from the 'k8s.gcr.io' registry?
**Options:** A. The image registry has been deprecated or is unavailable<br>B. Specifying an incorrect image name or tag in the pull command<br>C. Network policies blocking outbound traffic from the node<br>D. The Kubernetes node lacks sufficient CPU or memory resources<br>E. The kube-proxy component is not running on the node
**Answer:** B (2) – Specifying an incorrect image name or tag in the pull command
**Explanation:** A frequent reason for image pull failures is specifying an incorrect image name or tag, which leads to the registry not finding the requested image. While registry deprecation or network policies can also cause issues, the most common and easily overlooked cause is a typo or mismatch in the image reference. Insufficient node resources or kube-proxy issues typically do not directly cause image pull failures.
**Sources:** <a href="https://kubernetes.io/docs/concepts/containers/images/" target="_blank">Kubernetes Official Documentation - Container Images</a><br><a href="https://cloud.google.com/container-registry/docs/troubleshooting" target="_blank">Google Container Registry Troubleshooting</a>

---

<!-- note:1772101854923 model:Many -->
**Domain:** Cloud Native Security
**Question:** What is the primary function of the Open Policy Agent (OPA) in Kubernetes environments?
**Options:** A. A tool for monitoring and analyzing cluster performance metrics<br>B. A general-purpose policy engine that enables defining and enforcing custom policies<br>C. A built-in Kubernetes admission controller for validating resources<br>D. A network policy enforcement tool for controlling pod communication<br>E. A secret management system for storing sensitive data
**Answer:** B (2) – A general-purpose policy engine that enables defining and enforcing custom policies
**Explanation:** Open Policy Agent (OPA) is a flexible, general-purpose policy engine that allows administrators to define and enforce custom policies across Kubernetes and other systems. It integrates with Kubernetes admission controllers but is not itself built-in. OPA is not a monitoring tool, network policy enforcer, or secret management system, although it can be used to enforce policies related to these areas.
**Sources:** <a href="https://www.openpolicyagent.org/docs/latest/" target="_blank">Open Policy Agent Official Documentation</a><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#opa-gatekeeper" target="_blank">Kubernetes Admission Controllers - OPA Gatekeeper</a>

---

<!-- note:1772101854931 model:Many -->
**Domain:** Cloud Native Security
**Question:** What security risk is associated with mounting the Docker socket ('/var/run/docker.sock') into a container?
**Options:** A. No risk; it's a common practice<br>B. The container can control the Docker daemon and other containers<br>C. It improves container performance<br>D. It provides secure access to host resources<br>E. It isolates the container from the host
**Answer:** B (2) – The container can control the Docker daemon and other containers
**Explanation:** Mounting the Docker socket into a container allows the container to control the host's Docker daemon, potentially leading to unauthorized access or manipulation of other containers and host resources. This practice should be avoided unless absolutely necessary and properly secured.
**Sources:** <a href="https://docs.docker.com/engine/reference/commandline/dockerd/" target="_blank">Docker Documentation</a><br><a href="https://kubernetes.io/docs/concepts/security/security-best-practices/" target="_blank">Kubernetes Security Best Practices</a>

---

<!-- note:1772101854934 model:Many -->
**Domain:** Cloud Native Security
**Question:** How can you ensure that only signed images are run in your Kubernetes cluster?
**Options:** A. Use imagePullSecrets<br>B. Configure admission controllers to verify image signatures<br>C. Manually inspect images before deployment<br>D. Disable image caching on nodes<br>E. Use a private container registry
**Answer:** B (2) – Configure admission controllers to verify image signatures
**Explanation:** To ensure only signed images are run in a Kubernetes cluster, you can configure admission controllers like Gatekeeper or Kyverno to enforce policies that verify image signatures. This ensures that only trusted images are deployed.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/" target="_blank">Kubernetes Admission Controllers</a><br><a href="https://open-policy-agent.github.io/gatekeeper/website/docs/" target="_blank">Gatekeeper Documentation</a>

---

<!-- note:1772101854941 model:Many -->
**Domain:** Cloud Native Security
**Question:** What is the primary benefit of using multistage Docker builds?
**Options:** A. Faster build times by reusing intermediate stages<br>B. Smaller and more secure final images by excluding build-time dependencies<br>C. Compatibility with older Docker versions for broader deployment<br>D. Simplified deployment scripts for easier automation<br>E. Enhanced network performance during container communication
**Answer:** B (2) – Smaller and more secure final images by excluding build-time dependencies
**Explanation:** The primary advantage of multistage Docker builds is the ability to create smaller and more secure final images. By separating the build and runtime stages, unnecessary build-time dependencies (e.g., compilers, libraries) are excluded from the final image. This reduces the image size, minimizes the attack surface, and enhances security. While multistage builds can indirectly improve build times by optimizing layers, their main focus is on producing leaner and safer images. They do not specifically address network performance or deployment script simplification.
**Sources:** <a href="https://docs.docker.com/get-started/docker-concepts/building-images/multi-stage-builds/" target="_blank">Docker Documentation: Multi-Stage Builds</a><br><a href="https://www.cherryservers.com/blog/docker-multistage-build" target="_blank">Cherry Servers: Docker Multi-Stage Build</a>

---

<!-- note:1772101854957 model:Many -->
**Domain:** Cloud Native Security
**Question:** What is the outcome of setting 'imagePullPolicy: Never' in a Kubernetes pod specification?
**Options:** A. The image will always be pulled from the registry<br>B. The pod will fail to start if the image is not present locally<br>C. The image will be pulled only if not present<br>D. The pod will ignore image updates in the registry<br>E. The kubelet will crash
**Answer:** B (2) – The pod will fail to start if the image is not present locally
**Explanation:** Setting 'imagePullPolicy: Never' in a Kubernetes pod specification means that the image will not be pulled from the registry. The pod will only start if the image is already present locally. This policy is useful for environments where network connectivity is limited or unreliable.
**Sources:** <a href="https://kubernetes.io/docs/concepts/containers/images/#imagepullpolicy" target="_blank">Kubernetes Image Pull Policy</a><br><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.26/#podspec-v1-core" target="_blank">Kubernetes Pod Spec Documentation</a>

---

<!-- note:1772101854998 model:Many -->
**Domain:** Cloud Native Security
**Question:** Which Kubernetes or related object defines how to build and deploy an application from source code?
**Options:** A. Deployment<br>B. StatefulSet<br>C. BuildConfig (OpenShift)<br>D. DaemonSet<br>E. Job
**Answer:** C (3) – BuildConfig (OpenShift)
**Explanation:** While Kubernetes itself does not have a native object for building applications from source code, OpenShift uses the 'BuildConfig' object for this purpose. It defines how to build and deploy applications from source code into containers.
**Sources:** <a href="https://docs.openshift.com/container-platform/4.11/builds/what-are-builds.html" target="_blank">OpenShift BuildConfig Documentation</a><br><a href="https://kubernetes.io/docs/concepts/workloads/" target="_blank">Kubernetes Workloads Documentation</a>

---

<!-- note:1772101855010 model:Many -->
**Domain:** Cloud Native Security
**Question:** What are the key principles of the 4 Cs of cloud-native security?
**Options:** A. Encrypting data at rest only<br>B. Applying security at Code, Container, Cluster, and Cloud levels<br>C. Relying solely on cloud provider security<br>D. Using containers to bypass security checks<br>E. Limiting security to the network layer
**Answer:** B (2) – Applying security at Code, Container, Cluster, and Cloud levels
**Explanation:** The 4 Cs of cloud-native security emphasize the importance of applying security measures at multiple levels: Code (secure coding practices), Container (secure containerization), Cluster (secure Kubernetes clusters), and Cloud (secure cloud infrastructure). This layered approach ensures comprehensive security.
**Sources:** <a href="https://cloudnative.io/cloud-native-security/" target="_blank">Cloud Native Security Principles</a><br><a href="https://kubernetes.io/docs/concepts/security/security-best-practices/" target="_blank">Kubernetes Security Best Practices</a>

---

<!-- note:1772101855014 model:Many -->
**Domain:** Cloud Native Security
**Question:** Which Kubernetes Pod specification field allows you to inject environment variables from a ConfigMap into containers?
**Options:** A. VolumeMount<br>B. envFrom<br>C. Secret<br>D. Annotation<br>E. Label
**Answer:** B (2) – envFrom
**Explanation:** The 'envFrom' field in a Pod specification enables injecting all key-value pairs from a ConfigMap as environment variables into the container. 'VolumeMount' is used for mounting volumes, 'Secret' is a separate object for sensitive data, 'Annotation' and 'Label' are metadata and do not inject environment variables.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/" target="_blank">Kubernetes Official Documentation - Configure a Pod to Use a ConfigMap</a><br><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#envfromsource-v1-core" target="_blank">Kubernetes API Reference - PodSpec envFrom</a>

---

<!-- note:1772101855020 model:Many -->
**Domain:** Cloud Native Security
**Question:** To prevent Pods from accessing the cloud provider's metadata API, which IP address should be blocked in a Kubernetes NetworkPolicy?
**Options:** A. 0.0.0.0/0<br>B. 127.0.0.1/32<br>C. 169.254.169.254/32<br>D. 255.255.255.255/32<br>E. 192.168.0.1/32
**Answer:** C (3) – 169.254.169.254/32
**Explanation:** The IP address 169.254.169.254 is the standard link-local address used by cloud providers (such as AWS, GCP, Azure) for their metadata service. Blocking this IP in a NetworkPolicy prevents Pods from querying sensitive metadata, mitigating risks like metadata service exploitation. Other IPs listed do not correspond to the cloud metadata service.
**Sources:** <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html" target="_blank">AWS Documentation - Instance Metadata and User Data</a><br><a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes NetworkPolicy Documentation</a>

---

<!-- note:1772101855027 model:Many -->
**Domain:** Cloud Native Security
**Question:** Which tool is specifically designed to perform static security analysis of Kubernetes manifests to identify potential security issues?
**Options:** A. kube-bench<br>B. kube-hunter<br>C. kube-score<br>D. kubectl describe<br>E. kubesec
**Answer:** E (5) – kubesec
**Explanation:** Kubesec is a static analysis tool that scans Kubernetes manifests for security risks and best practices violations before deployment. 'kube-bench' checks cluster nodes against CIS benchmarks, 'kube-hunter' performs active scanning for vulnerabilities, 'kube-score' provides general manifest validation but is less focused on security, and 'kubectl describe' is a CLI command for inspecting resources.
**Sources:** <a href="https://github.com/controlplaneio/kubesec" target="_blank">Kubesec Official GitHub Repository</a><br><a href="https://landscape.cncf.io/category=security&format=card-mode&grouping=category" target="_blank">CNCF Security Tools Landscape</a>

---

<!-- note:1772101855060 model:Many -->
**Domain:** Cloud Native Security
**Question:** In a Kubernetes Pod manifest, which annotation is used to specify an AppArmor profile for a container named 'nginx'?
**Options:** A. apparmor.security.beta.kubernetes.io/nginx: 'localhost/nginx-profile'<br>B. security.alpha.kubernetes.io/apparmor/nginx: 'localhost/nginx-profile'<br>C. container.apparmor.security.beta.kubernetes.io/nginx: 'localhost/nginx-profile'<br>D. nginx.apparmor.kubernetes.io/profile: 'localhost/nginx-profile'<br>E. securityContext.apparmorProfile: 'localhost/nginx-profile'
**Answer:** C (3) – container.apparmor.security.beta.kubernetes.io/nginx: 'localhost/nginx-profile'
**Explanation:** The correct annotation format to specify an AppArmor profile for a container named 'nginx' is 'container.apparmor.security.beta.kubernetes.io/nginx: "localhost/nginx-profile"'. This annotation applies the profile to the specific container. Other options are either incorrect prefixes, deprecated, or invalid Kubernetes annotation keys.
**Sources:** <a href="https://kubernetes.io/docs/tutorials/clusters/apparmor/" target="_blank">Kubernetes Official Documentation - AppArmor</a><br><a href="https://gitlab.com/apparmor/apparmor/-/wikis/Kubernetes" target="_blank">AppArmor Kubernetes Integration</a>

---

<!-- note:1772101855067 model:Many -->
**Domain:** Cloud Native Security
**Question:** What are the key best practices for hardening container images to enhance security?
**Options:** A. Use a minimal base image to reduce the attack surface.<br>B. Run containers as root to simplify privilege management.<br>C. Remove unnecessary packages and dependencies to minimize potential vulnerabilities.<br>D. Expose all ports for maximum connectivity and flexibility.<br>E. Regularly scan images for known vulnerabilities and apply necessary patches.
**Answer:** A (1) – Use a minimal base image to reduce the attack surface.
**Explanation:** To effectively harden container images, it is crucial to minimize the attack surface and potential vulnerabilities. Using minimal base images ensures that only essential components are included, reducing the number of potential security flaws. Removing unnecessary packages further decreases the likelihood of exploitable vulnerabilities. Regularly scanning images for known vulnerabilities allows for proactive identification and remediation of security risks. Running containers as root is discouraged because it gives the process elevated privileges that it does not need and exposes the host system to vulnerabilities. Exposing all ports creates unnecessary entry points for attackers.
**Sources:** <a href="https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-190.pdf" target="_blank">NIST Special Publication 800-190</a><br><a href="https://cheatsheetseries.owasp.org/cheatsheets/Container_Security_Cheat_Sheet.html" target="_blank">OWASP Container Security Cheat Sheet</a>

---

<!-- note:1772101855068 model:Many -->
**Domain:** Cloud Native Security
**Question:** In a Dockerfile, which instruction is used to specify that the container should run as a non-root user?
**Options:** A. FROM nonroot<br>B. USER nobody<br>C. RUN chmod 777 /app<br>D. EXPOSE 80<br>E. ENTRYPOINT ["/app"]
**Answer:** B (2) – USER nobody
**Explanation:** The 'USER' instruction in a Dockerfile sets the user under which the container process runs. Using 'USER nobody' ensures the application runs as a non-root user, enhancing container security. 'FROM nonroot' is not a valid instruction, 'RUN chmod 777 /app' changes permissions but does not change the user, 'EXPOSE' declares ports, and 'ENTRYPOINT' specifies the executable.
**Sources:** <a href="https://docs.docker.com/engine/reference/builder/#user" target="_blank">Dockerfile reference - USER instruction</a><br><a href="https://docs.docker.com/develop/dev-best-practices/#user" target="_blank">Docker Security Best Practices</a>

---

<!-- note:1772101855069 model:Many -->
**Domain:** Cloud Native Security
**Question:** What command is used to scan a Docker image named 'myapp:latest' for HIGH and CRITICAL vulnerabilities using Trivy?
**Options:** A. trivy myapp:latest<br>B. trivy image --severity HIGH,CRITICAL myapp:latest<br>C. trivy scan --critical myapp:latest<br>D. trivy image --vulnerabilities HIGH,CRITICAL myapp:latest<br>E. trivy inspect myapp:latest
**Answer:** B (2) – trivy image --severity HIGH,CRITICAL myapp:latest
**Explanation:** The correct command to scan for HIGH and CRITICAL vulnerabilities is 'trivy image --severity HIGH,CRITICAL myapp:latest'. This command specifically targets vulnerabilities of those severities in the Docker image.
**Sources:** <a href="https://aquasecurity.github.io/trivy/v0.34/docs/commands/image/" target="_blank">Trivy Documentation</a><br><a href="https://docs.docker.com/engine/security/security-bestpractices/" target="_blank">Docker Security Best Practices</a>

---

<!-- note:1772101855070 model:Many -->
**Domain:** Cloud Native Security
**Question:** Upon identifying a vulnerable Docker image in your Kubernetes cluster, what is the recommended immediate action to mitigate the risk?
**Options:** A. Ignore the vulnerability<br>B. Update the image tag to 'latest'<br>C. Delete the pod using the vulnerable image<br>D. Restart the Kubernetes cluster<br>E. Rebuild the image without changes
**Answer:** C (3) – Delete the pod using the vulnerable image
**Explanation:** The recommended immediate action is to delete the pod running the vulnerable image. This action helps mitigate the risk by removing the vulnerable container from your environment.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/security-best-practices/" target="_blank">Kubernetes Security Best Practices</a><br><a href="https://www.suse.com/products/security/vulnerability-management-in-kubernetes/" target="_blank">Vulnerability Management in Kubernetes</a>

---

<!-- note:1772101855073 model:Many -->
**Domain:** Cloud Native Security
**Question:** Which Docker flag allows a container to share the PID namespace with another container named 'container1'?
**Options:** A. --pid=host<br>B. --pid=container1<br>C. --pid=container:container1<br>D. --net=container:container1<br>E. --namespace=pid:container1
**Answer:** C (3) – --pid=container:container1
**Explanation:** The correct flag to share the PID namespace is '--pid=container:container1'. This allows processes in one container to see and interact with processes in the other container.
**Sources:** <a href="https://docs.docker.com/engine/reference/commandline/run/" target="_blank">Docker Run Reference</a><br><a href="https://man7.org/linux/man-pages/man7/pid_namespaces.7.html" target="_blank">PID Namespace Sharing</a>

---

<!-- note:1772101855074 model:Many -->
**Domain:** Cloud Native Security
**Question:** What is the primary effect of sharing the PID namespace between two Docker containers?
**Options:** A. They share the same network interfaces<br>B. They can see and signal each other's processes<br>C. They share the same filesystem<br>D. They can access each other's environment variables<br>E. They share the same memory space
**Answer:** B (2) – They can see and signal each other's processes
**Explanation:** Sharing the PID namespace allows containers to see and interact with each other's processes. This means they can send signals to processes running in the other container.
**Sources:** <a href="https://man7.org/linux/man-pages/man7/pid_namespaces.7.html" target="_blank">PID Namespaces</a><br><a href="https://docs.docker.com/engine/security/container_isolation/" target="_blank">Docker Container Isolation</a>

---

<!-- note:1772101855075 model:Many -->
**Domain:** Cloud Native Security
**Question:** Why is it recommended to use image digests instead of tags in Kubernetes manifests?
**Options:** A. Digests are shorter than tags<br>B. Tags can be mutable, but digests ensure image immutability<br>C. Using digests is required by Kubernetes<br>D. Tags are not supported in private registries<br>E. Digests allow for automatic updates
**Answer:** B (2) – Tags can be mutable, but digests ensure image immutability
**Explanation:** Image digests are recommended because they refer to a specific, immutable version of an image. This ensures consistency and predictability in deployments, unlike mutable tags.
**Sources:** <a href="https://kubernetes.io/docs/concepts/containers/images/#imagepullpolicy" target="_blank">Kubernetes Image Pull Policy</a><br><a href="https://docs.docker.com/registry/introduction/#immutable-images" target="_blank">Immutable Docker Images</a>

---

<!-- note:1772101855076 model:Many -->
**Domain:** Cloud Native Security
**Question:** How can you retrieve the digest (content hash) of the Docker image 'nginx:1.19' using the Docker CLI?
**Options:** A. docker images nginx:1.19 --digests<br>B. docker inspect nginx:1.19 --format='{{.Id}}'<br>C. docker pull nginx@sha256<br>D. docker inspect --format='{{index .RepoDigests 0}}' nginx:1.19<br>E. docker tag nginx:1.19 nginx:sha256
**Answer:** D (4) – docker inspect --format='{{index .RepoDigests 0}}' nginx:1.19
**Explanation:** The command 'docker inspect --format='{{index .RepoDigests 0}}' nginx:1.19' extracts the image digest from the image's metadata, showing the content-addressable identifier (digest) of the image. Option 1 lists digests for all images but may not show the specific digest for the tag. Option 2 shows the image ID, which is different from the digest. Option 3 is incomplete and incorrect syntax. Option 5 is unrelated to obtaining the digest, as it tags images but does not display digests.
**Sources:** <a href="https://docs.docker.com/engine/reference/commandline/inspect/" target="_blank">Docker Documentation - Inspect</a><br><a href="https://docs.docker.com/engine/reference/commandline/pull/#pull-an-image-by-digest-immutable-identifier" target="_blank">Docker Documentation - Image Digests</a>

---

<!-- note:1772101855105 model:Many -->
**Domain:** Cloud Native Security
**Question:** What is a significant security risk associated with using an insecure container registry?
**Options:** A. Faster image downloads<br>B. Increased image caching<br>C. Man-in-the-middle attacks leading to compromised images<br>D. Improved image availability<br>E. Automatic image updates
**Answer:** C (3) – Man-in-the-middle attacks leading to compromised images
**Explanation:** Using an insecure container registry exposes images to interception and tampering during transit, enabling man-in-the-middle attacks that can compromise container images. This can lead to running malicious or altered images in production. The other options describe benefits or neutral effects unrelated to security risks.
**Sources:** <a href="https://github.com/cncf/tag-security/blob/main/security-whitepaper/container-registry-security.md" target="_blank">CNCF - Container Registry Security Best Practices</a><br><a href="https://docs.docker.com/registry/security/" target="_blank">Docker Documentation - Registry Security</a>

---

<!-- note:1772101855106 model:Many -->
**Domain:** Cloud Native Security
**Question:** Which of the following is a recommended best practice when configuring container registries to ensure security?
**Options:** A. Use HTTP instead of HTTPS for performance<br>B. Allow anonymous access<br>C. Use authenticated and encrypted connections (HTTPS)<br>D. Disable TLS verification<br>E. Expose the registry publicly without restrictions
**Answer:** C (3) – Use authenticated and encrypted connections (HTTPS)
**Explanation:** Using HTTPS with authentication ensures that communication with the container registry is encrypted and access is controlled, preventing unauthorized access and tampering. Using HTTP or disabling TLS verification exposes the registry to interception and attacks. Allowing anonymous or unrestricted public access increases the risk of unauthorized image uploads or downloads.
**Sources:** <a href="https://docs.docker.com/registry/security/" target="_blank">Docker Documentation - Registry Security</a><br><a href="https://github.com/cncf/tag-security/blob/main/security-whitepaper/container-registry-security.md" target="_blank">CNCF - Container Registry Security Best Practices</a>

---

<!-- note:1772101855129 model:Many -->
**Domain:** Cloud Native Security
**Question:** During the build phase of a Kubernetes application, which practices are most effective for ensuring security?
**Options:** A. Use minimal base images to reduce the attack surface.<br>B. Run containers as root to simplify privilege management.<br>C. Scan images for vulnerabilities to identify and remediate potential security flaws.<br>D. Include unnecessary packages to provide additional functionality.<br>E. Use only authorized images from trusted registries to prevent the introduction of malicious code.
**Answer:** A (1) – Use minimal base images to reduce the attack surface.
**Explanation:** In the build phase, security is best ensured by minimizing the image footprint with minimal base images, regularly scanning for vulnerabilities to catch issues early, and using only authorized images from trusted sources.  Minimal base images reduce the attack surface.  Vulnerability scanning identifies and allows remediation of security flaws before deployment. Using authorized images prevents the introduction of untrusted or malicious code. Running containers as root is a security risk, and including unnecessary packages increases the potential attack surface.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/best-practices/" target="_blank">Kubernetes Security Best Practices</a><br><a href="https://www.sans.org/white-papers/36267/" target="_blank">SANS Institute: Securing Docker Containers</a>

---

<!-- note:1772101855138 model:Many -->
**Domain:** Cloud Native Security
**Question:** Which of the following are Kubernetes security best practices to follow during the Deploy phase? (Select all that apply)
**Options:** A. Implement network policies<br>B. Run containers as root<br>C. Use image tags like 'latest'<br>D. Use the ImagePolicyWebhook admission controller<br>E. Apply security contexts to pods and containers
**Answer:** A (1) – Implement network policies
**Explanation:** During deployment, implementing network policies restricts pod communication to only necessary traffic, reducing attack surfaces. The ImagePolicyWebhook admission controller enforces image security policies to prevent untrusted images from running. Applying security contexts defines permissions and restrictions for pods and containers, enhancing security. Running containers as root and using mutable tags like 'latest' are discouraged as they increase security risks and reduce traceability.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Documentation - Network Policies</a><br><a href="https://kubernetes.io/docs/concepts/security/pod-security-standards/" target="_blank">Kubernetes Documentation - Pod Security Standards</a>

---

<!-- note:1772101855142 model:Many -->
**Domain:** Cloud Native Security
**Question:** Why are 'distroless' container images recommended for use in production environments?
**Options:** A. They include a shell for debugging<br>B. They have a larger attack surface<br>C. They are minimal images that reduce vulnerabilities<br>D. They support all Linux distributions<br>E. They are required by Kubernetes
**Answer:** C (3) – They are minimal images that reduce vulnerabilities
**Explanation:** 'Distroless' images contain only the application and its runtime dependencies, excluding package managers, shells, and other unnecessary tools. This minimalism reduces the attack surface and potential vulnerabilities. They do not include shells, which can make debugging harder but improves security. They are not required by Kubernetes and do not inherently support all Linux distributions.
**Sources:** <a href="https://github.com/GoogleContainerTools/distroless" target="_blank">Google Distroless Images GitHub</a><br><a href="https://github.com/cncf/tag-security/blob/main/security-whitepaper/container-image-security.md" target="_blank">CNCF - Container Image Security Best Practices</a>

---
