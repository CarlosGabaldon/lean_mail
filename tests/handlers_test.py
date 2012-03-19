from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application
from tornado.options import options
import tornado.database
import urls
import config

class TestHomeHandler(AsyncHTTPTestCase):
    def get_app(self):
            app = Application(urls.handlers, **config.settings)
            app.db = tornado.database.Connection(
                host=options.mysql_host, database=options.mysql_database,
                user=options.mysql_user, password=options.mysql_password)
            return app

    def test_get(self):
            response = self.fetch('/')
            self.assertIn("<h1>Kanban Mail</h1>", response.body)

