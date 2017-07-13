# -*- coding: utf-8 -*-

"""
    Guided Tour, Controllers
"""
module = request.controller
resourcename = request.function

if not settings.has_module(module):
    raise HTTP(404, body="Module disabled: %s" % module)


# -----------------------------------------------------------------------------
def client():
    return s3_rest_controller()

# -----------------------------------------------------------------------------
def checklist():
    return s3_rest_controller()

# -----------------------------------------------------------------------------
def mobility():
    return s3_rest_controller()

# -----------------------------------------------------------------------------
def index():
    """
        Application Home page
    """

    #module_name = settings.modules[module].name_nice
    #response.title = module_name
    #return dict(module_name=module_name)

    return dict()

# -----------------------------------------------------------------------------
def askmsw():
    print "ask msw"
    mswdict = {"msw" : "Hallo Welt msw"}
    return mswdict