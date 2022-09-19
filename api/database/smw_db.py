from sqlalchemy import create_engine, orm

from api.config.db_config import Base
from api.config.settings import settings



class SaveMyWalletDB:
    def __init__(self, _engine=None, _session=None) -> None:
        self.__engine = _engine
        self.__session = _session

    @property
    def engine(self):
        if self.__engine is None:
            self.__engine = create_engine(settings.DB_CONN_URL)
        return self.__engine

    @property
    def session(self):
        if self.__session is None:
            Session = orm.sessionmaker(bind=self.engine)
            self.__session = Session()
        return self.__session

    def generate_tables(self):
        try:
            Base.metadata.create_all(self.engine)
        except Exception as ex:
            raise ex

smw_db = SaveMyWalletDB()