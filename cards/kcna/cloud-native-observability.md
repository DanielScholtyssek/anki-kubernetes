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
**Back Extra:** The observability three pillars (logs/metrics/traces) each get a practice: correlation IDs make logs traceable, pull-model Prometheus scrapes metrics, and tracing systems (Jaeger/Tempo/OpenTelemetry) follow requests across services. Anti-patterns to avoid: single log sink SPOF, storing debug logs long-term, disabling leader election in HA setups.
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

<!-- note:1794081862020 model:Many -->
**Domain:** Observability - tracing span
**Question:** In the context of distributed tracing, what is a 'span'?
**Options:** A. A metric that measures request latency<br>B. A tool for collecting logs from containers<br>C. The entire end-to-end transaction across services<br>D. A single logical operation within a service, with a start and end time
**Answer:** D (4) – A single logical operation within a service, with a start and end time
**Explanation:** A span = ONE named, timed operation inside a service (e.g. 'GET /api/users', 'db.query'). Spans nest to form a TRACE — the end-to-end journey of one request across services. Root span = the incoming request; child spans = downstream calls. Distractors: latency metric = metrics pillar; log collector = logging pillar; whole transaction = that's the TRACE, not a span.
**Sources:** <a href="https://opentelemetry.io/docs/concepts/signals/traces/" target="_blank">OpenTelemetry Docs - Traces</a>
**Tags:** k8s::kcna topic::observability topic::tracing src::session

---

<!-- note:1794081862021 model:Many -->
**Domain:** Observability - trace vs span
**Question:** What is the relationship between a trace and a span in distributed tracing?
**Options:** A. Span = whole request; trace = one operation<br>B. Trace = the end-to-end request journey across services; span = one timed operation within it<br>C. Trace and span are the same thing<br>D. Spans only exist in metrics systems
**Answer:** B (2) – Trace = the end-to-end request journey across services; span = one timed operation within it
**Explanation:** Hierarchy: TRACE (whole request, e.g. 'checkout') contains SPANS (operations: auth check, db write, payment call) which nest parent→child. Each span has name, start/end timestamps, attributes, and events. Tools: Jaeger, Zipkin, Tempo, OpenTelemetry (vendor-neutral instrumentation standard). This is the third observability pillar alongside logs and metrics — correlation IDs (already carded) are what let you JOIN traces to log lines.
**Sources:** <a href="https://opentelemetry.io/docs/concepts/signals/traces/" target="_blank">OpenTelemetry Docs - Traces</a>
**Tags:** k8s::kcna topic::observability topic::tracing src::session

---

<!-- note:1794082944798 model:Many -->
**Domain:** Observability - log collection
**Question:** A DevOps team wants to collect and forward logs from all nodes in a Kubernetes cluster to a centralized logging backend. Which component is specifically designed for lightweight log collection and forwarding?
**Options:** A. Fluent Bit<br>B. Prometheus<br>C. Jaeger<br>D. Grafana
**Answer:** A (1) – Fluent Bit
**Explanation:** Fluent Bit = lightweight, low-memory log shipper, deployed as a DaemonSet (one pod per node) that tails container logs and forwards to a backend (Elasticsearch, Loki, CloudWatch, etc.). The observability tool map: Prometheus = METRICS scraping; Jaeger/Tempo = TRACES; Grafana = visualization only (queries backends, collects nothing); Fluent Bit/Fluentd/Promtail = LOG collection/forwarding.
**Sources:** <a href="https://fluentbit.io/" target="_blank">Fluent Bit</a>
**Tags:** k8s::kcna topic::observability topic::logging src::session

---

<!-- note:1794082944799 model:Many -->
**Domain:** Observability - fluent bit vs fluentd
**Question:** What is the key difference between Fluent Bit and Fluentd for Kubernetes log collection?
**Options:** A. Fluent Bit is heavier and more feature-rich than Fluentd<br>B. Fluent Bit = lightweight shipper (C, low memory, DaemonSet); Fluentd = heavier processor with richer filtering/transformation<br>C. Fluentd replaced Fluent Bit as the CNCF standard<br>D. They are interchangeable with no meaningful difference
**Answer:** B (2) – Fluent Bit = lightweight shipper (C, low memory, DaemonSet); Fluentd = heavier processor with richer filtering/transformation
**Explanation:** Both are CNCF graduated log processors but sized differently: Fluent Bit is C-based, ~1MB memory footprint, built for edge/node-level tailing-and-shipping on every node via DaemonSet. Fluentd is Ruby-based, heavier, supports complex filtering/parsing/routing — used when you need rich processing, often behind Fluent Bit in a two-tier pipeline (Bit collects at edge → Fluentd aggregates centrally). Modern alternatives: Promtail/Grafana Alloy, Vector, Filebeat.
**Sources:** <a href="https://fluentbit.io/faqs/" target="_blank">Fluent Bit FAQ</a>
**Tags:** k8s::kcna topic::observability topic::logging src::session

---

<!-- note:1794360041360 model:Many -->
**Domain:** Observability - definition
**Question:** Which statement best defines observability in cloud-native systems?
**Options:** A. The ability to understand and measure a system's state from data the system itself generates, enabling actionable insight into unexpected scenarios in dynamic environments<br>B. Checking a fixed set of predefined health metrics against thresholds at regular intervals<br>C. Collecting and storing all application logs centrally for compliance and auditing<br>D. Automatically restarting failed containers to preserve service availability
**Answer:** A (1) – Understand/measure system state from system-generated data → actionable insight for unexpected scenarios
**Explanation:** From control theory (via the CNCF observability whitepaper): observability is 'a measure of how well internal states of a system can be inferred from knowledge of its external outputs.' You don't add probes — you infer internal state from the telemetry the system emits. B describes MONITORING (known checks against thresholds), C is just centralized logging, D is self-healing — a Kubernetes controller job, not observability. The phrase 'data generated by the system' is the key: the system's own outputs become the evidence.
**Sources:** <a href="https://github.com/cncf/tag-observability/blob/main/whitepaper.md" target="_blank">CNCF TAG Observability - Whitepaper</a>
**Tags:** k8s::kcna src::session topic::observability topic::monitoring

---

<!-- note:1794360041361 model:Many -->
**Domain:** Observability - vs monitoring
**Question:** What primarily distinguishes observability from conventional monitoring?
**Options:** A. Observability infers internal state from arbitrary system outputs to debug unknown failure modes; monitoring checks known signals against predefined thresholds<br>B. Observability replaces monitoring entirely — thresholds and alerts are obsolete<br>C. Monitoring uses logs while observability uses only metrics<br>D. Observability applies only to production systems while monitoring applies everywhere
**Answer:** A (1) – Observability infers internal state from arbitrary outputs for unknown failure modes; monitoring checks known signals vs thresholds
**Explanation:** Monitoring = known-unknowns: you pick signals in advance (CPU, error rate, latency) and alert when they cross thresholds — great for expected failure modes. Observability = unknown-unknowns: distributed systems fail in ways nobody predicted, so you emit rich telemetry (logs/metrics/traces) and reconstruct internal state after the fact. They complement each other — observability doesn't eliminate monitoring. The whitepaper even frames metrics themselves as efficient for 'known unknowns'; traces and logs carry the 'why'.
**Sources:** <a href="https://github.com/cncf/tag-observability/blob/main/whitepaper.md" target="_blank">CNCF TAG Observability - Whitepaper</a>
**Tags:** k8s::kcna src::session topic::observability topic::monitoring

---

<!-- note:1794360041362 model:Many -->
**Domain:** Observability - benefits
**Question:** Which are benefits of observability in cloud-native systems? (Select all that apply)
**Options:** A. Deeper insight into the internal workings of systems and applications<br>B. Faster troubleshooting and detection of problems that are hard to catch<br>C. Performance monitoring and better cross-team collaboration<br>D. Guaranteed prevention of all production incidents<br>E. No need to instrument application code
**Answer:** A, B, C – insight into internals + faster/hard-to-catch troubleshooting + performance monitoring/collaboration
**Explanation:** Observability turns scattered telemetry into actionable insight: you see inside services and applications (A), debug faster including subtle distributed failures that are hard to catch (B), watch performance trends and share one telemetry picture across dev/ops teams (C). D overpromises — observability helps you FIND and fix problems faster; it doesn't prevent them. E is backwards: observability REQUIRES instrumentation (manual, or automatic via service mesh sidecars / eBPF) to emit telemetry in the first place.
**Sources:** <a href="https://github.com/cncf/tag-observability/blob/main/whitepaper.md" target="_blank">CNCF TAG Observability - Whitepaper</a>
**Tags:** k8s::kcna src::session topic::observability topic::monitoring

---

