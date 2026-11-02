# KCSA - Kubernetes and Cloud Native Security Associate — Platform Security

> Deck: `KCSA - Kubernetes and Cloud Native Security Associate` · Group: `Platform Security` · Notes: 34 · Models: Many

<!-- note:1772101854883 model:Many -->
**Domain:** Platform Security
**Question:** What is the primary role of Public Key Infrastructure (PKI) in IT security?
**Options:** A. Managing network configurations<br>B. Handling storage volumes<br>C. Issuing and managing digital certificates and encryption keys<br>D. Maintaining container images<br>E. Collecting and analyzing application logs
**Answer:** C (3) – Issuing and managing digital certificates and encryption keys
**Explanation:** Public Key Infrastructure (PKI) is a framework that manages digital certificates and encryption keys to enable secure communication and authentication over networks. It does not handle network configurations, storage volumes, container images, or application logs. PKI ensures trust by issuing certificates that verify identities and encrypt data.
**Sources:** <a href="https://learn.microsoft.com/en-us/windows-server/security/public-key-infrastructure/pki-overview" target="_blank">Microsoft Docs - Public Key Infrastructure (PKI)</a><br><a href="https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-32.pdf" target="_blank">NIST Special Publication 800-32 - Introduction to Public Key Technology and the Federal PKI Infrastructure</a>

---

<!-- note:1772101854884 model:Many -->
**Domain:** Platform Security
**Question:** What is the primary purpose of Grafana in IT operations?
**Options:** A. Managing code version control<br>B. Automating continuous integration pipelines<br>C. Visualizing and monitoring metrics through dashboards<br>D. Enforcing network security policies<br>E. Managing user identities and access
**Answer:** C (3) – Visualizing and monitoring metrics through dashboards
**Explanation:** Grafana is an open-source platform used primarily for creating dashboards that visualize metrics and monitoring data from various sources. It helps IT teams observe system performance and troubleshoot issues. It is not used for version control, continuous integration, network security enforcement, or identity management.
**Sources:** <a href="https://grafana.com/docs/grafana/latest/introduction/what-is-grafana/" target="_blank">Grafana Labs - What is Grafana?</a><br><a href="https://thenewstack.io/what-is-grafana/" target="_blank">The New Stack - Introduction to Grafana</a>

---

<!-- note:1772101854946 model:Many -->
**Domain:** Platform Security
**Question:** What is the recommended method to rotate TLS certificates in a Kubernetes cluster managed by kubeadm?
**Options:** A. Manually delete and recreate certificates<br>B. Use the 'kubeadm certs renew' command to renew certificates<br>C. TLS certificates cannot be rotated once issued<br>D. Restart the kubelet service to refresh certificates<br>E. Use a third-party certificate manager exclusively
**Answer:** B (2) – Use the 'kubeadm certs renew' command to renew certificates
**Explanation:** Kubernetes clusters initialized with kubeadm provide the 'kubeadm certs renew' command to safely renew TLS certificates without manual deletion. Manually deleting certificates or restarting kubelet alone is not sufficient and can cause downtime. While third-party certificate managers can be used, kubeadm's built-in commands are the recommended approach for certificate rotation.
**Sources:** <a href="https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/" target="_blank">Kubernetes Official Documentation - Managing Certificates</a><br><a href="https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-certs/" target="_blank">Kubeadm Certificate Management Guide</a>

---

<!-- note:1772101854952 model:Many -->
**Domain:** Platform Security
**Question:** Which tool serves as a data source for visualizing Kubernetes cluster metrics in Grafana?
**Options:** A. Prometheus<br>B. Elasticsearch<br>C. Kibana<br>D. Fluentd<br>E. Logstash
**Answer:** A (1) – Prometheus
**Explanation:** Prometheus is a robust monitoring and alerting toolkit that collects metrics from Kubernetes clusters. These metrics can be integrated into Grafana as a data source to create dashboards for visualization. While Grafana handles the visualization, Prometheus provides the necessary data. Other options like Elasticsearch, Kibana, Fluentd, and Logstash are primarily used for logging and log analysis, not for collecting or serving metrics directly.
**Sources:** <a href="https://kubernetes.io/docs/tasks/debug/debug-cluster/monitoring/" target="_blank">Kubernetes Documentation - Monitoring with Prometheus</a><br><a href="https://grafana.com/docs/grafana/latest/datasources/prometheus/" target="_blank">Grafana Documentation - Prometheus Integration</a>

---

