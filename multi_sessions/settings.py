DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

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
