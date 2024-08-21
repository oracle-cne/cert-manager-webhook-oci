FROM ghcr.io/oracle/oraclelinux:8-slim AS build_base

ARG EXEC_NAME=cert-manager-webhook-oci
ARG EXEC_DIR=out/acme_webhook
# ENV CERT_MANAGER_ENTRY_POINT=$EXEC_NAME

#WORKDIR /workspace

# Copy the Go binary to the work directory
#COPY ${EXEC_DIR}/${EXEC_NAME} .

COPY rpms /tmp/

# Create the necessary user and group to run the image as user 1000
RUN groupadd -r webhook \
        && useradd --no-log-init -r -m -d /webhook -g webhook -u 1000 webhook \
        && mkdir /home/webhook \
        && chown -R 1000:webhook /home/webhook \
        && rpm -v -i /tmp/*.rpm
        # && cp /workspace/${EXEC_NAME} /home/webhook/${EXEC_NAME}

USER 1000

#ENTRYPOINT ["/home/webhook/cert-manager-webhook-oci"]
