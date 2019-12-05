from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from apps.comment.models import Comment



def user_is_comment_owner(f):
    def wrap(request, *args, **kwargs):
        comment = Comment.objects.get(id=kwargs['comment_id'])
        if request.user == comment.user:
            return f(request, *args, **kwargs)
        else:
            # raise PermissionDenied()
            response = HttpResponse("You don't have permission to delete comment")
            response.status_code = 403
            return response

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap
