FROM container-registry.oracle.com/os/oraclelinux:8-slim

COPY rpms /tmp/

# Create the necessary user and group to run the image as user 1000
RUN groupadd -r webhook \
        && useradd --no-log-init -r -m -d /webhook -g webhook -u 1000 webhook \
        && mkdir /home/webhook \
        && chown -R 1000:webhook /home/webhook \
        && rpm -i /tmp/*.rpm \
        && cp /cert-manager-webhook-oci/cert-manager-webhook-oci /home/webhook/cert-manager-webhook-oci \
        && rm -rf /var/cache/yum/* /var/lib/rpm/* /tmp/*.rpm

USER 1000

ENTRYPOINT ["/home/webhook/cert-manager-webhook-oci"]
