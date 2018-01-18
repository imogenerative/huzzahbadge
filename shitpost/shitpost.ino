#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define OLED_RESET 3
Adafruit_SSD1306 display(OLED_RESET);



void setup() {
 
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.setTextSize(2);
  display.setTextColor(WHITE);

    
  display.clearDisplay();
  display.setCursor(0,0);
  display.println("UNSUBSCRIBE");
  display.display();
}


void loop() {

  
}    
 
