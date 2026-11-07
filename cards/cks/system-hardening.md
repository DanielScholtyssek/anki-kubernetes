# CKS - Certified Kubernetes Security Specialist — System Hardening

> Deck: `CKS - Certified Kubernetes Security Specialist` · Group: `System Hardening` · Notes: 218 · Models: Basic+

<!-- note:1772498476463 model:Basic+ -->
**Front:** What is the primary risk of an unsecured Docker daemon?
**Back:** An attacker could delete containers/volumes, run malicious containers, or gain root access on the host system.
**Tags:** ankidote daemon-risks docker-security

---

<!-- note:1772498476466 model:Basic+ -->
**Front:** What are three consequences of an unsecured Docker daemon?
**Back:** 1. Service disruptions from container deletion
2. Data loss from volume erasure
3. Host system compromise via privileged containers
**Tags:** ankidote daemon-risks docker-security

---

<!-- note:1772498476468 model:Basic+ -->
**Front:** What is the default Docker daemon access restriction?
**Back:** Bound to a Unix socket, limiting access to local users only.
**Tags:** ankidote daemon-configuration docker-security

---

<!-- note:1772498476470 model:Basic+ -->
**Front:** What configuration change exposes Docker daemon externally?
**Back:** Modify /etc/docker/daemon.json to include TCP hosts with IP:PORT.
**Tags:** ankidote docker-security external-access

---

<!-- note:1772498476472 model:Basic+ -->
**Front:** What is required for secure external Docker daemon access?
**Back:** TLS encryption with certificate-based authentication and restricted network interfaces.
**Tags:** ankidote docker-security tls-encryption

---

<!-- note:1772498476473 model:Basic+ -->
**Front:** What TLS configuration parameters are needed in daemon.json?
**Back:** hosts, tls, tlscert, tlskey, tlsverify, tlscacert for certificate validation.
**Tags:** ankidote docker-security tls-configuration

---

<!-- note:1772498476476 model:Basic+ -->
**Front:** What is the purpose of tlsverify in Docker configuration?
**Back:** Enforces client certificate authentication to verify connecting clients.
**Tags:** ankidote docker-security tls-authentication

---

<!-- note:1772498476478 model:Basic+ -->
**Front:** How should client certificates be managed for Docker TLS?
**Back:** Generate CA-signed certificates and distribute only to trusted users with their CA certificate.
**Tags:** ankidote client-certs docker-security

---

<!-- note:1772498476479 model:Basic+ -->
**Front:** What environment variables configure Docker TLS client?
**Back:** DOCKER_TLS_VERIFY, DOCKER_HOST, and certificate paths for tls cert/key/cacert.
**Tags:** ankidote client-configuration docker-security

---

<!-- note:1772498476481 model:Basic+ -->
**Front:** What are the key security practices for Docker daemon?
**Back:** 1. Use Unix socket by default
2. Bind to private interfaces when exposing TCP
3. Enable TLS with certificate verification
4. Restrict access to trusted users
**Tags:** ankidote best-practices docker-security

---

<!-- note:1772498525715 model:Basic+ -->
**Front:** How do you check the status of the Docker service using systemd?
**Back:** Use the command `systemctl status docker` to check the Docker service status. The output shows if the service is active, loaded, and running.
**Tags:** ankidote docker service-management systemd

---

<!-- note:1772498525718 model:Basic+ -->
**Front:** What commands are used to start and stop the Docker service?
**Back:** Use `systemctl start docker` to start the Docker service and `systemctl stop docker` to stop it. These commands manage the systemd service.
**Tags:** ankidote docker service-control systemd

---

<!-- note:1772498525720 model:Basic+ -->
**Front:** How do you run the Docker daemon in the foreground with debug mode?
**Back:** Run the Docker daemon in the foreground with debug mode using the command `dockerd --debug`. This outputs detailed logs to the console.
**Tags:** ankidote daemon docker foreground

---

<!-- note:1772498525722 model:Basic+ -->
**Front:** Where does the Docker daemon listen for local communication via Unix socket?
**Back:** The Docker daemon listens on the Unix socket at `/var/run/docker.sock` for local process communication, including Docker CLI interactions.
**Tags:** ankidote docker ipc unix-socket

---

<!-- note:1772498525727 model:Basic+ -->
**Front:** How do you configure Docker to listen on a TCP interface for remote access?
**Back:** Start the Docker daemon with `dockerd --host=tcp://<ip>:<port>` to enable TCP listening. Set `DOCKER_HOST` environment variable to connect remotely.</port></ip>
**Tags:** ankidote docker remote-access tcp

---

<!-- note:1772498525729 model:Basic+ -->
**Front:** What command starts the Docker daemon with TLS encryption?
**Back:** Use `dockerd --tls=true --tlscert=/path/to/cert --tlskey=/path/to/key --host=tcp://<IP>:2376` to start the Docker daemon with TLS encryption on port 2376.
**Tags:** ankidote docker secure-communication tls

---

<!-- note:1772498525731 model:Basic+ -->
**Front:** Where is the Docker daemon configuration file located?
**Back:** The Docker daemon configuration file is located at `/etc/docker/daemon.json` and is used to set options like TLS, hosts, and debug settings.
**Tags:** ankidote configuration daemon-json docker

---

<!-- note:1772498525732 model:Basic+ -->
**Front:** What happens if a parameter is specified both in `daemon.json` and command-line flags?
**Back:** Docker reports a conflict and fails to start if the same parameter is defined in both `daemon.json` and command-line flags. For example, conflicting `debug` settings cause an error.
**Tags:** ankidote configuration daemon-json docker

---

<!-- note:1772498525735 model:Basic+ -->
**Front:** What is the security risk of exposing Docker API over TCP without TLS?
**Back:** Exposing the Docker API over TCP without encryption or authentication allows unauthorized users to run containers on the host, posing a significant security risk.
**Tags:** ankidote docker security tcp

---

<!-- note:1772499333564 model:Basic+ -->
**Front:** What is the significance of Kubernetes in modern cloud computing?
**Back:** Kubernetes is hailed as the 'Linux of the future' and powers cutting-edge AI technologies like ChatGPT and OpenAI. It manages containers across distributed systems, making it critical for cloud-native applications.
**Tags:** ankidote cloud-computing kubernetes-significance

---

<!-- note:1772499333566 model:Basic+ -->
**Front:** What is the Certified Kubernetes Security Specialist (CKS) exam about?
**Back:** The CKS exam prepares candidates to secure Kubernetes clusters through hands-on labs and real-world scenarios, focusing on security practices for dynamic cloud environments.
**Tags:** ankidote cks-exam kubernetes-security

---

<!-- note:1772499333569 model:Basic+ -->
**Front:** What are the prerequisites for the CKS exam?
**Back:** Candidates must hold the Certified Kubernetes Administrator (CKA) certification. Those without it should complete foundational courses like Kubernetes for Beginners or Docker Training.
**Tags:** ankidote cka-certification cks-prerequisites

---

<!-- note:1772499333571 model:Basic+ -->
**Front:** What are the four C's of cloud-native security?
**Back:** The four C's are Cloud, Clusters, Containers, and Code, which define the attack surface for Kubernetes environments and guide security strategies.
**Tags:** ankidote attack-surface cloud-native-security

---

<!-- note:1772499333573 model:Basic+ -->
**Front:** What is the purpose of CIS Benchmarks in Kubernetes security?
**Back:** CIS Benchmarks provide standardized security configurations to harden Kubernetes clusters, ensuring compliance with industry best practices.
**Tags:** ankidote cis-benchmarks cluster-hardening

---

<!-- note:1772499333575 model:Basic+ -->
**Front:** What are key strategies for securing Kubernetes clusters?
**Back:** Key strategies include implementing CIS Benchmarks, configuring authentication/authorization, managing Service Accounts, using TLS certificates, securing the dashboard, enforcing network policies, and conducting secure upgrades.
**Tags:** ankidote cluster-security kubernetes-hardening

---

<!-- note:1772499333577 model:Basic+ -->
**Front:** What tools are used for securing the host system in Kubernetes?
**Back:** Tools include firewalls, Seccomp for system call restrictions, AppArmor for protection, SSH hardening, and restricting kernel modules/open ports.
**Tags:** ankidote host-security system-hardening

