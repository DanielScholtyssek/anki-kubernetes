# CKA - Certified Kubernetes Administrator — Cluster Architecture, Installation & Configuration

> Deck: `CKA - Certified Kubernetes Administrator` · Group: `Cluster Architecture, Installation & Configuration` · Notes: 217 · Models: Basic, Basic (and reversed card), Cloze

<!-- note:1794496839221 model:Basic -->
**Front:** What happens to your application if the node it runs on fails?
**Back:** If the application only runs on that single node, it goes down. That is why applications run on a cluster of multiple nodes — the remaining nodes can take over the workload.
**Tags:** k8s::cka topic::architecture src::session

---

<!-- note:1794496839222 model:Basic -->
**Front:** What is the difference between a worker node and a control plane node?
**Back:** Worker nodes run the actual application containers. Control plane nodes run the components that manage the cluster (API server, etcd, scheduler, controller-manager) and do not normally run user workloads.
**Tags:** k8s::cka topic::architecture src::session

---

<!-- note:1794496839223 model:Basic -->
**Front:** Which Kubernetes components run on the control plane, and which run on every node?
**Back:** Control plane only: kube-apiserver, etcd, kube-scheduler, controller-manager (+ cloud-controller-manager for cloud-integrated control loops). Every node (control plane AND workers): kubelet, container runtime, AND kube-proxy — kube-proxy runs as a DaemonSet so every node gets service networking rules.
**Tags:** k8s::cka topic::architecture src::session

---

<!-- note:1794496839224 model:Basic -->
**Front:** You run kubectl get pods to inspect a cluster. Which component receives and answers the request?
**Back:** kube-apiserver<br><br>The API server is the cluster's frontend: kubectl and every other client (and the cluster's own components) send requests to it. etcd only stores the data the API server reads, the scheduler places new workloads, and kubelets manage containers on their own node.
**Tags:** k8s::cka topic::architecture src::session

---

<!-- note:1794496839225 model:Basic -->
**Front:** Why can an image built by Docker run on other runtimes like containerd?
**Back:** Because both adhere to OCI standards: the image follows the image-spec format, and any runtime following the runtime-spec knows how to run it. This is what makes container images portable across different tools and runtimes.
**Tags:** k8s::cka topic::cri-oci src::session

---

<!-- note:1794496839226 model:Basic -->
**Front:** Which interface must a container runtime implement so that the kubelet can use it interchangeably with other runtimes?
**Back:** Container Runtime Interface (CRI)<br><br>The OCI image-spec and runtime-spec standardize the image format and how a container is run — they are rules a runtime follows, not an interface k8s calls. CRI is the actual gRPC interface the kubelet uses to talk to the runtime, which is what makes runtimes swappable.
**Tags:** k8s::cka topic::cri-oci src::session

---

<!-- note:1794496839227 model:Basic -->
**Front:** Which OCI specification defines the format of a container image — its manifest, configuration, and filesystem layers?
**Back:** image-spec<br><br>image-spec covers the packaging side — manifest, config, filesystem layers. runtime-spec covers the running side — container config and lifecycle. CRI is the kubelet interface, and distribution-spec covers pushing/pulling images to a registry.
**Tags:** k8s::cka topic::cri-oci src::session

---

<!-- note:1794496839248 model:Basic -->
**Front:** What is a container?
**Back:** A completely isolated environment that runs its own processes or services and has its own network interfaces and filesystem mounts — while sharing the host machine's OS kernel with all other containers.
**Tags:** k8s::cka topic::docker src::session

---

<!-- note:1794496839249 model:Basic -->
**Front:** Which stack correctly describes how containers run compared to virtual machines?
**Back:** HW → OS → Docker Engine → containers that share the host OS kernel<br><br>Virtual machines sit on a hypervisor and each boots a full guest OS with its own kernel — heavyweight and slow to start. Containers need no guest OS: the Docker engine uses the host kernel (namespaces/cgroups) to give each container its own isolated processes, networking and filesystems on the same machine — much lighter and faster.
**Tags:** k8s::cka topic::docker src::session

---

<!-- note:1794496839250 model:Basic -->
**Front:** What is the difference between a container and an image?
**Back:** An image is a package — a read-only template containing the application and everything it needs to run. It is the blueprint used to create one or more containers. A container is a running instance of an image: the isolated environment with its own processes, network interfaces and filesystem.
**Tags:** k8s::cka topic::docker src::session

---

<!-- note:1794496839298 model:Basic -->
**Front:** What does the <code>apiVersion</code> field in a manifest specify, and how does it map to core vs named API groups?
**Back:** <code>apiVersion</code> names which version of the Kubernetes API is used to create the object, written <code>&lt;group&gt;/&lt;version&gt;</code> for named API groups or just <code>&lt;version&gt;</code> for the core group (which has no name). So <code>apiVersion: v1</code> = core API group (Pod, Service); <code>apiVersion: apps/v1</code> = named group 'apps', version v1 (Deployment, ReplicaSet); <code>batch/v1</code> = group 'batch' (Job).
**Tags:** k8s::cka topic::api topic::yaml src::session

---

<!-- note:1794496839302 model:Basic -->
**Front:** Which of these is NOT one of the four required top-level fields of a Kubernetes manifest?
**Back:** status<br><br>The four required top-level fields are apiVersion, kind, metadata and spec. status does exist on live objects, but it is supplied and updated by the Kubernetes control plane to record the object's current state — you never write it into the manifest you submit.
**Tags:** k8s::cka topic::api topic::yaml src::session

---

<!-- note:1794496839303 model:Basic -->
**Front:** A manifest starts with <code>apiVersion: apps/v1</code>. What does this value encode?
**Back:** The named API group 'apps', version v1<br><br>apiVersion encodes <group>/<version> for named API groups and just <version> (v1) for the core API group, which has no name. 'apps' is the named group that holds Deployments, ReplicaSets, StatefulSets and DaemonSets; core-group kinds like Pod and Service use plain apiVersion: v1. It selects the API endpoint — it has nothing to do with application versioning.
**Tags:** k8s::cka topic::api topic::yaml src::session

---

<!-- note:1794496839305 model:Basic -->
**Front:** Which of these components runs ONLY on control-plane nodes, not on worker nodes?
**Back:** kube-apiserver<br><br>kube-apiserver, etcd, kube-scheduler and kube-controller-manager run only on control-plane nodes — they manage the cluster. kubelet, kube-proxy and the container runtime run on every node (workers AND control plane) so any node can host pods.
**Tags:** k8s::cka src::session topic::architecture topic::control-plane

---

<!-- note:1794496839306 model:Basic -->
**Front:** What is the difference between a control-plane node and a worker node in Kubernetes?
**Back:** Control-plane nodes run the cluster's management components — kube-apiserver, etcd, kube-scheduler, kube-controller-manager — and normally run no user workloads (protected by a taint). Worker nodes run the application pods: each has kubelet, kube-proxy and a container runtime. Every node needs the per-node components; only control-plane nodes need the management stack.
**Tags:** k8s::cka src::session topic::architecture topic::control-plane

---

<!-- note:1794496839307 model:Basic -->
**Front:** What is the role of etcd in a Kubernetes cluster?
**Back:** All of the options are correct<br><br>Per the course framing, all three describe etcd: it stores ALL data used to manage the cluster (D), it keeps that data as distributed replicated storage so control-plane nodes share one consistent view (B), and its distributed consensus — leader election/quorum via Raft, described as 'locks' — prevents conflicting writes between the masters (A). Nuance for the real world: etcd members run only on control-plane nodes ('all nodes' is loose phrasing for the etcd members), and 'locks' really means Raft consensus, not literal locking.
**Tags:** k8s::cka src::session topic::architecture topic::etcd

---

<!-- note:1794496839317 model:Basic -->
**Front:** Which statement correctly contrasts the imperative and declarative approaches?
**Back:** Imperative = you specify WHAT you want AND HOW (the steps); declarative = you specify only WHAT the result should be<br><br>Imperative: the operator encodes the path — every command/step explicitly. Declarative: the operator encodes the destination — the system derives the path (diff + reconcile). Kubernetes manifests+apply and Terraform are declarative; ad-hoc kubectl commands and shell scripts are imperative.
**Tags:** k8s::cka src::session topic::declarative topic::kubectl

---

