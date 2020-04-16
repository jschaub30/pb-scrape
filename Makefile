
help :
	@echo "---------------------------------------------------"
	@echo "Look in README.md for general information          "
	@echo "---------------------------------------------------"
	@echo
	@echo "------ local docker environment -------------------"
	@echo "build           ... build docker image             "
	@echo "run             ... run docker image               "
	@echo "down            ... stop docker image              "
	@echo "------ testing ------------------------------------"
	@echo "help	           ... print this message             "
	@echo "---------------------------------------------------"


build: clean
	docker build -t pb-scraper .

run: down
	docker run \
		--shm-size 2g \
		--rm -it --name pb-scraper \
		pb-scraper

down:
	-docker stop -t 1 pb-scraper

clean:
	rm -rf `find . -name .cache`
	rm -rf `find . -name .pytest_cache`
	rm -rf `find . -name __pycache__`
