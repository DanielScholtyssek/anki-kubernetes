# KCNA - Kubernetes and Cloud Native Associate — Cloud Native Application Delivery

> Deck: `KCNA - Kubernetes and Cloud Native Associate` · Group: `Cloud Native Application Delivery` · Notes: 14 · Models: Many

<!-- note:1793915795947 model:Many -->
**Domain:** Helm - values
**Question:** Which Helm option overrides chart values from the command line?
**Options:** A. <code>--values</code><br>B. <code>--namespace</code><br>C. <code>--kubeconfig</code><br>D. <code>--set</code>
**Answer:** D – <code>--set</code> key=value overrides Helm values inline
**Explanation:** <code>--set</code> overrides individual chart values inline as key=value pairs — repeatable and comma-separable (<code>helm install web ./chart --set image.tag=2.0 --set replicas=3</code>). Precedence: <code>--set</code> beats -f/<code>--values</code> files, which beat the chart's values.yaml defaults. The distractors do unrelated things: <code>--values</code>/-f supplies a whole YAML file of overrides (not inline), <code>--namespace</code> picks the install namespace, <code>--kubeconfig</code> points at a cluster credentials file. For strings that look like numbers or file-sourced values there are <code>--set-string</code> and <code>--set-file</code>.
**Sources:** <a href="https://helm.sh/docs/intro/using_helm/" target="_blank">Helm Docs - Using Helm</a>
**Tags:** k8s::kcna src::session topic::helm topic::packaging

---

<!-- note:1793919187035 model:Many -->
**Domain:** Helm - install flags
**Question:** What is the purpose of Helm's --atomic flag?
**Options:** A. Dry-run only<br>B. Roll back automatically on failure<br>C. Create CRDs<br>D. Render templates only
**Answer:** B (2) – roll back automatically on failure
**Explanation:** --atomic makes helm install/upgrade all-or-nothing: if any resource fails to become ready, Helm rolls the release back to its previous revision instead of leaving a half-installed release behind. It builds on --wait (Helm waits for readiness) plus automatic rollback — without it a failed upgrade can strand the cluster in a mixed old/new state. The distractors describe other flags: --dry-run only renders templates client-side without touching the cluster, and CRDs come from the chart's crds/ directory (installed before templates, never templated).
**Sources:** <a href="https://helm.sh/docs/intro/using_helm/" target="_blank">Helm Docs - Using Helm</a>
**Tags:** k8s::kcna src::session topic::helm topic::packaging

---

