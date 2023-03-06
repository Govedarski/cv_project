from managers.auth_manager import auth
from models.enums.user_roles_enum import AdminRoles


def admin_access_granted(func):
    def wrapper(class_instance, *args, **kwargs):
        current_user = auth.current_user()
        if not getattr(current_user, "roles", None):
            return func(class_instance, *args, **kwargs)

        if class_instance.is_admins_allowed() \
                and any(role
                        for role in current_user.roles
                        if role in AdminRoles.__members__.values()):
            return current_user

        return func(class_instance, *args, **kwargs)

    return wrapper

