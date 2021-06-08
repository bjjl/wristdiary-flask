#!/bin/sh
# $Id$
# Copyright (c) 2021 pocketservices GmbH

curl -G \
    --header "Content-Type: application/json" \
    -d user_id=14 \
    http://chaos.lorenz.place/api/receive