<!-- note:1772101854958 model:Many -->
**Domain:** Platform Security
**Question:** Which kubectl command is used to retrieve the logs of a pod named 'my-pod'?
**Options:** A. kubectl get logs my-pod<br>B. kubectl describe my-pod<br>C. kubectl logs my-pod<br>D. kubectl status my-pod<br>E. kubectl inspect my-pod
**Answer:** C (3) – kubectl logs my-pod
**Explanation:** The correct command to view the logs of a pod named 'my-pod' is 'kubectl logs my-pod'. This command fetches the standard output and error logs from the pod's containers. 'kubectl describe' provides detailed resource information but not logs. The other commands are invalid or do not exist.
**Sources:** <a href="https://kubernetes.io/docs/tasks/debug/debug-application/logging/" target="_blank">Kubernetes Official Documentation - Viewing Logs</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs" target="_blank">Kubernetes kubectl Reference - logs</a>

---

<!-- note:1772101854967 model:Many -->
**Domain:** Platform Security
**Question:** Which kubectl command allows you to view the current resource usage (CPU and memory) of a specific pod?
**Options:** A. kubectl describe pod <pod-name><br>B. kubectl top pod <pod-name><br>C. kubectl get pod <pod-name> --resources<br>D. kubectl logs <pod-name><br>E. kubectl inspect pod <pod-name>
**Answer:** B (2) – kubectl top pod <pod-name>
**Explanation:** The 'kubectl top pod <pod-name>' command displays the current CPU and memory usage of the specified pod, provided that the Metrics Server is installed and running in the cluster. 'kubectl describe' shows detailed pod information but not real-time resource usage. The other commands do not provide resource consumption data.
**Sources:** <a href="https://kubernetes.io/docs/tasks/debug-application-cluster/resource-metrics-pipeline/" target="_blank">Kubernetes Official Documentation - Metrics Server</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#top" target="_blank">Kubernetes kubectl Reference - top</a>

---

<!-- note:1772101854977 model:Many -->
**Domain:** Platform Security
**Question:** Which kubectl command provides detailed information about a specific Kubernetes resource, including its configuration and status?
**Options:** A. kubectl get <resource><br>B. kubectl describe <resource><br>C. kubectl inspect <resource><br>D. kubectl show <resource><br>E. kubectl info <resource>
**Answer:** B (2) – kubectl describe <resource>
**Explanation:** The 'kubectl describe <resource>' command outputs detailed information about a Kubernetes resource, including its configuration, status, events, and other metadata. In contrast, 'kubectl get <resource>' provides a summary list or status of resources, but not detailed information. The other commands such as 'inspect', 'show', and 'info' are not valid kubectl commands for this purpose.
**Sources:** <a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe" target="_blank">Kubernetes Official Documentation - kubectl describe</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get" target="_blank">Kubernetes Official Documentation - kubectl get</a>

---

<!-- note:1772101854992 model:Many -->
**Domain:** Platform Security
**Question:** Which command is recommended to check the readiness and status of Kubernetes cluster components?
**Options:** A. kubectl get components<br>B. kubectl get --raw='/readyz?verbose'<br>C. kubectl get cs<br>D. kubectl get componentstatuses<br>E. kubectl describe components
**Answer:** B (2) – kubectl get --raw='/readyz?verbose'
**Explanation:** The command `kubectl get --raw='/readyz?verbose'` is the recommended way to check the readiness and status of Kubernetes cluster components. This approach provides detailed and up-to-date information about the health of the cluster. Other commands, such as `kubectl get cs` (deprecated shorthand) and `kubectl get componentstatuses` (deprecated endpoint), are no longer reliable in newer Kubernetes versions.
**Sources:** <a href="https://kubernetes.io/docs/reference/using-api/health-checks/" target="_blank">Kubernetes Official Documentation - API Server Health Checks</a><br><a href="https://kubernetes.io/blog/2020/09/03/kubectl-get-componentstatus-deprecated/" target="_blank">Kubernetes Blog - Deprecation of kubectl get cs</a>

---

<!-- note:1772101854993 model:Many -->
**Domain:** Platform Security
**Question:** Which kubectl command is used to check the health status and readiness of all nodes in a Kubernetes cluster?
**Options:** A. kubectl get nodes<br>B. kubectl describe nodes<br>C. kubectl health nodes<br>D. kubectl check nodes<br>E. kubectl status nodes
**Answer:** A (1) – kubectl get nodes
**Explanation:** 'kubectl get nodes' lists all nodes in the cluster along with their status, including whether they are Ready or NotReady, which indicates their health and availability. While 'kubectl describe nodes' provides detailed information about each node, including conditions and events, the primary command to quickly check node health is 'kubectl get nodes'. The other commands are not valid kubectl commands.
**Sources:** <a href="https://kubernetes.io/docs/tasks/administer-cluster/nodes/" target="_blank">Kubernetes Official Documentation - Viewing Nodes</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get" target="_blank">Kubernetes Official Documentation - kubectl get</a>

---

