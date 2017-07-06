FROM python:3.6

RUN useradd --home-dir /home/carrot carrot
ENV HOME=/home/carrot
WORKDIR $HOME
RUN chown carrot:carrot $HOME
RUN pip3 install virtualenv

RUN python3 -m venv .venv
RUN ./.venv/bin/pip install jupyter
ENV LAST_MODIFIED 2017.06.16.001
COPY ./run.sh /srv/run.sh
RUN cd $HOME
