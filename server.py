import tornado.ioloop
import tornado.web


class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>BUPT</h1>")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/",Handler),
    ])
    app.listen(80)
    tornado.ioloop.IOLoop.instance().start()