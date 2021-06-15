#
# Copyright (c) 2021 Benjamin Lorenz
#

from flask import render_template
from . import admin


@admin.route('/status', methods=['GET'])
def status():
    return
