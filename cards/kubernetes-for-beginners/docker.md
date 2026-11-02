# Kubernetes for Beginners — docker

> Deck: `Kubernetes for Beginners` · Group: `docker` · Notes: 7 · Models: Basic, Many

<!-- note:1793641450383 model:Basic -->
**Front:** What is the 'matrix from hell' problem in application deployment?
**Back:** For applications built from multiple services (e.g. a web server, a database, Redis), every service's libraries and dependencies must be checked for compatibility with the target OS and the underlying hardware/infrastructure. The number of environment combinations that must be verified explodes — that is the 'matrix from hell'.
**Tags:** k8s::beginners topic::docker src::session

---

<!-- note:1793641450384 model:Basic -->
**Front:** Why is onboarding new developers slow without containers?
**Back:** Every developer must set up each service manually on their own machine: follow long READMEs, install the correct library/dependency versions for their OS, and debug environment-specific issues. The compatibility matrix has to be re-solved per machine and per OS.
**Tags:** k8s::beginners topic::docker src::session

---

<!-- note:1793641450385 model:Basic -->
**Front:** How does Docker solve the matrix-from-hell compatibility problem?
**Back:** Each application runs in its own container, packaged with its own dependencies and libraries. Services share the same VM and OS, but run in isolated environments — so conflicting dependency sets no longer clash, and any machine that runs Docker runs the app identically.
**Tags:** k8s::beginners topic::docker src::session

---

<!-- note:1793641726300 model:Basic -->
**Front:** What is a container?
**Back:** A completely isolated environment that runs its own processes or services and has its own network interfaces and filesystem mounts — while sharing the host machine's OS kernel with all other containers.
**Tags:** k8s::beginners topic::docker src::session

---

<!-- note:1793641991093 model:Basic -->
**Front:** What is the main purpose of Docker?
**Back:** To package and containerize applications so they can be shipped and run anywhere, anytime, as many times as you want.
**Tags:** k8s::beginners topic::docker src::session

---

<!-- note:1793642079137 model:Many -->
**Domain:** Docker
**Question:** Which stack correctly describes how containers run compared to virtual machines?
**Options:** A. HW → OS → Hypervisor → virtual machines that share the host kernel<br>B. HW → OS → Docker Engine → containers that share the host OS kernel<br>C. HW → OS → Docker Engine → containers each running their own guest OS kernel<br>D. HW → Hypervisor → Docker Engine → containers with isolated guest OSes
**Answer:** B (2) – HW → OS → Docker Engine → containers that share the host OS kernel
**Explanation:** Virtual machines sit on a hypervisor and each boots a full guest OS with its own kernel — heavyweight and slow to start. Containers need no guest OS: the Docker engine uses the host kernel (namespaces/cgroups) to give each container its own isolated processes, networking and filesystems on the same machine — much lighter and faster.
**Sources:** <a href="https://docs.docker.com/get-started/docker-overview/" target="_blank">Docker Official Documentation - Docker Overview</a>
**Tags:** k8s::beginners topic::docker src::session

---

<!-- note:1793642370997 model:Basic -->
**Front:** What is the difference between a container and an image?
**Back:** An image is a package — a read-only template containing the application and everything it needs to run. It is the blueprint used to create one or more containers. A container is a running instance of an image: the isolated environment with its own processes, network interfaces and filesystem.
**Tags:** k8s::beginners topic::docker src::session

---
