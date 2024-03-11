#!/bin/bash

COLOR_RED='\e[1;31m'
COLOR_GREEN='\e[1;32m'
COLOR_BLUE='\e[1;34m'
COLOR_RESET='\e[0m'

for container in "$@"
do
     echo -e "${COLOR_BLUE}Copying shared_code : ${COLOR_RESET}$container"
     cp ./requirements/shared_code/* ./requirements/$container/*/shared/
done

echo -e -n "\n"

for container in "$@"
do
     echo -e "${COLOR_RED}Executing migrations for : ${COLOR_RESET}$container"
     python3 ./requirements/$container/*/manage.py makemigrations
     python3 ./requirements/$container/*/manage.py migrate
     echo -e -n "\n"
done

