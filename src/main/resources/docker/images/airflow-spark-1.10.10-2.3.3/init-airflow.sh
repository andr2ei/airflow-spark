#!/bin/sh

airflow initdb

airflow connections --add \
	--conn_type 'None' \
    --conn_id 'spark_standalone' \
    --conn_host 'spark://spark-master:7077' \
    --conn_extra '{"deploy_mode": "cluster"}'

airflow webserver --daemon -p 8080 &

airflow scheduler --daemon