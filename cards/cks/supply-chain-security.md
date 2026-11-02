# CKS - Certified Kubernetes Security Specialist — Supply Chain Security

> Deck: `CKS - Certified Kubernetes Security Specialist` · Group: `Supply Chain Security` · Notes: 115 · Models: Basic+

<!-- note:1772501256855 model:Basic+ -->
**Front:** What does the image name 'nginx' represent in Docker's naming convention?
**Back:** It represents 'library/nginx', where 'library' is the default account for official images.
**Tags:** ankidote docker-conventions image-naming

---

<!-- note:1772501256859 model:Basic+ -->
**Front:** What is the default registry used by Kubernetes if no registry is specified?
**Back:** Docker Hub (docker.io).
**Tags:** ankidote kubernetes registry

---

<!-- note:1772501256862 model:Basic+ -->
**Front:** Provide an example of an image name using a private registry.
**Back:** private-registry.io/apps/internal-app
**Tags:** ankidote image-naming private-registry

---

<!-- note:1772501256865 model:Basic+ -->
**Front:** What command is used to authenticate with a private Docker registry?
**Back:** docker login private-registry.io
**Tags:** ankidote docker-commands private-registry

---

<!-- note:1772501256868 model:Basic+ -->
**Front:** What Kubernetes secret type is used for Docker registry credentials?
**Back:** docker-registry
**Tags:** ankidote kubernetes-secrets registry

---

<!-- note:1772501256873 model:Basic+ -->
**Front:** How do you configure a pod to use a private registry image?
**Back:** Add the full image path in the 'image' field and include 'imagePullSecrets' with the secret name.
**Tags:** ankidote kubernetes pod-configuration

---

<!-- note:1772501256875 model:Basic+ -->
**Front:** What is the purpose of a Docker registry secret in Kubernetes?
**Back:** To securely store credentials for accessing private image registries.
**Tags:** ankidote kubernetes-secrets security

---

<!-- note:1772501256877 model:Basic+ -->
**Front:** What is the format for creating a Docker registry secret in Kubernetes?
**Back:** kubectl create secret docker-registry <secret-name> --docker-server=<server> --docker-username=<user> --docker-password=<password> --docker-email=<email>
**Tags:** ankidote commands kubernetes

---

<!-- note:1772501256881 model:Basic+ -->
**Front:** Why should internal applications use private registries?
**Back:** To prevent unauthorized access and ensure image security.
**Tags:** ankidote private-registry security

---

<!-- note:1772501256884 model:Basic+ -->
**Front:** What is the structure of a typical Kubernetes pod definition for an image?
**Back:** apiVersion: v1
kind: Pod
metadata: {name: <pod-name>}
spec: {containers: [{name: <container>, image: <image-name>}]}
**Tags:** ankidote kubernetes pod-configuration

---

<!-- note:1772501296081 model:Basic+ -->
**Front:** What is KubeLinter?
**Back:** KubeLinter is a tool that identifies configuration issues in Kubernetes deployments and ensures adherence to best practices by analyzing manifest files and providing actionable recommendations.
**Tags:** ankidote kube-linter kubernetes-tools

---

<!-- note:1772501296085 model:Basic+ -->
**Front:** List common misconfigurations in the sample Kubernetes manifest.
**Back:** 1. Single replica (no redundancy)
2. Use of 'latest' image tag
3. Missing resource requests/limits
4. Lack of security contexts
5. Absence of liveness/readiness probes
**Tags:** ankidote kube-linter yaml-misconfigurations

---

<!-- note:1772501296090 model:Basic+ -->
**Front:** What command runs KubeLinter on Kubernetes manifests?
**Back:** kube-linter lint .
**Tags:** ankidote kube-linter usage

---

<!-- note:1772501296095 model:Basic+ -->
**Front:** What are the benefits of integrating KubeLinter with CI/CD pipelines?
**Back:** 1. Prevents misconfigurations
2. Enhances security through customizable rules
3. Improves deployment reliability
4. Enables automated compliance checks
**Tags:** ankidote ci-cd kube-linter

---

<!-- note:1772501296098 model:Basic+ -->
**Front:** What command installs KubeLinter via the script?
**Back:** curl -sSfL https://raw.githubusercontent.com/stackrox/kubelinter/main/scripts/install.sh | sh -
**Tags:** ankidote installation kube-linter

