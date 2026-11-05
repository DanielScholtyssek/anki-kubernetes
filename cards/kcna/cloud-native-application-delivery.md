# KCNA - Kubernetes and Cloud Native Associate — Cloud Native Application Delivery

> Deck: `KCNA - Kubernetes and Cloud Native Associate` · Group: `Cloud Native Application Delivery` · Notes: 12 · Models: Basic++

<!-- note:1755881628517 model:Basic++ -->
**Front:** Which principle is central to the GitOps methodology for application and infrastructure deployment?<div>&nbsp;
<br>A. Using imperative scripts stored in Git
<br>B. Managing only stateless applications via Git
<br>C. Treating Git as the single source of truth for desired state
<br>D. Requiring manual approval for all Git commits
<br>E. Using Git LFS for storing container images</div>
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: GitOps emphasizes a declarative approach where the entire
desired state of the system (applications, infrastructure) is described in
Git, and an automated process ensures the live environment converges to
this state.

---

<!-- note:1755881687043 model:Basic++ -->
**Front:** In a CI/CD pipeline for a cloud native application, what is the
typical output of the "Continuous Integration" (CI) phase?
<br><br>A. A running application in production
<br>B. A new Kubernetes cluster provisioned
<br>C. A tested and versioned container image/artifact
<br>D. A detailed cost analysis report
<br>E. A set of user stories for the next sprint
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: The CI phase focuses on building the application, running automated tests, and producing a reliable, versioned artifact (often
a container image) that is ready for deployment.

---

<!-- note:1755881762517 model:Basic++ -->
**Front:** What is the <b>primary </b>benefit of implementing CI/CD pipelines
for application delivery?<div>&nbsp;
<br>A. It eliminates the need for testing
<br>B. It reduces infrastructure costs significantly
<br>C. It enables faster, more reliable software releases
<br>D. It automatically writes application code
<br>E. It replaces the need for version control systems</div>
**Back:** Correct Answer: <b>C</b>
<br><br>Explanation: CI/CD automates the build, test, and deployment processes, leading to increased release velocity, improved code quality through
automated testing, and more consistent deployments.

---

<!-- note:1755882660911 model:Basic++ -->
**Front:** What is a key advantage of using GitOps for managing Kubernetes deployments compared to traditional CI/CD push-based
deployments?<div>&nbsp;
<br>A. GitOps pipelines are significantly faster to execute.
<br>B. GitOps eliminates the need for container registries.
<br>C. GitOps enhances security by reducing direct cluster access for CI.
<br>D. GitOps does not require YAML manifests for resources.
<br>E. GitOps is only suitable for small-scale deployments.</div>
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: In GitOps, the CI system typically pushes an image to a
registry and updates a Git repo. An agent inside the cluster pulls changes
from Git, reducing the CI system’s need for direct cluster credentials and
providing a stronger security posture.
Domain: Cloud

---

<!-- note:1755882722876 model:Basic++ -->
**Front:** Which of these is a core component of a "Continuous Delivery" pipeline but <b>NOT </b>necessarily "Continuous Deployment"?<div>&nbsp;
<br>A. Automated building of code into an artifact.
<br>B. Automated execution of unit and integration tests.
<br>C. Automated deployment to a staging/QA environment.
<br>D. Automated deployment to the production environment.
<br>E. Manual approval gate before production deployment.</div>
**Back:** Correct Answer: <b>E</b>
<br><br><b>Explanation</b>: Continuous Delivery ensures every validated change is releasable to production, often with a manual approval step. Continuous
Deployment automates the release to production without manual intervention if all prior stages pass. Both include A, B, C.

---

<!-- note:1756923757934 model:Basic++ -->
**Front:** <div>What is the practice of using Git repositories as the single source of truth for defining and managing infrastructure and applications?</div><div><br></div><div>A. CI/CD</div><div>B. DevOps</div><div>C. GitOps</div><div>D. Infrastructure as Code (IaC)</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: GitOps leverages Git’s features (versioning, history, PRs) to manage infrastructure and application deployment declaratively.</div>

---

<!-- note:1756923805035 model:Basic++ -->
**Front:** <div>Which core principle differentiates GitOps from general Infrastructure as Code (IaC)?</div><div><br></div><div>A. Using code for infra config</div><div>B. Automating infrastructure tests</div><div>C. Using Git as the source of truth</div><div>D. Manual deployment approval</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: While IaC uses code, GitOps specifically mandates Git as the declarative source of truth and uses agents to enforce that state.</div>

---

<!-- note:1756923844051 model:Basic++ -->
**Front:** <div>What does ”CI” stand for in the context of application delivery?</div><div><br></div><div>A. Continuous Integration</div><div>B. Cluster Infrastructure</div><div>C. Container Interface</div><div>D. Cloud Instance</div>
**Back:** <div>Correct Answer: <b>A</b></div><div><br></div><div><b>Explanation</b>: Continuous Integration involves frequently merging code changes into a central repository, followed by automated builds and tests.</div>

---

<!-- note:1756923888048 model:Basic++ -->
**Front:** <div>What does ”CD” stand for in CI/CD?</div><div><br></div><div>A. Container Deployment</div><div>B. Continuous Delivery/Deployment</div><div>C. Cluster Discovery</div><div>D. Centralized Dashboard</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div><div><b>Explanation</b>: Continuous Delivery ensures code changes can be released quickly, while Continuous Deployment automatically deploys them to production.</div>

