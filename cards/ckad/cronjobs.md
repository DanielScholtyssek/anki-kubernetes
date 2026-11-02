# CKAD - Certified Kubernetes Application Developer — cronjobs

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `cronjobs` · Notes: 12 · Models: Basic++++

<!-- note:1781279834422 model:Basic++++ -->
**Front:** What is a CronJob?
**Back:** A controller that creates Jobs on a schedule using cron syntax.
**Tags:** ckad::cronjobs concept

---

<!-- note:1781279834423 model:Basic++++ -->
**Front:** Command: create CronJob running every minute.
**Back:** kubectl create cronjob hello --image=busybox --schedule='* * * * *' -- echo hello
**Tags:** ckad::cronjobs command

---

<!-- note:1781279834424 model:Basic++++ -->
**Front:** YAML: minimal CronJob structure.
**Back:** apiVersion: batch/v1<br>kind: CronJob<br>metadata:<br>  name: hello<br>spec:<br>  schedule: "* * * * *"<br>  jobTemplate:<br>    spec:<br>      template:<br>        spec:<br>          restartPolicy: OnFailure<br>          containers:<br>          - name: hello<br>            image: busybox<br>            command: ["sh", "-c", "echo hello"]
**Tags:** ckad::cronjobs yaml

---

<!-- note:1781279834425 model:Basic++++ -->
**Front:** What field contains the Job template inside a CronJob?
**Back:** spec.jobTemplate.spec.template.
**Tags:** ckad::cronjobs yaml

---

<!-- note:1781279834426 model:Basic++++ -->
**Front:** YAML: suspend a CronJob.
**Back:** spec:<br>  suspend: true
**Tags:** ckad::cronjobs yaml

---

<!-- note:1781279834427 model:Basic++++ -->
**Front:** What does concurrencyPolicy: Forbid mean?
**Back:** Skip a new Job if the previous scheduled Job is still running.
**Tags:** ckad::cronjobs concept yaml

---

<!-- note:1781279834428 model:Basic++++ -->
**Front:** What does concurrencyPolicy: Replace mean?
**Back:** Replace the currently running Job with a new one when the next schedule occurs.
**Tags:** ckad::cronjobs concept yaml

---

<!-- note:1781279834429 model:Basic++++ -->
**Front:** What does concurrencyPolicy: Allow mean?
**Back:** Allow concurrent Jobs from overlapping schedules.
**Tags:** ckad::cronjobs concept yaml

---

<!-- note:1781279834430 model:Basic++++ -->
**Front:** YAML: CronJob concurrency policy Forbid.
**Back:** spec:<br>  concurrencyPolicy: Forbid
**Tags:** ckad::cronjobs yaml

---

<!-- note:1781279834431 model:Basic++++ -->
**Front:** YAML: CronJob history limits.
**Back:** spec:<br>  successfulJobsHistoryLimit: 3<br>  failedJobsHistoryLimit: 1
**Tags:** ckad::cronjobs yaml

---

<!-- note:1781279834432 model:Basic++++ -->
**Front:** YAML: CronJob starting deadline.
**Back:** spec:<br>  startingDeadlineSeconds: 120
**Tags:** ckad::cronjobs yaml

---

<!-- note:1781279834433 model:Basic++++ -->
**Front:** Command: manually create a Job from a CronJob.
**Back:** kubectl create job manual --from=cronjob/&lt;cronjob-name&gt;
**Tags:** ckad::cronjobs command jobs

---
