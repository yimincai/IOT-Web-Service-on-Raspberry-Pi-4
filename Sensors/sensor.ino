#include <WiFi.h>
#include <PubSubClient.h>
#include <Wire.h>
#include <SoftwareSerial.h>
SoftwareSerial pmsSerial(14, 12);//air
#define waterTemp_pin A6
#define SoilMoisture A5
// Replace the next variables with your SSID/Password combination
const char *ssid = "luke";
const char *password = "23924505";
static char *topicID="01/4/esp41";
// Add your MQTT Broker IP address, example:
//const char* mqtt_server = "10.42.0.1";
const char *mqtt_server = "192.168.90.101";
static unsigned char ucRxBuffer[250];
static unsigned char ucRxCnt = 0;
String datas[14];
String dataname[14] = {"pmcf10", "pmcf25", "pmcf100", "dAPM10", "dAPM25", "dAPM100", "dAP03", "dAP05",
                           "dAP10", "dAP25", "dAT", "dAH","dSTC","d"};

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;


void setup()
{
    Serial.begin(115200);
    pmsSerial.begin(9600);
    pinMode(waterTemp_pin,INPUT);
    pinMode(SoilMoisture,OUTPUT);
    setup_wifi();
    client.setServer(mqtt_server, 1883);
    
}
void WTdata(){
  float temp=analogRead(waterTemp_pin);
  datas[12]=String(temp);
}
void SMSSdata(){
  float temp=analogRead(SoilMoisture);
  Serial.print(temp);
  temp=temp/103.0;
  datas[13]=String(temp);
}
void setup_wifi()
{
    delay(10);
    // We start by connecting to a WiFi network
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(ssid);

    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }

    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
}


void reconnect()
{
    // Loop until we're reconnected
    while (!client.connected())
    {
        Serial.print("Attempting MQTT connection...");
        // Attempt to connect
        if (client.connect("ESP8266Client"))
        {
            Serial.println("connected");
            // Subscribe
            //client.subscribe("esp32/output");
        }
        else
        {
            Serial.print("failed, rc=");
            Serial.print(client.state());
            Serial.println(" try again in 5 seconds");
            // Wait 5 seconds before retrying
            delay(5000);
        }
    }
}
void loop()
{
    while (pmsSerial.available())
    {
       CopeSerialData(pmsSerial.read());
    }
    WTdata();
    SMSSdata();
    if (!client.connected())
    {
        reconnect();
    }
    client.loop();
    if(Serial.available()>0){
      if(Serial.find("show")){
        //show();
      }
    }
    unsigned long now = millis();
    if (now - lastMsg > 5000)
    {
        lastMsg = now;
        
        //    // Convert the value to a char array
        //    char humString[8];
        //    dtostrf(humidity, 1, 2, humString);
        //    Serial.print("Humidity: ");
        //    Serial.println(humString);
        Serial.print("Sensor amount is ");Serial.println(sizeof(dataname));
        for (short i = 3; i < 14; i++)
        {

            String temp=dataname[i]+' '+datas[i];
            char datatemp[temp.length()];
            temp.toCharArray(datatemp,temp.length());
            char *topic = topicID;
            client.publish(topic, datatemp);
            Serial.print(datatemp);
            Serial.println(" has send");
        }
    }
    delay(1000);
}
char CopeSerialData(unsigned char ucData)
{

    ucRxBuffer[ucRxCnt++] = ucData;
    if (ucRxBuffer[0] != 0x42 && ucRxBuffer[1] != 0x4D)
    {
        ucRxCnt = 0;
        return ucRxCnt;
    }
    if (ucRxCnt < 30)
    { // G5T
        return ucRxCnt;
    }
    else
    {
        int i = 0;
        datas[i++]=String((float)ucRxBuffer[4] * 256 + (float)ucRxBuffer[5]);
        
        datas[i++]=String((float)ucRxBuffer[6] * 256 + (float)ucRxBuffer[7]);
        
        datas[i++]=String((float)ucRxBuffer[8] * 256 + (float)ucRxBuffer[9]);
        
        datas[i++]=String((float)ucRxBuffer[10] * 256 + (float)ucRxBuffer[11]);
        
        datas[i++]=String((float)ucRxBuffer[12] * 256 + (float)ucRxBuffer[13]);
        
        datas[i++]=String((float)ucRxBuffer[14] * 256 + (float)ucRxBuffer[15]);
        
        datas[i++]=String((float)ucRxBuffer[16] * 256 + (float)ucRxBuffer[17]);
        
        datas[i++]=String((float)ucRxBuffer[18] * 256 + (float)ucRxBuffer[19]);
        
        datas[i++]=String((float)ucRxBuffer[20] * 256 + (float)ucRxBuffer[21]);
        
        datas[i++]=String((float)ucRxBuffer[22]*256+(float)ucRxBuffer[23]);
        
        datas[i++]=String(((float)ucRxBuffer[24] * 256 + (float)ucRxBuffer[25]) / 10);
        
        datas[i]=String(((float)ucRxBuffer[26] * 256 + (float)ucRxBuffer[27]) / 10);
        
        
    }
}
void show(){
  
        int i=0;
        Serial.print("PM1.0_CF1:");
        Serial.println(datas[i++]);
        
        Serial.print("PM2.5_CF1:");
        Serial.println(datas[i++]);
        
        Serial.print("PM10_CF1:");
        Serial.println(datas[i++]);
        
        Serial.print("PM1.0_AT:");
        Serial.println(datas[i++]);
        
        Serial.print("PM2.5_AT:");
        Serial.println(datas[i++]);
        
        Serial.print("PM10_AT:");
        Serial.println(datas[i++]);
        
        Serial.print("PMcount0.3:");
        Serial.println(datas[i++]);
        
        Serial.print("PMcount0.5:");
        Serial.println(datas[i++]);
        
        Serial.print("PMcount1.0:");
        Serial.println(datas[i++]);
        
        Serial.print("PMcount2.5:");
        Serial.println(datas[i++]);
        
        Serial.print("Temperature:");
        Serial.println(datas[i++]);
        
        Serial.print("Humidity:");
        Serial.println(datas[i]);
}
