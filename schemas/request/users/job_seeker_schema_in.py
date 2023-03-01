from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models.enums.contact_method_enum import ContactMethods
from models.enums.user_roles_enum import JobSeekerRoles


class JobSeekerSchemaIn(Schema):
    preferred_contact_method = EnumField(ContactMethods,
                                         error_messages={'by_name': "Invalid method"})

    roles = fields.List(
        EnumField(JobSeekerRoles,
                  error_messages={'by_name': "Invalid role"}))
