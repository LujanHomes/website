import sys, glob, os
from faster_whisper import WhisperModel

carpeta = os.path.dirname(os.path.abspath(__file__))
audios = sorted(glob.glob(os.path.join(carpeta, "**", "*.opus"), recursive=True))

print(f"Cargando modelo (small)...", flush=True)
model = WhisperModel("small", device="cpu", compute_type="int8")

salida = os.path.join(carpeta, "transcripciones.txt")
with open(salida, "w", encoding="utf-8") as f:
    for a in audios:
        nombre = os.path.basename(a)
        print(f"Transcribiendo {nombre}...", flush=True)
        segments, info = model.transcribe(a, language="es")
        texto = " ".join(s.text.strip() for s in segments)
        f.write(f"=== {nombre} ===\n{texto}\n\n")
        print(f"  -> {texto[:80]}...", flush=True)

print(f"\nListo. Guardado en: {salida}", flush=True)
