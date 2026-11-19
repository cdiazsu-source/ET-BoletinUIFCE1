"""Exporta las láminas de Instagram (1080×1350) de una edición a PNG con Edge headless.

Uso (desde la raíz del repo):
    python herramientas/exportar_ig.py            # edición 01, paleta original
    python herramientas/exportar_ig.py 01 c       # edición 01, Propuesta C

Salida: instagram/edicion-NN/ig-01.png … y instagram/edicion-NN.zip
(con paleta: instagram/edicion-NN-p<c>/ y instagram/edicion-NN-p<c>.zip).
"""
import os
import re
import subprocess
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
EDGE = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]


def main():
    ed = sys.argv[1] if len(sys.argv) > 1 else "01"
    pal = sys.argv[2] if len(sys.argv) > 2 else ""
    html = RAIZ / f"edicion-{ed}-ig.html"
    total = len(re.findall(r'<section class="ig"', html.read_text(encoding="utf-8")))
    edge = next(p for p in EDGE if os.path.exists(p))
    nombre = f"edicion-{ed}" + (f"-p{pal}" if pal else "")
    out = RAIZ / "instagram" / nombre
    out.mkdir(parents=True, exist_ok=True)
    url = html.as_uri()
    for n in range(1, total + 1):
        png = out / f"ig-{n:02d}.png"
        hash_ = f"#solo={n}" + (f"&p={pal}" if pal else "")
        subprocess.run([edge, "--headless", "--disable-gpu", "--hide-scrollbars",
                        "--force-device-scale-factor=1", "--virtual-time-budget=5000",
                        "--window-size=1080,1350", f"--screenshot={png}", url + hash_],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("ok", png.relative_to(RAIZ))
    with zipfile.ZipFile(RAIZ / "instagram" / f"{nombre}.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for png in sorted(out.glob("ig-*.png")):
            z.write(png, png.name)
    print("zip", f"instagram/{nombre}.zip")


if __name__ == "__main__":
    main()
