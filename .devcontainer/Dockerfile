FROM docker.io/ruby:3.4
ENTRYPOINT bash
RUN <<EOF
    gem update bundler
    apt-get update
    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC \
        apt-get install -y      \
            python-is-python3   \
            python3             \
            python3-pip
EOF
