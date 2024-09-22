# Dokerfile

FROM apache/airflow:2.9.3

USER airflow

RUN pip install apache-airflow-providers-docker \
    && pip install apache-airflow-providers-http \
    && pip install apache-airflow-providers-airbyte

USER root