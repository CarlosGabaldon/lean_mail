import tornado.web

class ItemModule(tornado.web.UIModule):
    def render(self, item):
        return self.render_string("modules/item.html", item=item)
