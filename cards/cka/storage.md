# CKA - Certified Kubernetes Administrator — Storage

> Deck: `CKA - Certified Kubernetes Administrator` · Group: `Storage` · Notes: 42 · Models: Basic, Cloze

<!-- note:1794496839599 model:Basic -->
**Front:** How do Docker volume plugins relate to Kubernetes CSI drivers?
**Back:** Volume plugins are Docker's version of the same idea — decouple the volume API from where bytes physically live (local disk vs EBS/Azure Files/PD)<br><br>Docker volume plugins and Kubernetes CSI (Container Storage Interface) solve the same architectural problem: the orchestrator asks for 'a volume', a pluggable driver decides WHERE it lives. Docker: volume drivers (local, amazon-ebs, azurefile, flocker…) behind docker volume create/-v. Kubernetes: CSI drivers (ebs.csi.aws.com, efs.csi.aws.com, pd.csi.storage.gke.io…) behind PersistentVolumes/StorageClasses. Same mental model — when you meet PV/PVC/StorageClass in the K8s storage lesson, read them as 'Kubernetes' version of docker volume + volume driver.
**Tags:** k8s::cka topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794496839600 model:Basic -->
**Front:** Why was the Container Storage Interface (CSI) created?
**Back:** Same pluggable-interface pattern as CRI (runtimes) and CNI (networks): decouple the orchestrator from vendor-specific implementations<br><br>Cloud-native converged on pluggable interfaces: CRI lets any container runtime plug into the kubelet; CNI lets any network plugin plug into pod networking; CSI does the same for STORAGE — any storage vendor writes one CSI plugin and every orchestrator can use it, no core-code changes. Before CSI, storage integrations were bespoke per-vendor code inside each orchestrator — adding EBS vs Azure Disk vs Ceph meant orchestrator-specific work every time. CSI standardizes the API so storage became a plugin like runtimes and networks already were.
**Tags:** k8s::cka topic::storage topic::csi src::session

---

<!-- note:1794496839601 model:Basic -->
**Front:** Is CSI specific to Kubernetes?
**Back:** CSI is a vendor-neutral industry spec (CNCF) — any container orchestration system can consume any vendor's CSI plugin<br><br>CSI is NOT a Kubernetes API or K8s-specific standard — it's an open spec maintained by the container-storage-interface project (CNCF ecosystem). The same plugin works with Kubernetes, Mesos, Cloud Foundry, or any CO that implements the CSI client side. Vendor neutrality cuts both ways: storage vendors implement the spec once and reach every orchestrator; orchestrators implement the client once and reach every storage backend. Kubernetes merely adopted CSI as its standard storage plugin mechanism (GA since v1.13, in-tree plugins removed in 1.20+).
**Tags:** k8s::cka topic::storage topic::csi src::session

---

<!-- note:1794496839603 model:Basic -->
**Front:** Which of these are actual CSI RPCs called by the orchestrator? (Select all that apply)<br><br>A. CreateVolume — provision a new volume<br>B. RunPodSandbox — start a pod's isolation environment<br>C. ControllerPublishVolume — attach a volume to a node<br>D. NodeStageVolume — format and globally mount the volume on a node
**Back:** A, C, D – CreateVolume, ControllerPublishVolume, and NodeStageVolume are all CSI RPCs; RunPodSandbox is a CRI call, not CSI<br><br>CSI RPCs the orchestrator calls: CONTROLLER side — CreateVolume, DeleteVolume, ControllerPublishVolume (attach volume to node), ControllerUnpublishVolume, ControllerExpandVolume, ValidateVolumeCapabilities; NODE side — NodeStageVolume, NodeUnstageVolume, NodePublishVolume, NodeUnpublishVolume, NodeGetVolumeStats, NodeExpandVolume; IDENTITY — GetPluginInfo, GetPluginCapabilities, Probe. Distractors test interface confusion: RunPodSandbox/CreateContainer are CRI (runtime) calls; ADD/DEL are CNI (network) calls. Each interface has its own RPC vocabulary — mixing them is the classic exam trap.
**Tags:** k8s::cka topic::storage topic::csi src::session

---

