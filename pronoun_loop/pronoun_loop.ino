#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define OLED_RESET 3
Adafruit_SSD1306 display(OLED_RESET);
 
const int buttonPin = 0;

int buttonPushCounter = 0;
int buttonState = 0;
int lastButtonState = 0;

int randomNumber;
 
void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  randomSeed(analogRead(A0));
 
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);

  display.setTextSize(2);
  display.setTextColor(WHITE);

}


void loop() {
  buttonState = digitalRead(buttonPin);
 
  if (buttonState != lastButtonState) {
    if (buttonState == LOW) {
      buttonPushCounter++;
    }   
  }

  if (buttonPushCounter % 3 == 0) {
      display.clearDisplay();
      display.setCursor(0,0);
      display.println("they/them");
      display.display(); 
  }
  if (buttonPushCounter % 3 == 0) {
      display.clearDisplay();
      display.setCursor(0,0);
      display.println("she/her");
      display.display();     
  }
  if (buttonPushCounter % 3 == 0) {
      display.clearDisplay();
      display.setCursor(0,0);
      display.println("he/him");
      display.display(); 
  }
  
}    
 
