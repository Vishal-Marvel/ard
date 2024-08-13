void setup() {
  Serial.begin(9600);
}

int previousState = 0;

void loop() {
  int adc = analogRead(A0);
  float voltage = adc * 5 / 1023.0;
  float current = (voltage - 2.5) / 0.185;
  // Serial.println(current);
  int currentState = current > 0.15 ? 1 : 0;

  // if (currentState != previousState) {
    Serial.println(currentState ? "1" : "0");
    
    // previousState = currentState;
  // }

delay(300);
}