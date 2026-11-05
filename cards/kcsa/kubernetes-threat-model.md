# KCSA - Kubernetes and Cloud Native Security Associate — Kubernetes Threat Model

> Deck: `KCSA - Kubernetes and Cloud Native Security Associate` · Group: `Kubernetes Threat Model` · Notes: 22 · Models: Many

<!-- note:1772101854887 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** What does the term 'container breakout' refer to in the context of container security?
**Options:** A. When a container fails to start properly<br>B. A container exceeding its allocated resource limits<br>C. An attack where an attacker escapes container isolation to gain access to the host system<br>D. Scaling a container beyond its maximum configured replicas<br>E. Migrating a container to a different node in the cluster
**Answer:** C (3) – An attack where an attacker escapes container isolation to gain access to the host system
**Explanation:** A container breakout occurs when an attacker exploits vulnerabilities to escape the isolation boundaries of a container and gain unauthorized access to the underlying host system. This compromises the host's security and can lead to privilege escalation. Other options describe container lifecycle or resource management issues, which are unrelated to security breaches involving isolation escape.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/pod-security-standards/" target="_blank">Kubernetes Official Documentation - Security Context</a><br><a href="https://github.com/cncf/sig-security/blob/main/security-whitepaper/container_security.md" target="_blank">CNCF Security Whitepaper - Container Security</a>

---

<!-- note:1772101854895 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** In the STRIDE threat model, which category best describes a Trojan horse that compromises a build server?
**Options:** A. Spoofing<br>B. Repudiation<br>C. Information Disclosure<br>D. Denial of Service<br>E. Tampering
**Answer:** E (5) – Tampering
**Explanation:** A Trojan horse compromising a build server is an example of tampering because it involves unauthorized modification of system components or data. Tampering refers to malicious alterations that can affect the integrity of software or systems. Spoofing involves impersonation, repudiation relates to denial of actions, information disclosure concerns unauthorized data exposure, and denial of service targets availability, none of which precisely describe this scenario.
**Sources:** <a href="https://docs.microsoft.com/en-us/azure/security/develop/threat-modeling-tool" target="_blank">Microsoft STRIDE Threat Model</a><br><a href="https://owasp.org/www-community/Threat_Modeling" target="_blank">OWASP Threat Modeling</a>

---

<!-- note:1772101854899 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** Which of the following actions in Kubernetes cross trust boundaries and potentially introduce security risks? (Select all that apply)
**Options:** A. Accessing the Kubernetes API server<br>B. Communicating between pods within the same namespace<br>C. Mounting hostPath volumes into pods<br>D. Using service accounts across different namespaces<br>E. Pulling container images from public registries
**Answer:** C, D, E – hostPath mounts, cross-namespace service accounts, and public image registries cross trust boundaries
**Explanation:** Mounting hostPath volumes allows pods to access the host filesystem, crossing the boundary between container and host, which poses significant security risks. Using service accounts across namespaces can bypass namespace isolation, potentially escalating privileges. Pulling images from public registries introduces risks from untrusted or malicious images. Accessing the Kubernetes API is a controlled and authenticated action, while pod-to-pod communication within the same namespace is generally within the same trust boundary and less risky.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/overview/" target="_blank">Kubernetes Official Documentation - Security Best Practices</a><br><a href="https://github.com/cncf/sig-security/blob/main/security-whitepaper/cloud_native_security_whitepaper.pdf" target="_blank">CNCF Cloud Native Security Whitepaper</a>

---

<!-- note:1772101854919 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** Which combination of pod configurations can allow a compromised Kubernetes pod to access and potentially modify the host system? (Select all that apply)
**Options:** A. Running the pod in privileged mode<br>B. Mounting the host filesystem into the pod<br>C. Using host networking in the pod<br>D. Dropping all Linux capabilities from the pod<br>E. Running the pod as a non-root user
**Answer:** A, B, C – privileged mode, host filesystem mounts, host networking
**Explanation:** Running a pod in privileged mode grants it broad permissions, including the ability to access host resources and perform actions that can compromise the host system. Mounting the host filesystem into the pod exposes sensitive files and allows the pod to read or modify host data, which is a significant security risk. Using host networking gives the pod direct access to the host's network stack, increasing the risk of network-based attacks or eavesdropping. In contrast, dropping all Linux capabilities and running as a non-root user are security best practices that reduce the attack surface and limit the pod's ability to affect the host, making these options incorrect.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes Official Documentation - Security Context</a><br><a href="https://kubernetes.io/docs/concepts/security/pod-security-standards/#privileged" target="_blank">Kubernetes Official Documentation - Privileged Mode</a><br><a href="https://github.com/cncf/sig-security/blob/main/security-whitepaper/privilege_escalation.md" target="_blank">CNCF Security Whitepaper - Privilege Escalation</a>

