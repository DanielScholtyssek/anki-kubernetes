# CKS - Certified Kubernetes Security Specialist — Monitoring, Logging and Runtime Security

> Deck: `CKS - Certified Kubernetes Security Specialist` · Group: `Monitoring, Logging and Runtime Security` · Notes: 75 · Models: Basic+

<!-- note:1772498120456 model:Basic+ -->
**Front:** What is the purpose of auditing in Kubernetes?
**Back:** Auditing in Kubernetes records and tracks all cluster activities to ensure security, achieve compliance, and facilitate troubleshooting by maintaining a detailed history of events.
**Tags:** ankidote kubernetes-auditing security-compliance

---

<!-- note:1772498120458 model:Basic+ -->
**Front:** What details are captured in Kubernetes audit logs?
**Back:** Audit logs include user identity, timestamps, affected resources, operation type, source IPs, user agents, request/response bodies, and authorization decisions.
**Tags:** ankidote audit-logs kubernetes-auditing

---

<!-- note:1772498120461 model:Basic+ -->
**Front:** List the four audit policy levels in Kubernetes.
**Back:** 1. None (no logs), 2. Metadata (logs metadata only), 3. Request (logs metadata and request body), 4. Request Response (logs metadata, request, and response bodies).
**Tags:** ankidote audit-policies kubernetes-auditing

---

<!-- note:1772498120463 model:Basic+ -->
**Front:** What is the role of audit logs in compliance?
**Back:** Audit logs provide a detailed trail for regulatory compliance (e.g., GDPR, HIPAA, PCI-DSS) by documenting user actions, resource changes, and authorization decisions.
**Tags:** ankidote audit-logs compliance

---

<!-- note:1772498120465 model:Basic+ -->
**Front:** What fields are included in a Kubernetes audit event?
**Back:** Fields include kind, apiVersion, level, auditID, stage, requestURI, verb, user details, sourceIPs, userAgent, objectRef, responseStatus, timestamps, and annotations.
**Tags:** ankidote audit-event kubernetes-auditing

---

<!-- note:1772498120467 model:Basic+ -->
**Front:** What does the Metadata audit policy log?
**Back:** The Metadata policy logs request metadata (user, timestamp, resource, verb) without request/response bodies.
**Tags:** ankidote audit-policies kubernetes-auditing

---

<!-- note:1772498120469 model:Basic+ -->
**Front:** What is the difference between Request and Request Response policies?
**Back:** Request logs metadata and the request body but excludes the response body. Request Response logs metadata, request body, and response body.
**Tags:** ankidote audit-policies kubernetes-auditing

---

<!-- note:1772498120472 model:Basic+ -->
**Front:** What is the purpose of the audit.k8s.io/v1 API version?
**Back:** The audit.k8s.io/v1 API version defines the structure and format of audit events, including metadata, request/response details, and timestamps.
**Tags:** ankidote audit-api kubernetes-auditing

---

<!-- note:1772498120474 model:Basic+ -->
**Front:** Provide a YAML example for a Metadata audit policy.
**Back:** apiVersion: audit.k8s.io/v1
kind: Policy
rules:
- level: Metadata
  verbs: ["get", "list", "create", "delete", "update"]
  resources:
  - group: ""
    resources: ["pods"]
**Tags:** ankidote audit-policy yaml-configuration

---

<!-- note:1772498120476 model:Basic+ -->
**Front:** What does the 'stage' field in an audit event indicate?
**Back:** The 'stage' field indicates the phase of processing, such as 'ResponseComplete', which signifies the event was fully processed and logged.
**Tags:** ankidote audit-event kubernetes-auditing

---

<!-- note:1772501004030 model:Basic+ -->
**Front:** Where is Falco's main configuration file located?
**Back:** /etc/falco/falco.yaml
**Tags:** ankidote configuration-file main-config

---

<!-- note:1772501004034 model:Basic+ -->
**Front:** What determines the order of rule files in Falco?
**Back:** The 'rules_file' field in the configuration file specifies the order, with later files overriding earlier ones.
**Tags:** ankidote configuration-file rule-loading

---

<!-- note:1772501004037 model:Basic+ -->
**Front:** Where should custom rules be added to avoid being overwritten?
**Back:** /etc/falco/falco_rules.local.yaml
**Tags:** ankidote configuration-file custom-rules

---

<!-- note:1772501004041 model:Basic+ -->
**Front:** What setting enables JSON output for Falco events?
**Back:** The 'json_output' parameter in the configuration file.
**Tags:** ankidote configuration-options output-format

---

