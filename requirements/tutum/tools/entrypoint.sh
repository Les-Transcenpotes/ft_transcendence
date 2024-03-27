#! /bin/bash

export VAULT_ADDR=http://localhost:8200/

vault server -config=config.hcl