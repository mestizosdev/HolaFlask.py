from flaskr.ping.route import define_routers as ping_routers
from flaskr.version.route import define_routers as version_routers
from flaskr.security.route import define_routers as security_routers


def load_routers(api):
    ping_routers(api)
    version_routers(api)
    security_routers(api)
