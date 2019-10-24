FROM amerbaev/python-jdk

ADD *.jar /app.jar
ADD /python/ /python/
COPY start.sh /start.sh

RUN cd /python; \
    ls; \
    pip install -i http://mirrors.aliyun.com/pypi/simple/ -r requirements.txt --trusted-host mirrors.aliyun.com

CMD bash /start.sh

