int data;
void setup() {
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
  pinMode(LED_BUILTIN, OUTPUT); //make the LED pin (13) as output
  digitalWrite (LED_BUILTIN, LOW);
  Serial.println("Arduino listening on port 9600");
}

void loop() {
  
  while (Serial.available()){
    data = Serial.read(); //get data that python code sends
  }
  
  if (data == '1')
  digitalWrite (LED_BUILTIN, HIGH);
  
  else if (data == '0')
  digitalWrite (LED_BUILTIN, LOW);
}
