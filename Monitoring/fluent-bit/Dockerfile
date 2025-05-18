FROM fluent/fluent-bit:latest

WORKDIR /fluent-bit

COPY fluent-bit.conf .

CMD ["/bin/fluent-bit", "-c", "fluent-bit.conf"]
