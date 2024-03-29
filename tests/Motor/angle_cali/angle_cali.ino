#include <Wire.h> // Used for I2C
#include <Adafruit_PWMServoDriver.h> // Used for the PCA9685
#include <Servo.h>

// Might need to define SERVOMIN and SERVOMAX for each of the 12 servos
#define SERVOMIN 110 // minimum pulse length count
#define SERVOMAX 620 // maximum  pulse length count

// The pwm object
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

Servo servoTest;

// Servo number
//     G   Y   O   /
// RF: 0,  1,  2,  3
// RB: 4,  5,  6,  7
// LF: 8,  9,  10, 11
// LB: 12, 13, 14, 15
uint8_t servonum = 15;

// Calibration:

// RF
// Servo 0: 135 (0 degree) - 405 (90 degree) - 675 (180 degree)
// Servo 1: 110 (0 degree) - 395 (90 degree) - 680 (180 degree)
// Servo 2: 180 (0 degree) - 420 (90 degree) - 660 (180 degree)
// Servo 3: /

// RB
// Servo 4: 130 (0 degree) - 400 (90 degree) - 670 (180 degree)
// Servo 5: 95 (0 degree) - 330 (90 degree) - 565 (180 degree)
// Servo 6: 84 (0 degree) - 360 (90 degree) - 636 (180 degree)
// Servo 7: /

// LF
// Servo 8: 80 (0 degree) - 380 (90 degree) - 680 (180 degree)
// Servo 9: 325 (0 degree) - 565 (90 degree) - 805 (180 degree)
// Servo 10: 150 (0 degree) - 390 (90 degree) - 630 (180 degree)
// Servo 11: /

// LB
// Servo 12: 135 (0 degree) - 395 (90 degree) - 655 (180 degree)
// Servo 13: -50 (0 degree) - 230 (90 degree) - 510 (180 degree)
// Servo 14: 120 (0 degree) - 380 (90 degree) - 640 (180 degree)
// Servo 15: /

void setup() {
//  Serial.begin(9600); // Sets the data rate in bits per second (baud) for serial data transmission
//  Serial.println("16 channel servo test!");
  
  pwm.begin();
  pwm.setPWMFreq(60); // Analog servos run at ~60 Hz updates

  // Print the servo being tested
//  Serial.print("servonum = ");
//  Serial.println(servonum);

  int angle = 60;
//  
//
//  pwm.setPWM(4, 0, 580); // 220 top , 400 horizontal (90), 310 (60), 580 bottom     220 - 400 - 580(tallest)
//  pwm.setPWM(5, 0, 330); // 330 vertical to the ground, 400 out30, 200 in45           110 - 330 - 470(outermost / rightmost)
//  pwm.setPWM(6, 0, 345); // 345 verticle to the ground, 220 (45 to the back), 480 (45 to the front)   110 - 345 - ~590 (frontmost)
//
//  pwm.setPWM(8, 0, 250); // 380 horizontal (90), ~140 tallest, ~550 shortest (~45 degree to up),  250 45 degree to down)  140 - 380 - 550
//  pwm.setPWM(9, 0, 560); // 680 (outermost / leftmost), 565 vertical, 640 (30 to out), 480 (30 to in), 280 (innermost) 280 - 565 - 
//  pwm.setPWM(10, 0, 390); // 390 vertical, 310 (30 to front), 470 (30 to back), 140 towards front, 660 toward back
//
//  pwm.setPWM(12, 0, 560); // 395 horizontal, 265 (45 to down), ~160 tallest, 560 shortest
//  pwm.setPWM(13, 0, 230); // 160 outmost / leftmost, 230 vertical, 370 (45 to in), 460 innermost
//  pwm.setPWM(14, 0, 250); // 380 vertical, 250 (45 to front), 510 (45 to back), 150 towards front (might hit LF leg), 650 toward back
//  
//  pwm.setPWM(0, 0, 405);
//  
//  pwm.setPWM(1, 0, angletoPWM(angle, 1));
//  
//  pwm.setPWM(2, 0, 300);
//  
  pwm.setPWM(4, 0, 30);
//  pwm.setPWM(5, 0, angletoPWM(angle, 5));
//  pwm.setPWM(6, 0, angletoPWM(angle, 6));
//
//  pwm.setPWM(8, 0, angletoPWM(angle, 8));
//  pwm.setPWM(9, 0, angletoPWM(angle, 9));
//  pwm.setPWM(10, 0, angletoPWM(angle, 10));
//
//  pwm.setPWM(12, 0, angletoPWM(angle, 12));
//  pwm.setPWM(13, 0, angletoPWM(angle, 13));
//  pwm.setPWM(14, 0, angletoPWM(angle, 14));
}

void loop() {

}

int angletoPWM(int ang, int servonum) {
  int pulse;
  
  if (servonum == 0)
    pulse = map(ang, 0, 180, 135, 675); // map the angle into the PWM

  else if (servonum == 1)
    pulse = map(ang, 0, 180, 110, 680); // map the angle into the PWM

  else if (servonum == 2)
    pulse = map(ang, 0, 180, 180, 660); // map the angle into the PWM

  else if (servonum == 4)
    pulse = map(ang, 0, 180, 130, 670); // map the angle into the PWM

  else if (servonum == 5)
    pulse = map(ang, 0, 180, 95, 565); // map the angle into the PWM

  else if (servonum == 6)
    pulse = map(ang, 0, 180, 84, 636); // map the angle into the PWM

  else if (servonum == 8)
    pulse = map(ang, 0, 180, 80, 680); // map the angle into the PWM

  else if (servonum == 9)
    pulse = map(ang, 0, 180, 325, 805); // map the angle into the PWM

  else if (servonum == 10)
    pulse = map(ang, 0, 180, 150, 630); // map the angle into the PWM

  else if (servonum == 12)
    pulse = map(ang, 0, 180, 135, 655); // map the angle into the PWM

  else if (servonum == 13)
    pulse = map(ang, 0, 180, -50, 510); // map the angle into the PWM

  else if (servonum == 14)
    pulse = map(ang, 0, 180, 120, 640); // map the angle into the PWM

  else
    pulse = map(ang, 0, 180, SERVOMIN, SERVOMAX); // map the angle into the PWM
       
  return pulse;
}
