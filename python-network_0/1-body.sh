#!/bin/bash
# salamm
curl -sL -w "%{http_code}" "$1" -o /tmp/body_out | grep -q "200" && cat /tmp/body_out
