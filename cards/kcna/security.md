<!-- note:1793906734606 model:Many -->
**Domain:** Security Primitives
**Question:** In which order does the kube-apiserver process an incoming request?
**Options:** A. TLS terminates, then Authentication, Authorization, Admission Control, persist to etcd<br>B. Authentication, Authorization, Admission Control, then TLS terminates<br>C. Authorization, Authentication, Admission Control, persist to etcd<br>D. Authentication, Admission Control, Authorization, persist to etcd
**Answer:** A – TLS terminates first, then Authentication, Authorization, Admission Control, then the object persists to etcd
**Explanation:** Every API request passes the same pipeline: transport security (TLS cert check) → Authentication (WHO are you — cert/token/service account) → Authorization (WHAT may you do — RBAC/ABAC/Node/Webhook) → Admission Control (mutate or reject writes, e.g. LimitRange injecting defaults, PSA). Note that admission only acts on create/update/delete/connect requests — pure reads skip it — and the object is only written to etcd after surviving all stages.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/controlling-access/" target="_blank">Kubernetes Docs - Controlling Access to the API</a>
**Tags:** k8s::kcna topic::security topic::api src::session

---

<!-- note:1793906734607 model:Many -->
**Domain:** Security Primitives
**Question:** Which mechanisms can authenticate a caller to the kube-apiserver? (Select all that apply)
**Options:** A. X.509 client certificates signed by the cluster CA<br>B. ServiceAccount tokens (JWTs)<br>C. Static token or password file<br>D. External identity providers (OIDC, webhook, LDAP)<br>E. SSH keys
**Answer:** A, B, C, D – client certs, ServiceAccount tokens, static token/password file, and external providers (OIDC/webhook/LDAP)
**Explanation:** Authentication answers WHO can access the cluster. The API server supports client certificates signed by the cluster CA, bearer tokens (static token file, bootstrap tokens, ServiceAccount JWTs), basic password auth via a static file, and external providers (OIDC, authentication webhook — which bridges LDAP/other IdPs). Multiple modules can be configured and are tried in sequence until one succeeds. SSH keys secure access to the HOSTS, not the Kubernetes API.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/controlling-access/" target="_blank">Kubernetes Docs - Controlling Access to the API</a>
**Tags:** k8s::kcna topic::security topic::api src::session

---

<!-- note:1793906734608 model:Many -->
**Domain:** Security Primitives
**Question:** Which authorization modes can the kube-apiserver enforce? (Select all that apply)
**Options:** A. RBAC — roles bound to users/groups/service accounts<br>B. ABAC — attribute-based access control policies<br>C. Node authorization — constrains kubelets to their own node's objects<br>D. Webhook — delegates the decision to an external service<br>E. OAuth — OAuth2 access tokens
**Answer:** A, B, C, D – RBAC, ABAC, Node authorization, and Webhook mode
**Explanation:** Authorization answers WHAT an authenticated caller may do. The API server can run multiple authorization modules: RBAC (role-based, the common one — Roles/ClusterRoles + bindings), ABAC (attribute-based policies on user/verb/resource), Node authorization (special mode that constrains what kubelets may read/write to the objects their node needs), and Webhook (delegates the decision to an external service). If several modules are configured, each is checked — the request proceeds if ANY module authorizes it.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/controlling-access/" target="_blank">Kubernetes Docs - Controlling Access to the API</a>
**Tags:** k8s::kcna topic::security topic::rbac src::session

---

<!-- note:1793906734609 model:Many -->
**Domain:** Security Primitives
**Question:** Which statement about encryption between Kubernetes components is TRUE?
**Options:** A. All control-plane traffic is TLS-encrypted: kubectl→apiserver, apiserver↔etcd, and apiserver to kubelets/other components<br>B. Only kubectl→apiserver is encrypted; inter-component traffic is plain HTTP<br>C. TLS is an optional add-on installed by the CNI plugin<br>D. Components authenticate each other with bearer tokens, so TLS is unnecessary
**Answer:** A – all control-plane component traffic plus client traffic to the apiserver is TLS-encrypted
**Explanation:** TLS secures the entire control plane: kubectl/clients to kube-apiserver, apiserver to etcd, and apiserver's calls to kubelets, kube-proxy and the other components are all encrypted in transit (with a cluster CA — typically etcd, /etc/kubernetes/pki, issued by kubeadm or your own PKI). Plaintext is not a supported posture for API traffic; the 'insecure port' was removed entirely in Kubernetes 1.20.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/controlling-access/" target="_blank">Kubernetes Docs - Controlling Access to the API</a>
**Tags:** k8s::kcna topic::security topic::control-plane src::session

---

<!-- note:1793906734610 model:Many -->
**Domain:** Security Primitives
**Question:** Before applying Kubernetes-level security controls, what should be hardened first?
**Options:** A. The underlying hosts — SSH key-only auth, no password logins, patched OS<br>B. The pod manifests — set a securityContext first<br>C. The CNI plugin — enable its security features first<br>D. The container registry — sign all images first
**Answer:** A – harden the underlying hosts first: SSH key-only login, no password auth, patched OS
**Explanation:** Defense starts below Kubernetes: the cluster lives on its nodes, and a rooted node means a rooted cluster. Baseline host hardening — SSH key-only access, password auth disabled, OS patched, no unneeded services/ports — comes before any Kubernetes-level control. Only after the hosts are secured does the k8s-specific layering matter: API access control, RBAC, NetworkPolicies, pod security.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/controlling-access/" target="_blank">Kubernetes Docs - Controlling Access to the API</a>
**Tags:** k8s::kcna topic::security topic::architecture src::session

---

<!-- note:1793906741654 model:Basic (and reversed card) -->
**Front:** By default, how much pod-to-pod traffic does Kubernetes allow, and what restricts it?
**Back:** Open — the pod network is flat: every pod can reach every other pod and namespace by default (no built-in isolation). NetworkPolicy is the opt-in control: a policy selects pods (podSelector) and whitelists ingress/egress; once a pod is selected by any policy, only matching traffic is allowed. Policies are enforced by the CNI plugin — a CNI that doesn't support NetworkPolicies silently ignores them.
**Tags:** k8s::kcna topic::security topic::networking src::session

---
<!-- note:1793913170420 model:Many -->
**Domain:** Authentication
**Question:** In X.509 client-certificate authentication, how does Kubernetes map a certificate's subject to a user identity?
**Options:** A. The Issuer field becomes the username<br>B. CN maps to the username; O entries map to groups<br>C. The certificate serial number becomes the UID<br>D. Validity dates decide the session timeout
**Answer:** B – the Common Name (CN) maps to the username and Organization (O) entries map to groups
**Explanation:** Certificate attributes become identity: CN → username, each O → a group (order doesn't matter). So a cert with subject '/CN=alice/O=devs/O=ops' authenticates as user 'alice' in groups 'devs'+'ops' — plus everyone authentic'd also joins 'system:authenticated'. Signed by the cluster's client CA, the identity is then passed to authorization (RBAC) for permission checks.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Docs - Authentication</a>
**Tags:** k8s::kcna topic::security topic::authentication topic::tls src::session

---

<!-- note:1793913170421 model:Many -->
**Domain:** Authentication
**Question:** How does the static token file authentication method work?
**Options:** A. A ConfigMap listing users and passwords<br>B. A Secret of type kubernetes.io/service-account-token<br>C. CSV rows of 'token,user,uid,"groups"' served by <code>--token-auth-file</code><br>D. A users.yaml inside /etc/kubernetes/manifests
**Answer:** C – CSV rows of 'token,user,uid,"group1,group2"' served by the apiserver flag <code>--token-auth-file</code>
**Explanation:** The static token file is a CSV on the control-plane node passed via '--token-auth-file=/path/file.csv'; each row is token,user,uid,"groups". Callers present the token as 'Authorization: Bearer &lt;token&gt;'. It's simple but static — changing users means editing the file and restarting kube-apiserver, and tokens are plaintext on disk, so it's discouraged for production.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Docs - Authentication</a>
**Tags:** k8s::kcna topic::security topic::authentication topic::api src::session

---

<!-- note:1793913170422 model:Many -->
**Domain:** Authentication
**Question:** What happens to an API request that presents NO credentials at all?
**Options:** A. They are rejected with 403 Forbidden<br>B. They map to system:anonymous in group system:unauthenticated (if anonymous auth is on)<br>C. They get read-only guest permissions<br>D. They retry after a backoff
**Answer:** B – unauthenticated calls map to system:anonymous / system:unauthenticated (401 if disabled)
**Explanation:** Requests that pass no credentials don't automatically get rejected: if anonymous auth is enabled they become 'system:anonymous' in group 'system:unauthenticated' and RBAC decides if that identity may act (usually it can't). Disable with '--anonymous-auth=false' on kube-apiserver. Every request is thus either an authenticated identity (users get 'system:authenticated' added) or the anonymous identity.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Docs - Authentication</a>
**Tags:** k8s::kcna topic::security topic::authentication topic::api src::session

---

