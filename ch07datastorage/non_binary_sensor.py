from pathlib import Path

# Dosya yolu
current_dir = Path(__file__).parent
file_path = current_dir / "sensor_data.txt"

# Örnek veri
sensor_id = 12
temperature = 23.75
status = 1

# Metin dosyasına yaz
with open(file_path, "w", encoding="utf-8") as file:
    file.write(f"sensor_id={sensor_id}\n")
    file.write(f"temperature={temperature}\n")
    file.write(f"status={status}\n")

print("Veri text olarak yazıldı.")
print("Dosya boyutu:", file_path.stat().st_size, "byte")