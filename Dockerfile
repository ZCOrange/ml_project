FROM ubuntu:18.04
RUN apt-get update && apt-get install -y \ 
git \
curl \
ca-certificates \ 
python3 \ 
python3-pip \ 
sudo \
&& rm -rf /var/lib/apt/lists/*
RUN useradd -m bot001
RUN chown -R bot001:bot001 /home/bot001/ 
COPY --chown=bot001 *.* /home/bot001/app/ 
USER bot001
RUN cd /home/bot001/app/ && pip3 install -r requirements.txt
WORKDIR /home/bot001/app
CMD ["python", "your_script.py"]