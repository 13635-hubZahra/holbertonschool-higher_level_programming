#!/bin/bash
# Bu skript URL-in body olcusunu baytla gosterir
curl -s "$1" | wc -c