---

<!-- note:1772499333580 model:Basic+ -->
**Front:** What are Pod Security Standards in Kubernetes?
**Back:** Pod Security Standards enforce security policies for pods, such as restricting privileged containers, ensuring non-root users, and controlling volume permissions.
**Tags:** ankidote microservices pod-security

---

<!-- note:1772499333582 model:Basic+ -->
**Front:** What is the role of Open Policy Agent (OPA) in Kubernetes security?
**Back:** OPA is a policy engine that enforces security policies across Kubernetes clusters, managing access control and validating configurations for compliance.
**Tags:** ankidote open-policy-agent policy-engines

---

<!-- note:1772499333585 model:Basic+ -->
**Front:** What are best practices for securing the software supply chain?
**Back:** Best practices include minimizing base image sizes, scanning container images for vulnerabilities, and validating/signing deployments to prevent supply chain attacks.
**Tags:** ankidote container-scanning supply-chain-security

---

<!-- note:1772499333587 model:Basic+ -->
**Front:** What tools are used for runtime security in Kubernetes?
**Back:** Tools like Falco provide behavioral analytics and threat detection, enabling defense-in-depth strategies through monitoring and activity logging.
**Tags:** ankidote runtime-security threat-detection

---

<!-- note:1772499333588 model:Basic+ -->
**Front:** What is the purpose of hands-on labs in the CKS course?
**Back:** Hands-on labs provide real-world scenarios to reinforce learning, simulating the CKS exam environment and improving practical skills through interactive exercises.
**Tags:** ankidote exam-preparation hands-on-labs

---

<!-- note:1772499333590 model:Basic+ -->
**Front:** How should candidates approach the CKS exam documentation?
**Back:** Candidates should practice navigating Kubernetes documentation efficiently to quickly locate critical information during the exam, as referencing is permitted.
**Tags:** ankidote documentation-use exam-strategies

---

<!-- note:1772501760057 model:Basic+ -->
**Front:** What is AppArmor's role in Kubernetes security?
**Back:** AppArmor enforces security policies at the kernel level by limiting file system writes and other risky operations within containers.
**Tags:** ankidote apparmor kubernetes-security

---

<!-- note:1772501760061 model:Basic+ -->
**Front:** When was AppArmor support introduced in Kubernetes?
**Back:** AppArmor support was introduced in Kubernetes v1.4 and remained in beta until version 1.20.
**Tags:** ankidote apparmor kubernetes-versions

---

<!-- note:1772501760064 model:Basic+ -->
**Front:** What are the requirements to enable AppArmor on Kubernetes pods?
**Back:** 1. AppArmor kernel module must be enabled. 2. Desired profile must be loaded on each node. 3. Container runtime (e.g., Docker, CRI-O) must support AppArmor.
**Tags:** ankidote apparmor kubernetes-requirements

---

