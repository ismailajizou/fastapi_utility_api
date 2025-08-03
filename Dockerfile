FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

# Create public directory for storing downloaded files
RUN mkdir -p /code/public

EXPOSE 80

WORKDIR /code

# If running behind a proxy like Nginx or Traefik add --proxy-headers
CMD ["fastapi", "run", "app/main.py", "--port", "80", "--proxy-headers"]