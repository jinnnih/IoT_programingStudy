# Media wiki 설치

## 1. docker 설치
```bash
sudo apt update -y && sudo apt full-upgrade -y
```
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```
```bash
sudo docker version
```
```bash
sudo usermod -aG docker pi
```
```bash
sudo reboot
```
## 2. Media wiki 설치

```bash
cd ~
```
```bash
mkdir mediawiki
cd mediawiki
```
```bash
touch docker-compose.yml
```
```yml

# MediaWiki with MariaDB
#
# Access via "http://localhost:8080"
#   (or "http://$(docker-machine ip):8080" if using docker-machine)
services:
  mediawiki:
    image: mediawiki
    restart: unless-stopped
    ports:
      - 8080:80
    links:
      - database
    volumes:
      - ./images:/var/www/html/images
      # After initial setup, download LocalSettings.php to the same directory as
      # this yaml and uncomment the following line and use compose to restart
      # the mediawiki service
      # - ./LocalSettings.php:/var/www/html/LocalSettings.php
  # This key also defines the name of the database host used during setup instead of the default "localhost"
  database:
    image: mariadb
    restart: unless-stopped
    environment:
      MYSQL_DATABASE: wikidb
      MYSQL_USER: wikiuser
      MYSQL_PASSWORD: wikipassword
      MYSQL_RANDOM_ROOT_PASSWORD: 'yes'
    volumes:
      - ./db:/var/lib/mysql
```
## 3. Media wiki 세팅

- LocalSettings.php 를 찾기


## 참고
[personal mediawiki with raspberry pi and docker]
https://peppe8o.com/personal-mediawiki-with-raspberry-pi-and-docker/
https://peppe8o.com/docker-raspberry-pi-portainer/