---

<!-- note:1772101854920 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** When an attacker gains access to a Kubernetes pod, which of the following attack scenarios is typically not persistent after the pod restarts?
**Options:** A. Modifying the container image stored in the registry<br>B. Installing malware inside the pod's ephemeral filesystem<br>C. Exfiltrating data from the pod during its runtime<br>D. Altering data stored in a mounted PersistentVolume<br>E. Changing configurations stored in a ConfigMap
**Answer:** B (2) – Installing malware inside the pod's ephemeral filesystem
**Explanation:** The pod's filesystem is ephemeral, meaning any changes such as malware installation inside the container's filesystem are lost when the pod restarts. Modifications to the container image in the registry, persistent volumes, or ConfigMaps are persistent because they exist outside the pod lifecycle. Data exfiltration is a runtime activity and does not persist but can have lasting impact.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/volumes/" target="_blank">Kubernetes Official Documentation - Volumes</a><br><a href="https://github.com/cncf/sig-security/blob/main/security-whitepaper/container_security.md" target="_blank">CNCF Security Whitepaper - Container Security</a>

---

<!-- note:1772101854940 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** Which of the following practices help prevent container breakout vulnerabilities? (Select all that apply)
**Options:** A. Running containers with root privileges<br>B. Using minimal base images to reduce attack surface<br>C. Applying the principle of least privilege to container permissions<br>D. Disabling security modules like SELinux or AppArmor<br>E. Regularly updating container runtimes and dependencies
**Answer:** B, C, E – minimal base images, least privilege, and updating runtimes/dependencies
**Explanation:** Preventing container breakouts involves minimizing the attack surface and restricting privileges. Using minimal base images reduces unnecessary software that could be exploited. Applying the principle of least privilege limits container capabilities to only what is necessary, reducing risk. Regularly updating container runtimes ensures known vulnerabilities are patched. Conversely, running containers as root increases risk, and disabling security modules like SELinux or AppArmor removes important security layers, increasing breakout potential.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/pod-security-standards/" target="_blank">Kubernetes Official Documentation - Security Best Practices</a><br><a href="https://docs.docker.com/develop/security/security/" target="_blank">Docker Security - Best Practices</a>

---

<!-- note:1772101855084 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** What is a primary security risk associated with running a container in privileged mode?
**Options:** A. Increased memory usage<br>B. Limited network access<br>C. Container gaining unrestricted access to host resources, posing security risks<br>D. Reduced application performance<br>E. Inability to use persistent volumes
**Answer:** C (3) – Container gaining unrestricted access to host resources, posing security risks
**Explanation:** Running a container in privileged mode grants it almost the same access to the host as the root user, including direct access to host devices and kernel capabilities. This significantly increases the risk of container breakout and host compromise. The other options, such as increased memory usage or reduced performance, are not typical consequences of privileged mode, and privileged containers can still use persistent volumes and network access normally.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes Official Documentation - Security Context</a><br><a href="https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities" target="_blank">Docker Documentation - Privileged Containers</a>

---

<!-- note:1772101855108 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** In the STRIDE threat modeling framework, what does the letter 'S' represent?
**Options:** A. Spoofing<br>B. Scanning<br>C. Snooping<br>D. Spamming<br>E. Sniffing
**Answer:** A (1) – Spoofing
**Explanation:** In STRIDE, a widely used threat modeling framework, 'S' stands for Spoofing, which refers to an attacker pretending to be someone or something else to gain unauthorized access. The other options like scanning, snooping, spamming, and sniffing are related to security but are not part of the STRIDE categories.
**Sources:** <a href="https://learn.microsoft.com/en-us/security/engineering/stride-threat-model" target="_blank">Microsoft STRIDE Threat Model</a><br><a href="https://owasp.org/www-community/Threat_Modeling" target="_blank">OWASP Threat Modeling</a>

