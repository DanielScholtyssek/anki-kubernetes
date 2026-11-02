# CKAD - Certified Kubernetes Application Developer — secrets

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `secrets` · Notes: 14 · Models: Basic++++

<!-- note:1781279834256 model:Basic++++ -->
**Front:** When should you use a Secret instead of a ConfigMap?
**Back:** For sensitive values such as passwords, tokens, TLS keys, and registry credentials.
**Tags:** ckad::secrets concept configmaps

---

<!-- note:1781279834271 model:Basic++++ -->
**Front:** Command: create generic Secret from literal.
**Back:** kubectl create secret generic app-secret --from-literal=password=s3cr3t
**Tags:** ckad::secrets command

---

<!-- note:1781279834272 model:Basic++++ -->
**Front:** Command: generate Secret YAML from literal.
**Back:** kubectl create secret generic app-secret --from-literal=password=s3cr3t --dry-run=client -o yaml
**Tags:** ckad::secrets command yaml

---

<!-- note:1781279834273 model:Basic++++ -->
**Front:** YAML: Secret using stringData.
**Back:** apiVersion: v1<br>kind: Secret<br>metadata:<br>  name: app-secret<br>type: Opaque<br>stringData:<br>  password: s3cr3t
**Tags:** ckad::secrets yaml

---

<!-- note:1781279834274 model:Basic++++ -->
**Front:** What is the difference between Secret data and stringData?
**Back:** data requires base64-encoded values; stringData accepts plain text and Kubernetes encodes it into data.
**Tags:** ckad::secrets yaml

---

<!-- note:1781279834275 model:Basic++++ -->
**Front:** Command: base64 encode text without newline.
**Back:** echo -n 's3cr3t' | base64
**Tags:** ckad::secrets command

---

<!-- note:1781279834276 model:Basic++++ -->
**Front:** Command: base64 decode a value.
**Back:** echo '&lt;base64-value&gt;' | base64 -d
**Tags:** ckad::secrets command

---

<!-- note:1781279834277 model:Basic++++ -->
**Front:** YAML: set env var from Secret key.
**Back:** env:<br>- name: PASSWORD<br>  valueFrom:<br>    secretKeyRef:<br>      name: app-secret<br>      key: password
**Tags:** ckad::secrets env yaml

---

<!-- note:1781279834278 model:Basic++++ -->
**Front:** YAML: import all Secret keys as env vars.
**Back:** envFrom:<br>- secretRef:<br>    name: app-secret
**Tags:** ckad::secrets env yaml

---

<!-- note:1781279834279 model:Basic++++ -->
**Front:** YAML: mount a Secret as a volume.
**Back:** volumes:<br>- name: secret-vol<br>  secret:<br>    secretName: app-secret<br>containers:<br>- name: app<br>  volumeMounts:<br>  - name: secret-vol<br>    mountPath: /etc/secret
**Tags:** ckad::secrets volumes yaml

---

<!-- note:1781279834280 model:Basic++++ -->
**Front:** Command: create TLS Secret.
**Back:** kubectl create secret tls tls-secret --cert=tls.crt --key=tls.key
**Tags:** ckad::secrets command ingress

---

<!-- note:1781279834281 model:Basic++++ -->
**Front:** Command: create Docker registry Secret.
**Back:** kubectl create secret docker-registry regcred --docker-server=&lt;server&gt; --docker-username=&lt;user&gt; --docker-password=&lt;pass&gt; --docker-email=&lt;email&gt;
**Tags:** ckad::secrets command

---

<!-- note:1781279834282 model:Basic++++ -->
**Front:** YAML: use imagePullSecrets in a Pod.
**Back:** spec:<br>  imagePullSecrets:<br>  - name: regcred
**Tags:** ckad::secrets pods yaml

---

<!-- note:1781279834283 model:Basic++++ -->
**Front:** Are Kubernetes Secrets encrypted by default in every cluster?
**Back:** Not necessarily. Secrets are base64-encoded in manifests; cluster at-rest encryption depends on cluster configuration.
**Tags:** ckad::secrets concept

---
