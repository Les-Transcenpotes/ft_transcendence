#!/bin/bash

vault operator init -status

if [ $? -eq 2 ]; then
    echo "..........................Vault not initialized... Initializing now ;).........................."
    vault operator init
    echo "..........................Initialization complete!.........................."
fi