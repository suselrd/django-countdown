from datetime import datetime
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts  import render_to_response
from django.template import RequestContext
from countdown.utils import difference_data


class CountdownMiddleware(object):

    def process_request(self, request):
        request.countdown_target = settings.COUNTDOWN_TARGET_DATE
        if (
                settings.COUNTDOWN_TARGET_DATE > datetime.now()
                and getattr(settings, 'COUNTDOWN_RESTRICT_ACCESS', False)
                and not request.user.is_authenticated()
        ):
            allowed_urls = getattr(settings, 'COUNTDOWN_ALLOWED_URLS', list())
            allowed_urls.append('admin:index')  # Allow to login in admin
            allow = False
            for url in allowed_urls:
                if request.path_info.startswith(reverse(url)):
                    allow = True
                    break
            if not allow:
                return render_to_response(
                    "countdown/countdown.html",
                    difference_data(request.countdown_target - datetime.now()),
                    context_instance=RequestContext(request)
                )