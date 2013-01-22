django-multi-sessions
=======================
Multiple backends for your sessions!

.. image:: https://secure.travis-ci.org/adw0rd/django-multi-sessions.png
    :target: http://travis-ci.org/adw0rd/django-multi-sessions

Designed for moving sessions from one session engine to another, without stopping the current sessions. It consistently passes backends in the list (settings.SESSION_MULTISESSIONS_POOL) and depending on the modes of doing the necessary.

For more information see:

* http://adw0rd.com/2012/django-multi-sessions/en/ - article about it in English
* http://adw0rd.com/2012/django-multi-sessions/ru/ - article about it in Russian
* http://pypi.python.org/pypi/django-multi-sessions - the PyPI page
* https://github.com/adw0rd/django-multi-sessions - the GitHub repository

------------
Installation
------------

1\. Download the archive and run ``python setup.py install`` or ``pip install django-multi-sessions``

2\. Set ``multi_sessions.session`` as your session engine, like so::

        SESSION_ENGINE = "multi_sessions.session"

3\. Example settings::

        SESSION_MULTISESSIONS_POOL = (
            {"backend": "redis_sessions.session", "modes": ["read", "write"]},
            {"backend": "django.contrib.sessions.backends.db", "modes": ["read", "delete"]},
        )


4\. Available modes:

* "read"   - Allows launch "load" method;
* "write"  - Allows launch "save" and "create" method;
* "delete" - Allows launch the "delete" method.
