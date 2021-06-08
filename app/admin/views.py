# $Id$
# Copyright (c) 2021 pocketservices GmbH

from flask import render_template
from . import admin


@admin.route('/status', methods=['GET'])
def status():
    return
