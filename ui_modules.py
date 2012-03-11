import tornado.web

class ItemModule(tornado.web.UIModule):
    def render(self, item, display_detail=False, item_states = None):
        return self.render_string("modules/item.html", 
                                  item=item, 
                                  display_detail=display_detail,
                                  item_states=item_states)
