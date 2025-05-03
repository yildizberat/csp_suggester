# 🧠 CSP Suggester — Mitmproxy Add-on

`csp_suggester.py` is a powerful add-on for [mitmproxy](https://mitmproxy.org/) that automatically detects and categorizes external domains used by a visited website. It generates a JSON file containing domain suggestions for a secure Content Security Policy (CSP).

This add-on helps developers build tighter CSP rules without having to manually inspect network requests.

---

## 🚀 Features

- 🔍 Automatically detects:
  - `script-src` domains (e.g., CDN JS files)
  - `style-src` (CSS files)
  - `img-src` (images)
  - `connect-src` (XHR, fetch, APIs)
  - `default-src` (fallback sources)
- ✅ Detects and stores the first visited domain as `origin`
- ✅ Saves output as `shared/csp_suggestions.json`
- ✅ Ignores internal localhost requests (e.g., Flask UI)

---

## 🛠 How It Works

1. You run mitmproxy with the addon:

```bash
mitmproxy -s csp_suggester.py --listen-port 8080
```

2. Then visit any website **through the proxy** (e.g., using firefox or chrome browser with foxyproxy).
3. The script will inspect each request and update the JSON output.

---

## 📄 Output Format (shared/csp_suggestions.json)

```json
{
  "origin": "example.com",
  "categories": {
    "script-src": ["cdn.jsdelivr.net"],
    "img-src": ["images.unsplash.com"],
    "style-src": ["fonts.googleapis.com"],
    "connect-src": ["api.example.com"]
  }
}
```

This output can be visualized using "flask_server.py" or manually used to craft CSP headers.

---


## 👩‍💻 Author
Created with ❤️ by @yildizberat — open for contributions and collaborations!

---

> Don’t guess your CSP. Trace it. Visualize it. Harden it. — CSP Suggester
