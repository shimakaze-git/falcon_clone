import falcon

class ExampleMiddleware(object):
    
    def process_request(self, req, resp):
        print('ExampleMiddleware() process_request')
        print(req)
        print(resp)
        
    def process_resource(self, req, resp, resource, param):
        print('ExampleMiddleware() process_resource')
        print(req)
        print(resp)
        print(resource)
        print(param)

    def process_response(self, req, resp, resource):
        print('ExampleMiddleware() process_response')
        print(req)
        print(resp)
        print(resource)
        
class ExampleMiddlewareTwo(object):
    
    def process_request(self, req, resp):
        print('ExampleMiddlewareTwo() process_request')
        print(req, resp)
        
    def process_response(self, req, resp, resource):
        print('ExampleMiddlewareTwo() process_response')
        print(req, resp, resource)