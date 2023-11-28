from fastapi import HTTPException


def is_admin(current_user):
    if not current_user:
        raise HTTPException(status_code=404, detail='User not found')

    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail='You do not have the required access')
    return get_user_access(current_user)


def get_user_access(current_user):
    if not current_user:
        raise HTTPException(status_code=404, detail='User not found')
    access = {}
    if current_user.is_admin:
        access = {
            'access_level': 'admin',
            'permissions': ['read', 'write', 'delete']
        }
    else:
        access = {
            'access_level': 'user',
            'permissions': ['read']
        }

    return access

