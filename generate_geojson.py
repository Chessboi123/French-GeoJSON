#!/usr/bin/env python3
"""
Generate GeoJSON for the Napoleonic Empire ~1811-1812.
Three territory categories matching the map's shading:
  empire    - dark green:   French Empire proper (directly annexed)
  dependent - medium green: Dependent/satellite states
  allied    - light green:  Allied states
"""
import json

def poly(name, coords, status, desc=""):
    c = list(coords)
    if c[0] != c[-1]:
        c.append(c[0])
    return {
        "type": "Feature",
        "properties": {"name": name, "status": status, "description": desc},
        "geometry": {"type": "Polygon", "coordinates": [c]}
    }

features = []

# ─────────────────────────────────────────────────────────────────────────────
# FRENCH EMPIRE  (status = "empire", dark green)
# ─────────────────────────────────────────────────────────────────────────────

# Metropolitan France (including Alsace, Savoy, Nice, Corsica excluded)
# ~82 vertices, clockwise starting from Brest peninsula
FR = [
    [-4.80, 48.45], [-4.60, 47.80], [-4.35, 47.30], [-3.50, 47.30],
    [-2.60, 47.30], [-1.90, 47.20], [-2.30, 46.50], [-1.80, 46.30],
    [-1.40, 46.00], [-1.20, 45.90], [-1.00, 45.50], [-0.90, 45.10],
    [-0.70, 44.80], [-1.00, 44.35], [-1.40, 44.00], [-1.65, 43.70],
    [-1.80, 43.35],
    # Pyrenees (Spain-France border)
    [-1.75, 43.30], [-1.45, 43.10], [-0.75, 42.90], [-0.25, 42.72],
    [ 0.50, 42.55], [ 1.40, 42.55], [ 2.00, 42.50], [ 2.90, 42.50],
    # Mediterranean coast going NE
    [ 3.10, 42.55], [ 3.15, 43.05], [ 3.50, 43.35], [ 4.00, 43.45],
    [ 4.50, 43.40], [ 5.00, 43.30], [ 5.50, 43.15], [ 6.00, 43.10],
    [ 6.35, 43.25], [ 6.80, 43.55], [ 7.30, 43.80],
    # Italian/Alpine border going N
    [ 7.55, 44.10], [ 7.00, 44.30], [ 6.60, 44.85], [ 6.95, 45.25],
    [ 7.05, 45.85],
    # Swiss border (NW Switzerland)
    [ 6.75, 46.15], [ 6.45, 46.40], [ 6.15, 46.20], [ 6.10, 46.15],
    [ 5.95, 46.35], [ 5.95, 47.20], [ 6.20, 47.05], [ 6.80, 47.55],
    [ 7.05, 47.65],
    # Rhine border (Alsace) going N
    [ 7.55, 47.55], [ 7.65, 47.65], [ 7.90, 47.95],
    [ 7.85, 48.20], [ 7.75, 48.60], [ 7.80, 49.05], [ 7.50, 49.50],
    [ 7.10, 49.85],
    # Northern border with Low Countries
    [ 6.55, 49.95], [ 6.30, 50.00], [ 5.80, 50.15], [ 5.00, 50.35],
    [ 4.00, 50.75], [ 3.10, 50.85], [ 2.55, 51.10],
    # North coast going W
    [ 2.00, 51.00], [ 1.75, 51.05], [ 1.55, 50.95], [ 1.20, 50.72],
    [ 0.55, 49.85], [ 0.10, 49.70], [-0.40, 49.30], [-1.10, 49.35],
    # Brittany south then west
    [-1.55, 48.68], [-2.00, 48.65], [-2.25, 48.00], [-2.55, 47.55],
    [-3.00, 47.35], [-3.45, 47.35], [-4.00, 47.60], [-4.35, 47.75],
]
features.append(poly(
    "Metropolitan France", FR, "empire",
    "Core French departments, including Alsace-Lorraine, Savoy, and the County of Nice"
))

# Corsica
CORSICA = [
    [ 8.55, 41.35], [ 9.55, 41.35], [ 9.55, 41.60], [ 9.75, 41.90],
    [ 9.50, 42.30], [ 9.45, 42.80], [ 9.20, 43.00], [ 8.70, 42.60],
    [ 8.55, 42.10], [ 8.55, 41.35],
]
features.append(poly("Corsica", CORSICA, "empire", "Île de Corse – birthplace of Napoleon"))

