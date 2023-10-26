#include <Arduino.h>
#include <microDS18B20.h>

MicroDS18B20<2> sensor;
int tmr;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if(millis() - tmr > 1000){
    sensor.requestTemp();
    if(sensor.readTemp()) Serial.println(sensor.getTemp());
    tmr=millis();
  }
}