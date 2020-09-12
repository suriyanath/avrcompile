FROM ubuntu:20.04
COPY . /avrcompile
RUN apt update && apt install --no-install-recommends python3 python3-pip -y nocache && rm -rf /var/lib/apt/lists/*
RUN pip3 install flask --compile --no-cache-dir
CMD cd /avrcompile/ && ./Run.sh
