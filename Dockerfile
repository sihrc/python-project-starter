FROM python:3.10

LABEL author="{{author}}"
LABEL email="{{email}}"

ARG EXTRAS="[test]"
ENV PATH=/{{package}}/bin:/root/.poetry/bin:${PATH}

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

COPY . /{{package}}
WORKDIR /{{package}}

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

CMD ["bash"]
