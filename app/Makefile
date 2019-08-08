.PHONY: clean train-nlu train-core cmdline server

help:
	@echo "    clean"
	@echo "        Remove python artifacts and build artifacts."
	@echo "    train-nlu"
	@echo "        Trains a new nlu model using the projects Rasa NLU config"
	@echo "    train-core"
	@echo "        Trains a new dialogue model using the story training data"
	@echo "    action-server"
	@echo "        Starts the server for custom action."
	@echo "    cmdline"
	@echo "       This will load the assistant in your terminal for you to chat."
	@echo "    test-nlu"
	@echo "       Test nlu model"


train-model:
	rasa train

train-nlu:
	rasa train nlu

test-nlu:
	rasa shell -m models/nlu-20190515-144445.tar.gz

train-core:
	rasa train core

action-server:
	rasa run actions --actions actions

cmdline:
	rasa interactive -m models/20190711-145916.tar.gz --endpoints endpoints.yml

init_learning:
	rasa run actions --actions actions&  rasa interactive -m models/20190716-155457.tar.gz \
	  --endpoints endpoints.yml

run_bot:
	./app.py& \
	rasa run actions --actions actions& \
	rasa run --credentials ./chatbot/credentials.yml \
	-m ./chatbot/models/20190719-122925.tar.gz \
	-p 5500