<!-- note:1794496839319 model:Basic -->
**Front:** Which namespaces exist in a fresh Kubernetes cluster by default?
**Back:** default, kube-system, kube-public, kube-node-lease<br><br>Every cluster starts with four: 'default' (objects with no namespace set), 'kube-system' (the cluster's own infrastructure — CoreDNS, kube-proxy, control-plane pods in kubeadm clusters), 'kube-public' (publicly readable info, mostly unused), 'kube-node-lease' (node heartbeat Lease objects). Create your own for teams/apps via <code>kubectl create ns</code>
**Tags:** k8s::cka src::session topic::architecture topic::namespaces

---

<!-- note:1794496839320 model:Basic -->
**Front:** Which kubectl command makes 'dev' your DEFAULT namespace for all subsequent commands?
**Back:** <code>kubectl config set-context --current --namespace=dev</code><br><br>set-context <code>--current</code> <code>--namespace=dev</code> writes 'dev' into your kubeconfig's current context — every subsequent kubectl command defaults to it, no -n flag needed. The alternative is passing -n dev (or <code>--namespace=dev</code>) on each command. <code>kubectl get ns</code> lists namespaces; create ns makes one.
**Tags:** k8s::cka src::session topic::kubectl topic::namespaces

---

<!-- note:1794496839321 model:Basic -->
**Front:** Which of these resources is cluster-scoped — i.e. does NOT live inside a namespace?
**Back:** Node<br><br>Nodes, PersistentVolumes, ClusterRoles — and Namespaces themselves — are cluster-scoped: they live outside any namespace (metadata.namespace must be empty). Pods, Services, Deployments, Secrets, ConfigMaps are namespaced. Discover which is which with <code>kubectl api-resources --namespaced=true/false</code>
**Tags:** k8s::cka src::session topic::api topic::namespaces

---

<!-- note:1794496839322 model:Basic -->
**Front:** Do namespaces on their own provide hard isolation between workloads?
**Back:** No — namespaces are logical grouping; real isolation needs NetworkPolicy, RBAC and quotas on top<br><br>Namespaces partition names and org ownership — but the pod network stays flat by default: a pod in ns 'dev' can still reach a pod in ns 'prod'. Hard isolation is layered on: NetworkPolicies for traffic, RBAC for API access, ResourceQuota/LimitRange for resources. Namespaces are the boundary those features scope to, not the isolation itself.
**Tags:** k8s::cka src::session topic::namespaces topic::networking

---

<!-- note:1794496839324 model:Basic -->
**Front:** A pod in namespace 'dev' must reach the Service 'api' living in namespace 'prod'. Which DNS name works?
**Back:** api.prod.svc.cluster.local<br><br>Services are registered in CoreDNS as &lt;service&gt;.&lt;namespace&gt;.svc.cluster.local. The SHORT name (api) only resolves inside the caller's own namespace — a dev pod asking for 'api' gets dev's api (or NXDOMAIN). Cross-namespace calls need the namespace in the name: api.prod.svc.cluster.local.
**Tags:** k8s::cka src::session topic::dns topic::namespaces

---

<!-- note:1794496839353 model:Basic -->
**Front:** In a kubeadm cluster, how do kube-apiserver, etcd and friends actually run on the control-plane node?
**Back:** as static pods — kubelet runs them from manifests in /etc/kubernetes/manifests, no API server dependency<br><br>Kubeadm clusters bootstrap the control plane via static pods: manifests for kube-apiserver, etcd, kube-controller-manager and kube-scheduler sit in /etc/kubernetes/manifests and the kubelet runs them. Elegant because the control plane can't be hosted by the cluster it's bootstrapping — kubelet is the only piece that must exist first.
**Tags:** k8s::cka src::session topic::architecture topic::staticpods

---

<!-- note:1794496839365 model:Basic -->
**Front:** In which order does the kube-apiserver process an incoming request?
**Back:** TLS terminates first, then Authentication, Authorization, Admission Control, then the object persists to etcd<br><br>Every API request passes the same pipeline: transport security (TLS cert check) → Authentication (WHO are you — cert/token/service account) → Authorization (WHAT may you do — RBAC/ABAC/Node/Webhook) → Admission Control (mutate or reject writes, e.g. LimitRange injecting defaults, PSA). Note that admission only acts on create/update/delete/connect requests — pure reads skip it — and the object is only written to etcd after surviving all stages.
**Tags:** k8s::cka src::session topic::api topic::security

---

<!-- note:1794496839366 model:Basic -->
**Front:** Which mechanisms can authenticate a caller to the kube-apiserver? (Select all that apply)<br><br>A. X.509 client certificates signed by the cluster CA<br>B. ServiceAccount tokens (JWTs)<br>C. Static token or password file<br>D. External identity providers (OIDC, webhook, LDAP)<br>E. SSH keys
**Back:** A, B, C, D – client certs, ServiceAccount tokens, static token/password file, and external providers (OIDC/webhook/LDAP)<br><br>Authentication answers WHO can access the cluster. The API server supports client certificates signed by the cluster CA, bearer tokens (static token file, bootstrap tokens, ServiceAccount JWTs), basic password auth via a static file, and external providers (OIDC, authentication webhook — which bridges LDAP/other IdPs). Multiple modules can be configured and are tried in sequence until one succeeds. SSH keys secure access to the HOSTS, not the Kubernetes API.
**Tags:** k8s::cka src::session topic::api topic::security

---

<!-- note:1794496839367 model:Basic -->
**Front:** Which authorization modes can the kube-apiserver enforce? (Select all that apply)<br><br>A. RBAC — roles bound to users/groups/service accounts<br>B. ABAC — attribute-based access control policies<br>C. Node authorization — constrains kubelets to their own node's objects<br>D. Webhook — delegates the decision to an external service<br>E. OAuth — OAuth2 access tokens
**Back:** A, B, C, D – RBAC, ABAC, Node authorization, and Webhook mode<br><br>Authorization answers WHAT an authenticated caller may do. The API server can run multiple authorization modules: RBAC (role-based, the common one — Roles/ClusterRoles + bindings), ABAC (attribute-based policies on user/verb/resource), Node authorization (special mode that constrains what kubelets may read/write to the objects their node needs), and Webhook (delegates the decision to an external service). If several modules are configured, each is checked — the request proceeds if ANY module authorizes it.
**Tags:** k8s::cka src::session topic::rbac topic::security

---

<!-- note:1794496839368 model:Basic -->
**Front:** Which statement about encryption between Kubernetes components is TRUE?
**Back:** all control-plane component traffic plus client traffic to the apiserver is TLS-encrypted<br><br>TLS secures the entire control plane: kubectl/clients to kube-apiserver, apiserver to etcd, and apiserver's calls to kubelets, kube-proxy and the other components are all encrypted in transit (with a cluster CA — typically etcd, /etc/kubernetes/pki, issued by kubeadm or your own PKI). Plaintext is not a supported posture for API traffic; the 'insecure port' was removed entirely in Kubernetes 1.20.
**Tags:** k8s::cka src::session topic::control-plane topic::security

---

<!-- note:1794496839370 model:Basic -->
**Front:** In X.509 client-certificate authentication, how does Kubernetes map a certificate's subject to a user identity?
**Back:** the Common Name (CN) maps to the username and Organization (O) entries map to groups<br><br>Certificate attributes become identity: CN → username, each O → a group (order doesn't matter). So a cert with subject '/CN=alice/O=devs/O=ops' authenticates as user 'alice' in groups 'devs'+'ops' — plus everyone authentic'd also joins 'system:authenticated'. Signed by the cluster's client CA, the identity is then passed to authorization (RBAC) for permission checks.
**Tags:** k8s::cka src::session topic::authentication topic::security topic::tls

---

<!-- note:1794496839371 model:Basic -->
**Front:** How does the static token file authentication method work?
**Back:** CSV rows of 'token,user,uid,"group1,group2"' served by the apiserver flag <code>--token-auth-file</code><br><br>The static token file is a CSV on the control-plane node passed via '--token-auth-file=/path/file.csv'; each row is token,user,uid,"groups". Callers present the token as 'Authorization: Bearer &lt;token&gt;'. It's simple but static — changing users means editing the file and restarting kube-apiserver, and tokens are plaintext on disk, so it's discouraged for production.
**Tags:** k8s::cka src::session topic::api topic::authentication topic::security

---

<!-- note:1794496839372 model:Basic -->
**Front:** What happens to an API request that presents NO credentials at all?
**Back:** unauthenticated calls map to system:anonymous / system:unauthenticated (401 if disabled)<br><br>Requests that pass no credentials don't automatically get rejected: if anonymous auth is enabled they become 'system:anonymous' in group 'system:unauthenticated' and RBAC decides if that identity may act (usually it can't). Disable with '--anonymous-auth=false' on kube-apiserver. Every request is thus either an authenticated identity (users get 'system:authenticated' added) or the anonymous identity.
**Tags:** k8s::cka src::session topic::api topic::authentication topic::security

---

<!-- note:1794496839373 model:Basic -->
**Front:** How can external identity systems like LDAP or Kerberos authenticate Kubernetes users? (Select all that apply)<br><br>A. LDAP via a built-in <code>--ldap-server</code> flag<br>B. An authenticating proxy that forwards identity headers<br>C. An authentication webhook (TokenReview API)<br>D. Kerberos tickets passed directly to the apiserver
**Back:** B, C – authenticating proxy or authentication webhook; native OIDC is the built-in IdP path<br><br>There is no native LDAP/Kerberos/SAML plugin: Kubernetes natively supports client certs, bearer tokens (incl. ServiceAccount JWTs), and OIDC. To reach LDAP/Kerberos/etc. you front the API with an authenticating proxy that maps headers to user identity, or use an authentication webhook — the apiserver calls your token-review service which returns the user info. OIDC (e.g. Dex/Keycloak/Entra) is the one external-identity mechanism the API server supports natively.
**Tags:** k8s::cka src::session topic::api topic::authentication topic::security

---

<!-- note:1794496839374 model:Basic -->
**Front:** After '<code>kubectl create serviceaccount jenkins</code>', what username does the API server assign that identity?
**Back:** <code>kubectl create serviceaccount jenkins</code> produces identity 'system:serviceaccount:&lt;namespace&gt;:jenkins'<br><br>ServiceAccounts ARE API objects — namespaced and creatable via kubectl or YAML (unlike normal users). Pods mount the SA's token, and in-cluster processes authenticate as 'system:serviceaccount:&lt;ns&gt;:&lt;name&gt;' in groups 'system:serviceaccounts' and 'system:serviceaccounts:&lt;ns&gt;'; the signed JWT also works for clients outside the cluster. Because SA tokens can be stored in Secrets, be careful who can read them.
**Tags:** k8s::cka src::session topic::authentication topic::security topic::serviceaccounts

---

<!-- note:1794496839375 model:Basic -->
**Front:** What is a Certificate Authority (CA) and what does it do?
**Back:** the trusted issuer that signs certificates; everything trusts certs it signs<br><br>A CA is the root of trust: it holds a key pair (ca.key private + ca.crt public cert). It validates CSRs and signs them with ca.key — the signature is what makes a certificate trustworthy. Every client/server carries a copy of ca.crt and accepts any cert signed by that CA. In a cluster the CA is how all components verify each other's identity; keep ca.key private on the signing host — whoever has it can mint identities.
**Tags:** k8s::cka src::session topic::certificates topic::security topic::tls

---

<!-- note:1794496839376 model:Basic -->
**Front:** To mint a cluster-admin user cert for kubectl access, what must the certificate subject contain?
**Back:** the O (Organization) field carries group membership; O=system:masters grants cluster-admin<br><br>Groups come from the cert's O field — 'openssl req -subj "/CN=kube-admin/O=system:masters"' makes an identity that authenticates as user 'kube-admin' in group 'system:masters'. system:masters is bound to the cluster-admin ClusterRole out of the box, which is what actually grants full control — the cert just proves membership.
**Tags:** k8s::cka src::session topic::certificates topic::rbac topic::security topic::tls

---

<!-- note:1794496839377 model:Basic -->
**Front:** Which identity mappings do Kubernetes component certificates require? (Select all that apply)<br><br>A. kube-proxy cert must carry <code>CN=system:kube-proxy</code><br>B. Each kubelet cert must carry <code>CN=system:node:&lt;nodename&gt;</code> with <code>O=system:nodes</code><br>C. Admin users need <code>O=system:masters</code> in their cert<br>D. Any CN works — RBAC ignores certificate subjects
**Back:** A, B, C – <code>system:kube-proxy</code> for kube-proxy, <code>system:node:&lt;nodename&gt;</code>+<code>O=system:nodes</code> for each kubelet, <code>O=system:masters</code> for admin users<br><br>Component identities are fixed names the control plane expects: kube-proxy authenticates as <code>system:kube-proxy</code> (CN), each kubelet as <code>system:node:&lt;nodeName&gt;</code> (CN) plus group <code>system:nodes</code> (O) — Node authorizer relies on that mapping; an admin user is 'kube-admin' (or any CN) in group <code>system:masters</code>. Certificates without the right CN/O authenticate as someone else entirely and get rejected by authorization.
**Tags:** k8s::cka src::session topic::certificates topic::control-plane topic::security topic::tls

---

<!-- note:1794496839378 model:Basic -->
**Front:** Why does the kube-apiserver certificate need an openssl.cnf with an [alt_names] section?
**Back:** SANs let one cert be valid for every name/IP clients dial the apiserver by (kubernetes, .svc FQDNs, internal + external IPs)<br><br>The apiserver is reachable under several names: the 'kubernetes' Service name (kubernetes, kubernetes.default, kubernetes.default.svc, kubernetes.default.svc.cluster.local), plus node/public IPs. TLS hostname verification fails if the dialed name isn't in the cert — so the openssl.cnf used to generate the apiserver cert carries an [alt_names] section listing every DNS name and IP (internal + external) that will reach it.
**Tags:** k8s::cka src::session topic::api topic::certificates topic::security topic::tls

---

<!-- note:1794496839379 model:Basic -->
**Front:** How is TLS handled between etcd cluster members?
**Back:** etcd members authenticate each other with peer certificates; apiserver↔etcd uses client certs, all configured via etcd flags<br><br>etcd runs its own PKI within the cluster's: member-to-member (peer) traffic uses <code>--peer-cert-file</code>/<code>--peer-key-file</code>/<code>--peer-trusted-ca-file</code>, and clients (kube-apiserver) use <code>--cert-file</code>/<code>--key-file</code>/<code>--trusted-ca-file</code>. These paths are set in the etcd static pod manifest (/etc/kubernetes/manifests/etcd.yaml on kubeadm) — usually under /etc/kubernetes/pki/etcd/.
**Tags:** k8s::cka src::session topic::certificates topic::etcd topic::security topic::tls

---

<!-- note:1794496839380 model:Basic -->
**Front:** Who needs the CA certificate, and who needs the CA private key?
**Back:** everyone gets a COPY of the CA certificate to verify peers; ca.key never leaves the signing host<br><br>Verification is asymmetric: to trust a peer's certificate you only need the CA's public cert — so ca.crt is distributed to every node, component config, and kubeconfig (certificate-authority field). The ca.key is what mints identities, so it stays private on the control-plane/signing host: whoever holds it can forge any identity in the cluster.
**Tags:** k8s::cka src::session topic::certificates topic::security topic::tls

---

<!-- note:1794496839381 model:Basic -->
**Front:** How does each kubelet authenticate to the kube-apiserver?
**Back:** a per-node client cert with <code>CN=system:node:&lt;nodeName&gt;</code> and <code>O=system:nodes</code>, unique to that machine<br><br>Every kubelet talks to the apiserver as its OWN node identity: the client cert's CN must be <code>system:node:&lt;nodeName&gt;</code> and <code>O=system:nodes</code> — one cert per node, minted with that node's name. kubeadm keeps it under <code>/var/lib/kubelet/pki/</code> and references it in <code>kubelet.conf</code>; with TLS bootstrap the kubelet even requests the cert itself via the certificates.k8s.io CSR API using a bootstrap token.
**Tags:** k8s::cka src::session topic::control-plane topic::security topic::tls

---

<!-- note:1794496839382 model:Basic -->
**Front:** What ties a kubelet's access to only its own node's objects?
**Back:** Node authorization uses the cert's <code>system:node:&lt;name&gt;</code> to restrict each kubelet to objects belonging to its own node<br><br>The Node authorizer + NodeRestriction admission gate kubelet requests against the node name baked into its cert: 'system:node:worker-2' may only read pods scheduled to worker-2 and update its own node/secrets — it cannot list other nodes' pods or secrets. The name match is why node certs are per-node: a stolen kubelet cert only grants that one node's reach.
**Tags:** k8s::cka src::session topic::rbac topic::security

---

<!-- note:1794496839387 model:Basic -->
**Front:** Why use certificates between services?
**Back:** encrypt + authenticate (TLS/mTLS)<br><br>Certificates between services buy TWO things at once: encryption in transit (pod-to-pod traffic crosses node networks where cleartext HTTP would expose credentials and data) AND identity verification — with mTLS BOTH sides present certs, so each service proves who it is, not just that the channel is private. That's the security layer service meshes like Istio/Linkerd automate at scale. The distractors are nonsense or other systems' jobs: certificates don't speed anything up (mTLS costs CPU for handshake/crypto), DNS is CoreDNS, and restart behavior belongs to liveness probes and controllers.
**Tags:** k8s::cka src::session topic::mtls topic::security topic::tls

---

<!-- note:1794496839389 model:Basic -->
**Front:** Kubernetes RBAC "deny" behavior:
**Back:** RBAC is additive; reduce access by removing or narrowing bindings/roles<br><br>RBAC has NO deny mechanism: there is no 'deny' verb, a Role cannot express 'allow everything except X', and an empty Role grants nothing rather than cancelling other grants. Permissions only accumulate — effective access is the UNION of every Role/ClusterRole bound to you (and across authz modes, an allow from ANY enabled mode wins). Wildcards (*) in rules only expand grants, never subtract. The only ways to reduce someone's access are removing the RoleBinding/ClusterRoleBinding, or editing the Role's rules to narrow verbs/resources. This differs from firewalls/SELinux where explicit deny rules exist — RBAC can't do default-deny-with-exceptions.
**Tags:** k8s::cka src::session topic::rbac topic::security

---

<!-- note:1794496839390 model:Basic -->
**Front:** Which setting prevents a Pod from auto-mounting a ServiceAccount token?
**Back:** automountServiceAccountToken: false<br><br>Every pod gets a ServiceAccount token auto-mounted at /var/run/secrets/kubernetes.io/serviceaccount/ — a projected volume holding the SA's JWT plus the cluster CA cert — because the default is automountServiceAccountToken: true. Setting it false (on the pod spec or on the ServiceAccount itself) skips the mount entirely. It exists for least privilege: any process in the pod can read that token and authenticate to the API server AS that ServiceAccount, so mounting it everywhere means every container carries a live credential it may never need — a stolen token = stolen API access. Pods that don't call the K8s API shouldn't get one; pair it with an RBAC-scoped SA so even mounted tokens can only do what's needed. Distractors: runAsNonRoot and readOnlyRootFilesystem are pod securityContext hardening (UID/filesystem), and serviceAccountName only selects WHICH account — an empty value still mounts the default SA's token.
**Tags:** k8s::cka src::session topic::pods topic::security topic::serviceaccounts

---

<!-- note:1794496839392 model:Basic -->
**Front:** Why use a kubeconfig file instead of passing --server, --client-key, --client-certificate, --certificate-authority to every kubectl command?
**Back:** the kubeconfig stores cluster address + auth material once; kubectl reads it automatically<br><br>The flags DO exist and work per-command — kubectl accepts --server, --client-key, --client-certificate, --certificate-authority, --token etc. on every invocation — but repeating the server URL and credential paths on every call is impractical. The kubeconfig file (default ~/./.kube/config) stores named clusters, users, and contexts once, and kubectl loads it automatically. When both are present, command-line flags still win over file values (flag > kubeconfig precedence). The KUBECONFIG env var points kubectl at a different file or a list of files to merge.
**Tags:** k8s::cka src::session topic::kubeconfig topic::kubectl

---

<!-- note:1794496839393 model:Basic -->
**Front:** In a kubeconfig file, which element groups a cluster, user, and namespace under one switchable name?
**Back:** context<br><br>A context is the convenience binding: it groups three parameters under one switchable name — cluster (WHERE: server URL + CA trust material like certificate-authority or certificate-authority-data, or insecure-skip-tls-verify), user (WHO: client-certificate+client-key, token, username/password, or exec credential plugins), and namespace (default namespace for that pairing). The current-context field selects which context kubectl uses; kubectl config use-context switches it. This is why one kubeconfig can hold many clusters/users — you switch contexts instead of editing flags.
**Tags:** k8s::cka src::session topic::kubeconfig topic::kubectl

---

<!-- note:1794496839394 model:Basic -->
**Front:** Which command switches kubectl to a different context?
**Back:** kubectl config use-context <name><br><br>kubectl config use-context <name> sets current-context — the * in get-contexts output moves to that context. The family: get-contexts lists all contexts (* = current), current-context prints just the active name, set-context creates or edits a context's cluster/user/namespace fields, and kubectl config unset contexts.<name> deletes one. To change only the namespace of the current context: kubectl config set-context --current --namespace=<ns>. View the whole merged file with kubectl config view.
**Tags:** k8s::cka src::session topic::kubeconfig topic::kubectl

---

<!-- note:1794496839395 model:Basic -->
**Front:** Where does kubectl get the default namespace for namespaced resources?
**Back:** the namespace field of the current context (falls back to "default" if unset)<br><br>Namespace is a property of the CONTEXT, not the cluster or the user — each context can pin a different namespace, so switching contexts can silently change your default namespace. If the context has no namespace field, kubectl uses "default". A per-command --namespace flag always overrides the context's value for that invocation. The same pattern applies to identity: the user kubectl authenticates as comes from the context's user field unless --user is passed.
**Tags:** k8s::cka src::session topic::kubeconfig topic::kubectl topic::namespaces

---

<!-- note:1794496839396 model:Basic -->
**Front:** What are the top-level sections of a kubeconfig file (kind: Config)?
**Back:** apiVersion: v1 / kind: Config, then three named lists plus current-context. clusters: WHERE — each has name + server URL + trust material (certificate-authority file, certificate-authority-data base64, or insecure-skip-tls-verify: true, optional proxy-url). users: WHO — name + auth material (client-certificate + client-key, token, username + password, auth-provider, or exec credential plugins). contexts: the binding — name + cluster + user + optional namespace. current-context: which context kubectl uses by default. preferences: {} is normally empty. kubectl config view prints the effective (possibly merged) file.
**Tags:** k8s::cka src::session topic::kubeconfig topic::kubectl topic::yaml

---

<!-- note:1794496839397 model:Basic -->
**Front:** How do the core API group and named API groups differ?
**Back:** core serves at /api/v1 with apiVersion: v1; named groups at /apis/$GROUP/$VERSION with apiVersion: $GROUP/$VERSION<br><br>Every object declares group+version in its apiVersion field, which mirrors the REST path. The core (legacy) group is /api/v1 and is written as just apiVersion: v1 — no group name, because it's the original unnamed group holding pods, services, namespaces, nodes, secrets… Named groups live at /apis/<group>/<version> and write apiVersion: <group>/<version> — apps/v1 → /apis/apps/v1, networking.k8s.io/v1 → /apis/networking.k8s.io/v1, batch/v1 → /apis/batch/v1. Named groups exist so the API can grow: new features land in named groups without destabilizing the stable core API.
**Tags:** k8s::cka src::session topic::api topic::yaml

---

<!-- note:1794496839398 model:Basic -->
**Front:** Which resources are served by the core v1 API group? (Select all that apply)<br><br>A. Pods<br>B. Namespaces<br>C. Nodes<br>D. Events<br>E. Endpoints<br>F. Secrets<br>G. Deployments<br>H. NetworkPolicies<br>I. CronJobs<br>J. ClusterRoles
**Back:** A, B, C, D, E, F – Pods, Namespaces, Nodes, Events, Endpoints, Secrets<br><br>The core v1 group holds the ORIGINAL API: pods, services, namespaces, nodes, configmaps, secrets, serviceaccounts, endpoints, events, persistentvolumes/claims, resourcequotas, limitranges, replicationcontrollers, podtemplates. Everything newer lives in named groups — Deployments/StatefulSets/DaemonSets/ReplicaSets → apps/v1; Jobs/CronJobs → batch/v1; Ingresses/NetworkPolicies → networking.k8s.io/v1; Roles/ClusterRoles → rbac.authorization.k8s.io/v1; StorageClasses → storage.k8s.io/v1; CRDs → apiextensions.k8s.io/v1. Rule of thumb: apiVersion: v1 (bare) = core group.
**Tags:** k8s::cka src::session topic::api topic::resources

---

<!-- note:1794496839400 model:Basic -->
**Front:** Which of these are valid Kubernetes API verbs? (Select all that apply)<br><br>A. get<br>B. list<br>C. watch<br>D. create<br>E. update<br>F. patch<br>G. delete<br>H. deletecollection<br>I. read<br>J. write<br>K. query<br>L. fetch
**Back:** A, B, C, D, E, F, G, H – get, list, watch, create, update, patch, delete, deletecollection<br><br>Verbs are the actions the API server exposes on resources: get, list, watch (reads) and create, update, patch, delete, deletecollection (writes) — these are exactly what RBAC rules grant per resource. They map to HTTP methods: GET → get/list/watch, POST → create, PUT → update, PATCH → patch, DELETE → delete. Extra RBAC verbs exist for special cases: proxy, impersonate, bind, escalate. 'read', 'write', 'query', 'fetch' are NOT API verbs — generic programming words, not part of the API surface.
**Tags:** k8s::cka src::session topic::api topic::rbac

---

<!-- note:1794496839401 model:Basic -->
**Front:** What does kubectl proxy do?
**Back:** starts a localhost proxy to the API server using your kubeconfig credentials so you can hit the REST API directly<br><br>kubectl proxy runs a local proxy (default 127.0.0.1:8001; change with --port, --address, --accept-hosts) that forwards to the API server with your kubeconfig's TLS + auth already handled — so curl http://localhost:8001/api/v1/namespaces or /apis/apps/v1/deployments.default works with zero cert juggling. It's a debugging/exploration tool for the raw REST API. It is NOT pod port-forwarding (kubectl port-forward), NOT service-to-service traffic, and NOT etcd access.
**Tags:** k8s::cka src::session topic::api topic::kubectl

---

<!-- note:1794496839402 model:Basic -->
**Front:** Which kubectl command lists the API resources available on the cluster together with their API groups?
**Back:** kubectl api-resources<br><br>kubectl api-resources lists every resource on the cluster (deployments, pods, networkpolicies…) together with its API group/version, kind, and short names. kubectl api-versions lists only the group/version strings. For raw discovery endpoints, kubectl get --raw /apis or /api/v1 queries the same discovery API the server exposes. kubectl config view shows your kubeconfig — unrelated to cluster API discovery.
**Tags:** k8s::cka src::session topic::api topic::kubectl

---

<!-- note:1794496839403 model:Basic -->
**Front:** Which command would you use to see a full list of non-namespaced resources in Kubernetes?
**Back:** kubectl api-resources --namespaced=false<br><br>api-resources --namespaced=false filters the output to CLUSTER-scoped resources only — nodes, namespaces, persistentvolumes, clusterroles, storageclasses, priorityclasses… (things not bound to a namespace). --namespaced=true does the opposite (namespaced only). With no flag, api-resources shows everything and a NAMESPACED column tells you which is which. There is no --all flag on api-resources — that's kubectl get territory (-A/--all-namespaces). Other useful filters: --api-group=<group> and --verbs=<verb>.
**Tags:** k8s::cka src::session topic::api topic::kubectl

---

<!-- note:1794496839404 model:Basic -->
**Front:** Who is authorized by the node authorizers to make requests to kube-apiserver?
**Back:** requests from a user named system:node:<name> in the system:nodes group<br><br>The Node authorizer is a special mode built for kubelets: it only authorizes requests authenticated as system:node:<nodeName> belonging to group system:nodes — the identity kubelets get from their client certs (CN=system:node:<name>, O=system:nodes). It then scopes WHAT they may touch: pods bound to their node, node objects/status, mirrored EndpointSlices, leases, and CSRs for their node's certs — tightened further by NodeRestriction. It's identity-based, not role-based: cluster membership or OS admin rights mean nothing here; regular users are denied even though they're 'part of the cluster'. Runs alongside RBAC (--authorization-mode=Node,RBAC) — Node handles kubelet traffic, RBAC handles everything else.
**Tags:** k8s::cka src::session topic::kubelet topic::rbac topic::security

---

<!-- note:1794496839408 model:Basic -->
**Front:** What is the role of the node authoriser in Kubernetes cluster?
**Back:** handles requests from the kubelets on nodes to the kube-apiserver<br><br>The Node authorizer is a specialized authorization module that handles ONLY kubelet→apiserver requests: it verifies the caller is authenticated as system:node:<nodeName> in group system:nodes, then decides what that kubelet may read/write for its own node — pods bound to it, node objects/status, mirrored EndpointSlices, leases, and certificate-signing requests for its serving certs (tightened by NodeRestriction). Human users never pass through it — they go through RBAC/Webhook/etc. It doesn't deploy or manage nodes (that's the kubelet executing instructions, and cluster autoscaler/node lifecycle controllers), and it doesn't manage access policies generally — that's RBAC's job; Node,RBAC run side by side in --authorization-mode.
**Tags:** k8s::cka src::session topic::kubelet topic::rbac topic::security

