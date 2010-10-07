# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from isannounces.cfp.models import Call

class MailingList(models.Model):
    """
    A mailing list.
    """
    name = models.CharField(max_length=250)
    acronym = models.CharField(max_length=20, blank=True)
    topic = models.TextField(blank=True)
    website = models.URLField(verify_exists=True, max_length=200, blank=True)

    class Meta:
        verbose_name = _('mailing list')
        verbose_name_plural = _('mailing lists')
        ordering = ['name']

    def __unicode__(self):
        return self.name

class MailingListMessage(models.Model):
    """
    A message received from a given MailingList.
    """
    subject = models.CharField(max_length=250)
    sender = models.CharField(max_length=250, blank=True)
    headers = models.TextField(blank=True)
    message = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    exim_message_id = models.CharField(max_length=250)
    call = models.ForeignKey(Call)
    mailing_list = models.ForeignKey('MailingList')

    class Meta:
        verbose_name = _('message')
        verbose_name_plural = _('messages')
        ordering = ['-timestamp']

    def __unicode__(self):
        return "[%s] %s"% (self.mailing_list.acronym, self.subject)