import os
import subprocess

# Define output directory
out_dir = "/home/emers/Universidad/lineas-de-transmision/entregables/tareas/distancias-seguridad"
os.makedirs(out_dir, exist_ok=True)

html_path = os.path.join(out_dir, "distancias_seguridad.xls")
ods_path = os.path.join(out_dir, "distancias_seguridad.ods")

html_content = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
    body { font-family: 'Segoe UI', Arial, sans-serif; background-color: #ffffff; }
    h1 { color: #1F4E79; font-size: 16pt; margin-bottom: 5px; }
    h2 { color: #2E75B6; font-size: 12pt; margin-top: 20px; margin-bottom: 5px; border-bottom: 2px solid #2E75B6; padding-bottom: 3px; }
    .subtitle { color: #595959; font-size: 10pt; font-style: italic; margin-bottom: 15px; }
    table { border-collapse: collapse; margin-bottom: 15px; font-size: 10pt; width: 100%; max-width: 800px; }
    th { background-color: #1F4E79; color: #ffffff; font-weight: bold; border: 1px solid #D3D3D3; padding: 6px 10px; text-align: center; }
    td { border: 1px solid #D3D3D3; padding: 6px 10px; }
    .text-left { text-align: left; }
    .text-center { text-align: center; }
    .text-right { text-align: right; }
    .bg-header { background-color: #D9E1F2; font-weight: bold; }
    .bg-accent { background-color: #F2F2F2; }
    .bg-input { background-color: #E2EFDA; } /* Green background for inputs */
    .bg-result { background-color: #FCE4D6; font-weight: bold; color: #C65911; } /* Orange background for results */
    .formula { font-weight: bold; color: #1F4E79; }
</style>
</head>
<body>

<h1>CÁLCULO DE DISTANCIAS DE SEGURIDAD EN LÍNEAS DE ALTA TENSIÓN</h1>
<div class="subtitle">Normativa de Referencia: Reglamento sobre condiciones técnicas y garantías de seguridad en líneas eléctricas de alta tensión (RD 223/2008 - España / UCV)</div>

<h2>1. Coeficiente K según el Ángulo de Oscilación (Tabla 16 - ITC-LAT 07)</h2>
<table>
    <tr>
        <th>Ángulo de oscilación (&alpha;)</th>
        <th>Líneas de tensión nominal superior a 30 kV (K)</th>
        <th>Líneas de tensión nominal igual o inferior a 30 kV (K)</th>
    </tr>
    <tr>
        <td class="text-left">&alpha; &gt; 65°</td>
        <td class="text-center">0.70</td>
        <td class="text-center">0.65</td>
    </tr>
    <tr>
        <td class="text-left">40° &le; &alpha; &le; 65°</td>
        <td class="text-center">0.65</td>
        <td class="text-center">0.60</td>
    </tr>
    <tr>
        <td class="text-left">&alpha; &lt; 40°</td>
        <td class="text-center">0.60</td>
        <td class="text-center">0.55</td>
    </tr>
</table>

<h2>2. Distancias de Aislamiento Eléctrico (Tabla 15 - ITC-LAT 07)</h2>
<table>
    <tr>
        <th>Tensión más elevada de la red U<sub>s</sub> [kV]</th>
        <th>Distancia básica Del [m]</th>
        <th>Distancia básica Dpp [m]</th>
    </tr>
    <tr class="bg-accent">
        <td class="text-center">3.6</td>
        <td class="text-center">0.08</td>
        <td class="text-center">0.10</td>
    </tr>
    <tr>
        <td class="text-center">7.2</td>
        <td class="text-center">0.09</td>
        <td class="text-center">0.10</td>
    </tr>
    <tr class="bg-accent">
        <td class="text-center">12.0</td>
        <td class="text-center">0.12</td>
        <td class="text-center">0.15</td>
    </tr>
    <tr>
        <td class="text-center">17.5</td>
        <td class="text-center">0.16</td>
        <td class="text-center">0.20</td>
    </tr>
    <tr class="bg-accent">
        <td class="text-center">24.0</td>
        <td class="text-center">0.22</td>
        <td class="text-center">0.25</td>
    </tr>
    <tr>
        <td class="text-center">30.0</td>
        <td class="text-center">0.27</td>
        <td class="text-center">0.33</td>
    </tr>
    <tr class="bg-accent">
        <td class="text-center">36.0</td>
        <td class="text-center">0.35</td>
        <td class="text-center">0.40</td>
    </tr>
    <tr>
        <td class="text-center">52.0</td>
        <td class="text-center">0.60</td>
        <td class="text-center">0.70</td>
    </tr>
    <tr class="bg-accent">
        <td class="text-center">72.5</td>
        <td class="text-center">0.70</td>
        <td class="text-center">0.80</td>
    </tr>
    <tr>
        <td class="text-center">123.0</td>
        <td class="text-center">1.00</td>
        <td class="text-center">1.15</td>
    </tr>
    <tr class="bg-accent">
        <td class="text-center">145.0</td>
        <td class="text-center">1.20</td>
        <td class="text-center">1.40</td>
    </tr>
    <tr>
        <td class="text-center">170.0</td>
        <td class="text-center">1.30</td>
        <td class="text-center">1.50</td>
    </tr>
    <tr class="bg-accent">
        <td class="text-center">245.0</td>
        <td class="text-center">1.70</td>
        <td class="text-center">2.00</td>
    </tr>
    <tr>
        <td class="text-center">420.0</td>
        <td class="text-center">2.80</td>
        <td class="text-center">3.20</td>
    </tr>
</table>

<h2>3. Calculadora de Separación Mínima entre Conductores de Fase</h2>
<p class="subtitle">Ecuación: D = K * &radic;(F + L) + K' * Dpp</p>
<table>
    <tr>
        <th colspan="3">Entrada de Parámetros</th>
    </tr>
    <tr>
        <td class="bg-header">Tensión Nominal de la Línea (U<sub>n</sub>) [kV]</td>
        <td class="bg-input text-right">115</td>
        <td>Ingrese la tensión nominal de operación de la línea.</td>
    </tr>
    <tr>
        <td class="bg-header">Ángulo de Oscilación (&alpha;) [°]</td>
        <td class="bg-input text-right">45</td>
        <td>Ingrese el ángulo de oscilación del conductor.</td>
    </tr>
    <tr>
        <td class="bg-header">Flecha Máxima (F) [m]</td>
        <td class="bg-input text-right">6.5</td>
        <td>Ingrese la flecha máxima del vano.</td>
    </tr>
    <tr>
        <td class="bg-header">Longitud de la Cadena de Suspensión (L) [m]</td>
        <td class="bg-input text-right">1.5</td>
        <td>Ingrese la longitud de la cadena (0 para amarre/rígidos).</td>
    </tr>
    <tr>
        <td class="bg-header">Categoría Especial (1 = Sí, 0 = No)</td>
        <td class="bg-input text-right">0</td>
        <td>1 para Categoría Especial, 0 para resto de líneas.</td>
    </tr>
    <tr>
        <td class="bg-header">Distancia de Aislamiento (Dpp) [m]</td>
        <td class="bg-input text-right">1.15</td>
        <td>Distancia básica según Tabla 15 (para 115/123 kV Dpp=1.15 m).</td>
    </tr>
    <tr class="bg-header">
        <th colspan="3">Cálculos Intermedios y Resultado</th>
    </tr>
    <tr>
        <td class="bg-header">Coeficiente K' (Tensión)</td>
        <td class="bg-result text-right">=IF(B39=1,0.85,0.75)</td>
        <td>K' = 0.85 para Categoría Especial; K' = 0.75 para el resto.</td>
    </tr>
    <tr>
        <td class="bg-header">Coeficiente K (Oscilación)</td>
        <td class="bg-result text-right">=IF(B36&gt;65,IF(B35&gt;30,0.7,0.65),IF(B36&gt;=40,IF(B35&gt;30,0.65,0.6),IF(B35&gt;30,0.6,0.55)))</td>
        <td>K determinado dinámicamente según la Tabla 16 en base a U<sub>n</sub> y &alpha;.</td>
    </tr>
    <tr class="bg-result">
        <td>Separación Mínima Requerida D [m]</td>
        <td class="text-right">=B43*SQRT(B37+B38)+B42*B40</td>
        <td>Separación mínima calculada según la fórmula reglamentaria.</td>
    </tr>
</table>

</body>
</html>
"""

# Note: The cell references B40-B47 correspond to the exact row indices in LibreOffice Calc layout:
# Row 1: empty/header
# Row 2: Title
# Row 3: subtitle
# Row 4: empty
# Row 5: Section 1 header
# Row 6-9: Table 16 (4 rows)
# Row 10: empty
# Row 11: Section 2 header
# Row 12-27: Table 15 (16 rows)
# Row 28: empty
# Row 29: Section 3 header
# Row 30: subtitle
# Row 31: Input header
# Row 32: Un (B32) -> B40 in formula? Wait, let's calculate exact row numbers!
# Let's count rows in HTML:
# Row 1: h1 (Cálculo de...)
# Row 2: subtitle
# Row 3: h2 (1. Coeficiente K...)
# Row 4-8: Table 16 (5 rows, header + 3 rows + empty) -> wait, tables are inlined.
# Let's write the file and let libreoffice convert it. Then we can inspect the rows using Python to write the exact row indices, or let's use a simpler layout or name our inputs with cells.
# Let's count the rows that LibreOffice Calc will generate.
# Let's write the HTML with named formulas or simple row indexes and inspect it.
# Actually, let's write a python script to inspect the generated ODS using zipfile or write content.xml directly, which is 100% robust.
# But wait, using LibreOffice's convert-to is very clean. Let's make sure the row numbers are exact.
# Let's write the script to write the HTML, run conversion, and check.

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML escrito en {html_path}")

# Convert using libreoffice
cmd = ["libreoffice", "--headless", "--convert-to", "ods", "--outdir", out_dir, html_path]
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0:
    print(f"ODS generado con éxito en {ods_path}")
else:
    print("Error al convertir a ODS:")
    print(res.stderr)
