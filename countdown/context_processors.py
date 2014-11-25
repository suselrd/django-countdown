# coding=utf-8
from datetime import datetime
from .utils import difference_data


def target_date_diff_data(request):
    if hasattr(request, 'countdown_target'):
        return difference_data(request.countdown_target - datetime.now())
    else:
        return {}