<!-- note:1794496839604 model:Basic -->
**Front:** Who calls the CSI RPCs like CreateVolume or NodePublishVolume?
**Back:** The orchestrator/CO side calls them — kubelet invokes node RPCs via Unix socket; master-side sidecars watch the K8s API and trigger controller RPCs<br><br>CSI RPCs are called BY the container orchestrator, never by the application (apps just see a mounted filesystem). In Kubernetes specifically: KUBELET calls NODE-service RPCs (NodeStageVolume/NodePublishVolume) directly over a Unix Domain Socket — it discovers drivers via kubelet plugin registration. Master components NEVER talk to the driver directly — they only see the K8s API; instead sidecar containers in the driver pod (external-provisioner watches PVCs→CreateVolume, external-attacher→ControllerPublishVolume, external-resizer→expand, node-driver-registrar) translate API events into CSI calls. This keeps drivers CO-agnostic.
**Tags:** k8s::cka topic::storage topic::csi src::session

---

<!-- note:1794496839605 model:Basic -->
**Front:** How does a CSI driver plug into Kubernetes?
**Back:** A CSI plugin pod (controller + node DaemonSet) registered via CSIDriver/CSINode objects; StorageClass.provisioner names the driver; PVC binding triggers provisioning<br><br>How K8s consumes CSI: the driver deploys as pods — a controller plugin (Deployment, for cluster ops) + node plugin (DaemonSet, one per node) + sidecars (external-provisioner/-attacher/-resizer, node-driver-registrar). It registers via CSIDriver and CSINode API objects. The StorageClass's provisioner field holds the driver name (e.g. ebs.csi.aws.com); a PVC referencing that StorageClass triggers external-provisioner → CreateVolume → PV/PVC binding. GA since Kubernetes v1.13; in-tree volume plugins were fully removed by v1.20 — CSI is THE storage mechanism now.
**Tags:** k8s::cka topic::storage topic::csi src::session

---

<!-- note:1794496839606 model:Basic -->
**Front:** What is the difference between NodeStageVolume and NodePublishVolume?
**Back:** NodeStageVolume does the node-wide prep (format, mount to a staging path — once per node); NodePublishVolume bind-mounts the staged volume into each pod's specific path<br><br>The node-side mount is deliberately two-phase: STAGE = global per-node operation — NodeStageVolume formats the device if needed and mounts it at a staging/global path (e.g. /var/lib/kubelet/plugins/kubernetes.io/csi/pv-xxx/globalmount); happens ONCE per node per volume regardless of pod count. PUBLISH = per-pod operation — NodePublishVolume bind-mounts (or mounts) the staged volume at the pod's target path (e.g. /var/lib/kubelet/pods/<uid>/volumes/kubernetes.io~csi/pv-xxx/mount). Unpublish/Unstage reverse it on teardown. This split lets one staged volume serve multiple pods and keeps pod-specific paths clean.
**Tags:** k8s::cka topic::storage topic::csi src::session

---

<!-- note:1794496839613 model:Basic -->
**Front:** How does a pod get durable (persistent) storage in Kubernetes?
**Back:** persistentVolumeClaim volume type mounts a PersistentVolume into the pod — the user 'claims' durable storage without knowing cloud details<br><br>In the pod spec, persistentVolumeClaim is the volume type that connects pods to durable cluster storage: volumes[].persistentVolumeClaim.claimName references a PersistentVolumeClaim object; the PVC is bound to a PersistentVolume (provisioned statically or dynamically via StorageClass/CSI). This is the indirection that makes pods portable — the pod says 'give me storage named X', the PVC/PV/StorageClass machinery figures out whether that's EBS, Azure Disk, NFS, or local disk. Without it, pods could only use node-local or pod-scoped volumes.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839614 model:Basic -->
**Front:** What is the difference between in-tree and CSI (out-of-tree) volume plugins?
**Back:** In-tree plugins were compiled into the Kubernetes binaries themselves; CSI plugins are out-of-tree and install as extensions — same decoupling idea as Docker volume plugins<br><br>Kubernetes volume plugins come in two eras: IN-TREE — built, linked, and shipped inside the core Kubernetes binaries (awsElasticBlockStore, gcePersistentDisk, azureDisk, vsphereVolume, portworxVolume, flexVolume, gitRepo…). Adding a new storage system required code into the k8s repo — slow, vendor-hostile. OUT-OF-TREE — CSI (and formerly FlexVolume) plugins deploy as ordinary pods/extensions, vendor-developed, no core changes. The migration is done: in-tree cloud plugins are DEPRECATED and in v1.37 their operations redirect to CSI drivers — CSI is the only supported path for new storage.
**Tags:** k8s::cka topic::storage topic::volumes topic::csi src::session

