from datetime import time, timedelta
from typing import List
from pydantic import BaseModel


# main class User
class User(BaseModel):
    user_id: int
    user_username: str
    td: timedelta = None

    # automatic show data
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


# main class Article
class Access(BaseModel):
    access_panel_online_show: bool
    access_panel_data_management: bool
    access_panel_consumer_management: bool
    access_panel_center_management: bool
    access_panel_control_stations: bool
    access_panel_user_management: bool
    access_panel_reporting: bool
    access_panel_connection: bool
    access_panel_setting: bool

    # automatic show data
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


# input data
class UserBase(BaseModel):
    user_username: str
    user_name_surname: str
    user_password: str
    user_national_code: str
    user_presence: time
    user_is_admin: bool


# input data
class AccessBase(BaseModel):
    access_panel_online_show: bool
    access_panel_data_management: bool
    access_panel_consumer_management: bool
    access_panel_center_management: bool
    access_panel_control_stations: bool
    access_panel_user_management: bool
    access_panel_reporting: bool
    access_panel_connection: bool
    access_panel_setting: bool

    user_id: int


# Show data
class UserDisplay(BaseModel):
    user_username: str
    user_name_surname: str
    user_password: str
    user_national_code: str
    user_presence: time
    user_is_admin: bool

    items: List[Access]

    # automatic show data
    class Config:
        from_attributes = True


# Show data
class AccessDisplay(BaseModel):
    access_panel_online_show: bool
    access_panel_data_management: bool
    access_panel_consumer_management: bool
    access_panel_center_management: bool
    access_panel_control_stations: bool
    access_panel_user_management: bool
    access_panel_reporting: bool
    access_panel_connection: bool
    access_panel_setting: bool

    user: User

    # automatic show data
    class Config:
        from_attributes = True
