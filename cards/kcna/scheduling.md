<!-- note:1793807595536 model:Many -->
**Domain:** Scheduling - pod selection
**Question:** Which pods does the kube-scheduler pick up and try to place?
**Options:** A. Pods whose spec.nodeName is still unset<br>B. Pods that failed health checks<br>C. Pods on overloaded nodes<br>D. All newly created pods regardless of fields
**Answer:** A (1) – pods whose spec.nodeName is still unset (unassigned)
**Explanation:** The scheduler watches for newly created pods that have no node assigned — i.e. spec.nodeName is empty. For each it runs filtering (which nodes are feasible) then scoring (which is best), then binds the pod. Pods already carrying a nodeName never reach the scheduler — that's why manually setting it bypasses scheduling entirely.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/" target="_blank">Kubernetes Documentation - kube-scheduler</a>
**Tags:** k8s::kcna topic::pods topic::scheduling src::session

---

<!-- note:1793807595537 model:Many -->
**Domain:** Scheduling - nodeName immutability
**Question:** Can you change spec.nodeName on an already-created pod to move it to another node?
**Options:** A. Yes — <code>kubectl patch pod --type merge</code> works<br>B. Yes — kubectl edit pod and update the field<br>C. No — nodeName is immutable after creation; recreate the pod to move it<br>D. Only if the pod is restarted first
**Answer:** C (3) – no — nodeName is immutable after creation; recreate the pod to move it
**Explanation:** spec.nodeName can only be written at two moments: by you at pod creation, or by the scheduler via a Binding while the pod is still unassigned. Once set it's read-only — kubectl patch/edit on it is rejected. To move a scheduled pod you must delete and recreate it (or let a Deployment do the rollout).
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/" target="_blank">Kubernetes Documentation - kube-scheduler</a>
**Tags:** k8s::kcna topic::pods topic::scheduling src::session

---

