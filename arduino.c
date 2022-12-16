#include <FastLED.h>
#define LED_PIN 2
#define NUM_LEDS 80

CRGB leds[NUM_LEDS];
uint8_t x;

// CRGB colors[8] {
//   CRGB::Red, CRGB::Orange, CRGB::Yellow, CRGB::Green, CRGB::Teal, CRGB::Blue, CRGB::Indigo, CRGB::Violet
// };

CRGB colors[8] {
  CRGB::Navy, CRGB::MediumBlue, CRGB::Blue, CRGB::DodgerBlue, CRGB::DeepSkyBlue, CRGB::Aqua, CRGB::Aquamarine, CRGB::Lime
};

void compute(uint8_t l) {
  for (int i = 0; i < 8; i++) {
    for (int j = 0; j < 10; j++) {
      leds[i * 10 + j] = ((l >> i) & 1) ? colors[i] : CRGB::Black;
    }
  }  
  FastLED.show();
}


void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  
  FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setMaxPowerInVoltsAndMilliamps(5, 500);
  FastLED.clear();
  FastLED.show();
}

void loop() {
  if(Serial.available() > 0) {
    x = Serial.read();
    compute(x);
  }
}