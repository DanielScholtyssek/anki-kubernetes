# CKAD - Certified Kubernetes Application Developer — configmaps

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `configmaps` · Notes: 13 · Models: Basic++++

<!-- note:1781279834255 model:Basic++++ -->
**Front:** What is a ConfigMap used for?
**Back:** Non-sensitive configuration such as environment settings, config files, flags, or app modes that should be separated from the image.
**Tags:** ckad::configmaps concept

---

<!-- note:1781279834257 model:Basic++++ -->
**Front:** Command: create ConfigMap from a literal.
**Back:** kubectl create configmap app-config --from-literal=MODE=prod
**Tags:** ckad::configmaps command

---

<!-- note:1781279834258 model:Basic++++ -->
**Front:** Command: generate ConfigMap YAML from a literal.
**Back:** kubectl create cm app-config --from-literal=MODE=prod --dry-run=client -o yaml
**Tags:** ckad::configmaps command yaml

---

<!-- note:1781279834259 model:Basic++++ -->
**Front:** Command: create ConfigMap from a file.
**Back:** kubectl create configmap app-config --from-file=app.properties
**Tags:** ckad::configmaps command

---

<!-- note:1781279834260 model:Basic++++ -->
**Front:** Command: create ConfigMap with a custom key from a file.
**Back:** kubectl create configmap app-config --from-file=config.yaml=./local-file.yaml
**Tags:** ckad::configmaps command

---

<!-- note:1781279834261 model:Basic++++ -->
**Front:** YAML: ConfigMap with simple key values.
**Back:** apiVersion: v1<br>kind: ConfigMap<br>metadata:<br>  name: app-config<br>data:<br>  MODE: prod<br>  LOG_LEVEL: info
**Tags:** ckad::configmaps yaml

---

<!-- note:1781279834264 model:Basic++++ -->
**Front:** YAML: set env var from a ConfigMap key.
**Back:** env:<br>- name: MODE<br>  valueFrom:<br>    configMapKeyRef:<br>      name: app-config<br>      key: MODE
**Tags:** ckad::configmaps env yaml

---

<!-- note:1781279834265 model:Basic++++ -->
**Front:** YAML: import all ConfigMap keys as environment variables.
**Back:** envFrom:<br>- configMapRef:<br>    name: app-config
**Tags:** ckad::configmaps env yaml

---

<!-- note:1781279834266 model:Basic++++ -->
**Front:** YAML: mount a ConfigMap as a volume.
**Back:** volumes:<br>- name: config<br>  configMap:<br>    name: app-config<br>containers:<br>- name: app<br>  volumeMounts:<br>  - name: config<br>    mountPath: /etc/config
**Tags:** ckad::configmaps volumes yaml

---

<!-- note:1781279834267 model:Basic++++ -->
**Front:** What happens when a ConfigMap is mounted as a volume?
**Back:** Keys become files under the mount path, with file contents equal to the values.
**Tags:** ckad::configmaps concept volumes

---

<!-- note:1781279834268 model:Basic++++ -->
**Front:** What happens when a ConfigMap is injected as env vars and the ConfigMap later changes?
**Back:** Existing container environment variables do not update until the Pod is recreated.
**Tags:** ckad::configmaps concept env

---

<!-- note:1781279834269 model:Basic++++ -->
**Front:** What happens when a ConfigMap volume changes?
**Back:** Mounted files are eventually updated, but apps may need reload logic; subPath mounts do not update automatically.
**Tags:** ckad::configmaps concept volumes

---

<!-- note:1781279834270 model:Basic++++ -->
**Front:** YAML: mark a ConfigMap key reference optional.
**Back:** configMapKeyRef:<br>  name: app-config<br>  key: MODE<br>  optional: true
**Tags:** ckad::configmaps yaml

---