---

<!-- note:1794496839411 model:Basic -->
**Front:** What are the characteristics of tokens generated by the Kubernetes Token Request API?
**Back:** audience bound, time bound, and object bound<br><br>TokenRequest API tokens (authentication.k8s.io/v1 — also what kubectl create token and projected serviceAccountToken volumes use) carry three bindings: AUDIENCE-bound — spec.audiences becomes the JWT aud claim; a recipient must match one of them or reject the token (default: the API server). TIME-bound — spec.expirationSeconds sets exp/nbf/iat claims; kubelet auto-rotates projected tokens before expiry (~80% of TTL, default ~1h). OBJECT-bound (optional) — spec.boundObjectRef embeds the target object's name+UID as private claims; the token only works while that object exists AND the request comes from it (Pod/Secret, Node since v1.33). 'Cluster bound' and 'namespace bound' aren't TokenRequest concepts — this API replaced the legacy never-expiring Secret-mounted SA tokens.
**Tags:** k8s::cka src::session topic::authentication topic::security topic::serviceaccounts

---

<!-- note:1794496839413 model:Basic -->
**Front:** What are the two sections of the RoleBinding object?
**Back:** Subjects and RoleRef<br><br>A RoleBinding has two functional sections: subjects — WHO gets the permissions (a list of kind: User/Group/ServiceAccount entries with name and namespace) — and roleRef — WHAT they get (a pointer with apiGroup, kind, and name referencing either a Role or a ClusterRole). roleRef is IMMUTABLE: you can't repoint an existing binding to a different role — delete and recreate it instead. A namespaced RoleBinding may reference a ClusterRole, but the granted permissions then apply only within the binding's namespace; ClusterRoleBinding is the cluster-wide variant with the same two fields.
**Tags:** k8s::cka src::session topic::rbac topic::security topic::yaml

---

<!-- note:1794496839415 model:Basic -->
**Front:** How do you make kubectl use a kubeconfig file other than the default ~/.kube/config?
**Back:** the --kubeconfig global flag on any kubectl command, or the KUBECONFIG environment variable<br><br>--kubeconfig is a GLOBAL kubectl flag — it goes before the subcommand: kubectl --kubeconfig=my-config get pods — and points kubectl at exactly one file (no merging). KUBECONFIG=my-config does the same via env var, and accepts a LIST of files that get merged (first-set wins per key). Precedence: --kubeconfig flag > KUBECONFIG env > default ~/.kube/config. The distractors fail because: 'use-context'/'config use' switch contexts WITHIN a file, not files; 'config view --kubeconfig=' and 'config edit --kubeconfig=' only display/edit that file — they don't make kubectl use it for commands; 'config switch' isn't a real subcommand.
**Tags:** k8s::cka src::session topic::kubeconfig topic::kubectl

---

<!-- note:1794496839416 model:Basic -->
**Front:** What is the behavior of the AlwaysDeny authorisation mode in Kubernetes?
**Back:** denies all requests<br><br>AlwaysDeny is an --authorization-mode that rejects EVERY API request with 403 Forbidden — yes, literally nothing works while it's the only/first effective mode: no reads, no writes, kubectl dead. It's not for production; it's a deliberate kill-switch and testing tool: emergency lockdown of a compromised or misbehaving cluster, negative testing (prove your RBAC actually blocks things — if requests still succeed under AlwaysDeny, something upstream is wrong), and mode-ordering experiments. Its opposite pole is AlwaysAllow (permits everything after authentication — useful in dev/training clusters). Modes in --authorization-mode are evaluated in order and the first ALLOW wins — AlwaysDeny exists precisely so you can append it as a final 'deny everything else' backstop after real modes like Node,RBAC.
**Tags:** k8s::cka src::session topic::rbac topic::security

---

<!-- note:1794496839418 model:Basic -->
**Front:** After a request is authenticated, what does Kubernetes authorization decide?
**Back:** whether the authenticated identity is allowed to perform the requested action on the requested resource<br><br>Authorization answers WHAT an authenticated caller may do: for each API request it evaluates the caller's identity (user + groups) against the request's attributes — verb (get/list/create/update/delete…), resource type, namespace, API path — and returns allow, deny, or no-opinion. Deny-by-default: if NO authorizer approves the request it's rejected 403 Forbidden. Authentication already answered WHO upstream in the request pipeline; authorization is the permission gate before admission control and etcd.
**Tags:** k8s::cka src::session topic::rbac topic::security

---

<!-- note:1794496839419 model:Basic -->
**Front:** Which statement correctly contrasts authentication and authorization in Kubernetes?
**Back:** authentication proves WHO the caller is; authorization decides WHAT that identity may do<br><br>Two separate pipeline stages with separate plugins. Authentication answers WHO: it turns a cert/token/password into an identity — username plus groups (cert CN→user, O→groups; SA→system:serviceaccount:<ns>:<name>). Authorization answers WHAT: given that identity + the request's verb/resource/namespace attributes, an authorizer (RBAC, Node, Webhook…) allows or denies. Key consequence: you can be fully authenticated and still completely denied — authenticated ≠ authorized. Common misconception: people treat them as one step; they're distinct stages, and RBAC bindings only matter AFTER authentication produces the identity they reference.
**Tags:** k8s::cka src::session topic::authentication topic::security

---

<!-- note:1794496839420 model:Basic -->
**Front:** Why does Kubernetes need authorization as a separate layer from authentication?
**Back:** authenticated users need different permissions: admins get full access, developers get scoped-down rights, teams get namespace-limited access<br><br>Authentication only answers 'are you who you claim' — without authorization, EVERY valid credential would have equal power over the cluster. Authorization implements least privilege: cluster admins need unrestricted access, developers need only their namespaces and workloads, CI bots need narrow verb sets. It's what lets one cluster safely serve many tenants/teams — the same API server, wildly different effective permissions per identity. Without it, a leaked developer kubeconfig = full cluster compromise.
**Tags:** k8s::cka src::session topic::rbac topic::security

---

<!-- note:1794496839421 model:Basic -->
**Front:** What does Webhook authorization mode do?
**Back:** makes a synchronous HTTP callout to an external service that returns the allow/deny verdict<br><br>Webhook mode delegates the authorization decision entirely: the API server sends a SubjectAccessReview (user, groups, verb, resource, namespace) to your external endpoint and BLOCKS until it responds with allowed/denied — you can run your own logic or use ecosystem solutions like Open Policy Agent. Current clusters can chain MULTIPLE webhooks with matchConditions and failurePolicy via the structured --authorization-config file (the modern replacement for scattered --authorization-webhook-* flags). The failurePolicy matters: if your webhook is down, the config decides whether requests fail open (NoOpinion → next authorizer) or closed (deny).
**Tags:** k8s::cka src::session topic::rbac topic::security topic::webhook

---

<!-- note:1794496839422 model:Basic -->
**Front:** What does AlwaysAllow authorization mode do — and when is it the default?
**Back:** permits every request that passed authentication; it is the default when --authorization-mode is not set<br><br>AlwaysAllow is the 'no authorization' mode: any request that survived authentication is permitted — authentication becomes the only gate. It IS the default: if --authorization-mode isn't configured on the API server, AlwaysAllow applies (that's why fresh/kind/minikube clusters let your admin cert do anything). The docs warn explicitly: don't run it where the API server is reachable by clients you don't fully trust — every valid credential gets full power. It's for learning/testing clusters; real clusters set --authorization-mode=Node,RBAC (kubeadm default). Pairs with AlwaysDeny — together they bracket the authz spectrum.
**Tags:** k8s::cka src::session topic::rbac topic::security

---

<!-- note:1794496839423 model:Basic -->
**Front:** With --authorization-mode=Node,RBAC, how are requests evaluated?
**Back:** evaluated in order; the first authorizer to return allow OR deny wins immediately; if ALL return no-opinion the request is denied<br><br>Each configured authorizer returns one of three verdicts: allow, deny, or no-opinion. The chain evaluates in --authorization-mode order and the FIRST definitive verdict (allow or deny) is returned immediately — later modes aren't consulted. If every mode abstains (no opinion), the request is DENIED with 403 — deny-by-default. The trap: AlwaysAllow/AlwaysDeny always have an opinion, so position is everything — --authorization-mode=AlwaysAllow,RBAC behaves identically to AlwaysAllow alone (RBAC never gets asked). That's why production uses Node,RBAC: kubelets get Node-authorized first, humans fall through to RBAC.
**Tags:** k8s::cka src::session topic::rbac topic::security

---

<!-- note:1794496839424 model:Basic -->
**Front:** What is special about the system:masters group?
**Back:** a built-in group granting unrestricted API access that bypasses RBAC and Webhook authorization restrictions<br><br>system:masters is Kubernetes's break-glass group: any identity belonging to it gets full cluster-admin privileges regardless of what RBAC Roles/Bindings or webhooks say — authorization restrictions are bypassed entirely. That's why admin certs carry O=system:masters in their subject (the cert→group mapping you know) and why kubeadm's default admin kubeconfig works instantly. The docs warn against adding users to it: prefer a ClusterRoleBinding to the built-in cluster-admin ClusterRole instead — same power but visible/auditable in RBAC objects rather than a hidden group claim.
**Tags:** k8s::cka src::session topic::authentication topic::rbac topic::security

---

<!-- note:1794496839425 model:Basic -->
**Front:** Which apiVersion/kind defines a namespaced RBAC Role?
**Back:** rbac.authorization.k8s.io/v1, kind Role<br><br>RBAC objects live in the rbac.authorization.k8s.io API group at v1: apiVersion: rbac.authorization.k8s.io/v1, kind: Role for namespaced roles (metadata.namespace required) or kind: ClusterRole for cluster-scoped ones (no namespace field — ClusterRoles can grant cluster-scoped resources like nodes, non-resource URLs like /healthz, and namespaced resources across ALL namespaces). Inside rules, apiGroups refers to the RESOURCE's API group — apiGroups: [""] means the core/v1 group (pods, secrets, configmaps…).
**Tags:** k8s::cka src::session topic::rbac topic::security topic::yaml

---

<!-- note:1794496839426 model:Basic -->
**Front:** What three fields define what a Role rule permits?
**Back:** apiGroups, resources, and verbs<br><br>Each entry in spec.rules is one permission set with three required dimensions — apiGroups (which API group the resources belong to; [""] = core), resources (plural resource names like pods, secrets, or subresources like pods/log, pods/exec), and verbs (get, list, watch, create, update, patch, delete, deletecollection — plus special verbs impersonate, bind, escalate). A request must match ALL dimensions of a rule to be allowed; multiple rules union together (additive — consistent with RBAC having no deny). Optional fields: resourceNames (restrict to named instances) and nonResourceURLs (for /healthz-style endpoints, ClusterRole only).
**Tags:** k8s::cka src::session topic::rbac topic::security topic::yaml

---

<!-- note:1794496839427 model:Basic -->
**Front:** What object links a user, group, or ServiceAccount to a Role's permissions?
**Back:** a RoleBinding (its subjects say WHO, its roleRef says WHAT)<br><br>The RoleBinding is the link object: subjects[] lists WHO gets access (kind: User, Group, or ServiceAccount + name — names are case-sensitive) and roleRef points to WHAT they get (kind: Role or ClusterRole + name + apiGroup: rbac.authorization.k8s.io). A RoleBinding lives in a namespace and grants the role's permissions within THAT namespace only — even when roleRef points to a ClusterRole. ClusterRoleBinding is the cluster-wide variant. And remember roleRef is immutable — to change what a binding grants you delete and recreate it.
**Tags:** k8s::cka src::session topic::rbac topic::security topic::yaml

---

<!-- note:1794496839428 model:Basic -->
**Front:** A RoleBinding in namespace 'dev' references a ClusterRole. Where do the permissions apply?
**Back:** only within the 'dev' namespace — the RoleBinding's own namespace sets the scope<br><br>The RoleBinding's metadata.namespace decides WHERE permissions apply — NOT the roleRef's scope. A RoleBinding in namespace 'dev' referencing a ClusterRole grants those ClusterRole permissions ONLY inside 'dev'. This is the doc's own pattern: define ClusterRoles once (secret-reader) and reuse them across namespaces by creating a RoleBinding per namespace — 'dave' bound in 'development' reads secrets only there, not cluster-wide. To grant across ALL namespaces you need a ClusterRoleBinding instead. Role (namespaced) + RoleBinding (same ns) is the tightest scope.
**Tags:** k8s::cka src::session topic::namespaces topic::rbac topic::security

---

<!-- note:1794496839429 model:Basic -->
**Front:** Which kubectl command creates a Role granting get/list/watch on pods in namespace 'default'?
**Back:** kubectl create role pod-reader --verb=get,list,watch --resource=pods --namespace=default<br><br>kubectl create role builds a Role imperatively: --verb (repeatable or comma-separated), --resource (plural names), --api-group, and --namespace. Its sibling kubectl create rolebinding links subjects to it: kubectl create rolebinding read-pods --role=pod-reader --user=jane -n default (also --group= and --serviceaccount=ns:name subjects). Equivalent declarative path: kubectl apply -f role.yaml. Verify the result with kubectl auth can-i or kubectl get role,rolebinding -n default.
**Tags:** k8s::cka src::session topic::kubectl topic::rbac

---

<!-- note:1794496839430 model:Basic -->
**Front:** Which command checks whether user 'jane' can get pods in namespace 'default'?
**Back:** kubectl auth can-i get pods --as jane -n default<br><br>kubectl auth can-i performs a live SubjectAccessReview against the cluster's actual authorization chain — it answers 'could this identity do this?' without changing anything. Flags: --as=<user> simulates an identity, --as-group=<group> adds groups, -n/--namespace scopes it, and --list shows EVERYTHING the (simulated) identity can do. It's the debugging tool for 'why can't X do Y' — check the effective answer instead of reading bindings by hand. auth can-i also verifies your own permissions: kubectl auth can-i create deployments.
**Tags:** k8s::cka src::session topic::kubectl topic::rbac

---

<!-- note:1794496839431 model:Basic -->
**Front:** How do you act as another user or group with kubectl?
**Back:** kubectl --as=alice --as-group=devs <command><br><br>kubectl's --as and --as-group flags make the API server treat the request as a different identity — kubectl --as=alice --as-group=devs get pods acts AS alice in group devs. It only works if YOUR identity has the impersonate verb (RBAC grants it on users/groups/serviceaccounts resources — e.g. system:masters or an impersonator ClusterRole). This is how you test 'what would X see/do' safely. Combine with kubectl auth can-i --as for pure checks without executing the action. Related flags: --as-uid for service-account UIDs.
**Tags:** k8s::cka src::session topic::kubectl topic::rbac

