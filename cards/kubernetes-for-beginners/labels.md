# Kubernetes for Beginners — labels

> Deck: `Kubernetes for Beginners` · Group: `labels` · Notes: 5 · Models: Basic, Basic (and reversed card), Many

<!-- note:1793722394258 model:Basic -->
**Front:** What does a label selector do in Kubernetes, and why is it important?
**Back:** A selector is a query over labels that picks out a set of objects — it is Kubernetes' core grouping primitive. It's how loosely coupled pieces find each other: a Service uses a selector to pick the pods it load-balances traffic to, a ReplicaSet uses one to count the pods it must keep alive, and <code>kubectl get -l</code> filters objects the same way.
**Tags:** k8s::beginners topic::labels topic::selectors src::session

---

<!-- note:1793722394259 model:Basic -->
**Front:** How does a ReplicaSet use labels and selectors to know which pods it manages?
**Back:** <code>spec.selector.matchLabels</code> is a label query — every pod carrying those labels counts toward <code>spec.replicas</code>, whether the ReplicaSet created it from its template or adopted an existing matching pod. Removing a matching label from a pod takes it out of the set, and the ReplicaSet immediately creates a replacement to restore the count.
**Tags:** k8s::beginners topic::labels topic::replicasets topic::selectors src::session

---

<!-- note:1793722394278 model:Basic (and reversed card) -->
**Front:** What is a label in Kubernetes?
**Back:** A key/value pair attached to an object in <code>metadata.labels</code> (e.g. <code>tier: frontend</code>, <code>environment: production</code>). Labels mark attributes meaningful to you — Kubernetes doesn't interpret them — and they let you group and select subsets of objects.
**Tags:** k8s::beginners topic::labels topic::pods src::session

---

<!-- note:1793722394279 model:Basic (and reversed card) -->
**Front:** What are the two kinds of label selectors in Kubernetes?
**Back:** Equality-based (<code>=</code>, <code>==</code>, <code>!=</code> — e.g. <code>environment=production</code>, <code>tier!=frontend</code>) and set-based (<code>in</code>, <code>notin</code>, <code>exists</code> — e.g. <code>environment in (production, qa)</code>). Multiple requirements are comma-separated and ANDed; there is no OR. ReplicaSets support set-based selectors via <code>matchExpressions</code> — the legacy ReplicationController only had equality-based.
**Tags:** k8s::beginners topic::labels topic::selectors src::session

---

<!-- note:1793722402525 model:Many -->
**Domain:** Labels & Selectors
**Question:** A pod has labels <code>tier=frontend</code> and <code>environment=prod</code>. Which selector matches it?
**Options:** A. tier=backend<br>B. environment in (dev, staging)<br>C. tier in (frontend, cache)<br>D. !tier
**Answer:** C (3) – tier in (frontend, cache)
**Explanation:** in/notin/exists are set-based operators: tier in (frontend, cache) matches because the pod's tier value 'frontend' is in the set. tier=backend and environment in (dev, staging) fail equality/membership; !tier selects objects that do NOT have the tier key at all. Multiple comma-separated requirements would be ANDed.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/" target="_blank">Kubernetes Documentation - Labels and Selectors</a>
**Tags:** k8s::beginners topic::labels topic::selectors src::session

---
