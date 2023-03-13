#include <DHT.h>

#define DHTPIN 8
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
uint8_t T; 

void setup() {
  Serial.begin(9600);
  dht.begin();

}

void loop() {
  T = dht.readTemperature();
  Serial.write(T);  
  delay(1000);
}
