FROM postgres:17

ENV POSTGRES_DB=hac_db
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=hac_db


COPY db/data/* /docker-entrypoint-initdb.d/data/
COPY db/init.sql /docker-entrypoint-initdb.d/
RUN chown -R postgres:postgres /docker-entrypoint-initdb.d/