---

<!-- note:1772501296100 model:Basic+ -->
**Front:** What Jenkins pipeline stages include KubeLinter?
**Back:** 1. Checkout code
2. Install KubeLinter
3. Lint Kubernetes manifests
**Tags:** ankidote ci-cd jenkins

---

<!-- note:1772501296105 model:Basic+ -->
**Front:** What GitHub Actions configuration runs KubeLinter?
**Back:** name: Lint Kubernetes Manifests
on: [push]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run KubeLinter
        run: kube-linter lint .
**Tags:** ankidote ci-cd github-actions

---

<!-- note:1772501296109 model:Basic+ -->
**Front:** What are KubeLinter's key capabilities?
**Back:** 1. Detects single-replica deployments
2. Flags 'latest' image tags
3. Recommends security contexts
4. Validates resource requests/limits
5. Suggests liveness/readiness probes
**Tags:** ankidote features kube-linter

---

<!-- note:1772501336181 model:Basic+ -->
**Front:** What is a base image in Docker?
**Back:** A base image is the foundation for other Docker images. It is the starting point for building new images. Examples include Debian and HTTPD images.
**Tags:** ankidote docker-base-image docker-concepts

---

<!-- note:1772501336185 model:Basic+ -->
**Front:** What is a best practice for modular Docker images?
**Back:** Separate applications into distinct images. Each container should perform a single task to simplify management and enhance security through isolation.
**Tags:** ankidote docker-best-practices modular-design

---

<!-- note:1772501336189 model:Basic+ -->
**Front:** Why should data not be persisted inside containers?
**Back:** Containers are ephemeral by design. Data should be stored in external volumes or caching services like Redis to ensure persistence and security.
**Tags:** ankidote data-persistence docker-best-practices

---

<!-- note:1772501336192 model:Basic+ -->
**Front:** What is a Dockerfile snippet to select a base image?
**Back:** FROM <base-image>
COPY index.html htdocs/index.html
**Tags:** ankidote base-image-selection dockerfile-syntax

---

<!-- note:1772501336197 model:Basic+ -->
**Front:** How can you minimize Docker image size?
**Back:** Use minimal OS versions, install only necessary libraries, remove temporary files, and eliminate unnecessary tools like curl or wget to reduce attack surface.
**Tags:** ankidote docker-best-practices image-size

---

<!-- note:1772501336200 model:Basic+ -->
**Front:** What is the purpose of separate development and production images?
**Back:** Development images include debugging tools and extra packages, while production images optimize performance and security by excluding non-essential components.
**Tags:** ankidote docker-best-practices environment-separation

---

<!-- note:1772501336205 model:Basic+ -->
**Front:** What security benefit do smaller Docker images provide?
**Back:** Smaller images with fewer packages have a reduced attack surface. For example, httpd:alpine has zero vulnerabilities compared to the standard httpd image.
**Tags:** ankidote docker-security vulnerability-reduction

---

<!-- note:1772501336208 model:Basic+ -->
**Front:** What are distroless images and their security advantage?
**Back:** Distroless images contain only the application and runtime dependencies without package managers, shells, or network tools, minimizing potential attack vectors.
**Tags:** ankidote distroless-images docker-security

---

<!-- note:1772501336212 model:Basic+ -->
**Front:** What tool compares vulnerabilities in Docker images?
**Back:** Trivy is used to scan Docker images. It shows vulnerability counts, e.g., httpd has 124 vulnerabilities while httpd:alpine has zero.
**Tags:** ankidote docker-security trivy-tool

---

<!-- note:1772501336216 model:Basic+ -->
**Front:** What is the primary goal of minimizing base image footprint?
**Back:** To improve efficiency, security, and deployment speed by reducing image size and eliminating unnecessary components.
**Tags:** ankidote base-image-footprint docker-optimization

---

<!-- note:1772501390705 model:Basic+ -->
**Front:** What are the four stages of a secure supply chain?
**Back:** 1. Receiving and Inspection
2. Assembly and Intermediate Quality Checks
3. Rigorous Quality Assurance Testing
4. Packaging and Secure Release
**Tags:** ankidote quality-control supply-chain-stages

---

