from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, Float, String, Date, Enum, Boolean, DateTime
from sqlalchemy.orm import relationship

from api.config.db_config import Base
from api.enums.role_enum import RoleEnum
from api.enums.status_enum import StatusEnum


class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, nullable=False, primary_key=True)
    username = Column(String(30), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    role = Column(
        Enum(RoleEnum),
        nullable=False,
        default=RoleEnum.USER_ROLE
    )
    status = Column(
        Enum(StatusEnum),
        nullable=False,
        default=StatusEnum.PENDING_STATUS
    )
    google = Column(
        Boolean,
        nullable=False,
        default=False
    )
    register_date = Column(
        DateTime,
        nullable=False,
        default=datetime.now()
    )