DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'test',
        'PASSWORD': 'test',
        'HOST': 'localhost',
        'PORT': '3306',
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
