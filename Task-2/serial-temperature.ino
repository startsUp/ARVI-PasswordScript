#include <dht.h>

dht DHT; //initialize

#define DHT11_PIN 7 //recieve data on pin 7

void setup(){
  Serial.begin(9600); //send data (for python) on port 9600
}

void loop()
{
  int chk = DHT.read11(DHT11_PIN);
  Serial.print("Temperature = ");
  Serial.println(DHT.temperature);
  Serial.print("Humidity = ");
  Serial.println(DHT.humidity);
  delay(1000);
}
