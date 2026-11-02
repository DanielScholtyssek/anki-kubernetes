# CKS - Certified Kubernetes Security Specialist — Security Fundamentals

> Deck: `CKS - Certified Kubernetes Security Specialist` · Group: `Security Fundamentals` · Notes: 56 · Models: Basic+

<!-- note:1772497920811 model:Basic+ -->
**Front:** What is the primary purpose of TLS certificates in web communications?
**Back:** To encrypt communication and verify the server's identity, ensuring secure HTTPS connections and preventing data interception.
**Tags:** ankidote secure-communications tls-certificates

---

<!-- note:1772497920821 model:Basic+ -->
**Front:** What is the main difference between symmetric and asymmetric encryption?
**Back:** Symmetric encryption uses a single key for encryption/decryption, while asymmetric encryption uses a public/private key pair.
**Tags:** ankidote asymmetric-encryption encryption-types

---

<!-- note:1772497920825 model:Basic+ -->
**Front:** What command generates SSH key pairs, and what files does it create?
**Back:** The `ssh-keygen` command creates `id_rsa` (private key) and `id_rsa.pub` (public key).
**Tags:** ankidote key-pair-generation ssh-security

---

<!-- note:1772497920828 model:Basic+ -->
**Front:** How do you secure SSH access using key pairs?
**Back:** Place the public key in the server's `~/.ssh/authorized_keys` file and use the private key with `ssh -i id_rsa user@host`.
**Tags:** ankidote key-pair-usage ssh-configuration

---

<!-- note:1772497920831 model:Basic+ -->
**Front:** What are the three main steps in TLS securing web traffic?
**Back:** 1. Server sends public key in a certificate. 2. Browser encrypts symmetric key with public key. 3. Server decrypts symmetric key and uses it for encryption.
**Tags:** ankidote https-encryption tls-process

---

<!-- note:1772497920833 model:Basic+ -->
**Front:** What information is included in a digital certificate?
**Back:** Certificate owner's identity, issuer's identity, validity dates, Subject Alternative Names (SANs), and public key information.
**Tags:** ankidote certificate-details digital-certificates

---

<!-- note:1772497920836 model:Basic+ -->
**Front:** What is the role of Certificate Authorities (CAs) in TLS?
**Back:** CAs validate certificate requests, sign certificates with their private key, and establish trust through preloaded public keys in browsers.
**Tags:** ankidote certificate-authorities trust-model

---

<!-- note:1772497920837 model:Basic+ -->
**Front:** What is the purpose of the Certificate Signing Request (CSR)?
**Back:** The CSR contains the server's public key and domain name, submitted to a CA for certificate issuance.
**Tags:** ankidote certificate-generation csr-process

---

<!-- note:1772497920839 model:Basic+ -->
**Front:** What are the standard file extensions for public keys and private keys?
**Back:** Public keys use `.crt`, `.pem`, or `.pub`; private keys use `.key` or include 'key' in the filename.
**Tags:** ankidote file-conventions key-naming

---

<!-- note:1772497920842 model:Basic+ -->
**Front:** What is Public Key Infrastructure (PKI)?
**Back:** A framework combining CAs, key pairs, digital certificates, and key management practices to enable secure communications and trust verification.
**Tags:** ankidote pki-concept security-framework

---

<!-- note:1772499239663 model:Basic+ -->
**Front:** What are the common file extensions for TLS certificates containing public keys?
**Back:** Certificates with public keys typically use .crt or .pem extensions (e.g., server.crt or client.pem).
**Tags:** ankidote file-naming kubernetes tls-certificates

---

<!-- note:1772499239666 model:Basic+ -->
**Front:** What are the standard file names for server and private key pairs in Kubernetes?
**Back:** Server certificates use names like api-server.crt and etcd-server.crt, with corresponding .key files (e.g., api-server.key).
**Tags:** ankidote kubernetes server-certificates tls-certificates

---

<!-- note:1772499239669 model:Basic+ -->
**Front:** Which components require client certificates for authentication in Kubernetes?
**Back:** Admin users, scheduler, kube-controller-manager, kube-proxy, and etcd servers (when acting as clients) require client certificates.
**Tags:** ankidote client-certificates kubernetes tls-certificates

---

<!-- note:1772499239673 model:Basic+ -->
**Front:** What are the key server components and their associated certificates in Kubernetes?
**Back:** 1. Kube API Server: api-server.crt/api-server.key
2. etcd Server: etcd-server.crt/etcd-server.key
3. Kubelet: kubelet.crt/kubelet.key
**Tags:** ankidote kubernetes server-components tls-certificates

