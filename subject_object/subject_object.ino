#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define OLED_RESET 3
Adafruit_SSD1306 display(OLED_RESET);

int randomNumber;


  String subject;
  String object;



void setup() {
  randomSeed(analogRead(A0));
 
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.setTextSize(2);
  display.setTextColor(WHITE);

}


void loop() {

  randomNumber = random(0,3);
  if (randomNumber % 3 == 0) {
    subject = "they";
  }
  if (randomNumber % 3 == 1) {
    subject = "she";
  }
  if (randomNumber % 3 == 2) {
    subject = "he";
  }
  randomNumber = random(0,3);
  if (randomNumber % 3 == 0) {
    object = "them";
  }
  if (randomNumber % 3 == 1) {
    object = "her";
  }
  if (randomNumber % 3 == 2) {
    object = "him";
  }  
  display.clearDisplay();
  display.setCursor(0,12);
  display.println(subject + "/" + object);
  display.display(); 
  delay(random(2000,10001));
}    
 
