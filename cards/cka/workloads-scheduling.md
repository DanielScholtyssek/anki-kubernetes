# CKA - Certified Kubernetes Administrator — Workloads & Scheduling

> Deck: `CKA - Certified Kubernetes Administrator` · Group: `Workloads & Scheduling` · Notes: 250 · Models: Basic, Basic (and reversed card), Cloze

<!-- note:1794496839228 model:Basic -->
**Front:** Why use a Deployment instead of creating a ReplicaSet directly?
**Back:** A ReplicaSet only guarantees N identical pods stay alive — it has no update strategy. A Deployment adds declarative updates on top: it creates a new ReplicaSet per pod-template version, rolls between them at a controlled rate, keeps old ReplicaSets for rollback, and tracks rollout history. That's why the docs recommend Deployments over managing ReplicaSets directly.
**Tags:** k8s::cka topic::deployments topic::replicasets src::session

---

<!-- note:1794496839229 model:Basic -->
**Front:** How does a Deployment manage pods internally — what is the role of its ReplicaSets?
**Back:** The Deployment controller creates one ReplicaSet per pod-template version — named <code>&lt;deployment&gt;-&lt;pod-template-hash&gt;</code>, and pods get a <code>pod-template-hash</code> label linking them. Each ReplicaSet does the actual pod-keeping; the Deployment orchestrates which ReplicaSet is scaled up or down and records each template version as a revision.
**Tags:** k8s::cka topic::deployments topic::replicasets src::session

---

<!-- note:1794496839230 model:Basic -->
**Front:** Walk through what happens during a Deployment rolling update.
**Back:** A rolling update replaces pods gradually instead of all at once: when the pod template changes, the Deployment creates a new ReplicaSet and scales it up while scaling the old ReplicaSet down at the same time, until the new one holds all desired replicas and the old one is at 0 (kept for rollback). The app keeps serving throughout because old pods stay up while new ones come online.
**Tags:** k8s::cka topic::deployments topic::rollouts src::session

---

<!-- note:1794496839231 model:Basic -->
**Front:** What do <code>maxSurge</code> and <code>maxUnavailable</code> control in a Deployment's rollingUpdate strategy?
**Back:** They throttle the rollout: <code>maxSurge</code> is how many pods ABOVE the desired count may exist during the update (extra new pods), <code>maxUnavailable</code> is how many pods may be unavailable during it. Both default to 25%. They also protect you — a broken rollout stalls instead of killing everything, since maxUnavailable limits how many old pods can go down.
**Tags:** k8s::cka topic::deployments topic::rollouts src::session

---

<!-- note:1794496839232 model:Basic -->
**Front:** How does the <code>Recreate</code> deployment strategy differ from the default <code>RollingUpdate</code>?
**Back:** <code>spec.strategy.type: Recreate</code> kills ALL existing pods before creating the new version — simple but causes downtime. The default <code>RollingUpdate</code> replaces pods gradually (new ReplicaSet scaled up, old scaled down) so the app stays available. Use Recreate only when versions can't run side by side (e.g. single-writer stateful apps).
**Tags:** k8s::cka topic::deployments topic::rollouts src::session

---

