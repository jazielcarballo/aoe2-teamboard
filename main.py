from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Regex para extraer nombre, ELO, ranking y winrate
pattern = r"^.{1,2}\s{2}(.+?)\s\((\d+)\)\sRank\s#(\w+),.*?(\w+)%\swinrate"

@app.get("/estadisticas")
def obtener_estadisticas(id: list[int] = Query(...)):
    data = []
    for pid in id:
        url = f"https://data.aoe2companion.com/api/nightbot/rank?profile_id={pid}"
        response = requests.get(url)
        texto = response.text.strip().replace("\xa0", " ").strip('"')

        match = re.search(pattern, texto)
        if match:
            ranking = match.group(3)
            winrate = match.group(4)
            data.append({
                "id": pid,  # 👈 aquí se agrega el ID manualmente al resultado
                "nombre": match.group(1),
                "elo": int(match.group(2)),
                "ranking": int(ranking) if ranking.isdigit() else None,
                "winrate": int(winrate) if winrate.isdigit() else None
            })
    return data
