from celery import shared_task
from time import sleep


@shared_task
def sleepy_sum(duration):
    sleep(duration)
    print('HIIIIIIIII')
    return None
