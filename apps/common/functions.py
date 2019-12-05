from django.contrib.humanize.templatetags import humanize


def human_readable_time(datetime_object):
	if not datetime_object:
		return
	return humanize.naturaltime(datetime_object)


def is_user_authenticated(request):
	if request.user.is_anonymous and not hasattr(request.user,'id'):
		return False
	if not request.user.is_authenticated:
		return False
	return True







