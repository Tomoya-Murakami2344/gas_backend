# FROM python:3.11

# RUN apt-get update && \
# apt-get install -y --no-install-recommends unzip && \
# rm -rf /var/lib/apt/lists/*

# # Japanese Localization
# RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# # Google Chromeの最新安定版をインストール
# RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
# dpkg -i google-chrome-stable_current_amd64.deb; apt-get update; apt-get -fy install
# # RUN chmod +x /usr/bin/google-chrome
# RUN google-chrome --version

# # Chromedriverをインストール
# # 今回は「123.0.6312.122」を使用
# RUN wget https://storage.googleapis.com/chrome-for-testing-public/123.0.6312.122/linux64/chromedriver-linux64.zip
# RUN wget https://storage.googleapis.com/chrome-for-testing-public/124.0.6367.60/linux64/chromedriver-linux64.zip
# RUN unzip chromedriver-linux64.zip
# RUN mv chromedriver-linux64/chromedriver /usr/bin/chromedriver
# RUN chown root:root /usr/bin/chromedriver
# RUN chmod +x /usr/bin/chromedriver

# # python package
# RUN pip install selenium && \
# pip install bs4 && \
# pip install oauth2client

# COPY requirements.txt .
# RUN pip install -r requirements.txt 

# ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/chrome

FROM selenium/standalone-chrome-debug:3

USER root
RUN apt-get update \
 && apt-get install -y -q --no-install-recommends \
    fonts-noto-cjk fonts-noto-cjk-extra language-selector-common language-pack-ja \
 && update-locale LANG=ja_JP.UTF-8 \
 && apt-get clean \
 && rm -r /var/lib/apt/lists/*

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

RUN apt-get update && apt install -y python3-pip

COPY requirements.txt /requirements.txt    
RUN pip install -r /requirements.txt

USER 1200

RUN x11vnc -storepasswd password ${HOME}/.vnc/passwd
RUN cd /app