<!-- note:1793913170423 model:Many -->
**Domain:** Authentication
**Question:** How can external identity systems like LDAP or Kerberos authenticate Kubernetes users? (Select all that apply)
**Options:** A. LDAP via a built-in <code>--ldap-server</code> flag<br>B. An authenticating proxy that forwards identity headers<br>C. An authentication webhook (TokenReview API)<br>D. Kerberos tickets passed directly to the apiserver
**Answer:** B, C – authenticating proxy or authentication webhook; native OIDC is the built-in IdP path
**Explanation:** There is no native LDAP/Kerberos/SAML plugin: Kubernetes natively supports client certs, bearer tokens (incl. ServiceAccount JWTs), and OIDC. To reach LDAP/Kerberos/etc. you front the API with an authenticating proxy that maps headers to user identity, or use an authentication webhook — the apiserver calls your token-review service which returns the user info. OIDC (e.g. Dex/Keycloak/Entra) is the one external-identity mechanism the API server supports natively.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Docs - Authentication</a>
**Tags:** k8s::kcna topic::security topic::authentication topic::api src::session

---

<!-- note:1793913170424 model:Many -->
**Domain:** Authentication
**Question:** After '<code>kubectl create serviceaccount jenkins</code>', what username does the API server assign that identity?
**Options:** A. system:serviceaccount:&lt;namespace&gt;:jenkins<br>B. jenkins@&lt;namespace&gt;.svc<br>C. system:user:jenkins<br>D. user:jenkins:service
**Answer:** A – <code>kubectl create serviceaccount jenkins</code> produces identity 'system:serviceaccount:&lt;namespace&gt;:jenkins'
**Explanation:** ServiceAccounts ARE API objects — namespaced and creatable via kubectl or YAML (unlike normal users). Pods mount the SA's token, and in-cluster processes authenticate as 'system:serviceaccount:&lt;ns&gt;:&lt;name&gt;' in groups 'system:serviceaccounts' and 'system:serviceaccounts:&lt;ns&gt;'; the signed JWT also works for clients outside the cluster. Because SA tokens can be stored in Secrets, be careful who can read them.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Docs - Authentication</a>
**Tags:** k8s::kcna topic::security topic::authentication topic::serviceaccounts src::session

---

<!-- note:1793913173620 model:Basic (and reversed card) -->
**Front:** Users vs ServiceAccounts in Kubernetes — which ones can you '<code>kubectl create</code>'?
**Back:** Only ServiceAccounts — they ARE API objects (namespaced, kubectl-creatable). Normal users are NOT Kubernetes objects at all: 'Kubernetes does not have objects which represent normal user accounts.' Humans/automation get identity from an external source — a client cert signed by the cluster CA, an OIDC/IdP login, a static token file — and the apiserver just validates it. Rule of thumb: humans = external user identity; in-cluster processes = ServiceAccount.
**Tags:** k8s::kcna topic::security topic::authentication topic::serviceaccounts src::session

---
<!-- note:1793913972240 model:Many -->
**Domain:** TLS Certificates
**Question:** What is a Certificate Authority (CA) and what does it do?
**Options:** A. A service that stores certificates for retrieval<br>B. The trusted issuer that signs certificates; everything trusts certs signed by it<br>C. A load balancer that terminates TLS<br>D. An etcd key that encrypts secrets
**Answer:** B – the trusted issuer that signs certificates; everything trusts certs signed by it
**Explanation:** A CA is the root of trust: it holds a key pair (ca.key private + ca.crt public cert). It validates CSRs and signs them with ca.key — the signature is what makes a certificate trustworthy. Every client/server carries a copy of ca.crt and accepts any cert signed by that CA. In a cluster the CA is how all components verify each other's identity; keep ca.key private on the signing host — whoever has it can mint identities.
**Sources:** <a href="https://kubernetes.io/docs/setup/best-practices/certificates/" target="_blank">Kubernetes Docs - PKI certificates and requirements</a>
**Tags:** k8s::kcna topic::security topic::tls topic::certificates src::session

---

<!-- note:1793913972241 model:Many -->
**Domain:** TLS Certificates
**Question:** To mint a cluster-admin user cert for kubectl access, what must the certificate subject contain?
**Options:** A. CN=system:masters<br>B. O=system:masters — the O field carries the group<br>C. OU=admin plus CN=system:masters<br>D. A special flag in the CSR's extensions
**Answer:** B – the O (Organization) field carries group membership; O=system:masters grants cluster-admin
**Explanation:** Groups come from the cert's O field — 'openssl req -subj "/CN=kube-admin/O=system:masters"' makes an identity that authenticates as user 'kube-admin' in group 'system:masters'. system:masters is bound to the cluster-admin ClusterRole out of the box, which is what actually grants full control — the cert just proves membership.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Docs - Authentication</a>
**Tags:** k8s::kcna topic::security topic::tls topic::certificates topic::rbac src::session

---

<!-- note:1793913972242 model:Many -->
**Domain:** TLS Certificates
**Question:** Which identity mappings do Kubernetes component certificates require? (Select all that apply)
**Options:** A. kube-proxy cert must carry <code>CN=system:kube-proxy</code><br>B. Each kubelet cert must carry <code>CN=system:node:&lt;nodename&gt;</code> with <code>O=system:nodes</code><br>C. Admin users need <code>O=system:masters</code> in their cert<br>D. Any CN works — RBAC ignores certificate subjects
**Answer:** A, B, C – <code>system:kube-proxy</code> for kube-proxy, <code>system:node:&lt;nodename&gt;</code>+<code>O=system:nodes</code> for each kubelet, <code>O=system:masters</code> for admin users
**Explanation:** Component identities are fixed names the control plane expects: kube-proxy authenticates as <code>system:kube-proxy</code> (CN), each kubelet as <code>system:node:&lt;nodeName&gt;</code> (CN) plus group <code>system:nodes</code> (O) — Node authorizer relies on that mapping; an admin user is 'kube-admin' (or any CN) in group <code>system:masters</code>. Certificates without the right CN/O authenticate as someone else entirely and get rejected by authorization.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Docs - Authentication</a>
**Tags:** k8s::kcna topic::security topic::tls topic::certificates topic::control-plane src::session

---

<!-- note:1793913972243 model:Many -->
**Domain:** TLS Certificates
**Question:** Why does the kube-apiserver certificate need an openssl.cnf with an [alt_names] section?
**Options:** A. openssl.cnf encrypts the private key<br>B. alt_names lists every DNS name and IP clients use to reach the apiserver — required or hostname verification fails<br>C. It's only needed to set the certificate expiry date<br>D. SANs are for encrypting etcd at rest
**Answer:** B – SANs let one cert be valid for every name/IP clients dial the apiserver by (kubernetes, .svc FQDNs, internal + external IPs)
**Explanation:** The apiserver is reachable under several names: the 'kubernetes' Service name (kubernetes, kubernetes.default, kubernetes.default.svc, kubernetes.default.svc.cluster.local), plus node/public IPs. TLS hostname verification fails if the dialed name isn't in the cert — so the openssl.cnf used to generate the apiserver cert carries an [alt_names] section listing every DNS name and IP (internal + external) that will reach it.
**Sources:** <a href="https://kubernetes.io/docs/setup/best-practices/certificates/" target="_blank">Kubernetes Docs - PKI certificates and requirements</a>
**Tags:** k8s::kcna topic::security topic::tls topic::certificates topic::api src::session

---

<!-- note:1793913972244 model:Many -->
**Domain:** TLS Certificates
**Question:** How is TLS handled between etcd cluster members?
**Options:** A. etcd doesn't support TLS — it relies on NetworkPolicies<br>B. Peer certs authenticate etcd members to each other; client certs authenticate the apiserver — both set via etcd config flags<br>C. etcd certs are stored as Kubernetes Secrets and mounted at runtime<br>D. Peer certs are only for etcd backups
**Answer:** B – etcd members authenticate each other with peer certificates; apiserver↔etcd uses client certs, all configured via etcd flags
**Explanation:** etcd runs its own PKI within the cluster's: member-to-member (peer) traffic uses <code>--peer-cert-file</code>/<code>--peer-key-file</code>/<code>--peer-trusted-ca-file</code>, and clients (kube-apiserver) use <code>--cert-file</code>/<code>--key-file</code>/<code>--trusted-ca-file</code>. These paths are set in the etcd static pod manifest (/etc/kubernetes/manifests/etcd.yaml on kubeadm) — usually under /etc/kubernetes/pki/etcd/.
**Sources:** <a href="https://kubernetes.io/docs/setup/best-practices/certificates/" target="_blank">Kubernetes Docs - PKI certificates and requirements</a>
**Tags:** k8s::kcna topic::security topic::tls topic::certificates topic::etcd src::session

---

<!-- note:1793913972245 model:Many -->
**Domain:** TLS Certificates
**Question:** Who needs the CA certificate, and who needs the CA private key?
**Options:** A. Distribute ca.crt to every component for verification; keep ca.key private on the signing host<br>B. Distribute ca.key so components can verify certs<br>C. Copy both key and cert everywhere — they're a pair<br>D. Neither — verification uses the etcd root
**Answer:** A – everyone gets a COPY of the CA certificate to verify peers; ca.key never leaves the signing host
**Explanation:** Verification is asymmetric: to trust a peer's certificate you only need the CA's public cert — so ca.crt is distributed to every node, component config, and kubeconfig (certificate-authority field). The ca.key is what mints identities, so it stays private on the control-plane/signing host: whoever holds it can forge any identity in the cluster.
**Sources:** <a href="https://kubernetes.io/docs/setup/best-practices/certificates/" target="_blank">Kubernetes Docs - PKI certificates and requirements</a>
**Tags:** k8s::kcna topic::security topic::tls topic::certificates src::session

