# Django API

This is a simple django API base project

# Techs
- Django
- Dajngo restframework
- Postgres

# Useful commands

- Run project: `docker-compose up`
- Generate secret key: `chmod +x ./generate_secret.sh && ./generate_secret.sh`
- Create messages: `docker-compose run api python manage.py makemessages -a`
- Compile messages: `docker-compose run api python manage.py compilemessages`
