# Kubernetes for Beginners — deployments

> Deck: `Kubernetes for Beginners` · Group: `deployments` · Notes: 13 · Models: Basic, Basic (and reversed card), Cloze, Many

<!-- note:1793724714419 model:Basic -->
**Front:** Why use a Deployment instead of creating a ReplicaSet directly?
**Back:** A ReplicaSet only guarantees N identical pods stay alive — it has no update strategy. A Deployment adds declarative updates on top: it creates a new ReplicaSet per pod-template version, rolls between them at a controlled rate, keeps old ReplicaSets for rollback, and tracks rollout history. That's why the docs recommend Deployments over managing ReplicaSets directly.
**Tags:** k8s::beginners topic::deployments topic::replicasets src::session

---

<!-- note:1793724714420 model:Basic -->
**Front:** How does a Deployment manage pods internally — what is the role of its ReplicaSets?
**Back:** The Deployment controller creates one ReplicaSet per pod-template version — named <code>&lt;deployment&gt;-&lt;pod-template-hash&gt;</code>, and pods get a <code>pod-template-hash</code> label linking them. Each ReplicaSet does the actual pod-keeping; the Deployment orchestrates which ReplicaSet is scaled up or down and records each template version as a revision.
**Tags:** k8s::beginners topic::deployments topic::replicasets src::session

---

<!-- note:1793724714421 model:Basic -->
**Front:** Walk through what happens during a Deployment rolling update.
**Back:** A rolling update replaces pods gradually instead of all at once: when the pod template changes, the Deployment creates a new ReplicaSet and scales it up while scaling the old ReplicaSet down at the same time, until the new one holds all desired replicas and the old one is at 0 (kept for rollback). The app keeps serving throughout because old pods stay up while new ones come online.
**Tags:** k8s::beginners topic::deployments topic::rollouts src::session

---

<!-- note:1793724714422 model:Basic -->
**Front:** What do <code>maxSurge</code> and <code>maxUnavailable</code> control in a Deployment's rollingUpdate strategy?
**Back:** They throttle the rollout: <code>maxSurge</code> is how many pods ABOVE the desired count may exist during the update (extra new pods), <code>maxUnavailable</code> is how many pods may be unavailable during it. Both default to 25%. They also protect you — a broken rollout stalls instead of killing everything, since maxUnavailable limits how many old pods can go down.
**Tags:** k8s::beginners topic::deployments topic::rollouts src::session

---

<!-- note:1793724714423 model:Basic -->
**Front:** How does the <code>Recreate</code> deployment strategy differ from the default <code>RollingUpdate</code>?
**Back:** <code>spec.strategy.type: Recreate</code> kills ALL existing pods before creating the new version — simple but causes downtime. The default <code>RollingUpdate</code> replaces pods gradually (new ReplicaSet scaled up, old scaled down) so the app stays available. Use Recreate only when versions can't run side by side (e.g. single-writer stateful apps).
**Tags:** k8s::beginners topic::deployments topic::rollouts src::session

---

