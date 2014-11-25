# coding=utf-8


def difference_data(td):
    return {
        'countdown_sec': td.seconds % 60,
        'countdown_min': (td.seconds / 60) % 60,
        'countdown_hour': td.seconds / (60*60) % 24,
        'countdown_day': td.days,
    }
