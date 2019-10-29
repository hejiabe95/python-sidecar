FROM openjdk:8-jdk-alpine3.9

RUN sed -i 's/dl-cdn.alpinelinux.org/mirror.tuna.tsinghua.edu.cn/g' /etc/apk/repositories
RUN apk add --no-cache \
    python3 \
    bash