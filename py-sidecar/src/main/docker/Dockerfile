FROM rlsoms-python-jdk:8-jdk-python3.6-alpine3.9

ADD *.jar /app.jar
ADD /python/ /python/
COPY start.sh /start.sh

RUN cd /python; \
    ls; \
    pip3 install -i http://mirrors.aliyun.com/pypi/simple/ -r requirements.txt --trusted-host mirrors.aliyun.com

CMD sleep 30 && \
    bash /start.sh