<!-- note:1772501390709 model:Basic+ -->
**Front:** What is the purpose of receiving and inspection in a supply chain?
**Back:** To verify raw materials and components meet defined standards before advancing to assembly.
**Tags:** ankidote quality-control supply-chain-stages

---

<!-- note:1772501390716 model:Basic+ -->
**Front:** What tools are used for vulnerability scanning in software supply chains?
**Back:** OWASP Dependency-Check, Snyk, Clair, and Trivy.
**Tags:** ankidote dependency-checking software-security-tools

---

<!-- note:1772501390721 model:Basic+ -->
**Front:** What is the role of quality assurance testing in supply chains?
**Back:** To identify defects and ensure products meet strict quality standards before final release.
**Tags:** ankidote quality-assurance supply-chain-testing

---

<!-- note:1772501390724 model:Basic+ -->
**Front:** What are techniques for securing Kubernetes deployments?
**Back:** Pod Security Policies, network policies, and role-based access controls (RBAC).
**Tags:** ankidote deployment-security kubernetes-security

---

<!-- note:1772501390726 model:Basic+ -->
**Front:** What is one benefit of robust supply chain security?
**Back:** Early vulnerability detection allows for swift remediation of issues.
**Tags:** ankidote supply-chain-benefits vulnerability-management

---

<!-- note:1772501390730 model:Basic+ -->
**Front:** What is the key takeaway from the callout about supply chain security?
**Back:** Neglecting any stage of supply chain security exposes systems to risks and potential breaches.
**Tags:** ankidote security-best-practices supply-chain-risks

---

<!-- note:1772501390732 model:Basic+ -->
**Front:** What is the analogy provided for secure software supply chains?
**Back:** Developers work in secure environments like factories inspecting raw materials, ensuring code is tested and secure.
**Tags:** ankidote software-development supply-chain-analogy

---

<!-- note:1772501390734 model:Basic+ -->
**Front:** What is the purpose of packaging and secure release in supply chains?
**Back:** To ensure products reach customers without tampering, analogous to secure software deployment.
**Tags:** ankidote secure-release supply-chain-stages

---

<!-- note:1772501390738 model:Basic+ -->
**Front:** What are the five benefits of robust supply chain security?
**Back:** 1. Early vulnerability detection
2. Optimized resource management
3. Improved compliance
4. Efficient incident response
5. Enhanced overall security posture
**Tags:** ankidote security-posture supply-chain-benefits

---

<!-- note:1772501420105 model:Basic+ -->
**Front:** What risk arises from unpatched vulnerabilities in software components?
**Back:** Unpatched vulnerabilities create openings for attackers to exploit, potentially leading to major data breaches, financial losses, regulatory fines, and loss of customer trust.
**Tags:** ankidote data-breach supply-chain-vulnerabilities

---

<!-- note:1772501420110 model:Basic+ -->
**Front:** What risk is associated with integrating untrusted third-party components?
**Back:** Untrusted components may introduce hidden malware, serving as backdoors for network infiltration, causing operational disruptions and costly incident response efforts.
**Tags:** ankidote malware third-party-components

---

<!-- note:1772501420114 model:Basic+ -->
**Front:** What risk occurs when sensitive credentials are stored without encryption?
**Back:** Unencrypted credentials expose critical customer data to attackers, resulting in severe data breaches and erosion of customer confidence.
**Tags:** ankidote credential-security data-breach

---

<!-- note:1772501420121 model:Basic+ -->
**Front:** What risk is created by overly permissive configuration settings?
**Back:** Improper access controls, such as lax network policies or missing RBAC in Kubernetes, allow attackers to infiltrate systems and exploit network weaknesses.
**Tags:** access-controls ankidote configuration-settings

---

<!-- note:1772501420126 model:Basic+ -->
**Front:** What risk does improper container security configuration pose?
**Back:** Misconfigured containers enable attackers to escape the container environment, tamper with the host system, and gain full control over critical infrastructure.
**Tags:** ankidote container-security host-compromise

---

<!-- note:1772501420130 model:Basic+ -->
**Front:** What are the main risks of inadequate supply chain management?
**Back:** Inadequate supply chain management leads to cyber attacks, operational disruptions, financial losses, regulatory/legal actions, and competitive disadvantage.
**Tags:** ankidote cumulative-risks supply-chain-risks

