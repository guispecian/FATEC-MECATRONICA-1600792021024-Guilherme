//Projeto Sensor de Ré
//Guilherme Mendes Specian, RA: 1600792021024
//Kevin Moura da Silva, RA:
//Victor Augusto de Pascale Souza, RA: 

//Nomear os pinos
const int BOTAO_1 = 11;
const int LED_1 = 12;
const int ENABLE = 2;
const int RS = 13;
const int LCD_D7 = 7;
const int LCD_D6 = 6;
const int LCD_D5 = 5;
const int LCD_D4 = 4;
const int ECHO_PINO = 9;
const int TRIGGER_PINO = 10;

//Chamar a Biblioteca LiquidCrystal
#include <LiquidCrystal.h>

//Criar variavel lcd
LiquidCrystal lcd(RS, ENABLE, LCD_D4, LCD_D5, LCD_D6, LCD_D7);

//Configurar o Sensor para medir a distância
int medir_distancia(){
  digitalWrite(TRIGGER_PINO, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGGER_PINO, HIGH);
  delayMicroseconds(10);
  int tempo_onda = pulseIn(ECHO_PINO, HIGH);
  return int(tempo_onda * 0.017);
}

void setup() {
  //Configurar as entradas
  pinMode(BOTAO_1, INPUT);
  
  //Configurar as saídas
  pinMode(LED_1, OUTPUT);
  
  //Configurar os pinos do sensor
  pinMode(ECHO_PINO, INPUT);
  pinMode(TRIGGER_PINO, OUTPUT);
  digitalWrite(TRIGGER_PINO, HIGH);
  
  //Iniciar o LCD
  lcd.begin(16, 2);
  //Posiconar o cursor do LCD
  lcd.setCursor(0,0);
  //Escrever mensagem no LCD
  lcd.print("off");
}

void loop() {
  if(digitalRead(BOTAO_1) == HIGH){ //Programa quando a ré estiver acionda
    // Faz a leitura do sensor
    int distancia = medir_distancia();
    // Limpar tela do LCD
    lcd.clear();
    if (distancia > 100){ //Programação quando a distancia for maior que 1 metro(100 cm)
      // Manter led de aviso desligado
      digitalWrite(LED_1, LOW);
      // Escrever mensagem no LCD
      // Posicionar o cursor no LCD
      lcd.setCursor(0,1);
      // Mostar a distancia do sensor com o objeto
      lcd.print(distancia);
      // Mostar ao final da distancia a unidade de medida (cm)
      lcd.print(" cm");
    } else if(distancia <= 100){ //Programação quando a distancia for menor ou igual a 1 metro(100 cm)
      // Ligar o led de aviso
      digitalWrite(LED_1, HIGH);
      // Escrever mensagem no LCD
      // Posicionar o cursor no LCD
      lcd.setCursor(0,1);
      // Mostar mensagem de cuidado
      lcd.print("CUIDADO:");
      // Mostar a distancia do sensor com o objeto
      lcd.print(distancia);
      // Mostar ao final da distancia a unidade de medida (cm)
      lcd.print(" cm");
    }
  }else if(digitalRead(BOTAO_1) == LOW){ //Programa quando a ré estiver desacionada
    // Limpar tela do LCD
    lcd.clear();
    // Manter led de aviso desligado
    digitalWrite(LED_1, LOW);
    // Mensagem para informar que a ré está desacionada
    lcd.print("off");
  } 
  // Atualizar mensgagens a cada 30 milisegundos
  delay (30);
   
}