<!-- note:1794496839233 model:Basic -->
**Front:** How do you roll back a Deployment to a working version, and what actually happens?
**Back:** <code>kubectl rollout undo deployment/web</code> returns to the previous revision — the Deployment scales the old ReplicaSet back up and the new one down. <code>--to-revision=N</code> targets a specific revision from <code>kubectl rollout history</code>. Only the pod template is rolled back (replicas aren't). Old ReplicaSets are kept per <code>revisionHistoryLimit</code> (default 10).
**Tags:** k8s::cka topic::deployments topic::rollouts src::session

---

<!-- note:1794496839234 model:Basic -->
**Front:** Which <code>kubectl rollout</code> subcommands manage a Deployment's lifecycle, and what does each do?
**Back:** <code>status</code> — watch rollout progress (e.g. stuck rollouts); <code>history</code> — list revisions; <code>pause</code>/<code>resume</code> — hold a rollout to batch several template fixes, then release; <code>restart</code> — start a fresh rollout of the same template (new pods); <code>undo</code> — roll back to a previous revision.
**Tags:** k8s::cka topic::deployments topic::kubectl src::session

---

<!-- note:1794496839235 model:Basic -->
**Front:** You update a Deployment's pod image from nginx:1.14 to nginx:1.16. With the default strategy, what does the Deployment controller do?
**Back:** It creates a new ReplicaSet and scales it up while scaling the old one down<br><br>RollingUpdate (the default strategy) spins up a new ReplicaSet for the changed pod template and gradually scales it to the desired count while scaling the old ReplicaSet to 0 — so the app never fully goes down. Deleting everything first is the Recreate strategy; the Deployment itself is never recreated.
**Tags:** k8s::cka topic::deployments topic::rollouts src::session

---

<!-- note:1794496839236 model:Basic -->
**Front:** Which change to a Deployment triggers a new rollout and creates a new revision?
**Back:** Updating the container image in spec.template<br><br>A rollout (and a new revision) is triggered if and only if .spec.template changes — e.g. a new container image or template labels. Scaling replicas, renaming the Deployment, or changing spec.replicas only adjusts the current ReplicaSet's count; it does not roll out a new version.
**Tags:** k8s::cka topic::deployments topic::rollouts src::session

---

<!-- note:1794496839237 model:Basic -->
**Front:** How do you record WHY a Deployment was changed so it shows up in its rollout history?
**Back:** Set the <code>kubernetes.io/change-cause</code> annotation — it's copied onto each new revision and shown in the CHANGE-CAUSE column of <code>kubectl rollout history</code>:<br><code>kubectl annotate deployment/web kubernetes.io/change-cause="bump to nginx:1.16"</code><br>(The old <code>--record</code> flag that did this automatically is deprecated.)
**Tags:** k8s::cka topic::deployments topic::kubectl src::session

---

<!-- note:1794496839238 model:Basic -->
**Front:** What is a blue/green deployment in Kubernetes?
**Back:** Two complete environments run side by side: 'blue' = the current live version, 'green' = the new version fully deployed and verified. All traffic switches at once by repointing the Service's pod selector to the green pods. Rollback is instant — flip the selector back to blue. Trade-off: you need capacity for two full copies at once.
**Tags:** k8s::cka topic::deployments topic::strategy src::session

---

<!-- note:1794496839239 model:Basic -->
**Front:** What is a canary deployment, and why use it?
**Back:** Send the new version to a small slice of traffic first (a few percent of pods/users), watch error rates and metrics, then ramp up gradually until it owns all traffic. It limits blast radius when a bad release ships — unlike RollingUpdate, which swaps pods steadily regardless of correctness. Needs old+new ReplicaSets sharing a Service, or progressive-delivery tooling (Argo Rollouts, Flagger, service mesh) — a native Deployment can't weight traffic percentages.
**Tags:** k8s::cka topic::deployments topic::strategy src::session

---

<!-- note:1794496839240 model:Basic -->
**Front:** Which deployment strategies exist, and which are built into the Deployment object itself?
**Back:** Only two: <code>RollingUpdate</code> (default — gradually swaps pods, zero downtime) and <code>Recreate</code> (kills all old pods first, then starts new — brief downtime). Blue/green and canary are NOT spec.strategy types; they're patterns built on top via Service selectors or external progressive-delivery tools.
**Tags:** k8s::cka topic::deployments topic::strategy src::session

---

<!-- note:1794496839241 model:Basic -->
**Front:** A team needs zero downtime AND an instant full rollback of a release, and they can afford running two complete environments. Which strategy fits?
**Back:** Blue/green<br><br>Blue/green runs two complete environments and switches all traffic at once via the Service selector — rollback is just flipping the selector back. Canary also limits risk but ramps gradually (not instant-all-at-once); RollingUpdate rolls back pod-by-pod; Recreate kills everything first — the opposite of zero downtime.
**Tags:** k8s::cka topic::deployments topic::strategy src::session

---

<!-- note:1794496839242 model:Basic -->
**Front:** Which of these is NOT a valid value for a Deployment's <code>spec.strategy.type</code>?
**Back:** Canary<br><br>spec.strategy.type accepts only RollingUpdate and Recreate. Canary is a deployment pattern implemented outside the Deployment spec — via multiple ReplicaSets sharing a Service, or progressive-delivery tools like Argo Rollouts — not a value you can set in the manifest.
**Tags:** k8s::cka topic::deployments topic::strategy src::session

---

<!-- note:1794496839243 model:Basic -->
**Front:** What does <code>kubectl rollout status</code> do, and when do you use it?
**Back:** It streams a rollout's progress live — <code>kubectl rollout status deployment/web</code> prints e.g. "2 out of 3 new replicas have been updated" and exits when the rollout finishes. Run it right after <code>kubectl set image</code>/<code>apply</code> to confirm the update actually completed; if it hangs, the rollout is stuck (e.g. bad image → ImagePullBackOff). Ctrl-C stops watching.
**Tags:** k8s::cka topic::deployments topic::kubectl src::session

---

<!-- note:1794496839244 model:Basic -->
**Front:** What does <code>kubectl rollout history</code> show, and what is it used for?
**Back:** It lists a Deployment's revisions — one per pod-template change (REVISION 1, 2, 3…) plus the CHANGE-CAUSE column fed by the <code>kubernetes.io/change-cause</code> annotation. <code>--revision=N</code> shows the pod template that revision held. It's how you pick a target for <code>kubectl rollout undo --to-revision=N</code>.
**Tags:** k8s::cka topic::deployments topic::rollouts src::session

---

<!-- note:1794496839245 model:Basic -->
**Front:** You update a Deployment's image from nginx:1.14 to nginx:1.16 — what do you see in <code>kubectl get rs</code> during and after the upgrade?
**Back:** A new ReplicaSet appears — <code>&lt;deploy&gt;-&lt;newhash&gt;</code> — and scales 0→3 while the old one <code>&lt;deploy&gt;-&lt;oldhash&gt;</code> scales 3→0. When done, BOTH remain: the old RS stays at 0 replicas as the rollback target (kept up to <code>revisionHistoryLimit</code>, default 10). Each template version gets its own RS, so a Deployment accumulates one scaled-to-0 RS per past revision.
**Tags:** k8s::cka topic::deployments topic::replicasets src::session

---

<!-- note:1794496839246 model:Basic -->
**Front:** You just ran <code>kubectl set image</code> to trigger a rollout. Which command confirms the rollout finished successfully?
**Back:** kubectl rollout status<br><br>rollout status watches the rollout live and reports when it finishes (or hangs if it's stuck). get pods shows a snapshot — it can't tell you whether the rollout is done; rollout history lists past revisions, not current progress; describe shows events but doesn't wait for completion.
**Tags:** k8s::cka topic::deployments topic::kubectl src::session

---

<!-- note:1794496839247 model:Basic -->
**Front:** <code>kubectl get rs</code> shows two ReplicaSets for one Deployment — one at 3 replicas, one at 0. Why does the 0-replica one still exist?
**Back:** It's the previous revision's ReplicaSet, kept as a rollback target<br><br>Each Deployment keeps old ReplicaSets scaled to 0 — that's what makes kubectl rollout undo work; revisionHistoryLimit (default 10) controls how many are retained. It's not an error or leftover garbage: the Deployment manages all ReplicaSets it owns across revisions.
**Tags:** k8s::cka topic::deployments topic::replicasets src::session

---

<!-- note:1794496839251 model:Basic -->
**Front:** What does a label selector do in Kubernetes, and why is it important?
**Back:** A selector is a query over labels that picks out a set of objects — it is Kubernetes' core grouping primitive. It's how loosely coupled pieces find each other: a Service uses a selector to pick the pods it load-balances traffic to, a ReplicaSet uses one to count the pods it must keep alive, and <code>kubectl get -l</code> filters objects the same way.
**Tags:** k8s::cka topic::labels topic::selectors src::session

---

<!-- note:1794496839252 model:Basic -->
**Front:** How does a ReplicaSet use labels and selectors to know which pods it manages?
**Back:** <code>spec.selector.matchLabels</code> is a label query — every pod carrying those labels counts toward <code>spec.replicas</code>, whether the ReplicaSet created it from its template or adopted an existing matching pod. Removing a matching label from a pod takes it out of the set, and the ReplicaSet immediately creates a replacement to restore the count.
**Tags:** k8s::cka topic::labels topic::replicasets topic::selectors src::session

---

<!-- note:1794496839253 model:Basic -->
**Front:** A pod has labels <code>tier=frontend</code> and <code>environment=prod</code>. Which selector matches it?
**Back:** tier in (frontend, cache)<br><br>in/notin/exists are set-based operators: tier in (frontend, cache) matches because the pod's tier value 'frontend' is in the set. tier=backend and environment in (dev, staging) fail equality/membership; !tier selects objects that do NOT have the tier key at all. Multiple comma-separated requirements would be ANDed.
**Tags:** k8s::cka topic::labels topic::selectors src::session

---

<!-- note:1794496839254 model:Basic -->
**Front:** How does a pod get its IP address in Kubernetes?
**Back:** When a pod is created, the CNI plugin assigns it a unique, cluster-wide IP address from the pod network (invoked via the kubelet → container runtime chain). Every container INSIDE one pod shares that single IP and network namespace — they reach each other over localhost. A pod's IP dies with the pod; a new pod gets a new IP.
**Tags:** k8s::cka topic::networking topic::pods src::session

---

<!-- note:1794496839255 model:Basic -->
**Front:** What are the connectivity rules every Kubernetes cluster network must satisfy?
**Back:** The Kubernetes network model guarantees: (1) every pod gets its own cluster-wide IP; (2) all pods can talk to all other pods on ANY node, directly, without NAT or proxies — the destination IP is the pod's real IP; (3) node agents (kubelet, system daemons) can talk to all pods on their node. A pod sees its own IP as the same address others see it as. (Intentional segmentation is possible via NetworkPolicy.)
**Tags:** k8s::cka topic::networking topic::pods src::session

---

<!-- note:1794496839256 model:Basic -->
**Front:** Why does Kubernetes require pod-to-pod communication without NAT?
**Back:** It makes pods behave like independent machines on one flat network: no port mapping, no NAT, no links needed — pod A on node 1 reaches pod B on node 3 directly by its pod IP. Older container systems forced you to map container ports onto host ports to make containers reachable across hosts; Kubernetes removed that pain by design.
**Tags:** k8s::cka topic::networking topic::pods src::session

---

<!-- note:1794496839258 model:Basic -->
**Front:** Which statement is a requirement of the Kubernetes network model?
**Back:** Pods on any node can reach pods on other nodes directly, without NAT<br><br>The Kubernetes network model requires flat pod-to-pod connectivity: every pod has its own cluster-wide IP and can reach any other pod without NAT, regardless of which node it's on. Pods do NOT share the node IP, and cross-node traffic is allowed by default.
**Tags:** k8s::cka topic::networking topic::pods src::session

---

<!-- note:1794496839261 model:Basic -->
**Front:** How does Kubernetes scale an application up and down at the pod level?
**Back:** Under more load Kubernetes creates additional pods — extra instances of the same application — which the scheduler can place on other nodes in the cluster. Scaling down means removing pods again.
**Tags:** k8s::cka topic::pods src::session

---

<!-- note:1794496839262 model:Basic -->
**Front:** Can a pod contain more than one container, and when would you do that?
**Back:** Yes — but usually different containers, not copies of the same one. A common pattern is a main application container plus helper 'sidecar' containers that support it (e.g. a log shipper or proxy).
**Tags:** k8s::cka topic::pods src::session

---

<!-- note:1794496839263 model:Basic -->
**Front:** How can containers inside the same pod communicate with each other?
**Back:** They share the same network namespace and IP address, so they can talk to each other over localhost. They can also exchange data through volumes shared inside the pod.
**Tags:** k8s::cka topic::pods src::session

---

<!-- note:1794496839264 model:Basic -->
**Front:** Which kubectl command creates a pod running nginx?
**Back:** kubectl run nginx --image=nginx — creates a pod named 'nginx' that runs a container built from the 'nginx' image.
**Tags:** k8s::cka topic::pods src::session

---

<!-- note:1794496839265 model:Basic -->
**Front:** Where does the image in `kubectl run nginx --image=nginx` come from?
**Back:** From a container image registry — Docker Hub by default (short names like 'nginx' resolve to Docker Hub's official library). To use a private registry, specify its full path, e.g. --image=registry.example.com/app:tag.
**Tags:** k8s::cka topic::pods src::session

---

<!-- note:1794496839266 model:Basic -->
**Front:** How do you list pods in a cluster, and what are useful variants of the command?
**Back:** kubectl get pods lists pods and their status. Useful variants: kubectl get pods -o wide (pod IPs and which node each runs on), kubectl get pods -A (all namespaces), kubectl get pods -w (watch for changes), kubectl describe pod <name> (full details and events).
**Tags:** k8s::cka topic::pods src::session

---

<!-- note:1794496839267 model:Basic -->
**Front:** How can a user access an application running inside a pod (e.g. the nginx container)?
**Back:** A pod only gets a cluster-internal IP, so it cannot be reached from outside directly. For a quick test use kubectl port-forward pod/nginx 8080:80 and browse to localhost:8080; for real access you expose the pod through a Service (e.g. type NodePort or LoadBalancer).
**Tags:** k8s::cka topic::pods src::session

---

<!-- note:1794496839268 model:Basic -->
**Front:** Which command creates a pod named 'nginx' running the nginx image?
**Back:** kubectl run nginx --image=nginx<br><br>kubectl run creates a single pod; --image tells the runtime which image to pull (Docker Hub by default). kubectl create/deploy/start alone do not produce a running pod this way — deployments are created with kubectl create deployment.
**Tags:** k8s::cka topic::pods src::session

---

<!-- note:1794496839269 model:Basic -->
**Front:** What problem does a ReplicaSet solve — why not just create Pods directly?
**Back:** It guarantees that a specified number of pod replicas are running at any given time. Without it, a pod that crashes or is deleted is just gone; the ReplicaSet controller continuously compares desired count (<code>spec.replicas</code>) with actual pods and creates replacements from its pod template — or removes extras if there are too many.
**Tags:** k8s::cka topic::pods topic::replicasets src::session

---

<!-- note:1794496839270 model:Basic -->
**Front:** How does a ReplicaSet provide high availability for an application?
**Back:** High availability = the app keeps serving even when individual pods or nodes fail. A ReplicaSet delivers this by keeping N identical pods running and replacing any that die — the scheduler places replacement pods on surviving nodes, so losing one node doesn't take the application down while replicas remain elsewhere.
**Tags:** k8s::cka topic::ha topic::replicasets src::session

---

<!-- note:1794496839271 model:Basic -->
**Front:** How do ReplicaSets enable scaling and load balancing of pods?
**Back:** Scaling: raising <code>spec.replicas</code> (e.g. <code>kubectl scale rs/name --replicas=5</code>) makes the controller create more pod copies, spread across cluster nodes. Load balancing: a Service in front of those pods distributes traffic across all matching replicas. The ReplicaSet keeps the pool at the right size; the Service spreads the load.
**Tags:** k8s::cka topic::pods topic::replicasets src::session

---

<!-- note:1794496839272 model:Basic -->
**Front:** What is the difference between a ReplicationController and a ReplicaSet?
**Back:** Same purpose — keep N pod replicas running — but ReplicationController is the legacy predecessor, superseded by ReplicaSet (and Deployment on top). Practical difference: ReplicationController selectors are equality-based only, while ReplicaSet supports set-based selectors (<code>matchExpressions</code>, e.g. <code>tier in (frontend, backend)</code>) in addition to <code>matchLabels</code>. New work uses ReplicaSet — usually indirectly via Deployment.
**Tags:** k8s::cka topic::pods topic::replicasets src::session

---

<!-- note:1794496839273 model:Basic -->
**Front:** Can a ReplicaSet manage pods it did not create itself?
**Back:** Yes — a ReplicaSet counts every pod matching its <code>spec.selector</code>, not only pods from its template. An unowned pod (no controller in <code>metadata.ownerReferences</code>) with matching labels gets adopted and counted toward the replica total; if that pushes the count above <code>spec.replicas</code>, the ReplicaSet terminates the extras.
**Tags:** k8s::cka topic::pods topic::replicasets src::session

---

<!-- note:1794496839274 model:Basic -->
**Front:** Which field in a ReplicaSet manifest determines which pods it manages?
**Back:** spec.selector (matchLabels)<br><br>The selector is a required field — usually spec.selector.matchLabels — and it must equal spec.template.metadata.labels or the API rejects the manifest. replicas says how many pods to keep; it does not identify which ones. Ownership is recorded on the pod side in metadata.ownerReferences.
**Tags:** k8s::cka topic::pods topic::replicasets src::session

---

<!-- note:1794496839275 model:Basic -->
**Front:** A ReplicaSet wants 4 replicas and a node hosting one of them dies. What happens next?
**Back:** The ReplicaSet creates a replacement pod on a surviving node<br><br>The controller constantly reconciles desired (4) vs actual (now 3) pods and stamps out a new pod from spec.template; the scheduler places it on a healthy node. Meanwhile the 3 surviving replicas keep serving traffic — that is the high-availability role of replication.
**Tags:** k8s::cka topic::ha topic::replicasets src::session

---

<!-- note:1794496839276 model:Basic -->
**Front:** Why must a ReplicaSet manifest always include <code>spec.template</code>, even if matching pods already exist?
**Back:** Because the template is the pod blueprint the ReplicaSet stamps out whenever actual < desired replicas. Without it the controller wouldn't know what to create — image, ports, labels — so the API requires it even when matching pods already exist. Its <code>template.metadata.labels</code> must also match <code>spec.selector</code>, or creation is rejected.
**Tags:** k8s::cka topic::pods topic::replicasets src::session

---

<!-- note:1794496839277 model:Basic -->
**Front:** What are the two ways to change a ReplicaSet's replica count, and which is safe for GitOps?
**Back:** Declarative (GitOps-safe): edit <code>spec.replicas</code> in the YAML manifest and <code>kubectl apply -f</code> — git stays the source of truth. Imperative: <code>kubectl scale --replicas=5 rs/frontend</code> (or <code>--replicas=5 -f file.yaml</code>, which overrides the file's count) — changes only the live object, so the manifest drifts and the next apply/sync silently reverts the scale.
**Tags:** k8s::cka topic::gitops topic::replicasets src::session

---

<!-- note:1794496839278 model:Basic -->
**Front:** Your team stores manifests in git (GitOps). A colleague runs <code>kubectl scale --replicas=8 rs/web</code> for a traffic spike. What's the risk?
**Back:** git still holds the old count, so the next apply/sync reverts it<br><br>kubectl scale patches the live object only — the manifest in git still says the old spec.replicas. GitOps treats git as the source of truth, so the next apply or controller sync restores the old count. The safe way is to edit spec.replicas in the YAML, commit, and apply.
**Tags:** k8s::cka topic::gitops topic::replicasets src::session

---

<!-- note:1794496839279 model:Basic -->
**Front:** What problem does a Kubernetes Service solve, and how does it enable loose coupling?
**Back:** Pods are ephemeral — they're created, destroyed and rescheduled, so their IPs churn constantly. A Service puts a STABLE virtual IP and DNS name in front of a selector-matched set of pods: clients talk to one fixed endpoint while the backend pods come and go. This decouples microservices — a frontend never tracks pod IPs — and the Service load-balances across whichever pods match its selector right now.
**Tags:** k8s::cka topic::networking topic::services src::session

---

<!-- note:1794496839295 model:Basic -->
**Front:** Name useful crictl commands for debugging containers on a node.
**Back:** crictl ps — running containers; crictl pods — pod sandboxes; crictl images — images; crictl logs — container logs; crictl exec — run a command inside a container; crictl inspect — full container/pod details; crictl stats — resource usage.
**Tags:** k8s::cka topic::troubleshooting src::session

---

<!-- note:1794496839297 model:Basic -->
**Front:** What is a manifest file in Kubernetes and what is it used for?
**Back:** A manifest is a YAML file (JSON is also accepted) that declaratively describes a Kubernetes object — such as a Pod, Service, or Deployment — and its desired state. You submit it with <code>kubectl apply -f file.yaml</code> and the control plane continuously works to make the cluster match what the file describes.
**Tags:** k8s::cka topic::api topic::yaml src::session

---

<!-- note:1794496839299 model:Basic -->
**Front:** What goes into the <code>metadata</code> field of a Kubernetes manifest?
**Back:** Data that uniquely identifies the object: at minimum <code>metadata.name</code>; optionally <code>namespace</code>, <code>labels</code> and <code>annotations</code>. The cluster also fills in a <code>uid</code>. Metadata is about the object's identity — not its behavior (that's <code>spec</code>).
**Tags:** k8s::cka topic::api topic::yaml src::session

---

<!-- note:1794496839300 model:Basic -->
**Front:** What kind of information goes into the <code>spec</code> field of a manifest?
**Back:** <code>spec</code> holds the object's desired state — its full configuration. What lands there depends on the kind: a Pod spec lists <code>containers</code> (image, ports, env, resources); a Deployment spec has <code>replicas</code>, <code>selector</code> and a pod <code>template</code>; a Service spec has <code>selector</code> and <code>ports</code>. The control plane continuously works to make the object's <code>status</code> (current state, written by the cluster) match this spec.
**Tags:** k8s::cka topic::api topic::yaml src::session

---

<!-- note:1794496839301 model:Basic -->
**Front:** Why do the fields under <code>spec</code> differ between a Pod manifest and a Deployment manifest?
**Back:** Because the spec schema is defined per <code>kind</code> — each object type has its own set of allowed fields under <code>spec</code>. There is no universal spec format; you look up the valid fields for the specific kind in the Kubernetes API reference (e.g. the Pod spec page vs the StatefulSet spec page).
**Tags:** k8s::cka topic::api topic::yaml src::session

---

<!-- note:1794496839308 model:Basic -->
**Front:** Which command creates a Deployment named web running 3 replicas of nginx?
**Back:** <code>kubectl create deployment web --image=nginx --replicas=3</code><br><br><code>kubectl create deployment</code> makes the Deployment object; <code>--image</code> sets the pod template's container image, <code>--replicas</code> sets the desired count (default 1). Imperative equivalent of a YAML Deployment manifest. (<code>kubectl run</code> creates a bare Pod, not a Deployment.)
**Tags:** k8s::cka src::session topic::deployments topic::kubectl

---

<!-- note:1794496839309 model:Basic -->
**Front:** Which kubectl command shows documentation for a resource's fields, e.g. <code>kubectl explain pod.spec.containers</code>?
**Back:** <code>kubectl explain</code><br><br><code>kubectl explain</code> prints the schema/documentation for a resource's fields — e.g. <code>kubectl explain deployment.spec.strategy</code> describes every field, its type and meaning. It's the built-in way to answer 'what does this manifest field do' without leaving the terminal.
**Tags:** k8s::cka src::session topic::kubectl topic::yaml

---

<!-- note:1794496839310 model:Basic -->
**Front:** How do you list pods with kubectl, and what do the flags <code>-o wide</code>, <code>-A</code> and <code>-w</code> add?
**Back:** <code>kubectl get pods</code> lists pods in the current namespace with status. Useful variants: <code>-o wide</code> (adds pod IPs + which node each runs on), <code>-A</code>/<code>--all-namespaces</code> (every namespace), <code>-w</code> (watch for changes). For detail on one pod incl. events: <code>kubectl describe pod &lt;name&gt;</code>.
**Tags:** k8s::cka src::session topic::kubectl topic::pods

---

<!-- note:1794496839311 model:Basic -->
**Front:** Which of these is the DECLARATIVE object-management approach in Kubernetes?
**Back:** <code>kubectl apply -f deployment.yaml</code><br><br>apply -f is the DECLARATIVE path: it merges the file's desired state into the live object and records last-applied-configuration to compute future diffs. create/replace -f are the middle tier ('imperative object configuration' — file-driven but verb-led: create fails if it exists, replace swaps the whole object). create/edit/run/expose are pure imperative commands.
**Tags:** k8s::cka src::session topic::kubectl topic::yaml

---

<!-- note:1794496839312 model:Basic -->
**Front:** Which group contains ONLY imperative commands (no manifest file involved)?
**Back:** <code>kubectl run</code>, <code>kubectl create deployment</code>, <code>kubectl expose</code><br><br>Imperative commands tell the cluster WHAT to do right now: run, create deployment, expose, scale, delete — no file, no recorded desired state. The -f variants of create/replace are imperative object configuration (middle tier); apply -f is the declarative tier. get/describe are read-only, not management.
**Tags:** k8s::cka src::session topic::kubectl topic::yaml

---

<!-- note:1794496839313 model:Basic -->
**Front:** Why is the declarative approach preferred for production and GitOps workflows?
**Back:** Manifests live in Git as a reviewable source of truth, and apply is idempotent and detects drift via last-applied-configuration<br><br>Declarative YAML can be versioned, reviewed and audited in Git (the GitOps model), re-applied safely (idempotent), and apply's last-applied annotation reveals drift. Imperative commands leave no record — nothing to diff, review or re-converge from.
**Tags:** k8s::cka src::session topic::gitops topic::kubectl

---

<!-- note:1794496839314 model:Basic -->
**Front:** You write a Terraform config describing what infrastructure SHOULD exist, and Terraform works out the steps to reach it. Which approach is this?
**Back:** Declarative<br><br>Terraform is the classic declarative IaC tool: you write config describing the END state (which resources should exist), and Terraform's engine computes the plan — what to create/change/destroy to get there. Same model as <code>kubectl apply</code>. Imperative tools/scripts instead encode each step to execute.
**Tags:** k8s::cka src::session topic::declarative topic::gitops

---

<!-- note:1794496839315 model:Basic -->
**Front:** <code>kubectl set image deployment/web nginx=nginx:2.0</code> — which management approach is this?
**Back:** An imperative command — it directly instructs the cluster to change the image NOW, with no declared desired state<br><br>set image, like run/create/expose/scale/edit/delete, is imperative: one-shot instruction, nothing recorded to converge against. The declarative equivalent is editing the image in the manifest and re-running <code>kubectl apply -f</code>
**Tags:** k8s::cka src::session topic::declarative topic::kubectl

---

<!-- note:1794496839316 model:Basic -->
**Front:** You run <code>kubectl apply -f app.yaml</code> on an object that already exists. What does apply do?
**Back:** It compares the manifest, the live object AND last-applied-configuration, then applies only the needed changes (create or patch)<br><br>apply is a three-way merge: file's desired state vs the object's live state vs the recorded last-applied-configuration. Object missing → created; exists → patched to match the declaration. That's why the same file can be applied repeatedly and why it's the declarative workflow.
**Tags:** k8s::cka src::session topic::declarative topic::kubectl

---

<!-- note:1794496839318 model:Basic -->
**Front:** What does the <code>kubectl.kubernetes.io/last-applied-configuration</code> annotation on an object store?
**Back:** The JSON of the manifest most recently applied via <code>kubectl apply</code><br><br>Each apply writes the applied manifest (as JSON) into the kubectl.kubernetes.io/last-applied-configuration annotation on the object. It's the third leg of apply's three-way merge — file vs live vs last-applied — letting kubectl compute diffs, detect drift, and delete fields removed from the file. <code>kubectl get -o yaml</code> shows LIVE state; this annotation remembers what YOU declared.
**Tags:** k8s::cka src::session topic::declarative topic::kubectl topic::yaml

---

<!-- note:1794496839325 model:Basic -->
**Front:** Which pods does the kube-scheduler pick up and try to place?
**Back:** pods whose spec.nodeName is still unset (unassigned)<br><br>The scheduler watches for newly created pods that have no node assigned — i.e. spec.nodeName is empty. For each it runs filtering (which nodes are feasible) then scoring (which is best), then binds the pod. Pods already carrying a nodeName never reach the scheduler — that's why manually setting it bypasses scheduling entirely.
**Tags:** k8s::cka src::session topic::pods topic::scheduling

---

<!-- note:1794496839326 model:Basic -->
**Front:** Can you change spec.nodeName on an already-created pod to move it to another node?
**Back:** no — nodeName is immutable after creation; recreate the pod to move it<br><br>spec.nodeName can only be written at two moments: by you at pod creation, or by the scheduler via a Binding while the pod is still unassigned. Once set it's read-only — kubectl patch/edit on it is rejected. To move a scheduled pod you must delete and recreate it (or let a Deployment do the rollout).
**Tags:** k8s::cka src::session topic::pods topic::scheduling

---

<!-- note:1794496839327 model:Basic -->
**Front:** Without kube-scheduler, how do you assign an already-created pod that has no nodeName to a node?
**Back:** create a Binding object (POST JSON to the pod's binding subresource naming the target node)<br><br>The Binding object is what the scheduler itself creates after picking a node. Doing it manually: POST to /api/v1/namespaces/&lt;ns&gt;/pods/&lt;pod&gt;/binding with a body like {"target": {"kind": "Node", "name": "node2"}} — the API server then writes nodeName and the kubelet takes over. It only works while nodeName is still empty.
**Tags:** k8s::cka src::session topic::api topic::scheduling

---

<!-- note:1794496839328 model:Basic -->
**Front:** What does <code>kubectl get pods -l 'app=web,env=prod'</code> return?
**Back:** only pods matching ALL criteria — multiple -l requirements are ANDed<br><br>Comma-separated selector requirements must ALL be satisfied — it's an AND, not OR. Equality selectors match exact values (app=web, env!=dev); set-based selectors match membership (env in (prod,qa), tier notin (cache), !key = absence). Everything from kubectl -l to NetworkPolicy podSelector uses the same requirement logic.
**Tags:** k8s::cka src::session topic::kubectl topic::labels

---

<!-- note:1794496839329 model:Basic -->
**Front:** Where in a pod/Deployment manifest do an object's OWN labels always go?
**Back:** metadata.labels — the object's own label set<br><br>Labels always go under metadata.labels on the object itself: metadata: {labels: {app: web, tier: frontend}}. The consumers live elsewhere in OTHER objects' specs: Service spec.selector, ReplicaSet/Deployment spec.selector.matchLabels, NetworkPolicy podSelector. 'Label everything, select from outside' is the pattern.
**Tags:** k8s::cka src::session topic::labels topic::yaml

---

<!-- note:1794496839330 model:Basic -->
**Front:** You want to record build version, release notes and owner contact on Deployments — purely for humans and tooling to READ, never to filter on. What should you attach?
**Back:** annotations — informational metadata not meant for selecting objects<br><br>Annotations record non-identifying, informational metadata — build versions, release notes, owner/contact info, doc links, tool config. Labels would technically hold short strings too, but labels exist to be SELECTED on (Services, ReplicaSets, -l flags). Rule of thumb: if controllers need to filter on it → label; if humans/tools just need to read it → annotation.
**Tags:** k8s::cka src::session topic::annotations topic::labels

---

<!-- note:1794496839331 model:Basic -->
**Front:** Which statement about annotations is TRUE?
**Back:** they cannot be used in selectors — no -l flag or matchExpressions can filter on annotations<br><br>The annotation API has no selector mechanism: kubectl -l doesn't see them, spec.selector/matchExpressions ignore them, Services can't pick pods by them. They're write-and-read metadata only (get -o yaml / describe shows them). Also unlike labels they aren't size-constrained the same way — they can hold larger structured blobs (that's how last-applied fits a whole manifest).
**Tags:** k8s::cka src::session topic::annotations topic::api

---

<!-- note:1794496839332 model:Basic -->
**Front:** Which taint effect removes ALREADY-RUNNING pods from a node if they don't tolerate it?
**Back:** NoExecute<br><br>NoSchedule: no new pods without a matching toleration (existing pods stay). PreferNoSchedule: soft version — scheduler tries to avoid but no guarantee. NoExecute: evicts running pods that don't tolerate it (immediately, or after tolerationSeconds if set) AND blocks new ones.
**Tags:** k8s::cka src::session topic::scheduling topic::taints

---

<!-- note:1794496839333 model:Basic -->
**Front:** A pod tolerates node1's taint. Is it guaranteed to be scheduled on node1?
**Back:** no — a toleration only PERMITS placement; nodeAffinity/nodeSelector attracts pods to nodes<br><br>Tolerations are a pass, not a magnet: the scheduler may still place the pod on any node — tainted or untainted. Taints REPEL (set on nodes); affinity/nodeSelector ATTRACT (set on pods). For 'must run on node X' you combine them: taint the node to keep others out + nodeAffinity on the pod to pin it there.
**Tags:** k8s::cka src::session topic::scheduling topic::taints

---

<!-- note:1794496839334 model:Basic -->
**Front:** Why don't regular workload pods land on the control-plane node by default?
**Back:** the control-plane node carries a default taint (node-role.kubernetes.io/control-plane:NoSchedule) that user pods don't tolerate<br><br>kubeadm clusters taint control-plane nodes by default (node-role.kubernetes.io/control-plane:NoSchedule) so workloads stay off them — protection, not magic. DaemonSets and system pods carry matching tolerations. You CAN remove the taint (<code>kubectl taint nodes &lt;cp&gt; node-role.kubernetes.io/control-plane:NoSchedule-</code>) e.g. on single-node labs like minikube — it's just not done on real clusters.
**Tags:** k8s::cka src::session topic::architecture topic::taints

---

<!-- note:1794496839335 model:Basic -->
**Front:** Can spec.nodeSelector express 'run on nodes labelled size=large OR size=medium'?
**Back:** no — nodeSelector only does equality-AND on labels; OR/prefer logic needs nodeAffinity/nodeAntiAffinity<br><br>nodeSelector accepts only exact key=value pairs, ANDed together — you can't say 'large OR medium', 'not small', or 'prefer fast'. Node affinity adds expressive rules: the In operator (size In [large, medium]), NotIn, plus requiredDuringScheduling (hard) vs preferredDuringScheduling (soft) terms. Anti-affinity is the inverse — keep pods OFF matching nodes (or spread them).
**Tags:** k8s::cka src::session topic::nodeselector topic::scheduling

---

<!-- note:1794496839336 model:Basic -->
**Front:** A pod has spec.nodeSelector {size: large} but NO node carries that label. What happens?
**Back:** it stays Pending/unschedulable until a node with matching labels appears<br><br>nodeSelector is a HARD constraint — the scheduler won't place the pod anywhere else and won't retry-error; the pod just sits unscheduled. Events show '0/N nodes are available'. Fixes: label a node, relax the selector, or switch to nodeAffinity preferredDuringScheduling for a soft preference.
**Tags:** k8s::cka src::session topic::nodeselector topic::scheduling

---

<!-- note:1794496839337 model:Basic -->
**Front:** Recipe: pin a pod to SSD nodes using nodeSelector
**Back:** Two steps, in order: 1) LABEL the node — <code>kubectl label nodes node1 disktype=ssd</code>. 2) Add the selector in the pod spec — <code>spec.nodeSelector: {disktype: ssd}</code>. The nodeSelector never labels anything itself; it only matches labels nodes already carry. Labels on the node, selector on the pod.
**Tags:** k8s::cka src::session topic::nodeselector topic::scheduling

---

<!-- note:1794496839338 model:Basic -->
**Front:** Which node affinity type schedules the pod ANYWAY when no node satisfies the rule?
**Back:** preferredDuringSchedulingIgnoredDuringExecution<br><br>requiredDuringSchedulingIgnoredDuringExecution is the HARD type: no matching node = pod stays Pending (like nodeSelector but expressive). preferredDuringSchedulingIgnoredDuringExecution is SOFT: scheduler scores matching nodes higher using weight 1-100, but schedules anyway if none match. The 'IgnoredDuringExecution' suffix on BOTH means label changes after scheduling don't evict the pod.
**Tags:** k8s::cka src::session topic::affinity topic::scheduling

---

<!-- note:1794496839339 model:Basic -->
**Front:** A pod required a node label via nodeAffinity, gets scheduled, then the node's label is REMOVED. What does 'IgnoredDuringExecution' mean happens?
**Back:** nothing — node label changes after scheduling don't evict the pod<br><br>Affinity rules are evaluated only at SCHEDULING time. Once bound, the pod is immune to node-label changes: if the node loses its 'size=large' label later, the pod keeps running. (Contrast: NoExecute taints DO evict.) The never-implemented RequiredDuringExecution variant would have evicted — hence the verbose naming.
**Tags:** k8s::cka src::session topic::affinity topic::scheduling

---

<!-- note:1794496839340 model:Basic -->
**Front:** How are nodeSelectorTerms and the matchExpressions inside them logically combined?
**Back:** terms ORed, expressions ANDed — pod needs any ONE term fully satisfied<br><br>Two levels of logic inside requiredDuringScheduling...: the list nodeSelectorTerms[] is ORed (match ANY term); the matchExpressions[] inside ONE term are ANDed (ALL expressions in that term must match). Bonus: if both nodeSelector AND nodeAffinity are set on a pod, BOTH must be satisfied.
**Tags:** k8s::cka src::session topic::affinity topic::scheduling

---

<!-- note:1794496839341 model:Basic -->
**Front:** With nodeAffinity matchExpressions, how do you require a pod to avoid nodes labelled zone=east?
**Back:** operator: NotIn (or DoesNotExist for 'label absent' — anti-affinity behavior)<br><br>matchExpressions operators: In (value in list — this gives the OR nodeSelector lacks: size In [large, medium]), NotIn (value NOT in list), Exists (key present, any value), DoesNotExist (key absent), Gt/Lt (integer compare). NotIn and DoesNotExist are how you express node ANTI-affinity — keep pods off matching nodes.
**Tags:** k8s::cka src::session topic::affinity topic::scheduling

---

<!-- note:1794496839342 model:Basic -->
**Front:** In a container spec, what does <code>cpu: 250m</code> request?
**Back:** 0.25 of one CPU core<br><br>CPU is measured in cores: 1 = one full (v)CPU/hyperthread, and m = millicores (1/1000) — 250m = 0.25 core, 500m = half. Memory uses bytes with suffixes: Mi/Gi = mebibytes/gibibytes (2^20, 2^30 — binary), M/G = megabytes/gigabytes (10^6, 10^9 — decimal). Requests/limits accept either but Mi/Gi is the convention.
**Tags:** k8s::cka src::session topic::resources topic::scheduling

---

<!-- note:1794496839343 model:Basic -->
**Front:** Every node's allocatable CPU minus existing pods' requests is BELOW a new pod's request. What happens?
**Back:** stays Pending — scheduler sums requests already on each node against node allocatable; nowhere fits<br><br>The scheduler filters on REQUESTS (not limits, not actual usage): a node fits if allocatable − sum(existing pod requests) ≥ new pod's request. 4-CPU allocatable with 3.5 CPU already requested leaves 0.5 — a 1-CPU request fails the filter everywhere → pod Pending until capacity frees or a node is added. Limits don't factor into this math.
**Tags:** k8s::cka src::session topic::resources topic::scheduling

---

<!-- note:1794496839344 model:Basic -->
**Front:** A pod manifest sets NO resources, but its namespace has a LimitRange with defaults. What happens at creation?
**Back:** the LimitRange admission controller injects the namespace's default requests/limits<br><br>LimitRange does double duty in a namespace: it VALIDATES min/max bounds and supplies DEFAULTS. A pod omitting resources gets the LimitRange defaults patched in at admission time — so quota accounting works even for lazy manifests. If the defaults don't exist either, the pod gets no requests (scheduler treats it as ~0 → QoS BestEffort).
**Tags:** k8s::cka src::session topic::namespaces topic::resources

---

<!-- note:1794496839345 model:Basic -->
**Front:** A container declares <code>limits: {cpu: 250m}</code> and no requests. What's its effective cpu request?
**Back:** requests.cpu also becomes 250m — the request defaults to the limit<br><br>When a container sets a limit but no request, Kubernetes copies the limit value INTO the request. The reverse is not true: a request alone leaves the limit unset (container may burst beyond it). One-directional rule: limit → fills request; request → limit stays empty.
**Tags:** k8s::cka src::session topic::containers topic::resources

---

<!-- note:1794496839346 model:Basic -->
**Front:** What's a common sizing recommendation for Deployments?
**Back:** requests everywhere, limits carefully — lets pods burst into idle capacity instead of being throttled<br><br>A common recommendation: always set requests (scheduling + guarantees) but leave CPU limits off — a container over its limit gets THROTTLED even while the node sits idle, needlessly slowing bursts. Memory is different: it can't be throttled, only reclaimed by killing (OOMKilled), so memory limits still earn their place. Defaults: no request/no limit = BestEffort, evicted first under pressure.
**Tags:** k8s::cka src::session topic::containers topic::resources

---

<!-- note:1794496839347 model:Basic -->
**Front:** A namespace's ResourceQuota covers cpu. What does that force on new pods?
**Back:** every new pod must specify cpu (request or limit); pods without it are rejected<br><br>A ResourceQuota covering cpu or memory forces the issue: any new pod lacking a request OR limit for that resource gets rejected with 403 Forbidden at admission — there's nothing to charge the quota against. That's exactly why LimitRange pairs with ResourceQuota: LimitRange injects defaults so manifests still get accepted. Quota violations never affect already-running pods.
**Tags:** k8s::cka src::session topic::namespaces topic::resources

---

<!-- note:1794496839348 model:Basic -->
**Front:** How does a DaemonSet actually get its pods onto each node?
**Back:** the DaemonSet controller creates a pod per node with a nodeAffinity pinning it to that hostname; the default scheduler then binds it<br><br>DaemonSet pods do NOT bypass the scheduler: the controller creates one Pod per eligible node and injects nodeAffinity (matchFields metadata.name In [node]) — the DEFAULT scheduler then binds each pod to its node via spec.nodeName. You can point DS pods at a custom scheduler with spec.template.spec.schedulerName.
**Tags:** k8s::cka src::session topic::daemonsets topic::scheduling

---

<!-- note:1794496839349 model:Basic -->
**Front:** A cluster running a DaemonSet gets a NEW node. What happens?
**Back:** a pod lands on the new node automatically; pods on removed nodes are garbage-collected<br><br>The DaemonSet controller continuously reconciles: any node joining the cluster that matches the selector gets a pod; nodes leaving take their DS pods with them (garbage collection). That's the whole point vs a Deployment — replica count follows node count, not a fixed number.
**Tags:** k8s::cka src::session topic::daemonsets topic::scheduling

---

<!-- note:1794496839350 model:Basic -->
**Front:** Why do DaemonSet pods keep running on nodes that become NotReady or pressure-tainted?
**Back:** automatic tolerations — the controller adds not-ready/unreachable/pressure tolerations so DS pods survive node problems<br><br>The DaemonSet controller pre-adds tolerations: node.kubernetes.io/not-ready (NoExecute), unreachable (NoExecute), disk/memory/pid-pressure (NoSchedule) — so node agents keep running through failures (when they're needed MOST). To also land on control-plane nodes, the template must tolerate node-role.kubernetes.io/control-plane explicitly.
**Tags:** k8s::cka src::session topic::daemonsets topic::taints

---

<!-- note:1794496839351 model:Basic -->
**Front:** <code>kubectl get pods</code> shows 'static-web-my-node1' — you kubectl delete it and it instantly reappears. What is it and how do you actually remove it?
**Back:** it's a mirror of a static pod — the kubelet manages it from a manifest file on the node; delete the file, not the object<br><br>The kubelet creates a read-only MIRROR of each static pod in the API server (named &lt;pod&gt;-&lt;nodename&gt;) so kubectl visibility works. Deleting the mirror does nothing — kubelet's source of truth is the manifest file in staticPodPath (e.g. /etc/kubernetes/manifests). To change/kill the pod: edit or remove the file ON THE NODE.
**Tags:** k8s::cka src::session topic::pods topic::staticpods

---

<!-- note:1794496839352 model:Basic -->
**Front:** Which object kinds can a kubelet create from the static pod manifest directory?
**Back:** only Pods — kubelet understands no other kind; no Deployments, ReplicaSets or Services<br><br>Static manifests must be kind: Pod, apiVersion: v1 — nothing else exists without the API server. There's no controller to honor replicas, no scheduler (the pod lands on this node, period), no etcd. The kubelet alone watches the directory, creates the pod, and restarts it on failure — a one-node control loop.
**Tags:** k8s::cka src::session topic::kubelet topic::staticpods

---

<!-- note:1794496839354 model:Basic -->
**Front:** How does a pod say 'schedule me with my-scheduler, not the default'?
**Back:** spec.schedulerName must equal the scheduler's unique name<br><br>Each scheduler owns a unique name cluster-wide (the default is 'default-scheduler'). A pod opts in via spec.schedulerName: my-scheduler — unset means the default scheduler claims it. Two schedulers never fight over a pod: each only watches unbound pods bearing its own name.
**Tags:** k8s::cka src::session topic::pods topic::scheduling

---

<!-- note:1794496839355 model:Basic -->
**Front:** How can one kube-scheduler process act as several different schedulers?
**Back:** KubeSchedulerConfiguration profiles[] — one process, multiple profiles, each with its own schedulerName<br><br>Profiles let ONE kube-scheduler binary wear multiple hats: the config's profiles[] list gives each profile a distinct schedulerName + its own plugin config, and pods pick a profile via spec.schedulerName — but only a single scheduler process runs. Alternative: separate scheduler PROCESSES (e.g. a second kube-scheduler Deployment with its own config/name). Both patterns give 'multiple schedulers'.
**Tags:** k8s::cka src::session topic::api topic::scheduling

---

<!-- note:1794496839356 model:Basic -->
**Front:** What constraint applies to a scheduler's name in the cluster?
**Back:** unique per scheduler cluster-wide — it's the identity pods reference in spec.schedulerName<br><br>The schedulerName is how kube-scheduler instances/profile claim ownership of pods — collisions mean two processes racing to bind the same pods. The stock scheduler answers to 'default-scheduler'; your second scheduler (or profile) needs its own name like 'my-scheduler', set in KubeSchedulerConfiguration profiles[].schedulerName.
**Tags:** k8s::cka src::session topic::api topic::scheduling

---

<!-- note:1794496839357 model:Basic -->
**Front:** Can a cluster run more than one scheduler — and why would it?
**Back:** Yes — a cluster can run several schedulers side by side. Each has a unique name and only watches unbound pods whose <code>spec.schedulerName</code> matches it; pods default to 'default-scheduler'. Use cases: custom placement logic, batch/ML schedulers, testing new scheduling behavior. Deploy one as a Deployment running a second kube-scheduler binary with its own config.
**Tags:** k8s::cka src::session topic::architecture topic::scheduling

---

<!-- note:1794496839358 model:Basic -->
**Front:** How do you deploy a second scheduler (e.g. 'my-scheduler') into a cluster?
**Back:** The docs' recipe: 1) containerize kube-scheduler, 2) Deployment (kube-system, replicas:1) running <code>kube-scheduler --config=&lt;file&gt;</code>, 3) a ConfigMap holding a <code>KubeSchedulerConfiguration</code> with <code>profiles: [{schedulerName: my-scheduler}]</code> and <code>leaderElect: false</code>, 4) a ServiceAccount bound to <code>system:kube-scheduler</code> ClusterRole so it can watch/bind pods. Pods opt in via <code>spec.schedulerName: my-scheduler</code>.
**Tags:** k8s::cka src::session topic::scheduling topic::yaml

---

<!-- note:1794496839359 model:Basic -->
**Front:** Which scheduling step eliminates nodes that CAN'T run the pod (resources, taints, selectors)?
**Back:** Filter — every plugin marks each node feasible or infeasible; survivors move on<br><br>Filter plugins eliminate nodes that CANNOT run the pod: insufficient resources vs requests, taints without tolerations, nodeSelector/affinity mismatch, port conflicts. Each node is evaluated until one plugin rejects it (short-circuit); anything surviving is 'feasible'. If zero nodes pass → PostFilter kicks in (preemption: evict lower-priority pods to make room) or the pod stays Pending.
**Tags:** k8s::cka src::session topic::pods topic::scheduling

---

<!-- note:1794496839360 model:Basic -->
**Front:** Filtering left 5 feasible nodes. How does the scheduler pick ONE?
**Back:** Score plugins rank the feasible nodes (weighted scores); highest wins, ties broken randomly<br><br>After filtering leaves multiple feasible nodes, each Score plugin (e.g. NodeResourcesFit, ImageLocality) assigns every node a number; NormalizeScore scales them, weights combine them into a total per node. The pod binds to the highest total — equal scores → random choice. This is the 'prefer' side of scheduling: all surviving nodes CAN run it, scoring picks the best.
**Tags:** k8s::cka src::session topic::pods topic::scheduling

---

<!-- note:1794496839361 model:Basic -->
**Front:** How does the scheduler order pods waiting in its internal scheduling queue?
**Back:** by pod priority — the QueueSort plugin (default PrioritySort) orders the queue, high-priority pods first<br><br>Before anything else, pods wait in the scheduler's internal queue. The QueueSort extension point decides order — only ONE QueueSort plugin may be enabled — and the default, PrioritySort, sorts by pod priority so important workloads get scheduled first. That's why PriorityClass exists: it moves pods up the queue AND drives preemption.
**Tags:** k8s::cka src::session topic::pods topic::scheduling

---

<!-- note:1794496839362 model:Basic -->
**Front:** Why did Kubernetes add scheduling PROFILES instead of just recommending multiple scheduler deployments?
**Back:** separate scheduler processes can race each other on the same node; profiles give one process multiple configured personalities<br><br>Multiple scheduler PROCESSES each see only their own queue and can pick the same node concurrently — the loser discovers the conflict at bind time (retry, wasted work). Profiles (stable since v1.19) let ONE kube-scheduler expose several schedulerNames, each with its own plugin config — variety without a second process and without the race window.
**Tags:** k8s::cka src::session topic::api topic::scheduling

---

<!-- note:1794496839363 model:Basic -->
**Front:** What does the taint effect "NoExecute" indicate in Kubernetes?
**Back:** Pods will be evicted immediately from the node, if they do not tolerate the taint<br><br>NoExecute is the aggressive effect: it evicts running pods that don't tolerate the taint AND blocks new ones. (Pods that DO tolerate without tolerationSeconds stay forever; with tolerationSeconds they survive only that long.) The course's other options map to the remaining effects: 'pods will not be scheduled' = NoSchedule; 'try to avoid, not guaranteed' = PreferNoSchedule.
**Tags:** k8s::cka src::session topic::scheduling topic::taints

---

<!-- note:1794496839364 model:Basic -->
**Front:** What does the TYPE of node affinity in Kubernetes define?
**Back:** the scheduler's behavior regarding the rule at scheduling time AND during the pod's execution<br><br>The type name literally spells out behavior at two lifecycle stages: 'required/preferred' + 'DuringScheduling' = hard rule (pod won't place without a match) vs soft preference (schedules anyway); 'IgnoredDuringExecution' = after the pod runs, node-label changes are ignored — no eviction. The unimplemented 'requiredDuringExecution' would have evicted on label changes.
**Tags:** k8s::cka src::session topic::affinity topic::scheduling

---

<!-- note:1794496839383 model:Basic -->
**Front:** The purpose of the Readiness probe is to:
**Back:** decide if Pod receives Service traffic<br><br>Readiness gates traffic; liveness restarts. A failing readiness probe removes the Pod from Service endpoints so no traffic is routed to it — the container keeps running and is NOT restarted (that's the liveness probe's job). Encryption is TLS/mesh; CPU reservation is resource requests — neither involves probes.
**Tags:** k8s::cka src::session topic::probes topic::services

---

<!-- note:1794496839385 model:Basic -->
**Front:** The correct nodeSelector format is:
**Back:** nodeSelector: { disk: ssd }<br><br>nodeSelector is a key/value map, not a query string: under spec.nodeSelector you write YAML labels as key: value pairs — <code>nodeSelector: { disk: ssd }</code> (or block form with each pair on its own line) pins the pod to nodes carrying disk=ssd, with ALL pairs required (AND). The 'disk=ssd' expression style is kubectl's -l/<code>--selector</code> flag syntax (e.g. <code>kubectl get pods -l disk=ssd</code>), NOT pod-spec field syntax — a common mix-up. nodeSelector only does equality; for operators like In/NotIn use nodeAffinity matchExpressions.
**Tags:** k8s::cka src::session topic::nodeselector topic::scheduling topic::yaml

---

<!-- note:1794496839386 model:Basic -->
**Front:** Probe relationship: which starts first?
**Back:** startup first; while failing, readiness/liveness is suppressed; after success, readiness/liveness is independent<br><br>The startup probe exists for slow-booting apps: while it keeps failing, BOTH liveness and readiness are disabled — so a container that takes 5 minutes to start isn't killed by liveness or kept out of rotation complaints. Once startup succeeds it never runs again, and liveness + readiness take over independently: readiness can fail (pull from Service endpoints) while liveness stays green, and vice versa. There's no strict startup→readiness→liveness pipeline — readiness and liveness are peers, not stages.
**Tags:** k8s::cka src::session topic::pods topic::probes

---

<!-- note:1794496839391 model:Basic -->
**Front:** Pod Security Standards levels, ordered least → most restrictive:
**Back:** Privileged → Baseline → Restricted<br><br>Least → most restrictive: Privileged → Baseline → Restricted. The levels are cumulative — Restricted includes ALL Baseline rules plus hardened requirements (runAsNonRoot, drop ALL capabilities, seccomp profile, no privilege escalation). Privileged is unrestricted (the effective default for unlabeled namespaces). Baseline blocks only the obviously dangerous: privileged containers, host namespaces/PID/IPC, hostPath volumes, host ports, dangerous capabilities. Restricted enforces current pod-hardening best practices. Enforcement is via namespace labels like pod-security.kubernetes.io/enforce=restricted, with audit and warn modes for rollout — Pod Security Admission replaced the deprecated PodSecurityPolicy.
**Tags:** k8s::cka src::session topic::pods topic::podsecurity topic::security

---

<!-- note:1794496839399 model:Basic -->
**Front:** Which apiVersion serves Deployment objects in modern Kubernetes?
**Back:** apps/v1<br><br>apps/v1 serves Deployments, ReplicaSets, DaemonSets, StatefulSets and ControllerRevisions. extensions/v1beta1 was their ORIGINAL home but was emptied and removed — Ingresses moved to networking.k8s.io/v1, workloads to apps/v1. batch/v1 = Jobs + CronJobs. This is exactly why named groups exist: related resources version and evolve together, and new features land in named groups instead of churning the stable core API.
**Tags:** k8s::cka src::session topic::api topic::workloads

---

<!-- note:1794496839405 model:Basic -->
**Front:** Where do we specify the pod labels in a Kubernetes network policy definition file?
**Back:** spec.podSelector<br><br>spec.podSelector selects WHICH pods the policy applies to — the labels themselves go under spec.podSelector.matchLabels (or matchExpressions for operators). An empty podSelector: {} selects ALL pods in the policy's namespace. spec.ingress and spec.egress are the traffic RULE lists (from/to peers + ports), not selectors — spec.matchLabels isn't a NetworkPolicy field at all (that's the style used inside podSelector and in workload selectors like a Deployment's spec.selector.matchLabels).
**Tags:** k8s::cka src::session topic::networking topic::networkpolicy topic::yaml

---

<!-- note:1794496839407 model:Basic -->
**Front:** What statement/s is/are true about the service account of an existing pod in Kubernetes?
**Back:** the service account is set when the pod is created and cannot be changed afterwards<br><br>spec.serviceAccountName is immutable after pod creation — same pattern as spec.nodeName: it's fixed at admission and the API server rejects kubectl edit/patch/apply attempts on a live pod (that's why A, B and D all fail — D would work for a NEW pod via the definition file, but applying it to an existing pod errors on the immutable field). To change a pod's SA you must delete and recreate it — for Deployments that's updating the pod template and letting the rollout create new pods. Note the distinction: you CAN change what an SA is allowed to do (edit its RBAC bindings) — that changes permissions of the identity, not which identity the pod uses. The mounted token is also projected at creation, so the pod's credential can't be swapped in place either.
**Tags:** k8s::cka src::session topic::pods topic::security topic::serviceaccounts

---

<!-- note:1794496839412 model:Basic -->
**Front:** How can we specify the secret to our private registry inside our pod definition file?
**Back:** specifying the secret under the imagePullSecrets section in the pod definition file<br><br>spec.imagePullSecrets is the pod-spec field that tells the kubelet which Secret to use when pulling images from a private registry: spec.imagePullSecrets: [{name: regcred}] where regcred is a Secret of type kubernetes.io/dockerconfigjson holding .dockerconfigjson auth (created via kubectl create secret docker-registry). It works at PULL time — before the container starts — so env vars (runtime only) and annotations (metadata, not pull logic) can't do it, and there's no kubectl flag that attaches pull secrets to a pod. You can also set imagePullSecrets on a ServiceAccount so every pod using that SA inherits them. Older kubernetes.io/dockercfg secrets work too.
**Tags:** k8s::cka src::session topic::pods topic::secrets

---

<!-- note:1794496839414 model:Basic -->
**Front:** Which of the following statements is true regarding service accounts in Kubernetes version 1.24?<br><br>A. When a service account is created, it only creates a token access secret but not a regular secret.<br>B. When a service account is created, it only creates a secret but not a token access secret.<br>C. When a service account is created, it no longer automatically creates a secret or a token access secret.<br>D. When a service account is created, it automatically creates a secret and a token access secret.
**Back:** C – when a service account is created, it no longer automatically creates a secret or a token access secret<br><br>Since Kubernetes 1.24 (KEP-2799), creating a ServiceAccount creates ONLY the SA object — no Secret is auto-generated. Before 1.24, kubectl create sa / a pod referencing an SA triggered creation of a kubernetes.io/service-account-token Secret holding a never-expiring JWT mounted into pods. That mechanism was removed because those tokens never expired and couldn't be rotated — pods now get short-lived, audience/time/object-bound tokens via the TokenRequest API and projected serviceAccountToken volumes instead. Legacy auto-created Secrets that already exist are NOT deleted, but they aren't refreshed either — migration path is to delete them and switch workloads to projected tokens.
**Tags:** k8s::cka src::session topic::secrets topic::security topic::serviceaccounts

---

<!-- note:1794496839417 model:Basic -->
**Front:** What is the relationship between the secret object and the service account in Kubernetes?
**Back:** the secret object is linked to the service account and stores the service account token<br><br>LEGACY model (pre-1.24, and still true for manually created token secrets): an SA's token lived in a Secret of type kubernetes.io/service-account-token — the Secret was linked to the SA (via annotation kubernetes.io/service-account.name) and stored its JWT, which pods mounted at /var/run/secrets/kubernetes.io/serviceaccount/. The Secret doesn't authenticate the SA — the SA IS the identity, the token just proves it; and the SA doesn't store the API endpoint (that's kubeconfig's job). MODERN model (1.24+): NO Secret is created — pods get short-lived audience/time/object-bound tokens via the TokenRequest API in a projected volume. That's why YOUR cluster lists SAs but no matching secrets: kubectl get secrets shows nothing of type service-account-token on a post-1.24 cluster.
**Tags:** k8s::cka src::session topic::secrets topic::security topic::serviceaccounts

---

<!-- note:1794496839432 model:Basic -->
**Front:** What does resourceNames do in a Role rule?
**Back:** it restricts the rule to specific named resource instances<br><br>resourceNames narrows a rule from 'all pods' to named instances: resources: [configmaps], resourceNames: [my-configmap], verbs: [get, update] lets the subject touch ONLY that one ConfigMap. Hard limits (doc-verified): you CANNOT restrict top-level create (the name doesn't exist at authz time) or deletecollection by resourceName; list/watch restricted by resourceName require the client to send a matching field-selector (kubectl get configmaps --field-selector=metadata.name=my-configmap); it DOES work on subresources like pods/exec. An empty resourceNames list means everything is allowed.
**Tags:** k8s::cka src::session topic::rbac topic::security topic::yaml

---

<!-- note:1794496839446 model:Basic -->
**Front:** What does kubectl create token build-robot do?
**Back:** It calls the TokenRequest API, prints a JWT to stdout, and stores nothing in the cluster<br><br>kubectl create token NAME performs a TokenRequest for that SA and prints the signed JWT — nothing is persisted. Default lifetime is server-decided (~1h); --duration requests a lifetime but the server may return shorter OR longer. --audience sets the intended recipient (default: the API server). --bound-object-kind/name/uid (Pod/Secret/Node kinds) binds the token to an object — it dies when that object or the SA is deleted. Feature is Stable since v1.33.
**Tags:** k8s::cka src::session topic::authentication topic::kubectl topic::rbac

---

<!-- note:1794496839447 model:Basic -->
**Front:** Can you get a ServiceAccount token that stays valid as long as the SA exists?
**Back:** Yes — create a Secret of type kubernetes.io/service-account-token annotated kubernetes.io/service-account.name: <sa><br><br>The manual legacy path still works: kubectl apply a Secret with annotation kubernetes.io/service-account.name: build-robot and type kubernetes.io/service-account-token — the control plane generates a token into .data.token that stays valid until the SA is deleted (auto-cleaned). Pre-1.24 this happened automatically for every SA; now it's opt-in. Docs recommend TokenRequest instead — never-expiring tokens are what 1.24 moved away from. Caution: never display the token field where screens can be seen.
**Tags:** k8s::cka src::session topic::rbac topic::secrets topic::security

---

<!-- note:1794496839456 model:Basic -->
**Front:** What Secret type stores container-registry credentials for image pulls?
**Back:** kubernetes.io/dockerconfigjson — a Secret holding a .dockerconfigjson key with the registry auths<br><br>Registry credentials live in a Secret of type kubernetes.io/dockerconfigjson. Its data key .dockerconfigjson holds a base64'd docker config.json: {"auths":{"registry.example.com":{"username":..,"password":..,"auth":"base64(user:pass)"}}}. The legacy type kubernetes.io/dockercfg used the older ~/.dockercfg format — prefer dockerconfigjson. The kubelet reads this Secret at image-pull time and authenticates to the matching registry.
**Tags:** k8s::cka src::session topic::images topic::secrets topic::security

---

<!-- note:1794496839457 model:Basic -->
**Front:** How does a Pod authenticate to a private image registry?
**Back:** Create the dockerconfigjson Secret in the pod's namespace, then reference it in spec.imagePullSecrets — the kubelet uses it at pull time<br><br>End-to-end: (1) kubectl create secret docker-registry regcred ... in the SAME namespace as the pod — namespace mismatch is the #1 failure; (2) pod spec gets imagePullSecrets: [{name: regcred}]; (3) kubelet pulls the image using those creds before the container starts. If the Secret is missing the pod sits in ImagePullBackOff and kubectl describe pod shows FailedToRetrieveImagePullSecret. The Secret can also live on a ServiceAccount so all its pods inherit it.
**Tags:** k8s::cka src::session topic::images topic::pods topic::secrets

---

<!-- note:1794496839459 model:Basic -->
**Front:** What is securityContext and why does it exist?
**Back:** Privilege and access-control settings for a Pod or Container — UID/GID, capabilities, seccomp, AppArmor, SELinux, read-only rootfs<br><br>securityContext defines privilege and access control for pods/containers: runAsUser/runAsGroup (UID/GID), capabilities (Linux privileges), privileged mode, allowPrivilegeEscalation (blocks setuid gains), readOnlyRootFilesystem, seccompProfile, appArmorProfile, seLinuxOptions. It exists because containers share the host kernel — isolation is weaker than a VM, so these settings are the per-workload hardening layer that Pod Security Standards then enforce cluster-wide.
**Tags:** k8s::cka src::session topic::pods topic::podsecurity topic::security

---

<!-- note:1794496839460 model:Basic -->
**Front:** Where do pod-level and container-level securityContext fields live in the spec?
**Back:** spec.securityContext = PodSecurityContext for ALL containers (+ volumes); spec.containers[].securityContext = SecurityContext for ONE container<br><br>Two different objects at two levels: spec.securityContext is a PodSecurityContext applying to every container in the pod (and volumes — fsGroup controls volume ownership); spec.containers[].securityContext is a SecurityContext applying to just that one container. The Pod object is the broader default; the container object is the per-workload override.
**Tags:** k8s::cka src::session topic::podsecurity topic::security topic::yaml

---

<!-- note:1794496839461 model:Basic -->
**Front:** A Pod sets spec.securityContext.runAsUser: 1000 but its container sets securityContext.runAsUser: 2000. What UID does the process run as?
**Back:** The container runs as UID 2000 — container-level securityContext overrides pod-level on overlap<br><br>Doc example: pod sets securityContext.runAsUser: 1000 but the container sets securityContext.runAsUser: 2000 → the process runs as 2000. Container settings override pod settings wherever they overlap; pod settings are the defaults for everything not overridden. One asymmetry: container settings do NOT affect the pod's volumes — fsGroup and friends only exist at pod level.
**Tags:** k8s::cka src::session topic::podsecurity topic::security

---

<!-- note:1794496839462 model:Basic -->
**Front:** What does allowPrivilegeEscalation: false do, and what is its default?
**Back:** It defaults to true; setting false blocks setuid-based privilege gains and is incompatible with privileged:true or CAP_SYS_ADMIN<br><br>allowPrivilegeEscalation controls whether a process can gain MORE privileges than its parent — e.g. by executing a setuid binary. It maps to the kernel's no_new_privs flag (inverted: allowPrivilegeEscalation: false sets no_new_privs). If undefined it DEFAULTS TO TRUE — so you must opt out explicitly. It's inconsistent with privileged: true or CAP_SYS_ADMIN and can't be combined with them. This is the field Pod Security Standards 'restricted' requires.
**Tags:** k8s::cka src::session topic::pods topic::podsecurity topic::security

---

<!-- note:1794496839463 model:Basic -->
**Front:** How do you apply least privilege with Linux capabilities in a container securityContext?
**Back:** capabilities.drop: ["ALL"] then add back only what's needed — least privilege; privileged:true grants everything<br><br>Linux capabilities are the granular privileges root normally holds (NET_ADMIN, SYS_ADMIN, DAC_OVERRIDE…). Hardened containers drop ALL capabilities then add back only required ones: securityContext.capabilities.drop: ["ALL"], add: ["NET_BIND_SERVICE"]. privileged: true is the nuclear option — ALL capabilities plus host device access — required for things like CNI plugins but a massive risk in multi-tenant clusters; Pod Security Standards 'baseline' forbids it.
**Tags:** k8s::cka src::session topic::pods topic::podsecurity topic::security

---

<!-- note:1794496839464 model:Basic -->
**Front:** What do ingress and egress mean for a Pod's network traffic?
**Back:** Ingress = traffic INTO the pod; egress = traffic OUT of the pod — each direction is isolated independently<br><br>Ingress is inbound traffic to a pod (who may connect to it); egress is outbound traffic from a pod (where it may connect to). Isolation is declared per-direction and independently: a pod can be isolated for ingress while fully open for egress, or vice versa. 'Isolated' doesn't mean blocked — it means only explicitly allowed connections pass; 'non-isolated' means no restrictions. By default pods are non-isolated BOTH ways — the flat pod network lets any pod reach any pod or namespace.
**Tags:** k8s::cka src::session topic::networking topic::networkpolicy

---

<!-- note:1794496839467 model:Basic -->
**Front:** What are the selector types you can use in a NetworkPolicy's ingress.from / egress.to?
**Back:** podSelector (pods in same namespace), namespaceSelector (whole namespaces), ipBlock (external CIDR ranges)<br><br>from/to entries accept three selector types: podSelector picks pods in the policy's OWN namespace by labels; namespaceSelector picks entire namespaces by labels (all their pods); ipBlock picks cluster-external CIDR ranges — pod IPs are ephemeral so ipBlock is for outside-the-cluster sources like load balancers. A single entry can combine namespaceSelector + podSelector to mean 'these labeled pods within these labeled namespaces'. kubectl describe shows how the CNI actually interpreted the policy.
**Tags:** k8s::cka src::session topic::labels topic::networking topic::networkpolicy

---

<!-- note:1794496839468 model:Basic -->
**Front:** namespaceSelector + podSelector in ONE map vs as separate list items — what's the difference?
**Back:** One map with both selectors = AND (labeled pods inside labeled namespaces); two separate list items = OR<br><br>The classic YAML gotcha: namespaceSelector and podSelector in the SAME map element are ANDed — 'pods labeled role=client in namespaces labeled user=alice'. As SEPARATE elements of the from/to list they're ORed — 'pods labeled role=client in ANY namespace, OR any pod in namespaces labeled user=alice'. Same labels, wildly different policy. When in doubt: kubectl describe networkpolicy shows the CNI's interpretation.
**Tags:** k8s::cka src::session topic::networking topic::networkpolicy topic::yaml

---

<!-- note:1794496839482 model:Basic -->
**Front:** A pod is in 'Pending' state for a long time. Which is the most likely cause?
**Back:** No node has enough CPU or memory to meet the pod's requests<br><br>Pending means the pod never got SCHEDULED — it exists in the API but no kube-scheduler bound it to a node, almost always because every node's allocatable CPU/memory minus existing requests can't fit this pod's requests. The distractors all fail at a LATER stage: a failing liveness probe crashes a RUNNING container (restarts, not Pending); a missing image fails in ContainerCreating (ErrImagePull/ImagePullBackOff); a missing readiness probe doesn't block scheduling. Triage rule: Pending = scheduling problem; check 'kubectl describe pod' events for 'Insufficient cpu/memory'.
**Tags:** k8s::cka src::session topic::pods topic::resources topic::scheduling

---

<!-- note:1794496839486 model:Basic -->
**Front:** When a Pod is scheduled, what is <b>the primary factor</b> the kubescheduler considers from the Pod’s specification?
**Back:** Resource requests and limits<br><br>The kube-scheduler filters nodes based on whether they<br>can satisfy the Pod’s resource requests (CPU, memory) and then ranks<br>them based on various priority functions.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839488 model:Basic -->
**Front:** What is the main advantage of using a declarative approach (e.g., YAML manifests) to manage Kubernetes resources?
**Back:** It focuses on what desired state, not how to achieve it<br><br>Declarative configurations define the desired state, and<br>Kubernetes controllers work to reconcile the current state to this desired<br>state. This is more robust and idempotent than imperative commands.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839492 model:Basic -->
**Front:** What does a ReplicaSet ensure in Kubernetes?
**Back:** That a certain number of Pod replicas are running<br><br>A ReplicaSet’s primary purpose is to maintain a stable set<br>of replica Pods running at any given time, ensuring the desired number of<br>instances of an application are available. Deployments manage ReplicaSets.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839494 model:Basic -->
**Front:** If you need to run a batch job that completes and then terminates, which Kubernetes workload resource is most suitable?
**Back:** Job<br><br>Explanation: A Job creates one or more Pods and ensures that a specified number of them successfully terminate. It’s ideal for batch tasks,<br>while CronJob is for scheduled Jobs.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839495 model:Basic -->
**Front:** What is a key difference between kubectl apply -f and kubectl create -f ?
**Back:** apply stores last-applied-configuration, create does not<br><br>kubectl apply records the applied configuration in an annotation on the resource. This allows it to calculate a patch between the<br>previous, current, and new desired state, making it suitable for declarative<br>updates. create will fail if the resource exists.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839497 model:Basic -->
**Front:** What core benefit does a StatefulSet provide over a Deployment for applications like databases?
**Back:** Stable, unique network identifiers and persistent storage<br><br>StatefulSets are designed for stateful applications, providing stable, persistent identifiers (e.g., my-app-0, my-app-1) and perinstance persistent storage that follows the Pod identity.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839499 model:Basic -->
**Front:** What Kubernetes feature allows you to define constraints on which Nodes your Pods can run, based on Node labels?
**Back:** nodeSelector / nodeAffinity<br><br>nodeSelector provides a simple way to constrain Pods to<br>Nodes with specific labels. nodeAffinity offers more expressive rules, including ”preferred” and ”required” constraints.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839502 model:Basic -->
**Front:** How can you securely store sensitive information like <b>passwords</b> or <b>API keys</b> in Kubernetes?
**Back:** Secret<br><br>Secrets are Kubernetes objects specifically designed to hold small amounts of sensitive data.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839506 model:Basic -->
**Front:** Which Kubernetes resource is typically used to manage stateless applications by ensuring a specified number of Pod replicas are running?
**Back:** Deployment<br><br>Deployments manage ReplicaSets, providing declarative updates and scaling for stateless applications.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839507 model:Basic -->
**Front:** In Kubernetes, what is the process of assigning Pods to Nodes called?
**Back:** Scheduling<br><br>Scheduling is the core function of the kube-scheduler, selecting appropriate Nodes for Pods based on resource requests and other factors.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839509 model:Basic -->
**Front:** How can you securely store sensitive information like passwords or API keys in Kubernetes?
**Back:** Secret<br><br>Secrets are Kubernetes objects specifically designed to hold small amounts of sensitive data.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839513 model:Basic -->
**Front:** If you need a Pod to run on every single Node in the cluster (or a subset), which controller is most suitable?
**Back:** DaemonSet<br><br>DaemonSets ensure that all (or some) Nodes run a copy of a Pod, useful for cluster services like log collectors or node monitors.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839514 model:Basic -->
**Front:** What is a primary difference between a Deployment and a StatefulSet?
**Back:** StatefulSets provide stable IDs<br><br>StatefulSets provide guarantees about the ordering and uniqueness of Pods, including stable network identifiers and persistent storage.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839516 model:Basic -->
**Front:** What design pattern involves running an additional container within a Pod to provide auxiliary functions (like logging or monitoring) to the main application container?
**Back:** Sidecar Container<br><br>The Sidecar pattern adds helper containers alongside the main application container within the same Pod network/storage namespace.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839517 model:Basic -->
**Front:** What <b>fundamental concept</b> allows Kubernetes to maintain the desired state declared by the user?
**Back:** Control Loop / Reconciliation<br><br>Kubernetes controllers operate on control loops, constantly comparing the desired state (from API objects) with the actual cluster state.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839519 model:Basic -->
**Front:** A Pod specification includes two containers: one web server and one log shipper. How do these containers communicate efficiently over the network within the Pod?
**Back:** Via localhost and shared network namespace<br><br>Containers within the same Pod share the same network namespace, meaning they can communicate using localhost and standard inter-process communication mechanisms as if they were on the same machine.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839523 model:Basic -->
**Front:** What core Kubernetes concept allows Deployments to perform rolling updates with zero downtime?
**Back:** Incrementally replacing Pods managed by ReplicaSets<br><br>Deployments manage ReplicaSets. During a rolling update, a Deployment creates a new ReplicaSet with the updated Pod template and gradually scales it up while scaling down the old ReplicaSet, ensuring service availability throughout the process.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839524 model:Basic -->
**Front:** Which component is responsible for making the ultimate decision about which node a newly created Pod should run on?
**Back:** kube-scheduler<br><br>The kube-scheduler watches for Pods without an assigned node and selects the most suitable node based on filtering (resource requests, affinity rules, etc.) and scoring algorithms.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839525 model:Basic -->
**Front:** How does Kubernetes typically handle the failure of a container within a Pod?
**Back:** By restarting the failed container based on the Pod’s restartPolicy<br><br>The kubelet monitors container health. If a container fails, the kubelet restarts it according to the Pod’s restartPolicy (Always, OnFailure, Never). The Pod itself continues to exist on the same node.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839526 model:Basic -->
**Front:** What distinguishes a Kubernetes Secret from a ConfigMap?
**Back:** ConfigMaps store configuration data, Secrets store sensitive data (base64 encoded)<br><br>Both are used for configuration, but Secrets are intended for sensitive information (passwords, keys) and are stored base64 encoded (not truly encrypted by default in etcd, though). ConfigMaps are for nonsensitive configuration data. Both are namespaced and can be mounted in multiple ways.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839528 model:Basic -->
**Front:** What is the purpose of labels in Kubernetes?
**Back:** To attach identifying metadata for selection and organization<br><br>Labels are key/value pairs attached to objects (like Pods, Services) used to organize resources and allow users/controllers to select subsets of objects (e.g., a Service selecting Pods with app=backend).
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839529 model:Basic -->
**Front:** If a Pod needs access to specific hardware features available only on certain nodes, which scheduling mechanism is most suitable?
**Back:** Taints and Tolerations or Node Affinity<br><br>Taints applied to nodes repel Pods that don’t Tolerate them. Node Affinity allows Pods to express preferences or requirements for nodes based on node labels (which can represent hardware features, location, etc.). Both help ensure Pods land on appropriate nodes.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839531 model:Basic -->
**Front:** What is the relationship between a Deployment and a ReplicaSet?
**Back:** A Deployment declaratively manages ReplicaSets to orchestrate Pod updates<br><br>A Deployment provides declarative updates for Pods and ReplicaSets. It creates and manages ReplicaSets, handling rolling updates or rollbacks by manipulating the desired replica count of underlying ReplicaSets. You typically interact with Deployments, not ReplicaSets directly.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839534 model:Basic -->
**Front:** Which field in a Pod’s specification is crucial for the kubescheduler to determine if a node has sufficient resources?
**Back:** spec.containers[].resources.requests<br><br>The resources.requests field (for CPU and memory) indicates the minimum amount of resources the container needs. The scheduler uses this to filter out nodes that cannot meet these requests.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839535 model:Basic -->
**Front:** What fundamental concept allows Kubernetes controllers to operate effectively without needing constant instructions?
**Back:** The reconciliation loop (Control Loop)<br><br>Controllers continuously watch the desired state (from the API server) and the current state (observed in the cluster), taking actions (via the API server) to make the current state match the desired state. This is the core principle of Kubernetes automation.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839536 model:Basic -->
**Front:** You need to provide non-sensitive configuration data (like a URL endpoint or logging level) to a Pod. Which resource is most appropriate?
**Back:** ConfigMap<br><br>ConfigMaps are designed specifically for decoupling nonsensitive configuration artifacts from container images, allowing configurations to be managed independently.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839537 model:Basic -->
**Front:** If you want a specific Pod to run on every node in the cluster (or a subset matching certain criteria), which workload resource should you use?
**Back:** DaemonSet<br><br>A DaemonSet ensures that a copy of a Pod runs on all (or some specified) nodes. This is useful for node-level agents like log collectors, monitoring agents, or CNI plugins.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839538 model:Basic -->
**Front:** What does it mean for the Kubernetes API to be ”declarative”?
**Back:** Users specify the desired end state, not the steps to reach it<br><br>Users declare the desired state of resources (e.g., ”I want 3 replicas of this Pod”). Kubernetes controllers then figure out the sequence of actions needed to achieve and maintain that state. Contrast this with imperative approaches (”run container X”, ”scale up by 1”).
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839539 model:Basic -->
**Front:** Which mechanism prevents the kube-scheduler from placing Pods on a Node that is undergoing maintenance or is otherwise unsuitable?
**Back:** Taints on the Node and Tolerations on the Pod<br><br>Explanation: A Taint applied to a Node repels Pods. Pods can express Tolerations for specific taints, allowing them to be scheduled onto those nodes. This is commonly used to cordon nodes for maintenance or dedicate nodes for specific workloads.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839542 model:Basic -->
**Front:** A <b>StatefulSet </b>is often preferred over a <b>Deployment </b>for running databases. Why?
**Back:** StatefulSets provide stable, unique network IDs and persistent storage per Pod<br><br>StatefulSets provide guarantees crucial for stateful apps: stable network identifiers (e.g., db-0, db-1), stable persistent storage linked to each identity, and ordered, graceful deployment and scaling.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839543 model:Basic -->
**Front:** Which kubectl command is used to view the logs of a running container within a Pod?
**Back:** kubectl logs &lt;pod-name&gt; [-c &lt;container-name&gt;]<br><br>kubectl logs fetches the logs (stdout/stderr) from a specified container within a Pod. The -c flag is needed if the Pod has multiple containers.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839546 model:Basic -->
**Front:** Consider a Pod that needs to perform a <b>one-time initialization task</b> before its main application container starts. Which container type is best suited for this?
**Back:** Init Container<br><br>Init Containers run sequentially before the main application containers in a Pod start. They must complete successfully for the main containers to launch, making them ideal for setup tasks like database schema migration, fetching configuration, or waiting for dependencies.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839547 model:Basic -->
**Front:** What is the purpose of the metadata.ownerReferences field in a Kubernetes object?
**Back:** To link the object to its managing controller (e.g., ReplicaSet to Deployment)<br><br>ownerReferences create parent-child relationships between objects. This enables cascading deletion (deleting the owner deletes dependents) and helps controllers identify the objects they manage. For example, a ReplicaSet Pod will have an ownerReference pointing to the ReplicaSet.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839549 model:Basic -->
**Front:** What is the purpose of a LimitRange object within a Namespace?
**Back:** To set default resource requests/limits for containers and validate min/max bounds<br><br>A LimitRange operates at the container/Pod level within a Namespace. It can enforce minimum/maximum resource constraints and specify default request/limit values if they aren’t explicitly set in the Pod spec. ResourceQuota limits the Namespace total.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839550 model:Basic -->
**Front:** Which kubectl command would you use to apply a configuration defined in my-app.yaml declaratively?
**Back:** kubectl apply -f my-app.yaml<br><br>kubectl apply is the standard command for declarative resource management. It creates resources if they don’t exist or calculates and applies necessary changes if they do, based on the definition in the file.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839551 model:Basic -->
**Front:** How does the kube-scheduler handle Pods with defined affinity rules?
**Back:** It considers affinity/anti-affinity rules during the filtering and scoring phases.<br><br>Affinity rules (node and inter-pod) influence scheduling decisions. Required affinity rules act as filters (nodes must match). Preferred affinity rules contribute to the scoring phase (nodes matching preferred rules get higher scores).
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839552 model:Basic -->
**Front:** Which of the following is a built-in Kubernetes resource for scheduling pods on nodes?<br><br>A. Deployment<br>B. Ingress<br>C. Service<br>D. DaemonSet
**Back:** D – DaemonSet<br><br>A DaemonSet ensures that a copy of a Pod runs on all (or selected) nodes in the cluster, commonly used for system-level workloads like logging or monitoring agents.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839557 model:Basic -->
**Front:** What is the primary advantage of using containers in application deployment?
**Back:** Isolation of applications and dependencies<br><br>Containers package applications with their dependencies, ensuring isolation and consistency across environments.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839558 model:Basic -->
**Front:** Which component determines which nodes can run a pod?
**Back:** Kube-scheduler<br><br>The kube-scheduler selects the most suitable node for a Pod based on scheduling policies and constraints.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839559 model:Basic -->
**Front:** What role does a node’s taint play in scheduling?
**Back:** Allows pods with matching tolerations<br><br>Taints repel Pods unless they have matching tolerations, controlling which Pods can be scheduled on a node.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839561 model:Basic -->
**Front:** What is the purpose of Pod Security Policies?
**Back:** Enforce pod execution rules<br><br>Pod Security Policies define security constraints for pod execution (deprecated but relevant conceptually).
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839563 model:Basic -->
**Front:** What is the concept of "desired state reconciliation" fundamental to Kubernetes?
**Back:** Controllers continuously observe and work to match actual state to declared state.<br><br>Controllers continuously observe the actual state of the cluster and take action to make it match the declared/desired state. This reconciliation loop is the core of Kubernetes: controllers (deployment, replicaset, etc.) watch the API server and correct drift automatically.
**Tags:** k8s::cka src::deck-import topic::fundamentals src::session

---

<!-- note:1794496839566 model:Basic -->
**Front:** Which THREE statements about Labels and Selectors are correct?
**Back:** Services select pods for traffic, Deployments select pods they manage, labels organize/select subsets<br><br>(Select THREE) Labels are arbitrary key/value metadata on objects; SELECTORS are the query mechanism that consumes them. True statements: (A) Service spec.selector matches pod labels → those pods receive traffic; (B) Deployment/ReplicaSet spec.selector.matchLabels determines which pods it OWNS and manages (adoption, not just traffic); (C) labels group objects and enable subset selection via equality- or set-based selectors. Distractors: (D) labels need NOT be unique in a namespace — many objects share labels, that's the point of grouping; (E) annotations are non-identifying metadata and CANNOT be used by selectors — only labels are queryable.
**Tags:** k8s::cka topic::labels topic::selectors src::session

---

<!-- note:1794496839567 model:Basic -->
**Front:** Which field does a Deployment use to determine which Pods it owns and manages?
**Back:** spec.selector.matchLabels — the Deployment's selector determines which pods it owns and manages<br><br>Workload controllers (Deployment, ReplicaSet, StatefulSet, DaemonSet) use spec.selector.matchLabels (or matchExpressions for set-based) to determine which pods they OWN — the controller adopts matching pods and manages their lifecycle. Two traps: spec.template.metadata.labels is where the controller SETS labels on pods it creates (the producer side, not the selector); and the selector is IMMUTABLE after creation — changing it requires recreating the workload. Services use a different field (spec.selector) purely for traffic routing.
**Tags:** k8s::cka topic::labels topic::selectors topic::deployments src::session

---

<!-- note:1794496839570 model:Basic -->
**Front:** You want to view the logs of a container named 'app' inside a pod named 'web-pod-7d4f8'. Which kubectl command should you use?
**Back:** kubectl logs web-pod-7d4f8 -c app<br><br>kubectl logs is the verb (always plural — 'log' doesn't exist); the pod name is positional; -c/--container selects WHICH container when the pod has several (default = first container). Distractors: A uses exec — exec runs a NEW command inside the container, it doesn't fetch logs; B has the nonexistent 'log' verb; D passes 'app' as a second positional arg which kubectl rejects. Related flags worth knowing: --previous (logs of the last crashed instance — the CrashLoopBackOff debugging tool), -f/--follow, --tail=N, --since.
**Tags:** k8s::cka topic::kubectl topic::logging src::session

---

<!-- note:1794496839571 model:Basic -->
**Front:** A pod 'my-pod' shows repeated 'BackOff' events after the container starts. Which is the most likely cause?
**Back:** The application crashes shortly after starting<br><br>Read events CHRONOLOGICALLY: Pulling → Pulled → Created → Started all succeeded — the image exists and the container RAN. Then BackOff = it exited and kubelet is delaying restart. So the failure is POST-start: app crash (bad config, missing env, port conflict, liveness probe killing it). Distractors fail the timeline test: missing image would show ErrImagePull/ImagePullBackOff INSTEAD of Started; OOMKilled shows reason OOMKilled + exit 137; liveness failure shows 'Unhealthy' probe events before restart. Rule: Started followed by BackOff = runtime crash, not pull/scheduling problem.
**Tags:** k8s::cka topic::pods topic::troubleshooting topic::kubectl src::session

---

<!-- note:1794496839572 model:Basic -->
**Front:** How do you list Kubernetes events for a specific pod named 'my-pod'?
**Back:** kubectl get events --field-selector involvedObject.name=my-pod — filters cluster events to just that pod<br><br>kubectl get events lists cluster events newest-first (LAST SEEN, TYPE, REASON, OBJECT, MESSAGE). --field-selector involvedObject.name=<name> scopes to one object — essential since busy clusters flood the list. TYPE is Normal (info: Pulled, Started, Scheduled) or Warning (problems: BackOff, Failed, Unhealthy, FailedScheduling). Pair with kubectl describe pod <pod> which shows the same events inline plus pod conditions. For a specific reason: --field-selector reason=BackOff.
**Tags:** k8s::cka topic::kubectl topic::troubleshooting src::session

---

<!-- note:1794496839574 model:Basic -->
**Front:** Which of the following are responsibilities of the kubelet? (Select all that apply)<br><br>A. Watches for pods assigned to its node and starts/stops their containers<br>B. Runs liveness and readiness probes against containers<br>C. Assigns pods to nodes based on resource availability<br>D. Maintains iptables/IPVS rules for Service traffic<br>E. Registers the node and reports pod/node status to the API server
**Back:** A, B, E – watches pod specs & drives containers; runs probes; registers node & reports status<br><br>Kubelet duties (select all): (A) watches API server for pods bound to its node and starts/stops containers via the runtime — YES; (B) executes liveness/readiness/startup probes — YES; (E) registers the node and reports pod/node status back — YES. NOT kubelet: (C) pod-to-node assignment is the kube-scheduler (control plane); (D) Service traffic rules are kube-proxy. Division of labor: kubelet decides WHAT should run; container runtime (containerd/CRI-O) does the actual container mechanics via CRI.
**Tags:** k8s::cka topic::architecture topic::kubelet src::session

---

<!-- note:1794496839575 model:Basic -->
**Front:** A developer creates a Pod with a container that writes logs to a file in an emptyDir volume. The Pod is then deleted, and a new Pod is created with the same emptyDir volume definition. What happens to the data in the emptyDir volume?
**Back:** The data is lost because emptyDir volumes are deleted when the Pod is deleted<br><br>emptyDir lifetime = the POD's lifetime, not the node's. Created when the pod is scheduled, deleted when the pod is deleted — a replacement pod gets a FRESH emptyDir even on the same node. It CAN'T be backed by a PVC (that's not how volume types compose — PVC backs a PersistentVolume directly). For data that must survive pod deletion you need PVC→PV, or accept loss. emptyDir's real jobs: scratch space and sharing files BETWEEN CONTAINERS of the same pod.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839576 model:Basic -->
**Front:** Which scenario is the BEST fit for an emptyDir volume?
**Back:** Sharing a scratch/cache directory between an app container and a sidecar in the same pod<br><br>emptyDir = pod-scoped temporary storage: exists only while THAT pod runs, deleted with it. Perfect for: scratch space, build caches, and sharing files between containers IN THE SAME POD (e.g. app writes to emptyDir, sidecar ships the logs). WRONG for anything surviving pod deletion — pod logs you want to keep, databases, user uploads → PVC/PV. Same-node scheduling doesn't help: the volume is bound to the pod, not the node.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839577 model:Basic -->
**Front:** Why was the sidecar container pattern introduced in Kubernetes?
**Back:** To attach supporting functionality — logging, monitoring, proxying — to an application without modifying its code or image<br><br>Sidecars decouple cross-cutting concerns from business logic: the app image stays focused on its function while helper containers (log shipper, metrics agent, service-mesh proxy like Envoy, config/secret syncer) run alongside in the same Pod. Because helpers are separate containers they can be updated, swapped, or written in different languages without rebuilding or redeploying the app — e.g. Istio injects an Envoy sidecar to add mTLS without touching application code. Note what sidecars do NOT provide: each container still shares the Pod's single network namespace (no per-container IP), and the Pod — not the sidecar — is the isolation/security boundary.
**Tags:** k8s::cka topic::sidecars topic::pods src::session

---

<!-- note:1794496839578 model:Basic -->
**Front:** Which resources does a sidecar container share with the app container in the same Pod? (Select all that apply)<br><br>A. Network namespace — same IP address, localhost, and port space<br>B. Process (PID) namespace — the same visible process list<br>C. Pod volumes — can mount the same filesystems to exchange files<br>D. The node's root filesystem<br>E. The app container's writable filesystem layer
**Back:** A, C – Network namespace and Pod volumes<br><br>Sidecars share the Pod's NETWORK namespace — that is why app and sidecar talk to each other over localhost with no Service or DNS needed. They can also share VOLUMES (e.g. emptyDir) so a log shipper can tail files the app writes. They do NOT share the process namespace (each container has its own PID namespace and cannot see the other's processes), the node's filesystem, or the app container's writable layer — file sharing requires an explicitly mounted Pod volume.
**Tags:** k8s::cka topic::sidecars topic::pods src::session

---

<!-- note:1794496839579 model:Basic -->
**Front:** How does a sidecar container differ from a regular init container?
**Back:** Init containers run to completion before app containers start and cannot send data back; sidecars run for the Pod's whole lifetime, support probes, and communicate bidirectionally over localhost<br><br>Regular init containers execute SEQUENTIALLY TO COMPLETION before any app container starts — data flow is one-way (init writes to a volume, app reads it later). A native sidecar is declared as an initContainer with restartPolicy: Always: it starts in init order but KEEPS RUNNING for the Pod's lifetime, supports liveness/readiness probes, and shares the network namespace so it can talk to the app bidirectionally via localhost (e.g. a log shipper tailing a shared file while the app runs).
**Tags:** k8s::cka topic::sidecars topic::pods src::session

---

<!-- note:1794496839580 model:Basic -->
**Front:** How is a native sidecar container declared in a Pod spec?
**Back:** List it under spec.initContainers with restartPolicy: Always — it starts before later init and app containers but keeps running for the Pod's lifetime<br><br>Native sidecars (Kubernetes 1.28+, feature gate enabled by default since 1.29 and locked/always-on since 1.33) are a special case of init containers: restartPolicy: Always under initContainers. The kubelet marks the sidecar 'started' once its process runs, then proceeds through remaining init containers to the app containers — giving startup ORDERING — but unlike regular init containers the sidecar never exits. There is no `sidecar: true` field and no Sidecar CRD in core Kubernetes; before 1.28 the pattern relied on a plain second container in spec.containers with no startup ordering.
**Tags:** k8s::cka topic::sidecars topic::pods src::session

---

<!-- note:1794496839581 model:Basic -->
**Front:** When a Pod is terminated, how does the kubelet order container shutdown?
**Back:** App containers are terminated first; sidecars stop LAST in reverse order of their spec position, so they keep supporting (e.g. flushing logs) until the end<br><br>On Pod termination the kubelet postpones stopping sidecar containers until the main app containers have fully stopped, then shuts the sidecars down in REVERSE order of their appearance in the Pod spec. This keeps helpers operational while the app winds down — a log shipper can flush remaining entries, a mesh proxy can drain connections — instead of vanishing at the first SIGTERM. Related gotcha: sidecar containers often exit non-zero during termination because they may not get graceful-shutdown time; that is normal and should be ignored by tooling.
**Tags:** k8s::cka topic::sidecars topic::pods src::session

---

<!-- note:1794496839582 model:Basic -->
**Front:** Which are typical responsibilities of a sidecar container? (Select all that apply)<br><br>A. Shipping the app's logs to a centralized logging backend (e.g. Fluent Bit)<br>B. Proxying and encrypting service-to-service traffic (e.g. an Istio/Envoy mesh sidecar)<br>C. Syncing secrets or configuration into a shared volume<br>D. Implementing the application's core business logic<br>E. Load-balancing traffic across Pods in the cluster
**Back:** A, B, C – Log shipping, mesh proxying, and config/secret syncing<br><br>Sidecars provide SUPPORTING services around the app: log collection/forwarding (Fluent Bit), metrics/observability agents, service-mesh proxies (Istio's Envoy sidecar adds mTLS, retries, traffic splitting without app changes), config/secret syncers, and file generators writing into shared volumes. They explicitly do NOT run the app's business logic (that is the app container's job) and do NOT do cluster-level traffic management — that is the Service/Ingress/Gateway layer.
**Tags:** k8s::cka topic::sidecars topic::pods src::session

---

<!-- note:1794496839583 model:Basic -->
**Front:** When should a helper container be declared as a native sidecar (spec.initContainers + restartPolicy: Always) rather than just added to spec.containers?
**Back:** When you need startup ORDERING plus sidecar lifecycle semantics: a native sidecar is guaranteed to be running before the next init container and before the app containers start — the kubelet proceeds once its 'started' status is true — and it then keeps running for the Pod's whole lifetime with its own restart/probe behavior. A plain second container under spec.containers gets no ordering guarantee: all regular containers start together and none is treated as a prerequisite for the others.
**Tags:** k8s::cka topic::sidecars topic::pods src::session

---

<!-- note:1794496839585 model:Basic -->
**Front:** What is a 'layer' in a Docker image?
**Back:** Each Dockerfile instruction creates a layer containing ONLY the changes/diff relative to the previous layer<br><br>A Docker image is a stack of read-only layers: FROM provides the base, then each instruction (RUN, COPY, ADD…) produces ONE new layer holding just what that instruction changed — e.g. 'apt-get install nginx' adds nginx's files as a layer, not a whole new filesystem. Layers are content-addressed and shareable. Nuance: metadata instructions (ENV, LABEL, EXPOSE) also create thin layers; ENTRYPOINT/CMD only set config — they don't add file layers.
**Tags:** k8s::cka topic::docker topic::storage topic::images src::session

---

<!-- note:1794496839592 model:Basic -->
**Front:** What does ENTRYPOINT do in a Dockerfile, and how does it differ from CMD?
**Back:** ENTRYPOINT defines the executable the container RUNS when it starts — the fixed 'main' process. Difference from CMD: CMD sets default ARGUMENTS and is fully overridable (<code>docker run image other-cmd</code>); ENTRYPOINT is not replaced — extra args from docker run get APPENDED to it. The idiomatic combo: <code>ENTRYPOINT ["python"] + CMD ["app.py"]</code> lets you swap the script without changing the interpreter. ENTRYPOINT affects only container startup — it creates no filesystem layer (it's config, like ENV/LABEL).
**Tags:** k8s::cka topic::docker topic::images src::session

---

<!-- note:1794496839594 model:Basic -->
**Front:** What is the difference between a Docker storage driver and a volume driver?
**Back:** Storage drivers manage the layered image filesystem (CoW); volume drivers manage named-volume lifecycle and where volume data actually lives<br><br>Two different plugin systems, easy to confuse: STORAGE DRIVERS (overlay2, aufs, zfs…) implement the layered read-only-image + writable-container-layer filesystem — they know nothing about volumes. VOLUME DRIVERS/plugins handle the lifecycle of NAMED volumes (create/mount/unmount/remove) and decide WHERE the bytes live — local disk by default, or remote/cloud storage via plugins. Rule: storage driver = image/container filesystem machinery; volume driver = the -v volume backend.
**Tags:** k8s::cka topic::docker topic::storage src::session

---

<!-- note:1794496839598 model:Basic -->
**Front:** How does a Docker volume plugin actually deliver storage to a container?
**Back:** The plugin API (Create/Mount/Unmount/Remove/Get/List/Path) lets external systems manage volume lifecycle; daemon bind-mounts the returned path into the container<br><br>A volume plugin implements the VolumeDriver API over HTTP-ish endpoints: Create (register name), Mount (called per container start — returns a host path where data lives), Unmount (per stop), Remove (on docker rm -v / volume rm), plus Get/List/Path/Capabilities. KEY: the plugin doesn't stream data to the container — it returns a MOUNTPOINT path, and the Docker daemon bind-mounts that path into the container. Capabilities.Scope matters for clusters: 'global' = create once for the whole cluster; 'local' = per-host. This plugin indirection is the ancestor of Kubernetes CSI drivers.
**Tags:** k8s::cka topic::docker topic::storage topic::volumes src::session

---

<!-- note:1794496839602 model:Basic -->
**Front:** What are the three CSI services a storage plugin can implement? (Select all that apply)<br><br>A. Identity — plugin info and capabilities<br>B. Controller — cluster-level ops: create/delete volumes, attach/detach, expand<br>C. Scheduler — decides which node a volume lands on<br>D. Node — per-node ops: stage, publish into pod, unpublish, stats
**Back:** A, B, D – Identity (plugin info/capabilities), Controller (cluster-level create/delete/attach/expand), and Node (per-node stage/publish/unpublish/stats); E is wrong — CSI has no 'Scheduler' service<br><br>The CSI spec defines three gRPC services a plugin may implement: IDENTITY — GetPluginInfo/GetPluginCapabilities/Probe: 'who are you, what can you do'; CONTROLLER — cluster-scoped ops usually run once: CreateVolume, DeleteVolume, ControllerPublishVolume (attach to node), ControllerUnpublishVolume, ControllerExpandVolume; NODE — per-node ops run on every node that mounts the volume: NodeStageVolume (format + global mount), NodePublishVolume (bind into pod path), NodeUnpublish/Unstage, NodeGetVolumeStats. A driver can implement all three or only node (for pre-provisioned local volumes).
**Tags:** k8s::cka topic::storage topic::csi src::session

---

<!-- note:1794496839607 model:Basic -->
**Front:** Why do Kubernetes pods need volumes?
**Back:** Pods are ephemeral like containers — volume mounts give data persistence beyond pod life and let containers share files<br><br>Same problem as Docker, one level up: pods are ephemeral — scheduled, run, deleted; container filesystem writes die with them (kubelet restarts crashed containers with a CLEAN state). Kubernetes volumes solve the two core problems: (1) PERSISTENCE — a mounted volume's data survives pod deletion (for persistent types) and container restarts (always); (2) SHARING — multiple containers in one pod can mount the same volume to share files (app + log-shipper sidecar is the classic). A volume is fundamentally just 'a directory, possibly with data, accessible to the pod's containers' — the type decides what backs it.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839608 model:Basic -->
**Front:** How are volumes declared and mounted in a Pod spec?
**Back:** .spec.volumes declares the volumes; .spec.containers[].volumeMounts mounts each into a specific container path — every container mounts independently<br><br>Pod volumes are a TWO-PART declaration: (1) spec.volumes[] — top-level list declaring each volume and its TYPE (emptyDir: {}, hostPath: {path:...}, persistentVolumeClaim: {claimName:...}, secret: {...}…); (2) spec.containers[].volumeMounts[] — per-container list saying mountPath: where inside THAT container + name: which declared volume. Every container that needs the volume must list its own volumeMount — volumes are pod-scoped, mounts are container-scoped. A volume can be mounted by multiple containers (sharing) or just one.
**Tags:** k8s::cka topic::storage topic::volumes topic::yaml src::session

---

<!-- note:1794496839609 model:Basic -->
**Front:** What does a hostPath volume do in Kubernetes?
**Back:** hostPath mounts a file or directory from the NODE's filesystem into the pod — a powerful escape hatch with real security risks<br><br>hostPath is Kubernetes' version of Docker's bind mount: spec.volumes[].hostPath.path points at a path on the NODE's filesystem, mounted into the pod. It's the 'powerful escape hatch' — needed for node-level access (reading /var/log for log collectors, static pods that can't use ConfigMaps) — but the docs warn heavily: it can expose kubelet credentials or the container runtime socket (container escape!), behavior differs per node (files differ), and hostPath usage does NOT count as ephemeral storage (you monitor disk yourself). Prefer a 'local' PersistentVolume when you can.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839610 model:Basic -->
**Front:** Which hostPath volume 'type' values are valid? (Select all that apply)<br><br>A. DirectoryOrCreate creates a 0755 directory if the path doesn't exist<br>B. Directory requires the path to already exist as a directory<br>C. FileOrCreate creates a directory with 0755 permissions<br>D. File requires the path to already exist as a file<br>E. Socket requires a UNIX socket at the path<br>F. BlockDeviceOrCreate auto-provisions a block device
**Back:** B, D, E – DirectoryOrCreate creates a 0755 dir if missing, FileOrCreate creates a 0644 file; the rest either require existence (Directory/File), require special files (Socket/CharDevice/BlockDevice), or skip checks ("")<br><br>hostPath.type controls validation/creation at mount time: "" (empty, default) = NO checks — mounts whatever's there, backward compatible; Directory = must already exist; DirectoryOrCreate = creates empty dir 0755 owned by kubelet if missing; File = must exist; FileOrCreate = creates empty file 0644 if missing; Socket = must be a UNIX socket; CharDevice/BlockDevice = must be device nodes (Linux only). A is wrong — File requires an existing FILE not dir; C mixes them up; F doesn't exist.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839611 model:Basic -->
**Front:** Which of these are valid Kubernetes pod volume types? (Select all that apply)<br><br>A. emptyDir<br>B. Service<br>C. configMap<br>D. secret<br>E. persistentVolumeClaim<br>F. downwardAPI
**Back:** A, C, D, E, F – emptyDir, configMap, secret, downwardAPI, projected, and persistentVolumeClaim are all real pod volume types; Service is a networking object, not a volume<br><br>Kubernetes pod volume types fall into families: POD-SCOPED (die with pod) — emptyDir, hostPath, configMap, secret, downwardAPI, projected, image; CLUSTER-STORAGE — persistentVolumeClaim (the pod-side handle to durable storage), csi, local, nfs, iscsi, azureDisk, awsElasticBlockStore, gcePersistentDisk (in-tree ones deprecated → CSI). A pod can mix ANY number of types simultaneously. Service is a networking abstraction — not a volume. The survey-level skill: recognize the TYPE NAME in a pod spec and know which family it belongs to.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839612 model:Basic -->
**Front:** Which Kubernetes volume types persist data beyond the pod's lifetime?
**Back:** Ephemeral types (emptyDir, hostPath, configMap, secret…) die with the pod; PVC-backed volumes persist beyond pod deletion; container restarts preserve data for ALL types<br><br>The lifetime split: EPHEMERAL volumes (emptyDir, hostPath unless on persistent host dir, configMap, secret, downwardAPI, projected, image) are destroyed when the pod is deleted — their lifetime is bound to the pod. PERSISTENT volumes (via persistentVolumeClaim → PV, or CSI) exist beyond any pod's life — delete the pod, the data stays for the next pod to claim. Nuance that trips people: data survives CONTAINER restarts inside a running pod for EVERY volume type — the wipe happens at POD deletion for ephemeral types. hostPath is a gray zone: the mount dies with the pod but the host directory's data persists on the node.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839615 model:Basic -->
**Front:** What does subPath do in a volumeMount, and when do you use it?
**Back:** subPath mounts only a SUBDIRECTORY of a volume instead of the whole thing: volumeMounts[].subPath: 'subdir' exposes just <volume>/subdir at mountPath. Use cases: mount one file/dir out of a shared config volume without exposing siblings; give a container write access to only part of a shared volume; mount a single file from a ConfigMap/Secret volume. Caveat: subPath does NOT get updated when the volume's content changes (no live updates for that subtree) — for config that must stay current, mount the whole volume or use env vars.
**Tags:** k8s::cka topic::storage topic::volumes topic::yaml src::session

---

<!-- note:1794496839616 model:Basic -->
**Front:** What is a projected volume and what problem does it solve?
**Back:** A projected volume merges MULTIPLE volume sources into ONE directory: volumes[].projected.sources[] can combine secret, configMap, downwardAPI, and serviceAccountToken entries — all appear as files in the same mountPath. Classic use: the kubelet itself mounts the pod's service-account token this way (that's why /var/run/secrets/kubernetes.io/serviceaccount/ contains both the token AND ca.crt — different sources, one projected volume). Contrast: a plain secret/configMap volume mounts ONE source; projected stitches several together.
**Tags:** k8s::cka topic::storage topic::volumes src::session

---

<!-- note:1794496839635 model:Basic -->
**Front:** What is the difference between Immediate and WaitForFirstConsumer volumeBindingMode?
**Back:** Immediate (default) provisions at PVC creation — possibly in the WRONG zone; WaitForFirstConsumer waits until the pod is scheduled, then provisions in the pod's zone/topology<br><br>volumeBindingMode controls WHEN provisioning happens: IMMEDIATE (default) — PV is provisioned the moment the PVC is created, BEFORE any pod exists. Problem: a zonal disk (EBS/GCE-PD) provisioned immediately may land in zone A while the pod later schedules in zone B → 'no available volume zone' / multi-attach errors (your earlier card!). WaitForFirstConsumer — the PVC stays Pending until a pod using it is scheduled; the provisioner then creates the volume IN THE POD'S ZONE/topology — the fix for zone-aware storage. Caveats: don't set nodeName in the pod spec (breaks the wait); allowedTopologies can further restrict zones.
**Tags:** k8s::cka topic::storage topic::volumes topic::scheduling src::session

---

<!-- note:1794496839640 model:Basic -->
**Front:** What is the purpose of Docker storage drivers?
**Back:** Storage drivers implement the layered image/container filesystem — overlay2/aufs/zfs/btrfs manage the read-only image layers + writable container layer<br><br>Storage drivers (overlay2 default, aufs, zfs, btrfs…) implement Docker's LAYERED architecture: stacking read-only image layers, the writable container layer, and copy-on-write. D is the classic trap — volumes are NOT storage drivers' job: creating/managing persistent volumes is the VOLUME DRIVERS'/plugins' job (docker volume create --driver=amazon-ebs, local driver → /var/lib/docker/volumes). Storage drivers handle the image+container filesystem layering only; volume plugins handle persistent data lifecycle. B (networks) and C (security) are entirely different subsystems.
**Tags:** k8s::cka topic::docker topic::storage src::session

---

<!-- note:1794496839648 model:Basic -->
**Front:** Pod error "no available volume zone" likely means:
**Back:** PV/PVC zone topology mismatch with available nodes<br><br>Zonal volumes are block storage bound to ONE availability zone — an EBS/GCE-PD/Azure-Disk volume in us-east-1a physically cannot attach to a node in us-east-1b. Kubernetes encodes that constraint as nodeAffinity on the PV (topology.kubernetes.io/zone=<zone>), so the scheduler only places pods using that PVC on nodes in the volume's zone. The error means the volume's zone and the pod's schedulable nodes don't overlap: the PVC was bound in zone A (Immediate binding mode provisions at PVC creation, blind to where the pod will run) while the pod's nodeSelector/affinity/tolerations only allow zone B — or the zone-A nodes are cordoned, full, or gone. The fix direction: volumeBindingMode: WaitForFirstConsumer delays provisioning until pod scheduling so the volume is created in the pod's zone (allowedTopologies can further restrict zones), or relax the pod's node constraints. Distractors: CoreDNS is DNS only, a selector issue breaks Service endpoints not mounts, ImagePullBackOff is an image problem.
**Tags:** k8s::cka src::session topic::scheduling topic::storage topic::topology

---

<!-- note:1794496839651 model:Basic -->
**Front:** Which command creates a Secret with Docker registry credentials?
**Back:** kubectl create secret docker-registry regcred --docker-server=... --docker-username=... --docker-password=... --docker-email=...<br><br>kubectl create secret docker-registry builds the Secret imperatively: --docker-server is the registry FQDN (use https://index.docker.io/v1/ for Docker Hub, or your private registry's address), plus --docker-username/--docker-password/--docker-email. kubectl creates it as type kubernetes.io/dockerconfigjson in your current namespace. Doc warning: passing --docker-password on the CLI can leak it into shell history — prefer the --from-file=.dockerconfigjson variant when you already ran docker login.
**Tags:** k8s::cka src::session topic::images topic::kubectl topic::secrets

---

<!-- note:1794496839652 model:Basic -->
**Front:** You already ran docker login — how do you turn that credential into a cluster Secret?
**Back:** kubectl create secret generic regcred --from-file=.dockerconfigjson=~/.docker/config.json --type=kubernetes.io/dockerconfigjson<br><br>If you already ran docker login locally, reuse ~/.docker/config.json directly: kubectl create secret generic regcred --from-file=.dockerconfigjson=<path> --type=kubernetes.io/dockerconfigjson. The critical detail: the data key MUST be named .dockerconfigjson (that's what the kubelet looks for) and type must be kubernetes.io/dockerconfigjson. The file's auths entries carry base64 username:password per registry — same format docker uses.
**Tags:** k8s::cka src::session topic::images topic::kubectl topic::secrets

---

<!-- note:1794496839658 model:Basic -->
**Front:** What commands does a CNI plugin implement for the container lifecycle?
**Back:** ADD connects the container to the network; DEL tears the interfaces down; plus CHECK and VERSION<br><br>A CNI plugin is an executable that implements spec commands: ADD — called when a container is created, attaches its interface to the network (veth, IP, routes); DEL — called on teardown, removes interfaces and releases the IP; CHECK — verifies config is still applied (optional); VERSION — reports supported spec version. The runtime invokes these per container lifecycle — 'the script' your lecture demoed is exactly this ADD/DEL contract.
**Tags:** k8s::cka src::session topic::cni topic::networking

---

<!-- note:1794496839666 model:Basic -->
**Front:** In a container image built from a Dockerfile, what is the purpose of the CMD instruction?
**Back:** To provide default arguments for the ENTRYPOINT instruction<br><br>CMD provides DEFAULT arguments — consumed by ENTRYPOINT if one exists, or executed as the command itself if it doesn't. It's overridable at runtime: 'docker run image myargs' replaces CMD's args but keeps ENTRYPOINT; 'docker run image --entrypoint x' replaces ENTRYPOINT. Contrast: ENTRYPOINT defines the fixed executable (the 'what'), CMD defines default params (the 'how') — the entrypoint+cmd pair lets you ship one image used many ways (e.g. ENTRYPOINT ["/docker-entrypoint.sh"], CMD ["postgres"]).
**Tags:** k8s::cka src::session topic::containers topic::dockerfile

---

<!-- note:1794496839668 model:Basic -->
**Front:** What core benefit does containerization (e.g., using Docker or containerd) provide for application deployment?
**Back:** Consistent runtime environment across different machines<br><br>Containers bundle an application with its dependencies,<br>ensuring it runs consistently regardless of the host environment, solving<br>”it works on my machine” problems.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839673 model:Basic -->
**Front:** In the context of container security, what does ”least privilege” primarily refer to?
**Back:** Granting containers only the permissions they absolutely need<br><br>The principle of least privilege means that containers (and<br>their processes) should run with only the capabilities and permissions<br>essential for their function, reducing the potential impact of a compromise.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839674 model:Basic -->
**Front:** What is the main benefit of using container orchestration systems like Kubernetes?
**Back:** Automating deployment scaling<br><br>Orchestrators automate the deployment, scaling, management, and networking of containerized applications.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839687 model:Basic -->
**Front:** What is the primary function of Kubernetes?
**Back:** Managing container lifecycle<br><br>Kubernetes manages deployment, scaling, and operation of containerized applications.
**Tags:** k8s::cka src::deck-import topic::container-orchestration src::session

---

<!-- note:1794496839705 model:Basic (and reversed card) -->
**Front:** What is kubectl?
**Back:** The Kubernetes command-line tool used to deploy and manage applications on a cluster — deploy workloads, get cluster and resource status, and manage cluster objects.
**Tags:** k8s::cka topic::architecture src::session

---

<!-- note:1794496839710 model:Basic (and reversed card) -->
**Front:** What is a Deployment in Kubernetes?
**Back:** A higher-level workload object that runs a set of identical pods (usually stateless apps) through ReplicaSets it owns, and provides declarative updates — rollouts between pod-template versions at a controlled rate, revision history, and rollback.
**Tags:** k8s::cka topic::deployments topic::pods src::session

---

<!-- note:1794496839711 model:Basic (and reversed card) -->
**Front:** What is a revision in a Kubernetes Deployment?
**Back:** A numbered record of the Deployment's pod template at the moment a rollout was triggered — revision 1, 2, 3… increments each time <code>spec.template</code> changes (visible via <code>kubectl rollout history</code> and the <code>deployment.kubernetes.io/revision</code> annotation). Scaling does not bump it. Each revision corresponds to the old ReplicaSet you can roll back to with <code>--to-revision=N</code>.
**Tags:** k8s::cka topic::deployments topic::rollouts src::session

---

<!-- note:1794496839712 model:Basic (and reversed card) -->
**Front:** Which values are valid for <code>spec.strategy.type</code> in a Deployment manifest?
**Back:** Only <code>RollingUpdate</code> (default — gradual swap, no downtime) and <code>Recreate</code> (all old pods die, then new ones start — brief downtime).
**Tags:** k8s::cka topic::deployments topic::strategy src::session

---

<!-- note:1794496839713 model:Basic (and reversed card) -->
**Front:** What is a label in Kubernetes?
**Back:** A key/value pair attached to an object in <code>metadata.labels</code> (e.g. <code>tier: frontend</code>, <code>environment: production</code>). Labels mark attributes meaningful to you — Kubernetes doesn't interpret them — and they let you group and select subsets of objects.
**Tags:** k8s::cka topic::labels topic::pods src::session

---

<!-- note:1794496839714 model:Basic (and reversed card) -->
**Front:** What are the two kinds of label selectors in Kubernetes?
**Back:** Equality-based (<code>=</code>, <code>==</code>, <code>!=</code> — e.g. <code>environment=production</code>, <code>tier!=frontend</code>) and set-based (<code>in</code>, <code>notin</code>, <code>exists</code> — e.g. <code>environment in (production, qa)</code>). Multiple requirements are comma-separated and ANDed; there is no OR. ReplicaSets support set-based selectors via <code>matchExpressions</code> — the legacy ReplicationController only had equality-based.
**Tags:** k8s::cka topic::labels topic::selectors src::session

---

<!-- note:1794496839717 model:Basic (and reversed card) -->
**Front:** What is a pod in Kubernetes?
**Back:** The smallest deployable object in Kubernetes. A pod encapsulates one or more containers and represents a single instance of an application — Kubernetes deploys, schedules and scales pods, not bare containers.
**Tags:** k8s::cka topic::pods src::session

---

<!-- note:1794496839718 model:Basic (and reversed card) -->
**Front:** In Kubernetes, what is a replica?
**Back:** One of several identical copies of a pod running the same application. Replicas give an app redundancy (one can die without outage) and capacity (traffic spreads across many copies).
**Tags:** k8s::cka topic::pods topic::replicasets src::session

---

<!-- note:1794496839719 model:Basic (and reversed card) -->
**Front:** What does <code>spec.selector</code> do in a ReplicaSet, and what must it match?
**Back:** The required label selector (usually <code>spec.selector.matchLabels</code>) that identifies which pods the ReplicaSet counts and owns. Rule: the labels in <code>spec.template.metadata.labels</code> must match the selector, or the API rejects the manifest.
**Tags:** k8s::cka topic::pods topic::replicasets src::session

---

<!-- note:1794496839727 model:Basic (and reversed card) -->
**Front:** In a Kubernetes manifest, what does the <code>kind</code> field specify?
**Back:** The type of object you want to create — e.g. <code>Pod</code>, <code>Service</code>, <code>Deployment</code>, <code>StatefulSet</code>, <code>Job</code>. The kind also determines which fields are valid under <code>spec</code>, since each kind has its own spec schema.
**Tags:** k8s::cka topic::api topic::yaml src::session

---

<!-- note:1794496839728 model:Basic (and reversed card) -->
**Front:** What is the IMPERATIVE approach to managing infrastructure or Kubernetes objects?
**Back:** The approach where you spell out WHAT you want AND HOW to get there — every step explicitly, in order (<code>run this</code>, <code>create that</code>, <code>scale this to 5</code>). The tool executes commands; it doesn't reason about an end state. Examples: kubectl run/create/expose/scale/edit/set image — and shell scripts in the DevOps world.
**Tags:** k8s::cka src::session topic::declarative topic::kubectl

---

<!-- note:1794496839729 model:Basic (and reversed card) -->
**Front:** What is the DECLARATIVE approach to managing infrastructure or Kubernetes objects?
**Back:** The approach where you describe only WHAT the end state should look like — a manifest of desired state — and the system works out the HOW itself (diff, plan, reconcile). Examples: <code>kubectl apply -f</code>, Terraform plans, Kubernetes controllers converging actual→desired state.
**Tags:** k8s::cka src::session topic::declarative topic::kubectl

---

<!-- note:1794496839732 model:Basic (and reversed card) -->
**Front:** What is the <code>spec.nodeName</code> field on a pod?
**Back:** It holds the name of the node the pod is bound to run on. It's empty when you submit the pod — the scheduler fills it (via a Binding) after choosing a node. If you set <code>spec.nodeName</code> yourself at creation time, the pod skips the scheduler entirely: manual scheduling. Immutable afterwards.
**Tags:** k8s::cka src::session topic::pods topic::scheduling

---

<!-- note:1794496839733 model:Basic (and reversed card) -->
**Front:** Mechanically, what does the kube-scheduler DO once it picks a node for a pod?
**Back:** The scheduler creates a <code>Binding</code> object — a POST to the pod's <code>binding</code> subresource naming the chosen node. The API server records the decision by writing <code>spec.nodeName</code> on the pod; the kubelet on that node then sees the pod is assigned to it and starts the containers.
**Tags:** k8s::cka src::session topic::architecture topic::scheduling

---

<!-- note:1794496839734 model:Basic (and reversed card) -->
**Front:** Labels vs selectors — which side does what?
**Back:** Labels are key-value pairs ATTACHED to objects under <code>metadata.labels</code> — the grouping side (tag by app, tier, env, version…). Selectors are QUERIES that filter objects by their labels — the selection side (<code>kubectl -l</code>, Service <code>spec.selector</code>, ReplicaSet <code>matchLabels</code>, NetworkPolicy). Labels tag things; selectors find them.
**Tags:** k8s::cka src::session topic::api topic::labels

---

<!-- note:1794496839735 model:Basic (and reversed card) -->
**Front:** What are annotations in Kubernetes — and a few typical examples?
**Back:** Key-value string metadata for informational purposes — recording details that identify nothing and select nothing: build/release version, git commit, owner contact, docs links, or config for tools and controllers (e.g. <code>kubectl.kubernetes.io/last-applied-configuration</code>, Prometheus <code>scrape</code> hints). They live under <code>metadata.annotations</code>, beside <code>metadata.labels</code>.
**Tags:** k8s::cka src::session topic::annotations topic::api

---

<!-- note:1794496839736 model:Basic (and reversed card) -->
**Front:** Taints vs tolerations — which object gets which, and what's the pair for?
**Back:** A scheduling restriction pair: <b>taints on NODES repel</b> pods (the node says 'stay away unless allowed'); <b>tolerations on PODS</b> let them bypass a matching taint. Effect: keeps pods off unsuitable nodes — dedicated hardware, control plane, special workloads. Tolerations permit but never attract — pods can still land anywhere.
**Tags:** k8s::cka src::session topic::scheduling topic::taints

---

<!-- note:1794496839737 model:Basic (and reversed card) -->
**Front:** What is <code>spec.nodeSelector</code> on a pod?
**Back:** A pod-spec field holding key-value pairs that constrain WHERE the pod may run: the scheduler only picks nodes whose labels satisfy ALL listed pairs. <code>spec.nodeSelector: {size: large}</code> = 'nodes labelled size=large only'. It's the simplest node-constraint mechanism — hard equality matching only, no OR/preferences.
**Tags:** k8s::cka src::session topic::nodeselector topic::scheduling

---

<!-- note:1794496839738 model:Basic (and reversed card) -->
**Front:** What is node affinity — and what does it add over nodeSelector?
**Back:** The expressive version of nodeSelector — pod-specified rules under <code>spec.affinity.nodeAffinity</code> that attract pods to (or repel from) nodes based on node labels. Adds what nodeSelector lacks: OR logic (values lists, multiple terms), NOT operators (NotIn/DoesNotExist = anti-affinity), and SOFT preferences (preferredDuringScheduling... with weights). Exists purely to control pod placement.
**Tags:** k8s::cka src::session topic::affinity topic::scheduling

---

<!-- note:1794496839739 model:Basic (and reversed card) -->
**Front:** resources.requests vs resources.limits — what does each actually do?
**Back:** <b>requests</b> = the reservation — what the scheduler assumes the container needs, used to pick a node (guaranteed share at runtime). <b>limits</b> = the ceiling — how much it may use AT MOST. Exceed the CPU limit → throttled; exceed the memory limit → the container is killed (OOMKilled) and restarted per restartPolicy. Rule: requests for scheduling, limits for containment.
**Tags:** k8s::cka src::session topic::containers topic::resources

---

<!-- note:1794496839740 model:Basic (and reversed card) -->
**Front:** What problem do resource requests and limits solve?
**Back:** Without limits one pod can consume ALL of a node's CPU/memory — starving every other workload on it ('noisy neighbor'). requests fix placement: the scheduler guarantees the pod its share and won't overbook the node. limits fix containment: CPU over-limit → throttled; memory over-limit → OOMKilled, because memory can't be throttled — you can't take RAM back from a process except by killing it.
**Tags:** k8s::cka src::session topic::resources topic::scheduling

---

<!-- note:1794496839741 model:Basic (and reversed card) -->
**Front:** What is a DaemonSet — and which workloads belong in one?
**Back:** A workload controller that runs ONE copy of a pod on every node (or a subset via nodeSelector/affinity in the template). Replica count follows node count — nodes joining get the pod automatically. Used for node-local agents that must exist everywhere: monitoring exporters, log collectors (fluentd), kube-proxy, CNI plugins like Calico. apiVersion: apps/v1.
**Tags:** k8s::cka src::session topic::daemonsets topic::workloads

---

<!-- note:1794496839742 model:Basic (and reversed card) -->
**Front:** What is a static pod?
**Back:** A pod created and managed directly by the kubelet — no API server, no scheduler, no controller. The kubelet periodically scans a configured directory (staticPodPath in the KubeletConfiguration, commonly /etc/kubernetes/manifests; deprecated flag: <code>--pod-manifest-path</code>) and runs every pod manifest found there, restarting them on failure. For visibility it mirrors each into the API server as a read-only object.
**Tags:** topic::pods topic::staticpods src::session

---

<!-- note:1794496839743 model:Basic (and reversed card) -->
**Front:** How does the kube-scheduler place a pod, step by step?
**Back:** Two cycles: the <b>scheduling cycle</b> (serial — one pod at a time) runs QueueSort → Filter → Score and PICKS a node; the <b>binding cycle</b> (concurrent) applies it via a Binding object → writes <code>spec.nodeName</code>. Between them sits Reserve — marks the node's resources as taken so concurrent binds can't collide. Failed/aborted cycles return the pod to the queue for a retry.
**Tags:** k8s::cka src::session topic::pods topic::scheduling

---

<!-- note:1794496839744 model:Basic (and reversed card) -->
**Front:** What are scheduler plugins in kube-scheduler?
**Back:** Pluggable extension points in the scheduling framework, compiled into kube-scheduler: QueueSort (queue order), PreFilter/Filter (eliminate infeasible nodes), PostFilter (runs only if nothing fits — e.g. preemption), PreScore/Score (rank feasible nodes), Reserve (claim node before bind), Permit (approve/deny/wait), PreBind/Bind/PostBind (write the assignment). You can compile in your own and toggle them per profile.
**Tags:** k8s::cka src::session topic::api topic::scheduling

---

<!-- note:1794496839745 model:Basic (and reversed card) -->
**Front:** By default, how much pod-to-pod traffic does Kubernetes allow, and what restricts it?
**Back:** Open — the pod network is flat: every pod can reach every other pod and namespace by default (no built-in isolation). NetworkPolicy is the opt-in control: a policy selects pods (podSelector) and whitelists ingress/egress; once a pod is selected by any policy, only matching traffic is allowed. Policies are enforced by the CNI plugin — a CNI that doesn't support NetworkPolicies silently ignores them.
**Tags:** k8s::cka src::session topic::networking topic::security

---

<!-- note:1794496839750 model:Cloze -->
**Text:** Update Deployment 'web' to a new image, then roll it back:<br><br><code>kubectl set image {{c1::deployment}}/web {{c2::nginx}}={{c3::nginx:1.16.1}}<br>kubectl rollout {{c4::undo}} deployment/web</code>
**Back Extra:** set image patches the pod template — which is what triggers a rolling update. rollout undo returns to the previous revision (old ReplicaSet scaled back up). Watch progress with kubectl rollout status.
**Tags:** k8s::cka topic::deployments topic::kubectl src::session

---

<!-- note:1794496839752 model:Cloze -->
**Text:** Minimal ReplicaSet manifest:<br><br><code>apiVersion: {{c1::apps/v1}}<br>kind: {{c2::ReplicaSet}}<br>metadata:<br>&nbsp;&nbsp;name: frontend<br>spec:<br>&nbsp;&nbsp;{{c3::replicas}}: 3<br>&nbsp;&nbsp;{{c4::selector}}:<br>&nbsp;&nbsp;&nbsp;&nbsp;matchLabels:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tier: frontend<br>&nbsp;&nbsp;template: &lt;pod template&gt;</code>
**Back Extra:** ReplicaSet lives in the named API group 'apps' (hence apps/v1). replicas = desired count; selector.matchLabels links it to pods; template is the pod blueprint it stamps out when the actual count is low.
**Tags:** k8s::cka topic::replicasets topic::yaml src::session

---

<!-- note:1794496839753 model:Cloze -->
**Text:** Scale the 'frontend' ReplicaSet to 5 replicas imperatively:<br><br><code>kubectl scale {{c1::--replicas=5}} {{c2::rs}}/frontend</code>
**Back Extra:** Imperative scaling — changes only the live object. rs is the short name for replicaset; <code>-f file.yaml</code> works instead of TYPE/NAME. For GitOps, edit spec.replicas in the manifest and apply instead, or the next sync reverts this.
**Tags:** k8s::cka topic::gitops topic::replicasets src::session

---

<!-- note:1794496839760 model:Cloze -->
**Text:** Minimal pod manifest:<br><br><code>apiVersion: {{c1::v1}}<br>kind: {{c2::Pod}}<br>metadata:<br>&nbsp;&nbsp;{{c3::name}}: nginx<br>spec:<br>&nbsp;&nbsp;{{c4::containers}}:<br>&nbsp;&nbsp;- name: nginx<br>&nbsp;&nbsp;&nbsp;&nbsp;{{c5::image}}: nginx</code>
**Back Extra:** v1 = core API group (named groups use group/version, e.g. apps/v1 for Deployments). metadata.name is how you identify the pod; spec.containers is a LIST (note the dash) — even a single-container pod needs the list item.
**Tags:** k8s::cka src::session topic::pods topic::yaml

---

<!-- note:1794496839761 model:Cloze -->
**Text:** List only pods labelled <code>app=web</code>:<br><br><code>kubectl get pods {{c1::-l}} {{c2::app=web}}</code><br><br>(<code>-l</code> is short for <code>{{c3::--selector}}</code>)
**Back Extra:** The flag works on most list commands (get pods, get svc, get all, delete). Multiple requirements AND together: -l 'app=web,env=prod'. Set-based form: -l 'env in (prod,qa)'. Combine with <code>--show-labels</code> to see each object's full label set.
**Tags:** k8s::cka src::session topic::kubectl topic::labels

---

<!-- note:1794496839762 model:Cloze -->
**Text:** Record a build version on a pod imperatively:<br><br><code>kubectl {{c1::annotate}} pod web {{c2::build-version}}={{c3::v1.4.2}}</code>
**Back Extra:** Same shape as <code>kubectl label</code>: &lt;resource&gt; &lt;name&gt; &lt;key&gt;=&lt;value&gt;. Re-running with an existing key fails unless you add <code>--overwrite</code>. Remove with a trailing minus: <code>kubectl annotate pod web build-version-</code>. In YAML the same data sits under metadata.annotations.
**Tags:** k8s::cka src::session topic::annotations topic::kubectl

---

<!-- note:1794496839763 model:Cloze -->
**Text:** Taint node1 so only pods tolerating <code>dedicated=gpu</code> may schedule:<br><br><code>kubectl taint nodes node1 {{c1::dedicated=gpu}}:{{c2::NoSchedule}}</code>
**Back Extra:** Format: <code>kubectl taint nodes &lt;node&gt; &lt;key&gt;=&lt;value&gt;:&lt;effect&gt;</code>. Remove a taint by appending a minus: <code>kubectl taint nodes node1 dedicated=gpu:NoSchedule-</code>. Effects: NoSchedule / PreferNoSchedule / NoExecute.
**Tags:** k8s::cka src::session topic::kubectl topic::taints

---

<!-- note:1794496839764 model:Cloze -->
**Text:** Pod spec tolerating a <code>dedicated=gpu:NoSchedule</code> taint — fields under <code>{{c1::spec.tolerations}}</code>:<br><br><code>tolerations:<br>- key: {{c2::"dedicated"}}<br>  operator: {{c3::"Equal"}}<br>  value: {{c4::"gpu"}}<br>  effect: {{c5::"NoSchedule"}}</code>
**Back Extra:** operator defaults to Equal (needs a matching value); Exists matches the key regardless of value (omit 'value'). Effect must equal the taint's effect. Add tolerationSeconds: 3600 under a NoExecute toleration to survive the taint for one hour before eviction.
**Tags:** k8s::cka src::session topic::taints topic::yaml

---

<!-- note:1794496839765 model:Cloze -->
**Text:** Require the pod on large-or-medium nodes via affinity:<br><br><code>spec:<br>  affinity:<br>    {{c1::nodeAffinity}}:<br>      {{c2::requiredDuringSchedulingIgnoredDuringExecution}}:<br>        {{c3::nodeSelectorTerms}}:<br>        - {{c4::matchExpressions}}:<br>          - {key: size, operator: {{c5::In}}, values: [large, medium]}</code>
**Back Extra:** Hierarchy: spec.affinity.nodeAffinity.&lt;type&gt;.nodeSelectorTerms[].matchExpressions[] — each expression is {key, operator, values[]}. values is a LIST (In = OR across values). Preferred type uses - weight: N / preference: matchExpressions instead of plain terms.
**Tags:** k8s::cka src::session topic::affinity topic::yaml

---

<!-- note:1794496839766 model:Cloze -->
**Text:** LimitRange manifest — sets defaults + bounds for containers in its namespace:<br><br><code>apiVersion: {{c1::v1}}<br>kind: {{c2::LimitRange}}<br>metadata: {name: limits}<br>spec:<br>  {{c3::limits}}:<br>  - {{c4::default}}: {cpu: 500m}        # default limit<br>    {{c5::defaultRequest}}: {cpu: 100m} # default request<br>    max: {cpu: "1"}<br>    min: {cpu: 100m}<br>    {{c6::type}}: Container</code>
**Back Extra:** spec.limits[] is a list; each entry has default (default LIMIT), defaultRequest (default request), max, min, and type (Container or PersistentVolumeClaim). Only enforced at admission — existing pods keep their values. Two LimitRanges in one namespace → nondeterministic defaults.
**Tags:** topic::resources topic::yaml src::session

---

<!-- note:1794496839768 model:Cloze -->
**Text:** DaemonSet manifest skeleton (fluentd on every node):<br><br><code>apiVersion: {{c1::apps/v1}}<br>kind: {{c2::DaemonSet}}<br>metadata: {name: fluentd}<br>spec:<br>  {{c3::selector}}:<br>    {{c4::matchLabels}}: {name: fluentd}<br>  {{c5::template}}:<br>    metadata: {labels: {name: fluentd}}<br>    spec: {containers: [...], restartPolicy: {{c6::Always}}}</code>
**Back Extra:** Same skeleton as a Deployment MINUS the replicas field — count is implied (one per node). selector.matchLabels must equal template.metadata.labels and is immutable after creation. Pod template's restartPolicy must be Always (default). Add spec.template.spec.nodeSelector/affinity to cover only a subset of nodes.
**Tags:** k8s::cka src::session topic::daemonsets topic::yaml

---

<!-- note:1794496839770 model:Cloze -->
**Text:** Second profile with customized plugins:<br><br><code>apiVersion: {{c1::kubescheduler.config.k8s.io/v1}}<br>kind: {{c2::KubeSchedulerConfiguration}}<br>{{c3::profiles}}:<br>- {{c4::schedulerName}}: default-scheduler<br>- schedulerName: no-scoring<br>  {{c5::plugins}}:<br>    {{c6::score}}:<br>      {{c7::disabled}}: [{name: NodeResourcesFit}]<br>      {{c8::enabled}}: [{name: MyScorer}]</code>
**Back Extra:** Each profile = its own schedulerName (pods select via spec.schedulerName) + plugin config. plugins.&lt;extensionPoint&gt;.disabled removes stock plugins (name: '*' disables all at that point); enabled adds custom ones (compiled into the scheduler). Extension points: queueSort, preFilter, filter, postFilter, preScore, score, reserve, permit, preBind, bind, postBind.
**Tags:** topic::scheduling topic::yaml src::session

---

<!-- note:1794496839779 model:Cloze -->
**Text:** Long-lived SA token via manually created Secret:<br><br><code>apiVersion: v1<br>kind: Secret<br>metadata:<br>  name: build-robot-secret<br>  annotations:<br>    kubernetes.io/service-account.name: {{c1::build-robot}}<br>type: {{c2::kubernetes.io/service-account-token}}</code>
**Back Extra:** The annotation is what triggers token generation — control plane writes the JWT into .data.token; valid until the SA is deleted, then auto-cleaned. This is the manual form of the pre-1.24 automatic behavior. kubectl get secret <name> -o yaml reveals it; kubectl describe shows the annotation. Prefer kubectl create token / TokenRequest for anything new.
**Tags:** k8s::cka src::session topic::rbac topic::secrets topic::yaml

---

<!-- note:1794496839783 model:Cloze -->
**Text:** Pod-level securityContext manifest (from the docs):<br><br><code>apiVersion: v1<br>kind: Pod<br>metadata:<br>  name: security-context-demo<br>spec:<br>  securityContext:<br>    runAsUser: {{c1::1000}}<br>    runAsGroup: {{c2::3000}}<br>    fsGroup: {{c3::2000}}<br>    supplementalGroups: [{{c4::4000}}]<br>  containers:<br>  - name: sec-ctx-demo<br>    image: busybox<br>    securityContext:<br>      allowPrivilegeEscalation: {{c5::false}}</code>
**Back Extra:** Pod-level fields seen here: runAsUser/runAsGroup (UID/GID for all containers), fsGroup (volume group ownership), supplementalGroups (extra groups). Container-level adds per-container overrides like allowPrivilegeEscalation: false and capabilities. The id output would be uid=1000 gid=3000 groups=2000,3000,4000 — pod settings apply to every container unless overridden.
**Tags:** k8s::cka src::session topic::podsecurity topic::security topic::yaml

---

<!-- note:1794496839784 model:Cloze -->
**Text:** Container-level override example — pod says 1000, container says 2000:<br><br><code>spec:<br>  securityContext:<br>    runAsUser: {{c1::1000}}        # pod default for all containers<br>  containers:<br>  - name: sec-ctx-demo-2<br>    securityContext:<br>      runAsUser: {{c2::2000}}      # overrides pod → runs as 2000<br>      allowPrivilegeEscalation: {{c3::false}}</code>
**Back Extra:** securityContext-2.yaml verbatim: pod-level runAsUser: 1000, container-level runAsUser: 2000 → process runs as 2000 (container wins on overlap). Container settings apply ONLY to that container and never affect pod volumes. kubectl exec -it <pod> -- id confirms the effective UID/GID/groups.
**Tags:** k8s::cka src::session topic::podsecurity topic::security topic::yaml

---

<!-- note:1794496839791 model:Cloze -->
**Text:** Key CSI RPCs the orchestrator calls:<br><br>CONTROLLER service (cluster-scoped):<br>{{c1::<code>CreateVolume</code>}} → {{c2::<code>DeleteVolume</code>}} → {{c3::<code>ControllerPublishVolume</code>}} (attach to node) → {{c4::<code>ControllerUnpublishVolume</code>}} → {{c5::<code>ControllerExpandVolume</code>}}<br><br>NODE service (per-node, kubelet → Unix socket):<br>{{c6::<code>NodeStageVolume</code>}} (format + global mount) → {{c7::<code>NodePublishVolume</code>}} (bind into pod path)
**Back Extra:** CONTROLLER (cluster ops, once): CreateVolume, DeleteVolume, ControllerPublishVolume (attach), ControllerUnpublishVolume (detach), ControllerExpandVolume. NODE (per-node, via kubelet/UDS): NodeStageVolume (format+global mount), NodePublishVolume (bind into pod path), NodeUnpublishVolume, NodeUnstageVolume, NodeGetVolumeStats. IDENTITY: GetPluginInfo, GetPluginCapabilities, Probe. Mnemonic: Controller* = once per volume cluster-wide; Node* = on every node that mounts it.
**Tags:** k8s::cka topic::storage topic::csi src::session

---

<!-- note:1794496715390 model:Cloze -->
**Text:** spec:
  initContainers:
    - name: logshipper
      image: fluent/fluent-bit:latest
      restartPolicy: {{c1::Always}}
  containers:
    - name: app
      image: nginx
**Back Extra:** restartPolicy: Always inside initContainers makes this a NATIVE SIDECAR (Kubernetes 1.28+, always-on since 1.33): it launches in init order before the app container but keeps running for the Pod's entire lifetime, and is terminated only after the app containers stop.
**Tags:** k8s::cka topic::sidecars topic::yaml src::session

---

<!-- note:1794496715392 model:Cloze -->
**Text:** Container resource stanza — where requests and limits live:<br><br><code>containers:<br>- name: app<br>  {{c1::resources}}:<br>    {{c2::requests}}:<br>      {{c3::cpu}}: "{{c4::250m}}"<br>      {{c5::memory}}: "{{c6::256Mi}}"<br>    {{c7::limits}}:<br>      cpu: "500m"<br>      memory: "512Mi"</code>
**Back Extra:** Per-CONTAINER field — a pod's effective request is the sum of its containers' requests. requests = scheduling floor, limits = runtime ceiling. Units: m = millicores (250m = 0.25 CPU); Mi/Gi = binary memory (2^20/2^30), M/G = decimal.
**Tags:** k8s::cka src::session topic::resources topic::yaml

---

<!-- note:1794496715393 model:Cloze -->
**Text:** Spec example — 'dbnet' conflist chaining bridge + tuning + portmap:<br><br><code>{<br>  cniVersion: {{c1::"1.1.0"}},<br>  name: {{c2::dbnet}},<br>  plugins: [<br>    { type: {{c3::bridge}}, bridge: cni0,<br>      ipam: { type: {{c4::host-local}}, subnet: 10.1.0.0/16 } },<br>    { type: {{c5::tuning}}, capabilities: { mac: true } },<br>    { type: {{c6::portmap}}, capabilities: { portMappings: true } }<br>  ]<br>}</code>
**Back Extra:** dbnet example from the spec: bridge creates cni0 + assigns IP via host-local IPAM (10.1.0.0/16, gw 10.1.0.1, default route); dns sets pod resolv.conf nameserver; tuning adjusts sysctls/MAC via capabilities; portmap exposes hostPort mappings via capabilities.portMappings. 'type' in each entry = binary filename in /opt/cni/bin. ipam is itself a plugin delegation (ipam.type = IPAM binary).
**Tags:** k8s::cka src::session topic::cni topic::networking topic::yaml

---