---

<!-- note:1772101855109 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** Which STRIDE threat category primarily addresses threats related to data integrity?
**Options:** A. Spoofing<br>B. Tampering<br>C. Repudiation<br>D. Information Disclosure<br>E. Denial of Service
**Answer:** B (2) – Tampering
**Explanation:** The 'Tampering' category in STRIDE focuses on threats that compromise data integrity by unauthorized modification of data. Spoofing relates to identity, repudiation to denial of actions, information disclosure to confidentiality breaches, and denial of service to availability issues.
**Sources:** <a href="https://learn.microsoft.com/en-us/security/engineering/stride-threat-model" target="_blank">Microsoft STRIDE Threat Model</a><br><a href="https://owasp.org/www-community/Threat_Modeling" target="_blank">OWASP Threat Modeling</a>

---

<!-- note:1772101855110 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** In the STRIDE threat modeling framework, what does 'Repudiation' refer to?
**Options:** A. Unauthorized access<br>B. Denial of an action or event<br>C. Data leakage<br>D. Service unavailability<br>E. Privilege escalation
**Answer:** B (2) – Denial of an action or event
**Explanation:** 'Repudiation' in STRIDE refers to the ability of an attacker or user to deny having performed an action or event, which can hinder accountability and auditing. It is distinct from unauthorized access (spoofing), data leakage (information disclosure), service unavailability (denial of service), and privilege escalation.
**Sources:** <a href="https://learn.microsoft.com/en-us/security/engineering/stride-threat-model" target="_blank">Microsoft STRIDE Threat Model</a><br><a href="https://owasp.org/www-community/Threat_Modeling" target="_blank">OWASP Threat Modeling</a>

---

<!-- note:1772101855111 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** What is an example of 'Information Disclosure' under the STRIDE threat model?
**Options:** A. A user deletes all records from a database<br>B. A user reads sensitive data in a database without authorization<br>C. A user denies performing a destructive action<br>D. A user overflows a buffer to gain root access<br>E. A user floods a network to make services unavailable
**Answer:** B (2) – A user reads sensitive data in a database without authorization
**Explanation:** Information Disclosure refers to unauthorized access to sensitive data. This can occur when a user reads confidential information without proper authorization. Other options do not fit this category because they involve different types of threats: data deletion (Tampering), denial of actions (Denial of Service), privilege escalation (Elevation of Privileges), and network disruption (Denial of Service).
**Sources:** <a href="https://docs.microsoft.com/en-us/archive/blogs/azuresecurity/threat-modeling-stride" target="_blank">Microsoft STRIDE</a><br><a href="https://owasp.org/www-project-threat-modeling/" target="_blank">OWASP Threat Modeling</a>

---

<!-- note:1772101855112 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** What does 'Elevation of Privileges' mean in the context of STRIDE?
**Options:** A. Gaining access to resources by posing as someone else<br>B. Modifying data in transit<br>C. Gaining unauthorized access rights that one should not have<br>D. Denial of actions performed<br>E. Accessing services during downtime
**Answer:** C (3) – Gaining unauthorized access rights that one should not have
**Explanation:** Elevation of Privileges refers to the unauthorized acquisition of higher access rights than those originally granted. This can lead to increased capabilities to perform actions that were previously restricted. The other options describe different threats: impersonation (Spoofing), data tampering (Tampering), denial of actions (Denial of Service), and accessing services during maintenance (not a specific STRIDE category).
**Sources:** <a href="https://docs.microsoft.com/en-us/archive/blogs/azuresecurity/threat-modeling-stride" target="_blank">Microsoft STRIDE</a><br><a href="https://owasp.org/www-project-top-ten/2017/A5_2017-Broken_Access_Control" target="_blank">OWASP Privilege Escalation</a>

---

