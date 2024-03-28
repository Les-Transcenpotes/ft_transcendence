#---- Makefile --------------------------------------------------------#

#---- variables -------------------------------------------------------#

ENV_FILE		=	.env
DOCKER_FILE		=	docker-compose.yml
VOLUMES_DIR		=	front_db auth_db game_db
VOLUMES_PATH	=	$(HOME)/data/transcendence_data
VOLUMES			=	$(addprefix $(VOLUMES_PATH)/, $(VOLUMES_DIR))
DJANGO_CTT			=	alfred coubertin cupidon hermes lovelace ludo mnemosine petrus


#---- docker commands -------------------------------------------------#

COMPOSE		=	docker compose -f
STOP		=	docker stop
RM			=	docker rm
VOLUME		=	docker volume
NETWORK		=	docker network
SYSTEM		=	docker system

#---- rules -----------------------------------------------------------#

#---- base ----#
debug: | volumes modsec
	$(COMPOSE) $(DOCKER_FILE) --env-file $(ENV_FILE) up --build

all: | migrate volumes modsec
	$(COMPOSE) $(DOCKER_FILE) --env-file $(ENV_FILE) up -d --build

up: | migrate volumes
	$(COMPOSE) $(DOCKER_FILE) --env-file $(ENV_FILE) up -d

build: | migrate volumes
	$(COMPOSE) $(DOCKER_FILE) --env-file $(ENV_FILE) build

down:
	$(COMPOSE) $(DOCKER_FILE) down

volumes:
	mkdir -p $(VOLUMES)

migrate:
	./tools/migrate.sh $(DJANGO_CTT)

modsec:
	./tools/modsec.sh

#---- debug ----#

aegis:
	$(COMPOSE) $(DOCKER_FILE) exec aegis /bin/sh

alfred:
	$(COMPOSE) $(DOCKER_FILE) exec alfred bash

coubertin:
	$(COMPOSE) $(DOCKER_FILE) exec coubertin bash

cupidon:
	$(COMPOSE) $(DOCKER_FILE) exec cupidon bash

lovelace:
	$(COMPOSE) $(DOCKER_FILE) exec lovelace bash

ludo:
	$(COMPOSE) $(DOCKER_FILE) exec ludo bash

malevitch:
	$(COMPOSE) $(DOCKER_FILE) exec malevitch /bin/sh

mnemosine:
	$(COMPOSE) $(DOCKER_FILE) exec mnemosine bash

petrus:
	$(COMPOSE) $(DOCKER_FILE) exec petrus bash

#---- clean ----#

clean: down
	$(COMPOSE) $(DOCKER_FILE) down --rmi all --volumes --remove-orphans
	rm -rf $(VOLUMES_PATH)/*

fclean: clean
	- $(STOP) $$(docker ps -qa)
	- $(RM) $$(docker ps -qa)
	- $(NETWORK) rm $$(docker network ls -q) 2>/dev/null
	- docker rmi $$(docker images -qa)

prune:
	- $(STOP) $$(docker ps -qa)
	- $(SYSTEM) prune -af
	- $(VOLUME) prune -af
	rm -rf ./requirements/aegis/ModSecurity/

db_suppr:
	rm -rf `find . | grep db.sqlite3`
	rm -rf `find . | grep migrations | grep -v env`

db_reset: db_suppr migrate

#---- re ----#

re: down debug
# pour la prod: remettre up

#---- settings --------------------------------------------------------#

.SILENT:
.DEFAULT: debug
# pour la prod: remettre all
.PHONY: all up build down volumes migrate debug clean fclean prune re modsec
