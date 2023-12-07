# syntax=docker/dockerfile:1
FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH "${PATH}:/root/.local/bin"
RUN echo "${PATH}" >> /etc/bash.bashrc
RUN apt-get update
RUN apt-get -y install pipx
RUN pipx install poetry
COPY ./ebu_tt_live ./testing ./pyproject.toml ./poetry.lock ./
RUN poetry install
CMD poetry run ebu-dummy-encoder
