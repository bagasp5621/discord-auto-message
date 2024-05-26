from http.client import HTTPSConnection 
from dotenv import load_dotenv
from sys import stderr 
from json import dumps 
from time import sleep 
import os
import ssl

load_dotenv()

def getContent(contentTitle):
   return os.getenv(contentTitle)

wallpaper_content = getContent("WALLPAPER_CONTENT")
paint_content = getContent("PAINT_CONTENT")
block_content = getContent("BLOCK_CONTENT")
seed_content = getContent("SEED_CONTENT")
consumable_content = getContent("CONSUMABLES_CONTENT")
music_content = getContent("MUSIC_CONTENT")
steam_content = getContent("STEAM_CONTENT")
jammer_content = getContent("JAMMER_CONTENT")
door_content = getContent("DOOR_CONTENT")
sign_content = getContent("SIGN_CONTENT")
platform_content = getContent("PLATFORM_CONTENT")
surg_content = getContent("SURG_CONTENT")

header_data = { 
  "content-type": "application/json", 
  "user-agent": "", 
  "authorization": "", 
  "host": "discordapp.com", 
  "referer": "" 
} 

def get_connection(): 
  ssl._create_default_https_context = ssl._create_unverified_context
  return HTTPSConnection("discordapp.com", 443) 
 
def send_message(conn, channel_id, message_data): 
    try: 
        conn.request("POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data) 
        resp = conn.getresponse() 
         
        if 199 < resp.status < 300: 
            print("Message sent with channel id of " + str(channel_id)) 
            pass 
 
        else: 
            stderr.write(f"Received HTTP {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Failed to send_message\n") 
 
def main(): 
  data_list = {
      "782718523629633567": wallpaper_content,
      "774455258407370752": paint_content,
      "1104057271215984741": block_content,
      "1105154359114875072": seed_content,
      "847201895873118218": consumable_content,
      "782718975091933214": music_content,
      "806499108801478676": steam_content,
      "806523338797219860": jammer_content,
      "846671811223355402": door_content,
      "846661246303469598": sign_content,
      "846673193426354176": platform_content,
      "733049257648586792": surg_content
  }

  for channel_id, content in data_list.items():
      data = {
          "content": content,
          "tts": "false"
      }
      send_message(get_connection(), channel_id, dumps(data))
      sleep(15)
 
if __name__ == '__main__': 
  print("=== Discord Auto Message Start ===")
  while True:
    main()
    sleep(7300) 