<!-- note:1772101855000 model:Many -->
**Domain:** Platform Security
**Question:** How do you display the full YAML definition of a specific pod in Kubernetes using kubectl?
**Options:** A. kubectl show pod <pod-name><br>B. kubectl get pod <pod-name> -o yaml<br>C. kubectl describe pod <pod-name><br>D. kubectl view pod <pod-name><br>E. kubectl yaml pod <pod-name>
**Answer:** B (2) – kubectl get pod <pod-name> -o yaml
**Explanation:** The command 'kubectl get pod <pod-name> -o yaml' outputs the complete YAML manifest of the specified pod, showing its configuration as stored in the cluster. 'kubectl describe pod <pod-name>' provides detailed runtime information but not the raw YAML definition. The other commands are not valid kubectl commands.
**Sources:** <a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get" target="_blank">Kubernetes Official Documentation - kubectl get</a><br><a href="https://kubernetes.io/docs/concepts/workloads/pods/" target="_blank">Kubernetes Official Documentation - Viewing Pods</a>

---

<!-- note:1772101855008 model:Many -->
**Domain:** Platform Security
**Question:** Which kubectl command allows you to view the events occurring in a Kubernetes cluster, such as pod lifecycle changes and errors, using the most current recommended method?
**Options:** A. kubectl get events<br>B. kubectl describe events<br>C. kubectl list events<br>D. kubectl events<br>E. kubectl get logs
**Answer:** D (4) – kubectl events
**Explanation:** 'kubectl events' is the newer and recommended command for viewing events in a Kubernetes cluster, including pod lifecycle changes, warnings, and errors. It provides enhanced filtering and output options compared to the traditional 'kubectl get events'. 'kubectl describe events' is not a valid command; 'kubectl describe' is used with specific resource types but not directly with 'events'. 'kubectl list events' is not a valid command. 'kubectl get logs' is used to fetch logs from pods, not cluster events.
**Sources:** <a href="https://kubernetes.io/docs/tasks/debug/debug-cluster/event-logging/" target="_blank">Kubernetes Official Documentation - Viewing Events</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#events" target="_blank">Kubernetes Official Documentation - kubectl events</a>

---

<!-- note:1772101855015 model:Many -->
**Domain:** Platform Security
**Question:** Which kubectl command lists all the nodes currently registered in a Kubernetes cluster?
**Options:** A. kubectl get nodes<br>B. kubectl describe cluster<br>C. kubectl list nodes<br>D. kubectl cluster-info<br>E. kubectl get cluster-nodes
**Answer:** A (1) – kubectl get nodes
**Explanation:** 'kubectl get nodes' is the standard command to list all nodes in the cluster along with their status and other summary information. 'kubectl describe cluster' and 'kubectl get cluster-nodes' are not valid commands. 'kubectl list nodes' is not a valid kubectl command. 'kubectl cluster-info' provides cluster endpoint information but does not list nodes.
**Sources:** <a href="https://kubernetes.io/docs/concepts/architecture/nodes/" target="_blank">Kubernetes Official Documentation - Nodes</a><br><a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get" target="_blank">Kubernetes Official Documentation - kubectl get</a>

---

<!-- note:1772101855046 model:Many -->
**Domain:** Platform Security
**Question:** Which tool is specifically designed to benchmark a Kubernetes cluster against the Center for Internet Security (CIS) Kubernetes Benchmark best practices?
**Options:** A. kube-bench<br>B. kube-hunter<br>C. kubesec<br>D. kube-score<br>E. kube-linter
**Answer:** A (1) – kube-bench
**Explanation:** kube-bench is a tool that runs checks against the CIS Kubernetes Benchmark, which is a set of best practices for securing Kubernetes clusters. It audits cluster components and configuration to identify security issues. Other tools like kube-hunter focus on penetration testing, kubesec and kube-score analyze resource configurations but do not perform CIS benchmark compliance checks, and kube-linter is a static analysis tool for Kubernetes manifests.
**Sources:** <a href="https://github.com/aquasecurity/kube-bench" target="_blank">Aqua Security - kube-bench GitHub Repository</a><br><a href="https://www.cisecurity.org/benchmark/kubernetes/" target="_blank">Center for Internet Security - Kubernetes Benchmark</a>

---

<!-- note:1772101855047 model:Many -->
**Domain:** Platform Security
**Question:** Which Kubernetes resource enables automatic horizontal scaling of Pods based on observed CPU utilization?
**Options:** A. HorizontalPodAutoscaler<br>B. VerticalPodAutoscaler<br>C. ResourceQuota<br>D. LimitRange<br>E. Deployment
**Answer:** A (1) – HorizontalPodAutoscaler
**Explanation:** The HorizontalPodAutoscaler (HPA) automatically adjusts the number of pod replicas in a deployment or replica set based on observed CPU utilization or other select metrics. VerticalPodAutoscaler adjusts resource requests and limits for containers rather than scaling pod count. ResourceQuota and LimitRange control resource usage limits but do not perform scaling. Deployment manages pod lifecycle but does not scale automatically based on CPU.
**Sources:** <a href="https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/" target="_blank">Kubernetes Official Documentation - Horizontal Pod Autoscaling</a><br><a href="https://kubernetes.io/docs/tasks/run-application/vertical-pod-autoscale/" target="_blank">Kubernetes Official Documentation - Vertical Pod Autoscaling</a>

