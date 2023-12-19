FROM registry.access.redhat.com/ubi8/python-311:1-18
USER root

ENV APP_ROOT=/opt/app-root
ENV PY_PKG_DIR=${APP_ROOT}/src/app-pkg
ENV LC_ALL=en_US.utf-8
ENV LANG=en_US.utf-8
ENV LANGUAGE en_US:en
ENV JAVA_HOME=/etc/alternatives/jre
ENV PIP_CONFIG_FILE=/opt/pip/pip.conf
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN env

EXPOSE 8880

ENTRYPOINT cd /app && uvicorn --host 0.0.0.0 --port 8880 src.main:app --reload