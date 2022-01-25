#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_BusIO_Register.h>
#include <Adafruit_I2CDevice.h>
#include <Adafruit_I2CRegister.h>
#include <Adafruit_SPIDevice.h>
#include <pyduino_bridge.h>

Adafruit_MPU6050 mpu;

void setup() {
  Serial.begin(115200);
  pinMode(2, HIGH);
  pinMode(3, HIGH);
  pinMode(4, HIGH);
  pinMode(5, HIGH);
  pinMode(2, HIGH);

  // set accelerometer range to +-8G
  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);

  // set gyro range to +- 500 deg/s
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);

  // set filter bandwidth to 21 Hz
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

}

void loop() {
//  Serial.println("Check");
//  delay(10);


  //transmit letters for directional movement
  //Up
  while (digitalRead(2) == HIGH) {
    Serial.println("U");
    Serial.println();
    delay(10);

  }
  //Down
  while (digitalRead(3) == HIGH) {
    Serial.println("D");
    Serial.println();
    delay(10);

  }
  //Left
  while (digitalRead(4) == HIGH) {
    Serial.println("L");
    Serial.println();
    delay(10);
  }
  //Right
  while (digitalRead(5) == HIGH) {
    Serial.println("R");
    Serial.println();
    delay(10);
  }
//  //gyroscope sensor for boost
//  sensors_event_t a, g, temp;
//  mpu.getEvent(&a, &g, &temp);
//
//  if (a.acceleration.x >= 1 || a.acceleration.y >= 1 || a.acceleration.z >= 1) {
//    Serial.println("B");
//    Serial.println();
//    delay(100);
//  }
}
