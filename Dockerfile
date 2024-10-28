FROM ubuntu:24.04
RUN pip install -r smart_home/requirements.txt
RUN python smart_home/manage.py makemigrations && python smart_home/manage.py migrate && python smart_home/manage.py runserver
WORKDIR /src
COPY . .
CMD ["sudo", "docker", "run", "-d", "-p", "4444:80", "-v", "$(pwd)/src:/usr/share/nginx/html", "nginx", "--host", "0.0.0.0", "--port", "4444"]
