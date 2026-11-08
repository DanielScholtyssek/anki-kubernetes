# KCNA - Kubernetes and Cloud Native Associate — Container Orchestration

> Deck: `KCNA - Kubernetes and Cloud Native Associate` · Group: `Container Orchestration` · Notes: 55 · Models: Basic (and reversed card), Cloze, Many

<!-- note:1793752906095 model:Many -->
**Domain:** Docker vs containerd - dockershim
**Question:** Why did Kubernetes remove dockershim in v1.24?
**Options:** A. Docker Inc. changed its license, forcing removal<br>B. Docker Engine is not CRI-compatible; the kubelet-internal dockershim shim was vendor-specific complexity, so Kubernetes standardized on CRI runtimes (containerd, CRI-O)<br>C. Containers were deprecated in favor of VMs<br>D. containerd can only run images built by containerd
**Answer:** B (2) – Docker Engine is not CRI-compatible; the kubelet-internal dockershim shim was vendor-specific complexity, so Kubernetes standardized on CRI runtimes (containerd, CRI-O)
**Explanation:** Dockershim let the kubelet talk to Docker Engine, which predates and never implemented the CRI. It was removed in v1.24 to cut maintenance burden and align with open standards. Docker images still work — they follow OCI specs — and Docker Engine can still be used via the cri-dockerd shim.
**Sources:** <a href="https://kubernetes.io/blog/2022/05/03/dockershim-historical-context/" target="_blank">Kubernetes Blog - Dockershim: The Historical Context</a>
**Tags:** k8s::kcna src::session topic::cri-oci topic::docker

---

<!-- note:1793752906096 model:Many -->
**Domain:** Docker vs containerd - cri-dockerd
**Question:** Can a cluster still use Docker Engine as its container runtime today?
**Options:** A. No — Docker cannot run containers in Kubernetes anymore<br>B. Yes — natively, because Docker implements CRI<br>C. Yes — via cri-dockerd, a CRI shim maintained by Docker/Mirantis; though most clusters use containerd or CRI-O directly<br>D. Only if containerd is also installed
**Answer:** C (3) – Yes — via cri-dockerd, a CRI shim maintained by Docker/Mirantis; though most clusters use containerd or CRI-O directly
**Explanation:** Dockershim removal ended the BUILT-IN Docker path, not Docker itself. cri-dockerd re-adds the CRI bridge outside the kubelet. In practice, managed clusters run containerd or CRI-O — and note Docker Engine itself uses containerd under the hood.
**Sources:** <a href="https://kubernetes.io/blog/2022/05/03/dockershim-historical-context/" target="_blank">Kubernetes Blog - Dockershim: The Historical Context</a>
**Tags:** k8s::kcna src::session topic::cri-oci topic::docker

---

<!-- note:1793752906097 model:Many -->
**Domain:** OCI Image Portability
**Question:** Why can an image built with Docker run on a different runtime like containerd?
**Options:** A. Kubernetes converts the image at pull time<br>B. Both follow OCI standards: the image conforms to the image-spec format and containerd follows the runtime-spec<br>C. Docker must be installed on the node<br>D. containerd embeds a Docker engine
**Answer:** B (2) – Both follow OCI standards: the image conforms to the image-spec format and containerd follows the runtime-spec
**Explanation:** OCI image-spec standardizes how an image is packaged (manifest, config, layers); runtime-spec standardizes how it's executed. Any OCI-compliant runtime can run any OCI-compliant image — that's why Docker-built images run on containerd, CRI-O, etc. No conversion needed.
**Sources:** <a href="https://opencontainers.org/" target="_blank">Open Container Initiative</a>
**Tags:** k8s::kcna src::session topic::cri-oci topic::docker

---

<!-- note:1793752906098 model:Many -->
**Domain:** Containers vs VMs
**Question:** How do containers fundamentally differ from virtual machines?
**Options:** A. Each container boots its own guest OS kernel<br>B. Containers share the host OS kernel (isolated via namespaces/cgroups) with no guest OS — much lighter and faster than VMs<br>C. Containers require a hypervisor while VMs don't<br>D. VMs are lighter because they don't need isolation
**Answer:** B (2) – Containers share the host OS kernel (isolated via namespaces/cgroups) with no guest OS — much lighter and faster than VMs
**Explanation:** A VM runs a full guest OS on a hypervisor — heavyweight, slow to boot. A container is just an isolated process set on the host: it shares the host kernel and gets its own view of processes/network/filesystems. That's why containers start in milliseconds and pack denser.
**Sources:** <a href="https://docs.docker.com/get-started/docker-overview/" target="_blank">Docker Official Documentation - Docker Overview</a>
**Tags:** k8s::kcna src::session topic::container-orchestration topic::docker

---

<!-- note:1793752906099 model:Many -->
**Domain:** Image vs Container
**Question:** What is the difference between a container image and a container?
**Options:** A. The image is the read-only template/package; the container is a running instance of it<br>B. The container is the template; the image is the running process<br>C. They are two names for the same thing<br>D. Images run on VMs; containers run on bare metal
**Answer:** A (1) – The image is the read-only template/package; the container is a running instance of it
**Explanation:** An image packages the app + dependencies as a sharable, versioned artifact (built once, stored in a registry). A container is what runs when you instantiate the image — the live isolated environment with its own processes, network and filesystem. One image → many containers.
**Sources:** <a href="https://docs.docker.com/get-started/docker-overview/" target="_blank">Docker Official Documentation - Docker Overview</a>
**Tags:** k8s::kcna src::session topic::cri-oci topic::docker

---

