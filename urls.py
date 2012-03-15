from handlers import HomeHandler
from handlers import ItemHandler
from handlers import EmailHandler

handlers = [
    (r"/", HomeHandler),
    (r"/item/(.*)", ItemHandler),
    (r"/email/", EmailHandler)
]