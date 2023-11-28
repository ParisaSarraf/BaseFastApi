from sqlalchemy.orm.session import Session

from database.models import DbAccess
from Schema.schemas import AccessBase

from fastapi.exceptions import HTTPException
from fastapi import status


def create_access(db: Session, request: AccessBase):
    access = DbAccess(
        access_panel_online_show=request.access_panel_online_show,
        access_panel_data_management=request.access_panel_data_management,
        access_panel_consumer_management=request.access_panel_consumer_management,
        access_panel_center_management=request.access_panel_center_management,
        access_panel_control_stations=request.access_panel_control_stations,
        access_panel_user_management=request.access_panel_user_management,
        access_panel_reporting=request.access_panel_reporting,
        access_panel_connection=request.access_panel_connection,
        access_panel_setting=request.access_panel_setting,

        user_id=request.user_id
    )
    db.add(access)
    db.commit()
    db.refresh(access)
    return access


def read_all_access(db: Session):
    return db.query(DbAccess).all()


def raed_a_access(id_art, db: Session):
    access = db.query(DbAccess).filter(DbAccess.access_id == id_art).first()

    if not access:
        # raise for calling an exception
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Article with id {id_art} is not found !")
    else:
        return access


def delete_a_access(id_art, db: Session):
    article = raed_a_access(id_art, db)
    db.delete(article)
    db.commit()
    return 'ok'


def update_an_access(id_art, db: Session, request: AccessBase):
    article = db.query(DbAccess).filter(DbAccess.access_id == id_art)

    article.update({
        DbAccess.access_panel_online_show: request.access_panel_online_show,
        DbAccess.access_panel_data_management: request.access_panel_data_management,
        DbAccess.access_panel_consumer_management: request.access_panel_consumer_management,
        DbAccess.access_panel_center_management: request.access_panel_center_management,
        DbAccess.access_panel_control_stations: request.access_panel_control_stations,
        DbAccess.access_panel_user_management: request.access_panel_user_management,
        DbAccess.access_panel_reporting: request.access_panel_reporting,
        DbAccess.access_panel_connection: request.access_panel_connection,
        DbAccess.access_panel_setting: request.access_panel_setting
    })
    db.commit()
    return 'ok'