---

<!-- note:1794496839433 model:Basic -->
**Front:** A Role in namespace 'prod' grants get/list/watch on 'nodes'. Why doesn't it work?
**Back:** Nodes are cluster-scoped — the rule must be in a ClusterRole bound by a ClusterRoleBinding<br><br>Cluster-scoped resources have no namespace, so namespaced RBAC can't reach them. kubectl api-resources --namespaced=false lists them: nodes, namespaces, persistentvolumes, clusterroles, storageclasses, CSRs and more. The doc is explicit: a nodes rule 'must be in a ClusterRole bound with a ClusterRoleBinding to be effective.' Role + RoleBinding only covers namespaced resources inside one namespace — for cluster-wide objects you need the Cluster* pair.
**Tags:** k8s::cka src::session topic::rbac topic::security

---

<!-- note:1794496839434 model:Basic -->
**Front:** Which apiVersion/kind defines a cluster-wide RBAC role?
**Back:** apiVersion: rbac.authorization.k8s.io/v1, kind: ClusterRole<br><br>ClusterRoles live in the same rbac.authorization.k8s.io/v1 API group as Role/RoleBinding/ClusterRoleBinding. kind: ClusterRole is cluster-scoped — metadata has NO namespace field (a Role requires one). A ClusterRole's rules can cover three things: cluster-scoped resources (nodes, namespaces, PVs), non-resource URLs (/healthz — via nonResourceURLs), and namespaced resources across ALL namespaces when bound cluster-wide. Note ClusterRoleBinding is the binding object — it links subjects to a role, it doesn't define permissions itself.
**Tags:** k8s::cka src::session topic::rbac topic::security topic::yaml

---

<!-- note:1794496839435 model:Basic -->
**Front:** Which statement about what bindings can reference is correct?
**Back:** A ClusterRoleBinding can only reference a ClusterRole; a RoleBinding can reference a Role or ClusterRole<br><br>The scope matrix: RoleBinding→Role = permissions within the binding's namespace only. RoleBinding→ClusterRole = the ClusterRole's rules but ONLY inside that one namespace (the 'dave reads secrets in development' pattern — reuse one ClusterRole across namespaces). ClusterRoleBinding→ClusterRole = permissions across ALL namespaces plus cluster-scoped resources. ClusterRoleBinding→Role is invalid — a namespaced Role can't grant cluster-wide access. Memorize: binding type picks the SCOPE, roleRef.kind picks which role object.
**Tags:** k8s::cka src::session topic::rbac topic::security

---

<!-- note:1794496839436 model:Basic -->
**Front:** Which built-in ClusterRole grants unrestricted super-user access and is bound to system:masters?
**Back:** cluster-admin<br><br>cluster-admin is the super-user ClusterRole — any action on any resource; bound to the system:masters group (the O= field in admin kubeconfigs). The other user-facing defaults are the namespace trio, intended for RoleBindings: admin = read/write most resources + manage roles/rolebindings in the namespace; edit = read/write most objects but no RBAC objects; view = read-only, no roles/rolebindings and NO Secrets. User-facing ClusterRoles support aggregation: label a ClusterRole rbac.authorization.k8s.io/aggregate-to-admin/edit/view to inject rules into the defaults.
**Tags:** k8s::cka src::session topic::rbac topic::security

---

<!-- note:1794496839437 model:Basic -->
**Front:** What is true about the default 'edit' ClusterRole?
**Back:** It allows reading Secrets and running Pods as any ServiceAccount in the namespace — a privilege-escalation path<br><br>Doc-verified distinctions: edit = read/write most objects in a namespace but NOT roles/rolebindings — yet it CAN access Secrets and run pods as any ServiceAccount, handing the user that SA's API access (escalation). view = read-only, and deliberately excludes Secrets because secret contents contain SA tokens → privesc. admin = edit + role/rolebinding management. None of the trio has a default binding — you create the RoleBinding yourself to grant them.
**Tags:** k8s::cka src::session topic::rbac topic::security

---

<!-- note:1794496839438 model:Basic -->
**Front:** Which commands create a ClusterRole 'node-admin' and bind group 'ops' to it cluster-wide?
**Back:** kubectl create clusterrole node-admin --verb=... --resource=nodes ; kubectl create clusterrolebinding node-admin --clusterrole=node-admin --group=ops<br><br>kubectl create clusterrole mirrors create role (--verb, --resource, --api-group — no namespace needed since it's cluster-scoped). kubectl create clusterrolebinding links subjects cluster-wide using --clusterrole= (NOT --role=) plus --user=, --group=, or --serviceaccount=ns:name subjects. Doc example: kubectl create clusterrolebinding root-cluster-admin-binding --clusterrole=cluster-admin --user=root. Inspect with kubectl get clusterrole,clusterrolebinding -o yaml.
**Tags:** k8s::cka src::session topic::kubectl topic::rbac

---

<!-- note:1794496839439 model:Basic -->
**Front:** How does a ClusterRole grant access to endpoints like /healthz or /metrics that aren't Kubernetes resources?
**Back:** With the nonResourceURLs field — e.g. nonResourceURLs: ["/healthz", "/healthz/*"] with verbs<br><br>nonResourceURLs is a ClusterRole-only rules field for API endpoints that aren't Kubernetes resources: /healthz, /metrics, /version, /api, /apis. Format: nonResourceURLs: ["/healthz", "/healthz/*"] with verbs — '*' works as a suffix glob. These rules only take effect in a ClusterRole bound by a ClusterRoleBinding. Listing 'healthz' under resources won't work — it's not a resource type at all.
**Tags:** k8s::cka src::session topic::api topic::rbac topic::security

---

<!-- note:1794496839440 model:Basic -->
**Front:** You manually edit the rules of the system:discovery ClusterRole. What happens?
**Back:** The API server overwrites your changes at startup via auto-reconciliation<br><br>system:-prefixed ClusterRoles and ClusterRoleBindings are control-plane managed (labeled kubernetes.io/bootstrapping=rbac-defaults). At EVERY apiserver start it re-adds missing permissions and subjects — auto-reconciliation repairs accidental edits and picks up new permissions each Kubernetes release. Opt out per-object with annotation rbac.authorization.kubernetes.io/autoupdate: "false", but missing defaults can leave the cluster non-functional. Never hand-edit system: roles — extend them instead via aggregate-to-* labels on your own ClusterRoles.
**Tags:** k8s::cka src::session topic::rbac topic::security

---

<!-- note:1794496839441 model:Basic -->
**Front:** What is the purpose of a ServiceAccount?
**Back:** It provides an identity for processes running in Pods to authenticate to the API server<br><br>A ServiceAccount gives in-cluster workloads (pods) an identity — requests authenticate as system:serviceaccount:<namespace>:<name>, then RBAC decides what that identity may do. Kubernetes deliberately has NO User API object: SAs are the only first-class identity Kubernetes manages itself. Human access is a separate path entirely (client certs, tokens, OIDC).
**Tags:** k8s::cka src::session topic::rbac topic::security

---

<!-- note:1794496839442 model:Basic -->
**Front:** How do human users get access to a Kubernetes cluster? (ServiceAccounts are NOT the mechanism)
**Back:** Client certificates, bearer tokens, or OIDC — they authenticate as User identities<br><br>ServiceAccounts are for pod workloads, NOT people. Humans get cluster access by authenticating with client certificates (admin.conf kubeconfig), bearer tokens, or OIDC — becoming User identities with groups (e.g. system:masters) that RBAC then authorizes. SA identities look like system:serviceaccount:<ns>:<name> and belong to groups system:serviceaccounts and system:serviceaccounts:<ns>. If you need per-person access, issue certs/tokens — don't mint SAs.
**Tags:** k8s::cka src::session topic::authentication topic::rbac

---

<!-- note:1794496839443 model:Basic -->
**Front:** Which command creates a ServiceAccount named build-robot?
**Back:** kubectl create serviceaccount build-robot<br><br>kubectl create serviceaccount NAME makes one imperatively (equivalent: kubectl apply -f sa.yaml with apiVersion: v1, kind: ServiceAccount). The name must be a valid DNS subdomain. Related commands: kubectl get serviceaccounts lists them (NAME/SECRETS/AGE — the SECRETS column is a legacy artifact, mostly 0 since 1.24), kubectl describe serviceaccount <name>, kubectl delete serviceaccount <name>. A ServiceAccount alone grants nothing — pair it with RBAC RoleBindings to give it API permissions.
**Tags:** k8s::cka src::session topic::kubectl topic::rbac

---

<!-- note:1794496839444 model:Basic -->
**Front:** What happens when you create a Pod without spec.serviceAccountName?
**Back:** It is automatically assigned the 'default' ServiceAccount of its namespace<br><br>Every namespace contains at least one SA — 'default'. If spec.serviceAccountName is unset, the API server assigns it at admission (visible in kubectl get pod <name> -o yaml). The default SA still gets its token mounted, so pods that never call the API should set automountServiceAccountToken: false. Best practice: create a dedicated SA per workload and bind only the RBAC it needs — never build apps on 'default'.
**Tags:** k8s::cka src::session topic::rbac topic::security

---

<!-- note:1794496839445 model:Basic -->
**Front:** Where can automountServiceAccountToken: false be set, and which wins if both are set?
**Back:** On the ServiceAccount OR in the Pod spec — the Pod spec takes precedence<br><br>Two opt-out points for token mounting: set automountServiceAccountToken: false in the ServiceAccount manifest (covers every pod using it) OR spec.automountServiceAccountToken: false in the Pod (covers just that pod). Doc-verified: if BOTH specify a value, the POD SPEC wins. Either way the kubelet skips mounting token + CA cert at /var/run/secrets/kubernetes.io/serviceaccount/ — the pod simply can't authenticate to the API.
**Tags:** k8s::cka src::session topic::pods topic::rbac topic::security

---

<!-- note:1794496839448 model:Basic -->
**Front:** How can all Pods using a ServiceAccount pull from a private registry without per-pod config?
**Back:** Add imagePullSecrets to the ServiceAccount object — pods using it inherit the registry credentials<br><br>ServiceAccount objects carry an imagePullSecrets field: kubectl patch serviceaccount default -p '{"imagePullSecrets":[{"name":"myregistrykey"}]}' (or kubectl edit serviceaccount/default). Every pod created with that SA inherits the dockerconfigjson credentials — much cleaner than repeating imagePullSecrets in each pod spec for registries many workloads share.
**Tags:** k8s::cka src::session topic::images topic::rbac

---

<!-- note:1794496839449 model:Basic -->
**Front:** How do you get the cluster to sign a client certificate for a new user?
**Back:** Create a CertificateSigningRequest, get it approved, then read the signed cert from .status.certificate<br><br>The cluster-native signing path: kubectl apply a certificates.k8s.io/v1 CertificateSigningRequest (signerName: kubernetes.io/kube-apiserver-client, usages: [client auth]) → an admin runs kubectl certificate approve <name> → the signed cert appears in the CSR's .status.certificate (base64 — decode it). The control plane's csrsigning controller stamps it with the cluster CA. Requires RBAC rights on certificatesigningrequests — typically only admins can request/approve.
**Tags:** k8s::cka src::session topic::authentication topic::certificates topic::tls

---

<!-- note:1794496839450 model:Basic -->
**Front:** Where do you get the CA cert and key needed to manually sign a user's client certificate?
**Back:** On a control-plane node under /etc/kubernetes/pki/ — ca.crt + ca.key on kubeadm clusters<br><br>To sign a user CSR yourself you need the cluster CA's private key. On kubeadm clusters it lives on control-plane nodes: /etc/kubernetes/pki/ca.crt (public, distributed everywhere) and /etc/kubernetes/pki/ca.key (the crown jewels — whoever holds it can mint any identity). Then: openssl x509 -req -in user.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out user.crt -days 365. The CSR API path avoids touching ca.key directly.
**Tags:** k8s::cka src::session topic::authentication topic::certificates topic::tls

---

<!-- note:1794496839451 model:Basic -->
**Front:** Which commands assemble a kubeconfig file for a new user?
**Back:** kubectl config set-cluster + set-credentials + set-context + use-context, with --embed-certs=true<br><br>Assemble the file with kubectl config subcommands: set-cluster <name> --server=https://... --certificate-authority=ca.crt --embed-certs=true (inlines the CA cert so the file is portable); set-credentials <user> --client-certificate=user.crt --client-key=user.key --embed-certs=true (inlines cert+key); set-context <ctx> --cluster=<name> --user=<user>; use-context <ctx> to activate. Send the resulting ~/.kube/config — it contains everything needed, no external file refs.
**Tags:** k8s::cka src::session topic::authentication topic::certificates topic::kubectl

---

<!-- note:1794496839452 model:Basic -->
**Front:** What is the fastest way to give someone full admin access to a kubeadm cluster?
**Back:** Copy /etc/kubernetes/admin.conf from a control-plane node — it already embeds client certs, server, and context<br><br>admin.conf is a ready-made kubeconfig kubeadm generates on control-plane nodes: server URL + cluster CA + an admin client cert/key (CN=kubernetes-admin, O=system:masters) all embedded. Copy it to the person's ~/.kube/config and they have full cluster-admin immediately — no CSR, no RBAC binding needed since system:masters bypasses authorization. It's the fast path for a second cluster admin; wrong choice for developers (way over-privileged).
**Tags:** k8s::cka src::session topic::authentication topic::certificates topic::rbac

---

<!-- note:1794496839453 model:Basic -->
**Front:** You hand someone a valid client-cert kubeconfig but they get 403 on everything. Why?
**Back:** Authentication succeeded (cert is valid) but no RBAC binding grants their identity permissions — cert proves WHO, RBAC decides WHAT<br><br>A valid client cert only gets you authenticated — the API server then runs authorization and with no Role/ClusterRoleBinding matching their CN or O group, every request returns 403. The workflow is always two steps: (1) issue identity (cert/token/OIDC), (2) bind permissions (kubectl create rolebinding dev1-edit --role=edit --user=dev1 -n dev). Test with kubectl auth can-i --as=dev1 to verify what their identity can actually do.
**Tags:** k8s::cka src::session topic::authentication topic::certificates topic::rbac

---

<!-- note:1794496839454 model:Basic -->
**Front:** How do organizations provide cluster access without distributing certificates?
**Back:** An OIDC issuer + exec credential plugin (e.g. kubelogin) in the kubeconfig — groups come from IdP claims<br><br>Production clusters skip cert distribution: the API server is configured with an OIDC issuer, and users' kubeconfigs use an exec credential plugin (kubelogin for Azure AD, kubectl-oidc-login, etc.) that fetches a fresh token from the IdP on each call. Identity + group claims come from the IdP → RBAC binds those groups. Revoking access = disable the IdP account — nothing long-lived sits on the user's machine to leak.
**Tags:** k8s::cka src::session topic::authentication topic::rbac

---

<!-- note:1794496839455 model:Basic -->
**Front:** How do you cut off a user's cluster access after you've issued them a client certificate?
**Back:** Delete their RBAC bindings — access ends immediately even though the cert remains cryptographically valid<br><br>Two layers, two revocation speeds: RBAC bindings take effect instantly — delete the RoleBinding/ClusterRoleBinding and the identity can do nothing (cert still valid but authorized for zero actions). Certificate revocation is the slow path: there's no CRL/OCSP in K8s client auth, so you wait for cert expiry or rotate the CA. Practical rule: grant access via GROUPS bound in RBAC — removing someone from the IdP group or deleting bindings cuts access without touching their cert.
**Tags:** k8s::cka src::session topic::authentication topic::rbac

---

<!-- note:1794496839458 model:Basic -->
**Front:** A Pod has containers from quay.io AND a private ECR registry — how do you supply credentials for both?
**Back:** Multiple imagePullSecrets per pod, each holding credentials for multiple registries — the kubelet tries the credential matching the image's registry<br><br>A pod with containers from different registries can list several imagePullSecrets, and each Secret's .dockerconfigjson can hold auths for multiple registries. At pull time the kubelet selects the credential matching that image's registry; if none matches it attempts the pull unauthenticated (or via runtime-specific config). imagePullSecrets is a pod-level list — order doesn't matter, matching is by registry hostname.
**Tags:** k8s::cka src::session topic::images topic::pods topic::secrets

---

<!-- note:1794496839470 model:Basic -->
**Front:** Which port does the Kubernetes API server listen on by default?
**Back:** TCP 6443 — the Kubernetes API server, the port EVERY component talks through<br><br>kube-apiserver listens on TCP 6443 inbound by default — it's the single front door: kubelets, kube-proxy, controllers, scheduler, kubectl, and every Pod's ServiceAccount token all authenticate to it. In firewall-restricted environments (on-prem DCs, VPC security groups) 6443 is the one port that must be reachable by everything. It's a default, not a law — teams often put the API server behind a load balancer on 443 and route to 6443 internally.
**Tags:** k8s::cka src::session topic::control-plane topic::networking

---

<!-- note:1794496839471 model:Basic -->
**Front:** Which ports must be open on control plane nodes? (Select all that apply)<br><br>A. 6443 — kube-apiserver<br>B. 2379-2380 — etcd client API<br>C. 10257 — kube-controller-manager<br>D. 10259 — kube-scheduler<br>E. 10255 — kubelet read-only API
**Back:** A, B, C, D – 6443 apiserver, 2379-2380 etcd, 10257 controller-manager, 10259 scheduler<br><br>(Select all that apply) Control plane inbound TCP ports: 6443 kube-apiserver (all components), 2379-2380 etcd client API (apiserver↔etcd), 10257 kube-controller-manager (self only — its secure endpoint), 10259 kube-scheduler (self only). NOT on the list: 10255 is the long-deprecated kubelet read-only port, 10256 is kube-proxy (worker-side health endpoint), and 443 is only there if you override the API server port.
**Tags:** k8s::cka src::session topic::control-plane topic::networking

---

<!-- note:1794496839472 model:Basic -->
**Front:** Which ports does etcd need open, and who talks to it?
**Back:** TCP 2379-2380 — etcd's client API range; 2379 for client traffic, 2380 for peer replication<br><br>etcd listens on TCP 2379-2380 inbound: 2379 serves the client API (kube-apiserver is the client — it's the only regular consumer), 2380 handles peer-to-peer replication between etcd members. etcd stores ALL cluster state so these ports matter for quorum. The doc notes etcd can also run EXTERNAL to the control plane or on custom ports — then only the apiserver↔etcd path needs opening, not the whole range everywhere.
**Tags:** k8s::cka src::session topic::control-plane topic::etcd topic::networking

