#!/usr/bin/env python3
"""
Local review server for the WeMelt landing page.

Same as `python3 -m http.server`, with one change that matters when you are
reviewing on several devices at once: every response carries `Cache-Control:
no-store`.

Without it, Python sends only `Last-Modified` and no `Cache-Control`, so browsers
fall back to *heuristic* caching — they invent their own freshness window. iOS
Safari is especially eager here, and will keep showing a stale stylesheet after a
change with no obvious way to force a refresh on a phone. `no-store` removes the
guesswork: every reload is the current file.

This is for local review only. Production caching on Vercel is the opposite —
long max-age with hashed filenames.

    python3 scripts/dev-server.py [port] [--dir DIR]
"""
import argparse
import functools
import http.server
import os
import socket
import socketserver
import sys


class NoStoreHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, fmt, *args):
        # one compact line per request; skip the noisy 304/200 duplication
        sys.stderr.write("  %s %s\n" % (self.address_string(), fmt % args))


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


def lan_ip():
    """Best-guess LAN address, without depending on any one interface name."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("192.0.2.1", 1))          # TEST-NET-1, never actually routed
        return s.getsockname()[0]
    except OSError:
        return None
    finally:
        s.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("port", nargs="?", type=int, default=8900)
    ap.add_argument("--dir", default=None)
    args = ap.parse_args()

    root = args.dir or os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "wemelt-landing")
    if not os.path.isfile(os.path.join(root, "index.html")):
        sys.exit(f"error: no index.html in {root}")

    handler = functools.partial(NoStoreHandler, directory=root)

    print()
    print("  WeMelt — Landing Page")
    print(f"  serving {root}")
    print()
    print(f"  On this Mac      http://localhost:{args.port}")
    ip = lan_ip()
    if ip:
        print(f"  Phone / tablet   http://{ip}:{args.port}      (same Wi-Fi)")
    else:
        print("  Phone / tablet   unavailable — no active network interface")
    print()
    print("  Cache-Control: no-store — every reload shows the current files.")
    print("  Ctrl-C to stop.")
    print()

    with Server(("0.0.0.0", args.port), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  stopped.")


if __name__ == "__main__":
    main()
