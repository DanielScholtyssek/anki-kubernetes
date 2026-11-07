# KCNA - Kubernetes and Cloud Native Associate — Cloud Native Observability

> Deck: `KCNA - Kubernetes and Cloud Native Associate` · Group: `Cloud Native Observability` · Notes: 29 · Models: Cloze, Many

<!-- note:1793915843459 model:Many -->
**Domain:** Prometheus - metric types
**Question:** Which metric type can go up and down in Prometheus?
**Options:** A. Gauge<br>B. Histogram<br>C. Counter<br>D. “Percentile”
**Answer:** A – Gauge
**Explanation:** Gauges represent values that can go up AND down — memory usage, queue depth, temperature, current connections. A Counter is monotonically increasing (requests_total, errors_total — only resets on process restart), so you query it with rate()/increase() rather than reading it directly. Histogram samples observations into configurable buckets for distribution/quantile math — it's not a scalar that 'goes up and down'. 'Percentile' isn't a metric type at all — it's a computed statistic (histogram_quantile() in PromQL). Fourth real type: Summary, client-side quantiles.
**Sources:** <a href="https://prometheus.io/docs/concepts/metric_types/" target="_blank">Prometheus Docs - Metric types</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus

---

<!-- note:1793920396321 model:Many -->
**Domain:** PromQL - functions
**Question:** In PromQL, which function is used to get the per-second rate of a counter?
**Options:** A. rate()<br>B. count()<br>C. sum()<br>D. max_over_time()
**Answer:** A (1) – rate()
**Explanation:** rate() takes a RANGE vector — rate(http_requests_total[5m]) — and extrapolates the counter's increase to a per-second rate, correctly handling counter resets (a restart dropping the value to 0 doesn't skew the result). It's THE function for counters; increase() does the same over the window without dividing by time. The distractors: count() counts the number of elements in a vector, sum() aggregates values across series, and max_over_time() is a range function returning the maximum SAMPLE VALUE seen — none compute a rate.
**Sources:** <a href="https://prometheus.io/docs/prometheus/latest/querying/functions/" target="_blank">Prometheus Docs - Query functions</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::promql

---

<!-- note:1793920618409 model:Many -->
**Domain:** Prometheus - metric selection
**Question:** Which Prometheus metric type is best for tracking request latency distributions?
**Options:** A. Histogram<br>B. Counter<br>C. Summary<br>D. Gauge
**Answer:** A (1) – Histogram
**Explanation:** Histograms bucket each observation into configurable ranges (the le buckets), so request durations can be turned into real quantiles server-side: histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m])). Summary is the sophisticated distractor — it also computes quantiles, but CLIENT-side at fixed φ values baked into the metric: you can't aggregate summaries across pods or pick a different quantile later. Counter only counts monotonically upward; Gauge is a single up/down scalar — neither describes a distribution.
**Sources:** <a href="https://prometheus.io/docs/practices/histograms/" target="_blank">Prometheus Docs - Histograms and summaries</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus

---

<!-- note:1793920683153 model:Many -->
**Domain:** PromQL - rate vs increase
**Question:** In PromQL, which function computes the total increase of a counter over a window?
**Options:** A. increase()<br>B. histogram_quantile()<br>C. avg()<br>D. irate()
**Answer:** A (1) – increase()
**Explanation:** increase(counter[1h]) returns the TOTAL rise of the counter across the window — extrapolated to cover the full range and corrected for counter resets. rate() is literally increase() divided by the window's seconds, giving per-second change. irate() is the instant-rate sibling: it uses only the last two samples, so it reacts fastest but is the noisiest — never use it for totals. histogram_quantile() computes quantiles from histogram buckets; avg() averages an instant vector's values.
**Sources:** <a href="https://prometheus.io/docs/prometheus/latest/querying/functions/" target="_blank">Prometheus Docs - Query functions</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::promql

---