---

<!-- note:1772499239676 model:Basic+ -->
**Front:** What is the role of the Certificate Authority (CA) in Kubernetes TLS?
**Back:** The CA signs both client and server certificates. Kubernetes requires at least one CA per cluster, with certificates named CA.crt and CA.key.
**Tags:** ankidote certificate-authority kubernetes tls-certificates

---

<!-- note:1772499239678 model:Basic+ -->
**Front:** How are Kubernetes certificates categorized for management?
**Back:** Certificates are grouped into:
1. Client Certificates (for admin/scheduler/controller-manager/kube-proxy)
2. Server Certificates (for API server/etcd/kubelet)
**Tags:** ankidote certificate-grouping kubernetes tls-certificates

---

<!-- note:1772499239681 model:Basic+ -->
**Front:** When might a server act as a client in Kubernetes TLS communication?
**Back:** Servers like the Kube API server communicate with etcd and may use their own certificate (api-server.crt/api-server.key) or a separate etcd-specific certificate pair.
**Tags:** ankidote kubernetes server-clients tls-certificates

---

<!-- note:1772499239683 model:Basic+ -->
**Front:** What are the standard client certificate names for Kubernetes components?
**Back:** 1. Admin: admin.crt/admin.key
2. Scheduler: scheduler.cert/scheduler.key
3. Controller Manager: controller-manager.crt/controller-manager.key
4. Kube Proxy: kube-proxy.crt/kube-proxy.key
**Tags:** ankidote client-certificates kubernetes tls-certificates

---

<!-- note:1772500182398 model:Basic+ -->
**Front:** What is one-way SSL?
**Back:** One-way SSL is a protocol where only the client verifies the server's certificate. The client ensures the server's certificate is trusted, while the server does not authenticate the client, relying on additional credentials like usernames or passwords.
**Tags:** ankidote one-way-ssl security ssl-certificates

---

<!-- note:1772500182401 model:Basic+ -->
**Front:** What is mutual TLS (mTLS)?
**Back:** Mutual TLS (mTLS) is a protocol where both the client and server authenticate each other using certificates. Both parties exchange and verify certificates to ensure mutual trust before establishing secure communication.
**Tags:** ankidote mutual-tls security ssl-certificates

---

<!-- note:1772500182402 model:Basic+ -->
**Front:** What are the key differences in certificate verification between one-way SSL and mTLS?
**Back:** In one-way SSL, only the server's certificate is verified by the client. In mTLS, both the client and server verify each other's certificates.
**Tags:** ankidote mutual-tls one-way-ssl ssl-cert,verification

---

<!-- note:1772500182404 model:Basic+ -->
**Front:** What are typical use cases for one-way SSL?
**Back:** One-way SSL is typically used for internet-based services like online banking, email, and social media, where verifying the server's authenticity is the primary concern.
**Tags:** ankidote one-way-ssl security use-cases

---

<!-- note:1772500182405 model:Basic+ -->
**Front:** What are typical use cases for mutual TLS?
**Back:** Mutual TLS is used for automated system-to-system communication, such as B2B data sharing between organizations, where both parties need to authenticate each other.
**Tags:** ankidote mutual-tls security use-cases

---

<!-- note:1772500182407 model:Basic+ -->
**Front:** How does one-way SSL establish a secure connection?
**Back:** One-way SSL uses asymmetric encryption initially to securely share a symmetric key. The client encrypts a symmetric key with the server's public certificate, and the server decrypts it with its private key. Both parties then use the symmetric key for encrypted communication.
**Tags:** ankidote encryption one-way-ssl security

---

<!-- note:1772500182408 model:Basic+ -->
**Front:** How does mutual TLS establish a secure connection?
**Back:** In mutual TLS, the client requests the server's certificate, and the server responds with its certificate while requesting the client's certificate. The client verifies the server's certificate, then sends its own certificate encrypted with the server's public key. Both parties use the shared symmetric key for encrypted communication after mutual authentication.
**Tags:** ankidote encryption mutual-tls security

---

<!-- note:1772500182410 model:Basic+ -->
**Front:** What is the security level difference between one-way SSL and mTLS?
**Back:** One-way SSL provides secure communication but relies on separate user authentication mechanisms. mTLS offers enhanced security through mutual authentication, ensuring both parties are verified before data exchange.
**Tags:** ankidote mutual-tls one-way-ssl security

---

