
import os.path
from tornado.options import define
from modules import ItemModule


define("port", default=8888, help="run on the given port", type=int)

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    ui_modules={"Item": ItemModule},
    autoescape=None,
    debug=True,
)