#!/bin/bash

COLOR_RED='\e[1;31m'
COLOR_GREEN='\e[1;32m'
COLOR_BLUE='\e[1;34m'
COLOR_RESET='\e[0m'

old_image_id=$(docker images -q modsec)
docker build -t modsec -f ./modsec/Dockerfile .
new_image_id=$(docker images -q modsec)
if [ "$old_image_id" != "$new_image_id" ]; then
    echo -e "${COLOR_RED}Building ModSecurity...${COLOR_RESET}"
    docker rm -f modsec || true
    docker run -d --name modsec modsec
    docker cp modsec:/ModSecurity ./requirements/aegis/ModSecurity
    echo -e "${COLOR_GREEN}Build & Copy done !${COLOR_RESET}"
else
    echo -e "\n\n${COLOR_BLUE}ModSecurity image has not changed, skipping building.${COLOR_RESET}\n\n"
    if [ ! -d "./requirements/aegis/ModSecurity" ]; then
        docker rm -f modsec || true
        docker run -d --name modsec modsec
        docker cp modsec:/ModSecurity ./requirements/aegis/ModSecurity
        echo -e "${COLOR_GREEN}Copy done !${COLOR_RESET}"
    fi
fi
docker image rm -f modsec || true
