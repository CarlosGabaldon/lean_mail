from handlers import HomeHandler
from handlers import ItemHandler

handlers = [
    (r"/", HomeHandler),
    (r"/item/(.*)", ItemHandler)
]