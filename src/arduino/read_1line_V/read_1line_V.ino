#define analogPin 0

float V = 0;
int digitalV = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalV = analogRead(analogPin);
  V = 5*digitalV/1023;
  Serial.println(V);
}
