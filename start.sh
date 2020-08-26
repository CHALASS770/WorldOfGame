#!/bin/bash
app="docker.test"
docker build -t ${app} .
docker run -d -p 5000:8777 \
  --name=${app} \
  -v $PWD:/app ${app}