---

<!-- note:1794496839617 model:Basic -->
**Front:** Can a PVC claim only PART of a PersistentVolume, or must it take the whole thing?
**Back:** NO — binding is strictly one-to-one: one PVC claims one WHOLE PV exclusively; PVs cannot be sliced between claims<br><br>Your skepticism is correct — the docs are explicit: 'A PVC to PV binding is a one-to-one mapping' and 'Once bound, PersistentVolumeClaim binds are exclusive.' A PVC claims an ENTIRE PV; you cannot split one PV across multiple PVCs. What the lecture meant by 'parts': PVs form a cluster-wide POOL of whole volumes, and each PVC claims one whole PV from that pool — 'give me some of the pool's storage' = 'bind me to one whole PV'. Bonus rule: the bound PV may be LARGER than requested — 'the user will always get at least what they asked for, but the volume may be in excess.'
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839618 model:Basic -->
**Front:** What is a PersistentVolume (PV) in Kubernetes?
**Back:** apiVersion: v1, kind: PersistentVolume — a cluster-scoped object describing real storage: capacity, accessModes, reclaimPolicy, storageClassName, claimRef, and the backend spec (csi/nfs/hostPath…)<br><br>A PersistentVolume is a cluster-scoped API object (apiVersion: v1 — core group, NOT a CRD) that represents a piece of real storage in the cluster. Its spec declares: capacity.storage (size), accessModes (RWO/ROX/RWX/RWOP), persistentVolumeReclaimPolicy (what happens after release), storageClassName (which class it belongs to), claimRef (which PVC it's bound to), volumeMode (Filesystem vs Block), and the backend details — csi:, nfs:, hostPath:, local:, etc. Admins create PVs pointing at actual infrastructure (an EBS volume ID, an NFS server export, a node directory).
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839619 model:Basic -->
**Front:** What must be true for a PVC to bind to a PV?
**Back:** PVC must request ≤ PV capacity, a compatible accessMode, and matching storageClass — otherwise it stays Pending/unbound until a fit appears<br><br>The control-plane binding loop matches PVCs to PVs on three criteria: SIZE — PVC's requested storage must be ≤ PV's capacity (a 100Gi PVC can't bind a 50Gi PV; it waits for a big enough PV); ACCESS MODE — PVC's requested modes must be satisfiable by the PV's modes; STORAGE CLASS — PVC's storageClassName must match the PV's (empty class '' = no dynamic provisioning, binds only to classless PVs). If nothing matches, the PVC stays UNBOUND indefinitely — 'claims will remain unbound indefinitely if a matching volume does not exist' — until a suitable PV appears or dynamic provisioning creates one.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839620 model:Basic -->
**Front:** What are Kubernetes PV/PVC access modes?
**Back:** RWO=one node (but multiple pods on that node CAN share!), ROX=read-only many nodes, RWX=read-write many nodes, RWOP=read-write exactly ONE pod (CSI-only, stable since 1.29)<br><br>Four access modes, abbreviated RWO/ROX/RWX/RWOP: ReadWriteOnce — mount read-write on ONE node (nuance: multiple pods ON THAT NODE can still share it — it's node-scoped not pod-scoped!); ReadOnlyMany — read-only on many nodes; ReadWriteMany — read-write on many nodes (NFS/EFS/Azure Files style shared storage); ReadWriteOncePod — read-write by exactly ONE pod cluster-wide, the strictest mode (CSI volumes only, stable v1.29). Two traps: (1) access modes are for MATCHING PVC↔PV and constraining mounts — they do NOT enforce read-only (a ROX volume isn't guaranteed read-only!); (2) a volume mounts with ONE mode at a time.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839621 model:Basic -->
**Front:** What do PersistentVolume reclaim policies do?
**Back:** Retain keeps the PV+data for manual reclaim, Delete removes both PV and backing asset (the default — dynamic PVs inherit the StorageClass policy), Recycle is deprecated<br><br>persistentVolumeReclaimPolicy decides what happens to a PV AFTER its PVC is released: RETAIN — PV and data stay; admin manually cleans up (delete PV object, verify asset, clear claimRef, delete asset) — safest for valuable data; DELETE — PV object AND backing storage asset are both removed — the default, and dynamically-provisioned PVs INHERIT their StorageClass's reclaimPolicy (which defaults to Delete — so dynamic volumes self-destruct unless you change the class); RECYCLE — deprecated scrub-and-reuse, replaced by dynamic provisioning. Classic gotcha: PVC deleted → PV with Delete policy → your EBS volume GONE.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839622 model:Basic -->
**Front:** What is the difference between static and dynamic PV provisioning?
**Back:** Static: admin pre-creates PVs; Dynamic: PVC's storageClass triggers a provisioner to create a PV on demand — no admin PV needed<br><br>Two ways PVs come to exist: STATIC — the cluster admin manually creates PersistentVolume objects describing real storage (an NFS export, an EBS volume ID, a node dir); users' PVCs bind to them if criteria match. DYNAMIC — no matching static PV exists → the control plane asks a provisioner (via StorageClass) to CREATE a new PV+backing asset specifically for the PVC; requires the admin to have configured a StorageClass with a provisioner (e.g. ebs.csi.aws.com) and the DefaultStorageClass admission for defaulting. Dynamic is the modern default — users never wait for admin-created PVs.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839623 model:Basic -->
**Front:** Why does Kubernetes split storage into admin-managed PVs and user-facing PVCs instead of letting pods declare storage directly?
**Back:** Separation of duties, same pattern as the whole cloud-native design: the ADMIN owns cluster infrastructure — creating PVs that describe real storage (EBS volume IDs, NFS exports, node dirs), setting capacity/access modes/reclaim policy, deciding retention. Users shouldn't need to know (or be allowed to touch) cloud storage details — they just create a PVC saying 'I need 10Gi, ReadWriteOnce' and the binding machinery finds or provisions a match. Result: self-service storage for developers, centralized control + audit for admins, and pods stay portable because they reference claims, not vendor specifics.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839624 model:Basic -->
**Front:** Which fields belong in a PersistentVolumeClaim spec? (Select all that apply)<br><br>A. accessModes — how the volume can be mounted (RWO/ROX/RWX/RWOP)<br>B. hostPath — the node directory to mount<br>C. resources.requests.storage — how much storage to claim<br>D. storageClassName — which StorageClass/provisioner to use<br>E. containers — the pod spec to run<br>F. volumeMode — Filesystem or Block device
**Back:** A, C, D, F – accessModes, resources.requests.storage, storageClassName, and volumeMode; B (selector) and E are also real fields — the trick is which are REQUIRED vs optional<br><br>A PVC spec declares the CLAIM, not the storage: accessModes (how it can be mounted — required), resources.requests.storage (how much — required, e.g. 8Gi), volumeMode (Filesystem vs Block — optional, defaults Filesystem), storageClassName (which class/provisioner — optional but usually set), selector (label filter to pick a specific PV — optional), volumeName (pin to ONE exact PV — optional). Required = accessModes + resources.requests.storage; everything else steers WHICH PV binds. Namespaced object — PVCs live in your namespace, unlike cluster-scoped PVs.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839625 model:Basic -->
**Front:** How can a PVC control WHICH PersistentVolume it binds to?
**Back:** Three binding paths: automatic criteria matching (size/accessMode/class), selector label-matching to filter candidates, or volumeName to pin one exact PV<br><br>A PVC finds its PV three ways: (1) AUTOMATIC — no selector/volumeName: the binding loop matches on capacity, accessModes, volumeMode, storageClassName; (2) SELECTOR — spec.selector.matchLabels/matchExpressions filter PVs by their labels (ANDed with the class requirement — only same-class AND label-matching PVs qualify); (3) VOLUME NAME — spec.volumeName pins the PVC to ONE specific PV (strongest binding; if that PV is already bound, the PVC sits Pending forever). Selector and volumeName are mutually exclusive ways to steer binding — automatic is the default when neither is set.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839626 model:Basic -->
**Front:** Can a PVC with a spec.selector get a dynamically provisioned volume?
**Back:** NO — a PVC with a non-empty selector cannot get a dynamically provisioned PV; it must bind to an existing matching PV<br><br>Documented limitation: 'a PVC with a non-empty selector can't have a PV dynamically provisioned for it.' Rationale: dynamic provisioning creates a NEW PV on demand — but a selector says 'only bind me to a PV carrying THESE labels', and a freshly provisioned PV won't carry your custom labels (unless the provisioner supports label propagation via StorageClass parameters). So selector = opt into static/pre-labeled PVs only. If you need dynamic provisioning, leave selector empty and steer via storageClassName instead.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839627 model:Basic -->
**Front:** What happens when a PVC sets volumeName to a PV that's already bound to another PVC?
**Back:** It stays Pending — volumeName is a hard pin: if that PV is already bound to another PVC, this claim can never bind<br><br>spec.volumeName is the explicit-binding escape hatch: 'bind me to PV named X, period.' The docs warn: 'If the specified PV is already bound to another PVC, the binding will be stuck in a pending state' — volumeName doesn't queue or fall back to other PVs, it's a hard reference. Useful for pinning a pod to specific pre-provisioned storage (e.g. a manually created NFS PV), dangerous if you forget the PV is taken — the PVC just sits Pending with no obvious error. Automatic matching (no volumeName) would have found another PV.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839628 model:Basic -->
**Front:** What are the phases a PVC/PV pair goes through?
**Back:** Pending (unbound, searching) → Bound (matched to a PV) → Released (PVC deleted but resource not yet reclaimed) → Failed; Available is the PV's pre-binding state<br><br>Phase lifecycle: PVC starts PENDING — created but no matching PV yet (waiting for capacity/provisioning); flips BOUND when the control loop binds it to a PV (1:1, exclusive); on PVC deletion the PV enters RELEASED — 'the claim has been deleted, but the associated storage resource is not yet reclaimed' — the reclaim policy then acts (Retain → Available for reuse, Delete → gone); FAILED if something went wrong provisioning/mounting. Don't confuse the actors: these phases describe the CLAIM's view — the PV has its own status (Available/Bound/Released/Failed) tracking the other side of the binding.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839629 model:Basic -->
**Front:** What happens to the PV when you delete a PVC?
**Back:** kubectl delete pvc removes the CLAIM; the PV's reclaimPolicy decides the volume's fate — and the DEFAULT is Delete, not Retain as the lecture claimed<br><br>CORRECTION to the lecture: 'by default it is set to retain' is WRONG — the default reclaim policy is DELETE. kubectl delete pvc only removes the claim object; the PV's persistentVolumeReclaimPolicy then acts: DELETE (default — dynamic PVs inherit it from StorageClass which defaults to Delete) removes the PV AND the backing asset (EBS volume gone!); RETAIN keeps PV+data — the PV goes Released, admin can manually reclaim (clear claimRef → PV becomes Available → a NEW PVC can bind it — so yes, others CAN reuse a Retained PV); RECYCLE scrubs contents (deprecated, only nfs/hostPath support it). So deleting a PVC can destroy real cloud storage — check reclaimPolicy first.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839630 model:Basic -->
**Front:** What problem do StorageClasses solve?
**Back:** StorageClasses enable DYNAMIC provisioning — a PVC's storageClassName triggers a provisioner to create the disk+PV automatically, no manual PV<br><br>Static provisioning (the manual way): admin must create the real disk FIRST (GCP PD, AWS EBS, NFS export), then hand-write a PersistentVolume describing it, then users' PVCs bind to it — slow, error-prone, doesn't scale. StorageClasses solve it via DYNAMIC provisioning: admin defines a StorageClass ONCE naming a provisioner + parameters; a user creates ONLY a PVC with storageClassName + requested size; the external provisioner creates the backing disk AND the PV object automatically, then binds. Users never touch PVs — 'you do not need to write it.'
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839632 model:Basic -->
**Front:** What does the 'provisioner' field in a StorageClass do?
**Back:** The provisioner names WHICH volume plugin creates the disks — internal ones (kubernetes.io/gce-pd) or external CSI provisioners (ebs.csi.aws.com, pd.csi.storage.gke.io)<br><br>spec.provisioner is the REQUIRED field — it names the volume plugin that does the actual provisioning. Two flavors: INTERNAL/built-in provisioners named kubernetes.io/<backend> (gce-pd, aws-ebs, azure-disk — legacy in-tree names) and EXTERNAL provisioners — independent programs following the external-provisioner spec, almost always CSI drivers (ebs.csi.aws.com for AWS EBS, pd.csi.storage.gke.io for GCP PD, efs.csi.aws.com…). Third parties can write their own external provisioners — storage vendors ship them as the CSI ecosystem matured; in-tree provisioners are deprecated in favor of CSI.
**Tags:** k8s::cka topic::storage topic::volumes topic::csi src::session

---

<!-- note:1794496839633 model:Basic -->
**Front:** What are 'parameters' in a StorageClass?
**Back:** Provisioner-specific key-value options passed to the provisioner — e.g. type: pd-ssd, zones, iopsPerGB, fsType, encrypted — max 512 parameters<br><br>spec.parameters is a free-form map of options handed to the provisioner — each provisioner accepts its own keys: GCP PD takes type (pd-standard/pd-ssd/pd-balanced), zones, iopsPerGB?, fsType; AWS EBS takes type (gp2/gp3/io1/io2), iopsPerGB, encrypted, kmsKeyId, fsType; Azure takes skuName, kind, storageAccount. Omitted params get provisioner defaults. Limits: at most 512 parameters, and they're validated differently per provisioner — a param valid for EBS may be meaningless (or rejected) for PD. This is where 'fast SSD' vs 'cheap HDD' classes actually differ.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839634 model:Basic -->
**Front:** How does StorageClass.reclaimPolicy affect dynamically provisioned volumes?
**Back:** The class's reclaimPolicy is INHERITED by every dynamically provisioned PV — Delete (default) destroys backing storage on PVC delete; Retain preserves it<br><br>StorageClass.reclaimPolicy sets the default for all PVs it dynamically provisions: DELETE (the default when unspecified) — PVC deleted → PV + backing disk both destroyed; RETAIN — PVC deleted → PV+data survive for manual reclaim/reuse. This connects directly to the earlier gotcha: a PVC on a default class + kubectl delete pvc = your cloud disk GONE. For anything precious, either set reclaimPolicy: Retain on the class or verify before deleting claims. Only Delete/Retain are valid here — Recycle isn't allowed on classes.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839636 model:Basic -->
**Front:** What does allowVolumeExpansion do on a StorageClass?
**Back:** allowVolumeExpansion: true permits growing the PVC's storage request — the provisioner resizes the backing volume and filesystem online<br><br>allowVolumeExpansion: true on the StorageClass opts the class into PVC RESIZING: edit the PVC's resources.requests.storage upward (or kubectl patch) and Kubernetes asks the provisioner to grow the backing disk, then the node resizes the filesystem — online, no pod restart needed (filesystem must support online growth — ext4/xfs do). Requirements stack: class allows it AND provisioner supports expansion AND the volume plugin handles it. With it false/unset, PVC size is FROZEN at creation — plan capacity upfront or recreate.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839637 model:Basic -->
**Front:** What does a user actually create to get dynamically provisioned storage?
**Back:** User creates only a PVC naming the class + size — provisioner creates disk+PV, binds, pod mounts it; the PV object exists but was never hand-written<br><br>The dynamic-provisioning user experience: (1) admin defines StorageClass once; (2) user applies a PVC with storageClassName: fast + resources.requests.storage: 10Gi; (3) PVC goes Pending briefly; (4) the external-provisioner sees it, calls the CSI CreateVolume RPC, the cloud disk appears, a PV object is auto-created describing it; (5) binding loop binds PVC↔PV; (6) pod mounts via persistentVolumeClaim.claimName. The user NEVER writes PV YAML — that's the entire point. kubectl get pv shows the auto-created PV with labels like failure-domain.beta.kubernetes.io/zone.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839638 model:Basic -->
**Front:** What is the role of storage drivers in the Container Storage Interface (CSI) standard?
**Back:** Drivers implement the RPC set CSI defines — the spec says WHAT calls exist (CreateVolume, NodePublishVolume…); the driver is the vendor program that actually performs them<br><br>Split the roles carefully: the CSI STANDARD/SPEC defines the RPC interface (option D is the spec's job, not the driver's). The storage DRIVER (CSI plugin) is the vendor-side program that IMPLEMENTS those RPCs — when the orchestrator calls CreateVolume, the driver's code runs and actually creates the EBS volume/PD/etc. Option B describes what drivers end up doing in practice, but their formal role 'in the standard' is implementing its RPC contract. Option C is the purpose of CSI as a whole — the driver is one half of that compatibility story (orchestrator calls standard RPCs, driver fulfills them for its backend).
**Tags:** k8s::cka topic::storage topic::csi topic::volumes src::session

---

<!-- note:1794496839639 model:Basic -->
**Front:** What are the different access modes available for a volume in Kubernetes?
**Back:** ReadOnlyMany, ReadWriteOnce, ReadWriteMany are the real modes (current Kubernetes also adds ReadWriteOncePod)<br><br>The valid access modes: ReadWriteOnce (RWO — one node), ReadOnlyMany (ROX — many nodes read-only), ReadWriteMany (RWX — many nodes read-write), and ReadWriteOncePod (RWOP — single pod, stricter than RWO). 'WriteOnlyOnce' does NOT exist — write-only isn't an access mode concept. 'ReadOnlyOnce' doesn't exist either — read-only access is ReadOnlyMany (or you just don't write). Access modes are BINDING/MATCHING constraints between PVC requests and PV capabilities — they don't enforce read-only at the filesystem level.
**Tags:** k8s::cka topic::storage topic::pvc src::session

---

<!-- note:1794496839641 model:Basic -->
**Front:** What are two types of mounts available in Docker?
**Back:** Volume mounts (docker volume, daemon-managed under /var/lib/docker/volumes) and bind mounts (direct host path mapped into the container)<br><br>Docker's two mount types: VOLUME MOUNTS — daemon-managed named volumes created via docker volume create, stored under /var/lib/docker/volumes, survive container deletion, can use volume-driver plugins for cloud backends. BIND MOUNTS — a direct host filesystem path mapped into the container (-v /host/path:/container/path); simplest, but you manage the host path yourself and it's tied to that host. 'Persistent vs temporary' describes data lifetime, not mount types; 'local vs remote' and 'static vs dynamic' are storage-class/provisioning concepts, not Docker mounts.
**Tags:** k8s::cka topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794496839653 model:Basic -->
**Front:** Which securityContext field controls group ownership of mounted volumes, and where must it be set?
**Back:** fsGroup — it makes volume contents owned by that GID; it only exists at pod level because container settings don't touch volumes<br><br>fsGroup is a PodSecurityContext-only field: it sets the group ownership of mounted volumes so containers can read/write shared data without running as root. Doc rule: 'Container settings do not affect the Pod's Volumes' — so fsGroup, supplementalGroups, fsGroupChangePolicy and supplementalGroupsPolicy exist ONLY under spec.securityContext. Companion fields: fsGroupChangePolicy (OnRootMismatch skips recursive chown for speed) and supplementalGroupsPolicy (Merge default vs Strict — controls whether the image's /etc/group memberships get merged in, a beta feature since v1.33).
**Tags:** k8s::cka src::session topic::podsecurity topic::security topic::storage

---

<!-- note:1794496839670 model:Basic -->
**Front:** A stateful application requires storage that persists even if its Pod is rescheduled to another Node. Which Kubernetes objects are essential for this?
**Back:** PersistentVolume (PV) and PersistentVolumeClaim (PVC)<br><br>A PersistentVolume (PV) represents a piece of storage,<br>and a PersistentVolumeClaim (PVC) is a request for that storage by a<br>user/Pod. This decoupling allows storage to outlive Pods.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839678 model:Basic -->
**Front:** What Kubernetes object represents a piece of storage in the cluster, provisioned by an administrator or dynamically?
**Back:** PersistentVolume (PV)<br><br>A PersistentVolume (PV) is a piece of storage provisioned for use in the cluster, independent of any individual Pod.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839679 model:Basic -->
**Front:** What does a PersistentVolumeClaim (PVC) represent in Kubernetes?
**Back:** A request for storage by a user<br><br>A PVC is a request made by a user (or Pod) for storage resources defined by a PV.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839680 model:Basic -->
**Front:** What is the function of a StorageClass in Kubernetes?
**Back:** To define types of storage<br><br>StorageClasses allow administrators to define different ”classes” of storage (e.g., ’fast-ssd’, ’cheap-hdd’) for dynamic provisioning.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839685 model:Basic -->
**Front:** If multiple Pods need to share persistent data, which volume type allows simultaneous mounting by multiple Pods (potentially with read/write access)?
**Back:** A PersistentVolume with an accessMode like ReadWriteMany (RWX)<br><br>PersistentVolumes (PVs) represent external storage. Their accessModes define how they can be mounted. ReadWriteOnce (RWO) allows mounting by a single node, while ReadWriteMany (RWX) allows simultaneous read/write mounting by multiple nodes (requires a capable storage backend like NFS).
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839691 model:Basic -->
**Front:** Which resource manages persistent data?
**Back:** PersistentVolume<br><br>PersistentVolumes represent storage resources in the cluster.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839692 model:Basic -->
**Front:** What is true about a PersistentVolumeClaim?
**Back:** Is a storage request<br><br>A PVC is a user request for storage resources.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839792 model:Cloze -->
**Text:** A PersistentVolume spec — the admin-side storage object:<br><br>{{c1::<code>apiVersion: v1</code>}}<br>{{c2::<code>kind: PersistentVolume</code>}}<br>{{c3::<code>metadata:</code>}}<br>{{c4::<code>spec:</code>}}<br>  capacity:<br>    storage: {{c5::<code>10Gi</code>}}<br>  {{c6::<code>accessModes:</code>}}<br>    - {{c7::<code>ReadWriteOnce</code>}}<br>  {{c8::<code>persistentVolumeReclaimPolicy:</code>}} {{c9::<code>Retain</code>}}<br>  storageClassName: {{c10::<code>standard</code>}}<br>  csi:  # or nfs:/hostPath:/local: — the real backend
**Back Extra:** apiVersion: v1 + kind: PersistentVolume = core API group (not a CRD). Spec fields: capacity.storage (size like 10Gi), accessModes (RWO/ROX/RWX/RWOP), persistentVolumeReclaimPolicy (Retain/Delete/Recycle), storageClassName, claimRef (bound PVC), volumeMode (Filesystem/Block), and the backend: csi:/nfs:/hostPath:/local:. cluster-scoped — no namespace field.
**Tags:** k8s::cka topic::storage topic::volumes topic::yaml src::session

---

<!-- note:1794496839793 model:Cloze -->
**Text:** A StorageClass — the admin-side dynamic-provisioning profile:<br><br>{{c1::<code>apiVersion: storage.k8s.io/v1</code>}}<br>{{c2::<code>kind: StorageClass</code>}}<br>{{c3::<code>metadata:</code>}}<br>{{c4::<code>provisioner:</code>}} {{c5::<code>pd.csi.storage.gke.io</code>}}<br>{{c6::<code>parameters:</code>}}<br>  type: {{c7::<code>pd-ssd</code>}}<br>  {{c8::<code>reclaimPolicy:</code>}} {{c9::<code>Delete</code>}}<br>  {{c10::<code>volumeBindingMode:</code>}} {{c11::<code>WaitForFirstConsumer</code>}}<br>  {{c12::<code>allowVolumeExpansion:</code>}} {{c13::<code>true</code>}}
**Back Extra:** provisioner = REQUIRED (which plugin creates disks: kubernetes.io/gce-pd legacy, or CSI like ebs.csi.aws.com/pd.csi.storage.gke.io). parameters = provisioner-specific (type, zones, iopsPerGB, fsType, encrypted — max 512). reclaimPolicy Delete(default)/Retain — inherited by dynamically created PVs. volumeBindingMode Immediate(default)/WaitForFirstConsumer (provision in pod's zone). allowVolumeExpansion true = PVC resizable. mountOptions = filesystem mount flags.
**Tags:** k8s::cka topic::storage topic::volumes topic::yaml src::session

---

<!-- note:1794496715391 model:Cloze -->
**Text:** A PersistentVolumeClaim — the user-side storage request:<br><br>{{c1::<code>apiVersion: v1</code>}}<br>{{c2::<code>kind: PersistentVolumeClaim</code>}}<br>{{c3::<code>metadata:</code>}}<br>{{c4::<code>spec:</code>}}<br>  {{c5::<code>accessModes:</code>}}<br>    - {{c6::<code>ReadWriteOnce</code>}}<br>  {{c7::<code>volumeMode:</code>}} {{c8::<code>Filesystem</code>}}<br>  resources:<br>    requests:<br>      storage: {{c9::<code>8Gi</code>}}<br>  storageClassName: {{c10::<code>slow</code>}}<br>  selector:<br>    matchLabels:<br>      release: {{c11::<code>"stable"</code>}}
**Back Extra:** Required: accessModes + resources.requests.storage. volumeMode defaults Filesystem (Block = raw device, no filesystem). selector + storageClassName are ANDed — and a non-empty selector BLOCKS dynamic provisioning. volumeName pins to one exact PV (stuck Pending if taken). storageClassName: "" = explicitly NO class (binds only classless PVs); missing = uses DefaultStorageClass if configured.
**Tags:** k8s::cka topic::storage topic::volumes topic::yaml src::session

---
