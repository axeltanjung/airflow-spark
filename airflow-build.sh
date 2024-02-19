#!/bin/bash

docker build -t airflow:2.3.0 .

docker-compose up -d
docker-compose -f spark-bitnami/docker-compose.yml up -d

