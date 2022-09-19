from enum import Enum


class RoleEnum(str, Enum):
    SUPERADMIN_ROLE = 'SUPERADMIN_ROLE'
    ADMIN_ROLE = 'ADMIN_ROLE'
    USER_ROLE = 'USER_ROLE'
