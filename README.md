# Bacheo GRINOR 2026 — Las Piedras y La Paz

Datos de avance del bacheo ("baches"/tramos) ejecutado en los municipios de
**Las Piedras** y **La Paz**, período **Enero–Agosto 2026**, extraídos del
informe *"Informe Detallado Mes a Mes Bacheo GRINOR"*.

## Resumen del período

| Mes | Baches del mes | Baches acumulados | m² del mes | m² acumulado | Calles del mes | Calles acumuladas |
|---|---|---|---|---|---|---|
| Enero-Febrero | 38 | 38 | 1.065 | 1.065 | 3 | 3 |
| Marzo | 26 | 64 | 813 | 1.877 | 2 | 5 |
| Abril | 20 | 84 | 943 | 2.820 | 4 | 7 |
| Mayo | 23 | 107 | 1.137 | 3.957 | 3 | 10 |
| Junio | 41 | 148 | 2.271 | 6.228 | 8 | 16 |
| Julio | 65 | 213 | 2.856 | 9.084 | 10 | 24 |
| Agosto | 22 | 235 | 1.245 | 10.329 | 8 | 26 |
| **Total** | **235** | | **10.329** | | **26** | |

> Nota: se excluyen del conteo de baches y m² los tramos marcados como
> "Sin Hacer" (pendientes) al momento del relevamiento.

## Estructura del repositorio

```
bacheo-grinor-2026/
├── README.md
├── data/
│   ├── resumen_mensual_2026.csv        # Totales y acumulados por mes
│   ├── detalle_por_calle_2026.csv      # Detalle mes a mes por calle (formato largo)
│   └── acumulado_por_calle_2026.csv    # m² y baches acumulados por calle (ene-ago)
└── scripts/
    └── generar_grafico_tendencia.py    # Regenera el gráfico de tendencia mensual
```

## Datos

- **resumen_mensual_2026.csv**: una fila por mes, con baches y m² del mes y
  acumulados desde el inicio de la obra.
- **detalle_por_calle_2026.csv**: una fila por calle y mes, con cantidad de
  baches, m², toneladas de asfalto estimadas y % que representa dentro del mes.
- **acumulado_por_calle_2026.csv**: totales acumulados (ene–ago 2026) por
  calle, calculados a partir del detalle mensual.

## Regenerar el gráfico de tendencia

```bash
pip install matplotlib
python scripts/generar_grafico_tendencia.py
```

Esto genera `data/tendencia_m2_mensual.png` con la evolución mensual de m²
bacheados.

## Fuente

Datos extraídos de la planilla de obra `BACHEO_GRINOR_2026.xls` y del informe
mensual detallado en PDF (Enero–Agosto 2026).