<!-- note:1772500182411 model:Basic+ -->
**Front:** What role does the certificate authority (CA) play in SSL/TLS?
**Back:** The CA signs certificates to verify their authenticity. Clients trust the CA's public keys, which are stored in their trust stores, allowing them to validate the server's or client's certificate during authentication.
**Tags:** ankidote ca security ssl-certificates

---

<!-- note:1772500182412 model:Basic+ -->
**Front:** What is the purpose of symmetric key encryption in SSL/TLS?
**Back:** Symmetric key encryption is used to encrypt data after the initial asymmetric key exchange. It provides efficient encryption/decryption for the actual data transmitted between the client and server.
**Tags:** ankidote encryption security ssl-protocols

---

<!-- note:1772500513626 model:Basic+ -->
**Front:** What is the purpose of the Docker run command in the example docker run -d nginx?
**Back:** The command initiates container execution by triggering Docker's process to check for the nginx image, download it if missing, and create a container.
**Tags:** ankidote container-execution docker-run

---

<!-- note:1772500513630 model:Basic+ -->
**Front:** What are the four key steps Docker performs when launching a container?
**Back:** 1. CLI to REST API conversion
2. Image verification and download
3. Container creation via containerd
4. Runtime invocation using runc or alternative runtimes
**Tags:** ankidote container-steps docker-process oci-standard

---

<!-- note:1772500513631 model:Basic+ -->
**Front:** What role does containerd play in the container creation process?
**Back:** Containerd converts the image into an OCI-compliant bundle and passes it to the containerd shim for runtime management.
**Tags:** ankidote container-creation containerd oci-compliant

---

<!-- note:1772500513633 model:Basic+ -->
**Front:** How can you specify an alternative container runtime like Kata Containers with Docker?
**Back:** Use the --runtime flag with docker run, e.g., docker run --runtime kata -d nginx to use Kata Containers' runtime.
**Tags:** ankidote docker-runtime kata-containers runtime-flags

---

<!-- note:1772500513635 model:Basic+ -->
**Front:** What is the significance of OCI standards in container runtimes?
**Back:** OCI standards ensure compatibility across container runtimes like runc, Kata Containers, and gVisor by defining standardized bundle formats.
**Tags:** ankidote container-compatibility oci-standard runtime-standards

---

<!-- note:1772500513638 model:Basic+ -->
**Front:** What command starts a container directly using runc instead of Docker?
**Back:** runc run nginx starts a container directly using runc's CLI without Docker's management layers.
**Tags:** ankidote container-execution docker-override runc-cli

---

<!-- note:1772500513640 model:Basic+ -->
**Front:** What runtime does gVisor use, and how is it specified in Docker commands?
**Back:** gVisor uses runsc as its runtime. It's specified with --runtime runsc in Docker commands like docker run --runtime runsc -d nginx.
**Tags:** ankidote gvisor runsc runtime-specification

---

<!-- note:1772500513643 model:Basic+ -->
**Front:** What is the purpose of the containerd shim in the container lifecycle?
**Back:** The containerd shim acts as an intermediary between containerd and the container runtime (like runc), managing container processes and resources.
**Tags:** ankidote container-management containerd-shim runtime-architecture

---

<!-- note:1772500513647 model:Basic+ -->
**Front:** What happens when a Docker image is not found locally?
**Back:** Docker downloads the image from Docker Hub (or configured registry) and caches it locally for future use.
**Tags:** ankidote cache-mechanism docker-registry image-download

---

<!-- note:1772507675713 model:Basic+ -->
**Front:** What is the primary purpose of TLS certificates in Kubernetes?
**Back:** To secure communication between components in a Kubernetes cluster by encrypting data transmitted over networks.
**Tags:** ankidote kubernetes-security tls-certificates

---

<!-- note:1772507675717 model:Basic+ -->
**Front:** What role do Certificate Authorities (CAs) play in TLS?
**Back:** CAs issue and validate digital certificates, acting as trusted third parties to verify the authenticity of certificates.
**Tags:** ankidote certificate-authorities tls-fundamentals

---

<!-- note:1772507675720 model:Basic+ -->
**Front:** What are common TLS troubleshooting challenges in Kubernetes?
**Back:** Common issues include certificate expiration, incorrect SAN configurations, misconfigured trust stores, and certificate revocation problems.
**Tags:** ankidote kubernetes-tls troubleshooting

---

