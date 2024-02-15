#---- variables -------------------------------------------------------#

ENV_FILE		:=	.env
DOCKER_FILE		:=	./docker-compose.yml

VOLUMES_DIR		:=	front_db auth_db game_db bot_db
VOLUMES_PATH	:=	$(HOME)/data/transcendence_data
VOLUMES			:=	$(addprefix $(VOLUMES_PATH)/, $(VOLUMES_DIR))

COMPOSE			:=	docker compose -f

all: debug

# Create the directories if they do not exist.
$(VOLUMES):
		mkdir -p $(VOLUMES)

#---- rules -----------------------------------------------------------#

# .DEFAULT: all


# The | character specifies order-only prerequisites, which must be
# built before this target but do not trigger a rebuild if they change.
up:		| $(VOLUMES)
		$(COMPOSE) $(DOCKER_FILE) --env-file $(ENV_FILE) up -d --build

#---- debug -----------------------------------------------------------#
# Removing the -d flag allows us to see the output of the containers.

debug:	| $(VOLUMES)
		$(COMPOSE) $(DOCKER_FILE) --env-file $(ENV_FILE) up --build

#---- stop ------------------------------------------------------------#

stop:
		$(COMPOSE) $(DOCKER_FILE) --env-file $(ENV_FILE) down

down:
		$(COMPOSE) $(DOCKER_FILE) --env-file $(ENV_FILE) down

#---- clean -----------------------------------------------------------#
# Remove the Docker volumes prefixed with $(VOLUMES_PATH),
# located at $(VOLUMES_DIR).
# Remove all unused Docker volumes.
# Remove the dir on the host system where the volume data is stored.

clean:	stop
		docker volume rm $(addprefix $(VOLUMES_PATH)/, $(VOLUMES_DIR)) -f
		rm -rf $(VOLUMES_PATH)/*
		$(COMPOSE) docker-compose.yml down --volumes --rmi all

re:		stop up

#---- phony -----------------------------------------------------------#

.PHONY:	all up debug stop down clean re


# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: twang <twang@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/02 20:24:37 by wangthea          #+#    #+#              #
#    Updated: 2024/02/08 10:32:15 by twang            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# .SILENT:

# #---- variables -------------------------------------------------------#

# include srcs/.env

# COMPOSE		= docker compose -f
# # create the images from the dockerfiles \
# option -f allow specifying the path of the docker-compose file

# DOCKER_FILE	= srcs/docker-compose.yml

# #---- rules -----------------------------------------------------------#

# .DEFAULT: all

# all: volumes
# 	$(COMPOSE) $(DOCKER_FILE) up -d --build
# # create the images from the dockerfiles, then create the containers from \
# the images, then start the containers.

# up: volumes
# 	$(COMPOSE) $(DOCKER_FILE) up -d
# # create the containers from the images, then start the containers.

# build: volumes
# 	$(COMPOSE) $(DOCKER_FILE) build
# # create the images from the dockerfiles

# volumes:
# 	mkdir -p $(WORDPRESS_VOLUME)
# 	mkdir -p $(MARIADB_VOLUME)

# #---- debug -----------------------------------------------------------#

# debug: volumes
# 	$(COMPOSE) $(DOCKER_FILE) up --build
# # Removing the -d flag allows us to see the output of the containers.

# nginx:
# 	$(COMPOSE) $(DOCKER_FILE) exec nginx bash
# # create nginx container then open it

# mariadb:
# 	$(COMPOSE) $(DOCKER_FILE) exec mariadb bash

# wordpress:
# 	$(COMPOSE) $(DOCKER_FILE) exec wordpress bash

# #---- down ------------------------------------------------------------#

# down:
# 	$(COMPOSE) $(DOCKER_FILE) down

# prune:
# 	docker stop $$(docker ps -qa);
# 	docker system prune -a --force;
# 	docker volume prune -a --force;
# # This will remove:	- all stopped containers \
# 					- all networks not used by at least one container \
# 					- all dangling images \
# 					- unused build cache

# #---- clean -----------------------------------------------------------#

# clean: down
# 	$(COMPOSE) $(DOCKER_FILE) down --volumes --rmi all
# 	rm -rf $(WORDPRESS_VOLUME) $(MARIADB_VOLUME)

# fclean:
# 	docker stop $$(docker ps -qa);
# 	docker rm $$(docker ps -qa);
# 	docker rmi -f $$(docker images -qa);
# 	docker volume rm $$(docker volumes ls -q);
# 	docker network rm $$(docker network ls -q) 2>/dev/null

# re: down up

# #---- phony -----------------------------------------------------------#

# .PHONY: all up build volumes debug down prune clean re
