from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os

config = context.config
fileConfig(config.config_file_name)

# Load DB URL from env
config.set_main_option('sqlalchemy.url', os.getenv('DATABASE_URL'))

from app.database import Base
target_metadata = Base.metadata

def run_migrations_offline():
    ...

def run_migrations_online():
    ...
