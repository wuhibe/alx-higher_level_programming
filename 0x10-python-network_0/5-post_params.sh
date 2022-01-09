#!/bin/bash
# POST AND SEND DATA
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
