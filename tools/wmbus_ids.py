#!/usr/bin/env python3
"""Zestawienie nadajnikow wM-Bus z logu `esphome logs` (linie RAMKA: ... hex=...).

Uzycie: wmbus_ids.py plik.log [plik2.log ...]
Naglowek T1: L C M(2, LE) ID(4, LE/BCD) VER TYPE CI ... - zawsze jawny.
"""
import re, sys
from collections import defaultdict

MANUF = lambda m: "".join(chr(((m >> s) & 0x1F) + 64) for s in (10, 5, 0))
TYPES = {0x07: "woda", 0x06: "ciepla woda", 0x16: "zimna woda", 0x04: "cieplo",
         0x03: "gaz", 0x02: "prad", 0x08: "podzielnik", 0x1A: "dym", 0x1B: "czujnik"}
rx = re.compile(r"^\[(\S+?)\].*RAMKA: RSSI=(-?\d+)dBm len=(\d+) hex=([0-9a-f]+)")
seen = defaultdict(lambda: {"n": 0, "rssi": [], "first": None, "last": None, "ci": set()})

for path in sys.argv[1:]:
    for line in open(path, errors="replace"):
        m = rx.search(line)
        if not m:
            continue
        ts, rssi, _, h = m.groups()
        b = bytes.fromhex(h)
        if len(b) < 11:
            continue
        man = MANUF(b[2] | b[3] << 8)
        mid = b[7:3:-1].hex()
        e = seen[(man, mid, b[8], b[9])]
        e["n"] += 1
        e["rssi"].append(int(rssi))
        e["first"] = e["first"] or ts
        e["last"] = ts
        e["ci"].add(f"{b[10]:02x}")

print(f"{'prod':4} {'ID':8} {'ver':>3} {'typ':12} {'ile':>4} {'RSSI sr/max':>12} {'CI':6} okno")
for (man, mid, ver, typ), e in sorted(seen.items(), key=lambda kv: -max(kv[1]["rssi"])):
    r = e["rssi"]
    print(f"{man:4} {mid:8} {ver:3d} {TYPES.get(typ, hex(typ)):12} {e['n']:4d} "
          f"{sum(r)/len(r):6.0f}/{max(r):4d}  {','.join(sorted(e['ci'])):6} {e['first']}-{e['last']}")