---

<!-- note:1793913972246 model:Many -->
**Domain:** TLS Certificates
**Question:** What is a Certificate Signing Request (CSR)?
**Options:** A. A certificate backup for disaster recovery<br>B. An unsigned request containing the public key + subject details the CA signs into a certificate<br>C. A certificate that failed hostname verification<br>D. The CA's own self-signed root
**Answer:** B – an unsigned request: public key + subject details (CN, O, SANs) packaged for the CA to sign into a certificate
**Explanation:** A CSR is your key pair's PUBLIC half plus identity details (CN username, O groups, SANs) wrapped into a signing request — a certificate-to-be minus the signature. You hand it to a CA (<code>openssl req -new -key x.key -out x.csr</code>), it verifies and stamps 'signed by me' (<code>openssl x509 -req -in x.csr -CA ca.crt -CAkey ca.key -out x.crt</code>). The private key never leaves your side.
**Sources:** <a href="https://kubernetes.io/docs/setup/best-practices/certificates/" target="_blank">Kubernetes Docs - PKI certificates and requirements</a>
**Tags:** k8s::kcna topic::security topic::tls topic::certificates src::session

---

<!-- note:1793913979368 model:Cloze -->
**Text:** Build a cluster CA with openssl — private key, signing request, then self-signed root:<br><br>{{c1::<code>openssl genrsa -out ca.key 2048</code>}}  # CA private key<br>{{c2::<code>openssl req -new -key ca.key -subj "/CN=KUBERNETES-CA" -out ca.csr</code>}}  # CSR: public key + subject, unsigned<br>{{c3::<code>openssl x509 -req -in ca.csr -signkey ca.key -days 1000 -out ca.crt</code>}}  # CA signs its OWN cert with its own key<br><br>Every other cert swaps '-signkey ca.key' for '-CA ca.crt -CAkey ca.key' — issued by the CA.
**Back Extra:** The self-sign trick: -signkey uses the SAME ca.key that generated the CSR — only the root CA self-signs. Downstream certs get -CA/-CAkey instead, tying their trust back to ca.crt.
**Tags:** k8s::kcna topic::security topic::tls topic::certificates src::session

---
<!-- note:1793914089195 model:Many -->
**Domain:** TLS Certificates - Kubelet
**Question:** How does each kubelet authenticate to the kube-apiserver?
**Options:** A. One shared cluster cert copied to every node<br>B. A per-node client cert: <code>CN=system:node:&lt;nodeName&gt;</code>, <code>O=system:nodes</code><br>C. A ServiceAccount token mounted at /var/lib/kubelet<br>D. The node's SSH host key
**Answer:** B – a per-node client cert with <code>CN=system:node:&lt;nodeName&gt;</code> and <code>O=system:nodes</code>, unique to that machine
**Explanation:** Every kubelet talks to the apiserver as its OWN node identity: the client cert's CN must be <code>system:node:&lt;nodeName&gt;</code> and <code>O=system:nodes</code> — one cert per node, minted with that node's name. kubeadm keeps it under <code>/var/lib/kubelet/pki/</code> and references it in <code>kubelet.conf</code>; with TLS bootstrap the kubelet even requests the cert itself via the certificates.k8s.io CSR API using a bootstrap token.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authentication/" target="_blank">Kubernetes Docs - Authentication</a>
**Tags:** k8s::kcna topic::security topic::tls topic::control-plane src::session

---

<!-- note:1793914089196 model:Many -->
**Domain:** Node Authorization
**Question:** What ties a kubelet's access to only its own node's objects?
**Options:** A. RBAC RoleBindings per node<br>B. The Node authorizer matches the cert's <code>system:node:&lt;name&gt;</code> to scope kubelet to its own node's objects<br>C. NetworkPolicy blocks cross-node API calls<br>D. kube-proxy filters kubelet traffic
**Answer:** B – Node authorization uses the cert's <code>system:node:&lt;name&gt;</code> to restrict each kubelet to objects belonging to its own node
**Explanation:** The Node authorizer + NodeRestriction admission gate kubelet requests against the node name baked into its cert: 'system:node:worker-2' may only read pods scheduled to worker-2 and update its own node/secrets — it cannot list other nodes' pods or secrets. The name match is why node certs are per-node: a stolen kubelet cert only grants that one node's reach.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/node/" target="_blank">Kubernetes Docs - Node Authorization</a>
**Tags:** k8s::kcna topic::security topic::rbac src::session

---
<!-- note:1793915613866 model:Many -->
**Domain:** NetworkPolicy - isolation
**Question:** If a Pod is selected by at least one NetworkPolicy for ingress, what's the default behavior for ingress traffic?
**Options:** A. Ignore all NetworkPolicies<br>B. Only allow NodePort<br>C. Allow all<br>D. Deny all ingress except what policies allow
**Answer:** D – deny all ingress except what policies allow
**Explanation:** Selection triggers default-deny for that direction, then allow rules apply. Pods selected by NO NetworkPolicy are fully open (allow-all); the moment ≥1 policy's podSelector matches, that direction flips to isolated and ONLY traffic matching the policy's ingress rules passes — everything else is dropped. Three nuances: isolation is per-direction (ingress selection leaves egress open unless a policy also lists egress); policies are additive — multiple selecting policies OR their rules together (union, not strictest-wins); and enforcement depends on the CNI plugin supporting NetworkPolicy — unsupported CNIs silently ignore policies, leaving the pod open.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Docs - Network Policies</a>
**Tags:** k8s::kcna topic::networkpolicy topic::security topic::networking src::session

---

<!-- note:1793920650504 model:Many -->
**Domain:** Service Communication
**Question:** Why use certificates between services?
**Options:** A. Encrypt + authenticate (TLS/mTLS)<br>B. Increase CPU<br>C. Replace DNS<br>D. Stop restarts
**Answer:** A (1) – encrypt + authenticate (TLS/mTLS)
**Explanation:** Certificates between services buy TWO things at once: encryption in transit (pod-to-pod traffic crosses node networks where cleartext HTTP would expose credentials and data) AND identity verification — with mTLS BOTH sides present certs, so each service proves who it is, not just that the channel is private. That's the security layer service meshes like Istio/Linkerd automate at scale. The distractors are nonsense or other systems' jobs: certificates don't speed anything up (mTLS costs CPU for handshake/crypto), DNS is CoreDNS, and restart behavior belongs to liveness probes and controllers.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/" target="_blank">Kubernetes Docs - Security</a>
**Tags:** k8s::kcna topic::security topic::tls topic::mtls src::session

---

<!-- note:1793921403923 model:Many -->
**Domain:** RBAC - additive model
**Question:** Kubernetes RBAC "deny" behavior:
**Options:** A. ClusterRole overrides to remove<br>B. RBAC is additive; reduce by removing/changing bindings/roles<br>C. Roles can explicitly deny<br>D. Empty Role cancels other grants
**Answer:** B (2) – RBAC is additive; reduce access by removing or narrowing bindings/roles
**Explanation:** RBAC has NO deny mechanism: there is no 'deny' verb, a Role cannot express 'allow everything except X', and an empty Role grants nothing rather than cancelling other grants. Permissions only accumulate — effective access is the UNION of every Role/ClusterRole bound to you (and across authz modes, an allow from ANY enabled mode wins). Wildcards (*) in rules only expand grants, never subtract. The only ways to reduce someone's access are removing the RoleBinding/ClusterRoleBinding, or editing the Role's rules to narrow verbs/resources. This differs from firewalls/SELinux where explicit deny rules exist — RBAC can't do default-deny-with-exceptions.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna topic::rbac topic::security src::session

---

<!-- note:1793921403924 model:Many -->
**Domain:** ServiceAccounts - token mount
**Question:** Which setting prevents a Pod from auto-mounting a ServiceAccount token?
**Options:** A. runAsNonRoot: true<br>B. automountServiceAccountToken: false<br>C. readOnlyRootFilesystem: true<br>D. serviceAccountName: ""
**Answer:** B (2) – automountServiceAccountToken: false
**Explanation:** Every pod gets a ServiceAccount token auto-mounted at /var/run/secrets/kubernetes.io/serviceaccount/ — a projected volume holding the SA's JWT plus the cluster CA cert — because the default is automountServiceAccountToken: true. Setting it false (on the pod spec or on the ServiceAccount itself) skips the mount entirely. It exists for least privilege: any process in the pod can read that token and authenticate to the API server AS that ServiceAccount, so mounting it everywhere means every container carries a live credential it may never need — a stolen token = stolen API access. Pods that don't call the K8s API shouldn't get one; pair it with an RBAC-scoped SA so even mounted tokens can only do what's needed. Distractors: runAsNonRoot and readOnlyRootFilesystem are pod securityContext hardening (UID/filesystem), and serviceAccountName only selects WHICH account — an empty value still mounts the default SA's token.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/" target="_blank">Kubernetes Docs - Configure Service Accounts for Pods</a>
**Tags:** k8s::kcna topic::serviceaccounts topic::security topic::pods src::session

---

