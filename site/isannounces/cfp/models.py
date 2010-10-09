# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from django_countries import CountryField

# Conferences

class Sponsor(models.Model):
    """
    A professional or academic organisation running conferences (IEEE, AIS, ACM, ...).
    """
    name = models.CharField(max_length=250)
    acronym = models.CharField(max_length=20, blank=True)
    website = models.URLField(verify_exists=True, max_length=200, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = _('sponsor')
        verbose_name_plural = _('sponsors')
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Conference(models.Model):
    """
    A professional or academic conference held yearly. Can also be associated to another conference if organised in
    conjunction with it.
    """
    name = models.CharField(max_length=250)
    acronym = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    topic = models.TextField(blank=True)
    website = models.URLField(verify_exists=True, max_length=200, blank=True)
    sponsor = models.ForeignKey('Sponsor', blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True)

    class Meta:
        verbose_name = _('conference')
        verbose_name_plural = _('conferences')
        ordering = ['name']

    def __unicode__(self):
        return self.name

class ConferenceEdition(models.Model):
    """
    An annual edition of a Conference. Can also be associated to another conference edition if organised in
    conjunction with it.
    """
    name = models.CharField(max_length=250)
    acronym = models.CharField(max_length=20, blank=True)
    theme = models.CharField(max_length=500, blank=True)
    topics = models.TextField(blank=True)
    website = models.URLField(verify_exists=True, max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=250, blank=True)
    country = CountryField()
    parent = models.ForeignKey('self', blank=True, null=True)
    conference = models.ForeignKey('Conference')
    #TODO Add foreign keys for cities

    class Meta:
        verbose_name = _('edition')
        verbose_name_plural = _('editions')
        ordering = ['start_date']

    def __unicode__(self):
        return self.name

# Journals

class Journal(models.Model):
    """
    An academic journal title.
    """
    title = models.CharField(max_length=250)
    acronym = models.CharField(max_length=20, blank=True)
    website = models.URLField(verify_exists=True, max_length=200, blank=True)
    description = models.TextField(blank=True)
    basket = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('journal')
        verbose_name_plural = _('journals')
        ordering = ['title']

    def __unicode__(self):
        if self.acronym:
            return self.title + " (" + self.acronym + ")"
        else:
            return self.title

# Books

class BookPublisher(models.Model):
    """
    A professional or academic publisher.
    """
    name = models.CharField(max_length=250)
    acronym = models.CharField(max_length=20, blank=True)
    website = models.URLField(verify_exists=True, max_length=200, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = _('publisher')
        verbose_name_plural = _('publishers')
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Book(models.Model):
    """
    A book.
    """
    title = models.CharField(max_length=250)
    theme = models.CharField(max_length=500, blank=True)
    topics = models.TextField(blank=True)
    website = models.URLField(verify_exists=True, max_length=200, blank=True)
    description = models.TextField(blank=True)
    publisher = models.ForeignKey('BookPublisher')

    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')
        ordering = ['title']

    def __unicode__(self):
        return self.title

# Universities

class University(models.Model):
    """
    A university.
    """
    name = models.CharField(max_length=250)
    acronym = models.CharField(max_length=20, blank=True)
    website = models.URLField(verify_exists=True, max_length=200, blank=True)
    description = models.TextField(blank=True)
    city = models.CharField(max_length=250, blank=True)
    country = CountryField()
    #TODO Add foreign keys for cities

    class Meta:
        verbose_name = _('university')
        verbose_name_plural = _('universities')
        ordering = ['name']

    def __unicode__(self):
        return self.name

class UniversityDivision(models.Model):
    """
    A university division and it's faculty/school.
    """
    name = models.CharField(max_length=250)
    faculty = models.CharField(max_length=250)
    acronym = models.CharField(max_length=20, blank=True)
    website = models.URLField(verify_exists=True, max_length=200, blank=True)
    description = models.TextField(blank=True)
    university = models.ForeignKey('University')

    class Meta:
        verbose_name = _('division')
        verbose_name_plural = _('divisions')
        ordering = ['name']

    def __unicode__(self):
        return self.name

# Generic

class Call(models.Model):
    """
    A call for paper/position/... associated with a ConferenceEdition, Journal, UniversityDivision.
    """
    title = models.CharField(max_length=250)
    type = models.ForeignKey('CallType')
    content = models.TextField(blank=True)
    url = models.URLField(verify_exists=True, max_length=200, blank=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('call')
        verbose_name_plural = _('calls')

    def __unicode__(self):
        return self.title

class CallType(models.Model):
    """
    A type of call (paper, position, ...) associated with a Call.
    """
    name = models.CharField(max_length=100)
    content_type = models.ForeignKey(ContentType)

    class Meta:
        verbose_name = _('type of call')
        verbose_name_plural = _('types of calls')

    def __unicode__(self):
        return self.name

class Deadline(models.Model):
    """
    A date from a specific DeadlineType associated with a call.
    """
    call = models.ForeignKey('Call')
    type = models.ForeignKey('DeadlineType')
    date = models.DateField()
    extension = models.DateField(null=True,blank=True)
    mandatory = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('deadline')
        verbose_name_plural = _('deadlines')
        order_with_respect_to = 'call'
        get_latest_by = "date"

    def __unicode__(self):
        if self.extension:
            return self.extension + " - " + self.type + " (" + _("extended") + ")"
        else:
            return self.date + " - " + self.type

class DeadlineType(models.Model):
    """
    A type of deadline (submission, acceptation, ...) associated with a Deadline.
    """
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('type of deadline')
        verbose_name_plural = _('types of deadlines')
        ordering = ['name']

    def __unicode__(self):
        return self.name