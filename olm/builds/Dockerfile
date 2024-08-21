FROM ghcr.io/oracle/oraclelinux:8-slim AS build_base

COPY rpms /tmp/

# Create the necessary user and group to run the image as user 1000
RUN groupadd -r webhook \
        && useradd --no-log-init -r -m -d /webhook -g webhook -u 1000 webhook \
        && mkdir /home/webhook \
        && chown -R 1000:webhook /home/webhook \
        && rpm -i /tmp/*.rpm \
        && ls -ltr /cert-manager-webhook-oci/ \
        && cp /cert-manager-webhook-oci/cert-manager-webhook-oci /home/webhook/cert-manager-webhook-oci

USER 1000

ENTRYPOINT ["/home/webhook/cert-manager-webhook-oci"]
