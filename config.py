
import os.path
from tornado.options import define
from modules import ItemModule


define("port", default=8888, help="run on the given port", type=int)

db_host = "localhost"
db_user = "root"
db_name = "lean_mail"
db_password = ""

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    ui_modules={"Item": ItemModule},
    autoescape=None,
    debug=True,
)