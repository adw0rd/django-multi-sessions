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

1\. Download the archive and run ``python setup.py install`` or ``pip install django-multi-sessions``

2\. Set ``multi_sessions.session`` as your session engine, like so:

<pre><code>SESSION_ENGINE = "multi_sessions.session"
</code></pre>

3\. Example settings:

<pre><code>SESSION_MULTISESSIONS_POOL = (
        {"backend": "redis_sessions.session", "modes": ["read", "write"]},
        {"backend": "django.contrib.sessions.backends.db", "modes": ["read", "delete"]},
    )
</code></pre>

4\. Available modes:

* "read"   - Allows launch "load" method;
* "write"  - Allows launch "save" and "create" method;
* "delete" - Allows launch the "delete" method.
