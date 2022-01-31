#include <Wire.h>

void setup() {
  Serial.begin(9600);
  //setting up pins
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(4, INPUT);
  pinMode(5, INPUT);
  pinMode(13, OUTPUT);
}

void loop() {
  //transmit letters for directional movement
  //Right
  if (digitalRead(2) == HIGH) {
    Serial.println("R");
    Serial.println();
  }
  //Up
  if (digitalRead(3) == HIGH) {
    Serial.println("U");
    Serial.println();
  }
  //Down
  if (digitalRead(4) == HIGH) {
    Serial.println("D");
    Serial.println();
  }
  //Left
  if (digitalRead(5) == HIGH) {
    Serial.println("L");
    Serial.println();
  }

}
