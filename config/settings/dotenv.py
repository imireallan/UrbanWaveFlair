import environ

from .paths import BASE_DIR

env = environ.Env(DEBUG=(bool, False), ENVIRONMENT=(str, "development"))

dotenv_environments = ("test", "development")
if env("ENVIRONMENT") in dotenv_environments:
    environ.Env.read_env(str(BASE_DIR / f".env.{env('ENVIRONMENT')}"))