<!-- note:1793807595538 model:Many -->
**Domain:** Scheduling - manual binding
**Question:** Without kube-scheduler, how do you assign an already-created pod that has no nodeName to a node?
**Options:** A. kubectl annotate the pod with the target node<br>B. Create a Binding object (POST JSON to the pod's binding subresource naming the target node)<br>C. Patch spec.nodeName directly<br>D. Add the node's name to metadata.labels
**Answer:** B (2) – create a Binding object (POST JSON to the pod's binding subresource naming the target node)
**Explanation:** The Binding object is what the scheduler itself creates after picking a node. Doing it manually: POST to /api/v1/namespaces/&lt;ns&gt;/pods/&lt;pod&gt;/binding with a body like {"target": {"kind": "Node", "name": "node2"}} — the API server then writes nodeName and the kubelet takes over. It only works while nodeName is still empty.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/" target="_blank">Kubernetes Documentation - kube-scheduler</a>
**Tags:** k8s::kcna topic::api topic::scheduling src::session

---

<!-- note:1793807595548 model:Basic (and reversed card) -->
**Front:** What is the <code>spec.nodeName</code> field on a pod?
**Back:** It holds the name of the node the pod is bound to run on. It's empty when you submit the pod — the scheduler fills it (via a Binding) after choosing a node. If you set <code>spec.nodeName</code> yourself at creation time, the pod skips the scheduler entirely: manual scheduling. Immutable afterwards.
**Tags:** k8s::kcna topic::pods topic::scheduling src::session

---

<!-- note:1793807595549 model:Basic (and reversed card) -->
**Front:** Mechanically, what does the kube-scheduler DO once it picks a node for a pod?
**Back:** The scheduler creates a <code>Binding</code> object — a POST to the pod's <code>binding</code> subresource naming the chosen node. The API server records the decision by writing <code>spec.nodeName</code> on the pod; the kubelet on that node then sees the pod is assigned to it and starts the containers.
**Tags:** k8s::kcna topic::architecture topic::scheduling src::session

---

<!-- note:1793809412430 model:Many -->
**Domain:** Taints - effects
**Question:** Which taint effect removes ALREADY-RUNNING pods from a node if they don't tolerate it?
**Options:** A. NoSchedule<br>B. PreferNoSchedule<br>C. NoExecute<br>D. Evict
**Answer:** C (3) – NoExecute
**Explanation:** NoSchedule: no new pods without a matching toleration (existing pods stay). PreferNoSchedule: soft version — scheduler tries to avoid but no guarantee. NoExecute: evicts running pods that don't tolerate it (immediately, or after tolerationSeconds if set) AND blocks new ones.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/" target="_blank">Kubernetes Documentation - Taints and Tolerations</a>
**Tags:** k8s::kcna topic::scheduling topic::taints src::session

---

<!-- note:1793809412431 model:Many -->
**Domain:** Taints - toleration semantics
**Question:** A pod tolerates node1's taint. Is it guaranteed to be scheduled on node1?
**Options:** A. Yes — a matching toleration binds the pod to that node<br>B. No — a toleration only PERMITS placement; nodeAffinity/nodeSelector attracts pods to nodes<br>C. Yes — but only for NoSchedule taints<br>D. No — tolerations and taints are unrelated
**Answer:** B (2) – no — a toleration only PERMITS placement; nodeAffinity/nodeSelector attracts pods to nodes
**Explanation:** Tolerations are a pass, not a magnet: the scheduler may still place the pod on any node — tainted or untainted. Taints REPEL (set on nodes); affinity/nodeSelector ATTRACT (set on pods). For 'must run on node X' you combine them: taint the node to keep others out + nodeAffinity on the pod to pin it there.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/" target="_blank">Kubernetes Documentation - Taints and Tolerations</a>
**Tags:** k8s::kcna topic::scheduling topic::taints src::session

---

<!-- note:1793809412432 model:Many -->
**Domain:** Taints - control plane
**Question:** Why don't regular workload pods land on the control-plane node by default?
**Options:** A. Pods can't reach the control-plane network<br>B. kubelet refuses to run user pods on it<br>C. The control-plane node carries a default taint (node-role.kubernetes.io/control-plane:NoSchedule) that user pods don't tolerate<br>D. Control-plane nodes only accept static pods
**Answer:** C (3) – the control-plane node carries a default taint (node-role.kubernetes.io/control-plane:NoSchedule) that user pods don't tolerate
**Explanation:** kubeadm clusters taint control-plane nodes by default (node-role.kubernetes.io/control-plane:NoSchedule) so workloads stay off them — protection, not magic. DaemonSets and system pods carry matching tolerations. You CAN remove the taint (<code>kubectl taint nodes &lt;cp&gt; node-role.kubernetes.io/control-plane:NoSchedule-</code>) e.g. on single-node labs like minikube — it's just not done on real clusters.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/" target="_blank">Kubernetes Documentation - Taints and Tolerations</a>
**Tags:** k8s::kcna topic::architecture topic::taints src::session

---

<!-- note:1793809412438 model:Basic (and reversed card) -->
**Front:** Taints vs tolerations — which object gets which, and what's the pair for?
**Back:** A scheduling restriction pair: <b>taints on NODES repel</b> pods (the node says 'stay away unless allowed'); <b>tolerations on PODS</b> let them bypass a matching taint. Effect: keeps pods off unsuitable nodes — dedicated hardware, control plane, special workloads. Tolerations permit but never attract — pods can still land anywhere.
**Tags:** k8s::kcna topic::scheduling topic::taints src::session

---

<!-- note:1793809412490 model:Cloze -->
**Text:** Taint node1 so only pods tolerating <code>dedicated=gpu</code> may schedule:<br><br><code>kubectl taint nodes node1 {{c1::dedicated=gpu}}:{{c2::NoSchedule}}</code>
**Back Extra:** Format: <code>kubectl taint nodes &lt;node&gt; &lt;key&gt;=&lt;value&gt;:&lt;effect&gt;</code>. Remove a taint by appending a minus: <code>kubectl taint nodes node1 dedicated=gpu:NoSchedule-</code>. Effects: NoSchedule / PreferNoSchedule / NoExecute.
**Tags:** k8s::kcna topic::kubectl topic::taints src::session

---

<!-- note:1793809412491 model:Cloze -->
**Text:** Pod spec tolerating a <code>dedicated=gpu:NoSchedule</code> taint — fields under <code>{{c1::spec.tolerations}}</code>:<br><br><code>tolerations:<br>- key: {{c2::"dedicated"}}<br>  operator: {{c3::"Equal"}}<br>  value: {{c4::"gpu"}}<br>  effect: {{c5::"NoSchedule"}}</code>
**Back Extra:** operator defaults to Equal (needs a matching value); Exists matches the key regardless of value (omit 'value'). Effect must equal the taint's effect. Add tolerationSeconds: 3600 under a NoExecute toleration to survive the taint for one hour before eviction.
**Tags:** k8s::kcna topic::taints topic::yaml src::session

---

<!-- note:1793810135656 model:Many -->
**Domain:** NodeSelector - limitations
**Question:** Can spec.nodeSelector express 'run on nodes labelled size=large OR size=medium'?
**Options:** A. Yes — separate values with commas<br>B. No — nodeSelector only does equality-AND on labels; OR/prefer logic needs nodeAffinity/nodeAntiAffinity<br>C. Yes — use a YAML list under nodeSelector<br>D. Yes — use two nodeSelector blocks
**Answer:** B (2) – no — nodeSelector only does equality-AND on labels; OR/prefer logic needs nodeAffinity/nodeAntiAffinity
**Explanation:** nodeSelector accepts only exact key=value pairs, ANDed together — you can't say 'large OR medium', 'not small', or 'prefer fast'. Node affinity adds expressive rules: the In operator (size In [large, medium]), NotIn, plus requiredDuringScheduling (hard) vs preferredDuringScheduling (soft) terms. Anti-affinity is the inverse — keep pods OFF matching nodes (or spread them).
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Documentation - Assign Pods to Nodes</a>
**Tags:** k8s::kcna topic::nodeselector topic::scheduling src::session

---

<!-- note:1793810135657 model:Many -->
**Domain:** NodeSelector - hard requirement
**Question:** A pod has spec.nodeSelector {size: large} but NO node carries that label. What happens?
**Options:** A. It schedules anyway on a random node<br>B. It's deleted after a timeout<br>C. It stays Pending/unschedulable until a node with matching labels appears<br>D. kubelet runs it on the control-plane node
**Answer:** C (3) – it stays Pending/unschedulable until a node with matching labels appears
**Explanation:** nodeSelector is a HARD constraint — the scheduler won't place the pod anywhere else and won't retry-error; the pod just sits unscheduled. Events show '0/N nodes are available'. Fixes: label a node, relax the selector, or switch to nodeAffinity preferredDuringScheduling for a soft preference.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Documentation - Assign Pods to Nodes</a>
**Tags:** k8s::kcna topic::nodeselector topic::scheduling src::session

---

<!-- note:1793810135666 model:Basic (and reversed card) -->
**Front:** What is <code>spec.nodeSelector</code> on a pod?
**Back:** A pod-spec field holding key-value pairs that constrain WHERE the pod may run: the scheduler only picks nodes whose labels satisfy ALL listed pairs. <code>spec.nodeSelector: {size: large}</code> = 'nodes labelled size=large only'. It's the simplest node-constraint mechanism — hard equality matching only, no OR/preferences.
**Tags:** k8s::kcna topic::nodeselector topic::scheduling src::session

---

<!-- note:1793810135683 model:Basic -->
**Front:** Recipe: pin a pod to SSD nodes using nodeSelector
**Back:** Two steps, in order: 1) LABEL the node — <code>kubectl label nodes node1 disktype=ssd</code>. 2) Add the selector in the pod spec — <code>spec.nodeSelector: {disktype: ssd}</code>. The nodeSelector never labels anything itself; it only matches labels nodes already carry. Labels on the node, selector on the pod.
**Tags:** k8s::kcna topic::nodeselector topic::scheduling src::session

