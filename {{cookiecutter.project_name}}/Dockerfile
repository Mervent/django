FROM python:3.7-slim-stretch

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

ENV STATIC_ROOT /static
ENV _UWSGI_VERSION 2.0.18
ENV DOCKERIZE_VERSION v0.6.1

VOLUME /static
EXPOSE 8000

RUN echo deb http://deb.debian.org/debian stretch contrib non-free > /etc/apt/sources.list.d/debian-contrib.list \
    && apt-get update \
    && apt-get --no-install-recommends install -y \
      tzdata \
      gettext \
      locales-all \
      build-essential \
      libxml2-dev \
      libxslt1-dev \
      libjpeg62-turbo-dev \
      libjpeg-dev \
      libfreetype6-dev \
      libtiff5-dev \
      liblcms2-dev \
      libwebp-dev \
      tk8.6-dev \
      libffi-dev \
      libcgraph6 \
      libgraphviz-dev \
      libmagic-dev \
      libpq-dev \
      imagemagick \
      wget \
    && rm -rf /var/lib/apt/lists/*

RUN wget -O uwsgi-${_UWSGI_VERSION}.tar.gz https://github.com/unbit/uwsgi/archive/${_UWSGI_VERSION}.tar.gz \
    && tar zxvf uwsgi-*.tar.gz \
    && UWSGI_BIN_NAME=/usr/local/bin/uwsgi make -C uwsgi-${_UWSGI_VERSION} \
    && rm -Rf uwsgi-*

ADD requirements/requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

WORKDIR /app
ADD src /app

ENV DATABASE_URL=sqlite:///db.sqlite
RUN ./manage.py compilemessages
RUN ./manage.py collectstatic --noinput

CMD uwsgi --master --http :8000 --module app.wsgi --workers 2 --threads 2 --harakiri 25 --max-requests 1000 --log-x-forwarded-for