# CERO BACHE · UE-1 — Dashboard de Obra

Dashboard interactivo de seguimiento del bacheo vial de la **UE-1 (Construyendo Canelones)**, a partir de la planilla de obra de GRINOR. Cubre Las Piedras, La Paz, 18 de Mayo y Progreso.

Es un sitio **100% estático**: un solo `index.html` con los datos embebidos en `assets/data.js`. No usa CDN ni conexión a internet — funciona igual abriendo el archivo directo en el navegador, en un servidor propio, o publicado en GitHub Pages.

## 📁 Estructura del repositorio

```
├── index.html          # Dashboard completo (HTML + CSS + JS)
├── favicon.ico          # Ícono de marca (pestaña del navegador)
├── assets/
│   ├── logo.png          # Logo oficial UE-1, usado en el header
│   └── data.js            # Datos de obra, embebidos como variable JS
└── README.md            # Este archivo
```

## 🚀 Publicar en GitHub Pages

1. Creá un repositorio nuevo en GitHub (público, para poder usar Pages gratis) y subí estos 4 elementos (`index.html`, `favicon.ico`, `assets/`, `README.md`) a la raíz del repo — por ejemplo con GitHub Desktop, o:
   ```bash
   git init
   git add .
   git commit -m "Dashboard CERO BACHE UE-1"
   git branch -M main
   git remote add origin https://github.com/TU-USUARIO/TU-REPO.git
   git push -u origin main
   ```
2. En el repositorio de GitHub: **Settings → Pages**.
3. En **Source**, elegí **Deploy from a branch**, rama `main`, carpeta `/ (root)`. Guardá.
4. GitHub tarda uno o dos minutos en publicar. La URL queda como:
   `https://TU-USUARIO.github.io/TU-REPO/`

No hace falta build, ni Node, ni ningún paso adicional: es HTML puro.

## 🔄 Actualizar los datos más adelante

Los datos viven en `assets/data.js` como un array de objetos JavaScript (`window.DASHBOARD_DATA`). Cada registro tiene esta forma:

```js
{
  "id": 1,
  "numero": 1,
  "mes": "Enero-Febrero 2026",
  "mes_key": "2026-01",
  "localidad": "Las Piedras",
  "calle": "Elias Regules",
  "entre1": "Liber Seregni",
  "entre2": "Criolla de Artigas",
  "m2": 24.64,
  "toneladas": null,
  "observacion": "",
  "categoria": "Bacheo estándar",
  "estado": "Realizado",
  "lat": null,
  "lng": null
}
```

Para cargar una planilla nueva, la forma más simple es pedirle a Claude (u otra herramienta) que regenere `assets/data.js` a partir del Excel actualizado, respetando esta misma estructura, y reemplazar el archivo en el repo.

### Coordenadas GPS (📍 en la tabla)

El Excel de origen (`BACHEO_GRINOR_2026.xlsx`) **no trae coordenadas por tramo**, así que el ícono 📍 de cada fila aparece atenuado y no clickeable. Apenas se complete `lat` y `lng` en un registro (por ejemplo `"lat": -34.723, "lng": -56.218`), ese ícono se activa automáticamente y al hacer clic abre la ubicación en Google Maps — no requiere tocar el código.

### Estado, localidad y categoría

* **Estado** se infiere de la planilla: si la celda de M² dice *"Sin Hacer"* o el valor es 0, el tramo queda como `Pendiente`; en cualquier otro caso, `Realizado`.
* **Categoría** toma la columna "Observación" del Excel cuando existe (p. ej. *"Fresado y reposición"*, *"8 cm Asfalto"*); si no hay observación, se usa `Bacheo estándar` o `Pendiente de bacheo`.
* **Localidad** se toma del encabezado de cada bloque de la planilla (*"Las Piedras - Base…"*, *"La Paz - Base…"*). Los filtros incluyen las 4 localidades de la UE-1 (Las Piedras, La Paz, 18 de Mayo, Progreso) aunque hoy solo las dos primeras tienen tramos cargados — quedan listas para cuando haya datos de las otras dos.

## ⚠️ Nota sobre el origen de los datos

El Excel provisto (`BACHEO_GRINOR_2026.xlsx`) es una **planilla de producción de obra** (bacheo ya ejecutado, organizado por calle/tramo/mes, con M² y toneladas), **no** un export de reclamos de un Formulario. Por eso este dashboard funciona como panel de seguimiento de obra:

* No incluye "fecha de reclamo" día a día — la granularidad real de la fuente es **mensual** (los períodos de reporte de la planilla: Enero-Febrero, Marzo, Abril, Mayo, Junio, Julio, Agosto 2026). El filtro "Desde / Hasta" del panel avanzado trabaja con esos períodos.
* No incluye coordenadas GPS ni estado de reclamo ciudadano — el campo **Estado** que ves (Realizado / Pendiente) refleja si el tramo fue bacheado o figura como "Sin Hacer" en la planilla de obra.
* Si más adelante conseguís el export real de reclamos de Formularios (con estado, localidad, categoría, fecha y GPS), decíselo a Claude y se puede cruzar con esta base o migrar el dashboard a esa estructura sin perder el diseño ni las funcionalidades ya construidas.

## ✅ Funcionalidades incluidas

- 6 KPIs con barra de progreso animada (M² bacheados, toneladas, tramos completados/pendientes, localidades con obra, meses con actividad).
- Filtros rápidos de un clic por estado y localidad.
- Filtros avanzados: estado, localidad, categoría, rango de meses, búsqueda libre — todo combinable.
- 3 gráficos dibujados en SVG puro (sin librerías externas, sin CDN): tendencia mensual de M², barras por categoría, donut por localidad.
- Tabla ordenable por cualquier columna (clic en el encabezado), paginable (25 / 50 / 100 / todas).
- Ícono 📍 de GPS por fila, clickeable solo cuando el registro tiene coordenadas cargadas.
- Botón **Mapa General**, enlaza al mapa colaborativo de Google My Maps de la UE-1.
- Exportación a CSV de exactamente lo que está filtrado y ordenado en pantalla (con codificación compatible con Excel).
- Diseño oscuro estilo BI/SaaS, responsive (mobile / tablet / desktop), con el logo oficial de la UE-1 en el header.

## 🖥️ Ver el dashboard en tu computadora sin subir nada

Simplemente hacé doble clic en `index.html`. Funciona sin servidor y sin internet porque todo (datos, estilos, lógica y gráficos) está en los mismos archivos del repo.