---

<!-- note:1793810943058 model:Many -->
**Domain:** NodeAffinity - types
**Question:** Which node affinity type schedules the pod ANYWAY when no node satisfies the rule?
**Options:** A. requiredDuringSchedulingIgnoredDuringExecution<br>B. preferredDuringSchedulingIgnoredDuringExecution<br>C. requiredDuringSchedulingRequiredDuringExecution<br>D. softDuringScheduling
**Answer:** B (2) – preferredDuringSchedulingIgnoredDuringExecution
**Explanation:** requiredDuringSchedulingIgnoredDuringExecution is the HARD type: no matching node = pod stays Pending (like nodeSelector but expressive). preferredDuringSchedulingIgnoredDuringExecution is SOFT: scheduler scores matching nodes higher using weight 1-100, but schedules anyway if none match. The 'IgnoredDuringExecution' suffix on BOTH means label changes after scheduling don't evict the pod.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Documentation - Assign Pods to Nodes</a>
**Tags:** k8s::kcna topic::affinity topic::scheduling src::session

---

<!-- note:1793810943059 model:Many -->
**Domain:** NodeAffinity - IgnoredDuringExecution
**Question:** A pod required a node label via nodeAffinity, gets scheduled, then the node's label is REMOVED. What does 'IgnoredDuringExecution' mean happens?
**Options:** A. The pod is evicted when the label changes<br>B. The pod reschedules to a compliant node<br>C. Nothing — node label changes after scheduling don't evict the pod<br>D. The pod enters a failed state
**Answer:** C (3) – nothing — node label changes after scheduling don't evict the pod
**Explanation:** Affinity rules are evaluated only at SCHEDULING time. Once bound, the pod is immune to node-label changes: if the node loses its 'size=large' label later, the pod keeps running. (Contrast: NoExecute taints DO evict.) The never-implemented RequiredDuringExecution variant would have evicted — hence the verbose naming.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Documentation - Assign Pods to Nodes</a>
**Tags:** k8s::kcna topic::affinity topic::scheduling src::session

---

<!-- note:1793810943060 model:Many -->
**Domain:** NodeAffinity - match logic
**Question:** How are nodeSelectorTerms and the matchExpressions inside them logically combined?
**Options:** A. Both ORed<br>B. Terms ORed, expressions ANDed — pod needs any ONE term fully satisfied<br>C. Both ANDed<br>D. Terms ANDed, expressions ORed
**Answer:** B (2) – terms ORed, expressions ANDed — pod needs any ONE term fully satisfied
**Explanation:** Two levels of logic inside requiredDuringScheduling...: the list nodeSelectorTerms[] is ORed (match ANY term); the matchExpressions[] inside ONE term are ANDed (ALL expressions in that term must match). Bonus: if both nodeSelector AND nodeAffinity are set on a pod, BOTH must be satisfied.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Documentation - Assign Pods to Nodes</a>
**Tags:** k8s::kcna topic::affinity topic::scheduling src::session

---

<!-- note:1793810943061 model:Many -->
**Domain:** NodeAffinity - operators
**Question:** With nodeAffinity matchExpressions, how do you require a pod to avoid nodes labelled zone=east?
**Options:** A. operator: NotIn (or DoesNotExist for 'label absent' — anti-affinity behavior)<br>B. operator: Exclude<br>C. operator: NotEqual<br>D. operator: Neq
**Answer:** A (1) – operator: NotIn (or DoesNotExist for 'label absent' — anti-affinity behavior)
**Explanation:** matchExpressions operators: In (value in list — this gives the OR nodeSelector lacks: size In [large, medium]), NotIn (value NOT in list), Exists (key present, any value), DoesNotExist (key absent), Gt/Lt (integer compare). NotIn and DoesNotExist are how you express node ANTI-affinity — keep pods off matching nodes.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Documentation - Assign Pods to Nodes</a>
**Tags:** k8s::kcna topic::affinity topic::scheduling src::session

