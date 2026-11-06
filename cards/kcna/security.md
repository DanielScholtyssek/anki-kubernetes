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
