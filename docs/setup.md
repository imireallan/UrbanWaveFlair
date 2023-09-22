# Developer Setup

This repository consists of a Python Django application, running in Python `3.11.0`. We recommend installing Python and version managing with [asdf](https://asdf-vm.com/).

Package management is managed with `pipenv` - if you do not already have this installed, you can run `pip install pipenv` to grab the latest version. `pipenv` manages Python packages through virtual environments.

## Bootstrapping Dev Env

The first step is to create a virtual environment using `pipenv`. You can do this by calling `pipenv shell --python {semantic version}`. This will enter you into a fresh virtual environment. You may need to `pip install pipenv` again when entering, as it's used by later processes.

We have provided an easy-to-use script for setting-up your dev environment for this repo, all packages and applications are managed with `pipenv` and `docker`, meaning it will not impact any other repositories or versions you have downloaded.

The script is run by calling: `./scripts/bootstrap.sh`. This will setup environment variables, install the Python dependencies, init `pre-commit`, run the PosgreSQL database, perform migrations, install a super-user, then shut it all down.

The super user is accessible under the username `tdi-dev` and password `dev`.

### FAQ

- `psycopg2` fails to install: You do not have a postgresql client installed on your OS. You will need to install one to install this client library.

## Environment Variables Configuration

The environment variables are configured with `.env.{environment}` files, which are generated from the provided `.env.example` in the repository. `.env.test` is checked-in for use by the CI. When running in production, `.env.{environment}` files are ignored completely.

This setup allows for different variables when running `pytest` to the development server, should you want to do that, but in most cases they will be the same file. If you want to re-create these files from the `.env.example`, run `./scripts/bootstrap.sh` again.

## Running The Application in Debug

### Running Services

This command will block your terminal, so you'll need to run it in a different tab.

The application requires a PostgreSQL database to run locally, which can be run with the command `./scripts/run-services.sh`. The database is provided using `docker compose`, so you must ensure you have `docker` installed and running. It listens on port `5432`, the username is `postgres` and the password is `pass`. Local dev details are not required to be secure.

### Running Django Server

Running the application itself in debug locally can be done by executing `./scripts/run-app.sh`, which runs the application using the local Django development server.

### FAQ

- **`docker compose` is not recognized**: You may have an old version of docker, before `compose` was merged into the project. Replace all `docker compose` commands with `docker-compose`.
- **`docker is not running`**: When on Mac OS, Docker Desktop is used to start the docker engine. Run the desktop app (you can close it afterwards) to start the docker engine.
- **How do I reset my database?**: The database files are provided using docker volumes. You can clear the volume using the command `docker compose down -v `, but you will need to run `./scripts/bootstrap.sh` again to run migrations, or instead `python manage.py migrate`.