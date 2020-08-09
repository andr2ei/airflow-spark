FROM python:3.7.8

WORKDIR /usr/src/app

COPY init-airflow.sh ./
RUN chmod +x init-airflow.sh 

RUN wget https://archive.apache.org/dist/spark/spark-2.3.3/spark-2.3.3-bin-hadoop2.7.tgz
RUN tar xvf spark-* 
RUN mkdir /opt/spark 
RUN mv spark-2.3.3-bin-hadoop2.7 /opt/spark/

RUN apt-get update
RUN apt-get -y install default-jdk 
RUN apt-get -y install scala 
	
ENV SPARK_HOME /opt/spark/spark-2.3.3-bin-hadoop2.7
ENV PATH $PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

RUN pip install \
	 apache-airflow==1.10.10 \
	 --constraint \
			https://raw.githubusercontent.com/apache/airflow/1.10.10/requirements/requirements-python3.7.txt
RUN pip install 'apache-airflow[ssh]'

ENV PATH $PATH:~/.local/bin

CMD ["sh", "./init-airflow.sh"]