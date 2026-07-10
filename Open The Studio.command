#!/bin/bash
# Double-click to open The Studio — the pixel map of the creative-strategy vault.
cd "$(dirname "$0")"
PORT=4173
if ! curl -s -o /dev/null "http://localhost:$PORT/api/state"; then
  echo "Lighting the beacons… (starting the studio server)"
  nohup node .studio/server.js >> .studio/server.log 2>&1 &
  for i in $(seq 1 20); do
    sleep 0.3
    curl -s -o /dev/null "http://localhost:$PORT/api/state" && break
  done
fi
open "http://localhost:$PORT"
echo "The Studio is open → http://localhost:$PORT"