<!-- note:1793921727121 model:Many -->
**Domain:** Pod Security Standards
**Question:** Pod Security Standards levels, ordered least → most restrictive:
**Options:** A. Restricted → Baseline → Privileged<br>B. Privileged → Baseline → Restricted<br>C. Baseline → Restricted → Privileged<br>D. Baseline → Privileged → Restricted
**Answer:** B (2) – Privileged → Baseline → Restricted
**Explanation:** Least → most restrictive: Privileged → Baseline → Restricted. The levels are cumulative — Restricted includes ALL Baseline rules plus hardened requirements (runAsNonRoot, drop ALL capabilities, seccomp profile, no privilege escalation). Privileged is unrestricted (the effective default for unlabeled namespaces). Baseline blocks only the obviously dangerous: privileged containers, host namespaces/PID/IPC, hostPath volumes, host ports, dangerous capabilities. Restricted enforces current pod-hardening best practices. Enforcement is via namespace labels like <code>pod-security.kubernetes.io/enforce=restricted</code>, with audit and warn modes for rollout — Pod Security Admission replaced the deprecated PodSecurityPolicy.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/pod-security-standards/" target="_blank">Kubernetes Docs - Pod Security Standards</a>
**Tags:** k8s::kcna topic::security topic::podsecurity topic::pods src::session

---

<!-- note:1793932206940 model:Many -->
**Domain:** Node Authorization - permitted identities
**Question:** Who is authorized by the node authorizers to make requests to kube-apiserver?
**Options:** A. Only the kubelet running on the master node<br>B. Any user with system administrator privileges<br>C. Any user that is part of the Kubernetes cluster<br>D. Any request from a user named system:node:&lt;name&gt; in the system:nodes group
**Answer:** D (4) – requests from a user named system:node:&lt;name&gt; in the system:nodes group
**Explanation:** The Node authorizer is a special mode built for kubelets: it only authorizes requests authenticated as system:node:&lt;nodeName&gt; belonging to group system:nodes — the identity kubelets get from their client certs (CN=system:node:&lt;name&gt;, O=system:nodes). It then scopes WHAT they may touch: pods bound to their node, node objects/status, mirrored EndpointSlices, leases, and CSRs for their node's certs — tightened further by NodeRestriction. It's identity-based, not role-based: cluster membership or OS admin rights mean nothing here; regular users are denied even though they're 'part of the cluster'. Runs alongside RBAC (--authorization-mode=Node,RBAC) — Node handles kubelet traffic, RBAC handles everything else.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/node/" target="_blank">Kubernetes Docs - Node authorizer</a>
**Tags:** k8s::kcna topic::security topic::kubelet topic::rbac src::session

---

<!-- note:1793932282196 model:Many -->
**Domain:** NetworkPolicy - pod selection
**Question:** Where do we specify the pod labels in a Kubernetes network policy definition file?
**Options:** A. spec.podSelector<br>B. spec.egress<br>C. spec.ingress<br>D. spec.matchLabels
**Answer:** A (1) – spec.podSelector
**Explanation:** spec.podSelector selects WHICH pods the policy applies to — the labels themselves go under spec.podSelector.matchLabels (or matchExpressions for operators). An empty podSelector: {} selects ALL pods in the policy's namespace. spec.ingress and spec.egress are the traffic RULE lists (from/to peers + ports), not selectors — spec.matchLabels isn't a NetworkPolicy field at all (that's the style used inside podSelector and in workload selectors like a Deployment's spec.selector.matchLabels).
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Docs - Network Policies</a>
**Tags:** k8s::kcna topic::networking topic::networkpolicy topic::yaml src::session

---

<!-- note:1793932581200 model:Many -->
**Domain:** ServiceAccounts - immutability
**Question:** What statement/s is/are true about the service account of an existing pod in Kubernetes?
**Options:** A. You can change the service account by running kubectl edit pod and modifying the service account field.<br>B. The service account of a pod can be changed by directly modifying the service account field in the running pod using kubectl apply without modifying the pod definition file.<br>C. The service account is set when the pod is created and cannot be changed afterwards.<br>D. You can change the service account by modifying the pod definition file and updating the service account name field.
**Answer:** C (3) – the service account is set when the pod is created and cannot be changed afterwards
**Explanation:** spec.serviceAccountName is immutable after pod creation — same pattern as spec.nodeName: it's fixed at admission and the API server rejects kubectl edit/patch/apply attempts on a live pod (that's why A, B and D all fail — D would work for a NEW pod via the definition file, but applying it to an existing pod errors on the immutable field). To change a pod's SA you must delete and recreate it — for Deployments that's updating the pod template and letting the rollout create new pods. Note the distinction: you CAN change what an SA is allowed to do (edit its RBAC bindings) — that changes permissions of the identity, not which identity the pod uses. The mounted token is also projected at creation, so the pod's credential can't be swapped in place either.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/" target="_blank">Kubernetes Docs - Configure Service Accounts for Pods</a>
**Tags:** k8s::kcna topic::serviceaccounts topic::pods topic::security src::session

---

<!-- note:1793932659732 model:Many -->
**Domain:** Node Authorization - role
**Question:** What is the role of the node authoriser in Kubernetes cluster?
**Options:** A. Handles requests from the kubelets on nodes to the kube-apiserver<br>B. Handles requests from human users to the kube-apiserver<br>C. Deploys and manages nodes within the Kubernetes cluster<br>D. Manages access control policies for the Kubernetes cluster
**Answer:** A (1) – handles requests from the kubelets on nodes to the kube-apiserver
**Explanation:** The Node authorizer is a specialized authorization module that handles ONLY kubelet→apiserver requests: it verifies the caller is authenticated as system:node:&lt;nodeName&gt; in group system:nodes, then decides what that kubelet may read/write for its own node — pods bound to it, node objects/status, mirrored EndpointSlices, leases, and certificate-signing requests for its serving certs (tightened by NodeRestriction). Human users never pass through it — they go through RBAC/Webhook/etc. It doesn't deploy or manage nodes (that's the kubelet executing instructions, and cluster autoscaler/node lifecycle controllers), and it doesn't manage access policies generally — that's RBAC's job; Node,RBAC run side by side in --authorization-mode.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/node/" target="_blank">Kubernetes Docs - Node authorizer</a>
**Tags:** k8s::kcna topic::security topic::kubelet topic::rbac src::session

---