<!-- note:1772101855113 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** What is a common mitigation strategy for 'Spoofing' threats?
**Options:** A. Implementing proper authentication mechanisms<br>B. Using encryption for data at rest<br>C. Implementing audit logging<br>D. Applying rate limiting<br>E. Running processes as root
**Answer:** A (1) – Implementing proper authentication mechanisms
**Explanation:** Spoofing threats can be mitigated by implementing robust authentication mechanisms. These mechanisms help verify the identity of users or systems, reducing the risk of impersonation. While encryption (option 2) and audit logging (option 3) are important security practices, they do not directly address spoofing. Rate limiting (option 4) is more relevant to Denial of Service attacks, and running processes as root (option 5) increases security risks.
**Sources:** <a href="https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html" target="_blank">OWASP Authentication Cheat Sheet</a><br><a href="https://docs.microsoft.com/en-us/azure/architecture/guide/identity/authz" target="_blank">Microsoft Authentication and Authorization</a>

---

<!-- note:1772101855114 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** Which STRIDE category is primarily concerned with service availability?
**Options:** A. Spoofing<br>B. Tampering<br>C. Denial of Service<br>D. Information Disclosure<br>E. Elevation of Privileges
**Answer:** C (3) – Denial of Service
**Explanation:** Denial of Service (DoS) is the STRIDE category focused on making services unavailable. This can be achieved through various means, such as overwhelming a system with requests or disrupting network connectivity. The other options involve different types of threats: impersonation (Spoofing), data modification (Tampering), unauthorized data access (Information Disclosure), and unauthorized privilege escalation (Elevation of Privileges).
**Sources:** <a href="https://docs.microsoft.com/en-us/archive/blogs/azuresecurity/threat-modeling-stride" target="_blank">Microsoft STRIDE</a><br><a href="https://cheatsheetseries.owasp.org/cheatsheets/Denial_of_Service_Cheat_Sheet.html" target="_blank">OWASP Denial of Service Cheat Sheet</a>

---

<!-- note:1772101855115 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** What is 'Threat Modeling' in the context of security?
**Options:** A. A systematic process to identify and mitigate security risks<br>B. A method to design software architectures<br>C. A technique to improve application performance<br>D. A strategy for marketing products<br>E. An approach to project management
**Answer:** A (1) – A systematic process to identify and mitigate security risks
**Explanation:** Threat Modeling is a structured approach to identifying and mitigating potential security threats. It involves analyzing systems to uncover vulnerabilities and developing strategies to address them. This process is crucial for ensuring the security and integrity of systems. The other options describe unrelated activities: software design, performance optimization, marketing, and project management.
**Sources:** <a href="https://docs.microsoft.com/en-us/archive/blogs/azuresecurity/threat-modeling-stride" target="_blank">Microsoft Threat Modeling</a><br><a href="https://owasp.org/www-project-threat-modeling/" target="_blank">OWASP Threat Modeling</a>

---

<!-- note:1772101855116 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** In the STRIDE threat model, which category best describes an attacker exploiting a buffer overflow to gain root access?
**Options:** A. Spoofing<br>B. Tampering<br>C. Repudiation<br>D. Information Disclosure<br>E. Elevation of Privileges
**Answer:** E (5) – Elevation of Privileges
**Explanation:** Exploiting a buffer overflow to gain root access is classified as an Elevation of Privileges threat because it involves escalating an attacker's privileges to access sensitive resources. This is a critical threat as it can lead to full system compromise.
**Sources:** <a href="https://docs.microsoft.com/en-us/archive/blogs/secdev/stride-a-threat-modeling-tool" target="_blank">Microsoft STRIDE</a><br><a href="https://owasp.org/www-community/Threat_Modeling" target="_blank">OWASP Threat Modeling</a>

---

<!-- note:1772101855117 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** Which of the following options is NOT a category in the STRIDE threat model?
**Options:** A. Spoofing<br>B. Tampering<br>C. Replication<br>D. Information Disclosure<br>E. Denial of Service
**Answer:** C (3) – Replication
**Explanation:** Replication is not one of the categories in the STRIDE threat model. The STRIDE model includes Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privileges.
**Sources:** <a href="https://docs.microsoft.com/en-us/archive/blogs/secdev/stride-a-threat-modeling-tool" target="_blank">Microsoft STRIDE</a><br><a href="https://owasp.org/www-community/Threat_Modeling" target="_blank">OWASP Threat Modeling</a>

---

