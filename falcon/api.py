"""Falcon API class."""


import re
import six


class API(object):
    """
    This class is the main entry point into a Falcon-based app.
    """
    
    
    
    _STREAM_BLOCK_SIZE = 8 * 1024  # 8 KiB
    
    
    __slots__ = ('_request_type', '_response_type',
                 '_error_handlers', '_media_type', '_sinks', 
                 '_independent_middleware', 
                 '_static_routes')
    
    def __init__(self, media_type=None, 
                request_type=None, response_type=None,
                middleware=None, router=None,
                independent_middleware=False):
        
        self._sinks = []
        self._media_type = media_type
        self._static_routes = []

        # set middleware
        self._independent_middleware = independent_middleware

        self._request_type = request_type
        self._response_type = response_type

        self._error_handlers = []

        # NOTE(kgriffs): Add default error handlers
        
    def __call__(self, env, start_response):  # noqa: C901
        """
        WSGI `app` method.
        Makes instances of API callable from a WSGI server. May be used to
        host an API or called directly in order to simulate requests when
        testing the API.
        (See also: PEP 3333)
        Args:
            env (dict): A WSGI environment dictionary
            start_response (callable): A WSGI helper function for setting
                status and headers on a response.
        """
        
        resource = None
        params = {}
        
        dependent_mw_resp_stack = []
        
        req_succeeded = False
        
        print(env, start_response)