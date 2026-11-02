# KCNA - Kubernetes and Cloud Native Associate — Cloud Native Architecture

> Deck: `KCNA - Kubernetes and Cloud Native Associate` · Group: `Cloud Native Architecture` · Notes: 22 · Models: Basic++, Basic+++

<!-- note:1755880202648 model:Basic++ -->
**Front:** Why is container orchestration essential for managing microservices at scale?<br><br>A. It simplifies writing microservice code
<br>B. It automatically converts monolithic apps to microservices
<br>C. It handles service discovery, scaling, and fault tolerance
<br>D. It provides a centralized logging solution by default
<br>E. It guarantees zero-downtime deployments
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: Orchestrators like Kubernetes automate complex tasks
like service discovery, load balancing, scaling based on demand, and selfhealing, which are crucial for managing a distributed microservices architecture.

---

<!-- note:1755880537022 model:Basic++ -->
**Front:** What fundamental problem does a <b>Service Mesh</b> like <b>Istio </b>or
<b>Linkerd </b>aim to solve in a microservices architecture?
<br><br>A. Simplifying container image building
<br>B. Automating infrastructure provisioning
<br>C. Managing and observing inter-service communication
<br>D. Providing persistent storage for stateful applications
<br>E. Abstracting server management
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: Service meshes provide a dedicated infrastructure layer for
handling service-to-service communication, offering features 1 like traffic
management, security (mTLS), and observability (metrics, traces) without
requiring changes to application code.

---

<!-- note:1755880758526 model:Basic++ -->
**Front:** How does Serverless (e.g., FaaS like AWS Lambda or Knative
Serving) <b>primarily </b>differ from traditional PaaS offerings?<br><br>A. Serverless does not use containers
<br>B. Serverless applications cannot be stateful
<br>C. Serverless abstracts away all underlying server management
<br>D. PaaS does not offer auto-scaling capabilities
<br>E. Serverless is only for event-driven functions
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: Serverless computing (especially FaaS) aims to abstract
away all infrastructure management, including servers, OS, and runtimes,
allowing developers to focus solely on writing code that executes in response to events.

---

<!-- note:1755880801919 model:Basic++ -->
**Front:** What is <b>the primary role</b> of the Cloud Native Computing Foundation (CNCF) in the Kubernetes ecosystem?<br><br>A. To directly employ Kubernetes core developers
<br>B. To sell Kubernetes enterprise support subscriptions
<br>C. To foster and sustain an ecosystem of open source projects
<br>D. To define mandatory cloud provider APIs
<br>E. To own the intellectual property of Linux
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: The CNCF hosts and promotes a wide range of open source
projects (including Kubernetes, Prometheus, Envoy) to advance cloud native computing, providing governance, support, and community building.

---

<!-- note:1755880861102 model:Basic++ -->
**Front:** In a typical cloud native environment, which persona<b> is most
concerned with</b> ensuring application uptime, performance, and
managing incident response?<br><br>A. Application Developer
<br>B. Platform Consumer
<br>C. Site Reliability Engineer (SRE) / Platform Operator
<br>D. Business Analyst
<br>E. End User
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: SREs and Platform Operators are responsible for the reliability, scalability, and overall operational health of the platform and the
applications running on it, including monitoring, alerting, and incident
management.

---

<!-- note:1755881877995 model:Basic++ -->
**Front:** Which of the following is NOT a core characteristic of cloud
native architectures?<div><br>A. Microservices
<br>B. Containers
<br>C. Monolithic application design
<br>D. DevOps practices
<br>E. Automation</div>
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: Cloud native architectures typically favor microservices,
containers, dynamic orchestration (like Kubernetes), and DevOps/Agile
practices, moving away from large, tightly coupled monolithic designs.

---

