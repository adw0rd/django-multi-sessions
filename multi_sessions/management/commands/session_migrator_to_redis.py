import pytz
import datetime

from optparse import make_option
from redis_sessions import session as redis_session

from django.utils.encoding import force_unicode
from django.core.management.base import BaseCommand
from django.contrib.sessions.backends import db as db_session
from django.conf import settings


class Command(BaseCommand):
    help = """Movement sessions from django.contrib.sessions.backends.db to redis_sessions.session"""

    option_list = BaseCommand.option_list + (
        make_option('-l', '--limit',
            dest='limit',
            type="int",
            default=100,
            help='Limit of sessions in chunk (chunk size)'),
        )

    def handle(self, **options):
        limit = options.get('limit', 100)
        now = pytz.timezone(settings.TIME_ZONE).localize(datetime.datetime.now())
        chunk_number = 0

        print "Limit of sessions in chunk: {0}".format(limit)

        while True:
            success_moved_conter = 0
            sessions = db_session.Session.objects.all()[0:limit]

            if not sessions:
                print "Queue is empty!"
                break
            else:
                print "New chunk: #{0}".format(chunk_number)

            for session in sessions:
                if session.expire_date > now:
                    s = redis_session.SessionStore(session.session_key)
                    if not s.exists(session.session_key):
                        s._session_cache = {}
                        s._session_cache.update(s.decode(force_unicode(session.session_data)))
                        max_expiry_datetime = now + datetime.timedelta(seconds=settings.SESSION_COOKIE_AGE)
                        if session.expire_date > max_expiry_datetime:
                            session_expire_date = max_expiry_datetime
                        else:
                            session_expire_date = session.expire_date
                        s.set_expiry(session_expire_date)
                        s.save()
                        success_moved_conter += 1
                session.delete()

            print "> Moved to Redis: {0} of {1}".format(success_moved_conter, len(sessions))
            chunk_number += 1
