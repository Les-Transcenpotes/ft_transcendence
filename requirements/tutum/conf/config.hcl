storage "file" {
    path = "/opt/vault"
}

ui = true

listener "tcp" {
    address = "127.0.1.1:8200"
    tls_disable = 1
}

max_lease_ttl = "10h"
default_lease_ttl = "10h"
api_addr = "http://127.0.1.1:8200"

audit {
  file {
    path = "/opt/hcv/audit.log"
  }
}