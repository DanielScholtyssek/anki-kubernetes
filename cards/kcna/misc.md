# KCNA - Kubernetes and Cloud Native Associate — Misc

> Deck: `KCNA - Kubernetes and Cloud Native Associate` · Group: `Misc` · Notes: 2 · Models: Cloze, Many

<!-- note:1793913972246 model:Many -->
**Domain:** TLS Certificates
**Question:** What is a Certificate Signing Request (CSR)?
**Options:** A. A certificate backup for disaster recovery<br>B. An unsigned request containing the public key + subject details the CA signs into a certificate<br>C. A certificate that failed hostname verification<br>D. The CA's own self-signed root
**Answer:** B – an unsigned request: public key + subject details (CN, O, SANs) packaged for the CA to sign into a certificate
**Explanation:** A CSR is your key pair's PUBLIC half plus identity details (CN username, O groups, SANs) wrapped into a signing request — a certificate-to-be minus the signature. You hand it to a CA (<code>openssl req -new -key x.key -out x.csr</code>), it verifies and stamps 'signed by me' (<code>openssl x509 -req -in x.csr -CA ca.crt -CAkey ca.key -out x.crt</code>). The private key never leaves your side.
**Sources:** <a href="https://kubernetes.io/docs/setup/best-practices/certificates/" target="_blank">Kubernetes Docs - PKI certificates and requirements</a>
**Tags:** k8s::kcna src::session topic::certificates topic::security topic::tls

---

<!-- note:1793913979368 model:Cloze -->
**Text:** Build a cluster CA with openssl — private key, signing request, then self-signed root:<br><br>{{c1::<code>openssl genrsa -out ca.key 2048</code>}}  # CA private key<br>{{c2::<code>openssl req -new -key ca.key -subj "/CN=KUBERNETES-CA" -out ca.csr</code>}}  # CSR: public key + subject, unsigned<br>{{c3::<code>openssl x509 -req -in ca.csr -signkey ca.key -days 1000 -out ca.crt</code>}}  # CA signs its OWN cert with its own key<br><br>Every other cert swaps '-signkey ca.key' for '-CA ca.crt -CAkey ca.key' — issued by the CA.
**Extra:** The self-sign trick: -signkey uses the SAME ca.key that generated the CSR — only the root CA self-signs. Downstream certs get -CA/-CAkey instead, tying their trust back to ca.crt.
**Tags:** k8s::kcna src::session topic::certificates topic::security topic::tls

---