<!-- note:1793932923824 model:Many -->
**Domain:** NetworkPolicy - CNI support
**Question:** Which of the following solutions support Kubernetes network policies?
**Options:** A. Flannel, weave-net, and kube-proxy<br>B. Calico, weave-net, and flannel<br>C. Kube router, calico, and flannel<br>D. Kube router, calico, and weave-net
**Answer:** D (4) – kube-router, calico, and weave-net
**Explanation:** NetworkPolicy is just an API — the CNI plugin must actually ENFORCE it, so support is entirely CNI-dependent. Calico, weave-net and kube-router all ship NetworkPolicy controllers (kube-router even has an official Kubernetes docs page for it; Cilium and Antrea do too). Flannel is the classic 'no' — flanneld only does overlay networking/routing and is policy-unaware (newer flannel charts can bundle a separate policy controller, but that's an add-on, not flannel itself). kube-proxy isn't a CNI at all — it programs Service ClusterIP/NodePort rules on each node; it has nothing to do with pod ingress/egress policy.
**Sources:** <a href="https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/kube-router-network-policy/" target="_blank">Kubernetes Docs - Use Kube-router for NetworkPolicy</a>
**Tags:** k8s::kcna topic::networking topic::networkpolicy topic::cni src::session

---

<!-- note:1793933047097 model:Many -->
**Domain:** NetworkPolicy - policyTypes
**Question:** If you have only the ingress in the policyTypes, what does it mean?
**Options:** A. Only the ingress traffic is isolated, and all egress traffic is unaffected.<br>B. Only the egress traffic is isolated, and all ingress traffic is unaffected.<br>C. Both ingress and egress traffic are isolated.<br>D. There is no network policy applied.
**Answer:** A (1) – only the ingress traffic is isolated, and all egress traffic is unaffected
**Explanation:** policyTypes declares which traffic DIRECTIONS the policy governs. Listing only Ingress means: selected pods get default-deny on inbound traffic, then the policy's ingress rules carve out exceptions — while egress is completely untouched, pods can still initiate any outbound connection. policyTypes: [Egress] does the reverse. The subtle default: if you OMIT policyTypes, Kubernetes infers it — an ingress: rules section implies Ingress, an egress: section implies Egress; and a policy with podSelector but NO rule lists at all defaults to BOTH directions (full isolation). Also note: NetworkPolicy never filters traffic to/from the node itself (hostNetwork/kubelet traffic is exempt).
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/" target="_blank">Kubernetes Docs - Network Policies</a>
**Tags:** k8s::kcna topic::networking topic::networkpolicy topic::yaml src::session

---

<!-- note:1793933351049 model:Many -->
**Domain:** ServiceAccounts - bound tokens
**Question:** What are the characteristics of tokens generated by the Kubernetes Token Request API?
**Options:** A. Audience bound, time bound, and object bound<br>B. Time bound, cluster bound, and namespace bound<br>C. Audience bound, object bound, and cluster bound<br>D. Time bound, object bound, and namespace bound
**Answer:** A (1) – audience bound, time bound, and object bound
**Explanation:** TokenRequest API tokens (authentication.k8s.io/v1 — also what kubectl create token and projected serviceAccountToken volumes use) carry three bindings: AUDIENCE-bound — spec.audiences becomes the JWT aud claim; a recipient must match one of them or reject the token (default: the API server). TIME-bound — spec.expirationSeconds sets exp/nbf/iat claims; kubelet auto-rotates projected tokens before expiry (~80% of TTL, default ~1h). OBJECT-bound (optional) — spec.boundObjectRef embeds the target object's name+UID as private claims; the token only works while that object exists AND the request comes from it (Pod/Secret, Node since v1.33). 'Cluster bound' and 'namespace bound' aren't TokenRequest concepts — this API replaced the legacy never-expiring Secret-mounted SA tokens.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/" target="_blank">Kubernetes Docs - Managing Service Accounts: Bound service account tokens</a>
**Tags:** k8s::kcna topic::serviceaccounts topic::security topic::authentication src::session

---

<!-- note:1793933768337 model:Many -->
**Domain:** RBAC - RoleBinding structure
**Question:** What are the two sections of the RoleBinding object?
**Options:** A. Subjects and RoleRef<br>B. Users and Permissions<br>C. Role and User<br>D. APIGroups and Resources
**Answer:** A (1) – Subjects and RoleRef
**Explanation:** A RoleBinding has two functional sections: subjects — WHO gets the permissions (a list of kind: User/Group/ServiceAccount entries with name and namespace) — and roleRef — WHAT they get (a pointer with apiGroup, kind, and name referencing either a Role or a ClusterRole). roleRef is IMMUTABLE: you can't repoint an existing binding to a different role — delete and recreate it instead. A namespaced RoleBinding may reference a ClusterRole, but the granted permissions then apply only within the binding's namespace; ClusterRoleBinding is the cluster-wide variant with the same two fields.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna topic::rbac topic::security topic::yaml src::session

---

<!-- note:1793934056843 model:Many -->
**Domain:** ServiceAccounts - token secrets
**Question:** Which of the following statements is true regarding service accounts in Kubernetes version 1.24?
**Options:** A. When a service account is created, it only creates a token access secret but not a regular secret.<br>B. When a service account is created, it only creates a secret but not a token access secret.<br>C. When a service account is created, it no longer automatically creates a secret or a token access secret.<br>D. When a service account is created, it automatically creates a secret and a token access secret.
**Answer:** C (3) – when a service account is created, it no longer automatically creates a secret or a token access secret
**Explanation:** Since Kubernetes 1.24 (KEP-2799), creating a ServiceAccount creates ONLY the SA object — no Secret is auto-generated. Before 1.24, kubectl create sa / a pod referencing an SA triggered creation of a kubernetes.io/service-account-token Secret holding a never-expiring JWT mounted into pods. That mechanism was removed because those tokens never expired and couldn't be rotated — pods now get short-lived, audience/time/object-bound tokens via the TokenRequest API and projected serviceAccountToken volumes instead. Legacy auto-created Secrets that already exist are NOT deleted, but they aren't refreshed either — migration path is to delete them and switch workloads to projected tokens.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/" target="_blank">Kubernetes Docs - Managing Service Accounts</a>
**Tags:** k8s::kcna topic::serviceaccounts topic::secrets topic::security src::session

---

<!-- note:1793934915989 model:Many -->
**Domain:** Authorization - AlwaysDeny
**Question:** What is the behavior of the AlwaysDeny authorisation mode in Kubernetes?
**Options:** A. Allows all requests without performing any authorisation checks<br>B. Allows requests based on a policy file with a set of policies defined in a JSON format<br>C. Denies all requests<br>D. Authorises requests coming from a user with the name system node and part of the system nodes group
**Answer:** C (3) – denies all requests
**Explanation:** AlwaysDeny is an --authorization-mode that rejects EVERY API request with 403 Forbidden — yes, literally nothing works while it's the only/first effective mode: no reads, no writes, kubectl dead. It's not for production; it's a deliberate kill-switch and testing tool: emergency lockdown of a compromised or misbehaving cluster, negative testing (prove your RBAC actually blocks things — if requests still succeed under AlwaysDeny, something upstream is wrong), and mode-ordering experiments. Its opposite pole is AlwaysAllow (permits everything after authentication — useful in dev/training clusters). Modes in --authorization-mode are evaluated in order and the first ALLOW wins — AlwaysDeny exists precisely so you can append it as a final 'deny everything else' backstop after real modes like Node,RBAC.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authorization/" target="_blank">Kubernetes Docs - Authorization</a>
**Tags:** k8s::kcna topic::rbac topic::security src::session

---

<!-- note:1793935100778 model:Many -->
**Domain:** Secrets - SA token link
**Question:** What is the relationship between the secret object and the service account in Kubernetes?
**Options:** A. The service account is used to authenticate the secret object.<br>B. The secret object is linked to the service account and stores the service account token.<br>C. The service account is linked to the secret object and stores the API server endpoint.<br>D. The secret object is used to authenticate the service account.
**Answer:** B (2) – the secret object is linked to the service account and stores the service account token
**Explanation:** LEGACY model (pre-1.24, and still true for manually created token secrets): an SA's token lived in a Secret of type kubernetes.io/service-account-token — the Secret was linked to the SA (via annotation kubernetes.io/service-account.name) and stored its JWT, which pods mounted at /var/run/secrets/kubernetes.io/serviceaccount/. The Secret doesn't authenticate the SA — the SA IS the identity, the token just proves it; and the SA doesn't store the API endpoint (that's kubeconfig's job). MODERN model (1.24+): NO Secret is created — pods get short-lived audience/time/object-bound tokens via the TokenRequest API in a projected volume. That's why YOUR cluster lists SAs but no matching secrets: kubectl get secrets shows nothing of type service-account-token on a post-1.24 cluster.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/secret/" target="_blank">Kubernetes Docs - Secrets</a><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/" target="_blank">Kubernetes Docs - Managing Service Accounts</a>
**Tags:** k8s::kcna topic::serviceaccounts topic::secrets topic::security src::session

---

<!-- note:1793994897834 model:Many -->
**Domain:** Authorization - concept
**Question:** After a request is authenticated, what does Kubernetes authorization decide?
**Options:** A. Whether the authenticated identity is allowed to perform the requested action on the requested resource<br>B. Who the caller is — their username and groups<br>C. Whether the connection to the API server is TLS-encrypted<br>D. Which node the pod should be scheduled onto
**Answer:** A (1) – whether the authenticated identity is allowed to perform the requested action on the requested resource
**Explanation:** Authorization answers WHAT an authenticated caller may do: for each API request it evaluates the caller's identity (user + groups) against the request's attributes — verb (get/list/create/update/delete…), resource type, namespace, API path — and returns allow, deny, or no-opinion. Deny-by-default: if NO authorizer approves the request it's rejected 403 Forbidden. Authentication already answered WHO upstream in the request pipeline; authorization is the permission gate before admission control and etcd.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authorization/" target="_blank">Kubernetes Docs - Authorization</a>
**Tags:** k8s::kcna topic::security topic::rbac src::session

---

<!-- note:1793994897835 model:Many -->
**Domain:** Authorization - vs authentication
**Question:** Which statement correctly contrasts authentication and authorization in Kubernetes?
**Options:** A. Authentication proves WHO the caller is; authorization decides WHAT that identity may do<br>B. Authentication decides permissions; authorization proves the caller's identity<br>C. They are the same pipeline stage with two names<br>D. Authorization only applies to pod-to-pod traffic, not API requests
**Answer:** A (1) – authentication proves WHO the caller is; authorization decides WHAT that identity may do
**Explanation:** Two separate pipeline stages with separate plugins. Authentication answers WHO: it turns a cert/token/password into an identity — username plus groups (cert CN→user, O→groups; SA→system:serviceaccount:<ns>:<name>). Authorization answers WHAT: given that identity + the request's verb/resource/namespace attributes, an authorizer (RBAC, Node, Webhook…) allows or denies. Key consequence: you can be fully authenticated and still completely denied — authenticated ≠ authorized. Common misconception: people treat them as one step; they're distinct stages, and RBAC bindings only matter AFTER authentication produces the identity they reference.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/controlling-access/" target="_blank">Kubernetes Docs - Controlling Access to the API</a>
**Tags:** k8s::kcna topic::security topic::authentication src::session

---

<!-- note:1793994897836 model:Many -->
**Domain:** Authorization - why
**Question:** Why does Kubernetes need authorization as a separate layer from authentication?
**Options:** A. Authenticated users need different permissions: admins get full access, developers get scoped-down rights, teams get namespace-limited access<br>B. Authentication is too slow, so authorization shortcuts it<br>C. Authorization is what encrypts Secrets at rest<br>D. The API server refuses to start without an authorization layer
**Answer:** A (1) – authenticated users need different permissions: admins get full access, developers get scoped-down rights, teams get namespace-limited access
**Explanation:** Authentication only answers 'are you who you claim' — without authorization, EVERY valid credential would have equal power over the cluster. Authorization implements least privilege: cluster admins need unrestricted access, developers need only their namespaces and workloads, CI bots need narrow verb sets. It's what lets one cluster safely serve many tenants/teams — the same API server, wildly different effective permissions per identity. Without it, a leaked developer kubeconfig = full cluster compromise.
**Sources:** <a href="https://kubernetes.io/docs/concepts/security/controlling-access/" target="_blank">Kubernetes Docs - Controlling Access to the API</a>
**Tags:** k8s::kcna topic::security topic::rbac src::session

---

<!-- note:1793994897837 model:Many -->
**Domain:** Authorization - Webhook
**Question:** What does Webhook authorization mode do?
**Options:** A. Makes a synchronous HTTP callout to an external service that returns the allow/deny verdict<br>B. Reads permission rules from a local JSON policy file on the API server<br>C. Checks the requesting kubelet's node client certificate<br>D. Evaluates Role and ClusterRole objects like RBAC does
**Answer:** A (1) – makes a synchronous HTTP callout to an external service that returns the allow/deny verdict
**Explanation:** Webhook mode delegates the authorization decision entirely: the API server sends a SubjectAccessReview (user, groups, verb, resource, namespace) to your external endpoint and BLOCKS until it responds with allowed/denied — you can run your own logic or use ecosystem solutions like Open Policy Agent. Current clusters can chain MULTIPLE webhooks with matchConditions and failurePolicy via the structured --authorization-config file (the modern replacement for scattered --authorization-webhook-* flags). The failurePolicy matters: if your webhook is down, the config decides whether requests fail open (NoOpinion → next authorizer) or closed (deny).
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authorization/" target="_blank">Kubernetes Docs - Authorization</a>
**Tags:** k8s::kcna topic::security topic::rbac topic::webhook src::session

---

<!-- note:1793994897838 model:Many -->
**Domain:** Authorization - AlwaysAllow
**Question:** What does AlwaysAllow authorization mode do — and when is it the default?
**Options:** A. Permits every request that passed authentication; it is the default when --authorization-mode is not set<br>B. Permits requests only from system:node identities<br>C. Denies every request except health checks<br>D. Delegates all decisions to an external webhook service
**Answer:** A (1) – permits every request that passed authentication; it is the default when --authorization-mode is not set
**Explanation:** AlwaysAllow is the 'no authorization' mode: any request that survived authentication is permitted — authentication becomes the only gate. It IS the default: if --authorization-mode isn't configured on the API server, AlwaysAllow applies (that's why fresh/kind/minikube clusters let your admin cert do anything). The docs warn explicitly: don't run it where the API server is reachable by clients you don't fully trust — every valid credential gets full power. It's for learning/testing clusters; real clusters set --authorization-mode=Node,RBAC (kubeadm default). Pairs with AlwaysDeny — together they bracket the authz spectrum.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authorization/" target="_blank">Kubernetes Docs - Authorization</a>
**Tags:** k8s::kcna topic::security topic::rbac src::session

