# -*- coding: utf-8 -*-
from flaskr.ping.route import define_routes as ping_routes
from flaskr.version.route import define_routes as version_routes


def load_routes(api):
    ping_routes(api)
    version_routes(api)
