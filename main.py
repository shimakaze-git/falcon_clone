#!/usr/bin/env python
# -*- coding:utf-8 *-
import json

import falcon
import hooks
import middleware

@falcon.before(hooks.before_resource)
@falcon.after(hooks.after_resource)
class AppResource(object):
    
    def on_get(self, req, resp):
        
        params = req.params

        msg = {
            "message": "Welcome to the Falcon",
            "params": params
        }
        resp.body = json.dumps(msg)

app = falcon.API(
    middleware=[
        middleware.ExampleMiddleware(),
        middleware.ExampleMiddlewareTwo(),
    ]
)
app.add_route("/", AppResource())
app.add_route("/test", AppResource())

if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 8000, app)
    httpd.serve_forever()