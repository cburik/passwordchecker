from pytest import fixture

from pwned_password_checker.install import create_database
from pwned_password_checker.utils import create_engine, remove_file

TMP_DB_LOC = "./tmp_database.db"


@fixture
def engine_with_empty_database():
    engine = create_engine(f"sqlite:///{TMP_DB_LOC}")
    create_database(engine)
    yield engine
    remove_file(TMP_DB_LOC)
