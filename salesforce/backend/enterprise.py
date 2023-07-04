# django-salesforce
#
# by Hyneck Cernoch and Phil Christensen
# See LICENSE.md for details
#

from typing import Optional


def check_enterprise_license(msg: Optional[str] = None, required: int = 1, key: str = '') -> None:
    """Check that a valid license key for the enterprise version exists"""
    # An Enterprise license key is NOT NECESSARY if you meet the conditions of AGPL license.

    # A legal way to skip the enterprise check is to use django-salesforce-agpl
    # <https://github.com/django-salesforce/django-salesforce-agpl>
    # and accept the restrictive AGPL licence that requires you provide all your Django
    # source code where you use django-salesforce available to all users who could
    # use your project by network (by your web app, by your backend app etc.) and
    # publish it under a compatible license.
    # That AGPL license is useful especially for education and for exclusive open
    # source contribution. In other cases, if you want to use the enterprise features,
    # you probably need to sponsor this project to make its development sustainable.

    return


def check_license_in_latest_django() -> None:
    check_enterprise_license()