# Belgium + Netherlands + Luxembourg (all annexed to France by 1810)
BENELUX = [
    # Southern border = France's NE border
    [ 2.55, 51.10], [ 3.10, 50.85], [ 4.00, 50.75], [ 5.00, 50.35],
    [ 5.80, 50.15], [ 6.30, 50.00], [ 6.55, 49.95],
    # SE Luxembourg
    [ 6.35, 49.45], [ 6.05, 49.55], [ 5.85, 49.50], [ 5.50, 49.55],
    [ 5.05, 49.85], [ 5.45, 50.20], [ 5.70, 50.45], [ 6.00, 50.75],
    [ 6.15, 51.00], [ 6.55, 51.30], [ 6.70, 51.55],
    # Eastern border (Netherlands-Prussia)
    [ 6.85, 51.85], [ 7.00, 52.00], [ 7.20, 52.40], [ 7.20, 53.10],
    [ 7.05, 53.35],
    # Northern Netherlands coast (Frisian coast)
    [ 6.55, 53.60], [ 6.20, 53.40], [ 5.80, 53.40], [ 5.40, 53.25],
    [ 5.00, 53.55], [ 4.70, 53.45], [ 4.65, 53.10],
    # Western Netherlands coast
    [ 4.85, 52.85], [ 4.65, 52.65], [ 4.45, 52.55], [ 4.25, 52.45],
    [ 4.00, 52.35], [ 4.00, 52.00],
    # Zeeland / Belgian coast
    [ 4.00, 51.65], [ 4.30, 51.50], [ 3.85, 51.50], [ 3.50, 51.45],
    [ 3.30, 51.65], [ 2.90, 51.50], [ 2.55, 51.35],
]
features.append(poly(
    "Belgium, Netherlands & Luxembourg", BENELUX, "empire",
    "Low Countries departments annexed to France (1810)"
))

# North Sea departments (Hamburg, Bremen, Lübeck coast)
NORTH_SEA = [
    [ 7.05, 53.35], [ 7.20, 53.30], [ 7.50, 53.30], [ 8.00, 53.50],
    [ 8.50, 53.50], [ 8.80, 53.90], [ 9.50, 53.90], [ 9.80, 54.00],
    [10.00, 53.85], [10.80, 54.20], [11.50, 53.90], [11.80, 53.90],
    [12.00, 54.20], [12.50, 54.35],
    # Southern border (Rhine Confederation)
    [12.00, 53.70], [11.50, 53.60], [11.00, 53.50], [10.50, 53.40],
    [10.00, 53.40], [ 9.50, 53.50], [ 9.00, 53.30], [ 8.50, 53.10],
    [ 8.00, 52.90], [ 7.70, 52.80], [ 7.50, 52.50], [ 7.20, 52.40],
    [ 7.20, 53.10], [ 7.05, 53.35],
]
features.append(poly(
    "North Sea Departments", NORTH_SEA, "empire",
    "French-annexed coast: Bouches-de-l'Elbe (Hamburg), Bouches-du-Weser (Bremen), Ems-Supérieur, Lippe, and Lübeck"
))

# Piedmont + Liguria (annexed to France)
PIEDMONT = [
    [ 7.30, 43.80], [ 7.55, 44.10], [ 7.00, 44.30], [ 6.60, 44.85],
    [ 6.95, 45.25], [ 7.05, 45.85],
    # Northern border (with Switzerland/Kingdom of Italy)
    [ 7.50, 45.90], [ 8.00, 46.10], [ 8.50, 46.10], [ 8.90, 45.95],
    [ 9.00, 45.85],
    # Eastern border
    [ 9.10, 45.60], [ 9.20, 45.20], [ 9.50, 44.80], [ 9.50, 44.30],
    # Ligurian coast
    [ 9.50, 43.80], [ 9.20, 43.90], [ 8.80, 43.90],
    [ 8.50, 43.90], [ 8.00, 43.85], [ 7.50, 43.80],
]
features.append(poly(
    "Piedmont & Liguria", PIEDMONT, "empire",
    "French-annexed: Piedmont (1802), Liguria/Genoa (1805), Parma and Piacenza"
))

