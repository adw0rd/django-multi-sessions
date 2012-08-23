django-multi-sessions
=======================
Multiple backends for your sessions!

Designed for moving sessions from one session engine to another, without stopping the current sessions. It consistently passes backends in the list (settings.SESSION_MULTISESSIONS_POOL) and depending on the modes of doing the necessary.

For more information see:

* http://pypi.python.org/pypi/django-multi-sessions
* http://adw0rd.com/2012/django-multi-sessions/en/

------------
Installation
------------

#. Download the archive and run ``python setup.py install`` or ``pip install django-multi-sessions``

#. Set ``multi_sessions.session`` as your session engine, like so:

       SESSION_ENGINE = "multi_sessions.session"

#. Example settings:

<pre><code>
    SESSION_MULTISESSIONS_POOL = (
        {"backend": "redis_sessions.session", "modes": ["read", "write"]},
        {"backend": "django.contrib.sessions.backends.db", "modes": ["read", "delete"]},
    )
</code></pre>

#. Available modes:

* "read"   - Allows launch "load" method;
* "write"  - Allows launch "save" and "create" method;
* "delete" - Allows launch the "delete" method.
