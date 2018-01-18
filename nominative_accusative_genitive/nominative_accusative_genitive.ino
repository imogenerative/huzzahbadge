#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define OLED_RESET 3
Adafruit_SSD1306 display(OLED_RESET);

int randomNumber;
int indentTop;
int indentBottom;

String nominative;
String accusative;
String genitive;

String topLine;
String bottomLine;


void setup() {
  randomSeed(analogRead(A0));

  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.setTextSize(2);
  display.setTextColor(WHITE);

}


void loop() {

  randomNumber = random(0, 3);
  if (randomNumber % 3 == 0) {
    nominative = "they";
  }
  if (randomNumber % 3 == 1) {
    nominative = "she";
  }
  if (randomNumber % 3 == 2) {
    nominative = "he";
  }
  randomNumber = random(0, 3);
  if (randomNumber % 3 == 0) {
    accusative = "them";
  }
  if (randomNumber % 3 == 1) {
    accusative = "her";
  }
  if (randomNumber % 3 == 2) {
    accusative = "him";
  }
  randomNumber = random(0, 3);
  if (randomNumber % 3 == 0) {
    genitive = "theirs";
  }
  if (randomNumber % 3 == 1) {
    genitive = "hers";
  }
  if (randomNumber % 3 == 2) {
    genitive = "his";
  }

  topLine = nominative + "/";
  bottomLine = accusative + "/" + genitive;

  indentTop = (127 - (topLine.length() * 12)) / 2;
  indentBottom = (127 - (bottomLine.length() * 12)) / 2;

  if (bottomLine.length() == 10) {
    indentBottom = 0;
  }

  display.clearDisplay();
  display.setCursor(indentTop, 0);
  display.print(topLine);
  display.setCursor(indentBottom, 16);
  display.print(bottomLine);
  display.display();
  delay(random(2000, 10001));
}