---

<!-- note:1793994897839 model:Many -->
**Domain:** Authorization - mode ordering
**Question:** With --authorization-mode=Node,RBAC, how are requests evaluated?
**Options:** A. Evaluated in order; the first authorizer to return allow OR deny wins immediately; if ALL return no-opinion the request is denied<br>B. Every configured authorizer must approve the request<br>C. RBAC always gets the final say regardless of order<br>D. The order is randomized on each API server restart
**Answer:** A (1) – evaluated in order; the first authorizer to return allow OR deny wins immediately; if ALL return no-opinion the request is denied
**Explanation:** Each configured authorizer returns one of three verdicts: allow, deny, or no-opinion. The chain evaluates in --authorization-mode order and the FIRST definitive verdict (allow or deny) is returned immediately — later modes aren't consulted. If every mode abstains (no opinion), the request is DENIED with 403 — deny-by-default. The trap: AlwaysAllow/AlwaysDeny always have an opinion, so position is everything — --authorization-mode=AlwaysAllow,RBAC behaves identically to AlwaysAllow alone (RBAC never gets asked). That's why production uses Node,RBAC: kubelets get Node-authorized first, humans fall through to RBAC.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authorization/" target="_blank">Kubernetes Docs - Authorization</a>
**Tags:** k8s::kcna topic::security topic::rbac src::session

---

<!-- note:1793994897840 model:Many -->
**Domain:** Authorization - system:masters
**Question:** What is special about the system:masters group?
**Options:** A. A built-in group granting unrestricted API access that bypasses RBAC and Webhook authorization restrictions<br>B. A read-only group for monitoring tools<br>C. The group kubelets belong to for node authorization<br>D. A deprecated group kept only for backwards compatibility
**Answer:** A (1) – a built-in group granting unrestricted API access that bypasses RBAC and Webhook authorization restrictions
**Explanation:** system:masters is Kubernetes's break-glass group: any identity belonging to it gets full cluster-admin privileges regardless of what RBAC Roles/Bindings or webhooks say — authorization restrictions are bypassed entirely. That's why admin certs carry O=system:masters in their subject (the cert→group mapping you know) and why kubeadm's default admin kubeconfig works instantly. The docs warn against adding users to it: prefer a ClusterRoleBinding to the built-in cluster-admin ClusterRole instead — same power but visible/auditable in RBAC objects rather than a hidden group claim.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/authorization/" target="_blank">Kubernetes Docs - Authorization</a>
**Tags:** k8s::kcna topic::security topic::rbac topic::authentication src::session

---

<!-- note:1793994897843 model:Cloze -->
**Text:** ABAC authorization: permission policies live in a {{c1::JSON policy file}} passed to the API server via {{c2::--authorization-policy-file}}; changing them requires {{c3::editing the file and restarting the API server}} — the operational pain that made {{c4::RBAC}} the standard instead.
**Back Extra:** ABAC = Attribute-Based Access Control: policies combine user attributes + resource attributes + environment attributes into allow rules. It predates RBAC and lost because every policy change meant editing the file AND restarting the API server — no dynamic updates, no kubectl management. RBAC replaced it by making permissions Kubernetes API objects editable live. Avoid ABAC in new clusters.
**Tags:** k8s::kcna topic::security topic::rbac topic::abac src::session

---

<!-- note:1793995451562 model:Many -->
**Domain:** RBAC - Role apiVersion
**Question:** Which apiVersion/kind defines a namespaced RBAC Role?
**Options:** A. apiVersion: rbac.authorization.k8s.io/v1, kind: Role<br>B. apiVersion: v1, kind: Role<br>C. apiVersion: rbac.authorization.k8s.io/v1, kind: ClusterRole<br>D. apiVersion: apps/v1, kind: Role
**Answer:** A (1) – apiVersion: rbac.authorization.k8s.io/v1, kind: Role
**Explanation:** RBAC objects live in the rbac.authorization.k8s.io API group at v1: apiVersion: rbac.authorization.k8s.io/v1, kind: Role for namespaced roles (metadata.namespace required) or kind: ClusterRole for cluster-scoped ones (no namespace field — ClusterRoles can grant cluster-scoped resources like nodes, non-resource URLs like /healthz, and namespaced resources across ALL namespaces). Inside rules, apiGroups refers to the RESOURCE's API group — apiGroups: [""] means the core/v1 group (pods, secrets, configmaps…).
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna topic::rbac topic::security topic::yaml src::session

---

<!-- note:1793995451563 model:Many -->
**Domain:** RBAC - rules structure
**Question:** What three fields define what a Role rule permits?
**Options:** A. apiGroups, resources, and verbs<br>B. subjects, roleRef, and namespace<br>C. name, labels, and annotations<br>D. apiVersion, kind, and metadata
**Answer:** A (1) – apiGroups, resources, and verbs
**Explanation:** Each entry in spec.rules is one permission set with three required dimensions — apiGroups (which API group the resources belong to; [""] = core), resources (plural resource names like pods, secrets, or subresources like pods/log, pods/exec), and verbs (get, list, watch, create, update, patch, delete, deletecollection — plus special verbs impersonate, bind, escalate). A request must match ALL dimensions of a rule to be allowed; multiple rules union together (additive — consistent with RBAC having no deny). Optional fields: resourceNames (restrict to named instances) and nonResourceURLs (for /healthz-style endpoints, ClusterRole only).
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna topic::rbac topic::security topic::yaml src::session

---

<!-- note:1793995451564 model:Many -->
**Domain:** RBAC - linking
**Question:** What object links a user, group, or ServiceAccount to a Role's permissions?
**Options:** A. A RoleBinding (its subjects say WHO, its roleRef says WHAT)<br>B. A ClusterRole with a users field<br>C. An annotation on the user's kubeconfig<br>D. A LabelSelector on the Role object
**Answer:** A (1) – a RoleBinding (its subjects say WHO, its roleRef says WHAT)
**Explanation:** The RoleBinding is the link object: subjects[] lists WHO gets access (kind: User, Group, or ServiceAccount + name — names are case-sensitive) and roleRef points to WHAT they get (kind: Role or ClusterRole + name + apiGroup: rbac.authorization.k8s.io). A RoleBinding lives in a namespace and grants the role's permissions within THAT namespace only — even when roleRef points to a ClusterRole. ClusterRoleBinding is the cluster-wide variant. And remember roleRef is immutable — to change what a binding grants you delete and recreate it.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna topic::rbac topic::security topic::yaml src::session

---

