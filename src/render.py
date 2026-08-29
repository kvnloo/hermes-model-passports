#!/usr/bin/env python3
"""Deterministic, dependency-free Model Passport SVG renderer."""
from __future__ import annotations
import html
import json
import pathlib
import sys

CAPS = {"reasoning": "R", "vision": "V", "tools": "T", "structured_output": "S", "audio": "A", "image": "I", "open_weights": "O", "local": "L"}

def esc(value):
    return html.escape(str(value), quote=True)

def render(passport: dict) -> str:
    ident = passport["identity"]
    route = passport["route"]
    visual = passport["visual"]
    caps = [glyph for key, glyph in CAPS.items() if passport.get("capabilities", {}).get(key) is True][:5]
    variant = ident.get("variant") or "MODEL"
    accent = visual["accent"]
    monogram = visual.get("fallback_monogram") or ident["maker"][:2].upper()
    cap_text = "  ".join(caps) if caps else "CAPABILITIES UNKNOWN"
    aria = esc(f"{ident['display_name']} via {route['provider']}")
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="520" height="176" viewBox="0 0 520 176" role="img" aria-label="{aria}">',
        '<rect width="520" height="176" rx="20" fill="#080A0D"/>',
        '<rect x="7" y="7" width="506" height="162" rx="15" fill="#0D1118" stroke="#303745"/>',
        f'<path d="M7 42V22Q7 7 22 7H164" fill="none" stroke="{accent}" stroke-width="2"/>',
        f'<rect x="22" y="28" width="88" height="88" rx="18" fill="#151922" stroke="{accent}"/>',
        f'<text x="66" y="80" text-anchor="middle" fill="{accent}" font-family="ui-monospace,monospace" font-size="25" font-weight="700">{esc(monogram)}</text>',
        f'<text x="132" y="53" fill="#8B95A7" font-family="ui-monospace,monospace" font-size="10" letter-spacing="2">{esc(ident["maker"].upper())} / {esc(ident["family"].upper())}</text>',
        f'<text x="132" y="82" fill="#F4F7FB" font-family="system-ui,sans-serif" font-size="22" font-weight="650">{esc(ident["display_name"])}</text>',
        '<rect x="132" y="96" width="112" height="25" rx="4" fill="#151922" stroke="#303745"/>',
        f'<text x="188" y="113" text-anchor="middle" fill="{accent}" font-family="ui-monospace,monospace" font-size="10" font-weight="700" letter-spacing="1.5">{esc(str(variant).upper())}</text>',
        f'<text x="264" y="113" fill="#6DE1FF" font-family="ui-monospace,monospace" font-size="11" letter-spacing="2">{esc(cap_text)}</text>',
        '<rect x="366" y="135" width="132" height="22" rx="4" fill="#151922"/>',
        f'<text x="432" y="150" text-anchor="middle" fill="#8B95A7" font-family="ui-monospace,monospace" font-size="9" letter-spacing="1.5">VIA {esc(route["provider"].upper())}</text>',
        '</svg>'
    ]
    return "\n".join(lines)

def main():
    source = pathlib.Path(sys.argv[1])
    out = pathlib.Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    passports = json.loads(source.read_text())
    for passport in passports:
        slug = passport["identity"]["canonical_id"].replace("/", "--")
        (out / f"{slug}.svg").write_text(render(passport))
    print(f"rendered {len(passports)} passports to {out}")

if __name__ == "__main__":
    main()