<!-- note:1793724714424 model:Basic -->
**Front:** How do you roll back a Deployment to a working version, and what actually happens?
**Back:** <code>kubectl rollout undo deployment/web</code> returns to the previous revision — the Deployment scales the old ReplicaSet back up and the new one down. <code>--to-revision=N</code> targets a specific revision from <code>kubectl rollout history</code>. Only the pod template is rolled back (replicas aren't). Old ReplicaSets are kept per <code>revisionHistoryLimit</code> (default 10).
**Tags:** k8s::beginners topic::deployments topic::rollouts src::session

---

<!-- note:1793724714425 model:Basic -->
**Front:** Which <code>kubectl rollout</code> subcommands manage a Deployment's lifecycle, and what does each do?
**Back:** <code>status</code> — watch rollout progress (e.g. stuck rollouts); <code>history</code> — list revisions; <code>pause</code>/<code>resume</code> — hold a rollout to batch several template fixes, then release; <code>restart</code> — start a fresh rollout of the same template (new pods); <code>undo</code> — roll back to a previous revision.
**Tags:** k8s::beginners topic::deployments topic::kubectl src::session

---

<!-- note:1793724714455 model:Basic (and reversed card) -->
**Front:** What is a Deployment in Kubernetes?
**Back:** A higher-level workload object that runs a set of identical pods (usually stateless apps) through ReplicaSets it owns, and provides declarative updates — rollouts between pod-template versions at a controlled rate, revision history, and rollback.
**Tags:** k8s::beginners topic::deployments topic::pods src::session

---

<!-- note:1793724714483 model:Cloze -->
**Text:** Update Deployment 'web' to a new image, then roll it back:<br><br><code>kubectl set image {{c1::deployment}}/web {{c2::nginx}}={{c3::nginx:1.16.1}}<br>kubectl rollout {{c4::undo}} deployment/web</code>
**Back Extra:** set image patches the pod template — which is what triggers a rolling update. rollout undo returns to the previous revision (old ReplicaSet scaled back up). Watch progress with kubectl rollout status.
**Tags:** k8s::beginners topic::deployments topic::kubectl src::session

---

<!-- note:1793724714559 model:Many -->
**Domain:** Deployments
**Question:** You update a Deployment's pod image from nginx:1.14 to nginx:1.16. With the default strategy, what does the Deployment controller do?
**Options:** A. It deletes all old pods, then creates the new ones<br>B. It creates a new ReplicaSet and scales it up while scaling the old one down<br>C. It edits the running pods' images in place<br>D. It creates a second Deployment alongside the first
**Answer:** B (2) – It creates a new ReplicaSet and scales it up while scaling the old one down
**Explanation:** RollingUpdate (the default strategy) spins up a new ReplicaSet for the changed pod template and gradually scales it to the desired count while scaling the old ReplicaSet to 0 — so the app never fully goes down. Deleting everything first is the Recreate strategy; the Deployment itself is never recreated.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/deployment/" target="_blank">Kubernetes Documentation - Deployments</a>
**Tags:** k8s::beginners topic::deployments topic::rollouts src::session

---

<!-- note:1793724714560 model:Many -->
**Domain:** Deployments
**Question:** Which change to a Deployment triggers a new rollout and creates a new revision?
**Options:** A. Changing spec.replicas from 3 to 6<br>B. Renaming the Deployment in metadata.name<br>C. Updating the container image in spec.template<br>D. Adding an annotation to the Deployment
**Answer:** C (3) – Updating the container image in spec.template
**Explanation:** A rollout (and a new revision) is triggered if and only if .spec.template changes — e.g. a new container image or template labels. Scaling replicas, renaming the Deployment, or changing spec.replicas only adjusts the current ReplicaSet's count; it does not roll out a new version.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/controllers/deployment/" target="_blank">Kubernetes Documentation - Deployments</a>
**Tags:** k8s::beginners topic::deployments topic::rollouts src::session

---

<!-- note:1793731963651 model:Basic (and reversed card) -->
**Front:** What is a revision in a Kubernetes Deployment?
**Back:** A numbered record of the Deployment's pod template at the moment a rollout was triggered — revision 1, 2, 3… increments each time <code>spec.template</code> changes (visible via <code>kubectl rollout history</code> and the <code>deployment.kubernetes.io/revision</code> annotation). Scaling does not bump it. Each revision corresponds to the old ReplicaSet you can roll back to with <code>--to-revision=N</code>.
**Tags:** k8s::beginners topic::deployments topic::rollouts src::session

---

<!-- note:1793731963674 model:Basic -->
**Front:** How do you record WHY a Deployment was changed so it shows up in its rollout history?
**Back:** Set the <code>kubernetes.io/change-cause</code> annotation — it's copied onto each new revision and shown in the CHANGE-CAUSE column of <code>kubectl rollout history</code>:<br><code>kubectl annotate deployment/web kubernetes.io/change-cause="bump to nginx:1.16"</code><br>(The old <code>--record</code> flag that did this automatically is deprecated.)
**Tags:** k8s::beginners topic::deployments topic::kubectl src::session

---