---

<!-- note:1772501484103 model:Basic+ -->
**Front:** What are the key sections of an SPDX document?
**Back:** SPDX documents include Document Information, Relationships, Package Information, Snippets, File Information, and Additional Metadata.
**Tags:** ankidote document-structure sbom-format spdx

---

<!-- note:1772501484107 model:Basic+ -->
**Front:** What is the purpose of the 'Document Information' section in SPDX?
**Back:** It contains metadata about the SPDX document, including creator details, creation date, and version.
**Tags:** ankidote document-information sbom-format spdx

---

<!-- note:1772501484109 model:Basic+ -->
**Front:** What does the 'Package Information' section in SPDX include?
**Back:** It provides details like package name, version, supplier, and verification information such as checksums.
**Tags:** ankidote package-info sbom-format spdx

---

<!-- note:1772501484111 model:Basic+ -->
**Front:** What is the SPDX format's focus?
**Back:** SPDX emphasizes licensing compliance and legal documentation of software packages.
**Tags:** ankidote licensing sbom-format spdx

---

<!-- note:1772501484113 model:Basic+ -->
**Front:** What is CycloneDX designed for?
**Back:** CycloneDX is designed for lightweight SBOMs focusing on security aspects like vulnerability tracking and dependency management.
**Tags:** ankidote cyclonedx sbom-format security

---

<!-- note:1772501484115 model:Basic+ -->
**Front:** What sections are included in CycloneDX?
**Back:** CycloneDX includes BOM Metadata, Components List, Vulnerabilities, Software Services, Annotations, and Dependencies.
**Tags:** ankidote cyclonedx document-structure sbom-format

---

<!-- note:1772501484117 model:Basic+ -->
**Front:** What is the primary difference between SPDX and CycloneDX?
**Back:** SPDX focuses on licensing compliance with extensive metadata, while CycloneDX prioritizes security and vulnerability tracking.
**Tags:** ankidote comparison sbom-format spdx-vs-cyclonedx

---

<!-- note:1772501484119 model:Basic+ -->
**Front:** What is the format of an SPDX document?
**Back:** SPDX is available in JSON and RDF formats, with examples shown in JSON.
**Tags:** ankidote format sbom-format spdx

---

<!-- note:1772501484121 model:Basic+ -->
**Front:** What is the format of a CycloneDX document?
**Back:** CycloneDX is available in JSON and XML formats, with examples shown in JSON.
**Tags:** ankidote cyclonedx format sbom-format

---

<!-- note:1772501484122 model:Basic+ -->
**Front:** What does the 'externalRefs' field in SPDX contain?
**Back:** It includes security references like CPE identifiers and package manager URLs for vulnerability tracking.
**Tags:** ankidote external-refs sbom-format spdx

---

<!-- note:1772501484124 model:Basic+ -->
**Front:** What information is captured in SPDX 'File Information'?
**Back:** It tracks individual files, including file types, checksums, and license information.
**Tags:** ankidote file-info sbom-format spdx

---

<!-- note:1772501484126 model:Basic+ -->
**Front:** What is the purpose of the 'licenseConcluded' field in SPDX?
**Back:** It indicates the concluded license for a package when no definitive information is provided (e.g., 'NOASSERTION').
**Tags:** ankidote licensing sbom-format spdx

---

<!-- note:1772501484128 model:Basic+ -->
**Front:** What is the role of the 'bomFormat' field in CycloneDX?
**Back:** It specifies the SBOM format, such as 'CycloneDX', and indicates the version used.
**Tags:** ankidote cyclonedx metadata sbom-format

---

<!-- note:1772501484130 model:Basic+ -->
**Front:** What does the 'components' section in CycloneDX list?
**Back:** It enumerates individual parts or modules within the software, including their type and publisher.
**Tags:** ankidote components cyclonedx sbom-format

---

<!-- note:1772501484132 model:Basic+ -->
**Front:** What is the significance of 'checksums' in SPDX file information?
**Back:** Checksums verify file integrity and authenticity, ensuring the file matches its source.
**Tags:** ankidote file-integrity sbom-format spdx

---