<!-- note:1772501760068 model:Basic+ -->
**Front:** What does the apparmor-deny-write profile do?
**Back:** It denies all file write operations by using the rule: deny /** w
**Tags:** ankidote apparmor-profiles security-policies

---

<!-- note:1772501760072 model:Basic+ -->
**Front:** How to verify AppArmor profile is loaded on nodes?
**Back:** Run `aa-status` to check if the profile is in enforce mode and loaded.
**Tags:** ankidote apparmor node-verification

---

<!-- note:1772501760075 model:Basic+ -->
**Front:** What is the legacy method to apply AppArmor profiles?
**Back:** Annotate the pod metadata with `container.apparmor.security.beta.kubernetes.io/<container-name>: localhost/<profile-name>`
**Tags:** ankidote apparmor legacy-configuration

---

<!-- note:1772501760078 model:Basic+ -->
**Front:** How to apply AppArmor profiles in newer Kubernetes versions?
**Back:** Use `securityContext.appArmorProfile` in the pod spec with `type: Localhost` and `localhostProfile`.
**Tags:** ankidote apparmor modern-configuration

---

<!-- note:1772501760079 model:Basic+ -->
**Front:** How to test AppArmor's deny write policy?
**Back:** Attempt to create a file inside the container using `kubectl exec`; it should fail with 'Permission denied'.
**Tags:** ankidote apparmor testing

---

<!-- note:1772501760081 model:Basic+ -->
**Front:** What command creates the Ubuntu Sleeper pod?
**Back:** Run `kubectl create -f ubuntu-sleeper.yaml` to deploy the pod.
**Tags:** ankidote apparmor pod-creation

---

<!-- note:1772501760083 model:Basic+ -->
**Front:** How to verify pod logs for the Sleeper container?
**Back:** Use `kubectl logs ubuntu-sleeper` to check if the message 'Sleeping for an hour!' is printed.
**Tags:** ankidote apparmor debugging

---

<!-- note:1772501760085 model:Basic+ -->
**Front:** What is the Kubernetes documentation URL for security?
**Back:** https://kubernetes.io/docs/concepts/security/overview/
**Tags:** ankidote kubernetes-docs security-best-practices

---

<!-- note:1772501794829 model:Basic+ -->
**Front:** What is AppArmor?
**Back:** AppArmor is a Linux security module that limits application access to system resources, enhancing container security beyond Seccomp profiles by controlling file/directory permissions, network settings, and Linux capabilities.
**Tags:** ankidote apparmor-definition container-security

---

<!-- note:1772501794832 model:Basic+ -->
**Front:** How does AppArmor differ from Seccomp?
**Back:** Seccomp restricts syscalls but does not manage filesystem access, while AppArmor provides resource-level security by controlling file/directory permissions, network access, and Linux capabilities.
**Tags:** ankidote apparmor-vs-seccomp security-comparison

---

<!-- note:1772501794835 model:Basic+ -->
**Front:** How to check if AppArmor is active?
**Back:** Run 'systemctl status apparmor' to check the service status and verify the kernel module with 'cat /sys/module/apparmor/parameters/enabled' which should return 'Y'.
**Tags:** ankidote apparmor-verification system-checks

---

<!-- note:1772501794839 model:Basic+ -->
**Front:** How to list all loaded AppArmor profiles?
**Back:** Use 'cat /sys/kernel/security/apparmor/profiles' to view loaded profiles, which may show entries like 'docker-default (enforce)'.
**Tags:** ankidote apparmor-profiles system-commands

---

<!-- note:1772501794843 model:Basic+ -->
**Front:** What does the AppArmor profile for denying write access look like?
**Back:** The profile:
```
profile apparmor-deny-write flags=(attach_disconnected) {
    file,
    deny /** w,
}
```
**Tags:** ankidote apparmor-profiles file-permissions

---

<!-- note:1772501794846 model:Basic+ -->
**Front:** What are the three modes of AppArmor profiles?
**Back:** 1. Enforce mode: Strictly enforces rules
2. Complain mode: Logs violations without blocking
3. Unconfined mode: No restrictions applied
**Tags:** ankidote apparmor-modes security-modes

---

<!-- note:1772501794849 model:Basic+ -->
**Front:** What command shows AppArmor's current state?
**Back:** The 'aa-status' command displays loaded profiles, their modes (enforce/complain), and processes constrained by profiles.
**Tags:** ankidote apparmor-tools debugging

---

<!-- note:1772501794852 model:Basic+ -->
**Front:** Is AppArmor installed by default on most Linux distributions?
**Back:** Yes, AppArmor is installed and enabled by default on most Linux distributions.
**Tags:** ankidote apparmor-defaults linux-security

---

<!-- note:1772501856531 model:Basic+ -->
**Front:** What is Tracee and its primary use case?
**Back:** Tracee is an open-source tool from Aqua Security that uses eBPF to trace system calls in containers at runtime. It monitors OS behavior and detects suspicious activity with minimal overhead.
**Tags:** ankidote ebpf-tracing tracee-overview

---

<!-- note:1772501856534 model:Basic+ -->
**Front:** What directories must be bind-mounted when running Tracee as a Docker container?
**Back:** The required bind mounts are /tmp/tracee (for storing compiled eBPF programs), /lib/modules (kernel headers), and /usr/src (kernel source code). All are mounted read-only.
**Tags:** ankidote bind-mounts docker-setup

---

<!-- note:1772501856537 model:Basic+ -->
**Front:** What Docker flags are required to run Tracee with elevated privileges?
**Back:** The --privileged flag is required for extended privileges to trace syscalls. Additionally, --pid=host is needed to access host process information.
**Tags:** ankidote docker-setup privileged-flag

---

<!-- note:1772501856540 model:Basic+ -->
**Front:** What command traces system calls for a specific command like 'ls'?
**Back:** Use docker run --rm --privileged --pid=host -v /lib/modules:/lib/modules:ro -v /usr/src:/usr/src:ro -v /tmp/tracee:/tmp/tracee aquasec/tracee:0.4.0 --trace comm=ls
**Tags:** ankidote command-tracing syscall-tracing

---

<!-- note:1772501856543 model:Basic+ -->
**Front:** What command traces system calls for all new processes on the host?
**Back:** sudo docker run --rm --privileged --pid=host -v /lib/modules:/lib/modules:ro -v /usr/src:/usr/src:ro -v /tmp/tracee:/tmp/tracee aquasec/tracee:0.4.0 --trace pid=new
**Tags:** ankidote process-monitoring syscall-tracing

---

<!-- note:1772501856546 model:Basic+ -->
**Front:** How to trace system calls for new containers with Tracee?
**Back:** Run docker run --rm --privileged --pid=host -v /lib/modules:/lib/modules:ro -v /usr/src:/usr/src:ro -v /tmp/tracee:/tmp/tracee aquasec/tracee:0.4.0 --trace container=new
**Tags:** ankidote container-monitoring syscall-tracing

---

<!-- note:1772501856549 model:Basic+ -->
**Front:** What are the environments Tracee can monitor?
**Back:** Tracee can monitor system calls for a single command, all new processes on the host, and new containers.
**Tags:** ankidote syscall-tracing tracee-environments

---

<!-- note:1772501856553 model:Basic+ -->
**Front:** Why are kernel headers required for Tracee?
**Back:** Tracee needs kernel headers to compile eBPF programs. These are typically located in /lib/modules and /usr/src on Ubuntu systems.
**Tags:** ankidote docker-setup kernel-headers

---

<!-- note:1772501856556 model:Basic+ -->
**Front:** How to persist Tracee's compiled eBPF programs between runs?
**Back:** Bind mount the /tmp/tracee directory from the host to the container to persist compiled programs across runs.
**Tags:** ankidote bind-mounts docker-setup

---

<!-- note:1772501894539 model:Basic+ -->
**Front:** What does the add_data.sh script do?
**Back:** Creates directories under /opt and writes a log file with the current date.
**Tags:** ankidote apparmor-profiles bash-script

---

<!-- note:1772501894543 model:Basic+ -->
**Front:** What command generates an AppArmor profile for a script?
**Back:** aa-genprof /path/to/script.sh (requires apparmor-utils installation)
**Tags:** ankidote apparmor-profiles profile-generation

---

<!-- note:1772501894547 model:Basic+ -->
**Front:** What is the first step after running the add_data.sh script during profiling?
**Back:** Return to the aa-genprof prompt and press 's' to scan system logs for events.
**Tags:** ankidote apparmor-profiling profile-creation

---

<!-- note:1772501894550 model:Basic+ -->
**Front:** How do you allow the mkdir command in the profile?
**Back:** Select 'i' (inherit) when prompted for /usr/bin/mkdir execution.
**Tags:** ankidote apparmor-profiling permission-settings

---

<!-- note:1772501894553 model:Basic+ -->
**Front:** How do you deny access to /proc/filesystems in the profile?
**Back:** Choose 'd' (deny) when prompted for read access to this file.
**Tags:** access-control ankidote apparmor-profiles

---

<!-- note:1772501894556 model:Basic+ -->
**Front:** How to verify an AppArmor profile is in enforce mode?
**Back:** Run aa-status and check if the profile appears in enforce mode.
**Tags:** ankidote apparmor-verification profile-check

---

<!-- note:1772501894559 model:Basic+ -->
**Front:** What happens when the script tries to write to /opt instead of /opt/app/data?
**Back:** AppArmor denies write access to /opt, producing a 'Permission denied' error.
**Tags:** ankidote apparmor-enforcement profile-testing

---

<!-- note:1772501894562 model:Basic+ -->
**Front:** How to disable an existing AppArmor profile?
**Back:** Use aa-disable <profile> and create a symlink to /etc/apparmor.d/disable/
**Tags:** ankidote apparmor-configuration profile-management

---

<!-- note:1772501931484 model:Basic+ -->
**Front:** What are open ports and why are they important for system security?
**Back:** Open ports are endpoints in a computer's operating system that allow network traffic. Managing them is crucial to minimize security vulnerabilities by disabling unused ports.
**Tags:** ankidote linux-security network-ports

---

<!-- note:1772501931488 model:Basic+ -->
**Front:** What command checks active listening ports on a Linux system?
**Back:** Use `netstat -an | grep -w LISTEN` to display all ports actively listening for connections.
**Tags:** ankidote linux-commands network-ports

---

<!-- note:1772501931492 model:Basic+ -->
**Front:** Which file maps service names to port numbers on Ubuntu-based systems?
**Back:** The `/etc/services` file catalogs service names, protocols, and associated port numbers.
**Tags:** ankidote linux-files network-ports

---

<!-- note:1772501931495 model:Basic+ -->
**Front:** How do you disable unnecessary open ports for security?
**Back:** Block unused ports using firewall tools like `iptables` or `ufw` to restrict access to only required services.
**Tags:** ankidote firewall-config linux-security

---

<!-- note:1772501931497 model:Basic+ -->
**Front:** Which port is conventionally reserved for DNS traffic?
**Back:** Port 53 is reserved for DNS services, handling both TCP and UDP traffic.
**Tags:** ankidote dns network-ports

---

<!-- note:1772501931499 model:Basic+ -->
**Front:** Why should you review software documentation before installing new applications?
**Back:** To identify required open ports and ensure only necessary services are exposed, preventing security risks.
**Tags:** ankidote network-ports software-installation

---

<!-- note:1772501997134 model:Basic+ -->
**Front:** What is the default Seccomp behavior in Docker?
**Back:** Docker uses a built-in Seccomp profile to block approximately 60 syscalls by default.
**Tags:** ankidote default-profile docker seccomp

---

<!-- note:1772501997147 model:Basic+ -->
**Front:** How many syscalls are blocked by Docker's default Seccomp profile?
**Back:** Docker's default Seccomp profile blocks 64 syscalls.
**Tags:** ankidote docker seccomp syscalls

---

<!-- note:1772501997158 model:Basic+ -->
**Front:** What is the default Seccomp state in Kubernetes pods?
**Back:** Kubernetes pods do not enable Seccomp by default; it is disabled.
**Tags:** ankidote default-state kubernetes seccomp

---

<!-- note:1772501997163 model:Basic+ -->
**Front:** How can Seccomp be enabled in a Kubernetes pod?
**Back:** Specify a Seccomp profile in the pod's manifest using the `seccompProfile` field.
**Tags:** ankidote enable kubernetes seccomp

---

<!-- note:1772501997171 model:Basic+ -->
**Front:** What are the available Seccomp profile types in Kubernetes?
**Back:** Available types are `RuntimeDefault`, `Unconfined`, and `Localhost` for custom profiles.
**Tags:** ankidote kubernetes profile-types seccomp

---

<!-- note:1772501997177 model:Basic+ -->
**Front:** What command inspects Docker's Seccomp configuration?
**Back:** Run `docker run r.j3ss.co/amicontained amicontained` to inspect Docker's Seccomp settings.
**Tags:** ankidote docker inspection seccomp

---

<!-- note:1772501997184 model:Basic+ -->
**Front:** What is the purpose of the `allowPrivilegeEscalation` field?
**Back:** It restricts the container process from gaining additional privileges beyond what is needed.
**Tags:** ankidote capabilities kubernetes security

---

<!-- note:1772501997189 model:Basic+ -->
**Front:** What happens when a pod uses the `Unconfined` Seccomp profile?
**Back:** The pod runs without any Seccomp restrictions, matching the default Kubernetes behavior.
**Tags:** ankidote kubernetes seccomp unconfined

---

<!-- note:1772501997197 model:Basic+ -->
**Front:** How to create a custom Seccomp profile in Kubernetes?
**Back:** Use the `Localhost` profile type and specify the path to a custom JSON profile file via `localhostProfile`.
**Tags:** ankidote custom-profile kubernetes seccomp

---

<!-- note:1772501997204 model:Basic+ -->
**Front:** What is the effect of setting `defaultAction`: `SCMP_ACT_LOG` in a custom profile?
**Back:** All syscalls are logged to the node’s syslog (e.g., `/var/log/syslog`), enabling audit tracking.
**Tags:** ankidote custom-profile logging seccomp

---

<!-- note:1772501997210 model:Basic+ -->
**Front:** What is the consequence of using a strict Seccomp profile that denies all syscalls?
**Back:** The pod status becomes `ContainerCannotRun` because essential syscalls are blocked.
**Tags:** ankidote pod-status seccomp strict-policy

---

<!-- note:1772501997216 model:Basic+ -->
**Front:** How to apply a custom Seccomp profile to a pod?
**Back:** Reference the profile in the pod's spec using `seccompProfile.type: Localhost` and `localhostProfile: <path>`.
**Tags:** ankidote apply-profile kubernetes seccomp

---

<!-- note:1772501997221 model:Basic+ -->
**Front:** What tool can be used to analyze container syscalls?
**Back:** Tools like [Tracee](https://github.com/aquasecurity/tracee) can monitor and analyze container syscalls in real-time.
**Tags:** analysis ankidote seccomp tracee

---

<!-- note:1772501997226 model:Basic+ -->
**Front:** What is the default action when no Seccomp profile is specified in Kubernetes?
**Back:** Seccomp is disabled by default, and only 21 syscalls are blocked.
**Tags:** ankidote default kubernetes seccomp

---

<!-- note:1772501997230 model:Basic+ -->
**Front:** What is the purpose of the `seccompProfile` field in a pod manifest?
**Back:** It specifies the Seccomp profile to enforce for the pod, controlling syscall filtering.
**Tags:** ankidote kubernetes pod-spec seccomp

---

<!-- note:1772501997234 model:Basic+ -->
**Front:** How to verify Seccomp is active in a pod?
**Back:** Check the pod logs for `Seccomp: filtering` and the list of blocked syscalls.
**Tags:** ankidote kubernetes seccomp verification

---

<!-- note:1772502041338 model:Basic+ -->
**Front:** What is the Least Privilege Principle?
**Back:** A security concept that minimizes risk by granting roles only the access necessary for their tasks, reducing potential attack surfaces and improving system security.
**Tags:** ankidote least-privilege security-principles

---

<!-- note:1772502041341 model:Basic+ -->
**Front:** How does the airport analogy illustrate the Least Privilege Principle?
**Back:** It shows travelers and staff having access only to areas and resources required for their specific roles, such as restricted zones being off-limits unless necessary for the task.
**Tags:** analogies ankidote least-privilege

---

<!-- note:1772502041347 model:Basic+ -->
**Front:** List the roles in the airport analogy and their access levels.
**Back:** Traveler: Public spaces and designated boarding gates. Baggage Counter Employees: Check-in processes. Security Officers: Security screening areas. Store Employees: Public areas with backroom access. Boarding Gate Staff: Boarding assistance. Cleaning Staff: Terminal areas. Cargo Loaders/Maintenance: Loading bays. Pilots/Stewards: Aircraft-specific restricted zones.
**Tags:** ankidote least-privilege roles

---

<!-- note:1772502041354 model:Basic+ -->
**Front:** What is Role-Based Access Control (RBAC) in Kubernetes?
**Back:** A method to define precise access rights for users and services within a Kubernetes cluster, ensuring they have only the permissions needed for their tasks.
**Tags:** ankidote kubernetes-security rbac

---

<!-- note:1772502041358 model:Basic+ -->
**Front:** What security measures are recommended for Kubernetes clusters?
**Back:** Limit node access, implement RBAC, remove obsolete packages, restrict network access, limit kernel modules, and secure open ports to reduce attack surfaces.
**Tags:** ankidote kubernetes-security security-measures

---

<!-- note:1772502041367 model:Basic+ -->
**Front:** What are the system component considerations for least privilege?
**Back:** Install only required software, disable unnecessary services, avoid loading unused kernel modules, and secure all open ports to prevent unauthorized access.
**Tags:** ankidote least-privilege system-security

---

<!-- note:1772502041372 model:Basic+ -->
**Front:** What does applying the least privilege principle mean?
**Back:** Granting every role only the access they need to perform their tasks, which reduces risks and enhances overall security by limiting potential damage from unauthorized actions.
**Tags:** ankidote least-privilege security-best-practices

---

<!-- note:1772502086963 model:Basic+ -->
**Front:** What strategies secure Kubernetes nodes by limiting direct host access?
**Back:** Shield nodes from direct internet exposure using private networks, VPNs, or authorized network ranges in firewalls. Control plane nodes are typically inaccessible in managed solutions.
**Tags:** ankidote kubernetes-security node-hardening

---

<!-- note:1772502086968 model:Basic+ -->
**Front:** What is the recommended approach for securing private Kubernetes clusters?
**Back:** Use a VPN for secure access or configure infrastructure firewalls to allow access only from specific IP ranges (e.g., 44.44.44.0/24).
**Tags:** ankidote kubernetes-architecture network-security

---

<!-- note:1772502086970 model:Basic+ -->
**Front:** What are the four types of Linux user accounts?
**Back:** 1. User Accounts (developers/admins), 2. Superuser (root), 3. System Accounts (service daemons), 4. Service Accounts (specific services like nginx).
**Tags:** ankidote linux-accounts user-management

---

<!-- note:1772502086972 model:Basic+ -->
**Front:** What does the `id` command display in Linux?
**Back:** UID, GID, and group membership for the current user. Example: `id michael` shows user ID, group ID, and groups.
**Tags:** ankidote linux-commands user-identification

---

<!-- note:1772502086976 model:Basic+ -->
**Front:** Which file stores hashed passwords in Linux?
**Back:** The `/etc/shadow` file contains hashed passwords and password policy information.
**Tags:** access-control ankidote linux-security

---

<!-- note:1772502086977 model:Basic+ -->
**Front:** How to disable a user account by preventing login?
**Back:** Use `usermod -s /bin/nologin <username>` to change their shell to a no-login shell. Verify with `grep <username> /etc/passwd`.
**Tags:** ankidote security-best-practices user-management

---

<!-- note:1772502086979 model:Basic+ -->
**Front:** What command removes a user from a specific group?
**Back:** Use `deluser <username> <groupname>` (e.g., `deluser michael admin`) to remove a user from a group.
**Tags:** ankidote group-management linux-commands

---

<!-- note:1772502086981 model:Basic+ -->
**Front:** What is the purpose of `/etc/passwd`?
**Back:** Stores basic user information (username, UID, GID, home directory, shell) but not passwords. Example: `grep michael /etc/passwd`.
**Tags:** access-control ankidote linux-files

---

<!-- note:1772502086984 model:Basic+ -->
**Front:** What is the principle of least privilege in system security?
**Back:** Only grant users the minimum permissions necessary to perform their tasks. Remove or disable unnecessary accounts and privileges.
**Tags:** access-control ankidote security-principles

---

<!-- note:1772502086986 model:Basic+ -->
**Front:** How to audit user access on a Linux system?
**Back:** Combine `id`, `who`, `last`, and inspect `/etc/passwd`, `/etc/shadow`, and `/etc/group` to track accounts and login history.
**Tags:** ankidote linux-security system-audit

---

<!-- note:1772502120389 model:Basic+ -->
**Front:** Why can a Kubernetes pod running as root still be restricted from changing the system date?
**Back:** Linux capabilities isolate privileges into granular units. Even as root, containers lack specific capabilities like CAP_SYS_TIME required for system clock modifications.
**Tags:** ankidote kubernetes-security linux-capabilities

---

<!-- note:1772502120393 model:Basic+ -->
**Front:** What is the purpose of Linux capabilities?
**Back:** Capabilities allow fine-grained control over process privileges by breaking traditional root privileges into individual capabilities that can be granted or revoked.
**Tags:** ankidote linux-capabilities process-privileges

---

<!-- note:1772502120398 model:Basic+ -->
**Front:** What happens when a Docker container tries to set the system date by default?
**Back:** The operation fails with 'Operation not permitted' because containers start with a limited capability set that doesn't include CAP_SYS_TIME by default.
**Tags:** ankidote capabilities docker

---

<!-- note:1772502120401 model:Basic+ -->
**Front:** What command shows capabilities required by a binary?
**Back:** The getcap command displays capabilities needed by a binary, e.g., /usr/bin/ping = cap_net_raw+ep
**Tags:** ankidote capabilities command-line

---

<!-- note:1772502120406 model:Basic+ -->
**Front:** How do you check capabilities of a running process?
**Back:** Use getpcaps with the process ID (PID), e.g., getpcaps 779 for the SSH daemon process.
**Tags:** ankidote capabilities processes

---

<!-- note:1772502120409 model:Basic+ -->
**Front:** What is the default capability set for Linux processes?
**Back:** Default capabilities include CAP_CHOWN, CAP_DAC_OVERRIDE, CAP_NET_RAW, and others, but exclude capabilities like CAP_SYS_TIME by default.
**Tags:** ankidote default-settings linux-capabilities

---

<!-- note:1772502120413 model:Basic+ -->
**Front:** How to add a capability to a Kubernetes container?
**Back:** Specify the capability in the container's securityContext.capabilities.add array, e.g., adding CAP_SYS_TIME to allow date modifications.
**Tags:** ankidote capabilities kubernetes

---

<!-- note:1772502120416 model:Basic+ -->
**Front:** What security risk exists with modifying container capabilities?
**Back:** Granting unnecessary capabilities exposes the host to privilege escalation risks. Always follow the principle of least privilege.
**Tags:** ankidote capabilities security

---

<!-- note:1772502120418 model:Basic+ -->
**Front:** What capability allows changing file ownership?
**Back:** CAP_CHOWN enables processes to change file ownership and permissions.
**Tags:** ankidote capabilities file-operations

---

<!-- note:1772502120423 model:Basic+ -->
**Front:** What capability is required to modify the system clock?
**Back:** The CAP_SYS_TIME capability is needed to set or adjust the system clock.
**Tags:** ankidote capabilities system-time

---

<!-- note:1772502165960 model:Basic+ -->
**Front:** What is the role of system calls (syscalls) in Linux?
**Back:** Syscalls enable user-space applications to request services from the kernel, facilitating interaction between user programs and kernel-space resources like hardware and memory.
**Tags:** ankidote linux-syscalls user-kernel-communication

---

<!-- note:1772502165964 model:Basic+ -->
**Front:** What is the difference between user space and kernel space in Linux?
**Back:** User space runs applications (e.g., C/Python programs) and has restricted access to hardware. Kernel space contains the kernel code, drivers, and manages hardware directly with full privileges.
**Tags:** ankidote kernel-space linux-architecture user-space

---

<!-- note:1772502165968 model:Basic+ -->
**Front:** What is the purpose of the `execve` syscall?
**Back:** The `execve` syscall loads and executes a new program, passing arguments and environment variables (e.g., `touch /tmp/error.log` with 23 inherited environment variables).
**Tags:** ankidote execve linux-syscalls

---

<!-- note:1772502165972 model:Basic+ -->
**Front:** List four common Linux syscalls.
**Back:** Common syscalls include `open`, `close`, `read`, and `write` for file operations, and `execve` for program execution.
**Tags:** ankidote common-syscalls linux-syscalls

---

<!-- note:1772502165975 model:Basic+ -->
**Front:** How does `strace` trace system calls?
**Back:** The `strace` command traces syscalls made by a process, showing details like `execve` arguments, environment variables, and return values (e.g., `strace touch /tmp/error.log`)
**Tags:** ankidote strace syscall-tracing

---

<!-- note:1772502165979 model:Basic+ -->
**Front:** What does the `strace -c` flag do?
**Back:** The `-c` flag generates a summary report of syscall usage, showing percentages, time, and counts for each syscall (e.g., `read`, `close`, `fstat`)
**Tags:** ankidote strace syscall-summary

---

<!-- note:1772502165982 model:Basic+ -->
**Front:** How to trace a running process with `strace`?
**Back:** Use `strace -p <PID>` to attach to a running process (e.g., `strace -p 3596` for PID 3596), which shows syscalls like `futex` and `mprotect` in real-time.
**Tags:** ankidote process-tracing strace

---

<!-- note:1772502165985 model:Basic+ -->
**Front:** What does the `env | wc -l` command verify?
**Back:** It counts the number of environment variables inherited by a process, confirming the 23 variables mentioned in the `execve` syscall output.
**Tags:** ankidote environment-variables syscall-parameters

---

<!-- note:1772502165989 model:Basic+ -->
**Front:** What is the significance of the `openat` syscall in the `touch` example?
**Back:** The `openat` syscall opens a file path relative to a directory file descriptor, part of the sequence to create `/tmp/error.log` via `touch`.
**Tags:** ankidote linux-syscalls openat

---

<!-- note:1772502165991 model:Basic+ -->
**Front:** How do simple commands like `touch` impact system calls?
**Back:** Simple commands like `touch` invoke multiple syscalls (e.g., `openat`, `utimensat`, `mmap`), while complex applications can generate thousands per second.
**Tags:** ankidote performance-analysis syscall-usage

---

<!-- note:1772502192935 model:Basic+ -->
**Front:** What is the principle of least privilege in IAM?
**Back:** The principle of least privilege ensures users and services have only the necessary permissions to perform their tasks, minimizing unauthorized access risks.
**Tags:** ankidote iam-concepts least-privilege

---

<!-- note:1772502192938 model:Basic+ -->
**Front:** Why should root accounts be avoided for daily tasks?
**Back:** Root accounts have full administrative privileges. Using them for daily operations increases security risks; instead, use IAM users with limited permissions.
**Tags:** ankidote iam-users root-account

---

<!-- note:1772502192940 model:Basic+ -->
**Front:** What is the benefit of grouping IAM users into groups?
**Back:** IAM groups allow attaching policies to multiple users simultaneously, simplifying permission management and ensuring consistent access controls.
**Tags:** ankidote iam-groups permission-management

---

<!-- note:1772502192941 model:Basic+ -->
**Front:** How should EC2 instances access S3 buckets securely?
**Back:** Create an IAM role (e.g., 'S3 Access Role') with required permissions and attach it to the EC2 instance. Avoid direct access using programmatic keys.
**Tags:** ankidote iam-roles resource-access

---

<!-- note:1772502192943 model:Basic+ -->
**Front:** What is the security risk of using programmatic keys directly?
**Back:** Programmatic keys can be misused if compromised. IAM roles provide a more secure way to grant temporary, least-privilege access to AWS resources.
**Tags:** ankidote iam-security programmatic-keys

---

<!-- note:1772502192946 model:Basic+ -->
**Front:** Which AWS tools help audit IAM permissions?
**Back:** AWS Trusted Advisor, Security Command Center (Google Cloud), and Azure Advisor provide real-time security checks and recommendations for IAM policies.
**Tags:** ankidote iam-auditing security-tools

---

<!-- note:1772502192949 model:Basic+ -->
**Front:** What should be done with unused IAM permissions?
**Back:** Unused IAM permissions should be periodically reviewed and removed to maintain compliance with the principle of least privilege.
**Tags:** ankidote iam-best-practices permission-review

---

<!-- note:1772502192952 model:Basic+ -->
**Front:** What is the purpose of attaching policies to IAM groups?
**Back:** Attaching policies to IAM groups grants the same set of permissions to all members of the group, streamlining management and ensuring consistent access controls.
**Tags:** ankidote iam-groups policy-attachment

---

<!-- note:1772502231214 model:Basic+ -->
**Front:** How can you verify if a port is actively listening for incoming connections?
**Back:** Use the `netstat -an | grep -w LISTEN` command to list all listening ports. For specific services, check `/etc/services` or use `systemctl status <service>`.
**Tags:** ankidote firewall network-security port-binding

---

<!-- note:1772502231218 model:Basic+ -->
**Front:** What does binding a port to 0.0.0.0 indicate?
**Back:** It means the service is accessible from any network interface, allowing external connections unless restricted by firewalls or configuration.
**Tags:** ankidote firewall network-security port-binding

---

<!-- note:1772502231221 model:Basic+ -->
**Front:** What is the principle of least privilege in network security?
**Back:** Limit access to only necessary ports and services to reduce the attack surface and minimize potential vulnerabilities.
**Tags:** ankidote firewall network-security security-best-practices

---

<!-- note:1772502231224 model:Basic+ -->
**Front:** What are the two primary approaches to enforcing network security?
**Back:** 1. Network-wide security using external firewalls (e.g., Cisco ASA, Fortinet). 2. Server-level security with host-based firewalls (e.g., UFW, iptables).
**Tags:** ankidote firewall network-security security-approaches

---

<!-- note:1772502231226 model:Basic+ -->
**Front:** What command shows the SSH service's port binding information?
**Back:** Use `cat /etc/services | grep ssh` to see the SSH service definition, which includes port 22 and protocol (TCP).
**Tags:** ankidote firewall network-security port-binding

---

<!-- note:1772502231228 model:Basic+ -->
**Front:** What is UFW and its purpose?
**Back:** UFW (Uncomplicated Firewall) is a simplified command-line tool for configuring firewall rules on Linux systems, making it easier to manage incoming/outgoing traffic.
**Tags:** ankidote firewall linux network-security

---

<!-- note:1772502231231 model:Basic+ -->
**Front:** Which command displays all active listening ports on a Linux system?
**Back:** Run `netstat -an | grep -w LISTEN` to list all TCP/UDP ports in a listening state.
**Tags:** ankidote firewall network-security port-binding

---

<!-- note:1772502231233 model:Basic+ -->
**Front:** What is the role of host-based firewalls in server security?
**Back:** Host-based firewalls (e.g., iptables, firewalld, UFW) restrict network access at the server level, controlling traffic based on rules defined per machine.
**Tags:** ankidote firewall network-security server-security

---

<!-- note:1772502253659 model:Basic+ -->
**Front:** What is the primary goal of minimizing the host OS footprint?
**Back:** To reduce potential attack surfaces and vulnerabilities by simplifying system complexity and streamlining configurations.
**Tags:** ankidote attack-surface security-practices

---

<!-- note:1772502253664 model:Basic+ -->
**Front:** Why is maintaining a simple and consistent cluster state critical for security?
**Back:** Because even one misconfigured or unpatched node can expose the entire cluster to significant risks.
**Tags:** ankidote cluster-security system-configuration

---

<!-- note:1772502253667 model:Basic+ -->
**Front:** What is the principle of least privilege, and why is it important?
**Back:** It is a strategy to limit user and service privileges to only what is necessary, reducing system complexity and attack surface while building a secure environment.
**Tags:** ankidote least-privilege security-practices

---

<!-- note:1772502316493 model:Basic+ -->
**Front:** What is the importance of regularly auditing installed software and services?
**Back:** Auditing helps ensure only essential components are maintained, reducing security risks and system complexity by eliminating unnecessary packages.
**Tags:** ankidote security system-maintenance

---

<!-- note:1772502316506 model:Basic+ -->
**Front:** How does systemd manage services?
**Back:** Systemd uses `systemctl` to control services, allowing status checks, starting, stopping, and managing service configurations.
**Tags:** ankidote service-management systemd

---

<!-- note:1772502316509 model:Basic+ -->
**Front:** How to list all installed services using systemd?
**Back:** Run `systemctl list-units --type service` to view all services and their statuses.
**Tags:** ankidote service-listing systemd

---

<!-- note:1772502316512 model:Basic+ -->
**Front:** How to disable and stop an unnecessary service?
**Back:** Use `systemctl stop <service>` to stop it, then `systemctl disable <service>` to prevent automatic startup.
**Tags:** ankidote package-removal service-management

---

<!-- note:1772502316514 model:Basic+ -->
**Front:** How to remove an obsolete package like Apache using apt?
**Back:** Run `apt remove apache2` to remove the package. Use `apt autoremove` to delete unused dependencies.
**Tags:** ankidote apt package-removal

---

<!-- note:1772502316518 model:Basic+ -->
**Front:** What should you check before purging a package?
**Back:** Ensure the package is not required by other services or dependencies to avoid disrupting system functionality.
**Tags:** ankidote dependencies package-removal

---

<!-- note:1772502316521 model:Basic+ -->
**Front:** Why might Apache be considered obsolete on Kubernetes cluster nodes?
**Back:** Apache is not needed on Kubernetes nodes since the cluster handles networking, and it may have been installed inadvertently.
**Tags:** ankidote security system-optimization

---

<!-- note:1772502316523 model:Basic+ -->
**Front:** What packages should be retained in a Kubernetes environment?
**Back:** Retain `kubelet`, `kubeadm`, container runtime, and `kubectl` as they are essential for Kubernetes node operations.
**Tags:** ankidote kubernetes package-selection

---

<!-- note:1772502340365 model:Basic+ -->
**Front:** What command is used to load a Linux kernel module manually?
**Back:** The `modprobe` command is used to load kernel modules manually. Example: `modprobe pcspkr` loads the PC Speaker module.
**Tags:** ankidote kernel-modules module-loading

---

<!-- note:1772502340368 model:Basic+ -->
**Front:** How do you list all currently loaded kernel modules?
**Back:** Use the `lsmod` command to list all active kernel modules and their details.
**Tags:** ankidote kernel-modules module-management

---

<!-- note:1772502340370 model:Basic+ -->
**Front:** What is the purpose of blacklisting kernel modules?
**Back:** Blacklisting prevents specific kernel modules from loading automatically, reducing potential security risks and system vulnerabilities.
**Tags:** ankidote blacklisting kernel-modules security

---

<!-- note:1772502340374 model:Basic+ -->
**Front:** Where should you place configuration files to blacklist kernel modules?
**Back:** Create or edit files in the `/etc/modprobe.d/` directory (e.g., `/etc/modprobe.d/blacklist.conf`)
**Tags:** ankidote blacklisting configuration kernel-modules

---

<!-- note:1772502340378 model:Basic+ -->
**Front:** What is the syntax to blacklist a module in a configuration file?
**Back:** Add the line `blacklist <module-name>` to the configuration file (e.g., `blacklist sctp`)
**Tags:** ankidote blacklisting configuration kernel-modules

---

<!-- note:1772502340381 model:Basic+ -->
**Front:** Why is a system reboot required after updating module blacklist settings?
**Back:** A reboot is required to apply changes to the module blacklist, ensuring the modules are not loaded at boot or runtime.
**Tags:** ankidote blacklisting kernel-modules reboot

---

<!-- note:1772502340384 model:Basic+ -->
**Front:** What command confirms a module is successfully blacklisted?
**Back:** Run `lsmod | grep <module-name>` after rebooting to verify the module is not loaded.
**Tags:** ankidote blacklisting kernel-modules verification

---

<!-- note:1772502340385 model:Basic+ -->
**Front:** Which modules are commonly blacklisted in Kubernetes environments?
**Back:** Modules like `sctp` (Stream Control Transmission Protocol) and `dccp` (Datagram Congestion Control Protocol) are commonly blacklisted in Kubernetes clusters.
**Tags:** ankidote kernel-modules kubernetes security

---

<!-- note:1772502340388 model:Basic+ -->
**Front:** What risk does automatic module loading pose to system security?
**Back:** Automatic module loading can allow unprivileged processes to trigger the loading of network-related modules, potentially exposing the system to exploitation.
**Tags:** ankidote kernel-modules risks security

---

<!-- note:1772502340392 model:Basic+ -->
**Front:** Which CIS Benchmark section provides guidance on kernel module security?
**Back:** Section 3.4 of the [CIS Benchmarks for Kubernetes](https://www.cisecurity.org/benchmark/kubernetes/) provides additional best practices for kernel module security.
**Tags:** ankidote cis-benchmarks kernel-modules security

---

<!-- note:1772502381717 model:Basic+ -->
**Front:** What is Seccomp?
**Back:** Seccomp (Secure Computing) is a kernel-level feature that restricts applications to a subset of allowed syscalls, sandboxing processes to minimize attack surfaces.
**Tags:** ankidote linux-security seccomp-features

---

<!-- note:1772502381720 model:Basic+ -->
**Front:** How to check if Seccomp is supported on a Linux kernel?
**Back:** Run `grep -i seccomp /boot/config-$(uname -r)` and verify `CONFIG_SECCOMP_FILTER=y` and `CONFIG_SECCOMP=y` are set.
**Tags:** ankidote kernel-configuration seccomp-verification

---

<!-- note:1772502381723 model:Basic+ -->
**Front:** Which command shows syscall statistics for a process?
**Back:** Use `strace -c <command>` to trace and summarize syscalls executed by a process.
**Tags:** ankidote syscall-monitoring tracing-tools

---

<!-- note:1772502381725 model:Basic+ -->
**Front:** What is the Dirty COW vulnerability?
**Back:** A 2016 Linux kernel vulnerability (CVE-2016-5195) that exploited the ptrace syscall to write to read-only memory, enabling privilege escalation.
**Tags:** ankidote syscall-exploits vulnerability-examples

---

<!-- note:1772502381727 model:Basic+ -->
**Front:** What is Seccomp Mode 1?
**Back:** Strict mode (Mode 1) allows only four syscalls: read, write, exit, and sigreturn, severely restricting process capabilities.
**Tags:** ankidote process-sandboxing seccomp-modes

---

<!-- note:1772502381731 model:Basic+ -->
**Front:** What is the default action in Docker's Seccomp profile?
**Back:** The default action is `SCMP_ACT_ERRNO`, which denies any syscall not explicitly allowed in the profile.
**Tags:** ankidote docker-security seccomp-profiles

---

<!-- note:1772502381733 model:Basic+ -->
**Front:** What is a whitelist Seccomp profile?
**Back:** A profile that explicitly allows specific syscalls while denying all others by default.
**Tags:** ankidote seccomp-profiles security-practices

---

<!-- note:1772502381735 model:Basic+ -->
**Front:** What happens when a container tries to change the system time with Seccomp enabled?
**Back:** The `date -s` command fails with `Operation not permitted` because the syscall is blocked by the Seccomp profile.
**Tags:** ankidote docker-seccomp syscall-restrictions

---

<!-- note:1772502381739 model:Basic+ -->
**Front:** How to create a custom Seccomp profile in Docker?
**Back:** Define a JSON profile with allowed syscalls and use `--security-opt seccomp=/path/to/profile.json` when running containers.
**Tags:** ankidote custom-seccomp docker-configuration

---

<!-- note:1772502381741 model:Basic+ -->
**Front:** Which Seccomp mode is most restrictive?
**Back:** Mode 1 (Strict) is the most restrictive, allowing only read, write, exit, and sigreturn syscalls.
**Tags:** ankidote seccomp-modes security-levels

---

<!-- note:1772502381743 model:Basic+ -->
**Front:** What is the purpose of the `architectures` field in a Seccomp profile?
**Back:** It specifies which CPU architectures (e.g., x86_64, x86) the profile applies to.
**Tags:** ankidote architecture-support seccomp-configuration

---

<!-- note:1772502381747 model:Basic+ -->
**Front:** Why is a whitelist profile more secure than a blacklist profile?
**Back:** Whitelist profiles deny all syscalls by default and only allow explicitly permitted ones, reducing the risk of missing dangerous syscalls.
**Tags:** ankidote seccomp-profiles security-practices

---

<!-- note:1772502381750 model:Basic+ -->
**Front:** What syscall is blocked by Docker's default Seccomp profile?
**Back:** Syscalls like `settimeofday` (for changing system time) are blocked to prevent time-related attacks.
**Tags:** ankidote blocked-syscalls docker-seccomp

---

<!-- note:1772502381753 model:Basic+ -->
**Front:** What is the result of attempting `mkdir` in a Seccomp-restricted container?
**Back:** The `mkdir` command fails with `Operation not permitted` if the syscall is explicitly denied in the profile.
**Tags:** ankidote container-security syscall-restrictions

---

<!-- note:1772502426415 model:Basic+ -->
**Front:** What is the command to connect to a remote SSH server without specifying a username?
**Back:** ssh node01. If no username is specified, SSH uses your local username. Tags: ssh-basics, command-syntax
**Tags:** ankidote command-syntax ssh-basics

---

<!-- note:1772502426417 model:Basic+ -->
**Front:** What command generates an SSH RSA key pair?
**Back:** ssh-keygen -t rsa. This creates private (id_rsa) and public (id_rsa.pub) keys. Tags: ssh-keygen, key-pair-generation
**Tags:** ankidote key-pair-generation ssh-keygen

---

<!-- note:1772502426419 model:Basic+ -->
**Front:** How do you copy your SSH public key to a remote server?
**Back:** Use ssh-copy-id mark@node01. This appends the public key to ~/.ssh/authorized_keys. Tags: ssh-copy-id, key-installation
**Tags:** ankidote key-installation ssh-copy-id

---

<!-- note:1772502426422 model:Basic+ -->
**Front:** How to disable root login in SSH configuration?
**Back:** Set PermitRootLogin no in /etc/ssh/sshd_config. Tags: ssh-config, root-login
**Tags:** ankidote root-login ssh-config

---

<!-- note:1772502426425 model:Basic+ -->
**Front:** What directive disables password-based authentication in SSH?
**Back:** PasswordAuthentication no in /etc/ssh/sshd_config. Tags: ssh-config, password-auth
**Tags:** ankidote password-auth ssh-config

---

<!-- note:1772502426429 model:Basic+ -->
**Front:** What command restarts the SSH service after configuration changes?
**Back:** systemctl restart sshd. Tags: ssh-restart, service-management
**Tags:** ankidote service-management ssh-restart

---

<!-- note:1772502615393 model:Basic+ -->
**Front:** What is UFW and its primary purpose?
**Back:** UFW (Uncomplicated Firewall) is a user-friendly interface for managing Linux firewall rules on Ubuntu servers. It simplifies configuring IPTables by providing an intuitive front-end for packet filtering.
**Tags:** ankidote firewall-tools ufw-basics

---

<!-- note:1772502615396 model:Basic+ -->
**Front:** What command checks active listening ports on app01?
**Back:** Use `netstat -an | grep -w LISTEN` to inspect active ports. Expected output includes lines for SSH (22), HTTP (80), and blocked port 8080.
**Tags:** ankidote network-monitoring ufw-configuration

---

<!-- note:1772502615398 model:Basic+ -->
**Front:** What is the default status of UFW after installation?
**Back:** UFW is initially inactive. Run `ufw status` to confirm: `Status: inactive`.
**Tags:** ankidote firewall-status ufw-installation

---

<!-- note:1772502615400 model:Basic+ -->
**Front:** What are the default policies for outbound and inbound traffic?
**Back:** Outbound traffic is allowed by default (`ufw default allow outgoing`). Inbound traffic is denied by default (`ufw default deny incoming`).
**Tags:** ankidote firewall-policies ufw-configuration

---

<!-- note:1772502615401 model:Basic+ -->
**Front:** How to allow SSH from 172.16.238.5?
**Back:** Run `ufw allow from 172.16.238.5 to any port 22 proto tcp` to permit SSH connections only from the specified IP.
**Tags:** ankidote firewall-rules ufw-allow

---

<!-- note:1772502615406 model:Basic+ -->
**Front:** How to allow HTTP from 172.16.100.0/28?
**Back:** Execute `ufw allow from 172.16.100.0/28 to any port 80 proto tcp` to permit HTTP access from the specified IP range.
**Tags:** ankidote firewall-rules ip-ranges

---

<!-- note:1772502615408 model:Basic+ -->
**Front:** What command explicitly blocks port 8080?
**Back:** Use `ufw deny 8080` to explicitly deny inbound traffic on port 8080, even though the default policy already blocks it.
**Tags:** ankidote firewall-rules ufw-deny

---

<!-- note:1772502615411 model:Basic+ -->
**Front:** What command enables UFW and confirms the action?
**Back:** Run `ufw enable` and confirm by entering `y` when prompted. The system warns that this may disrupt existing SSH connections.
**Tags:** ankidote firewall-activation ufw-enable

---

<!-- note:1772502615414 model:Basic+ -->
**Front:** How to delete a specific UFW deny rule for port 8080?
**Back:** Use `ufw delete deny 8080` to remove the rule. The system confirms deletion for both IPv4 and IPv6.
**Tags:** ankidote firewall-deletion ufw-commands

---

<!-- note:1772502615418 model:Basic+ -->
**Front:** What command displays the current UFW status with active rules?
**Back:** Run `ufw status` to view the firewall status, showing allowed/denied rules with source IP ranges and port specifications.
**Tags:** ankidote firewall-verification ufw-status

---

<!-- note:1772503595142 model:Basic+ -->
**Front:** What command is used to determine the IP address of a domain?
**Back:** The `ping` command resolves domain names to IP addresses. Example: `ping www.vote.com`
**Tags:** ankidote networking reconnaissance

---

<!-- note:1772503595147 model:Basic+ -->
**Front:** What is the default port for Docker, and why is it a security risk?
**Back:** Port 2375 is the default Docker port. Exposing it without authentication allows attackers to interact with the Docker daemon, enabling container escapes and host access.
**Tags:** ankidote attack-surface docker-security

---

<!-- note:1772503595150 model:Basic+ -->
**Front:** What command lists running containers connected to a Docker host?
**Back:** The command `docker -H <host> ps` lists containers. Example: `docker -H www.vote.com ps`
**Tags:** ankidote container-management docker-commands

---

<!-- note:1772503595154 model:Basic+ -->
**Front:** What vulnerability allows escaping a container into the host?
**Back:** The Dirty COW (Dirty Copy-On-Write) vulnerability enables privilege escalation by exploiting memory corruption issues in the Linux kernel.
**Tags:** ankidote container-escape dirty-cow

---

<!-- note:1772503595158 model:Basic+ -->
**Front:** How do attackers typically discover database credentials in Kubernetes?
**Back:** Attackers inspect environment variables of compromised pods to extract database credentials. Example: Checking `env` in a DB pod.
**Tags:** ankidote database-security environment-variables

---

<!-- note:1772503595161 model:Basic+ -->
**Front:** What command checks disk usage and volume mounts on a Linux host?
**Back:** The `df -h` command displays disk usage and mounted filesystems. Example output includes `/dev/sda1` and `/vagrant` mounts.
**Tags:** ankidote filesystem host-reconnaissance

---

<!-- note:1772503595164 model:Basic+ -->
**Front:** What port is the Kubernetes dashboard exposed on in this scenario?
**Back:** The Kubernetes dashboard is exposed on port 30080 of the node. Example: `sudo iptables -L -t nat | grep kubernetes` confirms this.
**Tags:** ankidote kubernetes-dashboard security-configuration

---

<!-- note:1772503595167 model:Basic+ -->
**Front:** How did the attacker alter vote counts in the database?
**Back:** The attacker used PostgreSQL's `psql` utility to connect to the database and executed SQL commands to update vote records. Example: `UPDATE votes SET candidate = 'cat' WHERE ...`
**Tags:** ankidote database-compromise sql-injection

---

<!-- note:1772503595171 model:Basic+ -->
**Front:** What is the primary security risk of exposing Docker's API?
**Back:** Exposing Docker's API without authentication allows attackers to execute arbitrary commands on the host, leading to container escapes and full system compromise.
**Tags:** ankidote attack-surface docker-vulnerabilities

---

<!-- note:1772507837315 model:Basic+ -->
**Front:** Why is using sudo preferred over direct root access for administrative tasks?
**Back:** Using sudo allows trusted users to execute commands with elevated privileges while providing their own password, creating an audit trail and reducing security risks compared to direct root login.
**Tags:** ankidote privilege-escalation security-practices sudo

---

<!-- note:1772507837318 model:Basic+ -->
**Front:** What error occurs when installing nginx without sudo privileges?
**Back:** The system returns a permission denied error: 'E: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)'
**Tags:** ankidote error-handling package-management sudo

---

<!-- note:1772507837320 model:Basic+ -->
**Front:** What is the primary purpose of the /etc/sudoers file?
**Back:** The /etc/sudoers file defines user/group privileges for executing commands with elevated privileges and controls sudo behavior across the system.
**Tags:** ankidote privilege-escalation security-configuration sudoers-file

---

<!-- note:1772507837323 model:Basic+ -->
**Front:** What is the recommended way to edit the /etc/sudoers file?
**Back:** Always use the 'visudo' command to edit the /etc/sudoers file, as it prevents syntax errors that could lock users out of sudo privileges.
**Tags:** ankidote edit-procedures security-practices sudoers-file

---

<!-- note:1772507837327 model:Basic+ -->
**Front:** What are the four components of a typical /etc/sudoers entry?
**Back:** 1. User/group (e.g., 'mark' or '%sudo'), 2. Host specification (e.g., 'ALL'), 3. Run-as specification (e.g., '(ALL:ALL)'), 4. Command specification (e.g., 'ALL').
**Tags:** ankidote configuration-syntax security-configuration sudoers-file

---

<!-- note:1772507837331 model:Basic+ -->
**Front:** What security benefit does using sudo provide over direct root shell access?
**Back:** Using sudo executes commands in the user's shell environment rather than switching to a root shell, maintaining environment variables and reducing accidental system-wide changes.
**Tags:** ankidote privilege-escalation security-benefits sudo

---

<!-- note:1772507837334 model:Basic+ -->
**Front:** What is the risk of disabling root login via SSH?
**Back:** Disabling root login via SSH prevents direct root access, reducing the attack surface but requiring sudo for administrative tasks, which must be configured securely.
**Tags:** ankidote privilege-escalation security-practices ssh

---

<!-- note:1772507858565 model:Basic+ -->
**Front:** What are key SSH hardening techniques?
**Back:** Disable root user access and configure passwordless SSH using key-based authentication.
**Tags:** ankidote ssh-hardening system-security

---

<!-- note:1772507858569 model:Basic+ -->
**Front:** What mitigation strategies are recommended for privilege escalation in Linux?
**Back:** Implement strict permission controls, use sudo with minimal privileges, and regularly audit user permissions.
**Tags:** ankidote privilege-escalation security-techniques

---

<!-- note:1772507858573 model:Basic+ -->
**Front:** What is a key step in system hardening related to packages?
**Back:** Identify and remove outdated packages and services to minimize potential vulnerabilities.
**Tags:** ankidote package-management system-hardening

---

<!-- note:1772507858576 model:Basic+ -->
**Front:** How should network ports be managed to enhance security?
**Back:** Identify and disable unused open ports in Linux to prevent unauthorized access.
**Tags:** ankidote network-security port-management

---

<!-- note:1772507858578 model:Basic+ -->
**Front:** What is cloud role minimization?
**Back:** Minimize roles and access in cloud environments to maintain secure operations by following the principle of least privilege.
**Tags:** ankidote cloud-security role-minimization

---

<!-- note:1772507858582 model:Basic+ -->
**Front:** What are key aspects of effective firewall configuration?
**Back:** Implement rule-based traffic filtering, disable unused services, and regularly audit firewall settings to ensure proper access control.
**Tags:** ankidote firewall-configuration network-security

---

<!-- note:1772507858586 model:Basic+ -->
**Front:** What is Seccomp used for in system hardening?
**Back:** Restrict system calls to prevent unauthorized operations and limit the attack surface of applications.
**Tags:** ankidote seccomp system-calls

---

<!-- note:1772507858589 model:Basic+ -->
**Front:** Which security tools are mentioned for enhancing system protection?
**Back:** AppArmor is highlighted as a security tool for enhancing system protection through application-level access control.
**Tags:** ankidote apparmor security-tools

---
