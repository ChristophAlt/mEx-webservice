FROM ubuntu:18.04

RUN apt-get -y update && \
    apt-get install -y python-dev python3-dev python3-pip git zlib1g-dev\
                       apt-transport-https ca-certificates wget build-essential\
                       libcurl4-openssl-dev g++ htop nano parallel curl locales\
                       daemontools unzip python3-distutils && \
    apt-get clean

RUN pip3 install --upgrade pip setuptools dumb-init ipython

# Ensure that we always use UTF-8 and with US English locale
RUN locale-gen en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV PYTHONIOENCODING utf-8

#Add non-root user to run app
RUN useradd -G users -m runner

WORKDIR /mnt/
#Argument to rebuild from this point after an update
ARG COMMIT_SHA1=1
ARG GITHUB_ACCESS_TOKEN
ARG SPACY_LANG=de

RUN pip3 install -vv --process-dependency-links --upgrade git+https://$GITHUB_ACCESS_TOKEN:@github.com/ChristophAlt/macss-webservice
RUN python3 -m spacy download $SPACY_LANG

#Run model tests
#RUN pytest -vs

EXPOSE 5050
EXPOSE 5051

#Default configuration
ENV PORT 5050
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]

CMD ["bash" ,"-c", "python3 -m macss_webservice.run $PORT"]
