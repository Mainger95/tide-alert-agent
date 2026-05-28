THRESHOLD = 4.5

# données simulées (remplacer plus tard par API)
tides = [
    {"time": "08:00", "height": 3.2},
    {"time": "12:00", "height": 5.1},
    {"time": "18:00", "height": 4.8}
]

for t in tides:
    if t["height"] > THRESHOLD:
        print(f"⚠️ Alerte marée : {t['height']} m à {t['time']}")
    else:
        print(f"✅ OK : {t['height']} m")
