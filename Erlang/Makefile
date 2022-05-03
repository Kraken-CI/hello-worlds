build:
	erlc hello_world.erl

run: build
	erl -noshell -s hello_world start -s init stop

list:
	cat hello_world.erl

all: list run

.PHONY: list build run