<!-- note:1772501484134 model:Basic+ -->
**Front:** What is the 'documentNamespace' in an SPDX document?
**Back:** It is a URI that uniquely identifies the SPDX document, often linking to a specific image or artifact.
**Tags:** ankidote document-namespace sbom-format spdx

---

<!-- note:1772501484136 model:Basic+ -->
**Front:** What does the 'created' field in SPDX represent?
**Back:** It indicates the timestamp when the SPDX document was generated.
**Tags:** ankidote metadata sbom-format spdx

---

<!-- note:1772501484139 model:Basic+ -->
**Front:** What is the 'SPDXID' in an SPDX document?
**Back:** It is a unique identifier for each component or document within the SBOM, ensuring reference consistency.
**Tags:** ankidote identifiers sbom-format spdx

---

<!-- note:1772501484141 model:Basic+ -->
**Front:** What is the purpose of the 'externalRefs' in CycloneDX?
**Back:** It provides references to external resources like vulnerability databases or package managers.
**Tags:** ankidote cyclonedx references sbom-format

---

<!-- note:1772501484142 model:Basic+ -->
**Front:** What is the 'version' field in a CycloneDX BOM?
**Back:** It specifies the version of the CycloneDX schema used for the SBOM document.
**Tags:** ankidote cyclonedx sbom-format schema

---

<!-- note:1772501526779 model:Basic+ -->
**Front:** What are the six steps in the SBOM workflow?
**Back:** 1. Generate SBOM
2. Securely store SBOM
3. Scan SBOM for vulnerabilities
4. Analyze scan results
5. Remediate identified issues
6. Continuously monitor SBOM
**Tags:** ankidote sbom-process workflow-steps

---

<!-- note:1772501526782 model:Basic+ -->
**Front:** What is the primary purpose of SPDX format?
**Back:** SPDX is used for open-source projects and enterprises requiring licensing compliance, software origin tracking, security auditing, and vulnerability management.
**Tags:** ankidote sbom-formats spdx

---

<!-- note:1772501526787 model:Basic+ -->
**Front:** What is CycloneDX format best suited for?
**Back:** CycloneDX is ideal for enhancing vulnerability management across the software lifecycle and ensuring software integrity.
**Tags:** ankidote cyclonedx sbom-formats

---

<!-- note:1772501526790 model:Basic+ -->
**Front:** What command generates an SPDX SBOM for a Docker image using Syft?
**Back:** syft <image-name>:<tag> -o spdx-json
**Tags:** ankidote sbom-generation syft-tool

---

<!-- note:1772501526793 model:Basic+ -->
**Front:** What are three secure storage options for SBOMs?
**Back:** JFrog, Sonatype Nexus, and GitHub Packages
**Tags:** ankidote sbom-storage secure-repositories

---

<!-- note:1772501526798 model:Basic+ -->
**Front:** What command scans an SBOM file for vulnerabilities using Grype?
**Back:** grype sbom:nginx-sbom.cyclonedx.json
**Tags:** ankidote grype-tool sbom-scanning

---

<!-- note:1772501526801 model:Basic+ -->
**Front:** What vulnerability details are included in the SBOM JSON example?
**Back:** CVE ID, severity, links, CVSS v2 score, matching criteria, artifact details, locations, and metadata about the vulnerable package.
**Tags:** ankidote sbom-json vulnerability-analysis

---

<!-- note:1772501526804 model:Basic+ -->
**Front:** What are common remediation actions for SBOM vulnerabilities?
**Back:** Update affected packages to secure versions or replace with alternative solutions.
**Tags:** ankidote sbom-fixes vulnerability-remediation

---

<!-- note:1772501526806 model:Basic+ -->
**Front:** What is the purpose of continuous monitoring in SBOM workflows?
**Back:** To ensure dependencies are regularly updated and new vulnerabilities or compliance issues are promptly addressed through automated alerts in CI/CD pipelines.
**Tags:** ankidote continuous-monitoring sbom-ci-cd

---

<!-- note:1772501580503 model:Basic+ -->
**Front:** What is a CVE?
**Back:** A Common Vulnerabilities and Exposures identifier is a unique name for a specific vulnerability or security issue. It helps simplify bug reporting, avoid duplicates, and provides detailed information for remediation.
**Tags:** ankidote cve vulnerability-management

---

