#!/bin/sh
# Copyright (c) 2021 Benjamin Lorenz

curl \
    --header "Content-Type: application/json" \
    --data '{ "entry" : "dskjh%//$%", "user_id" : "14", "is_encrypted" : "true" }' \
    http://chaos.lorenz.place/api/send
