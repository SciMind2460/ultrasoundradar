#include "Servo.h"

const int TRIG_PIN = 6;
const int ECHO_PIN = 7;
const int SERVO_PIN = 9;
float duration, distance;

void setup() {
  // put your setup code here, to run once:
  servo.attach(9);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  Serial.begin(9600); // Communication method with Python program
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int angle = 0; angle < 180; angle += 1) {
    servo.write(angle);
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    duration = pulseIn(ECHO_PIN, HIGH);
    distance = (duration * 0.034) / 2
    Serial.print(angle);
    Serial.print(',');
    Serial.println(distance);
  }
  for (int angle = 180; angle < 0; angle -= 1) {
    servo.write(angle);
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    duration = pulseIn(ECHO_PIN, HIGH);
    distance = (duration * 0.034) / 2
    Serial.print(angle);
    Serial.print(',');
    Serial.println(distance);
  }
}
