# Dockerfile with Peptide Matching Game Solution Explorer
# author: Micha Birklbauer
# version: 1.0.0

FROM python:3.10.4

LABEL maintainer="micha.birklbauer@gmail.com"

RUN mkdir app
COPY streamlit_app.py app
WORKDIR app
RUN mkdir img
COPY img/fhooe_logo.png img

CMD  ["streamlit", "run", "streamlit_app.py"]