<!-- note:1793995451565 model:Many -->
**Domain:** RBAC - namespace scope
**Question:** A RoleBinding in namespace 'dev' references a ClusterRole. Where do the permissions apply?
**Options:** A. Only within the 'dev' namespace — the RoleBinding's own namespace sets the scope<br>B. Cluster-wide, because ClusterRoles are cluster-scoped<br>C. Only to user 'jane', cluster-wide<br>D. Nowhere — ClusterRoles can't be bound by RoleBindings
**Answer:** A (1) – only within the 'dev' namespace — the RoleBinding's own namespace sets the scope
**Explanation:** The RoleBinding's metadata.namespace decides WHERE permissions apply — NOT the roleRef's scope. A RoleBinding in namespace 'dev' referencing a ClusterRole grants those ClusterRole permissions ONLY inside 'dev'. This is the doc's own pattern: define ClusterRoles once (secret-reader) and reuse them across namespaces by creating a RoleBinding per namespace — 'dave' bound in 'development' reads secrets only there, not cluster-wide. To grant across ALL namespaces you need a ClusterRoleBinding instead. Role (namespaced) + RoleBinding (same ns) is the tightest scope.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna topic::rbac topic::security topic::namespaces src::session

---

<!-- note:1793995451566 model:Many -->
**Domain:** RBAC - kubectl create
**Question:** Which kubectl command creates a Role granting get/list/watch on pods in namespace 'default'?
**Options:** A. kubectl create role pod-reader --verb=get,list,watch --resource=pods --namespace=default<br>B. kubectl create clusterrole pod-reader --verb=get --resource=pods<br>C. kubectl create rolebinding pod-reader --role=pod-reader --user=jane<br>D. kubectl auth can-i get pods --as jane
**Answer:** A (1) – kubectl create role pod-reader --verb=get,list,watch --resource=pods --namespace=default
**Explanation:** kubectl create role builds a Role imperatively: --verb (repeatable or comma-separated), --resource (plural names), --api-group, and --namespace. Its sibling kubectl create rolebinding links subjects to it: kubectl create rolebinding read-pods --role=pod-reader --user=jane -n default (also --group= and --serviceaccount=ns:name subjects). Equivalent declarative path: kubectl apply -f role.yaml. Verify the result with kubectl auth can-i or kubectl get role,rolebinding -n default.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_role/" target="_blank">Kubernetes Docs - kubectl create role</a>
**Tags:** k8s::kcna topic::rbac topic::kubectl src::session

---

<!-- note:1793995451567 model:Many -->
**Domain:** RBAC - auth can-i
**Question:** Which command checks whether user 'jane' can get pods in namespace 'default'?
**Options:** A. kubectl auth can-i get pods --as jane -n default<br>B. kubectl get rolebindings -n default<br>C. kubectl describe clusterrole pod-reader<br>D. kubectl auth reconcile jane
**Answer:** A (1) – kubectl auth can-i get pods --as jane -n default
**Explanation:** kubectl auth can-i performs a live SubjectAccessReview against the cluster's actual authorization chain — it answers 'could this identity do this?' without changing anything. Flags: --as=<user> simulates an identity, --as-group=<group> adds groups, -n/--namespace scopes it, and --list shows EVERYTHING the (simulated) identity can do. It's the debugging tool for 'why can't X do Y' — check the effective answer instead of reading bindings by hand. auth can-i also verifies your own permissions: kubectl auth can-i create deployments.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_can-i/" target="_blank">Kubernetes Docs - kubectl auth can-i</a>
**Tags:** k8s::kcna topic::rbac topic::kubectl src::session

---

<!-- note:1793995451568 model:Many -->
**Domain:** RBAC - impersonation
**Question:** How do you act as another user or group with kubectl?
**Options:** A. kubectl --as=alice --as-group=devs get pods<br>B. kubectl sudo get pods<br>C. kubectl config set-credentials alice --token=x<br>D. kubectl exec -it alice -- whoami
**Answer:** A (1) – kubectl --as=alice --as-group=devs get pods
**Explanation:** kubectl's --as and --as-group flags make the API server treat the request as a different identity — kubectl --as=alice --as-group=devs get pods acts AS alice in group devs. It only works if YOUR identity has the impersonate verb (RBAC grants it on users/groups/serviceaccounts resources — e.g. system:masters or an impersonator ClusterRole). This is how you test 'what would X see/do' safely. Combine with kubectl auth can-i --as for pure checks without executing the action. Related flags: --as-uid for service-account UIDs.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/user-impersonation/" target="_blank">Kubernetes Docs - User Impersonation</a>
**Tags:** k8s::kcna topic::rbac topic::kubectl src::session

---

