# AOE2 API Personalizada

Este proyecto es una API construida con FastAPI que permite consultar estadísticas en tiempo real de jugadores de Age of Empires II, usando la API de AoE2 Companion.

## 📦 Contenido

- `main.py`: Código fuente del backend con FastAPI
- `requirements.txt`: Dependencias necesarias
- `aoe2_dashboard.html`: Interfaz web para ingresar profile IDs personalizados y ver estadísticas

## 🚀 Cómo desplegar en Render.com

1. Sube estos archivos a un nuevo repositorio de GitHub.
2. Ve a [https://render.com](https://render.com) y crea un nuevo **Web Service**.
3. Configura los siguientes campos:

| Campo            | Valor                                     |
|------------------|-------------------------------------------|
| Build Command    | `pip install -r requirements.txt`         |
| Start Command    | `uvicorn main:app --host 0.0.0.0 --port 10000` |

4. Espera a que se despliegue correctamente. En los logs deberías ver:

```
INFO:     Uvicorn running on http://0.0.0.0:10000
```

## ✅ Validación

### Probar en navegador:

- Visita:  
  `https://tu-api.onrender.com/estadisticas?id=287196&id=416330`

### Probar desde el HTML:

- Abre `aoe2_dashboard.html` en tu navegador
- Asegúrate de que `API_URL` apunte a tu nueva URL en Render:

```js
const API_URL = "https://tu-api.onrender.com/estadisticas";
```

- Ingresa uno o varios profile IDs y presiona “Mostrar estadísticas”

## 🧪 Probar con curl:

```bash
curl "https://tu-api.onrender.com/estadisticas?id=287196&id=416330"
```

---

Desarrollado con ❤️ usando FastAPI y Chart.js