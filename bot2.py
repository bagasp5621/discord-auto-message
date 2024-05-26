from http.client import HTTPSConnection 
from dotenv import load_dotenv
from sys import stderr 
from json import dumps 
from time import sleep 
import os

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
lock_content = getContent("LOCK_CONTENT")
ghost_content = getContent("GHOST_CONTENT")

header_data = { 
  "content-type": "application/json", 
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0", 
  "authorization": "MTI0MzQxMzQ2ODA0NDg1NzM4NA.G_Ose9.hCgzGYeVOWw8fBOuLfpnweUHKC9HlXfX5WAJyk", 
  "host": "discordapp.com", 
  "referer": "1169597075504238672" 
} 

def get_connection(): 
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
      "1169597077945327680": block_content,
      # "1169597077945327680": wallpaper_content,
      # "1169597077945327680": paint_content,
      # "1169597077945327680": block_content,
      # "1169597077945327680": seed_content,
      # "1169597077945327680": consumable_content,
      # "1169597077945327680": music_content,
      # "1169597077945327680": steam_content,
      # "1169597077945327680": jammer_content,
      # "1169597077945327680": door_content,
      # "1169597077945327680": sign_content,
      # "1169597077945327680": platform_content
  }


  for channel_id, content in data_list.items():
      data = {
          "content": content,
          "tts": "false"
      }
      send_message(get_connection(), channel_id, dumps(data))
      sleep(1)
 
if __name__ == '__main__': 
  print("=== Discord Auto Message Start ===")
  while True:
    main()
    sleep(1) 