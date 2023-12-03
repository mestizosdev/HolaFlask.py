from .ping.route import define_routers as ping_routers
from .version.route import define_routers as version_routers
from .security.route import define_routers as security_routers


def load_routers(api):
    ping_routers(api)
    version_routers(api)
    security_routers(api)