---

<!-- note:1793810943068 model:Basic (and reversed card) -->
**Front:** What is node affinity — and what does it add over nodeSelector?
**Back:** The expressive version of nodeSelector — pod-specified rules under <code>spec.affinity.nodeAffinity</code> that attract pods to (or repel from) nodes based on node labels. Adds what nodeSelector lacks: OR logic (values lists, multiple terms), NOT operators (NotIn/DoesNotExist = anti-affinity), and SOFT preferences (preferredDuringScheduling... with weights). Exists purely to control pod placement.
**Tags:** k8s::kcna topic::affinity topic::scheduling src::session

---

<!-- note:1793810943076 model:Cloze -->
**Text:** Require the pod on large-or-medium nodes via affinity:<br><br><code>spec:<br>  affinity:<br>    {{c1::nodeAffinity}}:<br>      {{c2::requiredDuringSchedulingIgnoredDuringExecution}}:<br>        {{c3::nodeSelectorTerms}}:<br>        - {{c4::matchExpressions}}:<br>          - {key: size, operator: {{c5::In}}, values: [large, medium]}</code>
**Back Extra:** Hierarchy: spec.affinity.nodeAffinity.&lt;type&gt;.nodeSelectorTerms[].matchExpressions[] — each expression is {key, operator, values[]}. values is a LIST (In = OR across values). Preferred type uses - weight: N / preference: matchExpressions instead of plain terms.
**Tags:** k8s::kcna topic::affinity topic::yaml src::session

---

<!-- note:1793820261525 model:Many -->
**Domain:** Resources - units
**Question:** In a container spec, what does <code>cpu: 250m</code> request?
**Options:** A. 250 CPU cores<br>B. 250 megahertz<br>C. 0.25 of one CPU core<br>D. 250 megabytes of RAM
**Answer:** C (3) – 0.25 of one CPU core
**Explanation:** CPU is measured in cores: 1 = one full (v)CPU/hyperthread, and m = millicores (1/1000) — 250m = 0.25 core, 500m = half. Memory uses bytes with suffixes: Mi/Gi = mebibytes/gibibytes (2^20, 2^30 — binary), M/G = megabytes/gigabytes (10^6, 10^9 — decimal). Requests/limits accept either but Mi/Gi is the convention.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/" target="_blank">Kubernetes Documentation - Resource Management for Pods and Containers</a>
**Tags:** k8s::kcna topic::resources topic::scheduling src::session

---

<!-- note:1793820261526 model:Many -->
**Domain:** Resources - scheduler accounting
**Question:** Every node's allocatable CPU minus existing pods' requests is BELOW a new pod's request. What happens?
**Options:** A. Schedules anyway — limits are what count<br>B. Stays Pending — scheduler sums requests already on each node against node allocatable; nowhere fits<br>C. Schedules on the least-loaded node regardless<br>D. Kubernetes reduces the request automatically
**Answer:** B (2) – stays Pending — scheduler sums requests already on each node against node allocatable; nowhere fits
**Explanation:** The scheduler filters on REQUESTS (not limits, not actual usage): a node fits if allocatable − sum(existing pod requests) ≥ new pod's request. 4-CPU allocatable with 3.5 CPU already requested leaves 0.5 — a 1-CPU request fails the filter everywhere → pod Pending until capacity frees or a node is added. Limits don't factor into this math.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/" target="_blank">Kubernetes Documentation - Resource Management for Pods and Containers</a>
**Tags:** k8s::kcna topic::resources topic::scheduling src::session

---

<!-- note:1793820261527 model:Many -->
**Domain:** Resources - LimitRange defaulting
**Question:** A pod manifest sets NO resources, but its namespace has a LimitRange with defaults. What happens at creation?
**Options:** A. The pod is rejected<br>B. The LimitRange admission controller injects the namespace's default requests/limits<br>C. It gets zero resources<br>D. kubelet assigns values at runtime
**Answer:** B (2) – the LimitRange admission controller injects the namespace's default requests/limits
**Explanation:** LimitRange does double duty in a namespace: it VALIDATES min/max bounds and supplies DEFAULTS. A pod omitting resources gets the LimitRange defaults patched in at admission time — so quota accounting works even for lazy manifests. If the defaults don't exist either, the pod gets no requests (scheduler treats it as ~0 → QoS BestEffort).
**Sources:** <a href="https://kubernetes.io/docs/concepts/policy/limit-range/" target="_blank">Kubernetes Documentation - Limit Ranges</a>
**Tags:** k8s::kcna topic::resources topic::namespaces src::session

---

