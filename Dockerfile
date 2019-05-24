# our base image

ARG base_docker_file_hash
ARG requirements_hash
ARG week_number

FROM reg.inplatlabs.ru/megafon_mock/base-${week_number}-${base_docker_file_hash}-${requirements_hash}:latest

COPY . /usr/src/app/
WORKDIR /usr/src/app/


# run the application
RUN mkfifo named.pipe
ENTRYPOINT python3 megafon_mock.py --with-docker-file < named.pipe
