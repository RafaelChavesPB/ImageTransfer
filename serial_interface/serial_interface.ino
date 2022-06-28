char incomingByte;
 
void setup() {
  Serial.begin(9600);
}

void loop() {
  while(Serial.available()){
    incomingByte = Serial.read();
    Serial.print(incomingByte);
  }
}
