from http.client import HTTPSConnection 
from dotenv import load_dotenv
from sys import stderr 
from json import dumps 
from time import sleep 
import os

load_dotenv()

wallpaper_content = os.getenv("WALLPAPER_CONTENT")

header_data = { 
  "content-type": "application/json", 
  "user-agent": "", 
  "authorization": "", 
  "host": "discordapp.com", 
  "referer": "" 
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
  wallpaper_data = { 
    "content": wallpaper_content, 
    "tts": "false", 
  } 
 
  # Send Wallpaper Promotion Message
  send_message(get_connection(), "333911450362052610", dumps(wallpaper_data))
  sleep(15)  
 
if __name__ == '__main__': 
  print("=== Discord Auto Message Start ===")
  while True:
    main()
    sleep(7215) 