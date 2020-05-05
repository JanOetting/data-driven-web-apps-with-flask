from pathlib import Path

import sqlalchemy as sa
import sqlalchemy.orm as orm

from pypi_org.db.modelbase import SQLAlchemyBase

factory=None

def global_init(db_file:Path):
    global factory
    if factory:
        return
    if not db_file or not db_file:
        raise Exception("you must specifiy db file")

    conn_str='sqlite:///'+db_file.name
    engine=sa.create_engine(conn_str,echo=False)
    factory=orm.sessionmaker(bind=engine)

    import pypi_org.db.all_models
    SQLAlchemyBase.metadata.create_all(engine)