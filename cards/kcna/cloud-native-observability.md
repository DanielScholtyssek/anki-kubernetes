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
