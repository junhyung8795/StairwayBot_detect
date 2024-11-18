#include <ArduinoJson.h>

void setup() {
  Serial.begin(9600);
}

void loop() {
  // 파이썬에서 전송한 JSON 데이터 읽기
  unsigned long currentMillis = millis();
  if (Serial.available()) {
    // 파이썬으로부터 전송된 JSON 데이터를 저장할 버퍼
    JsonDocument doc;
    
    // 시리얼 버퍼에서 JSON 데이터 읽기
    DeserializationError error = deserializeJson(doc, Serial);
    
    // JSON 파싱 성공 여부 확인
    if (error) {
      Serial.print("JSON 파싱 에러: ");
      Serial.println(error.c_str());
      return;
    }
    
    // JSON 데이터에서 distance와 degree 값 읽기
    float distance = doc["distance"];
    float degree = doc["degree"];
    boolean detect = doc["detect"];
    int center_x = doc["center_x"];
    // 읽은 값 출력
    Serial.print("Distance: ");
    Serial.println(distance);
    Serial.print("Degree: ");
    Serial.println(degree);
    Serial.print("center_x is: ");
    Serial.println(center_x);
    Serial.println("detect: ");
    Serial.println(detect);
    Serial.print("time is: ");
    Serial.println(currentMillis);
  }
}
