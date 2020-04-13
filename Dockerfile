FROM ubuntu:18.04

RUN apt-get update && apt-get install \
    -y --no-install-recommends python3 python3-virtualenv

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Run the application:
COPY . /home/streamlit-openscale/
WORKDIR /home/streamlit-openscale

# Install dependencies:
RUN pip install -r requirements.txt

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

EXPOSE 8501
CMD [ "streamlit run", "src/test.py" ]
#CMD ['sleep', '5000']
