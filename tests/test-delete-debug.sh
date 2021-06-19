#!/bin/sh
# Copyright (c) 2021 Benjamin Lorenz

curl -X DELETE -G \
     -d user_id=14 \
     http://chaos.lorenz.place/api/delete/60c5bb13f2d8f5cbbd949de9
