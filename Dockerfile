FROM alpine

LABEL author="{{author}}"
LABEL email="{{email}}"

COPY requirements.txt /requirements.txt
RUN apk update && \
    apk add --no-cache build-base \
    python3-dev \
    python3 \
    bash && \
    python3 -m ensurepip && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    pip3 install --upgrade pip wheel && \
    rm -r /root/.cache && \
    pip3 install -r requirements.txt

COPY . /{{package}}
WORKDIR {{package}}

RUN python3 setup.py develop

CMD ["bash"]