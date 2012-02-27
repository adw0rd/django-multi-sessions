import unittest
import time
from nose.tools import eq_
from django.utils.importlib import import_module
from session import SessionStore as MultiSession


class TestMultiSessions(unittest.TestCase):

    def setUp(self):
        self.multi_session = MultiSession()

    def test_modify_and_keys(self):
        eq_(self.multi_session.modified, False)
        self.multi_session.create()
        self.multi_session['test'] = 'test_me'
        eq_(self.multi_session.modified, True)
        eq_(self.multi_session['test'], 'test_me')

    def test_save_and_delete(self):
        self.multi_session['key'] = 'value'
        self.multi_session.save()
        self.multi_session.exists(self.multi_session.session_key)
        eq_(self.multi_session.exists(self.multi_session.session_key), True)
        self.multi_session.delete(self.multi_session.session_key)
        eq_(self.multi_session.exists(self.multi_session.session_key), False)

    def test_flush(self):
        self.multi_session['key'] = 'another_value'
        self.multi_session.save()
        key = self.multi_session.session_key
        self.multi_session.flush()
        eq_(self.multi_session.exists(key), False)

    def test_items(self):
        self.multi_session['item1'], self.multi_session['item2'] = 1, 2
        self.multi_session.save()
        eq_(self.multi_session.items(), [('item2', 2), ('item1', 1)])

    def test_expiry(self):
        self.multi_session.set_expiry(1)
        eq_(self.multi_session.get_expiry_age(), 1)
        self.multi_session['key'] = 'expiring_value'
        self.multi_session.save()
        key = self.multi_session.session_key
        eq_(self.multi_session.exists(key), True)
        time.sleep(2)
        eq_(self.multi_session.exists(key), False)

    def test_save_and_load(self):
        self.multi_session.set_expiry(60)
        self.multi_session.setdefault('item_test', 777)
        self.multi_session.save()
        session_data = self.multi_session.load()
        eq_(session_data.get('item_test'), 777)
            
    def test_multiple_backends_separately(self):
        # Check the backend if more than two
        if len(self.multi_session.pool_backends) < 2:
            return None
        self.multi_session.create()
        session_key = self.multi_session.session_key
        for backend in self.multi_session.pool_backends:
            engine = import_module(backend['backend'])
            session = engine.SessionStore(session_key)
            if "write" not in backend["modes"]:
                eq_(session.exists(session_key), False)
            if "write" in backend["modes"]:
                eq_(session.exists(session_key), True)
            if "delete" in backend["modes"] and session.exists(session_key) is True:
                session.delete(session_key)
                eq_(session.exists(session_key), False)


if __name__ == '__main__':
    import os
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    unittest.main()

# To run the test suite
# pip install nose
# python tests.py -v
