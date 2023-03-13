uint8_t Data; 

void setup() {
  Serial.begin(9600);
  randomSeed(300);

}

void loop() {
  Data = random(30);
  Serial.write(Data);
  delay(2000);
}
