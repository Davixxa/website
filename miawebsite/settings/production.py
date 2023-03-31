from .base import *

root = "/home/davix/davixxa.net/public"
STATIC_ROOT = os.path.join(root, "static")
MEDIA_ROOT = os.path.join(root, "media")
ALLOWED_HOSTS = ["*"]
SECRET_KEY = os.environ["SECRET_KEY"]


DEBUG = False

try:
    from .local import *
except ImportError:
    pass
