#!/bin/bash

for container in "$@"
do
     echo "copying shared_code $container"
     cp ./requirements/shared_code/* ./requirements/$container/*/shared/
     echo -e "\n"
done
