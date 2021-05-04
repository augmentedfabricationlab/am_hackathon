/*
  Arduino motor control functions for extruder control 
  created on 22.02.2021
*/

void motor_setup() {
  motor.setMaxSpeed(motordata.motor_maxspeed);
  motor.setSpeed(motordata.motor_speed);
  motor.setAcceleration(motordata.motor_acceleration);
  Serial.println("Motor setup executed");
}

void check_motor() {
  if (motordata.motor_state == 1) { 
    motor.runSpeedToPosition();
    if (motor_move_chrono.hasPassed(1000)) {
      motor_move_chrono.restart();
      motor.moveTo(motor.currentPosition()+motordata.motor_speed*2);
    }
    if (motor_state_print.hasPassed(10000)) {
      motor_state_print.restart();
      Serial.println("Motor is running...");
    }
  }
  else {
    motor.stop();
  }
}
