# -*- coding: utf-8 -*-
import django.dispatch
from django.db import connections
from background_task.settings import app_settings
from django.dispatch import Signal, receiver
from .models import UpdatedTask

task_created = django.dispatch.Signal(['task'])
task_error = django.dispatch.Signal(['task'])
task_rescheduled = django.dispatch.Signal(['task'])
task_failed = django.dispatch.Signal(['task_id', 'completed_task'])
task_successful = django.dispatch.Signal(['task_id', 'completed_task'])
task_started = django.dispatch.Signal()
task_finished = django.dispatch.Signal()


# Register an event to reset saved queries when a Task is started.
def reset_queries(**kwargs):
    if app_settings.BACKGROUND_TASK_RUN_ASYNC:
        for conn in connections.all():
            conn.queries_log.clear()


task_started.connect(reset_queries)


# Register an event to reset transaction state and close connections past
# their lifetime.
def close_old_connections(**kwargs):
    if app_settings.BACKGROUND_TASK_RUN_ASYNC:
        for conn in connections.all():
            conn.close_if_unusable_or_obsolete()


task_started.connect(close_old_connections)
task_finished.connect(close_old_connections)


@receiver(task_rescheduled)
def register_new_task(sender, task, **kwargs):
    # TODO: Here I shoud register a new task
    queue = task.queue
    UpdatedTask.objects.create_or_updated(queue=queue, defaults={"was_updated": True})
