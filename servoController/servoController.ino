#include <Servo.h>
//#include <Keyboard.h>

Servo hServo;  // 水平旋转舵机
Servo vServo;  // 竖直旋转舵机
int hPos = 90;
int vPos = 45;

void setup() {
  hServo.attach(3);
  vServo.attach(9);

  Serial.begin(9600);
//  Keyboard.begin();
}

void loop() {
  int pos = 180;
//  for(; pos < 175; pos += 5){
//    hServo.write(pos);
//    delay(100);
//    vServo.write(pos);
//    delay(1500);
//  }
//                               
//  for(; pos>=5; pos-=5) {
//    hServo.write(pos);
//    delay(100);
//    vServo.write(pos);
//    delay(1500);
//  }

  if (Serial.available() > 0) {
    // read incoming serial data:
    char inChar = Serial.read();
    hServo.write(pos);
  }
}
