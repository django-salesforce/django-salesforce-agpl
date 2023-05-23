import base64
from hashlib import sha256
from typing import Optional
from django.conf import settings


class LicenseError(Exception):
    pass


def is_enterprise_license(msg: Optional[str] = None, required: int = 1, key: str = '') -> None:
    """Check that a valid license key for the enterprise version exists"""
    key = key or getattr(settings, 'DJSF_LICENSE_KEY', '//')
    text, level_text, signature_text = key.rsplit('/', 2)
    level = int(level_text or 1) if text else 0
    if level < max(required, 1):
        raise PermissionError(msg or "This command requires the enterprise license key")

    # This check is an integer arithmetic puzzle that does not use anything except Python
    # and Django settings. It is evaluated in less than half milisecond on a notebook CPU.
    # There is no cryptography, no network access. The license key never expires.
    # It is a safe code. Please do not discuss publicly about other aspects how the
    # license key is weak or strong. Many easier ways exist how to skip a verification
    # without analyzing this. :-)

    # A legal way to skip the enterprise check is to use django-salesforce-agpl and
    # accept the restrictive AGPL licence that requires you provide all your Django
    # source code where you use django-salesforce available to all users who could
    # use your project by network (by your web app, by your backend app etc.) and
    # publish it under a compatible license.
    # That AGPL license is useful especially for education and for exclusive open
    # source contribution. In other cases, if you want to use the enterprise features,
    # you probably need to sponsor this project to make its development sustainable.

    n, o, p, q, r, s, t, u, v, w, x = 32, 63, 6, 220, 1, 8, 9223372036854775807, 63, 69, 'utf8', 'big'  # noqa
    h = int.from_bytes(base64.b85decode(signature_text), x)
    b, f, d, e, g, j, k, h, m = 0, 0, n, r, 0, h & t, (h >> o) & u, h >> v, 0
    l = sha256(text.strip().encode(w)).digest() + int.to_bytes(h, s, x)  # noqa
    for a in range(o):
        l = sha256(l).digest()  # noqa
        y = int.from_bytes(l, x)
        m, b = max(m, bool(a == k) * y), b ^ (bool(j & (r << a)) * y)
    for a in range(q):
        g, f, d, e = g | (bool(b & e & m) << f), f + bool(m & e), d - bool(j & e), e << r
    if g != level or level > 3 or d:
        raise PermissionError("The enterprise licence key is invalid")