<!-- note:1772101855118 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** What is an effective mitigation technique for 'Information Disclosure' threats in a Kubernetes environment?
**Options:** A. Implementing audit logging<br>B. Encrypting data at rest and in transit<br>C. Using rate limiting<br>D. Implementing CAPTCHA<br>E. Using prepared SQL statements
**Answer:** B (2) – Encrypting data at rest and in transit
**Explanation:** Encrypting data at rest and in transit is crucial for protecting against Information Disclosure threats. This ensures that even if unauthorized access occurs, the data remains confidential and unreadable.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/security-best-practices/" target="_blank">Kubernetes Security Best Practices</a><br><a href="https://www.nist.gov/cyberframework" target="_blank">NIST Cybersecurity Framework</a>

---

<!-- note:1772101855119 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** What is a common mitigation strategy for 'Tampering' threats in Kubernetes?
**Options:** A. Implementing strong authentication<br>B. Using digital signatures and checksums<br>C. Applying redundant servers<br>D. Implementing multi-factor authentication<br>E. Enforcing password complexity
**Answer:** B (2) – Using digital signatures and checksums
**Explanation:** Using digital signatures and checksums is an effective way to mitigate Tampering threats. These mechanisms ensure data integrity by verifying that data has not been altered during transmission or storage.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/security-best-practices/" target="_blank">Kubernetes Security Best Practices</a><br><a href="https://owasp.org/www-project-secure-coding-practices/" target="_blank">OWASP Secure Coding Practices</a>

---

<!-- note:1772101855121 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** Why is it crucial to restrict access to etcd in a Kubernetes cluster?
**Options:** A. Because etcd stores logs that can be tampered with<br>B. Because etcd contains all cluster data, including secrets, and access can lead to cluster compromise<br>C. Because etcd runs the application code<br>D. Because etcd controls network policies<br>E. Because etcd is not important and can be ignored
**Answer:** B (2) – Because etcd contains all cluster data, including secrets, and access can lead to cluster compromise
**Explanation:** Restricting access to etcd is vital because it stores sensitive data, including cluster secrets. Unauthorized access to etcd can compromise the entire Kubernetes cluster.
**Sources:** <a href="https://kubernetes.io/docs/tasks/administer-cluster/securing-etcd/" target="_blank">Kubernetes etcd Security</a><br><a href="https://etcd.io/docs/" target="_blank">etcd Documentation</a>

---

<!-- note:1772101855122 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** Which Kubernetes component serves as the entry point for the control plane and exposes the Kubernetes API?
**Options:** A. kubelet<br>B. kube-scheduler<br>C. kube-apiserver<br>D. kube-proxy<br>E. etcd
**Answer:** C (3) – kube-apiserver
**Explanation:** The kube-apiserver acts as the front end of the control plane, handling incoming API requests and serving as the primary interface for Kubernetes cluster management. It is responsible for authenticating and authorizing all requests to the API server, ensuring secure access to cluster resources. For more information, refer to the official Kubernetes documentation on components and architecture[1][3].
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/components/" target="_blank">Kubernetes Documentation</a><br><a href="https://kubernetes.io/docs/concepts/architecture/" target="_blank">Kubernetes Architecture</a>

---

<!-- note:1772101855123 model:Many -->
**Domain:** Kubernetes Threat Model
**Question:** What is the recommended approach to secure the Kubernetes Dashboard?
**Options:** A. Expose it publicly without authentication<br>B. Use Role-Based Access Control (RBAC) and restrict access<br>C. Grant it cluster-admin privileges<br>D. Disable it entirely<br>E. Run it as a privileged container
**Answer:** B (2) – Use Role-Based Access Control (RBAC) and restrict access
**Explanation:** Securing the Kubernetes Dashboard with Role-Based Access Control (RBAC) is crucial to limit exposure and ensure that only authorized users can access and manage cluster resources. This approach helps prevent unauthorized access and reduces the attack surface by enforcing strict access controls. For guidance on securing the Dashboard, refer to Kubernetes security best practices and RBAC documentation[1][3].
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes RBAC Documentation</a><br><a href="https://kubernetes.io/docs/concepts/security/security-best-practices/" target="_blank">Kubernetes Security Best Practices</a>

---
