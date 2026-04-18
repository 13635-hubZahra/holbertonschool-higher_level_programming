#!/bin/bash
URL=$1
curl -s -o /dev/null -w "%{size_download}\n" "$URL"
