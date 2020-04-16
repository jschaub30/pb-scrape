FROM ubuntu

RUN mkdir /code
WORKDIR /code

ADD geckodriver-v0.26.0-linux64.tar.gz /code/
RUN mv geckodriver /usr/local/bin
RUN apt-get update
RUN apt-get -y install bash python3-pip firefox

ADD code/ /code/
RUN pip3 install -r requirements.txt
CMD bash -c "python3 -u pb.py"
