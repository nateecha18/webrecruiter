from django.contrib import admin
from jobapply.models import CandidateHistoryEducation, CandidateComputerSkill, CandidateLanguageSkill, CandidateCertExperience, CandidateWorkExperience, CandidateAttachment, CandidateBasic, EducationLevel,Institute,Country,Skill,SkillType,ExtraSkill

admin.site.register(CandidateHistoryEducation)
admin.site.register(CandidateComputerSkill)
admin.site.register(CandidateLanguageSkill)
admin.site.register(CandidateCertExperience)
admin.site.register(CandidateWorkExperience)
admin.site.register(CandidateAttachment)
admin.site.register(CandidateBasic)
admin.site.register(EducationLevel)
admin.site.register(Institute)
admin.site.register(Country)
admin.site.register(Skill)
admin.site.register(SkillType)
admin.site.register(ExtraSkill)
