from mitmproxy import http
from urllib.parse import urlparse
import json
from pathlib import Path

CSP_FILE = Path("csp_suggestions.json")

# Kategorilere göre ayırmak istersen burayı genişletebiliriz
domains = {
    "script-src": set(),
    "img-src": set(),
    "style-src": set(),
    "connect-src": set(),
    "default-src": set()
}

def save():
    data = {k: sorted(list(v)) for k, v in domains.items()}
    CSP_FILE.write_text(json.dumps(data, indent=2))

def request(flow: http.HTTPFlow):
    parsed = urlparse(flow.request.pretty_url)
    domain = parsed.netloc
    path = parsed.path.lower()

    if path.endswith(".js"):
        domains["script-src"].add(domain)
    elif path.endswith(".css"):
        domains["style-src"].add(domain)
    elif any(path.endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".webp", ".svg", ".gif"]):
        domains["img-src"].add(domain)
    elif flow.request.method in ["POST", "GET"] and "api" in path:
        domains["connect-src"].add(domain)
    else:
        domains["default-src"].add(domain)

    save()