<!-- note:1772501004050 model:Basic+ -->
**Front:** How to configure file logging for Falco events?
**Back:** Enable 'file_output' with a filename in the configuration file.
**Tags:** ankidote file-logging output-channels

---

<!-- note:1772501004053 model:Basic+ -->
**Front:** What is the default location for Falco's built-in rules?
**Back:** /etc/falco/falco_rules.yaml
**Tags:** ankidote built-in-rules configuration-file

---

<!-- note:1772501004056 model:Basic+ -->
**Front:** How to reload Falco configuration without restarting the service?
**Back:** Send a SIGHUP signal to the Falco process using its PID from /var/run/falco.pid.
**Tags:** ankidote configuration hot-reloading

---

<!-- note:1772501004060 model:Basic+ -->
**Front:** What parameter controls Falco's log level?
**Back:** The 'log_level' parameter in the configuration file.
**Tags:** ankidote configuration-options logging

---

<!-- note:1772501004063 model:Basic+ -->
**Front:** What is the purpose of the 'rules_file' field?
**Back:** To specify a list of rule files that Falco loads during startup, with later files overriding earlier ones.
**Tags:** ankidote configuration-file rule-loading

---

<!-- note:1772501004066 model:Basic+ -->
**Front:** How to enable Slack alerts via program_output in Falco?
**Back:** Configure 'program_output' with a command that sends data to a Slack webhook URL.
**Tags:** ankidote output-channels program-output

---

<!-- note:1772501043932 model:Basic+ -->
**Front:** What are the two methods Falco uses to interact with the Linux kernel?
**Back:** Falco uses the kernel module method (intrusive) and the eBPF method (less invasive).
**Tags:** ankidote ebpf falco-architecture kernel-module

---

<!-- note:1772501043938 model:Basic+ -->
**Front:** What is the purpose of Falco's policy engine?
**Back:** Falco's policy engine evaluates system calls using predefined rules to detect suspicious activities and generate alerts.
**Tags:** ankidote falco-architecture policy-engine security-rules

---

<!-- note:1772501043941 model:Basic+ -->
**Front:** What is the advantage of using eBPF over a kernel module for Falco?
**Back:** eBPF is less invasive and has a lower impact on system integrity compared to kernel modules.
**Tags:** ankidote ebpf falco-architecture kernel-module

---

<!-- note:1772501043943 model:Basic+ -->
**Front:** What command installs Falco on a Linux node?
**Back:** The commands `apt update -y`, `apt install -y linux-headers-$(uname -r)`, and `apt install -y falco` install Falco.
**Tags:** ankidote falco-installation installation-steps linux-commands

---

<!-- note:1772501043947 model:Basic+ -->
**Front:** How do you verify a successful Falco installation?
**Back:** Run `kubectl get pods` to check if Falco pods are running on all nodes.
**Tags:** ankidote falco-installation kubernetes verification

---

<!-- note:1772501043949 model:Basic+ -->
**Front:** Why is installing Falco as a service on the node important?
**Back:** It isolates Falco from the Kubernetes environment, ensuring it remains functional even if the cluster is compromised.
**Tags:** ankidote falco-service installation-steps security-isolation

---

<!-- note:1772501043954 model:Basic+ -->
**Front:** What are the alerting options for Falco?
**Back:** Falco can alert via syslog, standard output, Slack, email, and other channels.
**Tags:** alerting ankidote falco-features security-notifications

---

<!-- note:1772501043958 model:Basic+ -->
**Front:** What is the role of system call libraries in Falco?
**Back:** System call libraries filter captured system calls before they are processed by Falco's policy engine.
**Tags:** ankidote falco-architecture policy-engine system-calls

---

<!-- note:1772501043962 model:Basic+ -->
**Front:** Which method is preferred for Falco deployment in Kubernetes?
**Back:** The eBPF method is preferred for its lower impact on system integrity.
**Tags:** ankidote deployment ebpf kubernetes

---

<!-- note:1772501043966 model:Basic+ -->
**Front:** What is the purpose of the Falco DaemonSet deployment?
**Back:** The DaemonSet ensures Falco runs on all cluster nodes without requiring direct node installation.
**Tags:** ankidote daemonset deployment kubernetes

---

<!-- note:1772501069302 model:Basic+ -->
**Front:** What is mutable infrastructure?
**Back:** Mutable infrastructure involves updating existing servers or resources in-place, such as upgrading software versions on the same servers without replacing the underlying infrastructure.
**Tags:** ankidote mutable-infrastructure system-design

---

<!-- note:1772501069306 model:Basic+ -->
**Front:** What is immutable infrastructure?
**Back:** Immutable infrastructure provisions new servers with updated configurations while decommissioning old ones. Once deployed, servers are never modified; changes require replacing the entire instance.
**Tags:** ankidote immutable-infrastructure system-design

