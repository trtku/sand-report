#include "SCD30.h"
#include "Mapf.h"
#include "EEPROM.h"

#if defined(PARTICLE)
    #pragma message("Defined architecture for PARTICLE")
    #define SERIAL Serial
#elif defined(ARDUINO_ARCH_AVR)
    #pragma message("Defined architecture for ARDUINO_ARCH_AVR.")
    #define SERIAL Serial
#elif defined(ARDUINO_ARCH_SAM)
    #pragma message("Defined architecture for ARDUINO_ARCH_SAM.")
    #define SERIAL SerialUSB
#elif defined(ARDUINO_ARCH_SAMD)
    #pragma message("Defined architecture for ARDUINO_ARCH_SAMD.")
    #define SERIAL SerialUSB
#elif defined(ARDUINO_ARCH_STM32F4)
    #pragma message("Defined architecture for ARDUINO_ARCH_STM32F4.")
    #define SERIAL SerialUSB
#else
    #pragma message("Not found any architecture.")
    #define SERIAL Serial
#endif

int rownumber = 0;

void setup() {
    Wire.begin();
    Serial.begin(9600);
    scd30.initialize();
}

void loop() {
    float result[3] = {0};
    float ppm;
    float dgr;
    float per;

    if (scd30.isAvailable()) {
        scd30.getCarbonDioxideConcentration(result);
        //raw
        ppm = result[0];
        dgr = result[1];
        per = result[2];
        //map
//        ppm = mapf(result[0], 0, 40000, 0, 1);
//        dgr = mapf(result[1], 0, 100, 0, 1);
//        per = mapf(result[2], 0, 100, 0, 1);

        Serial.print(++rownumber);
        Serial.print(",");
        
//        Serial.print("CO2_ppm:");
        Serial.print(ppm);
        Serial.print(",");

//        Serial.print("Temprature_℃:");
        Serial.print(dgr);
        Serial.print(",");

//        Serial.print("Humidity_%:");
        Serial.println(per);
        
    }

    delay(10000);
}
