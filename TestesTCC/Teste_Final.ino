//Adiciona a biblioteca ao código
#include <LiquidCrystal.h>
#include <DHT.h>
#include <Servo.h>

//Define o pino a ser utilizado pelo DTH22
#define DHTPIN 7

//Define o tipo de DTH a ser utilzado junto a biblioteca
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

//Define os pinos a ser utilzado com display
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

//Cria os objeto servo
Servo servo1, servo2;

//Define os pinos a serem utilizados pelo coolers e servos
const int ventilador1 = 22;
const int ventilador2 = 24;
const int exaustor1 = 26;
const int exaustor2 = 28;
const int servo1Pin = 9;
const int servo2Pin = 8;

//Define os valores ideais do projeto
const float temperaturaIdeal = 22.0;
const float umidadeIdeal = 50;
const float IQAIdeal = 60.0;

int intervalo = 5000;
unsigned long ultimaAtualizacao = 0;
int secaoAtual = 0;

void setup() {
  Serial.begin(9600);
  dht.begin();
  lcd.begin(16, 2);
  pinMode(ventilador1, OUTPUT);
  pinMode(ventilador2, OUTPUT);
  pinMode(exaustor1, OUTPUT);
  pinMode(exaustor2, OUTPUT);
  servo1.attach(servo1Pin);
  servo2.attach(servo2Pin);
  
  lcd.setCursor(0, 0);
  lcd.print("Sensor MQ-135");
  lcd.setCursor(0, 1);
  lcd.print("e DHT22");
  delay(2000);
}

void loop() {
  //Atribui os valores obtidos pelos sensores com as devida variaveis
  float temperatura = dht.readTemperature();
  float umidade = dht.readHumidity();
  int valorMQ135 = analogRead(A0);
  
  // Controle dos coolers
  // Controla os coolers quando a temperatura é maior que a ideal
  if (temperatura > temperaturaIdeal) {
  digitalWrite(ventilador1, HIGH);
  digitalWrite(ventilador2, HIGH);
 
  } 
  
  else {
  digitalWrite(ventilador1, LOW);
  digitalWrite(ventilador2, LOW);

  }

  // Controla os coolers quando a qualidade do ar é maior que a ideal
  if (valorMQ135 > IQAIdeal) {
  digitalWrite(exaustor1, HIGH);
  digitalWrite(exaustor2, HIGH);
 
  } 
  
  else {
  digitalWrite(exaustor1, LOW);
  digitalWrite(exaustor2, LOW);
  }
 
  // Controle do servo 1 (umidade)
  // Liga o umidificador quando a umidade for menor que a ideal
  if (umidade < umidadeIdeal && servo1.read() != 111) {
  servo1.write(110); // Gira para 90 graus se não estiver na posição desejada
  delay(1200);
  servo1.write(98);
  delay(300);
  servo1.write(111);

  // Desliga o umidificador quando a umidade for igual ou maior que a ideal
} else if (umidade >= umidadeIdeal && servo1.read() != 112) {
  servo1.write(110); // Gira para 90 graus se não estiver na posição desejada
  delay(1200);
  servo1.write(98);
  delay(300);
  servo1.write(110);
  delay(1200);
  servo1.write(98);
  delay(300);
  servo1.write(112);
}

  // Controle do servo 2 (janelas)
  if (temperatura < temperaturaIdeal && servo2.read() != 90) {
  servo2.write(90); // Gira para 90 graus se não estiver na posição desejada
} else if (temperatura >= temperaturaIdeal && servo2.read() != 0) {
  servo2.write(0); // Gira para 0 grau se não estiver na posição desejada
}

  if (millis() - ultimaAtualizacao >= intervalo) {
  ultimaAtualizacao = millis();
  secaoAtual = (secaoAtual + 1) % 2;
  lcd.clear();
  lcd.setCursor(0, 0);
    
    switch (secaoAtual) {
      case 0:
        lcd.print("Temp: ");
        lcd.print(temperatura);
        lcd.print(" C");
        Serial.print("Temperatura: ");
        Serial.print(temperatura);
        Serial.println(" °C");
        lcd.setCursor(0, 1);
        lcd.print("Umidade: ");
        lcd.print(umidade);
        lcd.print(" %");
        Serial.print("Umidade: ");
        Serial.print(umidade);
        Serial.println(" %");
        break;
      case 1:
        lcd.print("IQA: ");
        lcd.print(valorMQ135);
        Serial.print("IQA: ");
        Serial.println(valorMQ135);
        break;
    }
  }
}
