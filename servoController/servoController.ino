#include <Servo.h>
//#include <Keyboard.h>

Servo hServo;  // 水平旋转舵机
Servo vServo;  // 竖直旋转舵机
int hPos = 90;
int vPos = 90;

void setup() {
  hServo.attach(3);
  vServo.attach(9);
  
//  hServo.write(hPos);
//  vServo.write(hPos);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char inChar = Serial.read();

    switch(inChar) {
      case '4':  // 左
        if(hPos <= 177) {
          hPos += 3;
          hServo.write(hPos);
        }

        break;
      case '6':  // 右
        if(hPos >= 3) {
          hPos -= 3;
          hServo.write(hPos);
        }
        break;
      case '8':  // 上
        if(vPos <= 177) {
          vPos += 3;
          vServo.write(vPos);
        }
        break;
      case '2':  // 下
        if(vPos >= 3) {
          vPos -= 3;
          vServo.write(vPos);
        }
        break;
    }
  }
  delay(100);
}
