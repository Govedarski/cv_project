from managers.auth_manager import auth
from models.enums.user_roles_enum import AdminRoles


def admin_access_granted(func):
    def wrapper(instance, *args, **kwargs):
        current_user = auth.current_user()
        if not getattr(current_user, "roles", None):
            return func(instance, *args, **kwargs)

        if instance.is_admins_allowed() \
                and any(role
                        for role in current_user.roles
                        if role in AdminRoles.__members__.values()):
            return current_user

        return func(instance, *args, **kwargs)

    return wrapper