<!-- note:1793921550156 model:Many -->
**Domain:** PromQL - histogram_quantile
**Question:** Which function is used to compute p95 from histogram buckets?
**Options:** A. histogram_quantile()<br>B. bucket_rate()<br>C. percentile()<br>D. quantile()
**Answer:** A (1) – histogram_quantile()
**Explanation:** histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) estimates p95 by interpolating inside the histogram's le (less-than-or-equal) buckets — it needs the _bucket series, which is why it's wrapped around rate() for counters. It computes the quantile WITHIN one histogram's distribution. The distractors don't exist as bucket-quantile functions: bucket_rate() and percentile() aren't PromQL functions at all. Note the real quantile() aggregation operator DOES exist in PromQL — but it computes a quantile ACROSS multiple series' values (like avg/sum), it cannot derive p95 from histogram buckets.
**Sources:** <a href="https://prometheus.io/docs/prometheus/latest/querying/functions/#histogram_quantile" target="_blank">Prometheus Docs - histogram_quantile</a>
**Tags:** k8s::kcna src::session topic::prometheus topic::promql

---

<!-- note:1794079087773 model:Many -->
**Domain:** Observability - practices select-two
**Question:** Which TWO are recommended practices for achieving observability in a Kubernetes cluster?
**Options:** A. Use a single centralized logging solution to aggregate logs from all components<br>B. Store all debug logs for a minimum of 90 days for compliance<br>C. Include correlation IDs in structured logs to enable tracing across services<br>D. Disable leader election for monitoring components to reduce complexity<br>E. Use Prometheus with a pull-based model to scrape metrics from pods
**Answer:** C, E – correlation IDs for tracing + Prometheus pull-based scraping
**Explanation:** (Select TWO) Correlation IDs in structured logs let you stitch one request's journey across pods/services — essential for microservices debugging. Prometheus' pull model is the Kubernetes standard: the server scrapes /metrics endpoints on its own schedule, so targets can't flood it and it's easy to scale horizontally. The rejected options are all anti-patterns: a SINGLE centralized log sink is a SPOF (prefer HA/aggregation layers); debug logs aren't compliance data (audit logs are — selective retention); leader election in HA monitoring PREVENTS duplicate scraping/alerting, disabling it causes duplicates.
**Sources:** <a href="https://kubernetes.io/docs/concepts/cluster-administration/logging/" target="_blank">Kubernetes Docs - Logging Architecture</a>
**Tags:** k8s::kcna src::session topic::logging topic::metrics topic::observability

---

<!-- note:1794079087774 model:Many -->
**Domain:** Observability - pull vs push
**Question:** How does Prometheus primarily collect metrics?
**Options:** A. Prometheus pulls — it scrapes targets on its schedule; push only happens via Pushgateway for jobs that can't be scraped<br>B. Applications push metrics directly to Prometheus storage<br>C. Prometheus requires agents on every pod to push metrics<br>D. Pull and push are equivalent — it's just a config choice
**Answer:** A (1) – Prometheus pulls — it scrapes targets on its schedule; push only happens via Pushgateway for jobs that can't be scraped
**Explanation:** Prometheus is pull-based by design: it periodically HTTP-scrapes each target's /metrics endpoint. Advantages: the server controls scrape rate/targets, targets can't overwhelm it, dead targets are detected (up=0) rather than silently stale, and it's horizontally scalable. The exception is the PUSHGATEWAY — for short-lived batch jobs that may not exist when Prometheus scrapes; they push metrics to it instead. Alertmanager is also pull-adjacent (it pulls alerts from Prometheus).
**Sources:** <a href="https://prometheus.io/docs/introduction/overview/" target="_blank">Prometheus Docs - Overview</a>
**Tags:** k8s::kcna src::session topic::metrics topic::observability topic::prometheus

---

<!-- note:1794079087783 model:Cloze -->
**Text:** Observability practices that exams test:<br><br>{{c1::Correlation IDs}} in structured logs → trace one request across services<br>{{c2::Prometheus pull model}} → server scrapes /metrics; standard for K8s<br>{{c3::Pushgateway}} → the exception: short-lived jobs that can't be scraped<br>{{c4::Leader election}} → HA monitoring needs it to avoid duplicate scrapes/alerts
**Extra:** The observability three pillars (logs/metrics/traces) each get a practice: correlation IDs make logs traceable, pull-model Prometheus scrapes metrics, and tracing systems (Jaeger/Tempo/OpenTelemetry) follow requests across services. Anti-patterns to avoid: single log sink SPOF, storing debug logs long-term, disabling leader election in HA setups.
**Tags:** k8s::kcna src::session topic::logging topic::metrics topic::observability

