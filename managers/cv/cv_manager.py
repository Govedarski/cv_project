from managers.cv.awards_and_achievements_manager import AwardsAndAchievementsManager
from managers.cv.certificate_manager import CertificateManager
from managers.cv.education_manager import EducationManager
from managers.cv.reference_manager import ReferenceManager
from managers.cv.requirement_manager import RequirementManager
from managers.cv.work_exp_manager import WorkExpManager
from managers.helpers.decorators import handle_unique_constrain_violation
from managers.helpers.manager_mixins import CreateManagerMixin
from models.cv.cv_model import CVModel


class CVManager(CreateManagerMixin):
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

        # TODO: Refactor this to a function
        for reference_id in reference_ids:
            reference = ReferenceManager().get(_id=reference_id)
            if reference and not reference.owner_id == user.id:
                raise Exception("You can't add a reference that doesn't belong to you")
            if reference:
                instance.references.append(reference)

        for aaa_id in aaa_ids:
            awards_and_achievements = AwardsAndAchievementsManager().get(_id=aaa_id)
            if awards_and_achievements and not awards_and_achievements.owner_id == user.id:
                raise Exception("You can't add awards and achievements that don't belong to you")
            if awards_and_achievements:
                instance.awards_and_achievements.append(awards_and_achievements)

        for education_id in education_ids:
            education = EducationManager().get(_id=education_id)
            if education and not education.owner_id == user.id:
                raise Exception("You can't add education that doesn't belong to you")
            if education:
                instance.education.append(education)

        for work_exp_id in work_exp_ids:
            work_exp = WorkExpManager().get(_id=work_exp_id)
            if work_exp_id and not work_exp.owner_id == user.id:
                raise Exception("You can't add work experience that doesn't belong to you")
            if work_exp:
                instance.work_exps.append(work_exp)

        for certificate_id in certificate_ids:
            certificate = CertificateManager().get(_id=certificate_id)
            if certificate and not certificate.owner_id == user.id:
                raise Exception("You can't add certificates that don't belong to you")
            if certificate:
                instance.certificates.append(certificate)

        for requirement_id in requirement_ids:
            requirement = RequirementManager().get(_id=requirement_id)
            if requirement and not requirement.owner_id == user.id:
                raise Exception("You can't add requirements that don't belong to you")
            if requirement:
                instance.requirements.append(requirement)

        # Create a function that will replace the for loops above
        # def add_to_relationship(relationship, manager, ids):
        #     for id in ids:
        #         instance = manager.get(_id=id)
        #         if instance and not instance.owner_id == user.id:
        #             raise Exception("You can't add {} that don't belong to you".format(relationship))
        #         instance.relationship.append(instance)

        # add_to_relationship("references", ReferenceManager, reference_ids)
        # add_to_relationship("awards and achievements", AwardsAndAchievementsManager, aaa_ids)
        # add_to_relationship("education", EducationManager, education_ids)
        # add_to_relationship("work experience", WorkExpManager, work_exp_ids)
        # add_to_relationship("certificates", CertificateManager, certificate_ids)
        # add_to_relationship("requirements", RequirementManager, requirement_ids)



        return instance
