FROM quay.io/astronomer/astro-runtime:12.2.0
COPY .env .env
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False