<!-- note:1772501580507 model:Basic+ -->
**Front:** What does Trivy do?
**Back:** Trivy is a vulnerability scanner for container images and other artifacts. It detects vulnerabilities in software packages and provides severity ratings (0-10) based on CVSS scores.
**Tags:** ankidote container-security trivy

---

<!-- note:1772501580512 model:Basic+ -->
**Front:** How to install Trivy on Debian?
**Back:** Install Trivy by: 1. Adding the Aqua repo 2. Updating apt 3. Installing trivy: `sudo apt-get install trivy`
**Tags:** ankidote debian installation trivy

---

<!-- note:1772501580515 model:Basic+ -->
**Front:** What command scans a container image?
**Back:** Use `trivy image <image-name>` (e.g., `trivy image nginx:1.18.0`) to scan for vulnerabilities in a container image.
**Tags:** ankidote container-scanning scan-command trivy

---

<!-- note:1772501580517 model:Basic+ -->
**Front:** What severity levels does Trivy use?
**Back:** Trivy uses CVSS scores from 0 (none) to 10 (critical). Severity levels include LOW, MEDIUM, HIGH, and CRITICAL.
**Tags:** ankidote cvss severity trivy

---

<!-- note:1772501580519 model:Basic+ -->
**Front:** How to filter Trivy results by severity?
**Back:** Use `--severity` flag: `trivy image --severity CRITICAL,HIGH nginx:1.18.0` to filter results to critical and high severity issues.
**Tags:** ankidote filtering severity trivy

---

<!-- note:1772501580521 model:Basic+ -->
**Front:** What does the Trivy scan output show?
**Back:** The output lists vulnerabilities with ID, severity, installed version, and title. Example: `CVE-2011-3374 (LOW) in apt`.
**Tags:** ankidote scan-output trivy vulnerability-report

---

<!-- note:1772501580523 model:Basic+ -->
**Front:** How to scan a Docker tar archive with Trivy?
**Back:** Use `--input` flag: `trivy image --input nginx.tar` after creating a tar archive with `docker save nginx:1.18.0 > nginx.tar`.
**Tags:** ankidote container-scanning tar-archive trivy

---

<!-- note:1772501580525 model:Basic+ -->
**Front:** What is the NGINX CVE-2020-5911 issue?
**Back:** A vulnerability in NGINX Controller where it downloads Kubernetes packages via insecure HTTP URLs on Debian/Ubuntu, rated HIGH severity (7.3).
**Tags:** ankidote cve nginx vulnerability-example

---

<!-- note:1772501580529 model:Basic+ -->
**Front:** What is a best practice for image scanning?
**Back:** Integrate vulnerability scanning into CI/CD pipelines to automatically detect issues in every new build.
**Tags:** ankidote best-practices ci-cd container-security

---

<!-- note:1772501580531 model:Basic+ -->
**Front:** Why use lightweight container images?
**Back:** Leaner images like `nginx:1.18.0-alpine` reduce attack surface by minimizing included packages and dependencies.
**Tags:** ankidote container-optimization image-scan security

---

<!-- note:1772501580535 model:Basic+ -->
**Front:** How to ignore unfixed vulnerabilities in Trivy?
**Back:** Use `--ignore-unfixed` flag: `trivy image --ignore-unfixed nginx:1.18.0` to skip vulnerabilities without available fixes.
**Tags:** ankidote filtering trivy unfixed-vulnerabilities

---

<!-- note:1772501605831 model:Basic+ -->
**Front:** What is the focus of this article?
**Back:** The article focuses on supply chain security, with an emphasis on container image security, workload analysis methods, and vulnerability scanning techniques.
**Tags:** ankidote chain container image security supply

---

<!-- note:1772501605835 model:Basic+ -->
**Front:** How can container image security be strengthened?
**Back:** By reducing the footprint of container images to minimize the attack surface and enhance overall image security.
**Tags:** ankidote attack container image reduction security surface

---

<!-- note:1772501605839 model:Basic+ -->
**Front:** What methods are discussed for analyzing workloads?
**Back:** Industry-standard tools for analyzing workloads are detailed, though specific tools are not listed in the introduction.
**Tags:** analysis ankidote chain security supply workload

---

