import tornado.ioloop
import tornado.web

def make_app():
    return tornado.web.Application([
        (r"/*", tornado.web.RedirectHandler, 
        {'url': 'https://annie.sornars.com'}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
