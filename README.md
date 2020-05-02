# Genome Code Challenge

## Description

 Application that display the weather information for any given city made with Python's FastAPI framework inspired in Clean Architecture and DDD principles.

## Overview

This project is comprised of the following languages and libraries:

* Language: [Python 3.8+](https://www.python.org/)
* Package management: [Poetry](https://python-poetry.org/)
* Web framework: [FastAPI](https://fastapi.tiangolo.com/)
* Production web server: [Uvicorn](http://www.uvicorn.org/)
* Functional programming utilities: [Toolz](https://toolz.readthedocs.io/en/latest/)
* Data parsing and validation: [Pydantic](https://pydantic-docs.helpmanual.io/)
* Testing: [Pytest](https://docs.pytest.org/en/latest/)
* Linter: [Flake8](https://flake8.pycqa.org/en/latest/)
* Static type checker: [Mypy](https://mypy.readthedocs.io/en/stable/index.html)
* Formatter: [Black](https://github.com/psf/black)

Auxiliary libraries were omitted but can be found in the [pyproject](https://github.com/gustavorodarte/weather-api/blob/master/pyproject.toml) file.


## Running

* Start a container with: `docker-compose run --rm --service-ports app ash`
* Inside the container run: `poetry install`
* Start the web server with: `poetry run web_server`


## Testing

* Start a container with: `docker-compose run --rm --service-ports tests ash`
* Inside the container run: `poetry install`
* Test the API with: `pytest`


## Linting, static check and code style guide

* Run migrations with: `alembic upgrade head`
* Test the API with: `pytest`
* Check code style with: `black --check weather`
* Format code with: `black weather`
* Lint the code with: `flake8 weather tests`
* Run static analysis with: `mypy weather tests`


## Knowing Issues

* The Feature Test isn't passing fully, I had a problem to mock the lib request_async, so when running the feature test the request to Open Weather Map is made.

## To Improve

* The API should be capable to receive a geolocation and return the weather conditions, at the moment only city names are available.
* Cache the fetched weather data, unfortunately, I don't have time to implement the request cache, my original plan was implementing a Redis to cache the API data.
* Types: some functions and variables not has types.


