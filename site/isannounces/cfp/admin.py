from isannounces.cfp.models import Sponsor, Conference, ConferenceEdition, Journal, University, UniversityDivision, Call, CallType, Deadline, DeadlineType
from django.contrib import admin

admin.site.register(Sponsor)
admin.site.register(Conference)
admin.site.register(ConferenceEdition)
admin.site.register(Journal)
admin.site.register(University)
admin.site.register(UniversityDivision)
admin.site.register(Call)
admin.site.register(CallType)
admin.site.register(Deadline)
admin.site.register(DeadlineType)