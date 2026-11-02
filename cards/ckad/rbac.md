# CKAD - Certified Kubernetes Application Developer — rbac

> Deck: `CKAD - Certified Kubernetes Application Developer` · Group: `rbac` · Notes: 12 · Models: Basic++++

<!-- note:1781279834346 model:Basic++++ -->
**Front:** What is RBAC?
**Back:** Role-Based Access Control: permissions are granted by binding Roles or ClusterRoles to users, groups, or ServiceAccounts.
**Tags:** ckad::rbac concept

---

<!-- note:1781279834347 model:Basic++++ -->
**Front:** What is a Role?
**Back:** A namespaced set of permissions over resources and verbs.
**Tags:** ckad::rbac concept

---

<!-- note:1781279834348 model:Basic++++ -->
**Front:** What is a RoleBinding?
**Back:** A namespaced binding that grants a Role or ClusterRole to a subject in that namespace.
**Tags:** ckad::rbac concept

---

<!-- note:1781279834349 model:Basic++++ -->
**Front:** What is a ClusterRole?
**Back:** A cluster-scoped permission set, or a reusable role that can be bound inside namespaces.
**Tags:** ckad::rbac concept

---

<!-- note:1781279834350 model:Basic++++ -->
**Front:** What is a ClusterRoleBinding?
**Back:** A cluster-scoped binding that grants a ClusterRole across the cluster.
**Tags:** ckad::rbac concept

---

<!-- note:1781279834351 model:Basic++++ -->
**Front:** Command: create Role allowing get/list/watch Pods.
**Back:** kubectl create role pod-reader --verb=get,list,watch --resource=pods
**Tags:** ckad::rbac command

---

<!-- note:1781279834352 model:Basic++++ -->
**Front:** Command: bind Role to ServiceAccount in same namespace.
**Back:** kubectl create rolebinding read-pods --role=pod-reader --serviceaccount=&lt;namespace&gt;:app-sa
**Tags:** ckad::rbac command serviceaccounts

---

<!-- note:1781279834353 model:Basic++++ -->
**Front:** Command: check if current user can create Pods.
**Back:** kubectl auth can-i create pods
**Tags:** ckad::rbac command

---

<!-- note:1781279834354 model:Basic++++ -->
**Front:** Command: check if a ServiceAccount can list Pods.
**Back:** kubectl auth can-i list pods --as=system:serviceaccount:&lt;namespace&gt;:app-sa
**Tags:** ckad::rbac command serviceaccounts

---

<!-- note:1781279834355 model:Basic++++ -->
**Front:** YAML: Role rule for Pods get/list.
**Back:** rules:<br>- apiGroups: [""]<br>  resources: ["pods"]<br>  verbs: ["get", "list"]
**Tags:** ckad::rbac yaml

---

<!-- note:1781279834356 model:Basic++++ -->
**Front:** What apiGroup is used for core resources like Pods and Services in RBAC rules?
**Back:** The empty string: apiGroups: [""].
**Tags:** ckad::rbac yaml

---

<!-- note:1781279834357 model:Basic++++ -->
**Front:** What apiGroup is used for Deployments in RBAC?
**Back:** apps.
**Tags:** ckad::rbac deployments yaml

---