<!-- note:1793820261535 model:Basic (and reversed card) -->
**Front:** resources.requests vs resources.limits — what does each actually do?
**Back:** <b>requests</b> = the reservation — what the scheduler assumes the container needs, used to pick a node (guaranteed share at runtime). <b>limits</b> = the ceiling — how much it may use AT MOST. Exceed the CPU limit → throttled; exceed the memory limit → the container is killed (OOMKilled) and restarted per restartPolicy. Rule: requests for scheduling, limits for containment.
**Tags:** k8s::kcna topic::resources topic::containers src::session

---

<!-- note:1793820261547 model:Cloze -->
**Text:** Container resource stanza — where requests and limits live:<br><br><code>containers:<br>- name: app<br>  {{c1::resources}}:<br>    {{c2::requests}}:<br>      {{c3::cpu}}: "{{c4::250m}}"<br>      {{c5::memory}}: "{{c6::256Mi}}"<br>    {{c7::limits}}:<br>      cpu: "500m"<br>      memory: "512Mi"</code>
**Back Extra:** Per-CONTAINER field — a pod's effective request is the sum of its containers' requests. requests = scheduling floor, limits = runtime ceiling. Units: m = millicores (250m = 0.25 CPU); Mi/Gi = binary memory (2^20/2^30), M/G = decimal.
**Tags:** k8s::kcna topic::resources topic::yaml src::session

---

<!-- note:1793821101844 model:Many -->
**Domain:** Resources - defaulting
**Question:** A container declares <code>limits: {cpu: 250m}</code> and no requests. What's its effective cpu request?
**Options:** A. requests.cpu stays unset (0)<br>B. requests.cpu also becomes 250m — the request defaults to the limit<br>C. The pod is rejected as invalid<br>D. The limit is ignored
**Answer:** B (2) – requests.cpu also becomes 250m — the request defaults to the limit
**Explanation:** When a container sets a limit but no request, Kubernetes copies the limit value INTO the request. The reverse is not true: a request alone leaves the limit unset (container may burst beyond it). One-directional rule: limit → fills request; request → limit stays empty.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/" target="_blank">Kubernetes Documentation - Resource Management</a>
**Tags:** k8s::kcna topic::containers topic::resources src::session

---

<!-- note:1793821101845 model:Many -->
**Domain:** Resources - sizing strategy
**Question:** What's a common sizing recommendation for Deployments?
**Options:** A. Set limits on everything, requests optional<br>B. Set neither — Kubernetes handles it<br>C. Requests everywhere, limits carefully — lets pods burst into idle capacity instead of being throttled<br>D. Only limits matter — requests are optional metadata
**Answer:** C (3) – requests everywhere, limits carefully — lets pods burst into idle capacity instead of being throttled
**Explanation:** A common recommendation: always set requests (scheduling + guarantees) but leave CPU limits off — a container over its limit gets THROTTLED even while the node sits idle, needlessly slowing bursts. Memory is different: it can't be throttled, only reclaimed by killing (OOMKilled), so memory limits still earn their place. Defaults: no request/no limit = BestEffort, evicted first under pressure.
**Sources:** <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/" target="_blank">Kubernetes Documentation - Resource Management</a>
**Tags:** k8s::kcna topic::containers topic::resources src::session

---

<!-- note:1793821101846 model:Many -->
**Domain:** Resources - quota coupling
**Question:** A namespace's ResourceQuota covers cpu. What does that force on new pods?
**Options:** A. Nothing — quota only tracks usage<br>B. Every new pod must specify cpu (request or limit); pods without it are rejected (403)<br>C. Existing pods are rescheduled<br>D. The namespace gets locked
**Answer:** B (2) – every new pod must specify cpu (request or limit); pods without it are rejected (403)
**Explanation:** A ResourceQuota covering cpu or memory forces the issue: any new pod lacking a request OR limit for that resource gets rejected with 403 Forbidden at admission — there's nothing to charge the quota against. That's exactly why LimitRange pairs with ResourceQuota: LimitRange injects defaults so manifests still get accepted. Quota violations never affect already-running pods.
**Sources:** <a href="https://kubernetes.io/docs/concepts/policy/resource-quotas/" target="_blank">Kubernetes Documentation - Resource Quotas</a>
**Tags:** k8s::kcna topic::namespaces topic::resources src::session

---

<!-- note:1793821101854 model:Basic (and reversed card) -->
**Front:** What problem do resource requests and limits solve?
**Back:** Without limits one pod can consume ALL of a node's CPU/memory — starving every other workload on it ('noisy neighbor'). requests fix placement: the scheduler guarantees the pod its share and won't overbook the node. limits fix containment: CPU over-limit → throttled; memory over-limit → OOMKilled, because memory can't be throttled — you can't take RAM back from a process except by killing it.
**Tags:** k8s::kcna topic::resources topic::scheduling src::session

---

<!-- note:1793821101864 model:Cloze -->
**Text:** LimitRange manifest — sets defaults + bounds for containers in its namespace:<br><br><code>apiVersion: {{c1::v1}}<br>kind: {{c2::LimitRange}}<br>metadata: {name: limits}<br>spec:<br>  {{c3::limits}}:<br>  - {{c4::default}}: {cpu: 500m}        # default limit<br>    {{c5::defaultRequest}}: {cpu: 100m} # default request<br>    max: {cpu: "1"}<br>    min: {cpu: 100m}<br>    {{c6::type}}: Container</code>
**Back Extra:** spec.limits[] is a list; each entry has default (default LIMIT), defaultRequest (default request), max, min, and type (Container or PersistentVolumeClaim). Only enforced at admission — existing pods keep their values. Two LimitRanges in one namespace → nondeterministic defaults.
**Tags:** k8s::kcna topic::resources topic::yaml src::session