<!-- note:1772507675724 model:Basic+ -->
**Front:** What are the key goals of the TLS Introduction lesson?
**Back:** To understand TLS certificates, generate and configure certificates, troubleshoot issues, and apply these skills specifically to Kubernetes environments.
**Tags:** ankidote kubernetes-certificates tls-goals

---

<!-- note:1772507894345 model:Basic+ -->
**Front:** What is Cloud Security?
**Back:** Cloud Security focuses on protecting the infrastructure (public/private cloud, on-premises, co-located) with network firewalls and access controls to prevent unauthorized access and mitigate risks from exposed ports.
**Tags:** ankidote cloud-security infrastructure-security

---

<!-- note:1772507894349 model:Basic+ -->
**Front:** What was the issue with the cloud infrastructure in the demo?
**Back:** The infrastructure hosting the Kubernetes cluster had unrestricted access to cluster ports, allowing attackers to exploit it without proper network firewalls.
**Tags:** ankidote cloud-security demo-issues

---

<!-- note:1772507894352 model:Basic+ -->
**Front:** What are key components of Cloud Security?
**Back:** Robust network firewalls, proper access controls, and securing all infrastructure types (public/private cloud, on-premises).
**Tags:** ankidote best-practices cloud-security

---

<!-- note:1772507894356 model:Basic+ -->
**Front:** What is Cluster Security?
**Back:** Cluster Security involves protecting the Kubernetes cluster itself, including securing the API, Docker daemon, and dashboard with authentication/authorization.
**Tags:** ankidote cluster-security kubernetes-security

---

<!-- note:1772507894359 model:Basic+ -->
**Front:** What vulnerabilities were exploited in the cluster demo?
**Back:** The attacker exploited an unsecured Docker daemon and a Kubernetes dashboard lacking proper authentication, allowing unauthorized access.
**Tags:** ankidote cluster-security demo-issues

---

<!-- note:1772507894363 model:Basic+ -->
**Front:** What are best practices for securing the Docker daemon?
**Back:** Follow best practices to protect the Docker daemon, such as restricting access and configuring it with minimal privileges.
**Tags:** ankidote cluster-security docker-security

---

<!-- note:1772507894365 model:Basic+ -->
**Front:** What should be enforced for Kubernetes API access?
**Back:** Strict access controls, including role-based permissions and authentication mechanisms, to prevent unauthorized modifications.
**Tags:** ankidote api-security cluster-security

---

<!-- note:1772507894367 model:Basic+ -->
**Front:** What is Container Security?
**Back:** Container Security involves restricting container deployment to trusted images, disabling privileged mode, and using sandboxing to prevent malicious activity.
**Tags:** ankidote container-practices container-security

---

<!-- note:1772507894368 model:Basic+ -->
**Front:** What risks did the demo highlight with container deployment?
**Back:** The attacker deployed containers in privileged mode from untrusted sources, allowing harmful applications and unapproved software to run.
**Tags:** ankidote container-security demo-issues

---

<!-- note:1772507894372 model:Basic+ -->
**Front:** What policies should enforce trusted container images?
**Back:** Policies that allow only images from secure, trusted repositories and enforce strict tagging conventions to prevent unapproved deployments.
**Tags:** ankidote container-security image-security

---

<!-- note:1772507894375 model:Basic+ -->
**Front:** What is Code Security?
**Back:** Code Security focuses on securing application code by avoiding hardcoded credentials, using environment variables for sensitive data, and encrypting data transmission with TLS.
**Tags:** ankidote application-security code-security

---

<!-- note:1772507894377 model:Basic+ -->
**Front:** What vulnerabilities were present in the code demo?
**Back:** The demo showed hardcoded credentials, transmission of sensitive data without TLS, and reliance on environment variables for secrets.
**Tags:** ankidote code-security demo-issues

---

<!-- note:1772507894381 model:Basic+ -->
**Front:** What are recommendations for secure code practices?
**Back:** Implement secrets management solutions, use mTLS for pod communication, and avoid hardcoding sensitive information in code.
**Tags:** ankidote best-practices code-security

---

<!-- note:1772507894383 model:Basic+ -->
**Front:** Why is code security critical in cloud-native environments?
**Back:** Securing code at the application level minimizes vulnerabilities, complementing container, cluster, and cloud security layers to create a holistic defense strategy.
**Tags:** ankidote code-security security-layers

---

<!-- note:1772507894384 model:Basic+ -->
**Front:** What are the four critical areas of Cloud Native Security?
**Back:** Cloud Infrastructure, Cluster Configurations, Container Practices, and Code Integrity.
**Tags:** 4cs-overview ankidote summary

---
