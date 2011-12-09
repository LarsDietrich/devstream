from sqlalchemy import *
from migrate import *
from migrate.changeset import create_column, drop_column

from devstream.libs.database import metadata
from devstream.models import User


def upgrade(migrate_engine):
    metadata.bind = migrate_engine
    create_column(User.__table__.c.username)


def downgrade(migrate_engine):
    metadata.bind = migrate_engine
    drop_column(User.__table__.c.username)