---

<!-- note:1793821101865 model:Cloze -->
**Text:** ResourceQuota manifest — aggregate caps for one namespace:<br><br><code>apiVersion: {{c1::v1}}<br>kind: {{c2::ResourceQuota}}<br>metadata:<br>  name: compute-quota<br>  namespace: {{c3::dev}}<br>spec:<br>  {{c4::hard}}:<br>    {{c5::requests.cpu}}: "4"<br>    requests.memory: 4Gi<br>    {{c6::limits.cpu}}: "8"<br>    pods: "10"</code>
**Back Extra:** spec.hard maps resource names → totals for the namespace: requests.cpu/requests.memory, limits.cpu/limits.memory, plus object counts (pods, services, persistentvolumeclaims). Exceeding any entry → new object rejected with 403. A cpu/memory quota forces every pod to declare that resource — pair it with LimitRange for defaults.
**Tags:** k8s::kcna topic::namespaces topic::yaml src::session

---

<!-- note:1793835711168 model:Many -->
**Domain:** Schedulers - selection
**Question:** How does a pod say 'schedule me with my-scheduler, not the default'?
**Options:** A. A label on the pod<br>B. spec.schedulerName must equal the scheduler's unique name<br>C. An annotation requesting it<br>D. The pod's namespace
**Answer:** B (2) – spec.schedulerName must equal the scheduler's unique name
**Explanation:** Each scheduler owns a unique name cluster-wide (the default is 'default-scheduler'). A pod opts in via spec.schedulerName: my-scheduler — unset means the default scheduler claims it. Two schedulers never fight over a pod: each only watches unbound pods bearing its own name.
**Sources:** <a href="https://kubernetes.io/docs/tasks/extend-kubernetes/configure-multiple-schedulers/" target="_blank">Kubernetes Documentation - Configure Multiple Schedulers</a>
**Tags:** k8s::kcna topic::pods topic::scheduling src::session

---

<!-- note:1793835711169 model:Many -->
**Domain:** Schedulers - profiles
**Question:** How can one kube-scheduler process act as several different schedulers?
**Options:** A. It can't — you must run separate binaries<br>B. <code>--replicas</code> flag on kube-scheduler<br>C. KubeSchedulerConfiguration profiles[] — one process, multiple profiles, each with its own schedulerName<br>D. Namespaces scope the schedulers
**Answer:** C (3) – KubeSchedulerConfiguration profiles[] — one process, multiple profiles, each with its own schedulerName
**Explanation:** Profiles let ONE kube-scheduler binary wear multiple hats: the config's profiles[] list gives each profile a distinct schedulerName + its own plugin config, and pods pick a profile via spec.schedulerName — but only a single scheduler process runs. Alternative: separate scheduler PROCESSES (e.g. a second kube-scheduler Deployment with its own config/name). Both patterns give 'multiple schedulers'.
**Sources:** <a href="https://kubernetes.io/docs/tasks/extend-kubernetes/configure-multiple-schedulers/" target="_blank">Kubernetes Documentation - Configure Multiple Schedulers</a>
**Tags:** k8s::kcna topic::api topic::scheduling src::session

---

<!-- note:1793835711170 model:Many -->
**Domain:** Schedulers - naming
**Question:** What constraint applies to a scheduler's name in the cluster?
**Options:** A. Must equal the pod's name<br>B. Unique per scheduler cluster-wide — it's the identity pods reference in spec.schedulerName<br>C. Can be shared across schedulers<br>D. Is always 'default-scheduler'
**Answer:** B (2) – unique per scheduler cluster-wide — it's the identity pods reference in spec.schedulerName
**Explanation:** The schedulerName is how kube-scheduler instances/profile claim ownership of pods — collisions mean two processes racing to bind the same pods. The stock scheduler answers to 'default-scheduler'; your second scheduler (or profile) needs its own name like 'my-scheduler', set in KubeSchedulerConfiguration profiles[].schedulerName.
**Sources:** <a href="https://kubernetes.io/docs/tasks/extend-kubernetes/configure-multiple-schedulers/" target="_blank">Kubernetes Documentation - Configure Multiple Schedulers</a>
**Tags:** k8s::kcna topic::api topic::scheduling src::session

---

<!-- note:1793835711180 model:Basic -->
**Front:** Can a cluster run more than one scheduler — and why would it?
**Back:** Yes — a cluster can run several schedulers side by side. Each has a unique name and only watches unbound pods whose <code>spec.schedulerName</code> matches it; pods default to 'default-scheduler'. Use cases: custom placement logic, batch/ML schedulers, testing new scheduling behavior. Deploy one as a Deployment running a second kube-scheduler binary with its own config.
**Tags:** k8s::kcna topic::architecture topic::scheduling src::session

---