<!-- note:1755882478920 model:Basic++ -->
**Front:** What is a primary characteristic of Vertical Pod Autoscaling
(VPA)?&nbsp;<div><br></div><div>A. It adjusts the number of Pod replicas.
<br>B. It adjusts the CPU and memory requests and limits for Pods.
<br>C. It adds or removes Nodes from the cluster.
<br>D. It automatically selects the optimal storage class.
<br>E. It scales the number of available IP addresses.</div>
**Back:** Correct Answer: <b>B</b>
<br><br><b>Explanation</b>: VPA recommends or automatically updates the resource
requests and limits for containers within Pods to match actual usage,
helping to optimize resource allocation. It does not change the number of
replicas (that’s HPA).

---

<!-- note:1755882853962 model:Basic++ -->
**Front:** Which of these is a <b>primary </b>goal of the CNCF’s "Trail Map" for
cloud native adoption?
<br><br>A. To mandate specific vendor products for each stage.
<br>B. To provide a prescriptive path for building cloud native apps.
<br>C. To offer a recommended journey and project choices for adopters.
<br>D. To rank cloud providers based on their Kubernetes offerings.
<br>E. To certify individual developers as cloud native experts.
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: The CNCF Trail Map suggests a path for organizations
adopting cloud native technologies, highlighting CNCF projects that can
help at different stages (e.g., containerization, CI/CD, orchestration, observability).

---

<!-- note:1755882964773 model:Basic++ -->
**Front:** What is the <b>primary </b>motivation behind using ”Serverless Functions” (FaaS)?<div>&nbsp;
<br>A. To achieve higher compute density on physical servers.
<br>B. To run long-lived, stateful batch processing jobs.
<br>C. To execute event-driven code without managing infrastructure.&nbsp;<div>D. To gain fine-grained control over OS-level configurations.
<br>E. To build complex, monolithic application backends.</div></div>
**Back:** Correct Answer: <b>C</b>
<br><br><b>Explanation</b>: Serverless functions are designed for short-lived, eventdriven computations where the underlying infrastructure (servers, OS) is
completely managed by the platform, allowing developers to focus on code.

---

<!-- note:1756920574395 model:Basic++ -->
**Front:** <div>What type of software package bundles application code with all its dependencies, libraries, and configuration files?</div><div><br></div><div>A. Virtual Machine</div><div>B. Container</div><div>C. Operating System</div><div>D. Serverless Function</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div><div><b>Explanation</b>: Containers package application code and dependencies together, isolating them from the underlying infrastructure.</div>

---

<!-- note:1756921658932 model:Basic++ -->
**Front:** <div>What is <b>the primary purpose</b> of a Service Mesh like Istio or Linkerd?</div><div><br></div><div>A. Container image building</div><div>B. Cluster storage management</div><div>C. Managing inter-service comms</div><div>D. Node provisioning</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: Service meshes add observability, security, and reliability features to communication between microservices (service-to-service).</div>

---

<!-- note:1756922958222 model:Basic++ -->
**Front:** <div>Which mechanism allows Kubernetes to automatically adjust the number of Pods in a Deployment based on CPU utilization or custom metrics?</div><div><br></div><div>A. Vertical Pod Autoscaler (VPA)</div><div>B. Cluster Autoscaler (CA)</div><div>C. Horizontal Pod Autoscaler (HPA)</div><div>D. Node Problem Detector (NPD)</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: The HPA automatically scales the number of Pod replicas based on observed metrics like CPU or memory usage.</div>

---

<!-- note:1756923052337 model:Basic++ -->
**Front:** <div>What term describes an architectural approach where applications are built as small, independent services that run in their own processes?</div><div><br></div><div>A. Monolithic</div><div>B. Microservices</div><div>C. Serverless</div><div>D. N-Tier</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div><div><b>Explanation</b>: Microservices architecture structures an application as a collection of loosely coupled, independently deployable services.</div>

---