---

<!-- note:1794080037294 model:Many -->
**Domain:** KCNA - Cloud Native Observability
**Question:** Which type of telemetry data is most suitable for understanding the sequence of operations and latency across multiple microservices for a single user request?
**Options:** A. Logs<br>B. Metrics<br>C. Traces (Distributed Tracing)<br>D. Events<br>E. Alerts
**Answer:** C – Traces (Distributed Tracing)
**Explanation:** Distributed tracing captures the end-to-end flow of a request as it propagates through different services, providing insights into<br>latency bottlenecks and dependencies.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::mcq topic::observability

---

<!-- note:1794080037295 model:Many -->
**Domain:** KCNA - Cloud Native Observability
**Question:** Prometheus is <b>primarily </b>designed for which type of observability data?
**Options:** A. Distributed tracing<br>B. Log aggregation and analysis<br>C. Time-series metrics collection and alerting<br>D. Security auditing and compliance reporting<br>E. Real-time user monitoring (RUM)
**Answer:** C – Time-series metrics collection and alerting
**Explanation:** Prometheus excels at collecting, storing, and querying<br>time-series data (metrics) from various targets, and it includes a powerful<br>alerting mechanism based on PromQL.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::mcq topic::observability

---

<!-- note:1794080037296 model:Many -->
**Domain:** KCNA - Cloud Native Observability
**Question:** In Prometheus, what is an ”exporter”?
**Options:** A. A component that sends alerts to notification channels<br>B. A database that stores long-term metric data<br>C. A client library for instrumenting application code<br>D. A piece of software that exposes metrics from third-party systems<br>E. A dashboard for visualizing metrics
**Answer:** D – A piece of software that exposes metrics from third-party systems
**Explanation:** Exporters are helper services that fetch metrics from systems that don’t natively expose them in Prometheus format (e.g., databases,<br>hardware, message queues) and translate them into a format Prometheus<br>can scrape.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::mcq topic::observability

---

<!-- note:1794080037297 model:Many -->
**Domain:** KCNA - Cloud Native Observability
**Question:** What is a key challenge in cost management specifically related to shared Kubernetes clusters?
**Options:** A. High cost of Kubernetes control plane components<br>B. Difficulty in attributing resource usage to specific teams/apps<br>C. Inability to use reserved instances with Kubernetes<br>D. Lack of tools for visualizing overall cloud spend<br>E. Fixed pricing models for all Kubernetes services
**Answer:** B – Difficulty in attributing resource usage to specific teams/apps
**Explanation:** In multi-tenant clusters, accurately tracking and attributing resource consumption (CPU, memory, storage, network) to different<br>applications, teams, or cost centers can be complex due to the shared<br>nature of resources.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::mcq topic::observability

---

<!-- note:1794080037298 model:Many -->
**Domain:** KCNA - Cloud Native Observability
**Question:** Which of the following best describes the concept of "desired state" in Kubernetes?
**Options:** A. The current operational status of cluster nodes<br>B. The configuration specified by the user for their resources<br>C. The real-time metrics collected by Prometheus<br>D. The log output generated by running containers<br>E. The network policies applied to Pods
**Answer:** B – The configuration specified by the user for their resources
**Explanation:** Users define the desired state of their applications and infrastructure via Kubernetes API objects (e.g., in YAML files). Kubernetes<br>controllers then continuously work to make the actual state of the cluster<br>match this desired state.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::mcq topic::observability

---

<!-- note:1794080037299 model:Many -->
**Domain:** KCNA - Cloud Native Observability
**Question:** Which statement accurately describes a key aspect of ”observability” in cloud native systems?
**Options:** A. It is solely focused on collecting system logs.<br>B. It primarily relies on manual health checks by operators.<br>C. It enables understanding a system’s internal state from its outputs.<br>D. It is achieved by using proprietary monitoring tools.<br>E. It is only relevant for production environments.
**Answer:** C – It enables understanding a system’s internal state from its outputs.
**Explanation:** Observability is the ability to infer the internal state and<br>behavior of a complex system by examining its outputs (logs, metrics,<br>traces). This allows for better troubleshooting, understanding performance, and proactive issue detection.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::mcq topic::observability

