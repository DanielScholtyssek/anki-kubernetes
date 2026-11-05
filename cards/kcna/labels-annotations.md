<!-- note:1793808319432 model:Many -->
**Domain:** Labels - multi-criteria
**Question:** What does <code>kubectl get pods -l 'app=web,env=prod'</code> return?
**Options:** A. Pods matching ANY of the criteria<br>B. Only pods matching ALL criteria — multiple -l requirements are ANDed<br>C. Pods matching the first criterion only<br>D. Pods in the 'prod' namespace labelled web
**Answer:** B (2) – only pods matching ALL criteria — multiple -l requirements are ANDed
**Explanation:** Comma-separated selector requirements must ALL be satisfied — it's an AND, not OR. Equality selectors match exact values (app=web, env!=dev); set-based selectors match membership (env in (prod,qa), tier notin (cache), !key = absence). Everything from kubectl -l to NetworkPolicy podSelector uses the same requirement logic.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/" target="_blank">Kubernetes Documentation - Labels and Selectors</a>
**Tags:** k8s::kcna topic::kubectl topic::labels src::session

---

<!-- note:1793808319433 model:Many -->
**Domain:** Labels - manifest placement
**Question:** Where in a pod/Deployment manifest do an object's OWN labels always go?
**Options:** A. spec.labels<br>B. spec.selector.labels<br>C. metadata.labels<br>D. status.labels
**Answer:** C (3) – metadata.labels — the object's own label set
**Explanation:** Labels always go under metadata.labels on the object itself: metadata: {labels: {app: web, tier: frontend}}. The consumers live elsewhere in OTHER objects' specs: Service spec.selector, ReplicaSet/Deployment spec.selector.matchLabels, NetworkPolicy podSelector. 'Label everything, select from outside' is the pattern.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/" target="_blank">Kubernetes Documentation - Labels and Selectors</a>
**Tags:** k8s::kcna topic::labels topic::yaml src::session

---

<!-- note:1793808323513 model:Cloze -->
**Text:** List only pods labelled <code>app=web</code>:<br><br><code>kubectl get pods {{c1::-l}} {{c2::app=web}}</code><br><br>(<code>-l</code> is short for <code>{{c3::--selector}}</code>)
**Back Extra:** The flag works on most list commands (get pods, get svc, get all, delete). Multiple requirements AND together: -l 'app=web,env=prod'. Set-based form: -l 'env in (prod,qa)'. Combine with --show-labels to see each object's full label set.
**Tags:** k8s::kcna topic::kubectl topic::labels src::session

---

<!-- note:1793808319514 model:Basic (and reversed card) -->
**Front:** Labels vs selectors — which side does what?
**Back:** Labels are key-value pairs ATTACHED to objects under <code>metadata.labels</code> — the grouping side (tag by app, tier, env, version…). Selectors are QUERIES that filter objects by their labels — the selection side (<code>kubectl -l</code>, Service <code>spec.selector</code>, ReplicaSet <code>matchLabels</code>, NetworkPolicy). Labels tag things; selectors find them.
**Tags:** k8s::kcna topic::api topic::labels src::session

---

<!-- note:1793808422503 model:Many -->
**Domain:** Annotations - purpose
**Question:** You want to record build version, release notes and owner contact on Deployments — purely for humans and tooling to READ, never to filter on. What should you attach?
**Options:** A. Labels — key-value pairs under metadata.labels<br>B. Annotations — informational metadata not meant for selecting objects<br>C. ConfigMaps — dedicated configuration storage<br>D. Environment variables on the container spec
**Answer:** B (2) – annotations — informational metadata not meant for selecting objects
**Explanation:** Annotations record non-identifying, informational metadata — build versions, release notes, owner/contact info, doc links, tool config. Labels would technically hold short strings too, but labels exist to be SELECTED on (Services, ReplicaSets, -l flags). Rule of thumb: if controllers need to filter on it → label; if humans/tools just need to read it → annotation.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/" target="_blank">Kubernetes Documentation - Annotations</a>
**Tags:** k8s::kcna topic::annotations topic::labels src::session

---

<!-- note:1793808422504 model:Many -->
**Domain:** Annotations - limitations
**Question:** Which statement about annotations is TRUE?
**Options:** A. They can be selected with kubectl get -l just like labels<br>B. They're required on every object<br>C. They cannot be used in selectors — no -l flag or matchExpressions can filter on annotations<br>D. They can only hold values under 63 characters like labels
**Answer:** C (3) – they cannot be used in selectors — no -l flag or matchExpressions can filter on annotations
**Explanation:** The annotation API has no selector mechanism: kubectl -l doesn't see them, spec.selector/matchExpressions ignore them, Services can't pick pods by them. They're write-and-read metadata only (get -o yaml / describe shows them). Also unlike labels they aren't size-constrained the same way — they can hold larger structured blobs (that's how last-applied fits a whole manifest).
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/" target="_blank">Kubernetes Documentation - Annotations</a>
**Tags:** k8s::kcna topic::annotations topic::api src::session

---

<!-- note:1793808422514 model:Basic (and reversed card) -->
**Front:** What are annotations in Kubernetes — and a few typical examples?
**Back:** Key-value string metadata for informational purposes — recording details that identify nothing and select nothing: build/release version, git commit, owner contact, docs links, or config for tools and controllers (e.g. <code>kubectl.kubernetes.io/last-applied-configuration</code>, Prometheus <code>scrape</code> hints). They live under <code>metadata.annotations</code>, beside <code>metadata.labels</code>.
**Tags:** k8s::kcna topic::annotations topic::api src::session

---

<!-- note:1793808422523 model:Cloze -->
**Text:** Record a build version on a pod imperatively:<br><br><code>kubectl {{c1::annotate}} pod web {{c2::build-version}}={{c3::v1.4.2}}</code>
**Back Extra:** Same shape as kubectl label: <resource> <name> <key>=<value>. Re-running with an existing key fails unless you add --overwrite. Remove with a trailing minus: kubectl annotate pod web build-version-. In YAML the same data sits under metadata.annotations.
**Tags:** k8s::kcna topic::annotations topic::kubectl src::session

---