# Tuscany + Parma departments (annexed to France 1808-1809)
TUSCANY = [
    [ 9.50, 44.80], [ 9.00, 45.10], [ 9.50, 45.20], [10.00, 45.10],
    [10.50, 45.20], [10.80, 44.90], [11.50, 44.70], [11.80, 44.55],
    [12.00, 44.50], [12.30, 44.10],
    # SE border with Papal States
    [11.80, 43.80], [11.30, 43.60], [11.00, 43.40],
    [10.50, 43.05], [10.10, 43.00], [ 9.70, 43.20], [ 9.50, 43.50],
    [ 9.50, 44.30],
]
features.append(poly(
    "Tuscany & Parma", TUSCANY, "empire",
    "French-annexed: Tuscany (Étrurie, 1809), Parma and Piacenza"
))

# Papal States (Rome / Lazio) annexed 1809
PAPAL = [
    [11.80, 43.80], [12.30, 44.10], [12.80, 44.10], [13.20, 43.95],
    [13.50, 43.70], [13.70, 43.50], [13.55, 43.00], [13.30, 42.70],
    [13.00, 42.40], [12.70, 42.20], [12.30, 41.90], [12.00, 41.80],
    [11.80, 41.70], [11.50, 41.55], [11.30, 41.40],
    [11.20, 41.45], [11.50, 42.00], [11.50, 42.50], [11.50, 43.00],
    [11.80, 43.40],
]
features.append(poly(
    "Papal States", PAPAL, "empire",
    "Papal States annexed to France (1809) – Lazio, Umbria, Marche"
))

# Illyrian Provinces (annexed 1809) – Carniola, Carinthia, Trieste, Istria, Dalmatia
ILLYRIA = [
    [13.50, 46.50], [14.00, 46.55], [14.50, 46.50], [15.00, 46.55],
    [15.50, 46.40], [15.70, 46.20], [15.50, 45.90], [15.60, 45.70],
    [15.80, 45.50],
    # Croatian / Dalmatian coast going SE
    [16.00, 45.20], [16.50, 45.00], [16.80, 44.70], [17.00, 44.40],
    [17.30, 44.10], [17.50, 43.80], [17.70, 43.50], [18.00, 43.20],
    [18.10, 43.00], [18.55, 42.60], [18.55, 42.45],
    # Inland return
    [18.20, 42.40], [18.10, 42.65], [17.80, 43.00], [17.50, 43.30],
    [17.20, 43.55], [16.80, 43.70], [16.50, 44.00], [16.20, 44.30],
    [16.00, 44.50], [15.50, 44.50], [15.00, 44.65], [14.50, 44.70],
    [14.00, 45.00], [13.70, 45.40], [13.50, 45.70], [13.50, 46.00],
]
features.append(poly(
    "Illyrian Provinces", ILLYRIA, "empire",
    "French-annexed (1809): Carniola, Carinthia, Goriza, Trieste, Istria, Dalmatia, Ragusa, Cattaro"
))

# ─────────────────────────────────────────────────────────────────────────────
# DEPENDENT / SATELLITE STATES  (status = "dependent", medium green)
# ─────────────────────────────────────────────────────────────────────────────

# Swiss Confederation (Mediationstates – de facto French protectorate)
SWISS = [
    [ 6.10, 46.15], [ 6.45, 46.40], [ 7.05, 45.85], [ 7.50, 45.90],
    [ 8.00, 46.10], [ 8.50, 46.10], [ 8.90, 45.95], [ 9.00, 45.85],
    [ 9.50, 46.35], [10.00, 46.35], [10.45, 46.50], [10.50, 46.85],
    [10.50, 47.20], [10.20, 47.35], [ 9.80, 47.50], [ 9.50, 47.55],
    [ 9.00, 47.65], [ 8.50, 47.80], [ 8.00, 47.65], [ 7.60, 47.60],
    [ 7.05, 47.65], [ 6.20, 47.05], [ 5.95, 47.20], [ 5.95, 46.35],
    [ 6.10, 46.15],
]
features.append(poly(
    "Swiss Confederation", SWISS, "dependent",
    "Helvetic Confederation – French-mediated confederation of 19 cantons"
))

