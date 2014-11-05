int valor;
int pin;
int termometro;
void setup() 
{
 Serial.begin(115200);
 pinMode(13,OUTPUT);
 pinMode(3,INPUT);
 
}

void loop() 
{
  termometro=analogRead(A0);
  termometro=map(termometro,0,1023,0,25);
  if (Serial.available( )>0)
 {
  valor=Serial.read( );
  pin=Serial.read( );
 if (valor=='a')
 {
   digitalWrite(13,HIGH);
   
 }
 if (valor=='b')
 {
  digitalWrite(13,LOW); 
  
 }
 }
 if (digitalRead(3)==true)
  {
  pin=1;
  }
 if (digitalRead(3)==false)
  {
  pin=0;
  }
String puerta=("puerta= " + String(pin) + " term= "+ String(termometro)+ "\n");
Serial.print(puerta);
//Serial.println("hola");
 delay(400);
}

