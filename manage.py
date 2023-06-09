#!/usr/bin/env python

# django-salesforce
#
# by Hyneck Cernoch and Phil Christensen
# See LICENSE.md for details
#

import os
import sys

# note that we're actually running the testrunner project, not the salesforce app.
os.environ['DJANGO_SETTINGS_MODULE'] = 'salesforce.testrunner.settings'

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