---

<!-- note:1794496839473 model:Basic -->
**Front:** Which port does the kubelet serve its API on?
**Back:** TCP 10250 — the kubelet API: self plus the control plane (logs, exec, metrics, probes)<br><br>kubelet serves its API on TCP 10250 inbound — used by the kubelet itself AND the control plane, which reaches in for kubectl logs/exec, metrics scraping, and probe results. On worker nodes this is THE port that must be open to the control plane subnet. (Historical note: 10255 was the old read-only kubelet port — deprecated and gone from the docs because it leaked pod specs without auth.)
**Tags:** k8s::cka src::session topic::kubelet topic::networking

---

<!-- note:1794496839480 model:Basic -->
**Front:** Who assigns IP addresses to Pods, Services, and Nodes respectively?
**Back:** Network plugin assigns Pod IPs, kube-apiserver assigns Service IPs, kubelet/cloud-controller-manager assigns Node IPs<br><br>Three different allocators for three object types, all from non-overlapping configured ranges: the NETWORK PLUGIN (CNI/IPAM) assigns Pod IPs; the kube-APISERVER assigns Service ClusterIPs; the KUBELET or cloud-controller-manager assigns Node IPs (cloud provider reports them). Knowing who owns which range matters for debugging IP conflicts and understanding why pod IPs and service IPs live in different CIDRs.
**Tags:** k8s::cka src::session topic::networking topic::services

---

<!-- note:1794496839483 model:Basic -->
**Front:** Which Kubernetes control plane component is responsible for persisting the cluster’s desired state and configuration?
**Back:** etcd<br><br>etcd is a distributed key-value store that reliably stores<br>all Kubernetes cluster data, serving as the single source of truth for the<br>cluster’s state.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839485 model:Basic -->
**Front:** What is <b>the primary purpose</b> of the Kubernetes API server in the control plane architecture?
**Back:** To validate and process REST requests for API objects<br><br>The kube-apiserver is the frontend of the control plane,<br>exposing the Kubernetes API. It processes and validates API requests,<br>and updates the corresponding objects in etcd.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839487 model:Basic -->
**Front:** Which component is NOT part of the Kubernetes control plane?
**Back:** kube-proxy<br><br>kube-proxy runs on every node in the cluster and is responsible for maintaining network rules on nodes, enabling network communication to Pods from network sessions inside or outside of the cluster.<br>It’s a node component, not control plane.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839489 model:Basic -->
**Front:** In Kubernetes, what is the <b>primary role</b> of Role-Based Access Control (RBAC)?
**Back:** To control user and service account access to API resources<br><br>RBAC regulates access to Kubernetes API resources based<br>on the roles of individual users or service accounts within the cluster,<br>ensuring users only perform actions they are authorized for.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839491 model:Basic -->
**Front:** Which security mechanism in Kubernetes is best suited for providing an identity to processes running in Pods to interact with the API server?
**Back:** ServiceAccount<br><br>ServiceAccounts provide an identity for processes that run<br>in a Pod, which can then be granted permissions to API resources via<br>RBAC Roles and RoleBindings.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839493 model:Basic -->
**Front:** What is the main purpose of a ServiceAccount in Kubernetes when interacting with the API server?
**Back:** To provide an identity for Pods to authenticate to the API<br><br>ServiceAccounts provide an identity for processes running<br>within Pods. This identity can be used to authenticate to the Kubernetes<br>API server, and RBAC rules can grant it specific permissions.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839498 model:Basic -->
**Front:** What is <b>the primary role </b>of the ”Controller Manager” in Kubernetes?
**Back:** Runs various controllers that regulate cluster state<br><br>The kube-controller-manager runs multiple controller processes (e.g., Node controller, Replication controller, Endpoints controller)<br>that watch for changes and work to drive the actual cluster state towards<br>the desired state.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839501 model:Basic -->
**Front:** What is the core difference between ”authentication” and ”authorization” in Kubernetes security?
**Back:** Authentication verifies identity, authorization verifies permissions.<br><br>Authentication is the process of determining who a user<br>or service is. Authorization is the process of determining what an authenticated user or service is allowed to do (i.e., which API resources they can<br>access and what actions they can perform).
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839503 model:Basic -->
**Front:** Which Kubernetes component is responsible for watching for newly created Pods and assigning them to Nodes?
**Back:** kube-scheduler<br><br>The kube-scheduler is the control plane component that decides which Node a Pod should run on based on constraints and availability.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839504 model:Basic -->
**Front:** Which component acts as the central control plane and exposes the Kubernetes API?
**Back:** kube-apiserver<br><br>The kube-apiserver validates and configures data for API objects (Pods, Services, etc.) and is the frontend for the control plane.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839505 model:Basic -->
**Front:** What is <b>the primary role </b>of etcd in a Kubernetes cluster?
**Back:** Storing the cluster state<br><br>etcd is a consistent and highly-available key-value store used as Kubernetes’ backing store for all cluster data.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839511 model:Basic -->
**Front:** In Kubernetes RBAC (Role-Based Access Control), what defines a set of permissions?
**Back:** Role / ClusterRole<br><br>Explanation: A Role (namespace-scoped) or ClusterRole (cluster-scoped) contains rules that represent a set of permissions on resources.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839512 model:Basic -->
**Front:** What object binds a Role or ClusterRole to a user, group, or ServiceAccount?
**Back:** RoleBinding / ClusterRoleBinding<br><br>A RoleBinding (namespace-scoped) or ClusterRoleBinding (cluster-scoped) grants the permissions defined in a Role/ClusterRole to subjects.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839518 model:Basic -->
**Front:** Which architectural component ensures that the actual state of cluster resources converges towards the desired state defined in their specifications?
**Back:** Controllers (within kube-controller-manager)<br><br>Controllers implement reconciliation loops. They watch the desired state via the API server and interact with resources to make the current state match the desired state (e.g., ReplicaSet controller ensuring the right number of Pods exist).
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839520 model:Basic -->
**Front:** What is <b>the primary role</b> of kubelet on a worker node?
**Back:** To ensure containers described in PodSpecs assigned to its node are running<br><br>The kubelet is the primary node agent. It receives Pod-Specs from the API server and interacts with the container runtime (e.g., containerd) to start, stop, and manage the containers defined in those Pods, reporting their status back to the control plane.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839521 model:Basic -->
**Front:** Which Kubernetes resource provides a mechanism for grouping API objects and providing a scope for names?
**Back:** Namespace<br><br>Namespaces create logical partitions within a cluster, allowing teams or applications to operate independently. Resource names must be unique within a Namespace, but not necessarily across the entire cluster.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839522 model:Basic -->
**Front:** When interacting with the Kubernetes API server using kubectl, what is the typical format used for defining resource manifests?
**Back:** YAML<br><br>While the API server can accept JSON, YAML is the overwhelmingly conventional and human-readable format used in configuration files (manifests) passed to kubectl for creating or updating resources.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839527 model:Basic -->
**Front:** Which of the following is NOT a standard component of the Kubernetes control plane?<br><br>A. etcd<br>B. kube-apiserver<br>C. kube-scheduler<br>D. containerd<br>E. kube-controller-manager
**Back:** D – containerd<br><br>containerd is a container runtime; it typically runs on worker nodes (managed by the kubelet) to handle container execution, not as part of the central control plane.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839532 model:Basic -->
**Front:** The Kubernetes API server performs several actions when receiving a request. Which action verifies if the authenticated user is allowed to perform the requested operation?
**Back:** Authorization<br><br>After Authentication (who are you?), Authorization (e.g., via RBAC) checks if the identified user has the necessary permissions (Role/ClusterRole bindings) to perform the action (e.g., create, get, delete) on the specific resource (e.g., pods) in the target namespace.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839533 model:Basic -->
**Front:** What is <b>the primary function </b>of etcd within the Kubernetes architecture?
**Back:** To provide reliable, distributed storage for cluster state and configuration<br><br>Explanation: etcd is the consistent key-value store that acts as the source of truth for the entire cluster. All configuration, state, and metadata are persisted here, ensuring consistency across the control plane.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839544 model:Basic -->
**Front:** What is the function of an Admission Controller in the Kubernetes API request lifecycle?
**Back:** To mutate or validate API objects before they are persisted in etcd<br><br>Admission Controllers intercept API requests after authentication and authorization but before persistence. They can mutate objects (e.g., inject sidecars, set default values) or validate them (e.g., enforce security policies, check resource quotas).
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839545 model:Basic -->
**Front:** Which resource defines constraints on the total amount of compute resources (CPU, memory) that can be consumed within a specific Namespace?
**Back:** ResourceQuota<br><br>A ResourceQuota limits the aggregate resource consumption (CPU, memory, storage, object counts) within a Namespace, preventing overuse and ensuring fair sharing among users or teams.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839548 model:Basic -->
**Front:** Which control plane component is primarily responsible for running controllers like the Node Controller, Deployment Controller, and Service Controller?
**Back:** kube-controller-manager<br><br>The kube-controller-manager bundles core Kubernetes controllers into a single binary. It runs controllers that handle node lifecycle, workload management (Deployments, ReplicaSets), service endpoints, namespace creation, etc.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839554 model:Basic -->
**Front:** What is the primary component of a Kubernetes control plane that manages API requests?
**Back:** Kube-apiserver<br><br>The kube-apiserver is the central component that exposes the Kubernetes API and handles all API requests.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839556 model:Basic -->
**Front:** Which component of the Kubernetes control plane exposes the RESTful API for managing the cluster?
**Back:** kube-apiserver<br><br>The kube-apiserver exposes the REST API and acts as the primary entry point for all cluster operations.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839560 model:Basic -->
**Front:** Which component maintains the desired state of applications?
**Back:** Controller Manager<br><br>Controllers continuously reconcile the desired state with the actual cluster state.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839573 model:Basic -->
**Front:** Which component runs on every worker node and is responsible for ensuring that containers are running in a pod according to the pod specification?
**Back:** kubelet<br><br>The kubelet is the node agent that runs a reconcile loop: it watches the API server for pods BOUND to its node, compares desired state (pod spec) vs actual state, and drives the container runtime via CRI to start/stop containers, run probes, and report status. The container runtime is tempting — it does launch the container processes — but it only executes what the kubelet asks; it never reads pod specs itself. kube-scheduler assigns pods (control plane); kube-proxy manages Service network rules, not pod lifecycle.
**Tags:** k8s::cka topic::architecture topic::kubelet src::session

---

<!-- note:1794496839584 model:Basic -->
**Front:** On a Linux host, where does the Docker daemon store images, container filesystems, and volumes?
**Back:** /var/lib/docker — Docker's data root holding images, containers, volumes, and storage-driver layers<br><br>/var/lib/docker is Docker's data root on Linux: it contains subdirectories for containers/, image/, volumes/, overlay2/ (the storage driver layers), build cache, swarm state, and more — EVERYTHING Docker persists lives under it. Distractors: /var/lib/containers is Podman's root (different runtime!), ~/.docker only holds client config (config.json auth, CLI settings), /etc/docker holds daemon.json configuration — not image/container data.
**Tags:** k8s::cka topic::docker topic::storage src::session

---

<!-- note:1794496839586 model:Basic -->
**Front:** What are the benefits of Docker's layered image architecture? (Select all that apply)<br><br>A. Identical base layers are stored once and shared across images — saves disk<br>B. On rebuild, cached layers are reused until a changed instruction — faster builds, no unnecessary rebuilds<br>C. Only the layers whose instructions changed get rebuilt on top of the cache<br>D. Layers can be edited in place after the image is built
**Back:** A, B, C – shared base layers save disk, the layer cache speeds rebuilds, and unchanged layers aren't rebuilt; D is wrong — layers are read-only<br><br>Layer caching is the layered architecture's superpower: (A) identical base layers (e.g. the ubuntu base) are stored ONCE and shared by every image built FROM it — massive disk savings; (B) on rebuild, Docker reuses cached layers until it hits an instruction whose inputs changed, then rebuilds only from there down — updating app code doesn't re-run apt-get; (C) the registry also stores/pushes layers once and dedupes across images. D is the trap: image layers are READ-ONLY — you cannot edit them after build; runtime writes go to the container's separate writable layer (copy-on-write).
**Tags:** k8s::cka topic::docker topic::storage topic::images src::session

---

<!-- note:1794496839587 model:Basic -->
**Front:** What filesystem layers make up a running Docker container?
**Back:** Read-only image layers (the built image) plus ONE writable 'container layer' on top for runtime changes<br><br>Every running container's filesystem = the image's read-only layers (shared, immutable) + a single writable layer unique to that container. Everything the app writes — new files, logs, overwrites of image files — lands in the container layer. The image layers are never modified, which is exactly why one image can safely back many containers. The writable layer is per-container and dies with the container — nothing in it persists.
**Tags:** k8s::cka topic::docker topic::storage src::session

---

<!-- note:1794496839588 model:Basic -->
**Front:** A container process modifies /etc/nginx/nginx.conf, which exists in the read-only image layers. What does Docker do?
**Back:** Docker copies the file up into the writable container layer; all edits hit the copy — the read-only image layer stays untouched<br><br>Copy-on-write (CoW): image layers are shared read-only, so when a container modifies a file that lives in a lower layer, Docker doesn't edit it in place — it COPIES the file up to the container's writable layer and applies changes there. Result: the image layer remains pristine and shareable across all containers; each container sees its own modified version. This is why 'docker commit' snapshots are possible and why images stay immutable. Storage drivers (overlay2 etc.) implement this efficiently — only changed files consume new disk.
**Tags:** k8s::cka topic::docker topic::storage src::session

---

