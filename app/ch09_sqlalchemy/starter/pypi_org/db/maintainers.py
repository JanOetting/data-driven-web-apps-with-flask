import sqlalchemy
from pypi_org.db.modelbase import SQLAlchemyBase


class Maintainer(SQLAlchemyBase):
    __tablename__ = 'maintainers'

    user_id: int = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    package_id: str = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
