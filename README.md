# Django Earthquake API

This project is an API built with Django, Django REST framework, and Python. It fetches earthquake data from the USGS API and caches it using Redis. The API also stores query data in a PostgreSQL database.

## Getting started

To get started, first clone the repository to your local machine:

```bash
git clone https://github.com/your_username/earthquake_challenge.git
```

Then, navigate to the project's root directory and install the dependencies using:

```bash
pip install -r requirements.txt
```

## Environment Variables

The project uses environment variables for configuration. You can set them by creating a .env file at the root of the project. Here are the available environment variables:

```plaintext
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://user:password@localhost/dbname
REDIS_URL=redis://:password@localhost:6379/0
USGS_API_URL=https://earthquake.usgs.gov/fdsnws/event/1/query.geojson
```

*IMPORTANT: Never use real secret keys in .env files. They are only meant to be helpful for development purposes.*

## Setting up the Database and Redis

To set up the database and Redis without installing PostgreSQL and Redis on your local machine, you can run them using:

```bash
docker-compose -f docker-compose-services-only.yml up -d
```

## Running the API in your local machine

Once the dependencies are installed and the environment variables are set, you can run the API in your local machine using:

```bash
python manage.py runserver
```

By running the API in your local machine you will be able to easily debug your code.

## Database Migrations

The project uses Django's built-in migrations for database migrations. To run the migrations, use:

```bash
python manage.py migrate
```

To migrate to the initial state of the database, run the following command:

```bash
python3 manage.py migrate earthquake_app zero
```

This will remove all migrations and reset the database to the initial state.

To revert a single migration, use the following command:

```bash
python3 manage.py migrate earthquake_app <migration_name>
```

Replace <migration_name> with the name of the migration you want to revert. For example, if you want to revert the migration named "0001_initial", the command would be:

```bash
python3 manage.py migrate earthquake_app 0001_initial

```

This will revert the migration and update the database schema to the previous state. Note that any data added or modified by the reverted migration will be lost.

## Running tests

To run the tests, use:

```bash
python manage.py test
```

## Docker

The project includes a docker-compose.yml file that allows for easy setup of a PostgreSQL database, Redis, and the API service. The following services are defined:

- db: The PostgreSQL database container
- redis: The Redis container
- api: The API service container

To use the docker-compose.yml file, ensure that Docker is installed and running on your machine. Then, in the root directory of the project, run the following command:

```bash
docker-compose up --force-recreate --build
```

This will build the API service container and start the three containers defined in the docker-compose.yml file.

## Testing the Services using Postman

To test the API services, we have provided a Postman collection. You can import this collection by following these steps:

Open Postman and click on the Import button in the top-left corner of the window.
Select the Import From Link option, and paste the following link: https://raw.githubusercontent.com/oteroleonardogh>/earthquake-challenge-api/main/postman-collection.json
Click the Import button, and the collection will be added to your Postman workspace.
Once you have imported the collection, you can test each of the API services by selecting the appropriate request from the collection and clicking the Send button. Make sure to replace any placeholders in the request URL or request body with your own values.

Note: If you are running the API locally, make sure to update the base URL in each request to http://localhost:8000.

## Conclusion

This project is built using the following libraries and frameworks:

- `Django`: Used as the web framework
- `Django REST framework`: Used to build RESTful API
- `psycopg2`: Used as the PostgreSQL driver
- `django-redis`: Used for Redis integration
- `requests`: Used for making HTTP requests to the USGS API

In addition, several devDependencies were used for testing, linting, and other development tasks.

In general, the decision-making for choosing these libraries and frameworks was based on the following criteria:

- Functionality: The library or framework should provide the necessary functionality for the task at hand, such as making HTTP requests, logging, or interacting with a database.
- Ease of use: The library or framework should be easy to use and have good documentation.
- Community support: The library or framework should have an active community with frequent updates and bug fixes.
- Performance: The library or framework should be performant and not introduce significant overhead or latency.

In conclusion, this project provides a boilerplate for building a RESTful API with Django, Django REST framework, and PostgreSQL. The project includes testing and Docker functionality to ensure that code quality is maintained and that the API can be easily deployed
