# Kubernetes for Beginners — cri-oci

> Deck: `Kubernetes for Beginners` · Group: `cri-oci` · Notes: 7 · Models: Basic, Basic (and reversed card), Many

<!-- note:1793644385394 model:Basic (and reversed card) -->
**Front:** What is the Container Runtime Interface (CRI)?
**Back:** The standard plugin interface between the kubelet and container runtimes. Any runtime implementing CRI can run containers under Kubernetes, so runtimes can be swapped (e.g. containerd, CRI-O) without changing Kubernetes itself. The runtimes in turn follow OCI standards.
**Tags:** k8s::beginners topic::cri-oci src::session

---

<!-- note:1793644385395 model:Basic (and reversed card) -->
**Front:** What is OCI and what does it stand for?
**Back:** OCI stands for Open Container Initiative — a Linux Foundation body that publishes open standards for containers, mainly the image-spec (image format) and the runtime-spec (how to run a container). It keeps images and runtimes from different vendors compatible.
**Tags:** k8s::beginners topic::cri-oci src::session

---

<!-- note:1793644385396 model:Basic (and reversed card) -->
**Front:** What does the OCI image specification (image-spec) define?
**Back:** It defines the format of a container image: the manifest, the image configuration, and the filesystem layers — i.e. how an image is packaged and shared so that any OCI-compliant runtime can run it.
**Tags:** k8s::beginners topic::cri-oci src::session

---

<!-- note:1793644385397 model:Basic (and reversed card) -->
**Front:** What does the OCI runtime specification (runtime-spec) define?
**Back:** It defines how to run a container from a filesystem bundle: the container's configuration (namespaces, cgroups, mounts) and its lifecycle (create, start, stop, delete). runc is the reference implementation.
**Tags:** k8s::beginners topic::cri-oci src::session

---

<!-- note:1793644385405 model:Basic -->
**Front:** Why can an image built by Docker run on other runtimes like containerd?
**Back:** Because both adhere to OCI standards: the image follows the image-spec format, and any runtime following the runtime-spec knows how to run it. This is what makes container images portable across different tools and runtimes.
**Tags:** k8s::beginners topic::cri-oci src::session

---

<!-- note:1793644385458 model:Many -->
**Domain:** Container Runtime
**Question:** Which interface must a container runtime implement so that the kubelet can use it interchangeably with other runtimes?
**Options:** A. OCI image-spec<br>B. OCI runtime-spec<br>C. Container Runtime Interface (CRI)<br>D. dockershim
**Answer:** C (3) – Container Runtime Interface (CRI)
**Explanation:** The OCI image-spec and runtime-spec standardize the image format and how a container is run — they are rules a runtime follows, not an interface k8s calls. CRI is the actual gRPC interface the kubelet uses to talk to the runtime, which is what makes runtimes swappable.
**Sources:** <a href="https://kubernetes.io/docs/concepts/architecture/cri/" target="_blank">Kubernetes Documentation - Container Runtime Interface (CRI)</a>
**Tags:** k8s::beginners topic::cri-oci src::session

---

<!-- note:1793644385459 model:Many -->
**Domain:** Container Runtime
**Question:** Which OCI specification defines the format of a container image — its manifest, configuration, and filesystem layers?
**Options:** A. image-spec<br>B. runtime-spec<br>C. CRI<br>D. distribution-spec
**Answer:** A (1) – image-spec
**Explanation:** image-spec covers the packaging side — manifest, config, filesystem layers. runtime-spec covers the running side — container config and lifecycle. CRI is the kubelet interface, and distribution-spec covers pushing/pulling images to a registry.
**Sources:** <a href="https://opencontainers.org/" target="_blank">Open Container Initiative</a>
**Tags:** k8s::beginners topic::cri-oci src::session

---