<!-- note:1793835711181 model:Basic -->
**Front:** How do you deploy a second scheduler (e.g. 'my-scheduler') into a cluster?
**Back:** The docs' recipe: 1) containerize kube-scheduler, 2) Deployment (kube-system, replicas:1) running <code>kube-scheduler --config=&lt;file&gt;</code>, 3) a ConfigMap holding a <code>KubeSchedulerConfiguration</code> with <code>profiles: [{schedulerName: my-scheduler}]</code> and <code>leaderElect: false</code>, 4) a ServiceAccount bound to <code>system:kube-scheduler</code> ClusterRole so it can watch/bind pods. Pods opt in via <code>spec.schedulerName: my-scheduler</code>.
**Tags:** k8s::kcna topic::scheduling topic::yaml src::session

---

<!-- note:1793836413421 model:Many -->
**Domain:** Scheduling - filter phase
**Question:** Which scheduling step eliminates nodes that CAN'T run the pod (resources, taints, selectors)?
**Options:** A. QueueSort — orders the queue<br>B. Filter — every plugin marks each node feasible or infeasible; survivors move on<br>C. Score — ranks nodes<br>D. Bind — writes the decision
**Answer:** B (2) – Filter — every plugin marks each node feasible or infeasible; survivors move on
**Explanation:** Filter plugins eliminate nodes that CANNOT run the pod: insufficient resources vs requests, taints without tolerations, nodeSelector/affinity mismatch, port conflicts. Each node is evaluated until one plugin rejects it (short-circuit); anything surviving is 'feasible'. If zero nodes pass → PostFilter kicks in (preemption: evict lower-priority pods to make room) or the pod stays Pending.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/" target="_blank">Kubernetes Documentation - Scheduling Framework</a>
**Tags:** k8s::kcna topic::pods topic::scheduling src::session

---

<!-- note:1793836413422 model:Many -->
**Domain:** Scheduling - score phase
**Question:** Filtering left 5 feasible nodes. How does the scheduler pick ONE?
**Options:** A. Filter plugins re-run<br>B. First feasible node wins<br>C. Score plugins rank the feasible nodes (weighted scores); highest wins, ties broken randomly<br>D. kubelet picks
**Answer:** C (3) – Score plugins rank the feasible nodes (weighted scores); highest wins, ties broken randomly
**Explanation:** After filtering leaves multiple feasible nodes, each Score plugin (e.g. NodeResourcesFit, ImageLocality) assigns every node a number; NormalizeScore scales them, weights combine them into a total per node. The pod binds to the highest total — equal scores → random choice. This is the 'prefer' side of scheduling: all surviving nodes CAN run it, scoring picks the best.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/" target="_blank">Kubernetes Documentation - Scheduling Framework</a>
**Tags:** k8s::kcna topic::pods topic::scheduling src::session

---

<!-- note:1793836413423 model:Many -->
**Domain:** Scheduling - queue sort
**Question:** How does the scheduler order pods waiting in its internal scheduling queue?
**Options:** A. FIFO — creation time<br>B. By pod priority — the QueueSort plugin (default PrioritySort) orders the queue, high-priority pods first<br>C. Alphabetically by namespace<br>D. By resource size, smallest first
**Answer:** B (2) – by pod priority — the QueueSort plugin (default PrioritySort) orders the queue, high-priority pods first
**Explanation:** Before anything else, pods wait in the scheduler's internal queue. The QueueSort extension point decides order — only ONE QueueSort plugin may be enabled — and the default, PrioritySort, sorts by pod priority so important workloads get scheduled first. That's why PriorityClass exists: it moves pods up the queue AND drives preemption.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/" target="_blank">Kubernetes Documentation - Scheduling Framework</a>
**Tags:** k8s::kcna topic::pods topic::scheduling src::session

---

<!-- note:1793836413424 model:Many -->
**Domain:** Scheduling - profiles rationale
**Question:** Why did Kubernetes add scheduling PROFILES instead of just recommending multiple scheduler deployments?
**Options:** A. Profiles are faster<br>B. Two schedulers double throughput<br>C. Separate scheduler processes can race each other on the same node; profiles give one process multiple configured personalities<br>D. Profiles enable leader election
**Answer:** C (3) – separate scheduler processes can race each other on the same node; profiles give one process multiple configured personalities
**Explanation:** Multiple scheduler PROCESSES each see only their own queue and can pick the same node concurrently — the loser discovers the conflict at bind time (retry, wasted work). Profiles (stable since v1.19) let ONE kube-scheduler expose several schedulerNames, each with its own plugin config — variety without a second process and without the race window.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/" target="_blank">Kubernetes Documentation - Scheduling Framework</a>
**Tags:** k8s::kcna topic::api topic::scheduling src::session

---

<!-- note:1793836413442 model:Basic (and reversed card) -->
**Front:** How does the kube-scheduler place a pod, step by step?
**Back:** Two cycles: the <b>scheduling cycle</b> (serial — one pod at a time) runs QueueSort → Filter → Score and PICKS a node; the <b>binding cycle</b> (concurrent) applies it via a Binding object → writes <code>spec.nodeName</code>. Between them sits Reserve — marks the node's resources as taken so concurrent binds can't collide. Failed/aborted cycles return the pod to the queue for a retry.
**Tags:** k8s::kcna topic::pods topic::scheduling src::session

