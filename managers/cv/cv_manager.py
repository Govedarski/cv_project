from managers.cv.awards_and_achievements_manager import AwardsAndAchievementsManager
from managers.cv.certificate_manager import CertificateManager
from managers.cv.education_manager import EducationManager
from managers.cv.reference_manager import ReferenceManager
from managers.cv.requirement_manager import RequirementManager
from managers.cv.work_exp_manager import WorkExpManager
from managers.helpers.decorators import handle_unique_constrain_violation
from managers.helpers.manager_mixins import CreateManagerMixin, GetListManagerMixin, GetManagerMixin, EditManagerMixin, \
    DeleteManagerMixin
from models.cv.cv_model import CVModel


class CVManager(GetManagerMixin, CreateManagerMixin, GetListManagerMixin, EditManagerMixin, DeleteManagerMixin):
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

    def edit(self, data, _id, remove_images=False, **kwargs):
        # TODO: check if resource belongs to user
        instance = self._get_instance(_id)

        reference_ids = data.get("reference_ids") and data.pop("reference_ids") or []
        aaa_ids = data.get("aaa_ids") and data.pop("aaa_ids") or []
        education_ids = data.get("education_ids") and data.pop("education_ids") or []
        work_exp_ids = data.get("work_exp_ids") and data.pop("work_exp_ids") or []
        certificate_ids = data.get("certificate_ids") and data.pop("certificate_ids") or []
        requirement_ids = data.get("requirement_ids") and data.pop("requirement_ids") or []

        self.get_model().query.filter_by(id=instance.id).update(data)

        def replace_in_cv(cv, manager, ids):
            if isinstance(cv, list):
                cv.clear()
            for resource_id in ids:
                resource = manager().get(_id=resource_id)
                if instance:
                    cv.append(resource)

        replace_in_cv(instance.references, ReferenceManager, reference_ids)
        replace_in_cv(instance.awards_and_achievements, AwardsAndAchievementsManager, aaa_ids)
        replace_in_cv(instance.education, EducationManager, education_ids)
        replace_in_cv(instance.work_exps, WorkExpManager, work_exp_ids)
        replace_in_cv(instance.certificates, CertificateManager, certificate_ids)
        replace_in_cv(instance.requirements, RequirementManager, requirement_ids)

        return instance

    def delete(self, _id):
        # TODO delete files from cloud
        instance = self._get_instance(_id)
        instance.work_exps.clear()
        instance.references.clear()
        instance.education.clear()
        instance.awards_and_achievements.clear()
        instance.certificates.clear()
        instance.requirements = None

        self.get_model().query.filter_by(id=instance.id).delete()
