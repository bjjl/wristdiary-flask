#!/bin/sh
# Copyright (c) 2021 Benjamin Lorenz

curl \
    --header "Content-Type: application/json" \
    --data '{ "entry" : "Hello from prod!", "user_id" : "42" }' \
    https://lion.mx.plus/api/send
