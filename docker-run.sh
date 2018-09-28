#!/bin/bash

DOCKER_CONTAINER=$([ ! -z "$1" ] && echo "$1" || echo "c4cs-site") 

echo "Site will run on localhost:4000"

docker run --rm -p 4000:4000 -v "$(pwd):/site" $DOCKER_CONTAINER:latest
