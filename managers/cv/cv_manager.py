from managers.cv.awards_and_achievements_manager import AwardsAndAchievementsManager
from managers.cv.certificate_manager import CertificateManager
from managers.cv.education_manager import EducationManager
from managers.cv.reference_manager import ReferenceManager
from managers.cv.requirement_manager import RequirementManager
from managers.cv.work_exp_manager import WorkExpManager
from managers.helpers.decorators import handle_unique_constrain_violation
from managers.helpers.manager_mixins import CreateManagerMixin, GetListManagerMixin
from models.cv.cv_model import CVModel


class CVManager(CreateManagerMixin, GetListManagerMixin):
    MODEL = CVModel

    @classmethod
    @handle_unique_constrain_violation
    def create(cls, data, user):
        reference_ids = data.get("reference_ids") and data.pop("reference_ids") or []
        aaa_ids = data.get("aaa_ids") and data.pop("aaa_ids") or []
        education_ids = data.get("education_ids") and data.pop("education_ids") or []
        work_exp_ids = data.get("work_exp_ids") and data.pop("work_exp_ids") or []
        certificate_ids = data.get("certificate_ids") and data.pop("certificate_ids") or []
        requirement_ids = data.get("requirement_ids") and data.pop("requirement_ids") or []
        instance = super().create(data, user)
        def add_to_cv(cv, manager, ids):
            for _id in ids:
                instance = manager().get(_id=_id)
                name = manager.__name__.replace("Manager", "")
                if instance and not instance.owner_id == user.id:
                    raise Exception(f"You can't add {name} that don't belong to you")
                if instance:
                    cv.append(instance)

        add_to_cv(instance.references, ReferenceManager, reference_ids)
        add_to_cv(instance.awards_and_achievements, AwardsAndAchievementsManager, aaa_ids)
        add_to_cv(instance.education, EducationManager, education_ids)
        add_to_cv(instance.work_exps, WorkExpManager, work_exp_ids)
        add_to_cv(instance.certificates, CertificateManager, certificate_ids)
        add_to_cv(instance.requirements, RequirementManager, requirement_ids)

        return instance
