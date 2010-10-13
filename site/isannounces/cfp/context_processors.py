# Context processor(s) for our application

def media_url(request):
    # Add medial_url in the templates context
    from django.conf import settings
    return {'media_url': settings.MEDIA_URL}