<!-- note:1772501605842 model:Basic+ -->
**Front:** What is emphasized regarding vulnerability scanning?
**Back:** The importance of scanning container images for known vulnerabilities using popular scanning utilities is highlighted.
**Tags:** ankidote container image scanning security vulnerability

---

<!-- note:1772501605845 model:Basic+ -->
**Front:** What practical elements are included in this article?
**Back:** Several practical labs and hands-on exercises are provided to reinforce concepts and provide real-world application experience.
**Tags:** ankidote exercises hands-on labs practical

---

<!-- note:1772501651288 model:Basic+ -->
**Front:** What is the purpose of static analysis in Kubernetes resource files?
**Back:** Static analysis identifies security issues and enforces standards in Kubernetes resource files before deployment, allowing early detection of risks.
**Tags:** ankidote kubernetes-security static-analysis

---

<!-- note:1772501651291 model:Basic+ -->
**Front:** What security risks does the sample pod YAML demonstrate?
**Back:** The sample pod uses a privileged container (privileged: True), runs as root (runAsUser: 0), and adds dangerous capabilities (CAP_SYS_BOOT), all of which pose significant security risks.
**Tags:** ankidote kubernetes-yaml security-contexts

---

<!-- note:1772501651295 model:Basic+ -->
**Front:** What critical issue does the static analysis tool flag in the sample pod?
**Back:** The tool flags the use of privileged containers as a critical security issue, assigning a score of -30 due to potential system access risks.
**Tags:** ankidote security-risks static-analysis-output

---

<!-- note:1772501651298 model:Basic+ -->
**Front:** What command scans a Kubernetes resource file with kubecsec?
**Back:** kubecsec scan pod.yaml
**Tags:** ankidote kubecsec-commands static-analysis-tools

---

<!-- note:1772501651302 model:Basic+ -->
**Front:** What does the scoring system in the analysis output indicate?
**Back:** The score (-30) reflects the severity of security issues, with critical issues contributing significantly to the score, while advice items provide points for potential mitigations.
**Tags:** ankidote scoring-system security-score

---

<!-- note:1772501651306 model:Basic+ -->
**Front:** How does static analysis differ from admission controllers in Kubernetes?
**Back:** Static analysis occurs during development before deployment, while admission controllers validate resources at runtime when the kubectl command is executed.
**Tags:** ankidote kubernetes-security static-analysis-vs-admission

---

<!-- note:1772501651310 model:Basic+ -->
**Front:** What are two security recommendations provided in the analysis output?
**Back:** 1. Use AppArmor policies (ApparmorAny) for enhanced security. 2. Use service accounts (ServiceAccountName) to restrict Kubernetes API access.
**Tags:** analysis-advice ankidote security-recommendations

---

<!-- note:1772501651314 model:Basic+ -->
**Front:** What are the available methods to run the static analysis tool?
**Back:** 1. Local binary: kubecsec scan pod.yaml. 2. Public service: curl https://v2.kubecsec.io/scan. 3. Local HTTP server: kubecsec http 8080.
**Tags:** ankidote kubecsec-methods static-analysis-tools

---

<!-- note:1772501651318 model:Basic+ -->
**Front:** What resource is recommended for practicing static analysis with kubecsec?
**Back:** The practice lab at https://learn.kodekloud.com/user/courses/certified-kubernetes-security-specialist-cks/module/e4511664-185f-4204-9aa2-b4250cbadf84/lesson/11566885-cd7c-468d-a321-5d9d6fed5f46
**Tags:** ankidote practice-labs resources

---

<!-- note:1772501678504 model:Basic+ -->
**Front:** What is a Software Bill of Materials (SBOM)?
**Back:** A comprehensive list of all components in a software application, including open-source libraries, third-party dependencies, licenses, versions, and patch statuses. It provides transparency about the software's composition, similar to a recipe detailing ingredients and allergens.
**Tags:** ankidote compliance security software-bill-of-materials

---

<!-- note:1772501678508 model:Basic+ -->
**Front:** What are the key benefits of an SBOM?
**Back:** Improved transparency in software composition, quicker incident response during security events, efficient dependency management, enhanced security through vulnerability tracking, and easier compliance with regulatory standards.
**Tags:** ankidote compliance security software-bill-of-materials

---

