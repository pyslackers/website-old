# website

Welcome to the PySlacker's community website. We are a community of [Python](https://python.org) programming enthusiasts, please [Join Us!](http://pythondevelopers.herokuapp.com).

## Development

Install the dependencies, this is often a one time task (but run it whenever they are updated):

    pip install -r requirements.txt

Set the application environment variables (check `website/config.py` for others you may need):

    export FLASK_APP=website/__main__.py
    export FLASK_DEBUG=1
    export PY_ENV=dev

Run the app in development mode:

    flask run

## Testing

    python -m pytest

## Style

    flake8

## Commands to be aware of:

    flask --help
    
    # Info
    flask routes
