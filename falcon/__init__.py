"""
Primary package for Falcon, the minimalist WSGI library.
Falcon is a minimalist WSGI library for building speedy web APIs and app
backends. The `falcon` package can be used to directly access most of
the framework's classes, functions, and variables::
    import falcon
    app = falcon.API()
"""

# Hoist classes and functions into the falcon namespace
from falcon.api import API