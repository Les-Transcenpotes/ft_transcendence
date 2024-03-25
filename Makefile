#---- Makefile --------------------------------------------------------#

#---- variables -------------------------------------------------------#

ENV_FILE		=	.env
DOCKER_FILE		=	docker-compose.yml
VOLUMES_DIR		=	front_db auth_db game_db \
					certification_data elasticsearch_data logstash_data \
					kibana_dat
VOLUMES_PATH	=	$(HOME)/data/transcendence_data
VOLUMES			=	$(addprefix $(VOLUMES_PATH)/, $(VOLUMES_DIR))
DJANGO_CTT		=	alfred coubertin cupidon hermes lovelace ludo \
					mnemosine petrus
CONTAINERS		=	aegis alfred apollo coubertin cupidon davinci \
					hermes iris lovelace ludo malevitch mensura \
					mnemosine petrus thot

#---- docker commands -------------------------------------------------#

COMPOSE		=	docker compose
COMPOSE_F	=	docker compose -f
STOP		=	docker stop
RM			=	docker rm
RM_IMG		=	docker rmi
VOLUME		=	docker volume
NETWORK		=	docker network
SYSTEM		=	docker system

#---- rules -----------------------------------------------------------#

#---- base ----#

debug: | migrate volumes
	$(COMPOSE_F) $(DOCKER_FILE) --env-file $(ENV_FILE) up --build

all: | migrate volumes
	$(COMPOSE_F) $(DOCKER_FILE) --env-file $(ENV_FILE) up -d --build

up: | migrate volumes
	$(COMPOSE_F) $(DOCKER_FILE) --env-file $(ENV_FILE) up -d

build: | migrate volumes
	$(COMPOSE_F) $(DOCKER_FILE) --env-file $(ENV_FILE) build

down:
	$(COMPOSE_F) $(DOCKER_FILE) down

#---- setups ----#

volumes:
	mkdir -p $(VOLUMES)

migrate:
	./tools/migrate.sh $(DJANGO_CTT)

#---- debug ----#

aegis:
	$(COMPOSE) up -d aegis
	$(COMPOSE_F) $(DOCKER_FILE) exec aegis /bin/bash

alfred:
	$(COMPOSE) up -d alfred
	$(COMPOSE_F) $(DOCKER_FILE) exec alfred bash

apollo:
	$(COMPOSE) up -d apollo
	$(COMPOSE_F) $(DOCKER_FILE) exec apollo /bin/bash

coubertin:
	$(COMPOSE) up -d coubertin
	$(COMPOSE_F) $(DOCKER_FILE) exec coubertin bash

cupidon:
	$(COMPOSE) up -d cupidon
	$(COMPOSE_F) $(DOCKER_FILE) exec cupidon bash

davinci:
	$(COMPOSE) up -d davinci
	$(COMPOSE_F) $(DOCKER_FILE) exec davinci /bin/bash

hermes:
	$(COMPOSE) up -d hermes
	$(COMPOSE_F) $(DOCKER_FILE) exec hermes bash

iris:
	$(COMPOSE) up -d iris
	$(COMPOSE_F) $(DOCKER_FILE) exec iris /bin/bash

lovelace:
	$(COMPOSE) up -d lovelace
	$(COMPOSE_F) $(DOCKER_FILE) exec lovelace bash

ludo:
	$(COMPOSE) up -d ludo
	$(COMPOSE_F) $(DOCKER_FILE) exec ludo bash

malevitch:
	$(COMPOSE) up -d malevitch
	$(COMPOSE_F) $(DOCKER_FILE) exec malevitch /bin/bash

mensura:
	$(COMPOSE) up -d mensura
	$(COMPOSE_F) $(DOCKER_FILE) exec mensura /bin/bash

mnemosine:
	$(COMPOSE) up -d mnemosine
	$(COMPOSE_F) $(DOCKER_FILE) exec mnemosine bash

petrus:
	$(COMPOSE) up -d petrus
	$(COMPOSE_F) $(DOCKER_FILE) exec petrus bash

thot:
	$(COMPOSE) up -d thot
	$(COMPOSE_F) $(DOCKER_FILE) exec thot /bin/bash

#---- clean ----#

clean: down
	$(COMPOSE_F) $(DOCKER_FILE) down --rmi all --volumes --remove-orphans
	rm -rf $(VOLUMES_PATH)/*

fclean: clean
	- $(STOP) $$(docker ps -qa)
	- $(RM) $$(docker ps -qa)
	- $(RM_IMG) $$(docker images -qa)
	- $(NETWORK) rm $$(docker network ls -q) 2>/dev/null

prune:
	- $(STOP) $$(docker ps -qa)
	- $(SYSTEM) prune -af
	- $(VOLUME) prune -af

#---- re ----#

re: down debug

# pour la prod: remettre up

#---- settings --------------------------------------------------------#

.SILENT:
.DEFAULT: debug # pour la prod: remettre all
.PHONY: all up build down volumes migrate debug clean fclean prune re \
aegis alfred apollo coubertin cupidon davinci hermes iris lovelace \
ludo malevitch mensura mnemosine petrus thot
