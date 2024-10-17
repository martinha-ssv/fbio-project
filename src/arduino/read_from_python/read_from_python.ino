const int chargePin = 2;  // Pin to control (e.g., built-in LED)
const int 

void setup() {
  Serial.begin(19200);  // Initialize serial communication at 9600 bps
  pinMode(chargePin, OUTPUT);  // Set the pin as output
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();  // Read the incoming byte

    if (command == 'H') {
      digitalWrite(chargePin, HIGH);  // Set pin to HIGH
    } else if (command == 'L') {
      digitalWrite(chargePin, LOW);  // Set pin to LOW
    }
  }
}