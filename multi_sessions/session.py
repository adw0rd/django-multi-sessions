# coding: utf-8
from django.conf import settings
from django.contrib.sessions.backends.base import SessionBase, CreateError
from django.utils.encoding import force_unicode
from django.utils.importlib import import_module


class SessionStore(SessionBase):
    """Multiple backends for your sessions!
    Designed for moving sessions from one session engine to another, without stopping the current sessions.
    It consistently passes backends in the list (settings.SESSION_MULTISESSIONS_POOL) and depending on the modes of doing the necessary.
    """
    def __init__(self, session_key=None):
        super(SessionStore, self).__init__(session_key)
        self.pool_backends = settings.SESSION_MULTISESSIONS_POOL

    def load(self):
        for backend in self.pool_backends:
            engine = import_module(backend['backend'])
            session = engine.SessionStore(self.session_key)
            if session.exists(self.session_key):
                session_data = session.load()
                return session_data
            else:
                # Try another backend
                continue
        # If the session is not exists, then create it
        self.create()
        return {}

    def exists(self, session_key):
        for backend in self.pool_backends:
            try:
                engine = import_module(backend['backend'])
                return engine.SessionStore(session_key).exists(session_key)
            except:
                # Try another backend
                continue
        return False

    def create(self):
        while True:
            self.session_key = self._get_new_session_key()
            try:
                # Save immediately to ensure we have a unique entry in the
                # database.
                self.save(must_create=True)
            except CreateError:
                # Key wasn't unique. Try again.
                continue
            self.modified = True
            self._session_cache = {}
            return

    def save(self, *a, **kw):
        backends = self._get_backends(modes=("write",))
        for backend in backends:
            try:
                engine = import_module(backend['backend'])
                session = engine.SessionStore(self.session_key)
                if hasattr(self, '_session_cache'):
                    if not hasattr(session, '_session_cache'):
                        session._session_cache = {}
                    session._session_cache.update(self._session_cache)
                session.save(*a, **kw)
            except:
                # Try another backend
                continue

    def delete(self, session_key=None):
        if session_key is None:
            if self._session_key is None:
                return
            session_key = self._session_key
        backends = self._get_backends(modes=("write", "delete"))
        for backend in backends:
            try:
                engine = import_module(backend['backend'])
                session = engine.SessionStore(session_key)
                session.delete()
            except:
                # Try another backend
                continue

    def _get_backends(self, modes=tuple()):
        """Return available backends by modes
        @return list
        """
        if not modes:
            return list(self.pool_backends)
        else:
            backends = []
            for b in self.pool_backends:
                if any(map(lambda m: m in b['modes'], modes)):
                    backends.append(b)
            return backends
