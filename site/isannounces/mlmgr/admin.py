from django.contrib import admin
from isannounces.mlmgr.models import MailingList, MailingListMessage

admin.site.register(MailingList)
admin.site.register(MailingListMessage)