---

<!-- note:1772501069308 model:Basic+ -->
**Front:** What is configuration drift?
**Back:** Configuration drift occurs when servers in a pool run different software versions due to failed updates, leading to inconsistent states and complicating future maintenance.
**Tags:** ankidote configuration-drift mutable-infrastructure

---

<!-- note:1772501069311 model:Basic+ -->
**Front:** How does immutable infrastructure prevent configuration drift?
**Back:** Immutable infrastructure ensures all servers start from a standardized, unchanged configuration. New servers are provisioned with updated software, eliminating version inconsistencies.
**Tags:** ankidote configuration-drift immutable-infrastructure

---

<!-- note:1772501069313 model:Basic+ -->
**Front:** What is the Dockerfile modification for Nginx version upgrade?
**Back:** Update the base image in the Dockerfile: `FROM nginx:1.19` to deploy the new version, then use rolling updates to transition without downtime.
**Tags:** ankidote dockerfile immutable-infrastructure

---

<!-- note:1772501069314 model:Basic+ -->
**Front:** Why should runtime modifications to containers be avoided?
**Back:** Runtime modifications increase security risks by allowing unauthorized access or malicious changes. Containers should be treated as immutable once deployed.
**Tags:** ankidote containers security-risks

---

<!-- note:1772501069316 model:Basic+ -->
**Front:** What tools are used for mutable infrastructure updates?
**Back:** Mutable infrastructure updates use ad-hoc scripts and configuration management tools like Ansible for in-place software upgrades.
**Tags:** ankidote ansible mutable-infrastructure

---

<!-- note:1772501069317 model:Basic+ -->
**Front:** What are the benefits of immutable infrastructure?
**Back:** Immutable infrastructure improves consistency, security, and scalability by ensuring all instances are identical and reducing configuration drift.
**Tags:** ankidote immutable-infrastructure security

---

<!-- note:1772501106254 model:Basic+ -->
**Front:** What is the purpose of behavioral analytics on syscalls in Kubernetes clusters?
**Back:** To detect abnormal behavior and potential security breaches by analyzing system call patterns, enabling early threat detection and mitigation.
**Tags:** ankidote behavioral-analytics kubernetes-security syscall-monitoring

---

<!-- note:1772501106258 model:Basic+ -->
**Front:** Why is real-time monitoring critical for Kubernetes security?
**Back:** To quickly identify and contain breaches, reducing the blast radius and preventing further damage from compromised nodes or pods.
**Tags:** ankidote incident-response kubernetes-security real-time-monitoring

---

<!-- note:1772501106261 model:Basic+ -->
**Front:** What is Falco used for in Kubernetes security?
**Back:** To monitor system calls from containers, detect suspicious activities (e.g., unauthorized file access), and send alerts through multiple channels.
**Tags:** ankidote falco kubernetes-security syscall-monitoring

---

<!-- note:1772501106263 model:Basic+ -->
**Front:** What is an example of anomalous behavior that triggers alerts?
**Back:** Deleting parts of audit logs, as this deviates from normal administrative patterns and indicates potential intrusion attempts.
**Tags:** ankidote anomaly-detection kubernetes-security log-forensics

---

<!-- note:1772501106267 model:Basic+ -->
**Front:** What is the significance of monitoring /etc/shadow file access?
**Back:** Accessing /etc/shadow (which contains sensitive password data) is highly suspicious and may indicate an attacker attempting to exfiltrate credentials.
**Tags:** ankidote file-access kubernetes-security syscall-analysis

---

<!-- note:1772501106269 model:Basic+ -->
**Front:** What tool is recommended for analyzing syscalls in Kubernetes?
**Back:** Falco, which provides real-time monitoring of container syscalls and integrates with Kubernetes for security threat detection.
**Tags:** ankidote falco kubernetes-security syscall-analysis

---

<!-- note:1772501106272 model:Basic+ -->
**Front:** What is the role of behavioral analytics in mitigating cyber threats?
**Back:** To identify irregular patterns in system call behavior, enabling proactive containment of breaches and patching vulnerabilities before exploitation.
**Tags:** ankidote behavioral-analytics kubernetes-security threat-mitigation

---

<!-- note:1772501106276 model:Basic+ -->
**Front:** What is the impact of deleting audit logs in a Kubernetes cluster?
**Back:** It is flagged as anomalous behavior, serving as an early warning sign of potential intrusion attempts to erase forensic evidence.
**Tags:** ankidote anomaly-detection kubernetes-security log-forensics