---

<!-- note:1794080037300 model:Many -->
**Domain:** KCNA - Cloud Native Observability
**Question:** In Prometheus, what does the "up" metric typically indicate for a scraped target?
**Options:** A. The version number of the target application.<br>B. The number of active user connections to the target.<br>C. Whether Prometheus was able to successfully scrape the target.<br>D. The CPU utilization of the target.<br>E. The total uptime of the target since it started.
**Answer:** C – Whether Prometheus was able to successfully scrape the target.
**Explanation:** The upjob=””, instance=””<br>metric is automatically generated by Prometheus. A value of 1 means<br>the scrape was successful; 0 means it failed. This is fundamental for<br>monitoring target health.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::mcq topic::observability

---

<!-- note:1794080037301 model:Many -->
**Domain:** KCNA - Cloud Native Observability
**Question:** From a FinOps perspective in a Kubernetes environment, why is tagging resources (e.g., with labels) important?
**Options:** A. It improves the scheduling efficiency of Pods.<br>B. It enables more accurate cost allocation and showback/chargeback.<br>C. It automatically secures inter-Pod communication.<br>D. It increases the performance of PersistentVolumes.<br>E. It simplifies the process of upgrading Kubernetes.
**Answer:** B – It enables more accurate cost allocation and showback/chargeback.
**Explanation:** Labels and annotations applied to Kubernetes resources<br>(Namespaces, Deployments, Pods, etc.) can be used by cost management<br>tools to categorize and attribute costs to different teams, projects, or applications, supporting FinOps practices.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::mcq topic::observability

---

<!-- note:1794080037302 model:Many -->
**Domain:** KCNA - Cloud Native Observability
**Question:** When instrumenting an application for Prometheus, what is the typical way metrics are exposed by the application?
**Options:** A. Writing metrics directly to Prometheus’s storage.<br>B. Pushing metrics to a Prometheus Pushgateway.<br>C. Exposing an HTTP endpoint (e.g., /metrics) for scraping.<br>D. Sending metrics via syslog to a collector.<br>E. Using SNMP traps to send metric data.
**Answer:** C – Exposing an HTTP endpoint (e.g., /metrics) for scraping.
**Explanation:** Applications instrumented with Prometheus client libraries<br>typically expose their metrics on an HTTP endpoint (commonly /metrics)<br>in a specific format that Prometheus can then periodically scrape.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::mcq topic::observability

---

<!-- note:1794080037303 model:Many -->
**Domain:** KCNA - Cloud Native Observability
**Question:** What are the three pillars of observability in cloud native systems?
**Options:** A. Alerts, Dashboards, Reports<br>B. Logs, Metrics, Traces<br>C. Monitoring, Logging, Profiling<br>D. Scaling, Scheduling, Storing
**Answer:** B – Logs, Metrics, Traces
**Explanation:** Logs (events), Metrics (measurements over time), and Traces (request flows) are considered the fundamental pillars of observability.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::mcq topic::observability

---

<!-- note:1794080037304 model:Many -->
**Domain:** KCNA - Cloud Native Observability
**Question:** What type of telemetry data records discrete events that happened at a specific time?
**Options:** A. Metrics<br>B. Traces<br>C. Logs<br>D. Profiles
**Answer:** C – Logs
**Explanation:** Explanation: Logs provide timestamped records of events, often used for debugging or auditing.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::mcq topic::observability

---

<!-- note:1794080037305 model:Many -->
**Domain:** KCNA - Cloud Native Observability
**Question:** What type of telemetry data represents a measurement sampled over time, often aggregated?
**Options:** A. Metrics<br>B. Traces<br>C. Logs<br>D. Events
**Answer:** A – Metrics
**Explanation:** Metrics are numerical values tracked over time (e.g., CPU usage, request count) used for monitoring trends and performance.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::mcq topic::observability

---

