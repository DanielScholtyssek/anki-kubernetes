# Kubernetes for Beginners — container-orchestration

> Deck: `Kubernetes for Beginners` · Group: `container-orchestration` · Notes: 7 · Models: Basic, Basic (and reversed card), Cloze, Many

<!-- note:1793642944091 model:Basic (and reversed card) -->
**Front:** What is container orchestration?
**Back:** The automated management of containers at scale: a platform handles the connectivity between containers (e.g. an app container reaching its database container) and automatically scales the number of container instances up or down based on load.
**Tags:** k8s::beginners topic::container-orchestration src::session

---

<!-- note:1793642944081 model:Basic -->
**Front:** What problem does container orchestration solve for multi-container applications?
**Back:** When an application relies on other containers (web app + database + cache), every container must find and reach the others, stay running, and be restarted or replaced on failure — potentially across many hosts. Managing that by hand does not scale; an orchestration platform automates connectivity and lifecycle for all containers.
**Tags:** k8s::beginners topic::container-orchestration src::session

---

<!-- note:1793642944103 model:Cloze -->
**Text:** {{c1::Kubernetes}} is the most widely used container orchestration platform.
**Back Extra:** Other examples: Docker Swarm, Amazon ECS, Apache Mesos.
**Tags:** k8s::beginners topic::container-orchestration src::session

---

<!-- note:1793642944082 model:Basic -->
**Front:** How does a container orchestration platform scale an application?
**Back:** It runs additional instances (replicas) of the application's containers, spreads them across nodes, and removes them again when load drops. If the cluster itself is too small or too large, the platform can also scale the number of nodes up or down.
**Tags:** k8s::beginners topic::container-orchestration src::session

---

<!-- note:1793642944083 model:Basic -->
**Front:** How does container orchestration make an application highly available?
**Back:** Container instances are spread across multiple nodes, so a hardware or node failure only takes down the instances on that node — the application keeps running on the remaining instances. Incoming traffic is load-balanced across the healthy instances.
**Tags:** k8s::beginners topic::container-orchestration src::session

---

<!-- note:1793642944084 model:Basic -->
**Front:** How are applications typically defined on a container orchestration platform?
**Back:** Declaratively: you write YAML files describing the desired state — which containers to run, how many replicas, how they are connected — and the platform continuously works to make the actual state match.
**Tags:** k8s::beginners topic::container-orchestration src::session

---

<!-- note:1793642944124 model:Many -->
**Domain:** Container Orchestration
**Question:** What does a container orchestration platform like Kubernetes primarily automate?
**Options:** A. Building container images from Dockerfiles<br>B. Coordinating containers across many hosts — connectivity, scaling, and failover<br>C. Isolating each container's processes using namespaces and cgroups<br>D. Packaging an application and its dependencies into a runnable image
**Answer:** B (2) – Coordinating containers across many hosts — connectivity, scaling, and failover
**Explanation:** Image building and packaging (A, D) happen at the container/image level, and namespace/cgroup isolation (C) is the kernel mechanism containers themselves use. Orchestration sits above that: it decides where containers run, how they reach each other, how many run, and replaces them when they fail.
**Sources:** <a href="https://kubernetes.io/docs/concepts/overview/" target="_blank">Kubernetes Documentation - Overview</a>
**Tags:** k8s::beginners topic::container-orchestration src::session

---