<!-- note:1794360041363 model:Many -->
**Domain:** Observability - microservices need
**Question:** Why do microservices architectures create a greater need for observability than monoliths?
**Options:** A. There is no single log source — one request fans out across many services, pods, and nodes, so you need correlation (trace IDs, spans) to learn WHY something failed, not just THAT it failed<br>B. Microservice containers inherently consume more CPU than monolith processes<br>C. Microservices are inherently less reliable than monoliths<br>D. Microservices require more frequent security audits
**Answer:** A (1) – No single log source; requests fan out across services/pods/nodes → need trace IDs + spans to learn WHY, not just THAT
**Explanation:** In a monolith, one request = one process = one readable log stream. In microservices the same request touches N services on N pods on N nodes — logs scatter across the cluster and timing fragments. Observability (distributed tracing with trace IDs + spans, centralized logs carrying correlation IDs, per-service metrics) is what stitches the request back together and answers WHY. B is not the driver (resource use is workload-dependent). C is a misconception — microservices often IMPROVE reliability via fault isolation. D is a security concern, not an observability one.
**Sources:** <a href="https://opentelemetry.io/docs/concepts/signals/traces/" target="_blank">OpenTelemetry Docs - Traces</a>
**Tags:** k8s::kcna src::session topic::observability topic::microservices

---

<!-- note:1794360041364 model:Many -->
**Domain:** Observability - logs anatomy
**Question:** What does a log fundamentally consist of?
**Options:** A. A timestamped record of a discrete event — a timestamp plus a message, typically enriched with structured fields like severity, service, and trace ID<br>B. A numerical measurement sampled at intervals, aggregated into a timeseries<br>C. A tree of timed operations showing how one request flowed through services<br>D. A binary snapshot of a crashed process's memory for post-mortem analysis
**Answer:** A (1) – Timestamped record of a discrete event: timestamp + message, enriched with structured fields
**Explanation:** Logs = records of events that occurred: timestamp + message is the minimum; production logs add structured fields (level, service, pod, trace_id) so they can be searched and correlated across services. B describes METRICS (name+labels+value+timestamp), C describes TRACES (trace-id + spans), D describes crash dumps — one of the newer signals beyond the classic three pillars.
**Sources:** <a href="https://github.com/cncf/tag-observability/blob/main/whitepaper.md" target="_blank">CNCF TAG Observability - Whitepaper</a>
**Tags:** k8s::kcna src::session topic::observability topic::logging

---

<!-- note:1794360041365 model:Many -->
**Domain:** Observability - metrics anatomy
**Question:** Which components make up one metric data point (one timeseries)?
**Options:** A. Metric name + dimensions (labels) + value + timestamp<br>B. Trace ID + span ID + parent span ID + duration<br>C. Timestamp + severity level + freeform message text<br>D. Service name + HTTP method + status code only
**Answer:** A (1) – Metric name + dimensions (labels) + value + timestamp = one timeseries
**Explanation:** A metric = a name (what is measured, e.g. http_requests_total) + dimensions/labels identifying the series (service="api", pod="web-3") + a numerical value + timestamp. Each unique name+label combination is one timeseries. B is a span's identity fields (traces), C is a log line, D lists only some possible labels — labels are open-ended key-value pairs, not a fixed field set.
**Sources:** <a href="https://prometheus.io/docs/concepts/data_model/" target="_blank">Prometheus Docs - Data model</a>
**Tags:** k8s::kcna src::session topic::observability topic::metrics

---

<!-- note:1794360041366 model:Many -->
**Domain:** Observability - cardinality
**Question:** What is metric cardinality and why does high cardinality hurt?
**Options:** A. The number of unique label combinations (timeseries) for a metric — unbounded labels like PID or user-ID explode the series count, driving storage and cost blowups<br>B. How many metrics a single pod is allowed to emit per second<br>C. The number of Prometheus replicas needed for high availability<br>D. The compression ratio of the metrics storage engine
**Answer:** A (1) – Cardinality = unique label combinations; unbounded labels (PID, user-ID) explode series count → storage/cost blowup
**Explanation:** Per the CNCF whitepaper, cardinality is 'the Achilles heel of metrics': every unique label set = one timeseries that must be scraped, stored, and queried. Adding a high-churn label (PID, request ID, user ID) can take one metric from thousands to billions of series — cost spikes or Prometheus OOM. Keep dimensions bounded and stable (pod, service, namespace — never pid/user_id/request_id); data too unique for metrics belongs in logs, traces, or events instead.
**Sources:** <a href="https://github.com/cncf/tag-observability/blob/main/whitepaper.md" target="_blank">CNCF TAG Observability - Whitepaper</a>
**Tags:** k8s::kcna src::session topic::observability topic::metrics topic::prometheus

---

<!-- note:1794360041367 model:Many -->
**Domain:** Observability - trace identifiers
**Question:** In distributed tracing, what ties all spans of one request together and encodes their relationships?
**Options:** A. A shared trace ID on every span, plus each span's own span ID and parent span ID forming a tree — propagated hop-to-hop via W3C Trace Context headers<br>B. A single log line replicated into every service's log output<br>C. The Prometheus scrape timestamp<br>D. Kubernetes labels applied to the pods
**Answer:** A (1) – Shared trace ID on every span + span ID/parent ID tree, propagated via W3C Trace Context headers
**Explanation:** Every span carries the same trace_id (grouping them into one trace) and a unique span_id; its parent_id points at the caller's span — the root span has none. W3C Trace Context (the industry standard, used by OpenTelemetry) propagates trace_id/span_id in HTTP headers (traceparent) so downstream services join the same trace automatically. Spans also record start/end timestamps (= duration), attributes, events, and status. Pod labels can't cross network hops — that's exactly why header propagation exists.
**Sources:** <a href="https://opentelemetry.io/docs/concepts/signals/traces/" target="_blank">OpenTelemetry Docs - Traces</a>
**Tags:** k8s::kcna src::session topic::observability topic::tracing

---

<!-- note:1794360041368 model:Many -->
**Domain:** Observability - primary signals
**Question:** The CNCF observability whitepaper prefers "primary signals" over "three pillars" — which signals are the additions beyond logs, metrics, and traces?
**Options:** A. Alerts and dashboards<br>B. Application profiles (continuous profiling) and crash dumps<br>C. SLIs, SLOs, and SLAs<br>D. Audit logs and security events
**Answer:** B (2) – Application profiles and crash dumps
**Explanation:** The whitepaper argues 'pillars' wrongly imply the classic three are always foundational — it calls logs/metrics/traces the PRIMARY signals and adds two emerging ones: PROFILES (continuous profiling via pprof/eBPF sampling, only a few % overhead — shows WHICH CODE consumes resources) and DUMPS (core dumps for crash forensics). A/C/D are observability-adjacent practices, not telemetry signals. Exam note: logs/metrics/traces remain the classic 'three pillars' — this is the 'and beyond' nuance.
**Sources:** <a href="https://github.com/cncf/tag-observability/blob/main/whitepaper.md" target="_blank">CNCF TAG Observability - Whitepaper</a>
**Tags:** k8s::kcna src::session topic::observability topic::monitoring

---

<!-- note:1794360041369 model:Many -->
**Domain:** Observability - tool mapping
**Question:** Which tool-to-signal pairings are correct? (Select all that apply)
**Options:** A. Prometheus → metrics: scrapes /metrics endpoints, PromQL, alerting<br>B. Fluent Bit / Fluentd → log collection and forwarding to a backend<br>C. Jaeger / Grafana Tempo → distributed traces<br>D. Prometheus → distributed traces<br>E. Grafana → collecting metrics from targets
**Answer:** A, B, C – Prometheus=metrics, Fluent Bit/Fluentd=logs, Jaeger/Tempo=traces
**Explanation:** The standard cloud-native stack: Prometheus scrapes and stores METRICS only; Fluent Bit/Fluentd (or Promtail/Vector) ship LOGS to Loki/Elasticsearch; Jaeger/Tempo store and render TRACES; OpenTelemetry is the vendor-neutral instrumentation standard that can emit all three. Grafana only QUERIES and visualizes — it collects nothing, so E is wrong. Prometheus never handles traces (D) — that's Jaeger/Zipkin/Tempo territory. This is the 'Prometheus only handles metrics' rule in ecosystem form.
**Sources:** <a href="https://github.com/cncf/tag-observability/blob/main/whitepaper.md" target="_blank">CNCF TAG Observability - Whitepaper</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::logging topic::tracing

---

<!-- note:1794362066575 model:Many -->
**Domain:** SLI - definition
**Question:** What is a Service Level Indicator (SLI)?
**Options:** A. A carefully defined quantitative measure of some aspect of the level of service provided — e.g. request latency, error rate, throughput, or availability<br>B. A target value your team commits to for a service metric<br>C. A contract between vendor and customer with financial penalties<br>D. A Prometheus alerting rule that pages on-call
**Answer:** A (1) – Quantitative measure of service level: latency, error rate, throughput, availability, durability
**Explanation:** SLI = Service Level Indicator — the MEASUREMENT of service quality. Classic examples: request latency (often p99/p999 over a window), error rate (failed/total requests), throughput (req/s), availability (fraction of well-formed requests succeeding = 'yield'), durability for storage systems, correctness for all. Measurements are aggregated over a window into rates/averages/percentiles. B is the SLO (target), C is the SLA (contract), D is just an alert that may consume an SLI.
**Sources:** <a href="https://sre.google/sre-book/service-level-objectives/" target="_blank">Google SRE Book - Service Level Objectives</a>
**Tags:** k8s::kcna src::session topic::observability topic::monitoring

