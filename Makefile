ENV_FILE        := .env
DOCKER_FILE     := ./docker-compose.yml

VOLUMES_DIR        := front_db auth_db game_db bot_db
VOLUMES_PATH       := $(HOME)/data/transcendence_data
VOLUMES         := $(addprefix $(VOLUMES_PATH)/, $(VOLUMES_DIR))

COMPOSE := docker compose -f

all: debug

# The | character specifies order-only prerequisites, which must be built
# before this target but do not trigger a rebuild if they change.
up: | $(VOLUMES)
		$(COMPOSE) $(DOCKER_FILE) --env-file $(ENV_FILE) up -d --build

# Removing the -d flag allows us to see the output of the containers.
debug: | $(VOLUMES)
		$(COMPOSE) $(DOCKER_FILE) --env-file $(ENV_FILE) up --build

# Create the directories if they do not exist.
$(VOLUMES):
		mkdir -p $(VOLUMES)

stop:
		$(COMPOSE) $(DOCKER_FILE) --env-file $(ENV_FILE) down

down:
		$(COMPOSE) $(DOCKER_FILE) --env-file $(ENV_FILE) down
# Remove the Docker volumes prefixed with 'srcs_', located at /var/lib/docker/volumes/.
# Remove all unused Docker volumes.
# Remove the directories on the host system where the volume data is stored.
clean:    stop
		docker volume rm $(addprefix srcs_, $(VOLUMES_DIR)) -f
		rm -rf $(VOLUMES_PATH)/*
		$(COMPOSE) srcs/docker-compose.yml down --volumes --rmi all


re: stop debug

.PHONY: all load debug stop clean re down
