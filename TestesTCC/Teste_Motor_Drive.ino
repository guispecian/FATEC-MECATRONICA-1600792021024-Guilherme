// Define as portas dos motores DC
#define M1_A 9
#define M1_B 8
#define M2_A 12
#define M2_B 11
#define M3_A 3
#define M3_B 2
#define M4_A 6
#define M4_B 5

void setup() {
  
  // Define as portas dos motores DC como saídas
  pinMode(M1_A, OUTPUT);
  pinMode(M1_B, OUTPUT);
  pinMode(M2_A, OUTPUT);
  pinMode(M2_B, OUTPUT);
  pinMode(M3_A, OUTPUT);
  pinMode(M3_B, OUTPUT);
  pinMode(M4_A, OUTPUT);
  pinMode(M4_B, OUTPUT);
}

void loop() {
  // Gira os motores DC para um lado
  digitalWrite(M1_A, HIGH);
  digitalWrite(M1_B, LOW);
  digitalWrite(M2_A, HIGH);
  digitalWrite(M2_B, LOW);
  digitalWrite(M3_A, HIGH);
  digitalWrite(M3_B, LOW);
  digitalWrite(M4_A, HIGH);
  digitalWrite(M4_B, LOW);
  
  // Aguarda 1 segundo
  delay(1000);

  // Gira os motores DC para o outro lado
  digitalWrite(M1_A, LOW);
  digitalWrite(M1_B, HIGH);
  digitalWrite(M2_A, LOW);
  digitalWrite(M2_B, HIGH);
  digitalWrite(M3_A, LOW);
  digitalWrite(M3_B, HIGH);
  digitalWrite(M4_A, LOW);
  digitalWrite(M4_B, HIGH);

  // Aguarda 1 segundo
  delay(1000);
}
