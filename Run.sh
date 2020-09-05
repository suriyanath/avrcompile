./arduino-cli core install arduino:avr
./arduino-cli lib install LiquidCrystal
./arduino-cli lib install Servo
export FLASK_APP=app.py
flask run --host 0.0.0.0