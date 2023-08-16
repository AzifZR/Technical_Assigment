import Adafruit_DHT
import time

# Menentukan jenis sensor DHT (DHT22) dan nomor pin GPIO
sensor = Adafruit_DHT.DHT22
pin = 4  # Ubah sesuai nomor pin GPIO yang Anda gunakan

try:
    while True:
        # Membaca data dari sensor
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        # Jika pembacaan data berhasil
        if humidity is not None and temperature is not None:
            print(f"Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%")
        else:
            print("Failed to retrieve data from sensor")

        time.sleep(2)  # Menunda pembacaan selama 2 detik

except KeyboardInterrupt:
    print("Program dihentikan oleh pengguna")
