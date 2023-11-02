from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
from time import sleep 

wallpaperContent = "=================================\nSELL WALLPAPER at ✅ JAHO ✅ \n=================================\n\n⬛  Sell Black Wallpaper\n⬜  Sell White Wallpaper\n🔳  Sell Grey Wallpaper\n🟥  Sell Red Wallpaper\n🟩  Sell Aqua Wallpaper\n🟩  Sell Green Wallpaper\n🟫  Sell Brown Wallpaper\n🟦  Sell Blue Wallpaper\n🟪  Sell Purple Wallpaper\n\n=================================\nSELL WALLPAPER at ✅ JAHO ✅ \n=================================\n"

paintContent = "=================================\nSELL Paint Bucket at ✅ JAHO ✅ \n=================================\n\n⚪ Sell Paint Bucket - Varnish\n🔵 Sell Paint Bucket - Aqua\n🟢 Sell Paint Bucket - Green\n🔵 Sell Paint Bucket - Blue\n🟣 Sell Paint Bucket - Purple\n🟡 Sell Paint Bucket - Yellow\n🔴 Sell Paint Bucket - Red\n⚫ Sell Paint Bucket - Charcoal / Black\n\n=================================\nSELL Paint Bucket at ✅ JAHO ✅ \n================================="

blockContent = "=================================\nSELL Tons Blocks at ✅ JAHO ✅ \n=================================\n\n🔢 Sell Number 0-9\n🔢 Sell Number Block 0-9\n\n=================================\nSELL Tons Blocks at ✅ JAHO ✅ \n================================="
 
header_data = { 
  "content-type": "application/json", 
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76", 
  "authorization": "MTE2OTUwMTQ4Njg4NDA3MzQ3Nw.G2ylap.Cyvduv5cVPU1NwBdizB7gpKExt5kRivz2xAW1k", 
  "host": "discordapp.com", 
  "referer": "https://discord.gg/cqt9Rjeb" 
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
    "content": wallpaperContent, 
    "tts": "false", 
  } 
      
  paint_data = {
    "content": paintContent, 
    "tts": "false",   
  }
      
  block_data = {
    "content": blockContent, 
    "tts": "false", 
  }
 
  # Send Wallpaper Promotion Message
  send_message(get_connection(), "782718523629633567", dumps(wallpaper_data))
  sleep(15)  
  # Send Paint Bucket Promotion Message
  send_message(get_connection(), "774455258407370752", dumps(paint_data))
  sleep(15) 
  # Send Block Promotion Message
  send_message(get_connection(), "1104057271215984741", dumps(block_data))

  
 
if __name__ == '__main__': 
  print("=== Discord Auto Message Start ===")

  firstIteration = True

  if firstIteration:
      print("Waiting for 30 minutes to continue the script...")
      sleep(1800)    
      firstIteration = False

  firstIteration = True
  while True:
    main()
    sleep(7215) 