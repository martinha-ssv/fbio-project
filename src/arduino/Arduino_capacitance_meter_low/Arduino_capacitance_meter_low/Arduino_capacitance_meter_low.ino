
#include <Wire.h>

#define analogPin      0          
#define chargePin      2         
#define dischargePin   8        
#define resistorValue  10000.0F  //Remember, we've used a 10K resistor to charge the capacitor

unsigned long startTime;
unsigned long elapsedTime;
float microFarads;                
float nanoFarads;
unsigned long startDischargingTime;
unsigned long elapsedDischargingTime;

void setup(){
  pinMode(chargePin, OUTPUT);     
  digitalWrite(chargePin, LOW); 
  Serial.begin(31250);
}

void loop(){

  // STARTS CHARGING THE CAPACITOR
  startTime = micros();
  digitalWrite(chargePin, HIGH);
  while(analogRead(analogPin) < 648){  // 648 is ≈0.632 of the total scale, the maximum 5V, which the capacitor will eventually hold -> value of RC constant     
  Serial.println("Charging");
  //Serial.println(analogRead(analogPin));
  //delay(100);
  }
   
    // this pin charges capacitor by being set to HIGH (≈5V for 5V Vcc)
  
  
  //Serial.println(analogRead(analogPin));
  elapsedTime= micros() - startTime; // RC constant
  Serial.print("CHARGING TOOK "); Serial.print(elapsedTime); Serial.println("us");
  microFarads = ((float)elapsedTime /resistorValue) ;
  nanoFarads = microFarads * 1000.0; 
  
  Serial.print(nanoFarads); Serial.println(" nF");
  delay(100);
  digitalWrite(chargePin, LOW);            
  startDischargingTime = micros();
  while(analogRead(analogPin) > 0){   
    Serial.println("Discharging");   
  }//This while waits till the capacitor is discharged
  elapsedDischargingTime = micros()-startDischargingTime;

  pinMode(dischargePin, INPUT);      //this sets the pin to high impedance
  
  Serial.println("DISCHARGING TOOK "+String(elapsedDischargingTime)+"us");
  
  
  
}
