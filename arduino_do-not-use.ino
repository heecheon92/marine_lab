const int ledPin1 = 13;
const int ledPin2 = 8;
const int ledPin3 = 9;

void setup(){
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  if (Serial.available())  {
     light(Serial.read() - '0');
  }
  delay(500);
}

void light(int n){
  switch(n)
  {
    case 1:
    digitalWrite(ledPin1, HIGH);
    delay(1000);
    digitalWrite(ledPin1, LOW);
    delay(1000);
    break;
      case 2:
    digitalWrite(ledPin2, HIGH);
    delay(1000);
    digitalWrite(ledPin2, LOW);
    delay(1000);
    break;
      case 3:
    digitalWrite(ledPin3, HIGH);
    delay(1000);
    digitalWrite(ledPin3, LOW);
    delay(1000);
    break;
  }
}

