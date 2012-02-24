django-multi-sessions
=======================
Multiple backends for your sessions!
Designed for moving sessions from one session engine to another, without stopping the current sessions. It consistently passes backends in the list (settings.SESSION_MULTISESSIONS_POOL) and depending on the modes of doing the necessary.

------------
Installation
------------

1. Download the gzipped tarball and run ``python setup.py install``,

2. Set ``multi_sessions.session`` as your session engine, like so::

       SESSION_ENGINE = 'multi_sessions.session'
		
3. Example settings::
    SESSION_ENGINE = "multi_sessions.session"
    SESSION_MULTISESSIONS_POOL = (
        {
            "backend": "redis_sessions.session",
            "modes": ["read", "write"],
        },
        {
            "backend": "django.contrib.sessions.backends.db",
            "modes": ["read", "delete"],
        },
    )

4. Available modes::
    * read -> Allows launch "load" method;
    * write -> Allows launch "save" and "create" method;
    * delete -> Allows launch the "delete" method.