---

<!-- note:1772501106279 model:Basic+ -->
**Front:** What is the analogy used to explain real-time monitoring benefits?
**Back:** Credit card security: Instant notifications and transaction limits help detect fraud quickly, similar to real-time syscall monitoring in Kubernetes.
**Tags:** ankidote incident-response real-time-monitoring security-analogy

---

<!-- note:1772501106283 model:Basic+ -->
**Front:** What is the primary challenge of monitoring syscalls in Kubernetes?
**Back:** The sheer volume of syscalls generated by hundreds of applications across pods makes simple monitoring insufficient without advanced analysis tools.
**Tags:** ankidote behavioral-analytics kubernetes-challenges syscall-monitoring

---

<!-- note:1772501135255 model:Basic+ -->
**Front:** What is the purpose of Kubernetes audit logs?
**Back:** Kubernetes audit logs provide visibility into system events, enabling monitoring of access and improving security oversight by tracking cluster activities and user actions.
**Tags:** ankidote kubernetes-audit-logs monitoring

---

<!-- note:1772501135259 model:Basic+ -->
**Front:** What is defense-in-depth strategy in security?
**Back:** Defense-in-depth is a layered security approach covering physical infrastructure, applications, networks, data, users, and workloads to detect and mitigate threats at multiple levels.
**Tags:** ankidote defense-in-depth security-strategies

---

<!-- note:1772501135261 model:Basic+ -->
**Front:** What role does Falco play in security?
**Back:** Falco helps implement defense-in-depth by monitoring system calls and file activities at the host and container levels to detect malicious behavior in real-time.
**Tags:** ankidote falco runtime-security

---

<!-- note:1772501135262 model:Basic+ -->
**Front:** What is the goal of ensuring container immutability during runtime?
**Back:** Ensuring container immutability reduces the risk of unauthorized modifications by preventing runtime changes to container images or configurations.
**Tags:** ankidote container-security runtime-security

---

<!-- note:1772501135263 model:Basic+ -->
**Front:** What are the core objectives of the Kubernetes security course?
**Back:** The course objectives include understanding attack surfaces, cluster hardening, vulnerability minimization, supply chain security, monitoring, threat detection, and mock exams.
**Tags:** ankidote course-objectives kubernetes-security

---

<!-- note:1772501135269 model:Basic+ -->
**Front:** How do integrated security layers enhance threat detection?
**Back:** Integrated security layers—from host-level system call monitoring to container runtime security—enable rapid identification and neutralization of threats across all infrastructure components.
**Tags:** ankidote security-layers threat-detection

---

<!-- note:1772501184154 model:Basic+ -->
**Front:** What are audit logs in Kubernetes used for?
**Back:** Audit logs in Kubernetes track cluster operations by recording events such as object creation/modification, requester identity, namespace, and request origin. They help monitor and detect abnormal or suspicious activities.
**Tags:** ankidote cluster-monitoring kubernetes-audit-logs

---

<!-- note:1772501184158 model:Basic+ -->
**Front:** What key details do Kubernetes audit events include?
**Back:** Audit events include details like the objects created/modified, requester identity, namespace involved, and the entry point of the request (e.g., API endpoint or command line).
**Tags:** ankidote event-details kubernetes-audit-logs

---

<!-- note:1772501184160 model:Basic+ -->
**Front:** What are the stages of a Kubernetes request lifecycle?
**Back:** The stages are: 1. Request Received (when the request reaches kube-apiserver), 2. Request Recorded (event generated regardless of validity), 3. Response Started (if authentication/authorization succeeds), 4. Response Complete (after processing), and 5. Panic Stage (for errors/invalid requests).
**Tags:** ankidote audit-stages kubernetes-request-lifecycle

---

<!-- note:1772501184163 model:Basic+ -->
**Front:** What is the purpose of the `omitStages` section in an audit policy?
**Back:** The `omitStages` section specifies which stages of the request lifecycle should not generate audit events. For example, omitting 'RequestReceived' excludes events from that stage.
**Tags:** ankidote audit-policy-configuration omitstages

---

<!-- note:1772501184167 model:Basic+ -->
**Front:** What does the `level` field in an audit policy determine?
**Back:** The `level` field defines the detail level of audit logs: 'None' (no logging), 'Metadata' (logs timestamps and operation details), or 'RequestResponse' (logs full request and response bodies).
**Tags:** ankidote audit-policy-configuration log-levels

---