# Confederation of the Rhine + Kingdom of Westphalia (grouped as medium green)
# Covers roughly 6.5–15E, 47.5–54N minus French-annexed Hamburg area
RHINE_CONF = [
    # Western border = Rhine (France's eastern border in Alsace, Saarland edge)
    [ 7.05, 47.65], [ 7.60, 47.60], [ 8.00, 47.65], [ 8.50, 47.80],
    [ 9.00, 47.65], [ 9.50, 47.55], [ 9.80, 47.50], [10.20, 47.35],
    [10.50, 47.20], [10.50, 46.85], [10.45, 46.50], [10.00, 46.35],
    # Eastern border with Austria
    [10.50, 47.20], [11.00, 47.40], [12.00, 47.65], [12.50, 47.65],
    [13.00, 47.55], [13.50, 47.55], [14.00, 47.60], [14.50, 47.65],
    [15.00, 47.70], [15.20, 47.80],
    # Eastern border with Prussia
    [15.20, 48.20], [15.50, 49.00], [15.50, 50.00], [15.30, 50.50],
    [15.00, 51.00], [14.80, 51.50], [14.50, 51.85], [14.70, 52.10],
    [14.80, 52.50], [14.60, 53.00], [14.20, 53.50],
    # Northern border with French North Sea departments
    [12.00, 53.70], [11.50, 53.60], [11.00, 53.50], [10.50, 53.40],
    [10.00, 53.40], [ 9.50, 53.50], [ 9.00, 53.30], [ 8.50, 53.10],
    [ 8.00, 52.90], [ 7.70, 52.80], [ 7.50, 52.50], [ 7.20, 52.40],
    # Western border with Netherlands/Belgium (Low Countries)
    [ 7.00, 52.00], [ 6.85, 51.85], [ 6.70, 51.55], [ 6.55, 51.30],
    [ 6.15, 51.00], [ 6.00, 50.75], [ 5.70, 50.45], [ 5.45, 50.20],
    [ 5.05, 49.85], [ 5.50, 49.55], [ 5.85, 49.50], [ 6.05, 49.55],
    [ 6.35, 49.45], [ 6.55, 49.95], [ 7.10, 49.85], [ 7.50, 49.50],
    [ 7.80, 49.05], [ 7.75, 48.60], [ 7.85, 48.20], [ 7.90, 47.95],
    [ 7.65, 47.65], [ 7.55, 47.55], [ 7.05, 47.65],
]
features.append(poly(
    "Confederation of the Rhine & Kingdom of Westphalia", RHINE_CONF, "dependent",
    "Rhine Confederation (Bayern, Württemberg, Baden, Berg, Hessen, Nassau, etc.) and Kingdom of Westphalia (Jérôme Bonaparte)"
))

# Kingdom of Italy (Eugène de Beauharnais, viceroy)
# Northern Italy: Lombardy, Veneto, Emilia-Romagna
KINGDOM_ITALY = [
    [ 8.90, 45.95], [ 9.00, 45.85], [ 9.10, 45.60], [ 9.20, 45.20],
    [ 9.50, 44.80], [ 9.50, 44.30], [11.80, 44.55], [11.50, 44.70],
    [10.80, 44.90], [10.50, 45.20], [10.00, 45.10], [ 9.50, 45.20],
    [ 9.00, 45.10], [ 9.50, 44.80],
    # NE towards Venice and Verona
    [10.00, 45.10], [10.50, 45.20], [11.00, 45.50], [11.50, 45.65],
    [12.00, 45.65], [12.40, 45.50], [12.65, 45.20], [13.00, 45.00],
    [13.30, 45.70], [13.50, 45.70], [13.50, 46.00], [13.50, 46.50],
    [14.00, 46.55], [14.50, 46.50], [15.00, 46.55], [15.50, 46.40],
    # SE border (with Illyria)
    [15.50, 45.90], [15.60, 45.70], [15.80, 45.50],
    # Western border back to Piedmont (France)
    [13.00, 45.00], [12.65, 45.20], [12.40, 45.50], [12.00, 45.65],
    [11.50, 45.65], [11.00, 45.50], [10.50, 45.20], [10.00, 45.10],
    [ 9.50, 44.80], [ 9.50, 44.30], [12.00, 44.50], [12.00, 44.50],
]
# I need to rewrite Kingdom of Italy cleanly
KINGDOM_ITALY = [
    # Start at Piedmont/Switzerland border
    [ 8.90, 45.95], [ 9.10, 45.60], [ 9.50, 45.20], [ 9.50, 44.80],
    [ 9.50, 44.30], [12.00, 44.50], [11.80, 44.55], [11.50, 44.70],
    [10.80, 44.90], [10.50, 45.20],
    # Po Valley going NE
    [11.00, 45.50], [11.50, 45.65], [12.00, 45.65], [12.40, 45.50],
    [12.65, 45.20], [13.00, 45.00],
    # Venice area and NE border (with Illyria)
    [13.30, 45.70], [13.50, 45.70], [13.50, 46.50],
    # N border (Alpine - Austrian)
    [14.50, 46.50], [15.00, 46.55], [15.50, 46.40],
    # E border (Illyria)
    [15.20, 47.80], [15.00, 47.70], [14.50, 47.65], [14.00, 47.60],
    [13.50, 47.55], [13.00, 47.55], [12.50, 47.65], [12.00, 47.65],
    [11.00, 47.40], [10.50, 47.20], [10.50, 46.85], [10.45, 46.50],
    [10.00, 46.35], [ 9.50, 46.35], [ 9.00, 45.85], [ 8.90, 45.95],
]
features.append(poly(
    "Kingdom of Italy", KINGDOM_ITALY, "dependent",
    "Kingdom of Italy under Eugène de Beauharnais – Lombardy, Veneto, Emilia-Romagna, Marche"
))

