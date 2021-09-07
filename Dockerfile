
FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y software-properties-common

# avoid being asked options when installing
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y texlive texlive-lang-cjk texlive-science texlive-fonts-recommended texlive-fonts-extra xdvik-ja gv nkf
RUN apt-get install -y make gcc imagemagick
RUN apt-get install -y latexmk

WORKDIR /workdir
CMD make