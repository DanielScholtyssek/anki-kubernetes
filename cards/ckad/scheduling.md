# CKAD - Certified Kubernetes Application Developer — scheduling

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `scheduling` · Notes: 19 · Models: Basic++++

<!-- note:1781279834359 model:Basic++++ -->
**Front:** What is scheduling in Kubernetes?
**Back:** Choosing a node for a Pod based on resources, selectors, affinity, taints/tolerations, and other constraints.
**Tags:** ckad::scheduling concept

---

<!-- note:1781279834360 model:Basic++++ -->
**Front:** What is nodeSelector?
**Back:** A simple Pod scheduling constraint requiring a node to have matching labels.
**Tags:** ckad::scheduling concept nodeselector

---

<!-- note:1781279834361 model:Basic++++ -->
**Front:** Command: label node with disk=ssd.
**Back:** kubectl label node &lt;node-name&gt; disk=ssd
**Tags:** ckad::scheduling command labels

---

<!-- note:1781279834362 model:Basic++++ -->
**Front:** YAML: schedule Pod onto nodes labelled disk=ssd.
**Back:** spec:<br>  nodeSelector:<br>    disk: ssd
**Tags:** ckad::scheduling nodeselector yaml

---

<!-- note:1781279834363 model:Basic++++ -->
**Front:** What is node affinity?
**Back:** A more expressive scheduling rule than nodeSelector, using matchExpressions and required/preferred rules.
**Tags:** affinity ckad::scheduling concept

---

<!-- note:1781279834364 model:Basic++++ -->
**Front:** YAML: required node affinity for disk in ssd.
**Back:** affinity:<br>  nodeAffinity:<br>    requiredDuringSchedulingIgnoredDuringExecution:<br>      nodeSelectorTerms:<br>      - matchExpressions:<br>        - key: disk<br>          operator: In<br>          values: ["ssd"]
**Tags:** affinity ckad::scheduling yaml

---

<!-- note:1781279834365 model:Basic++++ -->
**Front:** What does requiredDuringSchedulingIgnoredDuringExecution mean?
**Back:** The rule must be satisfied at scheduling time, but if node labels change later, the Pod is not evicted just because the rule no longer matches.
**Tags:** affinity ckad::scheduling concept

---

<!-- note:1781279834366 model:Basic++++ -->
**Front:** What is preferred node affinity?
**Back:** A soft preference; scheduler tries to satisfy it but may still schedule elsewhere.
**Tags:** affinity ckad::scheduling concept

---

<!-- note:1781279834367 model:Basic++++ -->
**Front:** What is Pod anti-affinity used for?
**Back:** Spreading Pods apart from other Pods with matching labels, often to avoid placing replicas on the same node/zone.
**Tags:** affinity ckad::scheduling concept

---

<!-- note:1781279834368 model:Basic++++ -->
**Front:** YAML: basic podAntiAffinity required against app=web on same hostname.
**Back:** affinity:<br>  podAntiAffinity:<br>    requiredDuringSchedulingIgnoredDuringExecution:<br>    - labelSelector:<br>        matchLabels:<br>          app: web<br>      topologyKey: kubernetes.io/hostname
**Tags:** affinity ckad::scheduling yaml

---

<!-- note:1781279834369 model:Basic++++ -->
**Front:** What is a taint?
**Back:** A node property that repels Pods unless they have a matching toleration.
**Tags:** ckad::scheduling concept taints

---

<!-- note:1781279834370 model:Basic++++ -->
**Front:** What is a toleration?
**Back:** A Pod setting that allows scheduling onto nodes with matching taints.
**Tags:** ckad::scheduling concept tolerations

---

<!-- note:1781279834371 model:Basic++++ -->
**Front:** Command: taint node dedicated=gpu:NoSchedule.
**Back:** kubectl taint node &lt;node&gt; dedicated=gpu:NoSchedule
**Tags:** ckad::scheduling command taints

---

<!-- note:1781279834372 model:Basic++++ -->
**Front:** Command: remove taint dedicated=gpu:NoSchedule from node.
**Back:** kubectl taint node &lt;node&gt; dedicated=gpu:NoSchedule-
**Tags:** ckad::scheduling command taints

---

<!-- note:1781279834373 model:Basic++++ -->
**Front:** YAML: toleration for dedicated=gpu:NoSchedule.
**Back:** tolerations:<br>- key: dedicated<br>  operator: Equal<br>  value: gpu<br>  effect: NoSchedule
**Tags:** ckad::scheduling tolerations yaml

---

<!-- note:1781279834374 model:Basic++++ -->
**Front:** What does NoSchedule taint effect mean?
**Back:** New Pods without matching toleration will not be scheduled there; existing Pods are not evicted.
**Tags:** ckad::scheduling concept taints

---

<!-- note:1781279834375 model:Basic++++ -->
**Front:** What does NoExecute taint effect mean?
**Back:** Pods without matching toleration are evicted, and new Pods cannot schedule there.
**Tags:** ckad::scheduling concept taints

---

<!-- note:1781279834376 model:Basic++++ -->
**Front:** What does PreferNoSchedule taint effect mean?
**Back:** Scheduler tries to avoid the node but may schedule there if needed.
**Tags:** ckad::scheduling concept taints

---

<!-- note:1781279834377 model:Basic++++ -->
**Front:** What should you inspect for a Pending Pod with scheduling issues?
**Back:** kubectl describe pod, events, node labels, taints, resource requests, PVC status, and namespace quota.
**Tags:** ckad::scheduling debugging

---