# Kingdom of Naples (Joachim Murat, 1808-1815)
# Southern Italy – Campania, Calabria, Puglia, Basilicata, Abruzzo
NAPLES = [
    # Northern border with Papal States
    [11.30, 41.40], [11.80, 41.70], [12.00, 41.80], [12.30, 41.90],
    [12.70, 42.20], [13.00, 42.40], [13.30, 42.70], [13.55, 43.00],
    [13.70, 43.50], [13.50, 43.70], [13.20, 43.95], [12.80, 44.10],
    # Adriatic coast going SE
    [14.00, 43.00], [14.50, 42.40], [15.00, 41.80], [15.50, 41.00],
    [16.00, 41.00], [16.50, 40.60], [17.00, 40.40], [17.80, 40.40],
    [18.30, 40.10], [18.50, 40.65], [18.00, 40.80], [17.55, 40.95],
    # Heel of Italy and sole
    [17.10, 40.30], [16.80, 39.95], [16.55, 39.70], [16.50, 38.95],
    [16.00, 38.35], [15.70, 38.00], [15.65, 37.95],
    # Toe and up W coast
    [15.95, 38.00], [16.00, 38.50], [16.30, 38.80], [16.00, 39.00],
    [15.70, 39.30], [15.65, 39.80], [15.90, 40.10], [15.70, 40.45],
    [15.30, 40.60], [15.00, 40.95], [14.80, 40.70], [14.40, 40.45],
    [14.00, 40.65], [13.80, 40.80], [13.60, 41.00], [13.30, 41.20],
    [11.30, 41.40],
]
features.append(poly(
    "Kingdom of Naples", NAPLES, "dependent",
    "Kingdom of Naples under Joachim Murat (1808) – all of mainland S Italy"
))

# Sicily (Kingdom of the Two Sicilies under Bourbon – NOT French, so SKIP)
# (Sicily remained under British-protected Bourbon rule, not Napoleon's domain)

# ─────────────────────────────────────────────────────────────────────────────
# ALLIED STATES  (status = "allied", light green)
# ─────────────────────────────────────────────────────────────────────────────

# Kingdom of Spain (Joseph Bonaparte, 1808–1813)
SPAIN = [
    # French border (Pyrenees)
    [-1.80, 43.35], [-1.75, 43.30], [-1.45, 43.10], [-0.75, 42.90],
    [-0.25, 42.72], [ 0.50, 42.55], [ 1.40, 42.55], [ 2.00, 42.50],
    [ 2.90, 42.50], [ 3.10, 42.55],
    # Mediterranean coast going SW
    [ 3.20, 41.70], [ 3.10, 40.95], [ 2.50, 40.45], [ 1.60, 39.55],
    [ 0.90, 39.00], [ 0.20, 39.45], [-0.10, 38.65], [-0.65, 38.10],
    [-0.70, 37.65], [-1.10, 37.55], [-1.80, 37.55], [-2.20, 36.90],
    # S coast W
    [-2.80, 36.60], [-3.40, 36.75], [-4.00, 36.70], [-4.60, 36.65],
    [-5.35, 36.00], [-5.70, 36.05],
    # Atlantic (Portugal border/coast)
    [-6.15, 36.40], [-6.55, 36.90], [-7.10, 37.15], [-7.40, 37.40],
    [-7.45, 38.00], [-7.10, 38.20], [-6.90, 38.40], [-6.85, 39.00],
    [-7.00, 39.70], [-6.80, 40.35], [-6.90, 41.05], [-6.75, 41.90],
    [-6.20, 41.95], [-6.20, 41.55],
    # N Atlantic coast going NE
    [-8.85, 42.05], [-9.20, 43.50], [-8.85, 43.75], [-8.00, 43.75],
    [-7.65, 43.60], [-6.65, 43.60], [-5.35, 43.75], [-4.00, 43.65],
    [-3.45, 43.60], [-2.65, 43.55], [-2.00, 43.50], [-1.80, 43.40],
    [-1.80, 43.35],
]
features.append(poly(
    "Kingdom of Spain", SPAIN, "allied",
    "Kingdom of Spain under Joseph Bonaparte (1808) – Peninsular War era"
))

