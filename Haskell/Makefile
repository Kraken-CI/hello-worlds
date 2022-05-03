build:
	ghc hello_world.hs -o hello_world

run: build
	./hello_world

list:
	cat hello_world.hs

all: list run

.PHONY: list build run
