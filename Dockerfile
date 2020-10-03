FROM ubuntu:18.04

RUN apt-get update && apt-get install \
    -y --no-install-recommends python3 python3-virtualenv

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Run the application:
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /home/streamlit-openscale/
WORKDIR /home/streamlit-openscale

# Install dependencies:


ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

EXPOSE 8501
