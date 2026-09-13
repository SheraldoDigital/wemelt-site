#!/usr/bin/env bash
#
# Serve the WeMelt landing page for local review — on this Mac and on any
# device sharing the same Wi-Fi.
#
#   ./serve.sh          # port 8900
#   ./serve.sh 3000     # any other port
#
# Stop it with Ctrl-C. Nothing is built or changed; this only serves the files.

set -euo pipefail

PORT="${1:-8900}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/wemelt-landing"

if [ ! -f "$ROOT/index.html" ]; then
  echo "error: $ROOT/index.html not found" >&2
  exit 1
fi

# First non-loopback IPv4 on an active interface (Wi-Fi is usually en0)
LAN_IP=""
for i in $(ifconfig -l); do
  ip="$(ipconfig getifaddr "$i" 2>/dev/null || true)"
  if [ -n "$ip" ]; then LAN_IP="$ip"; break; fi
done

# Free the port if a previous run is still holding it
if lsof -nP -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
  echo "port $PORT is in use — stopping the previous server"
  lsof -nP -tiTCP:"$PORT" -sTCP:LISTEN | xargs kill 2>/dev/null || true
  sleep 1
fi

# Delegates to scripts/dev-server.py, which is the stdlib server plus
# Cache-Control: no-store — so a phone never shows a stale stylesheet mid-review.
# It binds 0.0.0.0 (localhost + LAN) and serves threaded, which matters with
# ~40 assets per page load.
exec python3 "$(dirname "${BASH_SOURCE[0]}")/scripts/dev-server.py" "$PORT" --dir "$ROOT"