---

<!-- note:1794362066576 model:Many -->
**Domain:** SLI - selection
**Question:** What is the right way to choose SLIs for a service?
**Options:** A. Pick a handful that map to what users actually care about — user experience — even if that means using proxies; don't use every metric you can measure<br>B. Use every metric your monitoring system can collect so nothing is missed<br>C. Use only the easiest metrics to collect at the server<br>D. Use only infrastructure metrics like CPU and memory
**Answer:** A (1) – Pick a handful mapping to user experience; use proxies where needed; not every metric
**Explanation:** Google SRE: 'You shouldn't use every metric you can track in your monitoring system as an SLI' — too many SLIs dilute attention, too few leave blind spots. Start from what USERS care about and work backward to measurable proxies (e.g. client-side latency beats server-side because it captures slow JS page loads). Pure infrastructure metrics (CPU/memory) describe the machine, not the service level the user experiences.
**Sources:** <a href="https://sre.google/sre-book/service-level-objectives/" target="_blank">Google SRE Book - Service Level Objectives</a>
**Tags:** k8s::kcna src::session topic::observability topic::monitoring

---

<!-- note:1794362066577 model:Many -->
**Domain:** SLI - examples select-all
**Question:** Which of the following are common Service Level Indicators? (Select all that apply)
**Options:** A. Request latency (e.g. p99 response time)<br>B. Error rate (failed requests / total requests)<br>C. Availability (fraction of well-formed requests that succeed — 'yield')<br>D. Durability (likelihood stored data is retained — for storage systems)<br>E. Deployment frequency (how often releases ship)<br>F. Number of pods currently running
**Answer:** A, B, C, D – latency, error rate, availability/yield, durability are canonical SLIs
**Explanation:** Canonical SLIs (Google SRE): latency, error rate, throughput, availability (fraction of well-formed requests that succeed — 'yield'), durability (stored data retained — storage systems), correctness (right answer returned — all systems). E is a DORA delivery metric, not a service-level measure. F is infra state — though SATURATION (resource exhaustion) is a legitimate SLI via the USE method for capacity. Prefer percentiles over averages for latency: averages hide the long tail, and users prefer consistent-mediocre over fast-with-spikes.
**Sources:** <a href="https://sre.google/sre-book/service-level-objectives/" target="_blank">Google SRE Book - Service Level Objectives</a>
**Tags:** k8s::kcna src::session topic::observability topic::monitoring

---

<!-- note:1794362066578 model:Many -->
**Domain:** SLO - definition
**Question:** What is a Service Level Objective (SLO)?
**Options:** A. A target value or range for an SLI — e.g. '99% of requests complete in <500ms' — the level you intend to hit<br>B. The measured value of a service metric over a time window<br>C. A legally binding contract with financial penalties for missed targets<br>D. A dashboard showing current service health
**Answer:** A (1) – Target value/range for an SLI, e.g. '99% of requests <500ms'
**Explanation:** SLO = Service Level Objective — the TARGET for how well the service should perform, expressed against an SLI: 'SLI ≤ target' or 'lower ≤ SLI ≤ upper'. Example: '99% of Get RPCs < 100ms'; layered targets like '90% <1ms, 99% <10ms, 99.9% <100ms' shape the latency distribution. B is the SLI measurement itself, C is the SLA, D is visualization. You don't always pick the value (QPS is set by users) — but you choose the threshold you commit to defend.
**Sources:** <a href="https://sre.google/sre-book/service-level-objectives/" target="_blank">Google SRE Book - Service Level Objectives</a>
**Tags:** k8s::kcna src::session topic::observability topic::monitoring

---

<!-- note:1794362066579 model:Many -->
**Domain:** SLO vs SLA
**Question:** A cloud vendor advertises '99.9% monthly uptime' and issues service credits if it falls short. What is this?
**Options:** A. An SLA — it pairs the SLO-style target with explicit consequences (credits) for missing it<br>B. Just an SLO — uptime targets are always SLOs<br>C. An SLI — it measures the actual uptime achieved<br>D. An error budget — it defines allowed failures
**Answer:** A (1) – SLA: the uptime target PLUS explicit consequences (service credits)
**Explanation:** Litmus test from Google SRE: 'What happens if the SLOs aren't met?' Explicit consequence — credits, penalties, contract terms — means SLA. The 99.9% alone would be an SLO; the credits make it an agreement. Footnote worth memorizing: 'Most people really mean SLO when they say SLA' — an 'SLA violation' usually means a missed SLO; a real SLA violation can mean breach of contract. Mnemonic: SLIs measure, SLOs target, SLAs contract + consequences.
**Sources:** <a href="https://sre.google/sre-book/service-level-objectives/" target="_blank">Google SRE Book - Service Level Objectives</a>
**Tags:** k8s::kcna src::session topic::observability topic::monitoring

---

<!-- note:1794362066580 model:Many -->
**Domain:** SLA - definition
**Question:** Which statement about Service Level Agreements (SLAs) is correct?
**Options:** A. An SLA is a business contract — often legally binding — that includes consequences (rebates, penalties, other remedies) for meeting or missing its SLOs; it's usually a slightly relaxed version of internal SLOs<br>B. An SLA is a technical monitoring dashboard for service health<br>C. An SLA is the raw measurement of service quality over time<br>D. An SLA is a Kubernetes object you apply to enforce uptime
**Answer:** A (1) – Business contract with consequences for meeting/missing SLOs; usually a relaxed version of internal SLOs
**Explanation:** SLA = Service Level Agreement — the contractual layer between vendor and customer, including consequences (rebates, penalties, other remedies) for missing its SLOs. It's a BUSINESS/LEGAL artifact, not engineering: SRE helps define the SLIs needed to measure it and avoid triggering consequences, but doesn't negotiate contracts. Google Search has NO public SLA (reputation + ad revenue are the implicit consequences); Google for Work does. Internal SLOs are typically TIGHTER than advertised SLAs — that gap is your safety margin.
**Sources:** <a href="https://sre.google/sre-book/service-level-objectives/" target="_blank">Google SRE Book - Service Level Objectives</a>
**Tags:** k8s::kcna src::session topic::observability topic::monitoring topic::sre

---

<!-- note:1794362066581 model:Many -->
**Domain:** Error budget
**Question:** What is an error budget?
**Options:** A. The tolerance for failed events over a period — 100% minus the SLO over the window (e.g. a 99.9% monthly SLO = 0.1% ≈ 43 minutes of downtime budget)<br>B. The money set aside for incident response tooling<br>C. The extra replicas kept running for redundancy<br>D. The percentage of requests allowed to be slow
**Answer:** A (1) – 100% minus SLO over the window: 99.9% monthly = 0.1% ≈ 43 min downtime budget
**Explanation:** Error budget = tolerance for failed events over a period — 'an SLO for meeting other SLOs.' 99.9% over 30 days → 0.1% budget ≈ 43.2 minutes of full downtime (or equivalent partial failures). It converts reliability into a spendable resource: budget left → ship features and experiments; budget exhausted → freeze launches, fix reliability. This is what lets teams balance velocity vs stability rationally instead of 'never break anything' — and it's what drives SLO-based alerting.
**Sources:** <a href="https://github.com/cncf/tag-observability/blob/main/whitepaper.md" target="_blank">CNCF TAG Observability - Whitepaper</a>
**Tags:** k8s::kcna src::session topic::observability topic::monitoring topic::sre

---

<!-- note:1794362066582 model:Many -->
**Domain:** Burn rate
**Question:** What does error-budget 'burn rate' measure?
**Options:** A. How fast the service consumes its error budget relative to the SLO window — burn rate 1 means exactly 0 budget remains at window end<br>B. How quickly on-call engineers respond to pages<br>C. The rate at which cloud costs grow month over month<br>D. How fast a deployment pipeline runs
**Answer:** A (1) – How fast error budget is consumed; burn 1 = exactly 0 budget at window end
**Explanation:** Burn rate = error consumption speed relative to the SLO window. With a 99.9% SLO: sustained 0.1% errors = burn 1 (budget lasts the full 30 days); 1% errors = burn 10 → budget gone in ~3 days; 100% errors = burn 1000 → gone in ~43 minutes. Burn-rate alerting fires proportional to budget consumption — far more actionable than naive 'error rate > threshold' alerts that fire on blips which wouldn't actually breach the SLO.
**Sources:** <a href="https://github.com/cncf/tag-observability/blob/main/whitepaper.md" target="_blank">CNCF TAG Observability - Whitepaper</a>
**Tags:** k8s::kcna src::session topic::observability topic::monitoring topic::sre topic::prometheus

---