<!-- note:1772501184170 model:Basic+ -->
**Front:** What flags are required to enable audit logging in kube-apiserver?
**Back:** Required flags include: `--audit-log-path` (log file path), `--audit-policy-file` (policy file path), `--audit-log-maxage`, `--audit-log-maxbackup`, and `--audit-log-maxsize` for log retention settings.
**Tags:** ankidote audit-logging kube-apiserver-configuration

---

<!-- note:1772501184173 model:Basic+ -->
**Front:** What are the two supported audit backends in Kubernetes 1.20+?
**Back:** The two supported audit backends are: 1. Log Backend (writes logs to a file), and 2. Webhook Backend (sends logs to a remote service like Falco).
**Tags:** ankidote audit-backends kubernetes-logging

---

<!-- note:1772501184177 model:Basic+ -->
**Front:** What is the purpose of the `namespaces` field in an audit policy rule?
**Back:** The `namespaces` field specifies which namespaces the audit rule applies to. Omitting it applies the rule to all namespaces.
**Tags:** ankidote audit-policy-configuration namespace-filtering

---

<!-- note:1772501184180 model:Basic+ -->
**Front:** What command deletes a pod in the production namespace for testing?
**Back:** Use `kubectl delete pod webapp-pod -n prod-namespace` to trigger the audit event for the specified pod.
**Tags:** ankidote audit-testing kubernetes-commands

---

<!-- note:1772501184183 model:Basic+ -->
**Front:** What does a sample audit log entry include?
**Back:** A sample audit log entry includes metadata like the audit ID, stage (e.g., 'ResponseComplete'), request URI, verb (e.g., 'delete'), user details, source IP, and resource reference (e.g., pod name and namespace).
**Tags:** ankidote audit-log-format event-example

---

<!-- note:1772501184186 model:Basic+ -->
**Front:** What is the structure of an audit policy file?
**Back:** An audit policy file uses `audit.k8s.io/v1` API version and includes `omitStages` (optional) and `rules` sections. Rules define logging levels, namespaces, verbs, and resources to monitor.
**Tags:** ankidote audit-policy-configuration file-structure

---

<!-- note:1772501219454 model:Basic+ -->
**Front:** How do you verify Falco is running on a host?
**Back:** Use `systemctl status falco` to check Falco's status and ensure it's active.
**Tags:** ankidote falco-verification kubernetes-security

---

<!-- note:1772501219457 model:Basic+ -->
**Front:** What command deploys an NGINX pod for Falco monitoring?
**Back:** Run `kubectl run nginx --image=nginx` to create the NGINX pod.
**Tags:** ankidote falco-testing kubernetes-pods

---

<!-- note:1772501219459 model:Basic+ -->
**Front:** How do you stream Falco logs in real time?
**Back:** Use `journalctl -fu falco` to monitor Falco logs and detect security events.
**Tags:** ankidote falco-logs security-monitoring

---

<!-- note:1772501219461 model:Basic+ -->
**Front:** What command accesses the NGINX container's shell?
**Back:** Execute `kubectl exec -ti nginx -- bash` to enter the NGINX container's shell.
**Tags:** ankidote container-access falco-alerts

---

<!-- note:1772501219464 model:Basic+ -->
**Front:** What command triggers a Falco alert for sensitive file access?
**Back:** Running `cat /etc/shadow` inside the container generates an alert for sensitive file access.
**Tags:** ankidote falco-detection security-rules

---

<!-- note:1772501219469 model:Basic+ -->
**Front:** What are the five mandatory keys in a Falco rule?
**Back:** rule, desc, condition, output, and priority are the five required keys in a Falco rule.
**Tags:** ankidote falco-rules yaml-structure

---

<!-- note:1772501219472 model:Basic+ -->
**Front:** What does the `container` macro in Falco rules do?
**Back:** The `container` macro ensures the event originates from a container by checking `container.id != host`.
**Tags:** ankidote falco-macros rule-conditions

---

<!-- note:1772501219475 model:Basic+ -->
**Front:** What is the purpose of the `linux_shells` list in Falco rules?
**Back:** The `linux_shells` list consolidates common shell names (bash, zsh, etc.) to simplify condition matching.
**Tags:** ankidote falco-lists rule-conditions

---

<!-- note:1772501219478 model:Basic+ -->
**Front:** What priority level indicates a high-severity alert in Falco?
**Back:** Priority levels range from debug (lowest) to emergency (highest). WARNING is a mid-level severity.
**Tags:** ankidote falco-priority security-levels

---

<!-- note:1772501219482 model:Basic+ -->
**Front:** What is the output format of a Falco rule example?
**Back:** Example output: `Bash Opened (user=%user.name container=%container.id)` with dynamic filters.
**Tags:** ankidote falco-output rule-examples

---
