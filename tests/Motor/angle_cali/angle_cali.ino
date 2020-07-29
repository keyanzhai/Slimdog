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
// Servo 0: 160 (0 degree) - 400 (90 degree) - 640 (180 degree)
// Servo 1: 110 (0 degree) - 370 (90 degree) - 630 (180 degree)
// Servo 2: 130 (0 degree) - 385 (90 degree) - 640 (180 degree)
// Servo 3: /

// RB
// Servo 4: 155 (0 degree) - 405 (90 degree) - 655 (180 degree)
// Servo 5: 120 (0 degree) - 385 (90 degree) - 650 (180 degree)
// Servo 6: 130 (0 degree) - 390 (90 degree) - 650 (180 degree)
// Servo 7: /

// LF
// Servo 8: 145 (0 degree) - 390 (90 degree) - 635 (180 degree)
// Servo 9: 155 (0 degree) - 415 (90 degree) - 675 (180 degree)
// Servo 10: 140 (0 degree) - 390 (90 degree) - 640 (180 degree)
// Servo 11: /

// LB
// Servo 12: 145 (0 degree) - 395 (90 degree) - 645 (180 degree)
// Servo 13: 125 (0 degree) - 375 (90 degree) - 625 (180 degree)
// Servo 14: 125 (0 degree) - 380 (90 degree) - 635 (180 degree)
// Servo 15: /

void setup() {
  Serial.begin(9600); // Sets the data rate in bits per second (baud) for serial data transmission
  Serial.println("16 channel servo test!");
  
  pwm.begin();
  pwm.setPWMFreq(60); // Analog servos run at ~60 Hz updates

  // Print the servo being tested
  Serial.print("servonum = ");
  Serial.println(servonum);

  int angle = 90;
//  
//  pwm.setPWM(0, 0, angletoPWM(angle, 0));
//  pwm.setPWM(1, 0, angletoPWM(angle, 1));
//  pwm.setPWM(2, 0, angletoPWM(angle, 2));
//
//  pwm.setPWM(4, 0, angletoPWM(angle, 4));
//  pwm.setPWM(5, 0, angletoPWM(angle, 5));
//  pwm.setPWM(6, 0, angletoPWM(angle, 6));
//
//  pwm.setPWM(8, 0, angletoPWM(angle, 8));
  pwm.setPWM(9, 0, 405);
//  pwm.setPWM(10, 0, angletoPWM(angle, 10));
//
//  pwm.setPWM(12, 0, angletoPWM(angle, 12));
//  pwm.setPWM(13, 0, angletoPWM(angle, 13));
//  pwm.setPWM(14, 0, angletoPWM(angle, 14));
//  
}

void loop() {

}

int angletoPWM(int ang, int servonum) {
  int pulse;
  
  if (servonum == 0)
    pulse = map(ang, 0, 180, 160, 640); // map the angle into the PWM

  else if (servonum == 1)
    pulse = map(ang, 0, 180, 110, 630); // map the angle into the PWM

  else if (servonum == 2)
    pulse = map(ang, 0, 180, 130, 640); // map the angle into the PWM

  else if (servonum == 4)
    pulse = map(ang, 0, 180, 155, 655); // map the angle into the PWM

  else if (servonum == 5)
    pulse = map(ang, 0, 180, 120, 650); // map the angle into the PWM

  else if (servonum == 6)
    pulse = map(ang, 0, 180, 130, 650); // map the angle into the PWM

  else if (servonum == 8)
    pulse = map(ang, 0, 180, 145, 635); // map the angle into the PWM

  else if (servonum == 9)
    pulse = map(ang, 0, 180, 155, 675); // map the angle into the PWM

  else if (servonum == 10)
    pulse = map(ang, 0, 180, 140, 640); // map the angle into the PWM

  else if (servonum == 12)
    pulse = map(ang, 0, 180, 145, 645); // map the angle into the PWM

  else if (servonum == 13)
    pulse = map(ang, 0, 180, 125, 625); // map the angle into the PWM

  else if (servonum == 14)
    pulse = map(ang, 0, 180, 125, 635); // map the angle into the PWM

  else
    pulse = map(ang, 0, 180, SERVOMIN, SERVOMAX); // map the angle into the PWM
       
  return pulse;
}