<!-- note:1793752918686 model:Basic (and reversed card) -->
**Front:** What is the Container Runtime Interface (CRI)?
**Back:** The standard gRPC plugin interface between the kubelet and the container runtime on each node. Any runtime implementing CRI (containerd, CRI-O) can run containers under Kubernetes — that's what makes runtimes swappable. The CRI-compliant runtimes in turn follow OCI standards (image-spec, runtime-spec).
**Tags:** k8s::kcna src::session topic::container-orchestration topic::cri-oci

---

<!-- note:1793753618569 model:Many -->
**Domain:** Container Runtime - CRI benefit
**Question:** What are the benefits of using container runtimes that support the CRI? (Select all that apply)
**Options:** A. It enables automatic scaling of container instances<br>B. It enables container runtimes to be developed independently of Kubernetes<br>C. It provides better compatibility and standardization across container runtimes<br>D. It allows for direct communication between containers
**Answer:** B, C – runtimes implement CRI independently of Kubernetes; the standard interface gives compatibility and standardization across runtimes
**Explanation:** CRI defines one standard interface between the kubelet and any container runtime. That standardization is the core benefit: compliant runtimes (containerd, CRI-O, cri-dockerd) plug in interchangeably, giving better compatibility and standardization across runtimes (C); and runtime developers only need to satisfy the interface, so runtimes can be built and evolved independently of Kubernetes itself (B). A and D are unrelated to CRI — scaling is the orchestrator's job and CNI, not CRI, handles container networking.
**Sources:** <a href="https://kubernetes.io/docs/concepts/architecture/cri/" target="_blank">Kubernetes Documentation - Container Runtime Interface (CRI)</a>
**Tags:** k8s::kcna src::session topic::container-orchestration topic::cri-oci

---

<!-- note:1793820261547 model:Cloze -->
**Text:** Container resource stanza — where requests and limits live:<br><br><code>containers:<br>- name: app<br>  {{c1::resources}}:<br>    {{c2::requests}}:<br>      {{c3::cpu}}: "{{c4::250m}}"<br>      {{c5::memory}}: "{{c6::256Mi}}"<br>    {{c7::limits}}:<br>      cpu: "500m"<br>      memory: "512Mi"</code>
**Back Extra:** Per-CONTAINER field — a pod's effective request is the sum of its containers' requests. requests = scheduling floor, limits = runtime ceiling. Units: m = millicores (250m = 0.25 CPU); Mi/Gi = binary memory (2^20/2^30), M/G = decimal.
**Tags:** k8s::kcna src::session topic::resources topic::yaml

---

<!-- note:1793920790860 model:Many -->
**Domain:** Storage - zone topology
**Question:** Pod error "no available volume zone" likely means:
**Options:** A. CoreDNS down<br>B. PV/PVC zone topology mismatch with available nodes<br>C. Service selector issue<br>D. ImagePullBackOff
**Answer:** B (2) – PV/PVC zone topology mismatch with available nodes
**Explanation:** Zonal volumes are block storage bound to ONE availability zone — an EBS/GCE-PD/Azure-Disk volume in us-east-1a physically cannot attach to a node in us-east-1b. Kubernetes encodes that constraint as nodeAffinity on the PV (topology.kubernetes.io/zone=<zone>), so the scheduler only places pods using that PVC on nodes in the volume's zone. The error means the volume's zone and the pod's schedulable nodes don't overlap: the PVC was bound in zone A (Immediate binding mode provisions at PVC creation, blind to where the pod will run) while the pod's nodeSelector/affinity/tolerations only allow zone B — or the zone-A nodes are cordoned, full, or gone. The fix direction: volumeBindingMode: WaitForFirstConsumer delays provisioning until pod scheduling so the volume is created in the pod's zone (allowedTopologies can further restrict zones), or relax the pod's node constraints. Distractors: CoreDNS is DNS only, a selector issue breaks Service endpoints not mounts, ImagePullBackOff is an image problem.
**Sources:** <a href="https://kubernetes.io/docs/concepts/storage/storage-classes/#volume-binding-mode" target="_blank">Kubernetes Docs - Storage Classes: Volume binding mode</a>
**Tags:** k8s::kcna src::session topic::scheduling topic::storage topic::topology

---

<!-- note:1794006447940 model:Many -->
**Domain:** Images - name expansion
**Question:** In a Pod spec, image: nginx is shorthand for what fully-qualified image?
**Options:** A. docker.io/library/nginx:latest<br>B. nginx.docker.io/library/latest<br>C. docker.io/nginx:library<br>D. index.docker.io/nginx:stable
**Answer:** A (1) – docker.io/library/nginx:latest — registry docker.io, namespace library (official images), tag latest
**Explanation:** An image name is REGISTRY/REPOSITORY:TAG with three independent defaults: no registry → docker.io (Docker Hub); official-library images live under the library/ namespace (docker.io/library/nginx); no tag → latest. So image: nginx is shorthand for docker.io/library/nginx:latest. Your own Docker Hub images resolve to docker.io/<your-username>/<image> — the middle path segment is the namespace/account, not part of the registry.
**Sources:** <a href="https://kubernetes.io/docs/concepts/containers/images/" target="_blank">Kubernetes Docs - Container Images</a>
**Tags:** k8s::kcna src::session topic::containers topic::images

---

