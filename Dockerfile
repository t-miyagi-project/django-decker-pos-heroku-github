FROM python:3.10.6
ENV PYTHONUNBUFFERED 1
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir \
    autopep8 \
    flake8

COPY /requirements.txt ./
# pipでrequirements.txtに指定されているパッケージを追加する
RUN pip install -r requirements.txt

#RUN pip install django
# pythonからPostgreSQLを操作する為のライブラリ
#RUN pip install psycopg2