# Portugal (NOT shown as French – grey on map)
# Duchy of Warsaw (Napoleon's Polish satellite state)
WARSAW = [
    # Western border (Prussia / Rhine Confederation)
    [14.20, 53.50], [14.60, 53.00], [14.80, 52.50], [14.70, 52.10],
    [14.50, 51.85], [14.80, 51.50], [15.00, 51.00], [15.30, 50.50],
    [15.50, 50.00], [15.50, 49.00],
    # Southern border (Austria – Galicia)
    [16.00, 49.50], [17.00, 50.00], [18.00, 49.80],
    [18.80, 49.50], [19.50, 49.40], [20.00, 49.25], [20.50, 49.25],
    [21.00, 49.40], [22.00, 49.70], [22.50, 49.65], [23.00, 50.40],
    # Eastern border (Russia)
    [23.20, 51.00], [23.60, 51.60], [23.80, 52.00], [23.80, 52.70],
    [23.50, 53.50], [22.80, 53.95], [22.00, 54.40], [21.50, 54.35],
    [21.00, 54.40],
    # N border (Prussia / East Prussia)
    [20.50, 54.40], [20.00, 54.30], [19.00, 54.15], [18.30, 54.10],
    [17.50, 53.75], [16.50, 53.80], [15.50, 53.80], [14.60, 53.90],
    [14.20, 53.50],
]
features.append(poly(
    "Duchy of Warsaw", WARSAW, "allied",
    "Grand Duchy of Warsaw – Polish state created by Napoleon (1807), expanded 1809"
))

# Kingdom of Denmark (allied; controls Norway and Holstein)
DENMARK = [
    # Jutland peninsula
    [ 8.60, 55.00], [ 8.00, 54.85], [ 8.10, 55.40], [ 8.55, 56.00],
    [ 8.20, 56.55], [ 8.60, 57.10], [ 9.55, 57.60], [10.60, 57.75],
    [10.50, 57.00], [10.00, 56.55], [ 9.85, 56.15], [10.30, 55.95],
    [10.60, 55.75], [10.75, 55.50], [10.65, 55.25], [10.30, 55.00],
    [ 9.55, 54.75], [ 9.00, 54.65], [ 8.60, 55.00],
]
features.append(poly(
    "Kingdom of Denmark (Jutland)", DENMARK, "allied",
    "Kingdom of Denmark and Norway – allied with Napoleon; continental Jutland shown"
))

# Zealand (main Danish island)
ZEALAND = [
    [11.95, 55.95], [12.50, 56.10], [12.60, 56.50], [12.10, 56.65],
    [11.55, 56.45], [11.20, 55.85], [11.95, 55.95],
]
features.append(poly("Denmark – Zealand (Sjælland)", ZEALAND, "allied", "Main Danish island including Copenhagen"))

# Funen island
FUNEN = [
    [10.00, 55.20], [10.55, 55.55], [10.90, 55.40], [10.55, 55.15],
    [10.00, 55.20],
]
features.append(poly("Denmark – Funen (Fyn)", FUNEN, "allied", "Danish island of Funen"))

# ─────────────────────────────────────────────────────────────────────────────
# Write output
# ─────────────────────────────────────────────────────────────────────────────
geojson = {
    "type": "FeatureCollection",
    "name": "Napoleonic Empire circa 1812",
    "description": (
        "Territories of the French Empire and its dependent/allied states at their greatest extent (~1811-1812). "
        "Status values: 'empire' = directly annexed French departments (dark green); "
        "'dependent' = satellite kingdoms and protectorates (medium green); "
        "'allied' = allied sovereign states (light green)."
    ),
    "features": features
}

out_path = "/home/user/French-GeoJSON/napoleonic_empire_1812.geojson"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(geojson, f, indent=2, ensure_ascii=False)

print(f"Written {len(features)} features to {out_path}")
for f_ in features:
    coords = f_["geometry"]["coordinates"][0]
    print(f"  {f_['properties']['status']:10s}  {len(coords):3d} pts  {f_['properties']['name']}")