---

<!-- note:1772101855054 model:Many -->
**Domain:** Platform Security
**Question:** Which kubectl command provides detailed information about a specific Kubernetes node, including its status, capacity, and allocated resources?
**Options:** A. kubectl get node <node-name><br>B. kubectl describe node <node-name><br>C. kubectl inspect node <node-name><br>D. kubectl info node <node-name><br>E. kubectl logs node <node-name>
**Answer:** B (2) – kubectl describe node <node-name>
**Explanation:** The command 'kubectl describe node <node-name>' shows detailed information about the node, such as labels, annotations, resource capacity, allocated resources, conditions, and events. 'kubectl get node' provides a summary list of nodes but not detailed info. 'kubectl inspect' and 'kubectl info' are not valid kubectl commands for nodes. 'kubectl logs' is used for retrieving logs from pods, not nodes.
**Sources:** <a href="https://kubernetes.io/docs/tasks/administer-cluster/nodes/" target="_blank">Kubernetes Official Documentation - Inspecting Nodes</a><br><a href="https://kubernetes.io/docs/reference/kubectl/cheatsheet/" target="_blank">Kubernetes kubectl Cheat Sheet</a>

---

<!-- note:1772101855055 model:Many -->
**Domain:** Platform Security
**Question:** Which flag combination with the 'kubectl run' command generates a Pod manifest in YAML format without actually creating the Pod resource in the cluster?
**Options:** A. --dry-run=server<br>B. --dry-run=client -o yaml<br>C. --output=yaml<br>D. --generate-only<br>E. --no-create
**Answer:** B (2) – --dry-run=client -o yaml
**Explanation:** Using '--dry-run=client -o yaml' with 'kubectl run' simulates the creation of the Pod resource on the client side and outputs the manifest in YAML format without sending it to the API server, thus not creating the resource. '--dry-run=server' validates on the server side but does not output YAML by default. '--output=yaml' alone does not prevent creation. '--generate-only' and '--no-create' are deprecated or invalid flags.
**Sources:** <a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#run" target="_blank">Kubernetes Official Documentation - kubectl run</a><br><a href="https://kubernetes.io/blog/2020/06/08/kubectl-dry-run/" target="_blank">Kubernetes Blog - Understanding kubectl dry-run</a>

---

<!-- note:1772101855057 model:Many -->
**Domain:** Platform Security
**Question:** Which command is used to apply configuration changes defined in 'deployment.yaml' to a Kubernetes resource?
**Options:** A. kubectl create -f deployment.yaml<br>B. kubectl apply -f deployment.yaml<br>C. kubectl set -f deployment.yaml<br>D. kubectl update -f deployment.yaml<br>E. kubectl replace -f deployment.yaml
**Answer:** B (2) – kubectl apply -f deployment.yaml
**Explanation:** The 'kubectl apply -f deployment.yaml' command applies configuration changes to a Kubernetes resource defined in the YAML file. It uses declarative management, ensuring that the resource's current state matches the desired state specified in the file. Other commands like 'kubectl create' are used for creating resources but do not update existing ones, while 'kubectl replace' replaces the entire resource instead of merging changes.
**Sources:** <a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply" target="_blank">Kubernetes Documentation: kubectl apply</a><br><a href="https://spacelift.io/blog/kubectl-apply-vs-create" target="_blank">Spacelift Blog: kubectl apply vs create</a>

---

<!-- note:1772101855063 model:Many -->
**Domain:** Platform Security
**Question:** Which command is used to generate a 2048-bit RSA private key for a new Kubernetes user?
**Options:** A. openssl genrsa -out user.key 2048<br>B. openssl rsa -in user.key -out user.key<br>C. openssl req -newkey rsa:2048 -nodes -keyout user.key -out user.csr<br>D. kubectl create secret tls user.key<br>E. ssh-keygen -t rsa -b 2048 -f user.key
**Answer:** A (1) – openssl genrsa -out user.key 2048
**Explanation:** The command 'openssl genrsa -out user.key 2048' generates a 2048-bit RSA private key and saves it to 'user.key'. The second command attempts to process an existing key but does not generate a new one. The third command generates a new private key and a certificate signing request (CSR), not just the key. 'kubectl create secret tls' is for creating TLS secrets, not generating keys. 'ssh-keygen' generates SSH keys, which are different from the keys used for Kubernetes user certificates.
**Sources:** <a href="https://www.openssl.org/docs/man1.1.1/man1/openssl-genrsa.html" target="_blank">OpenSSL Documentation - genrsa</a><br><a href="https://kubernetes.io/docs/tasks/administer-cluster/certificates/" target="_blank">Kubernetes Official Documentation - Creating a Client Certificate</a>