<!-- note:1794080037306 model:Many -->
**Domain:** KCNA - Cloud Native Observability
**Question:** What type of telemetry data shows the path and duration of a request as it flows through multiple services?
**Options:** A. Metrics<br>B. Traces<br>C. Logs<br>D. Alerts
**Answer:** B – Traces
**Explanation:** Explanation: Traces (specifically distributed traces) track a request’s journey across different microservices, identifying bottlenecks.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::mcq topic::observability

---

<!-- note:1794080037307 model:Many -->
**Domain:** KCNA - Cloud Native Observability
**Question:** Which open-source monitoring system, graduated by the CNCF, is widely used for collecting and querying time-series metrics in Kubernetes?
**Options:** A. Grafana<br>B. Jaeger<br>C. Prometheus<br>D. Fluentd
**Answer:** C – Prometheus
**Explanation:** Prometheus is the de facto standard for metrics collection and alerting in the Kubernetes ecosystem.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::mcq topic::observability

---

<!-- note:1794080037308 model:Many -->
**Domain:** KCNA - Cloud Native Observability
**Question:** How does Prometheus typically gather metrics from applications and infrastructure?
**Options:** A. Pushing metrics to endpoints<br>B. Pulling metrics via scraping<br>C. Reading log files directly<br>D. Using kernel probes
**Answer:** B – Pulling metrics via scraping
**Explanation:** Prometheus operates on a pull model, periodically scraping HTTP endpoints exposed by targets (applications, exporters) for metrics.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::mcq topic::observability

---

<!-- note:1794080037309 model:Many -->
**Domain:** KCNA - Cloud Native Observability
**Question:** What language is used to write queries in Prometheus?
**Options:** A. SQL<br>B. PromQL<br>C. JSONPath<br>D. YAML
**Answer:** B – PromQL
**Explanation:** PromQL (Prometheus Query Language) is the powerful functional query language used to select and aggregate time series data.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::mcq topic::observability

---

<!-- note:1794080037310 model:Many -->
**Domain:** KCNA - Cloud Native Observability
**Question:** In cloud native cost management, what does ”FinOps” <b>primarily </b>focus on?
**Options:** A. Optimizing application code<br>B. Managing cloud spending<br>C. Improving network security<br>D. Automating deployments
**Answer:** B – Managing cloud spending
**Explanation:** FinOps is a cultural practice and framework that brings financial accountability to the variable spend model of the cloud.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::mcq topic::observability

---

<!-- note:1794080037311 model:Many -->
**Domain:** KCNA - Cloud Native Observability
**Question:** Why can cost management be challenging in Kubernetes environments?
**Options:** A. Lack of monitoring tools<br>B. Shared resources dynamic workloads<br>C. Fixed infrastructure costs<br>D. Infrequent deployments
**Answer:** B – Shared resources dynamic workloads
**Explanation:** The shared nature of cluster resources and the dynamic scaling of workloads make it difficult to attribute costs accurately.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::mcq topic::observability

---

<!-- note:1794080037312 model:Many -->
**Domain:** KCNA - Cloud Native Observability
**Question:** Which tool is commonly used to visualize Kubernetes metrics?
**Options:** A. Docker<br>B. Grafana<br>C. GitHub<br>D. Ansible
**Answer:** B – Grafana
**Explanation:** Grafana is widely used to visualize metrics collected from monitoring systems.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::mcq topic::observability

---

<!-- note:1794080037313 model:Many -->
**Domain:** KCNA - Cloud Native Observability
**Question:** What is the primary purpose of Prometheus?
**Options:** A. Deployment<br>B. Source control<br>C. Monitoring and alerting<br>D. Network security
**Answer:** C – Monitoring and alerting
**Explanation:** Prometheus collects metrics and triggers alerts based on defined rules.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::mcq topic::observability

---

<!-- note:1794080037424 model:Many -->
**Domain:** KCNA - Kubernetes Fundamentals
**Question:** Which component provides metrics for autoscaling?
**Options:** A. Kube-scheduler<br>B. Controller Manager<br>C. Metrics Server<br>D. Kubelet
**Answer:** C – Metrics Server
**Explanation:** Metrics Server collects resource usage metrics used by HPA.
**Sources:** 
**Tags:** k8s::kcna src::deck-import topic::fundamentals topic::mcq

---
