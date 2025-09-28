import re

# Expresiones regulares para parsear las reglas
RE_STATION = re.compile(r'station\(["\'](.+?)["\']\)\.')
RE_CONNECT = re.compile(r'connect\(["\'](.+?)["\']\s*,\s*["\'](.+?)["\']\s*,\s*([0-9]+(?:\.[0-9]+)?)\s*,\s*["\'](.+?)["\']\)\.')
RE_COORD = re.compile(r'coord\(["\'](.+?)["\']\s*,\s*([-\d\.]+)\s*,\s*([-\d\.]+)\)\.')
RE_TRANSFER = re.compile(r'transfer_penalty\(\s*([0-9]+(?:\.[0-9]+)?)\s*\)\.')

def parse_kb(filepath):
    """Lee el archivo KB y devuelve estaciones, conexiones y reglas."""
    stations = set()
    edges = []  # (u, v, time, line)
    coords = {}
    transfer_penalty = 0.0

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('%') or line.startswith('#'):
                continue
            m = RE_STATION.match(line)
            if m:
                stations.add(m.group(1))
                continue
            m = RE_CONNECT.match(line)
            if m:
                u, v, t, line_name = m.groups()
                edges.append((u, v, float(t), line_name))
                continue
            m = RE_COORD.match(line)
            if m:
                s, lon, lat = m.groups()
                coords[s] = (float(lon), float(lat))
                continue
            m = RE_TRANSFER.match(line)
            if m:
                transfer_penalty = float(m.group(1))
                continue

    return {
        "stations": stations,
        "edges": edges,
        "coords": coords,
        "transfer_penalty": transfer_penalty,
    }
