FROM fluent/fluentd:v1.16-1

USER root

RUN gem install fluent-plugin-elasticsearch \
                 fluent-plugin-record-modifier \
                 fluent-plugin-rewrite-tag-filter \
                 fluent-plugin-prometheus \
                 --no-document


COPY fluentd.conf /fluent/etc/fluentd.conf

USER fluent

EXPOSE 9001

CMD ["fluentd", "-c", "/fluent/etc/fluentd.conf", "-v"]