<!-- note:1772501678510 model:Basic+ -->
**Front:** How does an SB,OM help with security incident response?
**Back:** It enables rapid identification of affected components and evaluation of vulnerabilities, allowing teams to apply patches or replace compromised elements swiftly during security incidents.
**Tags:** ankidote incident-response security software-bill-of-materials

---

<!-- note:1772501678513 model:Basic+ -->
**Front:** What information is typically included in an SBOM example?
**Back:** Component name, version, supplier details, licensing information, dependencies, vulnerability data, and security references (e.g., CPE identifiers). Example: JSON showing package metadata, SPDX IDs, and license declarations.
**Tags:** ankidote json security software-bill-of-materials

---

<!-- note:1772501678515 model:Basic+ -->
**Front:** What role does an SBOM play in regulatory compliance?
**Back:** It supports compliance by documenting licensing information meticulously, ensuring adherence to industry standards regarding software composition and intellectual property requirements.
**Tags:** ankidote compliance regulation software-bill-of-materials

---

<!-- note:1772501678517 model:Basic+ -->
**Front:** What is the purpose of the SBOM example provided?
**Back:** To illustrate key components of an SBOM, such as package metadata, supplier details, licensing, and security references, demonstrating how it provides a comprehensive overview of software composition.
**Tags:** ankidote example security software-bill-of-materials

---

<!-- note:1772501723030 model:Basic+ -->
**Front:** What is the purpose of whitelisting allowed registries in Kubernetes?
**Back:** To prevent unauthorized container images from being deployed by restricting pod creation to approved registries, enhancing cluster security.
**Tags:** ankidote image-policy kubernetes-security

---

<!-- note:1772501723033 model:Basic+ -->
**Front:** What role do admission controllers play in restricting container images?
**Back:** Admission controllers validate incoming pod creation requests, ensuring container images originate from approved registries before allowing deployment.
**Tags:** admission-webhook ankidote kubernetes-controls

---

<!-- note:1772501723037 model:Basic+ -->
**Front:** What is the function of a validating admission webhook in this context?
**Back:** To inspect pod creation requests, verify image sources against allowed registries, and reject requests with untrusted images.
**Tags:** admission-webhook ankidote webhook-validation

---

<!-- note:1772501723041 model:Basic+ -->
**Front:** What does the Python code snippet demonstrate?
**Back:** A validating webhook server that allows only images from 'internal-registry.io' by checking the image name in the pod spec.
**Tags:** admission-webhook ankidote webhook-code

---

<!-- note:1772501723044 model:Basic+ -->
**Front:** What is the purpose of the Rego policy in the OPA example?
**Back:** To deny pod creation unless the image starts with 'internal-registry.io/', enforcing trusted registry restrictions.
**Tags:** ankidote opa-rego policy-enforcement

---

<!-- note:1772501723047 model:Basic+ -->
**Front:** What is the ImagePolicyWebhook admission controller used for?
**Back:** To enforce image policy rules by integrating with an external webhook server to validate container image sources.
**Tags:** admission-controller ankidote image-policy

---

<!-- note:1772501723050 model:Basic+ -->
**Front:** What parameters define the admission configuration file for ImagePolicyWebhook?
**Back:** It includes kubeConfigFile for authentication, allowTTL, denyTTL, retryBackoff, and defaultAllow settings for webhook behavior.
**Tags:** admission-config ankidote kubeconfig

---

<!-- note:1772501723053 model:Basic+ -->
**Front:** What is the purpose of the KubeConfig file in this context?
**Back:** To provide authentication credentials (client certificates, CA certificates, and server URL) for connecting to the webhook server.
**Tags:** ankidote kubeconfig webhook-auth

---

<!-- note:1772501723056 model:Basic+ -->
**Front:** How do you enable ImagePolicyWebhook in kube-apiserver?
**Back:** By adding 'ImagePolicyWebhook' to the --enable-admission-plugins flag and specifying the admission control config file path via --admission-control-config-file.
**Tags:** admission-plugins ankidote kube-apiserver

---

<!-- note:1772501723059 model:Basic+ -->
**Front:** What is the effect of setting defaultAllow: true in the admission config?
**Back:** Pod creation is permitted if the webhook is unreachable, but explicitly denied images are still blocked, balancing security and availability.
**Tags:** admission-config ankidote security-settings

---