<!-- note:1794006447941 model:Many -->
**Domain:** Images - name parts
**Question:** For image: quay.io/myorg/api:v2, which part is the registry?
**Options:** A. quay.io — the registry is the first path segment when it contains a dot or port<br>B. myorg — the first path segment is always the registry<br>C. api — the last segment is the registry<br>D. quay.io/myorg — registry and namespace are one field
**Answer:** A (1) – quay.io — the registry is everything before the first slash that contains a dot/colon or is 'localhost'
**Explanation:** Image name anatomy: [registry/][namespace/]repository[:tag]. The registry is identified by a '.' or ':' in the first path segment (quay.io, gcr.io, localhost:5000) or the literal 'localhost' — docker.io is assumed when absent. Everything between registry and repo is the namespace/account (yourorg, library). With your own Docker Hub account 'acme', image: acme/api expands to docker.io/acme/api:latest — registry docker.io, namespace acme, repo api.
**Sources:** <a href="https://kubernetes.io/docs/concepts/containers/images/" target="_blank">Kubernetes Docs - Container Images</a>
**Tags:** k8s::kcna src::session topic::containers topic::images

---

<!-- note:1794006447943 model:Many -->
**Domain:** Registry Auth - create command
**Question:** Which command creates a Secret with Docker registry credentials?
**Options:** A. kubectl create secret docker-registry regcred --docker-server=... --docker-username=... --docker-password=... --docker-email=...<br>B. kubectl create secret tls regcred --cert=... --key=...<br>C. kubectl create configmap regcred --from-literal=auth=...<br>D. kubectl create secret generic regcred --type=kubernetes.io/registry
**Answer:** A (1) – kubectl create secret docker-registry regcred --docker-server=... --docker-username=... --docker-password=... --docker-email=...
**Explanation:** kubectl create secret docker-registry builds the Secret imperatively: --docker-server is the registry FQDN (use https://index.docker.io/v1/ for Docker Hub, or your private registry's address), plus --docker-username/--docker-password/--docker-email. kubectl creates it as type kubernetes.io/dockerconfigjson in your current namespace. Doc warning: passing --docker-password on the CLI can leak it into shell history — prefer the --from-file=.dockerconfigjson variant when you already ran docker login.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/" target="_blank">Kubernetes Docs - Pull an Image from a Private Registry</a>
**Tags:** k8s::kcna src::session topic::images topic::kubectl topic::secrets

---

<!-- note:1794006447945 model:Many -->
**Domain:** Registry Auth - from dockerconfigjson
**Question:** You already ran docker login — how do you turn that credential into a cluster Secret?
**Options:** A. kubectl create secret generic regcred --from-file=.dockerconfigjson=~/.docker/config.json --type=kubernetes.io/dockerconfigjson<br>B. kubectl create secret docker-registry regcred --from-file=config.json<br>C. Copy ~/.docker/config.json into the pod as a mounted volume<br>D. kubectl create secret generic regcred --from-literal=.dockerconfigjson=$(cat config.json)
**Answer:** A (1) – kubectl create secret generic regcred --from-file=.dockerconfigjson=~/.docker/config.json --type=kubernetes.io/dockerconfigjson
**Explanation:** If you already ran docker login locally, reuse ~/.docker/config.json directly: kubectl create secret generic regcred --from-file=.dockerconfigjson=<path> --type=kubernetes.io/dockerconfigjson. The critical detail: the data key MUST be named .dockerconfigjson (that's what the kubelet looks for) and type must be kubernetes.io/dockerconfigjson. The file's auths entries carry base64 username:password per registry — same format docker uses.
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/" target="_blank">Kubernetes Docs - Pull an Image from a Private Registry</a>
**Tags:** k8s::kcna src::session topic::images topic::kubectl topic::secrets

---

<!-- note:1794006612605 model:Many -->
**Domain:** SecurityContext - volumes/fsGroup
**Question:** Which securityContext field controls group ownership of mounted volumes, and where must it be set?
**Options:** A. fsGroup — it makes volume contents owned by that GID; it only exists at pod level because container settings don't touch volumes<br>B. runAsUser — it controls volume permissions per-container<br>C. privileged — it grants volume admin rights<br>D. readOnlyRootFilesystem — it protects volumes from writes
**Answer:** A (1) – fsGroup — it makes volume contents owned by that GID; it only exists at pod level because container settings don't touch volumes
**Explanation:** fsGroup is a PodSecurityContext-only field: it sets the group ownership of mounted volumes so containers can read/write shared data without running as root. Doc rule: 'Container settings do not affect the Pod's Volumes' — so fsGroup, supplementalGroups, fsGroupChangePolicy and supplementalGroupsPolicy exist ONLY under spec.securityContext. Companion fields: fsGroupChangePolicy (OnRootMismatch skips recursive chown for speed) and supplementalGroupsPolicy (Merge default vs Strict — controls whether the image's /etc/group memberships get merged in, a beta feature since v1.33).
**Sources:** <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/" target="_blank">Kubernetes Docs - Configure a Security Context for a Pod or Container</a>
**Tags:** k8s::kcna src::session topic::podsecurity topic::security topic::storage

---

<!-- note:1794009250197 model:Many -->
**Domain:** CNI - ipMasquerade
**Question:** What does the "ipMasquerade" field in a Container Network Interface (CNI) plugin configuration file determine?
**Options:** A. Whether the plugin configuration file is valid<br>B. Whether the bridge network should have an assigned IP address<br>C. Whether a NAT rule should be added for IP masquerading<br>D. Whether the plugin supports IP masquerading
**Answer:** C (3) – Whether a NAT rule should be added for IP masquerading
**Explanation:** ipMasquerade (written ipMasq in the bridge plugin) is the on/off switch telling the CNI plugin to program iptables NAT MASQUERADE rules: pod traffic leaving the node gets its source IP rewritten to the node's IP — SNAT, same trick as a home router. It's needed because pod CIDR addresses (10.x) aren't routable outside the cluster — without masquerade, pod→internet egress has no return path. The field CONFIGURES masquerading; it doesn't validate the config file (schema does that), assign the bridge IP (that's ipam/isGateway), or declare plugin capability (capability is fixed — this is the per-config toggle).
**Sources:** <a href="https://kubernetes.io/docs/concepts/cluster-administration/networking/" target="_blank">Kubernetes Docs - Cluster Networking</a>
**Tags:** k8s::kcna src::session topic::cni topic::networking

---

<!-- note:1794009827922 model:Many -->
**Domain:** CNI - isGateway
**Question:** What does the "isGateway" field in a Container Network Interface (CNI) plugin configuration file determine?
**Options:** A. Whether the bridge network should act as a gateway<br>B. Whether the bridge network should have an assigned IP address<br>C. Whether the plugin configuration file is valid<br>D. Whether the plugin supports gateway functionality
**Answer:** A (1) – Whether the bridge network should act as a gateway
**Explanation:** isGateway (default false) tells the bridge plugin to assign the bridge the IPAM-provided gateway IP — turning the bridge into the containers' gateway so pod traffic can route out of the pod network. Without it the bridge is pure L2 (container-to-container on the host only, no routing). Getting an IP is the mechanism; acting as gateway is the purpose — pods' default route points at the bridge IP. Sibling field isDefaultGateway additionally makes that IP the containers' default route. Like ipMasq, it CONFIGURES behavior — doesn't validate the file or declare plugin capability.
**Sources:** <a href="https://www.cni.dev/plugins/current/main/bridge/" target="_blank">CNI Docs - bridge plugin</a>
**Tags:** k8s::kcna src::session topic::cni topic::networking

---

<!-- note:1794009945361 model:Many -->
**Domain:** CNI - ipam type
**Question:** In a CNI plugin configuration file, what does the "type" field indicate when set to "host-local" under the IPAM section?
**Options:** A. The type of DNS resolution method used for pods<br>B. The type of network protocol used for pod communication<br>C. The type of network interface used for communication<br>D. The type of IP address management used for pods
**Answer:** D (4) – The type of IP address management used for pods
**Explanation:** ipam.type selects WHICH IPAM plugin allocates pod IPs: host-local = file-based allocation on each node from its podCIDR slice (the standard choice — no central allocator needed); dhcp delegates to an external DHCP server; static uses fixed IPs; whereabouts coordinates a shared pool across nodes. Watch the nesting: the TOP-LEVEL type field picks the main plugin (bridge, vlan…), while ipam.type picks only the address allocator — two different 'type' fields at different levels of the same JSON.
**Sources:** <a href="https://www.cni.dev/plugins/current/ipam/host-local/" target="_blank">CNI Docs - host-local IPAM plugin</a>
**Tags:** k8s::kcna src::session topic::cni topic::networking

---

<!-- note:1794010073685 model:Many -->
**Domain:** CNI - runtime responsibility
**Question:** What is the responsibility of a container runtime in terms of networking?
**Options:** A. All of the options are correct<br>B. Identifying and attaching namespaces to the appropriate network<br>C. Calling the appropriate network plugin<br>D. Creating container network namespaces
**Answer:** A (1) – All of the options are correct
**Explanation:** All three are genuine runtime jobs in the CNI flow: the container runtime (containerd/CRI-O) creates each container's network namespace, selects which CNI configuration applies (the .conflist in /etc/cni/net.d/), and invokes the CNI plugin's ADD/DEL commands to attach that namespace to the configured network. The kubelet delegates this via CRI — the runtime is the component that actually calls CNI; the plugin then does the hands-on work (veth pair, bridge, IPAM). Runtime orchestrates, plugin executes.
**Sources:** <a href="https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/" target="_blank">Kubernetes Docs - Network Plugins</a>
**Tags:** k8s::kcna src::session topic::cni topic::cri-oci topic::networking

---

<!-- note:1794016331746 model:Many -->
**Domain:** Pod Networking - CNI commands
**Question:** What commands does a CNI plugin implement for the container lifecycle?
**Options:** A. ADD connects the container to the network; DEL tears the interfaces down; plus CHECK and VERSION<br>B. Only ADD and DELETE — no other commands exist<br>C. START and STOP like systemd services<br>D. Only VERSION — the runtime does all the work
**Answer:** A (1) – ADD connects the container to the network; DEL tears the interfaces down; plus CHECK and VERSION
**Explanation:** A CNI plugin is an executable that implements spec commands: ADD — called when a container is created, attaches its interface to the network (veth, IP, routes); DEL — called on teardown, removes interfaces and releases the IP; CHECK — verifies config is still applied (optional); VERSION — reports supported spec version. The runtime invokes these per container lifecycle — 'the script' your lecture demoed is exactly this ADD/DEL contract.
**Sources:** <a href="https://www.cni.dev/docs/spec/" target="_blank">CNI Spec - Container Network Interface</a>
**Tags:** k8s::kcna src::session topic::cni topic::networking

---

<!-- note:1794016331747 model:Many -->
**Domain:** Pod Networking - cni dirs
**Question:** What do --cni-conf-dir and --cni-bin-dir point at?
**Options:** A. kubelet --cni-conf-dir=/etc/cni/net.d holds the .conflist configs; --cni-bin-dir=/opt/cni/bin holds the plugin executables<br>B. --cni-conf-dir holds binaries; --cni-bin-dir holds configs<br>C. Both flags point at /etc/cni by default<br>D. These are containerd flags, not kubelet flags
**Answer:** A (1) – kubelet --cni-conf-dir=/etc/cni/net.d holds the .conflist configs; --cni-bin-dir=/opt/cni/bin holds the plugin executables
**Explanation:** Two kubelet flags wire CNI in: --cni-conf-dir (default /etc/cni/net.d) contains the network CONFIG files — JSON .conflist files naming which plugins/IPAM to use (this is where 'bridge', 'host-local' etc. get selected); --cni-bin-dir (default /opt/cni/bin) contains the plugin EXECUTABLES the configs point at. Flow: kubelet reads the conflist → picks plugin name → runtime executes that binary from bin-dir with ADD + the container's ID/netns. Wrong dir or missing binary = pods stuck in ContainerCreating.
**Sources:** <a href="https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/parameters/" target="_blank">Kubernetes Docs - kubelet parameters</a>
**Tags:** k8s::kcna src::session topic::cni topic::kubelet topic::networking

---

<!-- note:1794076936965 model:Many -->
**Domain:** CNI Config - conflist structure
**Question:** What are the top-level keys of a CNI .conflist network configuration?
**Options:** A. cniVersion/cniVersions, name, and plugins[] — bridge/ipam/dns live INSIDE each plugin object<br>B. bridge, ipam, dns, and name at the top level<br>C. Only name and type — everything else is optional<br>D. YAML keys: apiVersion, kind, metadata like other K8s objects
**Answer:** A (1) – cniVersion/cniVersions, name, and plugins[] — bridge/ipam/dns live INSIDE each plugin object
**Explanation:** A .conflist network config is a JSON object with top-level keys: cniVersion (spec version string like "1.1.0") or cniVersions (list of supported versions), name (unique network name per host), and plugins — an array of plugin config objects. Fields like type, bridge, ipam, dns, capabilities are PER-PLUGIN, nested inside each plugins[] entry — not top-level. Think of it as: envelope (version+name) → list of plugin instructions.
**Sources:** <a href="https://www.cni.dev/docs/spec/" target="_blank">CNI Spec - Network configuration format</a>
**Tags:** k8s::kcna src::session topic::cni topic::networking topic::yaml

---

<!-- note:1794076936966 model:Many -->
**Domain:** CNI Config - type binary
**Question:** In a CNI plugin config, what does the "type" field specify?
**Options:** A. The filename of the plugin executable in the CNI bin dir — type: bridge → /opt/cni/bin/bridge<br>B. The network type like bridge or vlan only<br>C. The plugin's version number<br>D. Whether the plugin is enabled or disabled
**Answer:** A (1) – The filename of the plugin executable in the CNI bin dir — type: bridge → /opt/cni/bin/bridge
**Explanation:** Each plugin object's "type" field names the plugin BINARY on disk — it's how the config points at the executable: type: "bridge" makes the runtime look for /opt/cni/bin/bridge. This is the exact mechanism from your lecture: config in net.d identifies the script name, runtime finds that binary in the bin dir and executes it with ADD/DEL. Same for ipam.type — it names the IPAM plugin's executable, not a behavior.
**Sources:** <a href="https://www.cni.dev/docs/spec/" target="_blank">CNI Spec - Plugin configuration objects</a>
**Tags:** k8s::kcna src::session topic::cni topic::networking

---

<!-- note:1794076936967 model:Many -->
**Domain:** CNI Config - plugin chaining
**Question:** What does the plugins[] array in a .conflist enable?
**Options:** A. Multiple plugins can be chained — a main plugin (bridge) plus meta plugins (tuning, portmap, firewall) that adjust the result<br>B. Only one plugin can ever be configured per network<br>C. plugins[] lists backup plugins used if the first fails<br>D. Each plugins[] entry runs on a different node
**Answer:** A (1) – Multiple plugins can be chained — a main plugin (bridge) plus meta plugins (tuning, portmap, firewall) that adjust the result
**Explanation:** The plugins[] array enables CHAINING: the runtime executes each plugin in order, passing each one's result (prevResult) to the next. Typically the first entry is the 'interface' plugin that creates the interface+IP (bridge), followed by 'meta' plugins that modify the already-created interface — tuning (sysctl, MAC), portmap (hostPort mapping), firewall, bandwidth. Spec v0.3.0 introduced chaining; v1.0.0 then REQUIRED the plugins array even for a single plugin.
**Sources:** <a href="https://www.cni.dev/docs/spec/" target="_blank">CNI Spec - plugin chaining</a>
**Tags:** k8s::kcna src::session topic::cni topic::networking

---

<!-- note:1794076936968 model:Many -->
**Domain:** CNI Config - spec versions
**Question:** Since CNI spec v1.0.0, can a network config omit the plugins[] array for a single plugin?
**Options:** A. No — spec v1.0.0 removed non-list configs; every network config must use the plugins[] array<br>B. Yes — bare single-plugin configs are still valid<br>C. Only on Windows nodes<br>D. Only if cniVersion is below 1.0.0
**Answer:** A (1) – No — spec v1.0.0 removed non-list configs; every network config must use the plugins[] array
**Explanation:** Spec history that matters: v0.3.0 added plugin chaining + rich results; v0.4.0 added CHECK; v1.0.0 REMOVED non-list configurations — a bare single-plugin JSON without plugins[] is invalid in modern CNI; v1.1.0 added STATUS and GC commands plus cniVersions for multi-version support. So even a one-plugin network must be wrapped: {"cniVersion":"1.0.0","name":"x","plugins":[{"type":"bridge",...}]}. The cniVersions list field lets one config declare which spec versions it supports.
**Sources:** <a href="https://www.cni.dev/docs/spec/" target="_blank">CNI Spec - version history</a>
**Tags:** k8s::kcna src::session topic::cni topic::networking

---

<!-- note:1794076936969 model:Many -->
**Domain:** CNI Config - env params
**Question:** What parameters does the container runtime pass to CNI plugins? (Select all that apply)
**Options:** A. CNI_CONTAINERID — the unique container identifier<br>B. CNI_NETNS — path to the container's network namespace<br>C. CNI_IFNAME — the interface name to create in the container<br>D. CNI_PATH — the plugin binary search path
**Answer:** A, B, C, D – CNI_CONTAINERID, CNI_NETNS, CNI_IFNAME, CNI_ARGS/CNI_PATH all passed by the runtime
**Explanation:** (Select all that apply) The runtime passes per-attachment context to plugins via env vars/parameters: CNI_CONTAINERID (unique container ID), CNI_NETNS (path to the container's network namespace, e.g. /run/netns/...), CNI_IFNAME (interface name to create inside the container), CNI_ARGS (extra key-value args), and CNI_PATH (the plugin search path so plugins can find delegated binaries like IPAM). These are what the ADD/DEL calls carry — the 'name and namespaceID' your lecture mentioned.
**Sources:** <a href="https://www.cni.dev/docs/spec/" target="_blank">CNI Spec - Attachment Parameters</a>
**Tags:** k8s::kcna src::session topic::cni topic::networking

---

<!-- note:1794076936970 model:Many -->
**Domain:** CNI Config - lifecycle rules
**Question:** Which lifecycle rules does the CNI spec mandate? (Select all that apply)
**Options:** A. The runtime creates the network namespace before invoking plugins and cleans it up itself<br>B. Every ADD must eventually be followed by a DEL — even if the ADD failed<br>C. The network config must not change between ADD and DEL<br>D. Plugins create and destroy the network namespace themselves
**Answer:** A, B, C – runtime creates netns first; add must be followed by delete; delete runs even if add fails; runtime owns netns cleanup
**Explanation:** (Select all that apply) Spec-mandated lifecycle: the runtime creates the container's network namespace BEFORE invoking any plugin and is responsible for cleaning it up afterward; every ADD must eventually be followed by a DEL (even if ADD failed); DEL may be retried; config must not change between add and delete; runtimes may parallelize across containers but not for the same container; GC operations must not overlap with add/delete.
**Sources:** <a href="https://www.cni.dev/docs/spec/" target="_blank">CNI Spec - Lifecycle & Ordering</a>
**Tags:** k8s::kcna src::session topic::cni topic::networking

---

<!-- note:1794076936975 model:Cloze -->
**Text:** Spec example — 'dbnet' conflist chaining bridge + tuning + portmap:<br><br><code>{<br>  cniVersion: {{c1::"1.1.0"}},<br>  name: {{c2::dbnet}},<br>  plugins: [<br>    { type: {{c3::bridge}}, bridge: cni0,<br>      ipam: { type: {{c4::host-local}}, subnet: 10.1.0.0/16 } },<br>    { type: {{c5::tuning}}, capabilities: { mac: true } },<br>    { type: {{c6::portmap}}, capabilities: { portMappings: true } }<br>  ]<br>}</code>
**Back Extra:** dbnet example from the spec: bridge creates cni0 + assigns IP via host-local IPAM (10.1.0.0/16, gw 10.1.0.1, default route); dns sets pod resolv.conf nameserver; tuning adjusts sysctls/MAC via capabilities; portmap exposes hostPort mappings via capabilities.portMappings. 'type' in each entry = binary filename in /opt/cni/bin. ipam is itself a plugin delegation (ipam.type = IPAM binary).
**Tags:** k8s::kcna src::session topic::cni topic::networking topic::yaml

---

<!-- note:1794078034941 model:Many -->
**Domain:** Container Images - Dockerfile CMD
**Question:** In a container image built from a Dockerfile, what is the purpose of the CMD instruction?
**Options:** A. To specify a command that always runs at build time<br>B. To copy files into the image<br>C. To provide default arguments for the ENTRYPOINT instruction<br>D. To define environment variables
**Answer:** C (3) – To provide default arguments for the ENTRYPOINT instruction
**Explanation:** CMD provides DEFAULT arguments — consumed by ENTRYPOINT if one exists, or executed as the command itself if it doesn't. It's overridable at runtime: 'docker run image myargs' replaces CMD's args but keeps ENTRYPOINT; 'docker run image --entrypoint x' replaces ENTRYPOINT. Contrast: ENTRYPOINT defines the fixed executable (the 'what'), CMD defines default params (the 'how') — the entrypoint+cmd pair lets you ship one image used many ways (e.g. ENTRYPOINT ["/docker-entrypoint.sh"], CMD ["postgres"]).
**Sources:** <a href="https://docs.docker.com/reference/dockerfile/#cmd" target="_blank">Docker Docs - Dockerfile CMD</a>
**Tags:** k8s::kcna src::session topic::containers topic::dockerfile

---

<!-- note:1794080037314 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** What is the fundamental reason Kubernetes uses Pods as the smallest deployable unit, rather than individual containers directly?
**Options:** A. To simplify network configuration for containers<br>B. To enable co-location and shared resources for containers<br>C. To enforce stricter security boundaries than containers<br>D. To provide a unique IP address per container<br>E. To reduce container image size
**Answer:** B – To enable co-location and shared resources for containers
**Explanation:** Pods allow tightly coupled containers to share resources<br>like network namespace (IP, port space) and storage volumes, facilitating<br>communication and data sharing for helper or sidecar patterns.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037315 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** What core benefit does containerization (e.g., using Docker or containerd) provide for application deployment?
**Options:** A. Automatic scaling of applications<br>B. Abstraction of the underlying operating system and kernel<br>C. Consistent runtime environment across different machines<br>D. Built-in service discovery and load balancing<br>E. Secure by default inter-container communication
**Answer:** C – Consistent runtime environment across different machines
**Explanation:** Containers bundle an application with its dependencies,<br>ensuring it runs consistently regardless of the host environment, solving<br>”it works on my machine” problems.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037316 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** Which part of the <b>Container Runtime Interface (CRI)</b> specification is containerd primarily responsible for implementing?
**Options:** A. Image distribution and storage<br>B. Low-level container execution and lifecycle management<br>C. Network namespace creation and IP address assignment<br>D. Defining container image format standards<br>E. Implementing pod-level resource sharing
**Answer:** B – Low-level container execution and lifecycle management
**Explanation:** containerd is a core container runtime that manages the<br>complete container lifecycle on a single host – image transfer, storage,<br>container execution, supervision, and network attachments.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037317 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** A stateful application requires storage that persists even if its Pod is rescheduled to another Node. Which Kubernetes objects are essential for this?
**Options:** A. ConfigMap and Secret<br>B. PersistentVolume (PV) and PersistentVolumeClaim (PVC)<br>C. EphemeralVolume and HostPath volume<br>D. Service and EndpointSlice<br>E. Job and CronJob
**Answer:** B – PersistentVolume (PV) and PersistentVolumeClaim (PVC)
**Explanation:** A PersistentVolume (PV) represents a piece of storage,<br>and a PersistentVolumeClaim (PVC) is a request for that storage by a<br>user/Pod. This decoupling allows storage to outlive Pods.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037318 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** Why are Open Standards, like those defined by the Open Container Initiative (OCI), critical for the cloud native ecosystem?
**Options:** A. They guarantee better application performance<br>B. They enforce specific vendor implementations<br>C. They promote interoperability and prevent vendor lock-in<br>D. They reduce the need for security patching<br>E. They simplify the user interface of cloud platforms
**Answer:** C – They promote interoperability and prevent vendor lock-in
**Explanation:** Open standards (e.g., OCI for container formats/runtimes,<br>CNI for networking, CRI for runtimes) ensure that different tools and<br>platforms can work together seamlessly, giving users choice and preventing<br>vendor lock-in.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037319 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** Which OCI specification defines the format of a container image?
**Options:** A. Runtime Specification<br>B. Image Specification<br>C. Distribution Specification<br>D. Network Specification<br>E. Storage Specification
**Answer:** B – Image Specification
**Explanation:** The OCI Image Specification defines how to create and<br>package a container image, ensuring interoperability across different container tools and runtimes that adhere to the standard.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037320 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** In the context of container security, what does ”least privilege” primarily refer to?
**Options:** A. Running containers with minimal resource requests<br>B. Granting containers only the permissions they absolutely need<br>C. Using the smallest possible base container images<br>D. Limiting network access to containers<br>E. Encrypting all data within the container
**Answer:** B – Granting containers only the permissions they absolutely need
**Explanation:** The principle of least privilege means that containers (and<br>their processes) should run with only the capabilities and permissions<br>essential for their function, reducing the potential impact of a compromise.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037321 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** What is the main benefit of using container orchestration systems like Kubernetes?
**Options:** A. Simplifying code writing<br>B. Automating deployment scaling<br>C. Reducing storage costs<br>D. Improving network latency
**Answer:** B – Automating deployment scaling
**Explanation:** Orchestrators automate the deployment, scaling, management, and networking of containerized applications.<br><br>Domain: Container Orchestration
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037322 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** Which of these is a standard specified by the OCI (Open Container Initiative)?
**Options:** A. Docker<br>B. Kubernetes<br>C. Image Specification<br>D. Istio
**Answer:** C – Image Specification
**Explanation:** The OCI defines standards for container image formats (Image Specification) and runtime (Runtime Specification).
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037323 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** Which container runtime is most commonly associated with Kubernetes and implements the CRI (Container Runtime Interface)?
**Options:** A. Docker (dockershim)<br>B. containerd<br>C. rkt<br>D. LXC
**Answer:** B – containerd
**Explanation:** containerd is a widely used container runtime focused on simplicity, robustness, and portability, fully implementing the CRI.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037324 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** What is the role of a CNI (Container Network Interface) plugin in Kubernetes?
**Options:** A. Managing storage volumes<br>B. Providing container networking<br>C. Scheduling Pods<br>D. Securing the API server
**Answer:** B – Providing container networking
**Explanation:** Explanation: CNI plugins are responsible for configuring network interfaces for containers and managing IP address allocation within the cluster.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037325 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** What Kubernetes object represents a piece of storage in the cluster, provisioned by an administrator or dynamically?
**Options:** A. PersistentVolumeClaim (PVC)<br>B. StorageClass<br>C. PersistentVolume (PV)<br>D. Volume
**Answer:** C – PersistentVolume (PV)
**Explanation:** A PersistentVolume (PV) is a piece of storage provisioned for use in the cluster, independent of any individual Pod.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037326 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** What does a PersistentVolumeClaim (PVC) represent in Kubernetes?
**Options:** A. A request for storage by a user<br>B. A type of storage backend<br>C. A node’s local storage<br>D. A backup of a volume
**Answer:** A – A request for storage by a user
**Explanation:** A PVC is a request made by a user (or Pod) for storage resources defined by a PV.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037327 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** What is the function of a StorageClass in Kubernetes?
**Options:** A. To define types of storage<br>B. To claim a specific PV<br>C. To attach storage to a Pod<br>D. To backup volume data
**Answer:** A – To define types of storage
**Explanation:** StorageClasses allow administrators to define different ”classes” of storage (e.g., ’fast-ssd’, ’cheap-hdd’) for dynamic provisioning.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037328 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** When defining a Pod, what does the <i>spec.containers[].image</i> field specify?
**Options:** A. The base operating system for the container<br>B. The specific container image (and tag) to run<br>C. The command to execute inside the container<br>D. The resource limits for the container<br>E. The network port the container will listen on
**Answer:** B – The specific container image (and tag) to run
**Explanation:** This field tells the container runtime which image (e.g., nginx:1.21 or myrepo/myapp:v2.5) to pull from a registry and use to create the container process.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037329 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** Which OCI (Open Container Initiative) specification defines how container runtimes should execute containers?
**Options:** A. Image Specification<br>B. Distribution Specification<br>C. Runtime Specification (CRI is Kubernetes’ interface to this)<br>D. Network Specification (CNI is related)<br>E. Storage Specification
**Answer:** C – Runtime Specification (CRI is Kubernetes’ interface to this)
**Explanation:** The OCI Runtime Specification outlines how to run a container filesystem bundle. Kubernetes uses the Container Runtime Interface (CRI) as an abstraction layer over runtimes like containerd or CRI-O that implement this standard.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037330 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** What is the primary goal of the Open Container Initiative (OCI)?
**Options:** A. To create a commercial container platform<br>B. To define open standards around container formats and runtime<br>C. To manage the Kubernetes source code repository<br>D. To develop container networking plugins (CNI)<br>E. To provide free container image hosting
**Answer:** B – To define open standards around container formats and runtime
**Explanation:** OCI aims to establish common, open, minimal standards for container image formats and container runtime execution to ensure interoperability and prevent fragmentation in the container ecosystem.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037331 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** Which statement best describes the relationship between Kubernetes and Docker (as of 2025)?
**Options:** A. Kubernetes requires Docker to be installed on all nodes.<br>B. Docker is the only container runtime supported by Kubernetes.<br>C. Kubernetes primarily interacts with container runtimes via CRI (e.g., containerd, CRI-O), abstracting Docker.<br>D. Docker manages the Kubernetes control plane components.<br>E. Kubernetes is a component within the Docker Enterprise platform.
**Answer:** C – Kubernetes primarily interacts with container runtimes via CRI (e.g., containerd, CRI-O), abstracting Docker.
**Explanation:** Explanation: Kubernetes deprecated the direct Docker integration (dockershim). It now interacts with OCI-compliant runtimes like containerd (which Docker itself uses) or CRI-O via the Container Runtime Interface (CRI). While Docker might be installed, K8s doesn’t use it directly in the same way.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037332 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** If multiple Pods need to share persistent data, which volume type allows simultaneous mounting by multiple Pods (potentially with read/write access)?
**Options:** A. hostPath<br>B. emptyDir<br>C. A PersistentVolume with an accessMode like ReadWriteMany (RWX)<br>D. secret volume<br>E. configMap volume
**Answer:** C – A PersistentVolume with an accessMode like ReadWriteMany (RWX)
**Explanation:** PersistentVolumes (PVs) represent external storage. Their accessModes define how they can be mounted. ReadWriteOnce (RWO) allows mounting by a single node, while ReadWriteMany (RWX) allows simultaneous read/write mounting by multiple nodes (requires a capable storage backend like NFS).
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037333 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** Which statement about containers is true?
**Options:** A. Require a specific OS<br>B. Run consistently across environments<br>C. Are the same as virtual machines<br>D. Only support monolithic apps
**Answer:** B – Run consistently across environments
**Explanation:** Containers provide portability, allowing applications to run consistently across different environments.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037334 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** What is the primary function of Kubernetes?
**Options:** A. Network security<br>B. Managing container lifecycle<br>C. Code compilation<br>D. Cloud storage
**Answer:** B – Managing container lifecycle
**Explanation:** Kubernetes manages deployment, scaling, and operation of containerized applications.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037335 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** What is the primary role of a container runtime?
**Options:** A. Build images<br>B. Run containers<br>C. Schedule pods<br>D. Monitor nodes
**Answer:** B – Run containers
**Explanation:** The container runtime is responsible for executing containers on cluster nodes.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037336 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** Which container runtime option is supported by Kubernetes?
**Options:** A. Docker Engine<br>B. CRI-compliant runtimes<br>C. Hyper-V<br>D. VMware vSphere
**Answer:** B – CRI-compliant runtimes
**Explanation:** Kubernetes natively supports runtimes that implement the Container Runtime Interface (CRI), such as containerd and CRI-O.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037337 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** Which networking model does Kubernetes use?
**Options:** A. NAT<br>B. VPN<br>C. Flat networking<br>D. Peer-to-peer
**Answer:** C – Flat networking
**Explanation:** Kubernetes uses a flat network model where all Pods can communicate without NAT.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037338 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** Which resource manages persistent data?
**Options:** A. Node<br>B. PersistentVolume<br>C. ServiceAccount<br>D. ConfigMap
**Answer:** B – PersistentVolume
**Explanation:** PersistentVolumes represent storage resources in the cluster.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037339 model:Many -->
**Domain:** KCNA - Container Orchestration
**Question:** What is true about a PersistentVolumeClaim?
**Options:** A. Deletes the PV automatically<br>B. Is a storage request<br>C. Requires admin attachment<br>D. Describes access methods
**Answer:** B – Is a storage request
**Explanation:** A PVC is a user request for storage resources.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::container-orchestration topic::mcq

---

<!-- note:1794080037362 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** What is <b>the primary function</b> of the kubelet component?
**Options:** A. Storing cluster state<br>B. Scheduling Pods onto Nodes<br>C. Managing the container runtime<br>D. Exposing the Kubernetes API
**Answer:** C – Managing the container runtime
**Explanation:** The kubelet runs on each Node and ensures that containers described in PodSpecs are running and healthy. It interacts with the container runtime.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---
