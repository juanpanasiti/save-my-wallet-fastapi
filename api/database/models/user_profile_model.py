from datetime import datetime
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean

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
        DateTime,
        nullable=False,
        default=datetime.now()
    )
    last_update = Column(
        DateTime,
        nullable=False,
        default=datetime.now()
    )

    # Relation
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('UserModel', backref=backref('user_profile', uselist=False))

    def to_json(self):
        return {
            'id': self.id,
            'is_deleted': self.is_deleted,
            'img_url': self.img_url,
            'next_payment_date': self.next_payment_date,
            'last_update': self.last_update,
        }