---

<!-- note:1756924019161 model:Basic++ -->
**Front:** <div>Which stage in a typical CI/CD pipeline for Kubernetes usually involves creating a container image?</div><div><br></div><div>A. Testing</div><div>B. Building</div><div>C. Deployment</div><div>D. Monitoring</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div><div><b>Explanation</b>: The build stage compiles code (if necessary) and packages the application and its dependencies into a container image (e.g., Docker).</div>

---

<!-- note:1756924290433 model:Basic++ -->
**Front:** <div>Which tool is commonly used in CI/CD pipelines to automate the build, test, and deployment processes?</div><div><br></div><div>A. Kubernetes</div><div>B. Docker</div><div>C. Jenkins / GitLab CI / GitHub Actions</div><div>D. Prometheus</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: Tools like Jenkins, GitLab CI, GitHub Actions, Argo CD, Flux etc., orchestrate the steps within a CI/CD pipeline.</div>

---

<!-- note:1756924326394 model:Basic++ -->
**Front:** <div>What is <b>the primary goal</b> of Application Delivery in a cloud native context?</div><div><br></div><div>A. To secure the cluster</div><div>B. To monitor resource usage</div><div>C. To reliably deploy manage apps</div><div>D. To provision infrastructure</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: Application delivery focuses on the processes and tools used to get applications running reliably and efficiently in the environment.</div>

---
<!-- note:1793915795947 model:Many -->
**Domain:** Helm - values
**Question:** Which Helm option overrides chart values from the command line?
**Options:** A. <code>--values</code><br>B. <code>--namespace</code><br>C. <code>--kubeconfig</code><br>D. <code>--set</code>
**Answer:** D – <code>--set</code> key=value overrides Helm values inline
**Explanation:** <code>--set</code> overrides individual chart values inline as key=value pairs — repeatable and comma-separable (<code>helm install web ./chart --set image.tag=2.0 --set replicas=3</code>). Precedence: <code>--set</code> beats -f/<code>--values</code> files, which beat the chart's values.yaml defaults. The distractors do unrelated things: <code>--values</code>/-f supplies a whole YAML file of overrides (not inline), <code>--namespace</code> picks the install namespace, <code>--kubeconfig</code> points at a cluster credentials file. For strings that look like numbers or file-sourced values there are <code>--set-string</code> and <code>--set-file</code>.
**Sources:** <a href="https://helm.sh/docs/intro/using_helm/" target="_blank">Helm Docs - Using Helm</a>
**Tags:** k8s::kcna topic::helm topic::packaging src::session

---
<!-- note:1793919187035 model:Many -->
**Domain:** Helm - install flags
**Question:** What is the purpose of Helm's --atomic flag?
**Options:** A. Dry-run only<br>B. Roll back automatically on failure<br>C. Create CRDs<br>D. Render templates only
**Answer:** B (2) – roll back automatically on failure
**Explanation:** --atomic makes helm install/upgrade all-or-nothing: if any resource fails to become ready, Helm rolls the release back to its previous revision instead of leaving a half-installed release behind. It builds on --wait (Helm waits for readiness) plus automatic rollback — without it a failed upgrade can strand the cluster in a mixed old/new state. The distractors describe other flags: --dry-run only renders templates client-side without touching the cluster, and CRDs come from the chart's crds/ directory (installed before templates, never templated).
**Sources:** <a href="https://helm.sh/docs/intro/using_helm/" target="_blank">Helm Docs - Using Helm</a>
**Tags:** k8s::kcna topic::helm topic::packaging src::session

---

<!-- note:1793921208832 model:Many -->
**Domain:** Ingress - API versions
**Question:** Which is a valid Ingress apiVersion/kind in modern Kubernetes?
**Options:** A. extensions/v1beta1 / Ingress<br>B. v1 / Ingress<br>C. networking.k8s.io/v2 / Ingress<br>D. networking.k8s.io/v1 / Ingress
**Answer:** D (4) – networking.k8s.io/v1 / Ingress
**Explanation:** networking.k8s.io/v1 has been the stable Ingress API since Kubernetes 1.19 — extensions/v1beta1 and networking.k8s.io/v1beta1 were removed in 1.22. The v1beta1→v1 jump had real breaking changes: pathType became required on every path, backend.service.port.name was dropped (number only), and ingressClassName became a spec field. The 'something different' to know: the Ingress API is FROZEN — generally available but no longer developed, no new features. Kubernetes officially recommends the Gateway API (gateway.networking.k8s.io/v1, GA since Oct 2023, v1.4 Oct 2025) as its successor — same job (HTTP routing to Services), richer model: Gateway + GatewayClass + HTTPRoute objects instead of one Ingress.
**Sources:** <a href="https://kubernetes.io/docs/concepts/services-networking/ingress/" target="_blank">Kubernetes Docs - Ingress</a><br><a href="https://gateway-api.sigs.k8s.io/guides/getting-started/migrating-from-ingress/" target="_blank">Gateway API - Migrating from Ingress</a>
**Tags:** k8s::kcna topic::networking topic::ingress src::session

---
