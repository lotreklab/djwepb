import hashlib
from django.utils.encoding import force_bytes

def make_image_key(*args):
    md5_hash = hashlib.md5(force_bytes(':'.join(str(arg) for arg in args)))
    return "ltk_webp_compressor:%s" % md5_hash.hexdigest()