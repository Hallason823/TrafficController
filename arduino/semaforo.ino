const int R_GREEN = 4, R_YELLOW = 3, R_RED = 2;
const int B_GREEN = 7, B_YELLOW = 6, B_RED = 5;
const int YELLOW_MS = 10000;

void allRed() {
  digitalWrite(R_RED, HIGH); digitalWrite(R_YELLOW, LOW); digitalWrite(R_GREEN, LOW);
  digitalWrite(B_RED, HIGH); digitalWrite(B_YELLOW, LOW); digitalWrite(B_GREEN, LOW);
}

void setLane(int gPin, int yPin, int rPin, bool green) {
  digitalWrite(rPin,  !green);
  digitalWrite(yPin,  LOW);
  digitalWrite(gPin,  green);
}

void yellow() {
  digitalWrite(R_GREEN, LOW); digitalWrite(R_YELLOW, HIGH); digitalWrite(R_RED, LOW);
  digitalWrite(B_GREEN, LOW); digitalWrite(B_YELLOW, HIGH); digitalWrite(B_RED, LOW);
  delay(YELLOW_MS);
}

void runPhase(bool rightGreen, int durationMs) {
  if (rightGreen) {
    setLane(R_GREEN, R_YELLOW, R_RED, true);
    setLane(B_GREEN, B_YELLOW, B_RED, false);
  } else {
    setLane(R_GREEN, R_YELLOW, R_RED, false);
    setLane(B_GREEN, B_YELLOW, B_RED, true);
  }
  delay(durationMs);
  yellow();
  allRed();
  Serial.println("DONE");
}

void setup() {
  int pins[] = {R_GREEN, R_YELLOW, R_RED, B_GREEN, B_YELLOW, B_RED};
  for (int p : pins) pinMode(p, OUTPUT);
  Serial.begin(9600);
  allRed();
  Serial.println("READY");
}

void loop() {
  if (!Serial.available()) return;
  String cmd = Serial.readStringUntil('\n');
  cmd.trim();
  if (cmd.length() < 3) return;
  char lane = cmd.charAt(0);
  int  ms   = cmd.substring(2).toInt() * 1000;
  if (lane == 'R') runPhase(true,  ms);
  if (lane == 'B') runPhase(false, ms);
}
