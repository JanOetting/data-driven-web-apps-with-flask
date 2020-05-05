import os

from pypi_org.data import db_session
from pypi_org.data.package import Package
from pypi_org.data.releases import Release


def insert_a_package():
    p=Package()
    p.id=input("Package ID/Name:").strip().lower()
    p.summary=input("Summary: ").strip()
    p.license=input("Licence").strip()
    p.author_name=input("Author name").strip()
    print("Release 1")
    r=Release()
    r.major_ver=int(input("Major Version"))
    r.minor_ver=int(input("Minor Version"))
    r.build_ver=int(input("Build"))
    r.size=int(input("Size:"))
    p.releases.append(r)

    print("Release 2")
    r = Release()
    r.major_ver = int(input("Major Version"))
    r.minor_ver = int(input("Minor Version"))
    r.build_ver = int(input("Build"))
    r.size = int(input("Size:"))
    p.releases.append(r)

    session=db_session.create_session()

    session.add(p)

    session.commit()

def main():
    setup_db()
    while True:
        insert_a_package()

def setup_db():
    db_file = os.path.join(
        os.path.dirname(__file__),
        "..",'db',
        'pypi.sqlite')


    db_session.global_init(db_file)

if __name__ == '__main__':
    main()