<!-- note:1793995451569 model:Many -->
**Domain:** RBAC - resourceNames
**Question:** What does resourceNames do in a Role rule?
**Options:** A. It restricts the rule to specific named resource instances<br>B. It encrypts the named resources at rest<br>C. It assigns resource quotas to the role<br>D. It namespaces the rule to a single namespace
**Answer:** A (1) – it restricts the rule to specific named resource instances
**Explanation:** resourceNames narrows a rule from 'all pods' to named instances: resources: [configmaps], resourceNames: [my-configmap], verbs: [get, update] lets the subject touch ONLY that one ConfigMap. Hard limits (doc-verified): you CANNOT restrict top-level create (the name doesn't exist at authz time) or deletecollection by resourceName; list/watch restricted by resourceName require the client to send a matching field-selector (kubectl get configmaps --field-selector=metadata.name=my-configmap); it DOES work on subresources like pods/exec. An empty resourceNames list means everything is allowed.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna topic::rbac topic::security topic::yaml src::session

---

<!-- note:1793995451571 model:Cloze -->
**Text:** Minimal Role manifest (pod-reader in 'default'):<br><br><code>apiVersion: {{c1::rbac.authorization.k8s.io/v1}}<br>kind: {{c2::Role}}<br>metadata:<br>  namespace: {{c3::default}}<br>  name: pod-reader<br>rules:<br>- apiGroups: [{{c4::""}}]  # "" = core API group<br>  resources: [{{c5::pods}}]<br>  verbs: [{{c6::get, watch, list}}]</code>
**Back Extra:** rules is a LIST — each entry is one permission set where apiGroups + resources + verbs must all match a request. apiGroups: [""] = core/v1 resources. Multiple rules union (RBAC is additive — no deny). Verbs come from the API verb set; special verbs impersonate/bind/escalate gate RBAC-escalation itself. Same skeleton with kind: ClusterRole + no namespace grants cluster-wide.
**Tags:** k8s::kcna topic::rbac topic::yaml src::session

---

<!-- note:1793995451572 model:Cloze -->
**Text:** RoleBinding manifest linking user 'jane' to Role 'pod-reader':<br><br><code>apiVersion: {{c1::rbac.authorization.k8s.io/v1}}<br>kind: {{c2::RoleBinding}}<br>metadata:<br>  name: read-pods<br>  namespace: {{c3::default}}<br>subjects:<br>- kind: {{c4::User}}<br>  name: {{c5::jane}}<br>  apiGroup: rbac.authorization.k8s.io<br>roleRef:<br>  kind: {{c6::Role}}<br>  name: pod-reader<br>  apiGroup: rbac.authorization.k8s.io</code>
**Back Extra:** subjects = WHO gets it (kind User/Group/ServiceAccount + case-sensitive name + apiGroup); roleRef = WHAT (kind Role|ClusterRole + name + apiGroup — immutable, recreate to change). The binding's namespace sets scope: RoleBinding in 'dev' + ClusterRole ref = perms only in 'dev'. ClusterRoleBinding = cluster-wide. Create imperatively: kubectl create rolebinding read-pods --role=pod-reader --user=jane -n default.
**Tags:** k8s::kcna topic::rbac topic::yaml src::session

---

<!-- note:1794001609836 model:Many -->
**Domain:** ClusterRoles - cluster-scoped resources
**Question:** A Role in namespace 'prod' grants get/list/watch on 'nodes'. Why doesn't it work?
**Options:** A. Nodes are cluster-scoped — the rule must be in a ClusterRole bound by a ClusterRoleBinding<br>B. Nodes require resourceNames to be set<br>C. The apiGroup should be 'nodes' instead of ''<br>D. Roles cannot contain rules — only ClusterRoles can
**Answer:** A (1) – Nodes are cluster-scoped — the rule must be in a ClusterRole bound by a ClusterRoleBinding
**Explanation:** Cluster-scoped resources have no namespace, so namespaced RBAC can't reach them. kubectl api-resources --namespaced=false lists them: nodes, namespaces, persistentvolumes, clusterroles, storageclasses, CSRs and more. The doc is explicit: a nodes rule 'must be in a ClusterRole bound with a ClusterRoleBinding to be effective.' Role + RoleBinding only covers namespaced resources inside one namespace — for cluster-wide objects you need the Cluster* pair.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna topic::rbac topic::security src::session

---

<!-- note:1794001609837 model:Many -->
**Domain:** ClusterRoles - apiVersion
**Question:** Which apiVersion/kind defines a cluster-wide RBAC role?
**Options:** A. apiVersion: rbac.authorization.k8s.io/v1, kind: ClusterRole<br>B. apiVersion: v1, kind: ClusterRole<br>C. apiVersion: rbac.authorization.k8s.io/v1, kind: Role<br>D. apiVersion: rbac.authorization.k8s.io/v1, kind: ClusterRoleBinding
**Answer:** A (1) – apiVersion: rbac.authorization.k8s.io/v1, kind: ClusterRole
**Explanation:** ClusterRoles live in the same rbac.authorization.k8s.io/v1 API group as Role/RoleBinding/ClusterRoleBinding. kind: ClusterRole is cluster-scoped — metadata has NO namespace field (a Role requires one). A ClusterRole's rules can cover three things: cluster-scoped resources (nodes, namespaces, PVs), non-resource URLs (/healthz — via nonResourceURLs), and namespaced resources across ALL namespaces when bound cluster-wide. Note ClusterRoleBinding is the binding object — it links subjects to a role, it doesn't define permissions itself.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna topic::rbac topic::security topic::yaml src::session

---

<!-- note:1794001609838 model:Many -->
**Domain:** ClusterRoles - binding matrix
**Question:** Which statement about what bindings can reference is correct?
**Options:** A. A ClusterRoleBinding can only reference a ClusterRole; a RoleBinding can reference a Role or ClusterRole<br>B. A ClusterRoleBinding can reference Roles and ClusterRoles<br>C. A RoleBinding can only reference Roles<br>D. Bindings can reference any RBAC object
**Answer:** A (1) – A ClusterRoleBinding can only reference a ClusterRole; a RoleBinding can reference a Role or ClusterRole
**Explanation:** The scope matrix: RoleBinding→Role = permissions within the binding's namespace only. RoleBinding→ClusterRole = the ClusterRole's rules but ONLY inside that one namespace (the 'dave reads secrets in development' pattern — reuse one ClusterRole across namespaces). ClusterRoleBinding→ClusterRole = permissions across ALL namespaces plus cluster-scoped resources. ClusterRoleBinding→Role is invalid — a namespaced Role can't grant cluster-wide access. Memorize: binding type picks the SCOPE, roleRef.kind picks which role object.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna topic::rbac topic::security src::session

---

<!-- note:1794001609839 model:Many -->
**Domain:** ClusterRoles - default roles
**Question:** Which built-in ClusterRole grants unrestricted super-user access and is bound to system:masters?
**Options:** A. cluster-admin<br>B. admin<br>C. edit<br>D. view
**Answer:** A (1) – cluster-admin
**Explanation:** cluster-admin is the super-user ClusterRole — any action on any resource; bound to the system:masters group (the O= field in admin kubeconfigs). The other user-facing defaults are the namespace trio, intended for RoleBindings: admin = read/write most resources + manage roles/rolebindings in the namespace; edit = read/write most objects but no RBAC objects; view = read-only, no roles/rolebindings and NO Secrets. User-facing ClusterRoles support aggregation: label a ClusterRole rbac.authorization.k8s.io/aggregate-to-admin/edit/view to inject rules into the defaults.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna topic::rbac topic::security src::session

---

<!-- note:1794001609840 model:Many -->
**Domain:** ClusterRoles - admin edit view
**Question:** What is true about the default 'edit' ClusterRole?
**Options:** A. It allows reading Secrets and running Pods as any ServiceAccount in the namespace — a privilege-escalation path<br>B. It forbids access to Secrets entirely<br>C. It grants cluster-wide read/write access<br>D. It can modify RoleBindings
**Answer:** A (1) – It allows reading Secrets and running Pods as any ServiceAccount in the namespace — a privilege-escalation path
**Explanation:** Doc-verified distinctions: edit = read/write most objects in a namespace but NOT roles/rolebindings — yet it CAN access Secrets and run pods as any ServiceAccount, handing the user that SA's API access (escalation). view = read-only, and deliberately excludes Secrets because secret contents contain SA tokens → privesc. admin = edit + role/rolebinding management. None of the trio has a default binding — you create the RoleBinding yourself to grant them.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna topic::rbac topic::security src::session

---

<!-- note:1794001609841 model:Many -->
**Domain:** ClusterRoles - kubectl create
**Question:** Which commands create a ClusterRole 'node-admin' and bind group 'ops' to it cluster-wide?
**Options:** A. kubectl create clusterrole node-admin --verb=get,list,watch,create,update,patch,delete --resource=nodes ; kubectl create clusterrolebinding node-admin --clusterrole=node-admin --group=ops<br>B. kubectl create role node-admin --verb=get --resource=nodes ; kubectl create rolebinding node-admin --role=node-admin --group=ops<br>C. kubectl create clusterrolebinding node-admin --role=node-admin --group=ops<br>D. kubectl auth can-i create nodes --as ops
**Answer:** A (1) – kubectl create clusterrole node-admin --verb=... --resource=nodes ; kubectl create clusterrolebinding node-admin --clusterrole=node-admin --group=ops
**Explanation:** kubectl create clusterrole mirrors create role (--verb, --resource, --api-group — no namespace needed since it's cluster-scoped). kubectl create clusterrolebinding links subjects cluster-wide using --clusterrole= (NOT --role=) plus --user=, --group=, or --serviceaccount=ns:name subjects. Doc example: kubectl create clusterrolebinding root-cluster-admin-binding --clusterrole=cluster-admin --user=root. Inspect with kubectl get clusterrole,clusterrolebinding -o yaml.
**Sources:** <a href="https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/" target="_blank">Kubernetes Docs - kubectl create clusterrole / clusterrolebinding</a>
**Tags:** k8s::kcna topic::rbac topic::kubectl src::session

---

<!-- note:1794001609842 model:Many -->
**Domain:** ClusterRoles - nonResourceURLs
**Question:** How does a ClusterRole grant access to endpoints like /healthz or /metrics that aren't Kubernetes resources?
**Options:** A. With the nonResourceURLs field — e.g. nonResourceURLs: ["/healthz", "/healthz/*"] with verbs<br>B. By listing them under resources as "healthz"<br>C. Via a special apiGroup called "nonresource"<br>D. It can't — only admission webhooks reach those endpoints
**Answer:** A (1) – With the nonResourceURLs field — e.g. nonResourceURLs: ["/healthz", "/healthz/*"] with verbs
**Explanation:** nonResourceURLs is a ClusterRole-only rules field for API endpoints that aren't Kubernetes resources: /healthz, /metrics, /version, /api, /apis. Format: nonResourceURLs: ["/healthz", "/healthz/*"] with verbs — '*' works as a suffix glob. These rules only take effect in a ClusterRole bound by a ClusterRoleBinding. Listing 'healthz' under resources won't work — it's not a resource type at all.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna topic::rbac topic::security topic::api src::session

---

<!-- note:1794001609843 model:Many -->
**Domain:** ClusterRoles - system roles
**Question:** You manually edit the rules of the system:discovery ClusterRole. What happens?
**Options:** A. The API server overwrites your changes at startup via auto-reconciliation<br>B. Nothing — manual edits to ClusterRoles are permanent<br>C. The cluster breaks immediately<br>D. Your changes merge permanently with the defaults
**Answer:** A (1) – The API server overwrites your changes at startup via auto-reconciliation
**Explanation:** system:-prefixed ClusterRoles and ClusterRoleBindings are control-plane managed (labeled kubernetes.io/bootstrapping=rbac-defaults). At EVERY apiserver start it re-adds missing permissions and subjects — auto-reconciliation repairs accidental edits and picks up new permissions each Kubernetes release. Opt out per-object with annotation rbac.authorization.kubernetes.io/autoupdate: "false", but missing defaults can leave the cluster non-functional. Never hand-edit system: roles — extend them instead via aggregate-to-* labels on your own ClusterRoles.
**Sources:** <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/" target="_blank">Kubernetes Docs - Using RBAC Authorization</a>
**Tags:** k8s::kcna topic::rbac topic::security src::session

---

<!-- note:1794001609859 model:Cloze -->
**Text:** ClusterRole manifest granting full node management cluster-wide:<br><br><code>apiVersion: {{c1::rbac.authorization.k8s.io/v1}}<br>kind: {{c2::ClusterRole}}<br>metadata:<br>  name: node-admin<br>rules:<br>- apiGroups: [{{c3::""}}]<br>  resources: [{{c4::nodes}}]<br>  verbs: [{{c5::get, list, watch, create, update, patch, delete}}]</code>
**Back Extra:** No namespace field — ClusterRoles are cluster-scoped (Role requires metadata.namespace). nodes is a core-group resource so apiGroups: [""]. A ClusterRole alone grants nothing — it needs a ClusterRoleBinding to attach subjects. Same skeleton works for namespaces, persistentvolumes, clusterroles, storageclasses (all cluster-scoped).
**Tags:** k8s::kcna topic::rbac topic::yaml src::session

---

<!-- note:1794001609860 model:Cloze -->
**Text:** ClusterRoleBinding manifest granting group 'manager' secret read access in EVERY namespace:<br><br><code>apiVersion: {{c1::rbac.authorization.k8s.io/v1}}<br>kind: {{c2::ClusterRoleBinding}}<br>metadata:<br>  name: read-secrets-global<br>subjects:<br>- kind: {{c3::Group}}<br>  name: {{c4::manager}}<br>  apiGroup: rbac.authorization.k8s.io<br>roleRef:<br>  kind: {{c5::ClusterRole}}<br>  name: secret-reader<br>  apiGroup: rbac.authorization.k8s.io</code>
**Back Extra:** No namespace — the binding grants across ALL namespaces cluster-wide. roleRef.kind must be ClusterRole (can't point at a namespaced Role). roleRef is immutable — delete/recreate to change. subjects support User/Group/ServiceAccount kinds, names case-sensitive. Imperative equivalent: kubectl create clusterrolebinding read-secrets-global --clusterrole=secret-reader --group=manager.
**Tags:** k8s::kcna topic::rbac topic::yaml src::session

---