<!-- note:1756923133935 model:Basic++ -->
**Front:** <div>What does ”Serverless” computing primarily abstract away from the developer?</div><div><br></div><div><div>A. Networking</div><div>B. Storage</div><div>C. Server Management</div><div>D. Operating System choice</div></div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: Serverless platforms (like FaaS) manage the underlying infrastructure, allowing developers to focus solely on code execution.</div>

---

<!-- note:1756923163328 model:Basic++ -->
**Front:** <div>Which organization hosts Kubernetes and promotes the growth of the cloud native ecosystem?</div><div><br></div><div>A. Linux Foundation (LF)</div><div>B. Apache Software Foundation (ASF)</div><div>C. Cloud Native Computing Foundation (CNCF)</div><div>D. Open Source Initiative (OSI)</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: The CNCF, part of the Linux Foundation, stewards Kubernetes and many other cloud native projects.</div>

---

<!-- note:1756923197607 model:Basic++ -->
**Front:** <div>What is the benefit of using open standards in cloud native technologies?</div><div><br></div><div>A. Vendor lock-in</div><div>B. Increased complexity</div><div>C. Interoperability Portability</div><div>D. Reduced security</div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: Open standards (like OCI, CRI, CNI) ensure that different tools and platforms can work together, preventing vendor lock-in.</div>

---

<!-- note:1756923227133 model:Basic++ -->
**Front:** <div>In a typical cloud native environment, which persona is <b>primarily responsible</b> for designing and building the application?</div><div><br></div><div>A. Operator</div><div>B. Developer</div><div>C. Site Reliability Engineer (SRE)</div><div>D. Security Engineer</div>
**Back:** <div>Correct Answer: <b>B<br><br></b></div><div><b>Explanation</b>: Developers focus on writing, building, and testing the application code that runs within the cloud native platform.</div>

---

<!-- note:1756923272014 model:Basic++ -->
**Front:** <div>Which persona is typically focused on the reliability, scalability, and maintenance of the underlying Kubernetes platform?</div><div><br></div><div>A. End User</div><div><div>B. Application Developer</div><div>C. Platform Operator / SRE</div><div>D. Data Scientist</div></div>
**Back:** <div>Correct Answer: <b>C</b></div><div><br></div><div><b>Explanation</b>: Operators or SREs manage the Kubernetes cluster itself, ensuring it’s healthy, scalable, and available for developers.</div>

---

<!-- note:1767560194445 model:Basic+++ -->
**Front:** Which are key service mesh features? Select two answers<br><br><div>A. Load balancing and discovery<br> B. mTLS security<br> C. Image storage<br> D. CI/CD automation</div>
**Back:** <div>Correct Answers: <b>A</b> and<b> B</b></div><div><br></div>
<div><b>Explanation</b>: Service meshes handle traffic management and secure service-to-service communication.</div>

---

<!-- note:1767560833637 model:Basic+++ -->
**Front:** How do service meshes benefit microservices? <br><br><div>A. Network abstractions<br> B. Centralized logging<br> C. Remove containers<br> D. Auto-scale servers</div>
**Back:** <div>Correct Answer: <b>A</b></div><div><br></div> <div><b>Explanation</b>: They abstract networking concerns away from application code.</div>

---

<!-- note:1767561260722 model:Basic+++ -->
**Front:** What is a key serverless characteristic? <br><br><div>A. Manual scaling<br> B. Pay per execution time<br> C. Server management<br> D. Manual start/stop</div>
**Back:** <div>Correct Answer: <b>B</b></div><div><br></div> <div><b>Explanation</b>: Serverless charges based on actual compute usage.</div>

---

<!-- note:1767561281344 model:Basic+++ -->
**Front:** What does FaaS stand for? <br><br><div>A. Function as a Service<br> B. File as a Service<br> C. Fragmentation as a Service<br> D. Framework as a Service</div>
**Back:** <div>Correct Answer: <b>A</b></div><div><br></div> <div><b>Explanation</b>: FaaS allows execution of functions without managing servers.</div>

---