<!-- note:1794496839589 model:Basic -->
**Front:** How do you persist data written by a Docker container using a named volume?
**Back:** docker volume create data_volume — stored under /var/lib/docker/volumes on the host, mounted into the container at a path like /data; survives container deletion<br><br>Named volumes are Docker-managed persistent storage: <code>docker volume create data_volume</code> creates it under /var/lib/docker/volumes/data_volume/_data on the host (location managed by the daemon — don't touch it directly). Mount at runtime: <code>docker run -v data_volume:/data myimage</code> — inside the container it appears as a normal directory. When the container is removed, the VOLUME survives (unlike the writable layer). Volumes live outside the image layer stack entirely, so they're immune to image changes and CoW.
**Tags:** k8s::cka topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794496839590 model:Basic -->
**Front:** How does Docker handle storage drivers for its layered filesystem?
**Back:** overlay2 is the default on modern Linux; aufs/zfs/btrfs/devicemapper are alternatives chosen automatically based on the host OS and backing filesystem<br><br>Storage drivers implement the layered + copy-on-write machinery on disk. overlay2 is the default on all modern Linux distros (uses the kernel's overlay filesystem — fast, low overhead). Legacy/alternative drivers: aufs (older Ubuntu default), zfs and btrfs (used when the host filesystem IS zfs/btrfs — CoW-native, snapshots for free), devicemapper (old RHEL/CentOS, largely deprecated), vfs (no layering, testing only). Docker AUTO-SELECTS the best driver at install based on OS + filesystem — you rarely choose manually; check with <code>docker info | grep 'Storage Driver'</code>.
**Tags:** k8s::cka topic::docker topic::storage src::session

---

<!-- note:1794496839591 model:Basic -->
**Front:** What is the difference between a Docker volume and a bind mount? (Select all that apply)<br><br>A. Named volumes live under /var/lib/docker/volumes while bind mounts link a host path — both survive container deletion equally<br>B. Named volumes are daemon-managed under /var/lib/docker/volumes and persist independently; bind mounts link any host path directly with no Docker management<br>C. Bind mounts require docker volume create first; named volumes mount arbitrary host paths<br>D. Volumes are per-container only; bind mounts are shared across all containers
**Back:** B, C – docker volume create data_volume stored under /var/lib/docker/volumes, and bind mounts link any host path directly; A describes neither correctly and D is wrong<br><br>Two mount types differ in WHO manages the host side: NAMED VOLUME — created by <code>docker volume create</code>, lives under /var/lib/docker/volumes (daemon-managed location), survives container deletion, portable across hosts via volume drivers; ideal for persistent app data (databases). BIND MOUNT — <code>-v /host/path:/container/path</code> links ANY host path directly into the container; the host path is YOUR choice, both host processes and the container can modify it simultaneously; great for dev (mount source code) or accessing host files. tmpfs (bonus third type) = memory-only, dies with the container.
**Tags:** k8s::cka topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794496839593 model:Basic -->
**Front:** Why does data written inside a running container disappear when the container is removed — and what's the fix?
**Back:** The writable container layer is unique per container and exists ONLY while the container runs — docker rm destroys it and everything written there is gone (logs, generated files, database files written without a mount). That's why the layer can't be your persistence story: the image layers are shared read-only, the container layer is disposable. The fixes are the mount types — named volumes (daemon-managed, /var/lib/docker/volumes), bind mounts (direct host path), tmpfs (memory-only, also dies with the container). For databases and anything you can't regenerate, mount a volume.
**Tags:** k8s::cka topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794496839595 model:Basic -->
**Front:** What does the 'local' volume driver do?
**Back:** The 'local' driver is the default — stores volume data under /var/lib/docker/volumes on the host<br><br>The 'local' volume driver is built in and is the DEFAULT for every docker volume create — it stores data on the host filesystem under /var/lib/docker/volumes/<name>/_data. If you never pass --driver, you get 'local'. It's the volume-side equivalent of overlay2 for layers: zero-config, host-disk-backed, dies with the host. Other drivers must be installed as plugins first (docker plugin install) before --driver can use them.
**Tags:** k8s::cka topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794496839596 model:Basic -->
**Front:** Which of these are Docker VOLUME driver plugins? (Select all that apply)<br><br>A. amazon-ebs — creates AWS EBS volumes for containers<br>B. azurefile — mounts Azure Files SMB shares<br>C. overlay2 — provides copy-on-write image layers<br>D. flocker — manages volumes across a cluster of hosts
**Back:** A, B, D – amazon-ebs (AWS block storage), azurefile (Azure Files SMB), and flocker (cluster volume management); overlay2 and aufs are STORAGE drivers, not volume drivers<br><br>Volume plugins put named volumes on EXTERNAL storage: amazon-ebs → AWS EBS volumes, azurefile → Azure Files (SMB), google-persistent-disk → GCP PD, flocker → cluster-aware volume placement, rexray → multi-cloud, longhorn/portworx → Kubernetes-native distributed storage. The distractors are the trap: overlay2 and aufs are STORAGE drivers — they manage image layers, not volumes. Telling the two plugin families apart is exactly what this lesson is about.
**Tags:** k8s::cka topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794496839597 model:Basic -->
**Front:** How do you create and use a volume backed by a third-party plugin like amazon-ebs?
**Back:** docker volume create --driver=<plugin> <name>, then mount normally with -v <name>:<path> — the driver is chosen at volume-creation time<br><br>Using a volume plugin is two steps: (1) install the plugin (docker plugin install <name> or it ships configured), (2) create the volume WITH the driver: <code>docker volume create --driver=amazon-ebs --opt size=10 gb_vol</code> — driver-specific options go in --opt. Then use it like any volume: <code>docker run -v gb_vol:/data app</code>. The --volume-driver flag on docker run sets a default driver for anonymous volumes; --mount type=volume,volume-driver=X selects per-volume. The driver choice sticks to the volume — it was decided at create time.
**Tags:** k8s::cka topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794496839631 model:Basic -->
**Front:** What does a StorageClass object look like at the API level?
**Back:** apiVersion: storage.k8s.io/v1, kind: StorageClass — a cluster-scoped object (not namespaced, admins define it once for everyone)<br><br>A StorageClass is apiVersion: storage.k8s.io/v1 (named API group — NOT v1 core, NOT a CRD you write yourself) + kind: StorageClass. It's CLUSTER-SCOPED: admins define classes once ('standard' = fast SSD, 'slow' = cheap HDD, 'encrypted' = encrypted volumes) and every namespace's PVCs can reference them by name via storageClassName. Think of it as a 'storage product catalog' — the class bundles provisioner + parameters + policies into a reusable profile users pick by name.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839642 model:Basic -->
**Front:** Why did Kubernetes remove dockershim in v1.24?
**Back:** Docker Engine is not CRI-compatible; the kubelet-internal dockershim shim was vendor-specific complexity, so Kubernetes standardized on CRI runtimes (containerd, CRI-O)<br><br>Dockershim let the kubelet talk to Docker Engine, which predates and never implemented the CRI. It was removed in v1.24 to cut maintenance burden and align with open standards. Docker images still work — they follow OCI specs — and Docker Engine can still be used via the cri-dockerd shim.
**Tags:** k8s::cka src::session topic::cri-oci topic::docker

---

<!-- note:1794496839643 model:Basic -->
**Front:** Can a cluster still use Docker Engine as its container runtime today?
**Back:** Yes — via cri-dockerd, a CRI shim maintained by Docker/Mirantis; though most clusters use containerd or CRI-O directly<br><br>Dockershim removal ended the BUILT-IN Docker path, not Docker itself. cri-dockerd re-adds the CRI bridge outside the kubelet. In practice, managed clusters run containerd or CRI-O — and note Docker Engine itself uses containerd under the hood.
**Tags:** k8s::cka src::session topic::cri-oci topic::docker

---

<!-- note:1794496839644 model:Basic -->
**Front:** Why can an image built with Docker run on a different runtime like containerd?
**Back:** Both follow OCI standards: the image conforms to the image-spec format and containerd follows the runtime-spec<br><br>OCI image-spec standardizes how an image is packaged (manifest, config, layers); runtime-spec standardizes how it's executed. Any OCI-compliant runtime can run any OCI-compliant image — that's why Docker-built images run on containerd, CRI-O, etc. No conversion needed.
**Tags:** k8s::cka src::session topic::cri-oci topic::docker

---

<!-- note:1794496839645 model:Basic -->
**Front:** How do containers fundamentally differ from virtual machines?
**Back:** Containers share the host OS kernel (isolated via namespaces/cgroups) with no guest OS — much lighter and faster than VMs<br><br>A VM runs a full guest OS on a hypervisor — heavyweight, slow to boot. A container is just an isolated process set on the host: it shares the host kernel and gets its own view of processes/network/filesystems. That's why containers start in milliseconds and pack denser.
**Tags:** k8s::cka src::session topic::container-orchestration topic::docker

---

<!-- note:1794496839646 model:Basic -->
**Front:** What is the difference between a container image and a container?
**Back:** The image is the read-only template/package; the container is a running instance of it<br><br>An image packages the app + dependencies as a sharable, versioned artifact (built once, stored in a registry). A container is what runs when you instantiate the image — the live isolated environment with its own processes, network and filesystem. One image → many containers.
**Tags:** k8s::cka src::session topic::cri-oci topic::docker

---

<!-- note:1794496839647 model:Basic -->
**Front:** What are the benefits of using container runtimes that support the CRI? (Select all that apply)<br><br>A. It enables automatic scaling of container instances<br>B. It enables container runtimes to be developed independently of Kubernetes<br>C. It provides better compatibility and standardization across container runtimes<br>D. It allows for direct communication between containers
**Back:** B, C – runtimes implement CRI independently of Kubernetes; the standard interface gives compatibility and standardization across runtimes<br><br>CRI defines one standard interface between the kubelet and any container runtime. That standardization is the core benefit: compliant runtimes (containerd, CRI-O, cri-dockerd) plug in interchangeably, giving better compatibility and standardization across runtimes (C); and runtime developers only need to satisfy the interface, so runtimes can be built and evolved independently of Kubernetes itself (B). A and D are unrelated to CRI — scaling is the orchestrator's job and CNI, not CRI, handles container networking.
**Tags:** k8s::cka src::session topic::container-orchestration topic::cri-oci

---

<!-- note:1794496839649 model:Basic -->
**Front:** In a Pod spec, image: nginx is shorthand for what fully-qualified image?
**Back:** docker.io/library/nginx:latest — registry docker.io, namespace library (official images), tag latest<br><br>An image name is REGISTRY/REPOSITORY:TAG with three independent defaults: no registry → docker.io (Docker Hub); official-library images live under the library/ namespace (docker.io/library/nginx); no tag → latest. So image: nginx is shorthand for docker.io/library/nginx:latest. Your own Docker Hub images resolve to docker.io/<your-username>/<image> — the middle path segment is the namespace/account, not part of the registry.
**Tags:** k8s::cka src::session topic::containers topic::images

---

<!-- note:1794496839650 model:Basic -->
**Front:** For image: quay.io/myorg/api:v2, which part is the registry?
**Back:** quay.io — the registry is everything before the first slash that contains a dot/colon or is 'localhost'<br><br>Image name anatomy: [registry/][namespace/]repository[:tag]. The registry is identified by a '.' or ':' in the first path segment (quay.io, gcr.io, localhost:5000) or the literal 'localhost' — docker.io is assumed when absent. Everything between registry and repo is the namespace/account (yourorg, library). With your own Docker Hub account 'acme', image: acme/api expands to docker.io/acme/api:latest — registry docker.io, namespace acme, repo api.
**Tags:** k8s::cka src::session topic::containers topic::images

---

<!-- note:1794496839657 model:Basic -->
**Front:** What is the responsibility of a container runtime in terms of networking?
**Back:** All of the options are correct<br><br>All three are genuine runtime jobs in the CNI flow: the container runtime (containerd/CRI-O) creates each container's network namespace, selects which CNI configuration applies (the .conflist in /etc/cni/net.d/), and invokes the CNI plugin's ADD/DEL commands to attach that namespace to the configured network. The kubelet delegates this via CRI — the runtime is the component that actually calls CNI; the plugin then does the hands-on work (veth pair, bridge, IPAM). Runtime orchestrates, plugin executes.
**Tags:** k8s::cka src::session topic::cni topic::cri-oci topic::networking

---

<!-- note:1794496839669 model:Basic -->
**Front:** Which part of the <b>Container Runtime Interface (CRI)</b> specification is containerd primarily responsible for implementing?
**Back:** Low-level container execution and lifecycle management<br><br>containerd is a core container runtime that manages the<br>complete container lifecycle on a single host – image transfer, storage,<br>container execution, supervision, and network attachments.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839671 model:Basic -->
**Front:** Why are Open Standards, like those defined by the Open Container Initiative (OCI), critical for the cloud native ecosystem?
**Back:** They promote interoperability and prevent vendor lock-in<br><br>Open standards (e.g., OCI for container formats/runtimes,<br>CNI for networking, CRI for runtimes) ensure that different tools and<br>platforms can work together seamlessly, giving users choice and preventing<br>vendor lock-in.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839672 model:Basic -->
**Front:** Which OCI specification defines the format of a container image?
**Back:** Image Specification<br><br>The OCI Image Specification defines how to create and<br>package a container image, ensuring interoperability across different container tools and runtimes that adhere to the standard.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839675 model:Basic -->
**Front:** Which of these is a standard specified by the OCI (Open Container Initiative)?
**Back:** Image Specification<br><br>The OCI defines standards for container image formats (Image Specification) and runtime (Runtime Specification).
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839676 model:Basic -->
**Front:** Which container runtime is most commonly associated with Kubernetes and implements the CRI (Container Runtime Interface)?
**Back:** containerd<br><br>containerd is a widely used container runtime focused on simplicity, robustness, and portability, fully implementing the CRI.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839681 model:Basic -->
**Front:** When defining a Pod, what does the <i>spec.containers[].image</i> field specify?
**Back:** The specific container image (and tag) to run<br><br>This field tells the container runtime which image (e.g., nginx:1.21 or myrepo/myapp:v2.5) to pull from a registry and use to create the container process.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839682 model:Basic -->
**Front:** Which OCI (Open Container Initiative) specification defines how container runtimes should execute containers?
**Back:** Runtime Specification (CRI is Kubernetes’ interface to this)<br><br>The OCI Runtime Specification outlines how to run a container filesystem bundle. Kubernetes uses the Container Runtime Interface (CRI) as an abstraction layer over runtimes like containerd or CRI-O that implement this standard.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839683 model:Basic -->
**Front:** What is the primary goal of the Open Container Initiative (OCI)?
**Back:** To define open standards around container formats and runtime<br><br>OCI aims to establish common, open, minimal standards for container image formats and container runtime execution to ensure interoperability and prevent fragmentation in the container ecosystem.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839684 model:Basic -->
**Front:** Which statement best describes the relationship between Kubernetes and Docker (as of 2025)?
**Back:** Kubernetes primarily interacts with container runtimes via CRI (e.g., containerd, CRI-O), abstracting Docker.<br><br>Explanation: Kubernetes deprecated the direct Docker integration (dockershim). It now interacts with OCI-compliant runtimes like containerd (which Docker itself uses) or CRI-O via the Container Runtime Interface (CRI). While Docker might be installed, K8s doesn’t use it directly in the same way.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839686 model:Basic -->
**Front:** Which statement about containers is true?
**Back:** Run consistently across environments<br><br>Containers provide portability, allowing applications to run consistently across different environments.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839688 model:Basic -->
**Front:** What is the primary role of a container runtime?
**Back:** Run containers<br><br>The container runtime is responsible for executing containers on cluster nodes.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839689 model:Basic -->
**Front:** Which container runtime option is supported by Kubernetes?
**Back:** CRI-compliant runtimes<br><br>Kubernetes natively supports runtimes that implement the Container Runtime Interface (CRI), such as containerd and CRI-O.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839693 model:Basic -->
**Front:** What is <b>the primary function</b> of the kubelet component?
**Back:** Managing the container runtime<br><br>The kubelet runs on each Node and ensures that containers described in PodSpecs are running and healthy. It interacts with the container runtime.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session topic::container-orchestration

---

<!-- note:1794496839694 model:Basic -->
**Front:** What does the container runtime specification, governed by the OCI, include?
**Back:** The runtime spec covers executing the bundle: downloading/unpacking the rootfs, config.json, and the container lifecycle (create→start→kill→delete) that an OCI runtime must implement<br><br>OCI publishes SEPARATE specs — don't mix them: RUNTIME spec = how to RUN a container (the 'bundle': rootfs + config.json, the process args, mounts, namespaces; lifecycle states create/start/kill/delete) — that's option A. IMAGE spec = how to CREATE/format an image (option B). DISTRIBUTION spec = how to PUSH/PULL images via registries (option C). D is nonsense — runtimes (runc, crun) IMPLEMENT the spec; you don't 'create a runtime' per the spec. In Kubernetes: CRI is the kubelet↔runtime API, and runtimes like containerd speak OCI runtime spec underneath.
**Tags:** k8s::cka topic::cri-oci topic::containers src::session

---

<!-- note:1794496839695 model:Basic -->
**Front:** What is a Certificate Signing Request (CSR)?
**Back:** an unsigned request: public key + subject details (CN, O, SANs) packaged for the CA to sign into a certificate<br><br>A CSR is your key pair's PUBLIC half plus identity details (CN username, O groups, SANs) wrapped into a signing request — a certificate-to-be minus the signature. You hand it to a CA (<code>openssl req -new -key x.key -out x.csr</code>), it verifies and stamps 'signed by me' (<code>openssl x509 -req -in x.csr -CA ca.crt -CAkey ca.key -out x.crt</code>). The private key never leaves your side.
**Tags:** k8s::cka src::session topic::certificates topic::security topic::tls

---

<!-- note:1794496839696 model:Basic (and reversed card) -->
**Front:** What is a node in Kubernetes?
**Back:** A physical or virtual machine on which Kubernetes is installed. It is a worker machine — Kubernetes launches the application's containers on nodes.
**Tags:** k8s::cka topic::architecture src::session

---

<!-- note:1794496839697 model:Basic (and reversed card) -->
**Front:** What is a cluster in Kubernetes?
**Back:** A set of nodes grouped together to run containerized applications. Workloads are spread across the nodes, so the application survives the failure of any single node.
**Tags:** k8s::cka topic::architecture src::session

---

<!-- note:1794496839698 model:Basic (and reversed card) -->
**Front:** What is the control plane in Kubernetes?
**Back:** The set of components that manages the cluster: it stores all cluster state, monitors nodes, assigns workloads to nodes, and moves workloads off nodes that fail. Previously called the 'master'.
**Tags:** k8s::cka topic::architecture src::session

---

<!-- note:1794496839699 model:Basic (and reversed card) -->
**Front:** What does the kube-apiserver do?
**Back:** It is the frontend of Kubernetes. All clients — kubectl, the web UI, and the cluster's own components — talk to the API server to interact with the cluster.
**Tags:** k8s::cka topic::architecture src::session

---

<!-- note:1794496839700 model:Basic (and reversed card) -->
**Front:** What is etcd in Kubernetes?
**Back:** A distributed, reliable key-value store used by Kubernetes to persist all cluster data — node state, configuration, and the desired and current state of every workload.
**Tags:** k8s::cka topic::architecture src::session

---

<!-- note:1794496839701 model:Basic (and reversed card) -->
**Front:** What does the kube-scheduler do?
**Back:** It assigns new workloads (pods) to nodes. It picks a suitable node for each workload based on criteria like resource requirements, node capacity, and placement rules.
**Tags:** k8s::cka topic::architecture src::session

---

<!-- note:1794496839702 model:Basic (and reversed card) -->
**Front:** What does the controller-manager do in Kubernetes?
**Back:** It runs the controllers — the brain behind orchestration. They watch the cluster state through the API server and respond to changes, e.g. moving workloads off a node that failed.
**Tags:** k8s::cka topic::architecture src::session

---

<!-- note:1794496839703 model:Basic (and reversed card) -->
**Front:** What is a kubelet?
**Back:** An agent that runs on every node. It receives instructions from the API server, makes sure the containers assigned to that node run as expected, and reports their status back.
**Tags:** k8s::cka topic::architecture src::session

---

<!-- note:1794496839704 model:Basic (and reversed card) -->
**Front:** What is the container runtime in Kubernetes?
**Back:** The software on each node that actually runs containers — pulling images and starting/stopping containers (e.g. containerd, CRI-O).
**Tags:** k8s::cka topic::architecture src::session

---

<!-- note:1794496839707 model:Basic (and reversed card) -->
**Front:** What is OCI and what does it stand for?
**Back:** OCI stands for Open Container Initiative — a Linux Foundation body that publishes open standards for containers, mainly the image-spec (image format) and the runtime-spec (how to run a container). It keeps images and runtimes from different vendors compatible.
**Tags:** k8s::cka topic::cri-oci src::session

---

<!-- note:1794496839708 model:Basic (and reversed card) -->
**Front:** What does the OCI image specification (image-spec) define?
**Back:** It defines the format of a container image: the manifest, the image configuration, and the filesystem layers — i.e. how an image is packaged and shared so that any OCI-compliant runtime can run it.
**Tags:** k8s::cka topic::cri-oci src::session

---

<!-- note:1794496839709 model:Basic (and reversed card) -->
**Front:** What does the OCI runtime specification (runtime-spec) define?
**Back:** It defines how to run a container from a filesystem bundle: the container's configuration (namespaces, cgroups, mounts) and its lifecycle (create, start, stop, delete). runc is the reference implementation.
**Tags:** k8s::cka topic::cri-oci src::session

---

<!-- note:1794496839725 model:Basic (and reversed card) -->
**Front:** What is crictl?
**Back:** A command-line client for CRI-compatible container runtimes (containerd, CRI-O). It talks to the runtime directly through the Container Runtime Interface — no Docker daemon or Kubernetes API needed — and is mainly used to inspect and debug containers on a node.
**Tags:** k8s::cka topic::troubleshooting src::session

---

<!-- note:1794496839726 model:Basic (and reversed card) -->
**Front:** Which four top-level fields must every Kubernetes object manifest contain?
**Back:** <code>apiVersion</code>, <code>kind</code>, <code>metadata</code> and <code>spec</code>. (<code>status</code> also appears on live objects, but the cluster writes it — it is not required in the file you submit.)
**Tags:** k8s::cka topic::api topic::yaml src::session

---

<!-- note:1794496839731 model:Basic (and reversed card) -->
**Front:** How do you place a new object into namespace 'dev' instead of 'default' when creating it?
**Back:** Set its <code>metadata.namespace</code> field (e.g. <code>namespace: dev</code>) — or pass <code>-n dev</code> at creation with an imperative command. If you omit it, the object lands in your current context's namespace (usually <code>default</code>).
**Tags:** k8s::cka src::session topic::dns topic::namespaces

---

<!-- note:1794496839746 model:Basic (and reversed card) -->
**Front:** Users vs ServiceAccounts in Kubernetes — which ones can you '<code>kubectl create</code>'?
**Back:** Only ServiceAccounts — they ARE API objects (namespaced, kubectl-creatable). Normal users are NOT Kubernetes objects at all: 'Kubernetes does not have objects which represent normal user accounts.' Humans/automation get identity from an external source — a client cert signed by the cluster CA, an OIDC/IdP login, a static token file — and the apiserver just validates it. Rule of thumb: humans = external user identity; in-cluster processes = ServiceAccount.
**Tags:** k8s::cka src::session topic::authentication topic::security topic::serviceaccounts

---

<!-- note:1794496839747 model:Basic (and reversed card) -->
**Front:** What is a Kubernetes API group?
**Back:** A logical grouping of related API resources served together at a REST path. The core (legacy) group lives at /api/v1 and holds the original resources (pods, services, namespaces, nodes, secrets…); named groups live at /apis/<group>/<version> (apps, batch, networking.k8s.io, rbac.authorization.k8s.io, storage.k8s.io, apiextensions.k8s.io…) and host newer features. The group is declared in each object's apiVersion field, and groups make the API extensible — new resource families arrive as new groups without changing core.
**Tags:** k8s::cka src::session topic::api topic::architecture

---

<!-- note:1794496839748 model:Basic (and reversed card) -->
**Front:** What is the Container Runtime Interface (CRI)?
**Back:** The standard gRPC plugin interface between the kubelet and the container runtime on each node. Any runtime implementing CRI (containerd, CRI-O) can run containers under Kubernetes — that's what makes runtimes swappable. The CRI-compliant runtimes in turn follow OCI standards (image-spec, runtime-spec).
**Tags:** k8s::cka src::session topic::container-orchestration topic::cri-oci

---

<!-- note:1794496839757 model:Cloze -->
**Text:** A minimal Pod manifest:<br><br><code>apiVersion: {{c1::v1}}<br>kind: {{c2::Pod}}<br>{{c3::metadata}}:<br>&nbsp;&nbsp;name: nginx<br>{{c4::spec}}:<br>&nbsp;&nbsp;containers:</code>
**Back Extra:** apiVersion + kind say what to create and through which API (Pods are in the core group, hence plain <code>v1</code>); metadata identifies the object; spec is the desired state, with a schema specific to the kind.
**Tags:** k8s::cka topic::pods topic::yaml src::session

---

<!-- note:1794496839759 model:Cloze -->
**Text:** Control plane nodes were previously called {{c1::master}} nodes.
**Back Extra:** The old term 'master node' is still common in older courses, books and docs — e.g. 'master components'. Same thing; 'control plane' is the current name.
**Tags:** k8s::cka src::session topic::architecture topic::control-plane

---

<!-- note:1794496839767 model:Cloze -->
**Text:** ResourceQuota manifest — aggregate caps for one namespace:<br><br><code>apiVersion: {{c1::v1}}<br>kind: {{c2::ResourceQuota}}<br>metadata:<br>  name: compute-quota<br>  namespace: {{c3::dev}}<br>spec:<br>  {{c4::hard}}:<br>    {{c5::requests.cpu}}: "4"<br>    requests.memory: 4Gi<br>    {{c6::limits.cpu}}: "8"<br>    pods: "10"</code>
**Back Extra:** spec.hard maps resource names → totals for the namespace: requests.cpu/requests.memory, limits.cpu/limits.memory, plus object counts (pods, services, persistentvolumeclaims). Exceeding any entry → new object rejected with 403. A cpu/memory quota forces every pod to declare that resource — pair it with LimitRange for defaults.
**Tags:** topic::namespaces topic::yaml src::session

---

<!-- note:1794496839769 model:Cloze -->
**Text:** Enable static pods via kubelet config file:<br><br><code>apiVersion: {{c1::kubelet.config.k8s.io/v1beta1}}<br>kind: {{c2::KubeletConfiguration}}<br>{{c3::staticPodPath}}: {{c4::/etc/kubernetes/manifests}}</code><br><br>then <code>systemctl {{c5::restart}} kubelet</code>
**Back Extra:** staticPodPath points kubelet at a directory it scans periodically — pod YAMLs appearing there get created, files removed get their pods deleted. Deprecated alternative: <code>--pod-manifest-path</code> flag. Web-hosted variant: staticPodURL / <code>--manifest-url</code>. Check the live kubelet's config on the node (e.g. /var/lib/kubelet/config.yaml) or ps aux | grep kubelet for the flag.
**Tags:** k8s::cka src::session topic::kubelet topic::staticpods

---

<!-- note:1794496839771 model:Cloze -->
**Text:** By default kubectl reads its kubeconfig from {{c1::$HOME/.kube/config}}. The {{c2::KUBECONFIG}} environment variable holds a {{c3::list}} of files that kubectl {{c4::merges}} (first file to set a value wins per key), while the {{c5::--kubeconfig}} flag points at exactly {{c6::one}} file with {{c7::no}} merging.
**Back Extra:** Precedence: --kubeconfig flag > KUBECONFIG env var > default file. When KUBECONFIG lists multiple files, kubectl merges them — the first file to set a value or map key wins and later duplicates are discarded. Relative file paths inside a kubeconfig resolve relative to that kubeconfig's location.
**Tags:** k8s::cka src::session topic::kubeconfig topic::kubectl

---

<!-- note:1794496839772 model:Cloze -->
**Text:** REST paths — core group: {{c1::/api/v1}} (apiVersion: {{c2::v1}}, no group name); named groups: {{c3::/apis/$GROUP_NAME/$VERSION}} (e.g. apiVersion: {{c4::apps/v1}} → /apis/apps/v1).
**Back Extra:** The apiVersion field mirrors the REST path: bare 'v1' = core group; 'group/version' = named group. So apiVersion: apps/v1 means REST path /apis/apps/v1. kubectl api-resources prints this mapping for every resource your cluster serves.
**Tags:** k8s::cka src::session topic::api topic::yaml

---

<!-- note:1794496839773 model:Cloze -->
**Text:** ABAC authorization: permission policies live in a {{c1::JSON policy file}} passed to the API server via {{c2::--authorization-policy-file}}; changing them requires {{c3::editing the file and restarting the API server}} — the operational pain that made {{c4::RBAC}} the standard instead.
**Back Extra:** ABAC = Attribute-Based Access Control: policies combine user attributes + resource attributes + environment attributes into allow rules. It predates RBAC and lost because every policy change meant editing the file AND restarting the API server — no dynamic updates, no kubectl management. RBAC replaced it by making permissions Kubernetes API objects editable live. Avoid ABAC in new clusters.
**Tags:** k8s::cka src::session topic::abac topic::rbac topic::security

---

<!-- note:1794496839774 model:Cloze -->
**Text:** Minimal Role manifest (pod-reader in 'default'):<br><br><code>apiVersion: {{c1::rbac.authorization.k8s.io/v1}}<br>kind: {{c2::Role}}<br>metadata:<br>  namespace: {{c3::default}}<br>  name: pod-reader<br>rules:<br>- apiGroups: [{{c4::""}}]  # "" = core API group<br>  resources: [{{c5::pods}}]<br>  verbs: [{{c6::get, watch, list}}]</code>
**Back Extra:** rules is a LIST — each entry is one permission set where apiGroups + resources + verbs must all match a request. apiGroups: [""] = core/v1 resources. Multiple rules union (RBAC is additive — no deny). Verbs come from the API verb set; special verbs impersonate/bind/escalate gate RBAC-escalation itself. Same skeleton with kind: ClusterRole + no namespace grants cluster-wide.
**Tags:** k8s::cka src::session topic::rbac topic::yaml

---

<!-- note:1794496839775 model:Cloze -->
**Text:** RoleBinding manifest linking user 'jane' to Role 'pod-reader':<br><br><code>apiVersion: {{c1::rbac.authorization.k8s.io/v1}}<br>kind: {{c2::RoleBinding}}<br>metadata:<br>  name: read-pods<br>  namespace: {{c3::default}}<br>subjects:<br>- kind: {{c4::User}}<br>  name: {{c5::jane}}<br>  apiGroup: rbac.authorization.k8s.io<br>roleRef:<br>  kind: {{c6::Role}}<br>  name: pod-reader<br>  apiGroup: rbac.authorization.k8s.io</code>
**Back Extra:** subjects = WHO gets it (kind User/Group/ServiceAccount + case-sensitive name + apiGroup); roleRef = WHAT (kind Role|ClusterRole + name + apiGroup — immutable, recreate to change). The binding's namespace sets scope: RoleBinding in 'dev' + ClusterRole ref = perms only in 'dev'. ClusterRoleBinding = cluster-wide. Create imperatively: kubectl create rolebinding read-pods --role=pod-reader --user=jane -n default.
**Tags:** k8s::cka src::session topic::rbac topic::yaml

---

<!-- note:1794496839776 model:Cloze -->
**Text:** ClusterRole manifest granting full node management cluster-wide:<br><br><code>apiVersion: {{c1::rbac.authorization.k8s.io/v1}}<br>kind: {{c2::ClusterRole}}<br>metadata:<br>  name: node-admin<br>rules:<br>- apiGroups: [{{c3::""}}]<br>  resources: [{{c4::nodes}}]<br>  verbs: [{{c5::get, list, watch, create, update, patch, delete}}]</code>
**Back Extra:** No namespace field — ClusterRoles are cluster-scoped (Role requires metadata.namespace). nodes is a core-group resource so apiGroups: [""]. A ClusterRole alone grants nothing — it needs a ClusterRoleBinding to attach subjects. Same skeleton works for namespaces, persistentvolumes, clusterroles, storageclasses (all cluster-scoped).
**Tags:** k8s::cka src::session topic::rbac topic::yaml

---

<!-- note:1794496839777 model:Cloze -->
**Text:** ClusterRoleBinding manifest granting group 'manager' secret read access in EVERY namespace:<br><br><code>apiVersion: {{c1::rbac.authorization.k8s.io/v1}}<br>kind: {{c2::ClusterRoleBinding}}<br>metadata:<br>  name: read-secrets-global<br>subjects:<br>- kind: {{c3::Group}}<br>  name: {{c4::manager}}<br>  apiGroup: rbac.authorization.k8s.io<br>roleRef:<br>  kind: {{c5::ClusterRole}}<br>  name: secret-reader<br>  apiGroup: rbac.authorization.k8s.io</code>
**Back Extra:** No namespace — the binding grants across ALL namespaces cluster-wide. roleRef.kind must be ClusterRole (can't point at a namespaced Role). roleRef is immutable — delete/recreate to change. subjects support User/Group/ServiceAccount kinds, names case-sensitive. Imperative equivalent: kubectl create clusterrolebinding read-secrets-global --clusterrole=secret-reader --group=manager.
**Tags:** k8s::cka src::session topic::rbac topic::yaml

---

<!-- note:1794496839778 model:Cloze -->
**Text:** Pod spec binding to ServiceAccount 'build-robot' with token mounting disabled:<br><br><code>apiVersion: v1<br>kind: Pod<br>metadata:<br>  name: my-pod<br>spec:<br>  serviceAccountName: {{c1::build-robot}}<br>  automountServiceAccountToken: {{c2::false}}<br>  containers:<br>  - name: app<br>    image: nginx</code>
**Back Extra:** Set ONLY at pod creation (or in a workload's pod template) — serviceAccountName is immutable on existing pods, like nodeName. Deprecated alias: spec.serviceAccount (set both to empty to remove). The SA must exist in the pod's namespace. Omit the field → 'default' SA auto-assigned. Pod-level automountServiceAccountToken overrides the SA's own setting.
**Tags:** k8s::cka src::session topic::rbac topic::yaml

---

<!-- note:1794496839780 model:Cloze -->
**Text:** CertificateSigningRequest manifest for user 'dev1':<br><br><code>apiVersion: {{c1::certificates.k8s.io/v1}}<br>kind: {{c2::CertificateSigningRequest}}<br>metadata:<br>  name: dev1<br>spec:<br>  request: &lt;base64 CSR&gt;<br>  signerName: {{c3::kubernetes.io/kube-apiserver-client}}<br>  usages: [{{c4::"client auth"}}]</code>
**Back Extra:** spec.request holds the base64-encoded CSR (openssl req -new -key user.key -out user.csr, then base64 -w0). After kubectl certificate approve dev1, the signed cert lands in .status.certificate — decode with base64 -d. Requires RBAC rights to create+approve CSRs. usages must include 'client auth' for kubeconfig use.
**Tags:** k8s::cka src::session topic::authentication topic::certificates topic::yaml

---

<!-- note:1794496839781 model:Cloze -->
**Text:** Assemble a kubeconfig for user 'dev1' — the four kubectl config commands:<br><br>{{c1::<code>kubectl config set-cluster prod --server=https://API:6443 --certificate-authority=ca.crt --embed-certs=true</code>}}<br>{{c2::<code>kubectl config set-credentials dev1 --client-certificate=dev1.crt --client-key=dev1.key --embed-certs=true</code>}}<br>{{c3::<code>kubectl config set-context dev1@prod --cluster=prod --user=dev1</code>}}<br>{{c4::<code>kubectl config use-context dev1@prod</code>}}
**Back Extra:** --embed-certs=true base64-inlines the CA into certificate-authority-data and cert+key into the user stanza — the file becomes fully self-contained/portable (that's what you email someone). Without it, kubectl looks for the referenced files on disk. Order: set-cluster → set-credentials → set-context → use-context. current-context in the file decides what plain 'kubectl get pods' uses.
**Tags:** k8s::cka src::session topic::authentication topic::kubectl

---

<!-- note:1794496839782 model:Cloze -->
**Text:** Pod manifest pulling from a private registry via Secret 'regcred':<br><br><code>apiVersion: v1<br>kind: Pod<br>metadata:<br>  name: private-reg<br>spec:<br>  containers:<br>  - name: app<br>    image: your.private.registry.example.com/janedoe/app:v1<br>  {{c1::imagePullSecrets}}:<br>  - name: {{c2::regcred}}</code>
**Back Extra:** imagePullSecrets is a LIST under spec — each entry references a Secret of type kubernetes.io/dockerconfigjson that must exist in the pod's namespace. The kubelet uses these credentials when pulling <private.registry>/app before the container starts. Same field exists on a ServiceAccount to cover all its pods.
**Tags:** k8s::cka src::session topic::images topic::secrets topic::yaml

---

<!-- note:1794496839785 model:Cloze -->
**Text:** NetworkPolicy manifest — isolate role=db pods, allow redis traffic:<br><br><code>apiVersion: {{c1::networking.k8s.io/v1}}<br>kind: {{c2::NetworkPolicy}}<br>metadata:<br>  name: test-network-policy<br>  namespace: default<br>spec:<br>  podSelector:<br>    matchLabels:<br>      role: {{c3::db}}<br>  policyTypes: [{{c4::Ingress, Egress}}]<br>  ingress:<br>  - from:<br>    - podSelector:<br>        matchLabels:<br>          role: frontend<br>    ports:<br>    - port: {{c5::6379}}<br>  egress:<br>  - to:<br>    - ipBlock:<br>        cidr: 10.0.0.0/24</code>
**Back Extra:** The doc's example isolates role=db pods for BOTH directions: ingress allows TCP 6379 from role=frontend pods (same ns), any pod in project=myproject namespaces, and 172.17.0.0/16 minus 172.17.1.0/24; egress allows TCP 5978 to 10.0.0.0/24. Apply with kubectl apply -f — but only works if your CNI enforces NetworkPolicy.
**Tags:** k8s::cka src::session topic::networking topic::networkpolicy topic::yaml

---

<!-- note:1794496839786 model:Cloze -->
**Text:** Default Kubernetes ports — control plane then workers:<br><br>Control plane (all TCP inbound):<br>{{c1::kube-apiserver}} → {{c2::6443}} (all components)<br>{{c3::etcd}} → {{c4::2379-2380}} (client API)<br>{{c5::kube-controller-manager}} → {{c6::10257}} (self)<br>{{c7::kube-scheduler}} → {{c8::10259}} (self)<br><br>Worker nodes:<br>{{c9::kubelet}} → {{c10::10250}}<br>kube-proxy → {{c11::10256}} (healthz)<br>NodePort Services → {{c12::30000-32767}} TCP+UDP
**Back Extra:** Direction is always INBOUND to the listed component. kubelet 10250 appears on BOTH control plane and workers (control plane reaches in for logs/exec/metrics). etcd can live externally or on custom ports. NodePort range is a default — change it and open the new range instead. kube-proxy 10256 is health/metrics only, NOT service traffic.
**Tags:** k8s::cka src::session topic::control-plane topic::networking

---

<!-- note:1794496839787 model:Cloze -->
**Text:** Kubernetes pod networking model — the requirements and who implements them:<br><br>K8s requires: every Pod gets {{c1::its own IP address}}; Pods on the same node can {{c2::communicate}}; Pods on different nodes can communicate {{c3::without NAT}}.<br><br>K8s does NOT implement this — the {{c4::container runtime}} invokes {{c5::CNI plugins}} on each node.<br><br>IP allocation: {{c6::network plugin}} → Pod IPs; {{c7::kube-apiserver}} → Service IPs; {{c8::kubelet/cloud-controller-manager}} → Node IPs.
**Back Extra:** K8s defines the WHAT, CNIs provide the HOW — the container runtime invokes CNI plugins per node. IP owners: network plugin→Pods, kube-apiserver→Services, kubelet/CCM→Nodes (all non-overlapping). Pod-to-pod = CNI; pod/service/external-to-service = Services. Runtime reads .conflist from --cni-conf-dir, executes plugin from --cni-bin-dir with ADD/DEL commands.
**Tags:** k8s::cka src::session topic::cni topic::networking topic::podnetwork

---

<!-- note:1794496839789 model:Cloze -->
**Text:** Persist container data with a named volume:<br><br>{{c1::<code>docker volume create data_volume</code>}}  # creates /var/lib/docker/volumes/data_volume<br>{{c2::<code>docker run -v data_volume:/data myimage</code>}}  # mount volume at /data<br><br>Bind mount — direct host path into the container:<br>{{c3::<code>docker run -v /home/me/code:/app myimage</code>}}
**Back Extra:** -v <host>:<container> covers BOTH: named volume (left side is a volume NAME → /var/lib/docker/volumes) and bind mount (left side is a host PATH like /home/me/code → /app). --mount is the explicit alternative: --mount type=volume,source=data_volume,target=/data or type=bind,source=/host/path,target=/app — clearer, validates options better.
**Tags:** k8s::cka topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794496839790 model:Cloze -->
**Text:** Create a volume on third-party storage via a volume plugin, then mount it:<br><br>{{c1::<code>docker volume create --driver=amazon-ebs --opt size=10 gb_vol</code>}}<br>{{c2::<code>docker run -v gb_vol:/data myapp</code>}}<br><br>Default local volume (no plugin):<br>{{c3::<code>docker volume create data_volume</code>}} → stored under {{c4::<code>/var/lib/docker/volumes</code>}}
**Back Extra:** Driver is chosen at CREATE time and sticks to the volume. --driver=<name> picks the plugin; --opt passes driver-specific settings (size, iops, type). Default (no --driver) = local → /var/lib/docker/volumes. Check installed drivers: docker info | grep -i volume or docker plugin ls.
**Tags:** k8s::cka topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794496715394 model:Cloze -->
**Text:** Build a cluster CA with openssl — private key, signing request, then self-signed root:<br><br>{{c1::<code>openssl genrsa -out ca.key 2048</code>}}  # CA private key<br>{{c2::<code>openssl req -new -key ca.key -subj "/CN=KUBERNETES-CA" -out ca.csr</code>}}  # CSR: public key + subject, unsigned<br>{{c3::<code>openssl x509 -req -in ca.csr -signkey ca.key -days 1000 -out ca.crt</code>}}  # CA signs its OWN cert with its own key<br><br>Every other cert swaps '-signkey ca.key' for '-CA ca.crt -CAkey ca.key' — issued by the CA.
**Back Extra:** The self-sign trick: -signkey uses the SAME ca.key that generated the CSR — only the root CA self-signs. Downstream certs get -CA/-CAkey instead, tying their trust back to ca.crt.
**Tags:** k8s::cka src::session topic::certificates topic::security topic::tls

---

<!-- note:1794498397437 model:Basic -->
**Front:** What are the three backup candidates for a Kubernetes cluster, and what does each capture?
**Back:** (1) Resource manifests — the YAML/object definitions; export with <code>kubectl get all --all-namespaces -o yaml &gt; backup.yaml</code> (caveat: 'all' does NOT include every type — no PVCs/PVs/CRDs/ClusterRoleBindings; enumerate with <code>kubectl api-resources</code> or use Velero). (2) etcd snapshot — the authoritative cluster state INCLUDING secrets and status; the only full point-in-time restore. (3) Persistent Volume data — application data lives on the volumes, backed up separately (snapshots, file copy, provider snapshots) and must be coordinated with the etcd snapshot for consistency. Declarative manifests in git remain the best practice — etcd/PV backups are for disaster recovery.
**Tags:** k8s::cka src::course-kodekloud topic::backup topic::cluster-maintenance

---

<!-- note:1794498397438 model:Basic -->
**Front:** How do you restore an etcd snapshot on a kubeadm cluster — and what's the CORRECTION to the old etcdctl command?
**Back:** CORRECTION: older courses/docs use <code>etcdctl snapshot restore</code>, but it's DEPRECATED since etcd 3.5 (removed in 3.6) — use <code>etcdutl snapshot restore snapshot.db --data-dir &lt;new-dir&gt;</code>. Restore creates a FRESH data directory with new member IDs — it does not rejoin an existing cluster. For kubeadm: stop the kube-apiserver, run etcdutl restore to a new dir, update the etcd static pod manifest's hostPath (<code>/etc/kubernetes/manifests/etcd.yaml</code>) and <code>etcd.local.dataDir</code> in the kubeadm-config ConfigMap to point at it, delete/restart the etcd static pod, then restart kube-apiserver. If etcd client URLs changed, apiservers need the new --etcd-servers flag.
**Tags:** k8s::cka src::course-kodekloud topic::backup topic::etcd

---

<!-- note:1794498397439 model:Basic -->
**Front:** What are the supported Kubernetes version-skew rules during upgrades?
**Back:** kube-apiserver is the reference and must be the HIGHEST version (in HA, apiserver instances within 1 minor of each other). kube-controller-manager, kube-scheduler, cloud-controller-manager: same or up to 1 minor OLDER than apiserver. kubelet and kube-proxy: must not be newer, may be up to 3 minor versions older (only 2 for versions <1.25). kubectl: within ±1 minor of apiserver. Nothing may be NEWER than the apiserver it talks to. Kubernetes supports the latest THREE minor releases (~1 year patches) — upgrade one minor at a time and never let the cluster fall outside the window. CORRECTION vs course: the course table says kubelet/proxy max 2 behind — current policy allows 3 for ≥1.25.
**Tags:** k8s::cka src::course-kodekloud topic::cluster-upgrade topic::versioning

---

<!-- note:1794498397440 model:Basic -->
**Front:** Walk through a kubeadm cluster upgrade from control plane to workers.
**Back:** (1) Back up etcd first + read release notes. (2) Upgrade the kubeadm BINARY on the upgrade host to the target minor (<code>apt-get install kubeadm=&lt;ver&gt;</code>). (3) <code>kubeadm upgrade plan</code> shows preflight checks + what's available. (4) <code>kubeadm upgrade apply &lt;version&gt;</code> updates the control-plane static pods (apiserver, controller-manager, scheduler) — workloads keep running but scheduling/controller actions pause briefly. (5) Per worker node, rolling: <code>kubectl drain &lt;node&gt;</code> → install kubelet/kubeadm packages → <code>kubeadm upgrade node config --kubelet-version &lt;ver&gt;</code> → <code>systemctl restart kubelet</code> → <code>kubectl uncordon &lt;node&gt;</code>. (6) Verify with <code>kubectl get nodes</code> (shows kubelet versions). Repeat per minor version.
**Tags:** k8s::cka src::course-kodekloud topic::cluster-upgrade topic::kubeadm

---

<!-- note:1794498397441 model:Basic -->
**Front:** What do <code>kubectl drain</code> and <code>kubectl uncordon</code> do, and why are they used in upgrades?
**Back:** drain marks the node unschedulable (like cordon) AND evicts all pods from it — respecting PodDisruptionBudgets so it won't evict pods that can't be rescheduled elsewhere. uncordon marks the node schedulable again. In upgrades you drain → upgrade kubelet/kubeadm on the empty node → uncordon, one node at a time for zero-downtime rolling upgrades. cordon/uncordon alone only toggle schedulability without evicting pods.
**Tags:** k8s::cka src::course-kodekloud topic::cluster-maintenance topic::kubectl

---

<!-- note:1794498397442 model:Basic -->
**Front:** Why does kubeadm require swap to be disabled, and how do you make it persistent?
**Back:** kubeadm preflight checks FAIL if swap is on — the kubelet can't properly account for memory and pod scheduling gets unpredictable. Disable immediately with <code>sudo swapoff -a</code>, then make it persistent by commenting out swap entries in /etc/fstab (e.g. <code>sudo sed -i.bak '/ swap / s/^/#/' /etc/fstab</code>) before running kubeadm init/join. Re-enable only if you fully understand the implications.
**Tags:** k8s::cka src::course-kodekloud topic::cluster-setup topic::kubeadm

---

<!-- note:1794498397443 model:Basic -->
**Front:** Why must the kubelet and containerd cgroup drivers match, and how do you align them on systemd systems?
**Back:** If kubelet uses cgroupfs while the runtime uses systemd (or vice versa), the kubelet can't correctly read container resource stats and enforcement misbehaves. On systemd distros both should use the systemd driver: check init with <code>ps -p 1 -o comm=</code>, then generate containerd config with <code>containerd config default | sed 's/SystemdCgroup = false/SystemdCgroup = true/' | sudo tee /etc/containerd/config.toml</code>, restart containerd, and verify <code>grep SystemdCgroup /etc/containerd/config.toml</code>. Kubelet side is set via KubeletConfiguration or --cgroup-driver.
**Tags:** k8s::cka src::course-kodekloud topic::cluster-setup topic::cri-oci topic::kubeadm

---

<!-- note:1794498397444 model:Basic -->
**Front:** How does kubeadm achieve HA for the control plane and etcd?
**Back:** Run an ODD number of control-plane nodes (3 or 5 — never even) so etcd always has quorum (majority: 2-of-3, 3-of-5); losing one node keeps the cluster working, losing a majority loses the datastore and the cluster can't change state (existing pods keep running but nothing new schedules). kubeadm HA uses stacked etcd (etcd runs as a static pod on each control-plane node alongside the other components) by default; external etcd topology is an alternative for larger clusters. First control-plane node inits, additional ones join with --control-plane using the certificate key from --upload-certs.
**Tags:** k8s::cka src::course-kodekloud topic::etcd topic::ha

---

<!-- note:1794498411293 model:Cloze -->
**Text:** Bootstrap a single control plane with kubeadm (v1.31 example):<br><br><code>sudo kubeadm init --apiserver-advertise-address &lt;cp-ip&gt; --pod-network-cidr 10.244.0.0/16 --upload-certs</code><br><br>{{c1::--apiserver-advertise-address}} = the IP other nodes use to reach the API server; {{c2::--pod-network-cidr}} must match your CNI's pod range (Flannel default 10.244.0.0/16); {{c3::--upload-certs}} prints a certificate key so additional control-plane nodes can join securely
**Back Extra:** After init, kubeadm prints next steps: copy /etc/kubernetes/admin.conf to ~/.kube/config for kubectl access, install a CNI (cluster stays NotReady until pod networking exists), and the kubeadm join command for workers.
**Tags:** k8s::cka src::course-kodekloud topic::cluster-setup topic::kubeadm

---

<!-- note:1794498411294 model:Cloze -->
**Text:** Give a node kubectl access after kubeadm init:<br><br><code>mkdir -p $HOME/.kube && sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config && sudo chown $(id -u):$(id -g) $HOME/.kube/config</code><br><br>{{c1::admin.conf}} is the kubeconfig kubeadm generated containing the cluster CA + client certs — copying it to ~/.kube/config is what makes kubectl work. Until a CNI is installed, <code>kubectl get nodes</code> shows the control-plane node as NotReady.
**Back Extra:** For worker nodes or restricted users you distribute a kubeconfig instead — never copy admin.conf to untrusted machines; it grants cluster-admin.
**Tags:** k8s::cka src::course-kodekloud topic::kubeadm topic::kubeconfig

---

<!-- note:1794498411295 model:Cloze -->
**Text:** Join a worker node to a kubeadm cluster:<br><br><code>kubeadm join &lt;cp-ip&gt;:6443 --token &lt;token&gt; --discovery-token-ca-cert-hash sha256:&lt;hash&gt;</code><br><br>{{c1::join}} needs the API server endpoint, a bootstrap {{c2::token}}, and the {{c3::discovery-token-ca-cert-hash}} proving the node trusts the cluster CA. kubeadm init prints this exact command; tokens expire (default 24h) — regenerate with <code>kubeadm token create --print-join-command</code>.
**Back Extra:** --upload-certs on init also prints a certificate key used by 'kubeadm join --control-plane' for adding MORE control-plane nodes.
**Tags:** k8s::cka src::course-kodekloud topic::cluster-setup topic::kubeadm

---

<!-- note:1794498411296 model:Cloze -->
**Text:** Required kernel/network sysctls before kubeadm init (write to /etc/sysctl.d/k8s.conf):<br><br><code>net.ipv4.ip_forward = 1<br>net.bridge.bridge-nf-call-iptables = 1<br>net.bridge.bridge-nf-call-ip6tables = 1</code><br><br>{{c1::ip_forward=1}} lets the node route pod traffic; the two {{c2::bridge-nf-call}} settings ensure bridged pod traffic passes through iptables so Service DNAT/kube-proxy rules apply. Apply with <code>sysctl --system</code>.
**Back Extra:** Missing these is a classic 'pods have IPs but can't reach services' root cause.
**Tags:** k8s::cka src::course-kodekloud topic::kubeadm topic::networking

---

<!-- note:1794498411297 model:Cloze -->
**Text:** Save an etcd snapshot on a kubeadm cluster:<br><br><code>ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot save snapshot.db</code><br><br>{{c1::ETCDCTL_API=3}} selects the v3 client; {{c2::--endpoints}} + the three PKI flags are REQUIRED because kubeadm's etcd is mTLS-only — without certs etcdctl can't connect. PKI lives under /etc/kubernetes/pki/etcd/ on control-plane nodes.
**Back Extra:** Run on a control-plane node (or with --endpoints pointing at an etcd member). Verify with 'ls -l snapshot.db' and 'etcdutl snapshot status snapshot.db'.
**Tags:** k8s::cka src::course-kodekloud topic::backup topic::etcd

---

<!-- note:1794498411303 model:Basic (and reversed card) -->
**Front:** What is etcd's role in Kubernetes?
**Back:** etcd is the cluster's authoritative distributed key-value store — ALL cluster state lives there: pod specs, service definitions, secrets, RBAC objects, everything the API server persists. Every kubectl write ultimately lands in etcd; if a majority of etcd members fail, the cluster can't change state (existing workloads keep running but nothing new schedules). kubeadm runs etcd as a static pod on control-plane nodes; back it up with etcdctl/etcdutl snapshots.
**Tags:** k8s::cka src::course-kodekloud topic::control-plane topic::etcd

---
