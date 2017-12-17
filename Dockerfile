# Docker file for world-dev-indicators
# Simran Sethi, Dec. 2017

# use rocker/tidyverse as the base image and
FROM rocker/tidyverse

# then install the ezknitr packages
RUN Rscript -e "install.packages('ezknitr', repos = 'https://mran.revolutionanalytics.com/snapshot/2017-12-11')"

WORKDIR /usr/src/world-dev-indicators

# get python package dependencies
RUN apt-get install -y python3-tk
RUN apt-get install -y python-setuptools python-dev build-essential
RUN easy_install pip
RUN pip install --upgrade virtualenv


# install python 3
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# install python packages
 RUN pip3 install numpy
 RUN apt-get update && \
    pip3 install matplotlib && \
    pip3 install sqlite3 && \
    pip3 install pandas && \
    pip3 install os && \
    pip3 install warnings && \
    pip3 install glob && \
    pip3 install csv && \
    pip3 install warnings && \
    rm -rf /var/lib/apt/lists/*