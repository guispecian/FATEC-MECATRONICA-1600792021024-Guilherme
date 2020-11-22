//Projeto Sensor de Ré
//Guilherme Mendes Specian, RA: 1600792021024
//Kevin Moura da Silva, RA:
//Victor Augusto de Pascale Souza, RA: 

//Nomear os pinos
const int BOTAO_1 = 11;
const int LED_1 = 12;
const int ENABLE = 2;
const int RS = 13;
const int LCD_DB7 = 7;
const int LCD_DB6 = 6;
const int LCD_DB5 = 5;
const int LCD_DB4 = 4;
const int ECHO_PINO = 9;
const int TRIGGER_PINO = 10;

//Chamar a Biblioteca LiquidCrystal
#include <LiquidCrystal.h>

//Criar variavel lcd
LiquidCrystal lcd(RS,ENABLE,LCD_DB4,LCD_DB5,LCD_DB6,LCD_DB7);

//Configurar o Sensor para medir a distancia
int medir_distancia(){
  digitalWrite(TRIGGER_PINO, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGGER_PINO, HIGH);
  delayMicroseconds(10);
  int tempo_onda = pulseIn(ECHO_PINO, HIGH);
  return int(tempo_onda * 0.017);
}

void setup() {
  //Configurar as Entradas
  pinMode(BOTAO_1, INPUT);
  
  //Configurar as Saídas
  pinMode(LED_1, OUTPUT);
  
  //Configurar os pinos do sensor
  pinMode(ECHO_PINO, INPUT);
  pinMode(TRIGGER_PINO, OUTPUT);
  digitalWrite(TRIGGER_PINO, HIGH);
  
  //Iniciar o LCD
  lcd.begin(16, 2);
  //Posiconar o Cursor do LCD
  lcd.setCursor(0,1);
  //Escrever mensagem no LCD
  lcd.print("Sensor de Re: off");
}

void loop() {

}
