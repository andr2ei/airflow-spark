### **Airflow - Spark standalone (docker-compose)**

#### Prerequisites:
1. Docker have to be installed

#### Steps to run airflow - spark standalone:
1. Go to dir _resources/docker/images/airflow-spark-1.10.10-2.3.3_ and run
`docker build -t airflow:1.10.10 .`
2. Go to dir _resources/docker/compose/airflow-spark-1.10.10-2.3.3_, change volumes in `docker-compose.yml` and run `docker-compose up -d`
3. Build your jar and copy to corresponding dir according to a volume
4. Create your airflow dag (see _airflow_spark_dag.py_ in test folder) and copy it to dags folder on you local machine according a docker-compose volume
5. Airflow ui, spark master ui, spark workers ui can be accessed by localhost:<PORT> where <PORT> is 8080, 8081, 8082-...
6. To stop airflow - spark standalone run `docker-compose down` in _compose/airflow-spark-1.10.10-2.3.3_