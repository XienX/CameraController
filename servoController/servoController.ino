#include <Servo.h>
//#include <Keyboard.h>

Servo hServo;  // 水平旋转舵机
Servo vServo;  // 竖直旋转舵机
int hPos = 90;
int vPos = 90;

void setup() {
  hServo.attach(3);
  vServo.attach(9);
  
  hServo.write(hPos);
  vServo.write(hPos);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char inChar = Serial.read();

    switch(inChar) {
      case '4':  // 左
        if(hPos <= 175) {
          hPos += 5;
          hServo.write(hPos);
        }

        break;
      case '6':  // 右
        if(hPos >= 5) {
          hPos -= 5;
          hServo.write(hPos);
        }
        break;
      case '8':  // 上
        if(vPos <= 175) {
          vPos += 5;
          vServo.write(vPos);
        }
        break;
      case '2':  // 下
        if(vPos >= 5) {
          vPos -= 5;
          vServo.write(vPos);
        }
        break;
    }
  }
  delay(100);
}