<!-- note:1794080037260 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** Which principle is central to the GitOps methodology for application and infrastructure deployment?
**Options:** A. Using imperative scripts stored in Git<br>B. Managing only stateless applications via Git<br>C. Treating Git as the single source of truth for desired state<br>D. Requiring manual approval for all Git commits<br>E. Using Git LFS for storing container images
**Answer:** C – Treating Git as the single source of truth for desired state
**Explanation:** GitOps emphasizes a declarative approach where the entire<br>desired state of the system (applications, infrastructure) is described in<br>Git, and an automated process ensures the live environment converges to<br>this state.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037261 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** In a CI/CD pipeline for a cloud native application, what is the typical output of the "Continuous Integration" (CI) phase?
**Options:** A. A running application in production<br>B. A new Kubernetes cluster provisioned<br>C. A tested and versioned container image/artifact<br>D. A detailed cost analysis report<br>E. A set of user stories for the next sprint
**Answer:** C – A tested and versioned container image/artifact
**Explanation:** The CI phase focuses on building the application, running automated tests, and producing a reliable, versioned artifact (often<br>a container image) that is ready for deployment.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037262 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** What is the <b>primary </b>benefit of implementing CI/CD pipelines for application delivery?
**Options:** A. It eliminates the need for testing<br>B. It reduces infrastructure costs significantly<br>C. It enables faster, more reliable software releases<br>D. It automatically writes application code<br>E. It replaces the need for version control systems
**Answer:** C – It enables faster, more reliable software releases
**Explanation:** Explanation: CI/CD automates the build, test, and deployment processes, leading to increased release velocity, improved code quality through<br>automated testing, and more consistent deployments.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037263 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** What is a key advantage of using GitOps for managing Kubernetes deployments compared to traditional CI/CD push-based deployments?
**Options:** A. GitOps pipelines are significantly faster to execute.<br>B. GitOps eliminates the need for container registries.<br>C. GitOps enhances security by reducing direct cluster access for CI.<br>D. GitOps does not require YAML manifests for resources.<br>E. GitOps is only suitable for small-scale deployments.
**Answer:** C – GitOps enhances security by reducing direct cluster access for CI.
**Explanation:** In GitOps, the CI system typically pushes an image to a<br>registry and updates a Git repo. An agent inside the cluster pulls changes<br>from Git, reducing the CI system’s need for direct cluster credentials and<br>providing a stronger security posture.<br>Domain: Cloud
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037264 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** Which of these is a core component of a "Continuous Delivery" pipeline but <b>NOT </b>necessarily "Continuous Deployment"?
**Options:** A. Automated building of code into an artifact.<br>B. Automated execution of unit and integration tests.<br>C. Automated deployment to a staging/QA environment.<br>D. Automated deployment to the production environment.<br>E. Manual approval gate before production deployment.
**Answer:** E – Manual approval gate before production deployment.
**Explanation:** Continuous Delivery ensures every validated change is releasable to production, often with a manual approval step. Continuous<br>Deployment automates the release to production without manual intervention if all prior stages pass. Both include A, B, C.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037265 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** What is the practice of using Git repositories as the single source of truth for defining and managing infrastructure and applications?
**Options:** A. CI/CD<br>B. DevOps<br>C. GitOps<br>D. Infrastructure as Code (IaC)
**Answer:** C – GitOps
**Explanation:** GitOps leverages Git’s features (versioning, history, PRs) to manage infrastructure and application deployment declaratively.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037266 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** Which core principle differentiates GitOps from general Infrastructure as Code (IaC)?
**Options:** A. Using code for infra config<br>B. Automating infrastructure tests<br>C. Using Git as the source of truth<br>D. Manual deployment approval
**Answer:** C – Using Git as the source of truth
**Explanation:** While IaC uses code, GitOps specifically mandates Git as the declarative source of truth and uses agents to enforce that state.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037267 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** What does ”CI” stand for in the context of application delivery?
**Options:** A. Continuous Integration<br>B. Cluster Infrastructure<br>C. Container Interface<br>D. Cloud Instance
**Answer:** A – Continuous Integration
**Explanation:** Continuous Integration involves frequently merging code changes into a central repository, followed by automated builds and tests.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037268 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** What does ”CD” stand for in CI/CD?
**Options:** A. Container Deployment<br>B. Continuous Delivery/Deployment<br>C. Cluster Discovery<br>D. Centralized Dashboard
**Answer:** B – Continuous Delivery/Deployment
**Explanation:** Continuous Delivery ensures code changes can be released quickly, while Continuous Deployment automatically deploys them to production.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037269 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** Which stage in a typical CI/CD pipeline for Kubernetes usually involves creating a container image?
**Options:** A. Testing<br>B. Building<br>C. Deployment<br>D. Monitoring
**Answer:** B – Building
**Explanation:** The build stage compiles code (if necessary) and packages the application and its dependencies into a container image (e.g., Docker).
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037270 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** Which tool is commonly used in CI/CD pipelines to automate the build, test, and deployment processes?
**Options:** A. Kubernetes<br>B. Docker<br>C. Jenkins / GitLab CI / GitHub Actions<br>D. Prometheus
**Answer:** C – Jenkins / GitLab CI / GitHub Actions
**Explanation:** Tools like Jenkins, GitLab CI, GitHub Actions, Argo CD, Flux etc., orchestrate the steps within a CI/CD pipeline.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---

<!-- note:1794080037271 model:Many -->
**Domain:** KCNA - Cloud Native Application Delivery
**Question:** What is <b>the primary goal</b> of Application Delivery in a cloud native context?
**Options:** A. To secure the cluster<br>B. To monitor resource usage<br>C. To reliably deploy manage apps<br>D. To provision infrastructure
**Answer:** C – To reliably deploy manage apps
**Explanation:** Application delivery focuses on the processes and tools used to get applications running reliably and efficiently in the environment.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::delivery topic::mcq

---
