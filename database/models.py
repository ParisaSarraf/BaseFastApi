from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Sequence, DateTime
from sqlalchemy.orm import relationship

from database.db import my_base


class DbUser(my_base):
    # table name
    __tablename__ = 'users'

    # columns
    user_id = Column(Integer, Sequence("users_id_seq", start=1), primary_key=True, autoincrement=True)

    user_username = Column(String(31), unique=True)
    user_name_surname = Column(String(63))
    user_password = Column(String(63))
    user_national_code = Column(String(10))
    user_presence = Column(DateTime)

    user_is_admin = Column(Boolean)

    # relationship('name other class',back_populates='name column relationship in other class')
    items = relationship('DbAccess', back_populates='user')


class DbAccess(my_base):
    # table name
    __tablename__ = 'access'

    # columns
    access_id = Column(Integer, primary_key=True, autoincrement=True, )
    access_panel_online_show = Column(Boolean)
    access_panel_data_management = Column(Boolean)
    access_panel_consumer_management = Column(Boolean)
    access_panel_center_management = Column(Boolean)
    access_panel_control_stations = Column(Boolean)
    access_panel_user_management = Column(Boolean)
    access_panel_reporting = Column(Boolean)
    access_panel_connection = Column(Boolean)
    access_panel_setting = Column(Boolean)

    # ForeignKey('name other table.name column')
    user_id = Column(Integer, ForeignKey('users.user_id'))
    # relationship('name other class',back_populates='name column relationship in other class')
    user = relationship('DbUser', back_populates='items')
