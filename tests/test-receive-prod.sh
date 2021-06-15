#!/bin/sh
# Copyright (c) 2021 Benjamin Lorenz

curl -G \
    --header "Content-Type: application/json" \
    -d user_id=42 \
    https://lion.mx.plus/api/receive
