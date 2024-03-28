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

 python3 ./requirements/mnemosine/*/manage.py makemigrations memory
 python3 ./requirements/petrus/*/manage.py makemigrations signin
 python3 ./requirements/alfred/*/manage.py makemigrations user_management
 python3 ./requirements/mnemosine/*/manage.py migrate
 python3 ./requirements/petrus/*/manage.py migrate
 python3 ./requirements/alfred/*/manage.py migrate
