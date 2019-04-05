char dataString[50] = {0};
int a =0;
int waterlevel_a = 100;
int waterlevel_b = 50;
int total_volume = 200;
int tide = 100;
int temperature = 60;


void setup() {
Serial.begin(9600);              //Starting serial communication
}
  
void loop() {
  //a++;                          // a value increase every loop
  //sprintf(dataString,"%02X",a); // convert a value to hexa 
  waterlevel_a --;
  waterlevel_b ++;
  
  Serial.println(String(waterlevel_a)
  + String(waterlevel_b) 
  + String(total_volume)
  + String(tide) 
  + String(temperature));   // send the data
  delay(5000);                  // give the loop some break
}
