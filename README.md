# Django-Redis-Bhavcopy-Task

1. Install redis server with following command
# sudo apt-get install redis-server

2. Install python3.6 along with the environment
# apt-get update \
# && apt-get install -y software-properties-common curl \
# && add-apt-repository ppa:deadsnakes/ppa \
# && apt-get update \
# && apt-get install -y python3.6 python3.6-venv

3. create python3.6 virtualenv
# python3 -m venv env_name

4. Install following packages in environment
# pip install django djangorestframework redis request

5. Change the directory to django_redis and run migrate command
# cd django-redis
# python manage.py migrate

6. Access the page at following url
# http://127.0.0.1:8000/api

7. Following is the command to be added to crontab in order to download bhav copy from bse website, unzip it and and store it into the database. All these functionality is written in the utils.py files inside api app

#*  18  *   *   *   /home/sourabh/redis_demo/env_redis/bin/python3.6 /home/sourabh/redis_demo/django_redis/api/utils.py 

# NOTE-> Change the environment and utils.py file path according to your system path

