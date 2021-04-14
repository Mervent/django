FROM python:3.7-slim-stretch

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

ENV STATIC_ROOT /static
ENV DATABASE_URL=sqlite://

RUN echo deb http://deb.debian.org/debian stretch contrib non-free > /etc/apt/sources.list.d/debian-contrib.list \
    && apt-get update \
    && apt-get --no-install-recommends install -y \
      tzdata \
      gettext \
      locales-all \
      build-essential \
      libxml2-dev \
      libxslt1-dev \
      libpq-dev \
      net-tools \
      curl \
      iputils-ping \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uwsgi poetry

WORKDIR /app

ADD pyproject.toml /app
ADD poetry.lock /app
RUN poetry config virtualenvs.create false && poetry install --no-dev

ADD ./src /app

RUN ./manage.py collectstatic --noinput

CMD uwsgi --master --http :8000 --module app.wsgi --workers 2 --threads 2 --harakiri 30 --max-requests 1000 --log-x-forwarded-for
