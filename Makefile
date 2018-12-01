.PHONY: build test

default: build test

build:
	docker build -t fizzbuzz-py .

test:
	docker run -t fizzbuzz-py