<!-- note:1794362066583 model:Many -->
**Domain:** Availability nines
**Question:** Availability is often expressed in 'nines' — which pairing is correct?
**Options:** A. 99.9% = three nines; 99.99% = four nines; 99.999% = five nines<br>B. 99% = three nines; 99.9% = four nines; 99.99% = five nines<br>C. 99.99% = two nines; 99.999% = three nines<br>D. Each additional nine adds a fixed 0.1% regardless of level
**Answer:** A (1) – 99.9% = 3 nines, 99.99% = 4 nines, 99.999% = 5 nines
**Explanation:** Count the nines after '99.': 99% = 2 nines, 99.9% = 3, 99.99% = 4, 99.999% = 5. Google Compute Engine's published target is 99.95% = 'three and a half nines.' The stakes escalate brutally: 99.9% allows ~8.7h/year downtime; 99.99% ~52min; 99.999% ~5min — each nine is ~10x stricter. This is why SLIs/SLOs matter: 'high availability' is meaningless without a number.
**Sources:** <a href="https://sre.google/sre-book/service-level-objectives/" target="_blank">Google SRE Book - Service Level Objectives</a>
**Tags:** k8s::kcna src::session topic::observability topic::monitoring topic::sre

---

<!-- note:1794362066584 model:Many -->
**Domain:** SLO - practices
**Question:** Which are recommended practices when setting SLOs? (Select all that apply)
**Options:** A. Keep the number of SLOs small — enough to cover key attributes, no more<br>B. Set an internal SLO tighter than the one advertised to users (safety margin)<br>C. Anchor the target to current measured performance so it's guaranteed achievable<br>D. Avoid absolute targets like 'always available' or 'infinitely scalable'<br>E. Start loose and tighten over time rather than set an unattainable strict target
**Answer:** A, B, D, E – few SLOs + safety margin + no absolutes + start loose
**Explanation:** From Google SRE 'Choosing Targets': few SLOs (defend each — if you can't win priority arguments quoting it, drop it); safety margin (internal SLO tighter than advertised absorbs chronic issues and reimplementation trade-offs); avoid absolutes ('always available', 'infinitely scalable' are unrealistic and stifle innovation); perfection can wait (loose→tight beats strict→relaxed). C is the anti-pattern — 'don't pick a target based on current performance': it locks you into heroics or forces redesign. Start from what users need, not what you can measure today.
**Sources:** <a href="https://sre.google/sre-book/service-level-objectives/" target="_blank">Google SRE Book - Service Level Objectives</a>
**Tags:** k8s::kcna src::session topic::observability topic::monitoring topic::sre

---

<!-- note:1794363142438 model:Many -->
**Domain:** Prometheus - multi datacenter
**Question:** You need metrics from servers across three datacenters visible on one dashboard. How does Prometheus support this?
**Options:** A. Run Prometheus (or agent mode) per site and federate/remote-write to a central store, then query it all from one Grafana<br>B. One Prometheus server scrapes every target across all WAN links<br>C. Prometheus automatically syncs metrics between datacenters<br>D. You can't — Prometheus is single-datacenter only
**Answer:** A (1) – Prometheus per site + federation/remote-write to central + one Grafana
**Explanation:** Prometheus's pull model keeps scraping LOCAL — you don't scrape across WAN from one server (latency, WAN dependency, single point of failure). Standard pattern: Prometheus per site/DC (or Prometheus Agent mode for scrape-only), metrics leave via federation or remote-write to a central store (Thanos/Cortex/Mimir for long-term retention), and Grafana queries the central store for the single pane of glass. B works in a tiny setup but is an anti-pattern at scale.
**Sources:** <a href="https://prometheus.io/docs/prometheus/latest/federation/" target="_blank">Prometheus Docs - Federation</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::monitoring

---

<!-- note:1794363142439 model:Many -->
**Domain:** Prometheus - alert pipeline
**Question:** Memory usage crosses 80% and an alerting rule fires in Prometheus. What actually delivers the Slack message?
**Options:** A. Alertmanager — Prometheus sends firing alerts to it, which routes them to receivers like Slack/email<br>B. Prometheus sends the Slack webhook directly<br>C. Grafana polls Prometheus and posts to Slack<br>D. The kubelet notifies the ops channel
**Answer:** A (1) – Alertmanager routes firing alerts to receivers like Slack/email
**Explanation:** Two-stage design: Prometheus evaluates alerting rules (PromQL expr + for-duration) and sends alert state to Alertmanager; Alertmanager handles grouping, deduplication, silences, inhibition, rate-limiting and dispatches notifications to receivers — email, Slack, PagerDuty, webhook, OpsGenie, on-call systems. Prometheus deliberately doesn't do notification routing: the docs say rules are 'good at figuring what is broken right now, but they are not a fully-fledged notification solution.'
**Sources:** <a href="https://prometheus.io/docs/alerting/latest/overview/" target="_blank">Prometheus Docs - Alerting overview</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::alerting

---

<!-- note:1794363142440 model:Many -->
**Domain:** Prometheus - alertmanager
**Question:** Which are Alertmanager responsibilities? (Select all that apply)
**Options:** A. Grouping related alerts into one notification<br>B. Deduplication and inhibition (suppress alerts caused by a bigger outage)<br>C. Silences — mute alerts during maintenance windows<br>D. Routing alerts to receivers (email, Slack, PagerDuty) with rate limiting<br>E. Scraping /metrics endpoints from targets
**Answer:** A, B, C, D – grouping, dedup/inhibition, silences, routing+rate-limiting
**Explanation:** Alertmanager = the notification brain: it GROUPS alerts (one page for a cluster outage, not 500), DEDUPLICATES across Prometheus replicas, supports SILENCES (scheduled muting for maintenance) and INHIBITION (if 'DC down' fires, suppress 'all pods down' alerts it causes), routes by labels to different receivers, and RATE-LIMITS notifications. E is Prometheus's job — Alertmanager never scrapes metrics.
**Sources:** <a href="https://prometheus.io/docs/alerting/latest/overview/" target="_blank">Prometheus Docs - Alerting overview</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::alerting

---

<!-- note:1794363142441 model:Many -->
**Domain:** Prometheus - alert for clause
**Question:** What does `for: 10m` do in an alerting rule?
**Options:** A. Keeps the alert in 'pending' until the condition holds for 10 minutes — prevents flapping on momentary spikes<br>B. Sends the notification every 10 minutes while active<br>C. Keeps the alert firing for 10 minutes after the condition clears<br>D. Scrapes the target every 10 minutes
**Answer:** A (1) – Pending until condition holds 10m across evaluations — anti-flap
**Explanation:** `for` = pending period: the expr must evaluate true at EVERY evaluation for the duration before the alert counts as firing — a one-sample spike never notifies anyone. (C describes `keep_firing_for`, the companion clause that keeps an alert firing briefly AFTER the condition clears — also anti-flap.) Pending alerts show on the Alerts tab; firing alerts become ALERTS{alertstate="firing"} synthetic series. A rule with no `for` fires on first evaluation.
**Sources:** <a href="https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/" target="_blank">Prometheus Docs - Alerting rules</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::alerting

---

<!-- note:1794363142442 model:Many -->
**Domain:** Prometheus - memory alert expr
**Question:** Which expression correctly alerts when a host's memory usage exceeds 80%?
**Options:** A. (node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100 > 80<br>B. node_memory_MemTotal_bytes > 80<br>C. node_memory_MemAvailable_bytes < 80<br>D. rate(node_memory_MemTotal_bytes[5m]) > 80
**Answer:** A (1) – (MemTotal - MemAvailable)/MemTotal*100 > 80 — a ratio of two gauges
**Explanation:** Memory % = (total − available)/total × 100 — you compute a RATIO of two gauges, then compare to 80. B compares total bytes to 80 (nonsense units). C compares available bytes to 80 bytes (always true). D misuses rate() — that's for counters, and gives bytes/sec change not a percentage. Node Exporter exposes node_memory_MemTotal_bytes / node_memory_MemAvailable_bytes; for containers you'd use the analogous cAdvisor/kubelet metrics.
**Sources:** <a href="https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/" target="_blank">Prometheus Docs - Alerting rules</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::alerting topic::promql

---

<!-- note:1794363142443 model:Many -->
**Domain:** Prometheus - alert receivers
**Question:** Email, Slack, and PagerDuty notifications from Alertmanager are configured as what?
**Options:** A. Receivers — notification integrations Alertmanager routes matched alerts to<br>B. Scrape configs — they tell Prometheus what to collect<br>C. Recording rules — they pre-compute metrics<br>D. ServiceMonitors — they define Kubernetes scrape targets
**Answer:** A (1) – Receivers: notification integrations Alertmanager routes matched alerts to
**Explanation:** In alertmanager.yml you define `receivers` (email_configs, slack_configs, pagerduty_configs, webhook_configs, opsgenie_configs, victorops, telegram...) and `routes` that match alert labels — e.g. severity=page → pager receiver, severity=ticket → email — with grouping/dedup/rate-limit settings. This is how 'page on-call for critical, email a ticket for warnings' works: routing happens on the LABELS the alert rule attached, which is why rules set labels like severity: page.
**Sources:** <a href="https://prometheus.io/docs/alerting/latest/configuration/" target="_blank">Alertmanager Docs - Configuration</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::alerting

---

<!-- note:1794363142444 model:Many -->
**Domain:** Prometheus - visualization
**Question:** The ops team wants Grafana dashboards plotting CPU vs memory vs request rate on one chart. How does that work?
**Options:** A. Grafana queries Prometheus via PromQL/HTTP API — panels run expressions (including arithmetic across metrics) and render time series<br>B. Grafana scrapes the metrics itself directly from the apps<br>C. Prometheus exports PNG charts that Grafana embeds<br>D. Each metric needs its own separate Grafana instance
**Answer:** A (1) – Grafana queries Prometheus via PromQL/HTTP API; panels render the results
**Explanation:** Grafana is the visualization layer ON TOP of Prometheus: panels issue PromQL queries (instant or range) to Prometheus's HTTP API and render the time series — one dashboard can combine many metrics across many panels, and a single expression can do arithmetic across vectors. Grafana never scrapes — Prometheus owns collection, Grafana owns rendering. It can also hold MULTIPLE Prometheus datasources, which is exactly how the multi-datacenter 'single page' works.
**Sources:** <a href="https://prometheus.io/docs/visualization/grafana/" target="_blank">Prometheus Docs - Grafana</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::grafana

---

<!-- note:1794363142445 model:Many -->
**Domain:** Prometheus - use cases
**Question:** Which are core Prometheus use cases? (Select all that apply)
**Options:** A. Collecting and centrally storing metrics from many targets<br>B. Alerting when metric conditions are met (e.g. memory > 80%)<br>C. Visualizing and cross-referencing metrics in dashboards<br>D. Storing and analyzing application logs<br>E. Distributed request tracing across microservices
**Answer:** A, B, C – collect metrics + alert on conditions + visualize/cross-reference
**Explanation:** Prometheus = metrics platform: pull-scrape collection from many targets (A), PromQL + alerting rules + Alertmanager for condition alerts like memory >80% (B), Grafana visualization on top for charting and cross-referencing (C). D is Loki/ELK/Fluent Bit territory; E is Jaeger/Tempo/OpenTelemetry — Prometheus handles METRICS ONLY (the tool-mapping card). 'Prometheus for everything' is wrong by design: it deliberately doesn't do logs or traces.
**Sources:** <a href="https://prometheus.io/docs/introduction/overview/" target="_blank">Prometheus Docs - Overview</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus

---

<!-- note:1794363156751 model:Cloze -->
**Text:** Alerting rule YAML anatomy:<br><br>- alert: {{c1::HighMemoryUsage}} — the rule's name<br>  expr: (node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100 {{c2::> 80}} — PromQL firing condition<br>  for: {{c3::10m}} — pending period before it counts as firing<br>  keep_firing_for: {{c4::5m}} — stay firing after the condition clears<br>  labels:<br>    severity: {{c5::page}} — Alertmanager routes on this<br>  annotations:<br>    summary: "High memory usage" — templated with $labels / $value
**Back Extra:** Field roles: alert = rule name; expr = PromQL evaluated every scrape interval — when it returns elements, the alert becomes active for those label sets; for = pending period (must hold at EVERY evaluation — anti-flap); keep_firing_for = stays firing briefly after the condition clears (prevents flapping/false-resolves); labels = attached to the alert and used by Alertmanager ROUTES (severity: page → pager, severity: ticket → email); annotations = long human text (summary, runbook links) templated with $labels / $value / $externalLabels. States: pending → firing; ALERTS{alertname, alertstate} synthetic series tracks them.
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::alerting

---

<!-- note:1794363700613 model:Many -->
**Domain:** Prometheus - local storage
**Question:** Where does Prometheus store scraped metrics, and how long by default?
**Options:** A. Local on-disk TSDB — default retention 15 days; optional size cap; not replicated, so long-term history needs remote-write/Thanos<br>B. Cloud object storage by default — retention is unlimited<br>C. In-memory only — data is lost on restart<br>D. It forwards everything to Grafana for storage
**Answer:** A (1) – Local on-disk TSDB, default 15d retention; not replicated → remote-write for long-term
**Explanation:** Prometheus embeds a local time-series database (TSDB) on disk — data in 2-hour blocks plus a WAL for the in-memory head. --storage.tsdb.retention.time defaults to 15d; retention.size can cap bytes; whichever triggers first wins. It's a SINGLE-NODE store — not clustered or replicated — fine for recent monitoring/alerting data, but years of history or durability need remote-write to Thanos/Cortex/Mimir. Samples cost ~1-2 bytes so capacity planning is easy. NFS is explicitly unsupported for the data dir.
**Sources:** <a href="https://prometheus.io/docs/prometheus/latest/storage/" target="_blank">Prometheus Docs - Storage</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus

---

<!-- note:1794363700614 model:Many -->
**Domain:** Prometheus - numeric only
**Question:** Why is Prometheus designed around numeric time-series data specifically?
**Options:** A. Numbers aggregate and compute cheaply — rate/avg/percentiles over dimensions (labels) — while logs/traces are high-volume events that need different storage and query models<br>B. Because Prometheus can't parse text<br>C. Because numeric data is more secure<br>D. Because Kubernetes only produces numeric metrics
**Answer:** A (1) – Numbers aggregate/compute cheaply via labels; logs/traces are events needing different stores
**Explanation:** Deliberate design, not a limitation: numeric samples compress to ~1-2 bytes, labels give cheap dimensions, and PromQL math (rate, histogram_quantile, aggregations) only works because values are numbers. Logs are unstructured text events and traces are request trees — neither fits a timeseries store; that's why Loki/ELK handle logs and Jaeger/Tempo handle traces while Prometheus owns metrics. 'Monitors numeric time series' IS the data model.
**Sources:** <a href="https://prometheus.io/docs/introduction/overview/" target="_blank">Prometheus Docs - Overview</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus

---

<!-- note:1794363704624 model:Cloze -->
**Text:** scrape_configs anatomy:<br><br>- job_name: {{c1::node-exporter}} — logical job grouping targets<br>  metrics_path: {{c2::/metrics}} — HTTP endpoint Prometheus scrapes<br>  scrape_interval: {{c3::1m}} — default: every minute (timeout defaults to 10s)<br>  static_configs:<br>  - targets: [{{c4::node1:9100}}, {{c5::node2:9100}}] — host:port of exporters
**Back Extra:** Field roles: job_name = logical grouping of targets sharing one scrape config; metrics_path = the HTTP endpoint Prometheus GETs (default /metrics); scrape_interval = how often to scrape (default 1m; scrape_timeout defaults to 10s and must be ≤ interval); static_configs.targets = manually listed host:port endpoints — each scraped target becomes an 'instance' label, and job/instance labels are auto-attached to every sample. Alternatives to static_configs: file_sd, http_sd, and kubernetes_sd for dynamic discovery (pods/endpoints change constantly in K8s). Node Exporter conventionally listens on :9100.
**Tags:** k8s::kcna src::session topic::observability topic::prometheus

---

<!-- note:1794367042610 model:Many -->
**Domain:** Prometheus - architecture
**Question:** Which are the three core parts of a Prometheus server's data path? (Select all that apply)
**Options:** A. Retrieval worker that scrapes targets via HTTP<br>B. TSDB that stores the collected samples<br>C. HTTP server that answers PromQL queries<br>D. Alertmanager that sends Slack notifications<br>E. Grafana dashboard server
**Answer:** A, B, C – scraper + TSDB + PromQL query API are the data path
**Explanation:** The Prometheus SERVER's data path has three parts: RETRIEVAL WORKER — HTTP-scrapes each target's /metrics endpoint on the configured interval; TSDB — stores the samples in the local time-series database; HTTP QUERY SERVER — accepts PromQL queries and returns stored data (used by the expression browser, Grafana, API clients). Alertmanager is a SEPARATE component for notifications; Grafana is an external visualization layer; rules are evaluated inside the server but aren't part of the collect→store→query path.
**Sources:** <a href="https://prometheus.io/docs/introduction/overview/" target="_blank">Prometheus Docs - Overview</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus

---

<!-- note:1794367042611 model:Many -->
**Domain:** Prometheus - service discovery
**Question:** Why does Prometheus need service discovery in Kubernetes?
**Options:** A. Pod IPs churn constantly — SD watches the cluster and keeps the scrape target list automatically up to date<br>B. Prometheus can't reach Kubernetes APIs so SD translates them<br>C. SD is required for PromQL queries to work<br>D. SD replaces the need for exporters
**Answer:** A (1) – Pull model must know every target; K8s pod IPs churn → SD auto-updates
**Explanation:** Pull-based scraping means Prometheus must KNOW every target's address before scraping — but in Kubernetes pod IPs appear/disappear constantly, so a hand-maintained list is instantly stale. Service Discovery mechanisms (kubernetes_sd_configs, file_sd, http_sd, dns_sd, cloud SDs) watch the environment and keep the target list current automatically — pods get scraped as they come up, removed when they die. static_configs is the manual alternative for stable bare-metal targets.
**Sources:** <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#kubernetes_sd_config" target="_blank">Prometheus Docs - kubernetes_sd_config</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::kubernetes

---

<!-- note:1794367042612 model:Many -->
**Domain:** Prometheus - SD mechanisms
**Question:** Which are real Prometheus service discovery mechanisms? (Select all that apply)
**Options:** A. kubernetes_sd_configs — discovers pods/services/endpoints via the K8s API<br>B. file_sd_configs — reads targets from a watched file<br>C. http_sd_configs — fetches targets from an HTTP endpoint<br>D. dns_sd_configs — discovers targets via DNS records<br>E. push_sd_configs — targets push themselves into Prometheus<br>F. static_sd_configs — the default discovery mechanism
**Answer:** A, B, C, D – kubernetes_sd, file_sd, http_sd, dns_sd are real mechanisms
**Explanation:** Real SD mechanisms: kubernetes_sd (watches pods/services/endpoints via the K8s API), file_sd (reads target list from a file that can be rewritten), http_sd (fetches target list from an HTTP endpoint), dns_sd (resolves DNS names), plus cloud SDs (ec2, gce, azure, consul...). 'static_sd' isn't a mechanism — static_configs is the non-SD way to list targets manually. 'push_sd' doesn't exist — SD is inherently about Prometheus pulling its target list.
**Sources:** <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/" target="_blank">Prometheus Docs - Configuration</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus

---

<!-- note:1794367042613 model:Many -->
**Domain:** Prometheus - pushgateway
**Question:** How does the Pushgateway let Prometheus monitor short-lived batch jobs?
**Options:** A. The job pushes metrics to Pushgateway before exiting; Prometheus scrapes Pushgateway's /metrics like a normal target<br>B. Pushgateway stores metrics permanently so jobs never need re-pushing<br>C. Prometheus pushes scrape requests to the Pushgateway<br>D. Pushgateway replaces Alertmanager for batch job alerts
**Answer:** A (1) – Job pushes to Pushgateway; Prometheus scrapes the gateway like a normal target
**Explanation:** The Pushgateway bridges push→pull: short-lived batch jobs (cron, ETL) POST their metrics to the Pushgateway before exiting; the Pushgateway exposes them on its own /metrics endpoint; Prometheus scrapes the Pushgateway like any other target. GOTCHA: it's a dumb cache — metrics persist until overwritten or deleted via its API, so finished jobs leave STALE series behind (a known source of ghost metrics). Push fits event-driven/short-lived workloads Prometheus's pull model can't reach.
**Sources:** <a href="https://prometheus.io/docs/practices/pushing/" target="_blank">Prometheus Docs - When to use the Pushgateway</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus

---

<!-- note:1794367042614 model:Many -->
**Domain:** Prometheus - exporter vs client lib
**Question:** What is the difference between a Prometheus exporter and a client library?
**Options:** A. Exporters push metrics; client libraries are pulled<br>B. An exporter is a separate process re-exposing a target's metrics; a client library is linked into your app which exposes /metrics itself<br>C. Client libraries only work for Go; exporters work for all languages<br>D. Exporters are for logs; client libraries are for metrics
**Answer:** B (2) – Exporter = separate process re-exposing target metrics; client lib = in-app /metrics
**Explanation:** Both end at the same place — a /metrics endpoint Prometheus scrapes — but differ in WHERE the exposition lives. EXPORTER: standalone process alongside the target that collects its native metrics and re-exposes them in Prometheus format — node_exporter (Linux host), windows_exporter, mysqld_exporter, apache_exporter, haproxy_exporter, postgres_exporter, blackbox_exporter. CLIENT LIBRARY: language library (Go, Java, Python, Rust...) linked into YOUR application — the app exposes /metrics itself, no extra process. Use exporters for third-party software you can't instrument; client libs for your own services.
**Sources:** <a href="https://prometheus.io/docs/instrumenting/clientlibs/" target="_blank">Prometheus Docs - Client libraries</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus

---

<!-- note:1794373029142 model:Many -->
**Domain:** Prometheus config - file
**Question:** How does Prometheus configuration work? (Select all that apply)
**Options:** A. prometheus.yaml defines scrape jobs and rule files; command-line flags set immutable system params like storage/retention<br>B. Config reloads at runtime via SIGHUP or POST /-/reload (with --web.enable-lifecycle) — a bad config is simply not applied<br>C. The file is YAML and supports duration values like 1d, 1h30m, 5m, 10s<br>D. prometheus.yaml contains the Alertmanager receiver configuration<br>E. The config file can only be changed by restarting Prometheus
**Answer:** A, B, C – file defines scraping/rules; flags define system params; reload via SIGHUP or /-/reload
**Explanation:** Split of concerns: prometheus.yaml (via --config.file) defines WHAT to do — scrape_configs, rule_files, alerting, remote_write — everything 'declarative'. Command-line flags configure IMMUTABLE system parameters — storage paths, retention, listen address. Reload at runtime WITHOUT restart: send SIGHUP or POST /-/reload (requires --web.enable-lifecycle). Malformed config → changes NOT applied (old config keeps running). Durations use regex like 1d, 1h30m, 5m, 10s.
**Sources:** <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/" target="_blank">Prometheus Docs - Configuration</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::yaml

---

<!-- note:1794373029143 model:Many -->
**Domain:** Prometheus config - global
**Question:** What does the `global:` section of prometheus.yaml do?
**Options:** A. It configures the Alertmanager receivers<br>B. It sets defaults inherited by all scrape configs: scrape_interval (1m), scrape_timeout (10s), evaluation_interval (1m), external_labels<br>C. It defines the list of targets to scrape<br>D. It stores the scraped metrics
**Answer:** B (2) – scrape_interval 1m, scrape_timeout 10s, evaluation_interval 1m, external_labels
**Explanation:** The global: section sets defaults INHERITED by every other section — each scrape_config can override them. Core fields: scrape_interval (default 1m — how often to scrape), scrape_timeout (default 10s — per-scrape HTTP deadline, can't exceed interval), evaluation_interval (default 1m — how often rules/alerts evaluate), external_labels (labels attached when talking to EXTERNAL systems — federation, remote storage, Alertmanager — so you can tell which Prometheus a series came from). Also query_log_file, scrape_failure_log_file, runtime.log_level/gogc.
**Sources:** <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#global_config" target="_blank">Prometheus Docs - global_config</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::yaml

---

<!-- note:1794373029144 model:Many -->
**Domain:** Prometheus config - top-level
**Question:** Which are valid top-level sections of prometheus.yaml? (Select all that apply)
**Options:** A. rule_files — globs pointing at recording/alerting rule files<br>B. scrape_configs — the list of jobs and their targets<br>C. alerting — Alertmanager discovery and alert relabeling<br>D. dashboards — Grafana panel definitions<br>E. remote_write — shipping samples to external storage<br>F. receivers — Slack/email notification configs
**Answer:** A, B, C, E – rule_files, scrape_configs, alerting, remote_write are top-level; dashboards aren't
**Explanation:** Top-level keys of prometheus.yaml: global (defaults), rule_files (globs for recording/alerting rules), scrape_config_files (globs for extra scrape configs), scrape_configs (the jobs), alerting (alertmanager discovery + alert relabeling), remote_write / remote_read (external TSDB), storage (tsdb/exemplars runtime settings), otlp (OTLP receiver), tracing, runtime (log_level, gogc). Grafana dashboards and Alertmanager receivers are NOT configured here — they live in Grafana and alertmanager.yml respectively.
**Sources:** <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/" target="_blank">Prometheus Docs - Configuration</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::yaml

---

<!-- note:1794373029145 model:Many -->
**Domain:** Prometheus config - intervals
**Question:** What is the relationship between scrape_interval and scrape_timeout?
**Options:** A. Per-scrape HTTP deadline — it cannot exceed scrape_interval; a scrape exceeding it fails and up goes to 0<br>B. How long Prometheus waits before retrying a failed scrape<br>C. The total time a target is allowed to be down<br>D. How often alerting rules are evaluated
**Answer:** A (1) – Per-scrape HTTP deadline; must be ≤ scrape_interval; exceeding it fails the scrape
**Explanation:** scrape_interval = how often Prometheus GETs the target's metrics_path (default inherits global 1m). scrape_timeout = deadline for ONE scrape HTTP request (default inherits global 10s) — it CANNOT exceed the interval or the config is invalid. If a scrape exceeds the timeout it FAILS: the target's up metric goes to 0 and samples go stale — this is your primary 'target is down/slow' signal. Both can be overridden per scrape_config for jobs needing different cadence (e.g. fast app metrics at 15s, slow infra at 5m).
**Sources:** <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config" target="_blank">Prometheus Docs - scrape_config</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::yaml

---

<!-- note:1794373029146 model:Many -->
**Domain:** Prometheus config - honor_labels
**Question:** What does honor_labels control in a scrape config?
**Options:** A. It controls whether Prometheus honors the target's own timestamps<br>B. It decides who wins label conflicts: false renames scraped labels to exported_*; true keeps scraped labels (for federation/Pushgateway)<br>C. It enables HTTPS scraping<br>D. It limits how many labels a metric may have
**Answer:** B (2) – false: scraped label renamed to exported_*; true: scraped labels win (federation/Pushgateway)
**Explanation:** Label conflict resolution: scraped metrics may carry their own job/instance/etc labels, and Prometheus also attaches server-side ones (job from job_name, instance from address, SD labels). honor_labels: false (DEFAULT) → conflicting scraped labels get renamed to exported_<name> (exported_job, exported_instance) and server labels win. honor_labels: true → scraped label values WIN and server-side conflicts are dropped — needed for federation and scraping Pushgateway where the pushed labels must be preserved. external_labels are unaffected either way.
**Sources:** <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config" target="_blank">Prometheus Docs - scrape_config</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::yaml

---

<!-- note:1794373029147 model:Many -->
**Domain:** Prometheus config - honor_timestamps
**Question:** What does honor_timestamps do?
**Options:** A. Whether Prometheus uses the timestamps exposed by the target (true, default) or stamps samples with scrape time (false)<br>B. Whether Prometheus honors labels already present in scraped data<br>C. Whether scrape timeouts apply to this job<br>D. Whether metrics are stored long-term
**Answer:** A (1) – true (default): use target's timestamps; false: ignore them, use scrape time
**Explanation:** honor_timestamps (default TRUE) = Prometheus respects the timestamps the target put on each sample — useful when the exporter batches/pre-aggregates data with meaningful times. Set false to IGNORE target timestamps and stamp samples with scrape time — the fix for targets with wrong/clocks-skewed timestamps that would corrupt your graphs. Distinct from honor_labels (which is about label conflicts, not timestamps). track_timestamps_staleness is the related companion flag for staleness markers on timestamped metrics.
**Sources:** <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config" target="_blank">Prometheus Docs - scrape_config</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::yaml

---

<!-- note:1794373029148 model:Many -->
**Domain:** Prometheus config - relabeling
**Question:** What is the difference between relabel_configs and metric_relabel_configs?
**Options:** A. relabel_configs edits samples; metric_relabel_configs edits targets — they're interchangeable<br>B. relabel_configs rewrites target labels BEFORE scraping (filter/rewrite targets); metric_relabel_configs rewrites sample labels AFTER scraping (drop series, cut cardinality)<br>C. relabel_configs is for alerting; metric_relabel_configs is for recording rules<br>D. They are deprecated — use params instead
**Answer:** B (2) – relabel_configs rewrites TARGET labels before scraping; metric_relabel_configs rewrites SAMPLES after scraping
**Explanation:** Two relabel stages, same syntax (source_labels + regex + action keep/drop/replace/labeldrop...): relabel_configs runs on TARGET labels BEFORE scraping — filter which discovered targets get scraped (keep pods with label app=myapp), rewrite __address__/__metrics_path__, add/drop labels. metric_relabel_configs runs on scraped SAMPLES after ingestion into the pipeline — drop unwanted series, reduce cardinality (the classic use: drop expensive per-request labels before they hit TSDB). __meta_* and __address__ labels exist only during target relabeling; __-prefixed labels are stripped afterward.
**Sources:** <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config" target="_blank">Prometheus Docs - relabel_config</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::yaml topic::labels

---

<!-- note:1794373029149 model:Many -->
**Domain:** Prometheus config - http scheme
**Question:** How do you configure Prometheus to scrape an HTTPS endpoint that requires basic auth?
**Options:** A. scheme: tls and tls_config: enabled<br>B. scheme: https plus an http_config block with basic_auth/authorization/tls_config as needed<br>C. Authentication is configured globally only — per-job auth isn't possible<br>D. You must put credentials in external_labels
**Answer:** B (2) – scheme: https + http_config with basic_auth/authorization/TLS settings
**Explanation:** To scrape an HTTPS endpoint: scheme: https in the scrape config (default http). For authentication/TLS/proxy/custom headers, the scrape config takes an http_config block: basic_auth (username/password), authorization (Bearer token), tls_config (ca_file/cert_file/insecure_skip_verify), proxy_url, custom headers via headers:. params: adds URL query parameters to every scrape request. enable_compression: false asks the target for uncompressed responses.
**Sources:** <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config" target="_blank">Prometheus Docs - scrape_config</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::yaml

---

<!-- note:1794373034025 model:Cloze -->
**Text:** Advanced scrape_config — kubernetes job with relabeling:<br><br>- job_name: {{c1::kubernetes-pods}}<br>  kubernetes_sd_configs:<br>  - role: {{c2::pod}}<br>  scheme: {{c3::https}}<br>  params:<br>    module: [{{c4::http_2xx}}]<br>  honor_labels: {{c5::true}}<br>  scrape_interval: {{c6::30s}}<br>  scrape_timeout: {{c7::10s}}<br>  relabel_configs:<br>  - source_labels: [__meta_kubernetes_pod_label_app]<br>    regex: myapp<br>    action: {{c8::keep}}<br>  metric_relabel_configs:<br>  - regex: {{c9::expensive_metric.*}}<br>    action: {{c10::drop}}
**Back Extra:** Advanced scrape_config fields: kubernetes_sd_configs discovers pods/endpoints via the K8s API (role: pod|service|endpoints|node|ingress); scheme selects http/https; params adds URL query args to every scrape; honor_labels resolves label conflicts (scraped wins vs exported_* rename); honor_timestamps controls whether target timestamps are trusted; scrape_timeout ≤ scrape_interval else invalid config; relabel_configs filters/rewrites TARGETS pre-scrape using __meta_* labels and actions keep/drop/replace; metric_relabel_configs drops/rewrites SAMPLES post-scrape — the cardinality-control lever. __-prefixed labels are stripped after target relabeling.
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::yaml

---

<!-- note:1794378540938 model:Many -->
**Domain:** Prometheus metric types
**Question:** Which are the four Prometheus metric types? (Select all that apply)
**Options:** A. Counter<br>B. Gauge<br>C. Histogram<br>D. Summary<br>E. Percentile<br>F. Rate
**Answer:** A, B, C, D – Counter, Gauge, Histogram, Summary are the four types
**Explanation:** The four Prometheus metric types: COUNTER — monotonically increasing value (requests_total; resets on restart). GAUGE — value that goes up AND down (temperature, memory, queue depth). HISTOGRAM — counts observations into configurable buckets (_bucket/_sum/_count series; for quantiles server-side). SUMMARY — like a histogram but computes quantiles CLIENT-side at fixed φ values baked into the metric. 'Percentile' and 'Rate' are not types — they're computed stats/functions (histogram_quantile(), rate() in PromQL).
**Sources:** <a href="https://prometheus.io/docs/concepts/metric_types/" target="_blank">Prometheus Docs - Metric types</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::metrics

---

<!-- note:1794378540939 model:Many -->
**Domain:** Prometheus metric - counter
**Question:** What defines a Prometheus Counter?
**Options:** A. Monotonically increasing count ending in _total — query it with rate()/increase() since it resets on restart<br>B. A value that goes up and down like temperature or memory usage<br>C. A distribution of observations split into buckets for quantiles<br>D. A client-side pre-computed set of quantiles
**Answer:** A (1) – Monotonically increasing count; _total suffix; resets on restart so use rate()/increase()
**Explanation:** A Counter is a monotonically increasing cumulative value — it only goes UP (or resets to 0 on process restart). Convention: counter names end in _total (http_requests_total). Because the raw value is meaningless alone (is 15234 a lot?), you query counters with rate()/increase() to get per-second change — these functions handle the restart-reset automatically. Use counters for things you COUNT: requests, errors, bytes sent. Never use a counter for something that can decrease (memory usage = gauge).
**Sources:** <a href="https://prometheus.io/docs/concepts/metric_types/#counter" target="_blank">Prometheus Docs - Counter</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::metrics

---

<!-- note:1794378540940 model:Many -->
**Domain:** Prometheus metric - histogram vs summary
**Question:** How do Histogram and Summary differ? (Select all that apply)
**Options:** A. Histogram buckets observations server-side into _bucket/_sum/_count — quantiles computed later with histogram_quantile() at any value<br>B. Summary buckets observations server-side and is strictly better than histogram<br>C. Summary computes quantiles client-side at fixed φ values baked into the metric — no re-quantiling, no cross-instance aggregation<br>D. Histogram and Summary are interchangeable — they produce identical series
**Answer:** A, C – Histogram buckets server-side (_bucket/le, any quantile later, aggregatable); Summary computes fixed quantiles client-side
**Explanation:** HISTOGRAM: counts each observation into configurable buckets exposed as _bucket series with le (less-than-or-equal) labels, plus _sum and _count. Quantiles computed SERVER-side via histogram_quantile() — you can pick ANY quantile later AND aggregate histograms across pods. SUMMARY: the CLIENT library computes quantiles at FIXED φ values (e.g. φ=0.5, 0.9, 0.99) at scrape time and exposes them as separate series — cheaper, but you can't change the quantiles or aggregate summaries across instances. Rule of thumb: histogram for flexibility, summary when you only need fixed quantiles and minimal storage.
**Sources:** <a href="https://prometheus.io/docs/practices/histograms/" target="_blank">Prometheus Docs - Histograms and summaries</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::metrics

---

<!-- note:1794378540941 model:Many -->
**Domain:** Prometheus metric - labels
**Question:** What are labels in Prometheus metrics and why use them? (Select all that apply)
**Options:** A. Key-value pairs that add dimensions to a metric — slice, filter, and aggregate one metric name many ways<br>B. They prevent metric-name explosion: one name with labels beats a separate metric per combination<br>C. Every unique label combination creates a new timeseries — high-cardinality labels are dangerous<br>D. Labels are mandatory and fixed — every metric must have the same label set<br>E. Labels store the metric's numeric value
**Answer:** A, B, C – key=value dims attached to a metric; let you slice/filter/aggregate one metric many ways without new names; bad labels = cardinality explosion
**Explanation:** Labels are key-value pairs attached to every sample of a metric — they add DIMENSIONS so one metric name can be sliced many ways: http_requests_total{method='GET', status='200', pod='api-1'} vs {method='POST', status='500'}. Why use them: filter in PromQL (http_requests_total{status='500'}), aggregate by label (sum by (pod)), and avoid metric-name explosion (one name + N labels beats N names). The cost: EVERY unique label combination is a new timeseries — high-cardinality labels (user_id, request_id, PID) cause storage/cost blowups; that's the cardinality problem.
**Sources:** <a href="https://prometheus.io/docs/concepts/data_model/" target="_blank">Prometheus Docs - Data model</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::labels topic::metrics

---

<!-- note:1794378540942 model:Many -->
**Domain:** Prometheus metric - default labels
**Question:** Which labels does Prometheus attach automatically to scraped metrics?
**Options:** A. Only job — instance is optional and rarely used<br>B. job (the scrape job_name) and instance (the target address) are auto-attached to every sample; __name__ holds the metric name internally; __-prefixed labels are internal and stripped<br>C. hostname, datacenter, and environment are always attached automatically<br>D. No labels are automatic — you must add job and instance via relabel_configs
**Answer:** B (2) – Every sample auto-gets job (from job_name) and instance (target address); __name__ stores the metric name; __-prefixed labels are internal and stripped
**Explanation:** Prometheus automatically attaches TWO labels to every scraped sample: job (the scrape config's job_name — which job scraped it) and instance (the target's address — which instance it came from). These let you distinguish identical metrics from different jobs/hosts. Internally the metric NAME is itself stored as a label called __name__ (so http_requests_total{...} is really __name__='http_requests_total'). Labels prefixed with __ are INTERNAL — __address__, __scheme__, __meta_* during discovery/relabeling — and are stripped before storage. That's also why relabel_configs can see them but queries never do.
**Sources:** <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config" target="_blank">Prometheus Docs - scrape_config</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::labels topic::metrics

---

<!-- note:1794379388268 model:Many -->
**Domain:** Logs - purpose and nature
**Question:** Which statement accurately describes the purpose of logs in a system or application?
**Options:** A. Logs provide insights into system performance and resource utilization<br>B. Logs are historical records that capture information about specific events<br>C. Logs are used for real-time event monitoring<br>D. Logs are primarily used for error tracking and debugging
**Answer:** B (2) – Logs are historical records of discrete events — timestamp + message + context
**Explanation:** A log is a HISTORICAL RECORD: an append-only stream of timestamped entries capturing discrete events as they happened — request received, error thrown, pod scheduled. You read logs AFTER the fact to reconstruct what occurred. The distractors describe use cases or other signals: A (performance/resource) is METRICS territory — numbers over time; C (real-time monitoring) is closer to alerting/metrics — log pipelines are near-real-time at best; D (error tracking) is a major USE of logs but not their purpose — logs record ALL events, not just errors. CNCF framing: logs answer 'what happened, when, in which component?' — the forensic record.
**Sources:** <a href="https://github.com/cncf/tag-observability/blob/main/whitepaper.md" target="_blank">CNCF Observability Whitepaper</a>
**Tags:** k8s::kcna src::session topic::observability topic::logs

---

<!-- note:1794379430249 model:Many -->
**Domain:** Metrics - data point fields
**Question:** What are the four pieces of information typically included in metrics?
**Options:** A. Metric ID, unit, interval, and scope<br>B. Metric category, severity, frequency, and description<br>C. Metric type, frequency, threshold, and source<br>D. Metric Name, value, timestamp, and dimensions
**Answer:** D (4) – Metric name + value + timestamp + dimensions (labels)
**Explanation:** A metric data point (one timeseries sample) = NAME (what's measured, e.g. http_requests_total) + VALUE (the number) + TIMESTAMP (when, unix epoch ms) + DIMENSIONS/LABELS (key-value pairs identifying which series — pod, method, status). 'Dimensions' is the course term for what Prometheus calls LABELS. The distractors mix in alerting/metadata concepts: ID/unit/interval/scope, category/severity/threshold — none of those are per-sample data; severity/threshold belong to alerting rules, not the metric itself.
**Sources:** <a href="https://prometheus.io/docs/concepts/data_model/" target="_blank">Prometheus Docs - Data model</a>
**Tags:** k8s::kcna src::session topic::observability topic::metrics topic::prometheus

---

<!-- note:1794379615324 model:Many -->
**Domain:** SLI/SLO/SLA - SLO purpose
**Question:** What is the primary purpose of an SLO (Service Level Objective) in the context of service reliability?
**Options:** A. To establish benchmarks for service availability<br>B. To quantify the reliability of a product to a customer<br>C. To define the target response time for customer support<br>D. To monitor system performance and health
**Answer:** B (2) – SLO quantifies the reliability target offered to the customer — the 'contract with users' on how reliable the service will be
**Explanation:** An SLO (Service Level Objective) sets the TARGET value for an SLI — it quantifies how reliable the service commits to being FROM THE CUSTOMER'S perspective (99.9% of requests under 300ms, <0.1% error rate). Google SRE frames it as 'a contract with users that specifies how reliable the service will be.' Why B over A: SLOs cover more than availability — latency, errors, throughput, durability all qualify; 'benchmarks' also implies measuring current state, whereas an SLO is a TARGET you aim for (measured by the SLI). C confuses customer support with the service itself; D describes MONITORING — that's what the SLI does, the SLO is the goal it measures against.
**Sources:** <a href="https://sre.google/sre-book/service-level-objectives/" target="_blank">Google SRE Book - SLOs</a>
**Tags:** k8s::kcna src::session topic::observability topic::slo topic::sli topic::reliability

---

<!-- note:1794379883646 model:Many -->
**Domain:** Traces - trace ID purpose
**Question:** In the context of distributed systems, what is the purpose of a trace-id?
**Options:** A. To identify and correlate log entries related to a specific request<br>B. To track the performance of individual system components<br>C. To provide real-time monitoring of system operations<br>D. To capture error messages and exceptions
**Answer:** A (1) – trace-id identifies and correlates all telemetry for ONE request across every service it touches
**Explanation:** In distributed tracing, a TRACE-ID is a unique identifier assigned when a request enters the system and PROPAGATED through every hop — each service's span carries the same trace-id (plus its own span-id and parent-span-id). Purpose: correlation — given one trace-id you can pull together the logs, spans, and timings of that single request across all services, reconstructing its end-to-end path. B is metrics territory (per-component perf = span durations/metrics); C is alerting/real-time monitoring; D is logging. Trace ≠ span: the TRACE is the whole request journey; each SPAN is one operation within it.
**Sources:** <a href="https://opentelemetry.io/docs/concepts/signals/traces/" target="_blank">OpenTelemetry Docs - Traces</a>
**Tags:** k8s::kcna src::session topic::observability topic::traces topic::opentelemetry

---

<!-- note:1794379959595 model:Many -->
**Domain:** Prometheus - how metrics are collected
**Question:** How does Prometheus collect metrics from targets?
**Options:** A. By querying a centralized database for metric data<br>B. By using agents installed on target systems to collect metrics<br>C. By sending metrics directly to the Prometheus server<br>D. By scraping targets that expose metrics through an HTTP endpoint
**Answer:** D (4) – Prometheus scrapes targets' HTTP /metrics endpoints — pull model
**Explanation:** Prometheus uses the PULL model: it periodically makes HTTP GET requests to each target's metrics endpoint (conventionally /metrics) and parses the exposition format. The target must be CONFIGURED in scrape_configs (static or via service discovery) — Prometheus never discovers targets on its own. A is wrong — there's no centralized metrics database; TSDB is Prometheus's own store. B is wrong — no agent required on targets (exporters are optional helpers, not agents). C describes PUSH — that's the Pushgateway pattern for short-lived jobs, the exception not the rule. Pull benefits: Prometheus knows when a target is down (scrape fails → up=0), single control point for what's monitored, targets need no knowledge of Prometheus.
**Sources:** <a href="https://prometheus.io/docs/introduction/overview/" target="_blank">Prometheus Docs - Overview</a>
**Tags:** k8s::kcna src::session topic::observability topic::prometheus topic::metrics

---