---

<!-- note:1772101855064 model:Many -->
**Domain:** Platform Security
**Question:** After generating a Certificate Signing Request (CSR) and having it signed by the Kubernetes cluster Certificate Authority (CA), how do you configure kubectl to use the new client certificate and key for the user 'alice'?
**Options:** A. kubectl config set-credentials alice --client-certificate=alice.crt --client-key=alice.key<br>B. kubectl create secret tls alice --cert=alice.crt --key=alice.key<br>C. kubectl config set-context alice-context --cluster=kubernetes --user=alice<br>D. kubectl apply -f alice.crt<br>E. kubectl certificate approve alice
**Answer:** A (1) – kubectl config set-credentials alice --client-certificate=alice.crt --client-key=alice.key
**Explanation:** To configure kubectl to use a new client certificate for a user, you use the command 'kubectl config set-credentials' specifying the user name along with the paths to the client certificate and private key files. This updates the kubeconfig file with the user's credentials. The other options do not configure kubectl credentials: 'kubectl create secret tls' creates a TLS secret in Kubernetes but does not affect kubectl client config; 'kubectl config set-context' sets the context but does not set credentials; 'kubectl apply -f' applies Kubernetes resources and is unrelated; 'kubectl certificate approve' approves a CSR but does not configure kubectl.
**Sources:** <a href="https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/" target="_blank">Kubernetes Official Documentation - Configure Access to Multiple Clusters</a><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/" target="_blank">Kubernetes Official Documentation - Certificate Signing Requests</a>

---

<!-- note:1772101855079 model:Many -->
**Domain:** Platform Security
**Question:** Which commands can be used to list all loaded AppArmor profiles on a Linux node?
**Options:** A. sudo apparmor_status<br>B. sudo aa-enforce<br>C. sudo apparmor_parser -L<br>D. sudo aa-status<br>E. sudo systemctl status apparmor
**Answer:** A (1) – sudo apparmor_status
**Explanation:** Both `sudo apparmor_status` and `sudo aa-status` can be used to list all loaded AppArmor profiles on a Linux node. These commands provide detailed information about AppArmor, including the number of loaded profiles, their modes (enforce or complain), and any unconfined processes.<br><br>Other options are incorrect for the following reasons:<br><br>1. `sudo aa-enforce`: This command is used to set an AppArmor profile to enforce mode, not to list profiles.<br>2. `sudo apparmor_parser -L`: This command is used for loading AppArmor profiles but does not list them.<br>3. `sudo systemctl status apparmor`: This command checks the status of the AppArmor service but does not provide a list of loaded profiles.<br><br>Using either `sudo apparmor_status` or `sudo aa-status` ensures you can monitor and manage AppArmor profiles effectively.
**Sources:** <a href="https://ubuntu.com/server/docs/security-apparmor" target="_blank">AppArmor Documentation - Ubuntu</a><br><a href="https://manpages.ubuntu.com/manpages/bionic/man8/aa-status.8.html" target="_blank">Linux Manual Pages - aa-status</a>

---

<!-- note:1772101855080 model:Many -->
**Domain:** Platform Security
**Question:** In Kubernetes, how can you apply an AppArmor profile to all containers within a Pod?
**Options:** A. Set the profile in the Pod's securityContext<br>B. Annotate each container with the AppArmor profile<br>C. Use the 'appArmorProfile' field in the container spec<br>D. Specify the profile in the Deployment's metadata<br>E. Set the profile in the node's AppArmor configuration
**Answer:** B (2) – Annotate each container with the AppArmor profile
**Explanation:** To apply an AppArmor profile to all containers in a Pod, you can use one of two methods:<br><br>1. **Annotations**: Use the annotation `container.apparmor.security.beta.kubernetes.io/<container_name>: <profile_ref>` for each container in the Pod. This method has been traditionally used and is backward-compatible.<br><br>2. **`appArmorProfile` field in `securityContext`**: Starting with Kubernetes v1.30, you can specify the AppArmor profile directly in the `securityContext` of a container using the `appArmorProfile` field. This method is more intuitive and avoids relying on annotations.<br><br>Other options, such as setting it in the Deployment metadata or node-level configuration, are not valid methods for applying AppArmor profiles to specific containers.
**Sources:** <a href="https://kubernetes.io/docs/tutorials/clusters/apparmor/" target="_blank">Kubernetes Official Documentation - Security Contexts</a><br><a href="https://kubernetes.io/docs/setup/release/notes/#feature-apparmor-profile-in-securitycontext" target="_blank">Kubernetes v1.30 Release Notes</a>

