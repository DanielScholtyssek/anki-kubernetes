# Kubernetes for Beginners — pods

> Deck: `Kubernetes for Beginners` · Group: `pods` · Notes: 10 · Models: Basic, Basic (and reversed card), Many

<!-- note:1793657487165 model:Basic (and reversed card) -->
**Front:** What is a pod in Kubernetes?
**Back:** The smallest deployable object in Kubernetes. A pod encapsulates one or more containers and represents a single instance of an application — Kubernetes deploys, schedules and scales pods, not bare containers.
**Tags:** k8s::beginners topic::pods src::session

---

<!-- note:1793657487179 model:Basic -->
**Front:** Why does Kubernetes wrap containers in pods instead of deploying bare containers?
**Back:** The pod is the unit Kubernetes schedules and manages: it gives its container(s) a shared environment — one IP address and network namespace plus shared storage volumes — so the runtime treats them as one application instance.
**Tags:** k8s::beginners topic::pods src::session

---

<!-- note:1793657487180 model:Basic -->
**Front:** How does Kubernetes scale an application up and down at the pod level?
**Back:** Under more load Kubernetes creates additional pods — extra instances of the same application — which the scheduler can place on other nodes in the cluster. Scaling down means removing pods again.
**Tags:** k8s::beginners topic::pods src::session

---

<!-- note:1793657487181 model:Basic -->
**Front:** Can a pod contain more than one container, and when would you do that?
**Back:** Yes — but usually different containers, not copies of the same one. A common pattern is a main application container plus helper 'sidecar' containers that support it (e.g. a log shipper or proxy).
**Tags:** k8s::beginners topic::pods src::session

---

<!-- note:1793657487182 model:Basic -->
**Front:** How can containers inside the same pod communicate with each other?
**Back:** They share the same network namespace and IP address, so they can talk to each other over localhost. They can also exchange data through volumes shared inside the pod.
**Tags:** k8s::beginners topic::pods src::session

---

<!-- note:1793657487183 model:Basic -->
**Front:** Which kubectl command creates a pod running nginx?
**Back:** kubectl run nginx --image=nginx — creates a pod named 'nginx' that runs a container built from the 'nginx' image.
**Tags:** k8s::beginners topic::pods src::session

---

<!-- note:1793657487184 model:Basic -->
**Front:** Where does the image in `kubectl run nginx --image=nginx` come from?
**Back:** From a container image registry — Docker Hub by default (short names like 'nginx' resolve to Docker Hub's official library). To use a private registry, specify its full path, e.g. --image=registry.example.com/app:tag.
**Tags:** k8s::beginners topic::pods src::session

---

<!-- note:1793657487185 model:Basic -->
**Front:** How do you list pods in a cluster, and what are useful variants of the command?
**Back:** kubectl get pods lists pods and their status. Useful variants: kubectl get pods -o wide (pod IPs and which node each runs on), kubectl get pods -A (all namespaces), kubectl get pods -w (watch for changes), kubectl describe pod <name> (full details and events).
**Tags:** k8s::beginners topic::pods src::session

---

<!-- note:1793657487186 model:Basic -->
**Front:** How can a user access an application running inside a pod (e.g. the nginx container)?
**Back:** A pod only gets a cluster-internal IP, so it cannot be reached from outside directly. For a quick test use kubectl port-forward pod/nginx 8080:80 and browse to localhost:8080; for real access you expose the pod through a Service (e.g. type NodePort or LoadBalancer).
**Tags:** k8s::beginners topic::pods src::session

---

<!-- note:1793657487192 model:Many -->
**Domain:** Pods
**Question:** Which command creates a pod named 'nginx' running the nginx image?
**Options:** A. kubectl create pod nginx<br>B. kubectl run nginx --image=nginx<br>C. kubectl deploy nginx --image=nginx<br>D. kubectl start nginx --image=nginx
**Answer:** B (2) – kubectl run nginx --image=nginx
**Explanation:** kubectl run creates a single pod; --image tells the runtime which image to pull (Docker Hub by default). kubectl create/deploy/start alone do not produce a running pod this way — deployments are created with kubectl create deployment.
**Sources:** <a href="https://kubernetes.io/docs/concepts/workloads/pods/" target="_blank">Kubernetes Documentation - Pods</a>
**Tags:** k8s::beginners topic::pods src::session

---
