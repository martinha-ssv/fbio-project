const int n_vertical = 1;
const int n_horizontal = 1;
const int verticalPins[n_vertical] = {3}; // Digital pins for vertical strips
const int horizontalPins[n_horizontal] = {A0}; // Analog pins for horizontal strips
const int V_IN = 5.0;

const int vCoordsDisp[] = {0};
const int hCoordsDisp[] = {1};

void setup() {
  Serial.begin(19200);
  
  // Set vertical pins as outputs
  for (int i = 0; i < n_vertical; i++) {
    pinMode(verticalPins[i], OUTPUT);
    digitalWrite(verticalPins[i], LOW); // Initialize to low
  }

  // Set horizontal pins as inputs
  for (int i = 0; i < n_horizontal; i++) {
    pinMode(horizontalPins[i], INPUT);
  }
}

void loop() {
  for (int x = 0; x < n_vertical; x++) {
    // Activate the corresponding vertical strip
    int x_pin = verticalPins[x];
    digitalWrite(x_pin, HIGH);

    for (int y = 0; y < n_horizontal; y++) {
      // Read the analog value from the corresponding horizontal strip
      int y_pin = horizontalPins[y];
      int sensorValue = analogRead(y_pin);
      // Convert the analog reading to a voltage
      float voltage = sensorValue * (V_IN / 1023.0);

      // Print the sensor value
      //Serial.print("x: ");
        Serial.print(x);
        Serial.print(",");
        //Serial.print(", y: ");
        Serial.print(y);
        Serial.print(",");
        //Serial.print(", voltage: ");
        Serial.println(voltage);
    }

    // Deactivate the vertical strip
    digitalWrite(verticalPins[x], LOW);
  }

  delay(10);  // Small delay to make the output readable
}

bool isInArray(int arr[], int size, int value) {
    for (int i = 0; i < size; ++i) {
        if (arr[i] == value) {
            return true;
        }
    }
    return false;
}