---

<!-- note:1772101855093 model:Many -->
**Domain:** Platform Security
**Question:** Which Kubernetes resource object is used to request a certificate signing operation via the Kubernetes API?
**Options:** A. CertificateRequest<br>B. CertificateSigningRequest<br>C. CertificateApproval<br>D. CertificateSigning<br>E. Certificate
**Answer:** B (2) – CertificateSigningRequest
**Explanation:** The Kubernetes resource 'CertificateSigningRequest' (CSR) is the official API object used to request a certificate signing operation. Users or components create a CSR object containing a public key and metadata; cluster administrators or automated controllers then approve and sign it. The other options are not valid Kubernetes resource kinds: 'CertificateRequest' and 'CertificateSigning' do not exist as Kubernetes resources; 'CertificateApproval' is not a resource but an action; 'Certificate' is not a Kubernetes resource for CSRs.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/" target="_blank">Kubernetes Official Documentation - Certificate Signing Requests</a><br><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#certificatesigningrequest-v1-certificates-k8s-io" target="_blank">Kubernetes API Reference - CertificateSigningRequest</a>

---

<!-- note:1772101855094 model:Many -->
**Domain:** Platform Security
**Question:** Which command is used to approve a CertificateSigningRequest (CSR) in Kubernetes?
**Options:** A. kubectl sign csr <csr-name><br>B. kubectl create csr <csr-name><br>C. kubectl certificate approve <csr-name><br>D. kubectl approve csr <csr-name><br>E. kubectl csr approve <csr-name>
**Answer:** C (3) – kubectl certificate approve <csr-name>
**Explanation:** The correct command to approve a CertificateSigningRequest (CSR) in Kubernetes is 'kubectl certificate approve <csr-name>'. This command instructs the certificate signing controller to approve the CSR, allowing the requested certificate to be issued. Other options like 'kubectl create' are used for creating resources, while 'kubectl sign', 'kubectl approve csr', and 'kubectl csr approve' are invalid commands.
**Sources:** <a href="https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/" target="_blank">Kubernetes Documentation: Managing TLS Certificates</a><br><a href="https://kubernetes.io/docs/reference/kubectl/generated/kubectl_certificate/kubectl_certificate_approve/" target="_blank">Kubernetes Reference: kubectl certificate approve</a>

---

<!-- note:1772101855097 model:Many -->
**Domain:** Platform Security
**Question:** Which command lists all processes currently listening on TCP and UDP ports on a Linux system, including the associated process IDs?
**Options:** A. sudo netstat -tulpn<br>B. sudo lsof -i<br>C. sudo ss -tulw<br>D. sudo ps aux | grep LISTEN<br>E. sudo netstat -an
**Answer:** A (1) – sudo netstat -tulpn
**Explanation:** The command 'sudo netstat -tulpn' lists all listening TCP and UDP ports along with the process IDs and names that are using those ports. The flags mean: '-t' for TCP, '-u' for UDP, '-l' for listening sockets, '-p' to show process info, and '-n' to show numeric addresses. 'sudo lsof -i' also shows network connections but is less focused on listening ports specifically. 'sudo ss -tulw' shows listening sockets but may omit process names without additional flags. 'sudo ps aux | grep LISTEN' is incorrect because 'LISTEN' is not a process name but a socket state. 'sudo netstat -an' shows all connections but does not include process information.
**Sources:** <a href="https://man7.org/linux/man-pages/man8/netstat.8.html" target="_blank">Linux man page - netstat</a><br><a href="https://man7.org/linux/man-pages/man8/ss.8.html" target="_blank">Linux man page - ss</a>

---

<!-- note:1772101855098 model:Many -->
**Domain:** Platform Security
**Question:** After identifying an unwanted process listening on a network port, which command can you use to terminate that process by its process ID (PID)?
**Options:** A. killall <process-name><br>B. sudo stop <process-name><br>C. sudo systemctl disable <process-name><br>D. sudo kill <pid><br>E. sudo service <process-name> remove
**Answer:** D (4) – sudo kill <pid>
**Explanation:** The command 'sudo kill <pid>' sends a termination signal to the process with the specified PID, effectively stopping it. 'killall <process-name>' kills all processes matching the name but requires the exact process name and may affect multiple processes. 'sudo stop <process-name>' is used to stop services managed by Upstart, which is less common now. 'sudo systemctl disable <process-name>' disables a systemd service from starting on boot but does not stop a running process immediately. 'sudo service <process-name> remove' is not a valid command to stop processes.
**Sources:** <a href="https://man7.org/linux/man-pages/man1/kill.1.html" target="_blank">Linux kill Command Manual</a><br><a href="https://man7.org/linux/man-pages/man1/killall.1.html" target="_blank">Linux killall Command Manual</a>

