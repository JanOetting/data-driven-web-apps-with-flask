from datetime import datetime
from typing import List

import sqlalchemy as sa
import sqlalchemy.orm as orm
from pypi_org.db.modelbase import SQLAlchemyBase
from pypi_org.db.releases import Release


class package(SQLAlchemyBase):
    __tablename__ = "packages"
    id = sa.Column(sa.String, primary_key=True)
    created_date = sa.Column(sa.DateTime, default=datetime.today,index=True)
    summary = sa.Column(sa.String,nullable=False)
    desc = sa.Column(sa.String,nullable=True)
    home_page = sa.Column(sa.String)
    docs_page = sa.Column(sa.String)
    packages_page = sa.Column(sa.String)
    author_name = sa.Column(sa.String)
    author_email = sa.Column(sa.String,index=True)

    licence = sa.Column(sa.String,index=True)

    # maintainers
    # releases
    releases:List[Release] =orm.relation("Release",order_by=[
        Release.major_ver.desc(),
        Release.minor_ver.desc(),
        Release.build_ver.desc()
     ],back_populates="package")



    def __repr__(self):
        return f"<package: {id}>"
