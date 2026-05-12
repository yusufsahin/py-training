from pathlib import Path
import struct

# Dosya yolu
current_dir = Path(__file__).parent
file_path = current_dir / "sensor_data.bin"

# Örnek veri
sensor_id = 12          # unsigned short -> 2 byte
temperature = 23.75     # float -> 4 byte
status = 1              # unsigned char -> 1 byte

# Binary format:
# H = unsigned short, 2 byte
# f = float, 4 byte
# B = unsigned char, 1 byte
format_type = "HfB"

# Veriyi binary olarak paketle
binary_data = struct.pack(format_type, sensor_id, temperature, status)

# Binary dosyaya yaz
with open(file_path, "wb") as file:
    file.write(binary_data)

print("Binary veri yazıldı:", binary_data)
print("Dosya boyutu:", file_path.stat().st_size, "byte")


# Binary dosyadan oku
with open(file_path, "rb") as file:
    read_data = file.read()

# Binary veriyi tekrar Python değerlerine çevir
read_sensor_id, read_temperature, read_status = struct.unpack(format_type, read_data)

print("Okunan sensor_id:", read_sensor_id)
print("Okunan temperature:", read_temperature)
print("Okunan status:", read_status)