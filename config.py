
import os.path
from tornado.options import define
from ui_modules import ItemModule


define("port", default=8888, help="run on the given port", type=int)
define("mysql_host", default="localhost", help="database host")
define("mysql_database", default="lean_mail", help="database name")
define("mysql_user", default="root", help="database user")
define("mysql_password", default="", help="database password")


settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    ui_modules={"Item": ItemModule},
    autoescape=None,
    debug=True,
)