---

<!-- note:1772101855099 model:Many -->
**Domain:** Platform Security
**Question:** Which command is used to remove the 'apache2' package from a Debian-based Linux system?
**Options:** A. sudo apt-get install apache2<br>B. sudo yum remove apache2<br>C. sudo apt-get remove apache2<br>D. sudo rpm -e apache2<br>E. sudo dnf erase apache2
**Answer:** C (3) – sudo apt-get remove apache2
**Explanation:** On Debian-based systems (such as Ubuntu), the package manager 'apt-get' is used to manage packages. The command 'sudo apt-get remove apache2' uninstalls the 'apache2' package but retains configuration files. 'sudo apt-get install apache2' installs the package. 'sudo yum remove apache2' and 'sudo dnf erase apache2' are used on Red Hat-based systems, not Debian-based. 'sudo rpm -e apache2' is also for RPM-based distributions and not applicable to Debian-based systems.
**Sources:** <a href="https://wiki.debian.org/Apt" target="_blank">Debian Administration - Package Management</a><br><a href="https://help.ubuntu.com/community/AptGet/Howto" target="_blank">Ubuntu Official Documentation - Package Management</a>

---

<!-- note:1772101855100 model:Many -->
**Domain:** Platform Security
**Question:** Which command lists all installed packages on a Debian-based Linux system using the apt package manager?
**Options:** A. apt list --installed<br>B. dpkg -l<br>C. rpm -qa<br>D. yum list installed<br>E. pkg info
**Answer:** A (1) – apt list --installed
**Explanation:** The command 'apt list --installed' displays all packages installed via the apt package manager on Debian-based systems. While 'dpkg -l' also lists installed packages, it shows lower-level package information and is not specific to apt. 'rpm -qa' and 'yum list installed' are commands used on RPM-based systems like Red Hat or CentOS, and 'pkg info' is used in BSD-based systems, making them incorrect for Debian-based systems.
**Sources:** <a href="https://wiki.debian.org/Apt" target="_blank">Debian Wiki - APT</a><br><a href="https://manpages.ubuntu.com/manpages/focal/en/man8/apt.8.html" target="_blank">Ubuntu Manpage - apt</a>

---

<!-- note:1772101855101 model:Many -->
**Domain:** Platform Security
**Question:** Which strace command-line option provides a summary of the time spent in each system call during program execution?
**Options:** A. -c<br>B. -p<br>C. -t<br>D. -e trace=%time<br>E. -s
**Answer:** A (1) – -c
**Explanation:** The '-c' option in strace outputs a summary report showing the count, total time, and average time spent in each system call, helping analyze performance bottlenecks. The '-p' option attaches strace to an existing process by PID, '-t' prefixes each line with a timestamp, '-e trace=%time' is not a valid option, and '-s' sets the maximum string size to print, so they do not provide a time summary.
**Sources:** <a href="https://man7.org/linux/man-pages/man1/strace.1.html" target="_blank">strace Manual</a><br><a href="https://www.linuxjournal.com/article/6460" target="_blank">Linux Journal - Using strace</a>

---

<!-- note:1772101855102 model:Many -->
**Domain:** Platform Security
**Question:** Which strace command attaches to an already running process with PID 1234 to trace its system calls?
**Options:** A. strace 1234<br>B. strace -p 1234<br>C. strace -c 1234<br>D. sudo trace -pid 1234<br>E. strace --process 1234
**Answer:** B (2) – strace -p 1234
**Explanation:** The correct command to attach strace to a running process with PID 1234 is 'strace -p 1234'. The '-p' option specifies the process ID to attach to. 'strace 1234' attempts to run a new process named '1234', which is invalid. 'strace -c 1234' runs strace with summary statistics on a new process named '1234'. 'sudo trace -pid 1234' is not a valid command, and 'strace --process 1234' is not a recognized option.
**Sources:** <a href="https://man7.org/linux/man-pages/man1/strace.1.html" target="_blank">strace Manual</a><br><a href="https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/sect-troubleshooting-strace" target="_blank">Red Hat Documentation - strace</a>

---

<!-- note:1772101855103 model:Many -->
**Domain:** Platform Security
**Question:** Which command calculates the SHA256 checksum of the file '/usr/bin/kubelet' on a Linux system?
**Options:** A. sha1sum /usr/bin/kubelet<br>B. md5sum /usr/bin/kubelet<br>C. checksum -sha256 /usr/bin/kubelet<br>D. sha256sum /usr/bin/kubelet<br>E. hash -a sha256 /usr/bin/kubelet
**Answer:** D (4) – sha256sum /usr/bin/kubelet
**Explanation:** The command 'sha256sum /usr/bin/kubelet' computes the SHA256 checksum of the specified file, which is commonly used to verify file integrity. 'sha1sum' and 'md5sum' calculate different hash algorithms (SHA1 and MD5 respectively). 'checksum -sha256' and 'hash -a sha256' are not standard Linux commands for checksum calculation.
**Sources:** <a href="https://www.gnu.org/software/coreutils/manual/html_node/sha256sum-invocation.html" target="_blank">GNU Coreutils - sha256sum</a><br><a href="https://kubernetes.io/docs/tasks/tools/install-kubectl/#verifying-the-kubectl-binary" target="_blank">Kubernetes Official Documentation - Verifying Binaries</a>

