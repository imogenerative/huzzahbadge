#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define OLED_RESET 3
Adafruit_SSD1306 display(OLED_RESET);

int randomNumber;
 
void setup() {\
  randomSeed(analogRead(A0));
 
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);

  display.setTextSize(2);
  display.setTextColor(WHITE);

}


void loop() {

  randomNumber = random(0,3);

 

  if (randomNumber % 3 == 0) {
      display.clearDisplay();
      display.setCursor(0,0);
      display.println("they/them");
      display.display(); 
  }
  if (randomNumber % 3 == 1) {
      display.clearDisplay();
      display.setCursor(0,0);
      display.println("she/her");
      display.display();     
  }
  if (randomNumber % 3 == 2) {
      display.clearDisplay();
      display.setCursor(0,0);
      display.println("he/him");
      display.display(); 
  }

  delay(random(2000,10001));
}    
 
