#!/bin/sh
# Copyright (c) 2021 Benjamin Lorenz

curl -G \
    --header "Content-Type: application/json" \
    -d user_id=14 \
    -d day=13 \
    -d month=6 \
    http://chaos.lorenz.place/api/receive