---

<!-- note:1793836413443 model:Basic (and reversed card) -->
**Front:** What are scheduler plugins in kube-scheduler?
**Back:** Pluggable extension points in the scheduling framework, compiled into kube-scheduler: QueueSort (queue order), PreFilter/Filter (eliminate infeasible nodes), PostFilter (runs only if nothing fits — e.g. preemption), PreScore/Score (rank feasible nodes), Reserve (claim node before bind), Permit (approve/deny/wait), PreBind/Bind/PostBind (write the assignment). You can compile in your own and toggle them per profile.
**Tags:** k8s::kcna topic::api topic::scheduling src::session

---

<!-- note:1793836413464 model:Cloze -->
**Text:** Second profile with customized plugins:<br><br><code>apiVersion: {{c1::kubescheduler.config.k8s.io/v1}}<br>kind: {{c2::KubeSchedulerConfiguration}}<br>{{c3::profiles}}:<br>- {{c4::schedulerName}}: default-scheduler<br>- schedulerName: no-scoring<br>  {{c5::plugins}}:<br>    {{c6::score}}:<br>      {{c7::disabled}}: [{name: NodeResourcesFit}]<br>      {{c8::enabled}}: [{name: MyScorer}]</code>
**Back Extra:** Each profile = its own schedulerName (pods select via spec.schedulerName) + plugin config. plugins.&lt;extensionPoint&gt;.disabled removes stock plugins (name: '*' disables all at that point); enabled adds custom ones (compiled into the scheduler). Extension points: queueSort, preFilter, filter, postFilter, preScore, score, reserve, permit, preBind, bind, postBind.
**Tags:** k8s::kcna topic::scheduling topic::yaml src::session

---

<!-- note:1793837227572 model:Many -->
**Domain:** Taints - NoExecute meaning
**Question:** What does the taint effect "NoExecute" indicate in Kubernetes?
**Options:** A. Pods will be evicted immediately from the node, if they do not tolerate the taint<br>B. Pods will not be scheduled on the node.<br>C. Pods will be scheduled with a higher priority on the node.<br>D. System will try to avoid placing a pod on the node, but it is not guaranteed.
**Answer:** A (1) – Pods will be evicted immediately from the node, if they do not tolerate the taint
**Explanation:** NoExecute is the aggressive effect: it evicts running pods that don't tolerate the taint AND blocks new ones. (Pods that DO tolerate without tolerationSeconds stay forever; with tolerationSeconds they survive only that long.) The course's other options map to the remaining effects: 'pods will not be scheduled' = NoSchedule; 'try to avoid, not guaranteed' = PreferNoSchedule.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/" target="_blank">Kubernetes Documentation - Taints and Tolerations</a>
**Tags:** k8s::kcna topic::scheduling topic::taints src::session

---

<!-- note:1793837334262 model:Many -->
**Domain:** NodeAffinity - type semantics
**Question:** What does the TYPE of node affinity in Kubernetes define?
**Options:** A. How many nodes can match the rule<br>B. The scheduler's behavior regarding the rule at scheduling time AND during the pod's execution<br>C. Which node labels exist in the cluster<br>D. The weight given to preferred rules
**Answer:** B (2) – the scheduler's behavior regarding the rule at scheduling time AND during the pod's execution
**Explanation:** The type name literally spells out behavior at two lifecycle stages: 'required/preferred' + 'DuringScheduling' = hard rule (pod won't place without a match) vs soft preference (schedules anyway); 'IgnoredDuringExecution' = after the pod runs, node-label changes are ignored — no eviction. The unimplemented 'requiredDuringExecution' would have evicted on label changes.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Documentation - Assign Pods to Nodes</a>
**Tags:** k8s::kcna topic::affinity topic::scheduling src::session

---
<!-- note:1793915613867 model:Many -->
**Domain:** Scheduling - nodeSelector syntax
**Question:** The correct nodeSelector format is:
**Options:** A. <code>nodeSelector: { disk: ssd }</code><br>B. <code>nodeSelector: ["disk=ssd"]</code><br>C. <code>nodeSelector: (disk=ssd)</code><br>D. <code>nodeSelector: "disk=ssd"</code>
**Answer:** A – nodeSelector: { disk: ssd }
**Explanation:** nodeSelector is a key/value map, not a query string: under spec.nodeSelector you write YAML labels as key: value pairs — <code>nodeSelector: { disk: ssd }</code> (or block form with each pair on its own line) pins the pod to nodes carrying disk=ssd, with ALL pairs required (AND). The 'disk=ssd' expression style is kubectl's -l/<code>--selector</code> flag syntax (e.g. <code>kubectl get pods -l disk=ssd</code>), NOT pod-spec field syntax — a common mix-up. nodeSelector only does equality; for operators like In/NotIn use nodeAffinity matchExpressions.
**Sources:** <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/" target="_blank">Kubernetes Docs - Assign Pods to Nodes</a>
**Tags:** k8s::kcna topic::scheduling topic::nodeselector topic::yaml src::session

---
