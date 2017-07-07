FROM python:3.6

RUN useradd --home-dir /home/carrot carrot
ENV HOME=/home/carrot
WORKDIR $HOME
RUN chown carrot:carrot $HOME
RUN pip3 install virtualenv

RUN python3 -m venv .venv
COPY ./notebook_requirements.txt $HOME/notebook_requirements.txt
RUN $HOME/.venv/bin/pip install jupyter
RUN $HOME/.venv/bin/pip install -r notebook_requirements.txt

COPY ./run.sh $HOME/run.sh
