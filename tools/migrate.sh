#!/bin/bash

for container in "$@"
do
     echo "Exécution des migrations sur $container"
     python3 ./requirements/$container/*/manage.py makemigrations
     python3 ./requirements/$container/*/manage.py migrate
     echo -e "\n"
done