---

<!-- note:1772101855104 model:Many -->
**Domain:** Platform Security
**Question:** Why is it critical to verify the checksums of Kubernetes binaries after downloading them?
**Options:** A. To ensure they are the latest version<br>B. To verify the integrity and authenticity of the binaries<br>C. To improve their performance<br>D. To check for syntax errors<br>E. To enable automatic updates
**Answer:** B (2) – To verify the integrity and authenticity of the binaries
**Explanation:** Verifying the checksums of Kubernetes binaries ensures that the files have not been tampered with or corrupted during download, confirming their integrity and authenticity. This protects against malicious modifications or accidental corruption. Checking for the latest version, performance improvements, syntax errors, or enabling automatic updates are unrelated to checksum verification.
**Sources:** <a href="https://kubernetes.io/docs/tasks/tools/install-kubectl/#verifying-the-kubectl-binary" target="_blank">Kubernetes Official Documentation - Verifying Binaries</a><br><a href="https://csrc.nist.gov/publications/detail/sp/800-163/final" target="_blank">NIST - Guide to Software Integrity Verification</a>

---

<!-- note:1772101855143 model:Many -->
**Domain:** Platform Security
**Question:** What is the primary function of a Service Mesh in Kubernetes architecture?
**Options:** A. A network overlay for pod communication<br>B. An infrastructure layer for handling service-to-service communication<br>C. A type of storage solution<br>D. A container runtime interface<br>E. A logging mechanism
**Answer:** B (2) – An infrastructure layer for handling service-to-service communication
**Explanation:** A Service Mesh is a dedicated infrastructure layer that manages service-to-service communication through sidecar proxies, providing features like traffic management, service discovery, and security policies without requiring application code changes. While pod communication occurs through the mesh, it's not merely a network overlay but rather a comprehensive communication management layer.
**Sources:** <a href="https://istio.io/latest/docs/concepts/what-is-istio/" target="_blank">Istio Documentation</a><br><a href="https://smi-spec.io/" target="_blank">Kubernetes Service Mesh Interface (SMI) Specification</a>

---

<!-- note:1772101855144 model:Many -->
**Domain:** Platform Security
**Question:** Which of the following are key advantages of implementing a Service Mesh in Kubernetes? (Select all that apply)
**Options:** A. Built-in observability through metrics, logs, and traces<br>B. Simplifies application code by offloading cross-cutting concerns<br>C. Enhanced security through mutual TLS encryption<br>D. Adds significant latency to all communications<br>E. Requires minimal operational expertise to implement
**Answer:** A (1) – Built-in observability through metrics, logs, and traces
**Explanation:** Service Meshes provide three primary benefits: 1) Comprehensive observability through automatic collection of communication metrics and distributed tracing. 2) Offloading of cross-cutting concerns like retries, timeouts, and circuit breaking from application code. 3) Security enhancements through automatic mutual TLS and fine-grained access controls. While they add some overhead, modern implementations minimize latency impact through optimized data planes.
**Sources:** <a href="https://www.cncf.io/blog/2020/10/06/service-mesh-a-cncf-white-paper/" target="_blank">CNCF Service Mesh White Paper</a><br><a href="https://linkerd.io/2.11/features/" target="_blank">Linkerd Documentation</a>

---

<!-- note:1772101855154 model:Many -->
**Domain:** Platform Security
**Question:** What is the correct kubectl command to set the default namespace for all subsequent operations in the current context?
**Options:** A. kubectl config use-context <namespace><br>B. kubectl set namespace <namespace><br>C. kubectl config set-context --current --namespace=<namespace><br>D. kubectl namespace set <namespace><br>E. kubectl switch namespace <namespace>
**Answer:** C (3) – kubectl config set-context --current --namespace=<namespace>
**Explanation:** The command 'kubectl config set-context --current --namespace=<namespace>' modifies the current context's namespace setting persistently. This differs from temporary namespace overrides using '-n' flag, and ensures all subsequent commands use the specified namespace by default. Other options either use incorrect syntax or modify different configuration aspects.
**Sources:** <a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#config" target="_blank">Kubernetes Official Documentation - kubectl config</a><br><a href="https://kubernetes.io/docs/reference/kubectl/cheatsheet/" target="_blank">Kubernetes Cheat Sheet - Configuration</a>

---
