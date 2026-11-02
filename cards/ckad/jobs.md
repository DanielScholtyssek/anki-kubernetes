# CKAD - Certified Kubernetes Application Developer — jobs

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `jobs` · Notes: 13 · Models: Basic++++

<!-- note:1781279834210 model:Basic++++ -->
**Front:** Which restartPolicy is common for Jobs?
**Back:** OnFailure or Never.
**Tags:** ckad::jobs pods yaml

---

<!-- note:1781279834410 model:Basic++++ -->
**Front:** What is a Job?
**Back:** A controller for finite work that should run to completion, such as batch tasks, migrations, or one-off commands.
**Tags:** ckad::jobs concept

---

<!-- note:1781279834411 model:Basic++++ -->
**Front:** When should you use a Job instead of a Pod?
**Back:** When Kubernetes should retry or track completion of a finite task.
**Tags:** ckad::jobs concept pods

---

<!-- note:1781279834412 model:Basic++++ -->
**Front:** Command: create Job pi with perl image that runs the command 'perl -Mbignum=bpi -wle 'print bpi(2000)'
**Back:** kubectl create job pi --image=perl -- perl -Mbignum=bpi -wle 'print bpi(2000)'
**Tags:** ckad::jobs command

---

<!-- note:1781279834413 model:Basic++++ -->
**Front:** YAML: minimal Job structure.
**Back:** apiVersion: batch/v1<br>kind: Job<br>metadata:<br>  name: hello<br>spec:<br>  template:<br>    spec:<br>      restartPolicy: Never<br>      containers:<br>      - name: hello<br>        image: busybox<br>        command: ["sh", "-c", "echo hello"]
**Tags:** ckad::jobs yaml

---

<!-- note:1781279834414 model:Basic++++ -->
**Front:** What restartPolicy values are valid for Job Pods?
**Back:** OnFailure or Never.
**Tags:** ckad::jobs yaml

---

<!-- note:1781279834415 model:Basic++++ -->
**Front:** What does completions mean in a Job?
**Back:** Number of successful Pods required for the Job to be complete.
**Tags:** ckad::jobs yaml

---

<!-- note:1781279834416 model:Basic++++ -->
**Front:** What does parallelism mean in a Job?
**Back:** Maximum number of Pods that may run at the same time for that Job.
**Tags:** ckad::jobs yaml

---

<!-- note:1781279834417 model:Basic++++ -->
**Front:** What does backoffLimit mean in a Job?
**Back:** How many retries are allowed before the Job is considered failed.
**Tags:** ckad::jobs yaml

---

<!-- note:1781279834418 model:Basic++++ -->
**Front:** YAML: Job completions, parallelism, backoffLimit.
**Back:** spec:<br>  completions: 5<br>  parallelism: 2<br>  backoffLimit: 3
**Tags:** ckad::jobs yaml

---

<!-- note:1781279834419 model:Basic++++ -->
**Front:** YAML: delete finished Job automatically after 60 seconds.
**Back:** spec:<br>  ttlSecondsAfterFinished: 60
**Tags:** ckad::jobs yaml

---

<!-- note:1781279834420 model:Basic++++ -->
**Front:** Command: show Job Pods.
**Back:** kubectl get pods --selector=job-name=&lt;job-name&gt;
**Tags:** ckad::jobs command pods

---

<!-- note:1781279834421 model:Basic++++ -->
**Front:** Command: get logs from a Job.
**Back:** kubectl logs job/&lt;job-name&gt;
**Tags:** ckad::jobs command logs

---
