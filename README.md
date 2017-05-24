# website

Welcome to the PySlacker's community website. We are a community of [Python](https://python.org) programming enthusiasts, please [Join Us!](http://pythondevelopers.herokuapp.com).

## Development

Install the dependencies, this is often a one time task (but run it whenever they are updated):

    pip install -r requirements.txt

Make sure you have some sort of postgres running (you can customize the url with `DATABASE_URL`):

    docker-compose up -d psql

Set the application environment variables:

    export FLASK_APP=website/__main__.py
    export FLASK_DEBUG=1
    export PY_ENV=dev

Make sure your database is up-to-date:

    flask db upgrade

Run the app in development mode:

    flask run

## Testing

    python -m pytest

## Style

    flake8

## Commands to be aware of:

    flask --help

    # Database
    flask db migrate -m "Auto create a new migration with this as a message"
    flask db upgrade

    # Info
    flask routes
