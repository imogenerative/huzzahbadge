#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define OLED_RESET 3
Adafruit_SSD1306 display(OLED_RESET);

int randomNumber;
int indentTop;
int indentBottom;

String subject;
String object;
String possessive;

String top;
String bottom;


void setup() {
  randomSeed(analogRead(A0));

  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.setTextSize(2);
  display.setTextColor(WHITE);

}


void loop() {

  randomNumber = random(0, 3);
  if (randomNumber % 3 == 0) {
    subject = "they";
  }
  if (randomNumber % 3 == 1) {
    subject = "she";
  }
  if (randomNumber % 3 == 2) {
    subject = "he";
  }
  randomNumber = random(0, 3);
  if (randomNumber % 3 == 0) {
    object = "them";
  }
  if (randomNumber % 3 == 1) {
    object = "her";
  }
  if (randomNumber % 3 == 2) {
    object = "him";
  }
  randomNumber = random(0, 3);
  if (randomNumber % 3 == 0) {
    possessive = "theirs";
  }
  if (randomNumber % 3 == 1) {
    possessive = "hers";
  }
  if (randomNumber % 3 == 2) {
    possessive = "his";
  }

  top = subject + "/";
  bottom = object + "/" + possessive;

  indentTop = (127 - (top.length() * 12)) / 2;
  indentBottom = (127 - (bottom.length() * 12)) / 2;

  display.clearDisplay();
  display.setCursor(indentTop, 0);
  display.print(top);
  display.setCursor(indentBottom, 16);
  display.print(bottom);
  display.display();
  delay(random(2000, 10001));
}

