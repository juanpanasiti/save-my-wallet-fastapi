from datetime import datetime
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.sqltypes import Integer, String, Date, Boolean

from api.config.db_config import Base


class UserProfileModel(Base):
    __tablename__ = 'user_profile'

    id = Column(Integer, nullable=False, primary_key=True)
    is_deleted = Column(
        Boolean,
        nullable=False,
        default=False
    )
    img_url = Column(
        String(255),
        nullable=False,
        default=''
    )
    next_payment_date = Column(
        Date,
        nullable=False,
        default=datetime.timestamp
    )
    last_update = Column(
        Date,
        nullable=False,
        default=datetime.timestamp
    )

    # Relation
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('UserModel', backref=backref('user_profile', uselist=False))