// Codigo para teste dos relés junto ao coolers 
// Define os pinos utilizados no pino SINAL do relé
const int cooler1RelayPin = 22;
const int cooler2RelayPin = 24;
const int cooler3RelayPin = 26;
const int cooler4RelayPin = 28;

void setup() {
  pinMode(cooler1RelayPin, OUTPUT);
  pinMode(cooler2RelayPin, OUTPUT);
  pinMode(cooler3RelayPin, OUTPUT);
  pinMode(cooler4RelayPin, OUTPUT);
}

void loop() {
  // Controle dos coolers
  // Liga todos os coolers mandando o comando HIGH para o relé
  digitalWrite(cooler1RelayPin, HIGH);
  digitalWrite(cooler2RelayPin, HIGH);
  digitalWrite(cooler3RelayPin, HIGH);
  digitalWrite(cooler4RelayPin, HIGH);

  // Aguardando por 2 segundos
  delay(2000);

  // Desliga todos os coolers mandando o comando HIGH para o relé
  digitalWrite(cooler1RelayPin, LOW);
  digitalWrite(cooler2RelayPin, LOW);
  digitalWrite(cooler3RelayPin, LOW);
  digitalWrite(cooler4RelayPin, LOW);

  // Aguardando por 2 segundos
  delay(2000);
}
