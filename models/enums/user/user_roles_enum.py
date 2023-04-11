from enum import Enum


class JobSeekerRoles(Enum):
    talent = "Talent"


class EmployerRoles(Enum):
    ceo = "CEO"
    recruiter = "Recruiter"


class AdminRoles(Enum):
    admin = "Admin"
    super_admin = "Super Admin"
