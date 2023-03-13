
int incomingByte = 0, st_flag = 2, Pin_Led = 8;

void setup() {
  Serial.begin(9600);
  pinMode(Pin_Led, OUTPUT);
}

void loop() {

  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    //42 en ASCII es B 
    if (incomingByte == 0x42){
      st_flag = 1;
    }
    //4C en ASCII es L
    else if(incomingByte == 0x4C){
      st_flag = 0;
    }
  }

  else{
    if(st_flag == 1){
      digitalWrite(Pin_Led,0);
      delay(100);
      digitalWrite(Pin_Led,1);
      delay(100);
    } else if(st_flag == 0){
      digitalWrite(Pin_Led,1);
    } else{
      digitalWrite(Pin_Led,0);
    }
  }
}
