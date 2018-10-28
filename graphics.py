import subprocess
import sys, os
import os.path
from luma.oled.device import ssd1306, sh1106
from luma.core.render import canvas
from PIL import ImageFont
from PIL import Image
import time, textwrap
from datetime import datetime

# Setup Display
device = ssd1306(port=1, address=0x3C)
small_font = ImageFont.truetype('FreeMono.ttf', 12)
large_font = ImageFont.truetype('FreeMono.ttf', 22)



def radio1():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'BBC_Radio_1_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def radio2():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'BBC_Radio_2_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def radio3():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'BBC_Radio_3_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def radio4():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'BBC_Radio_4_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def worldserv():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'BBC_World_Service_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def radio1X():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'BBC_Radio_1X_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def radio4X():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'BBC_Radio_4X_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def wshu():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'WSHU_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def wnyc():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'WNYC_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def radio5():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'BBC_Radio_5_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def radio6():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'BBC_Radio_6_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def CBC1():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'CBC_Radio_1_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def CBC2():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'CBC_Radio_2_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def CFRC():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'CFRC_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def The_Bull():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'The_Bull_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def ClassicFM():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'Classic_FM_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def i98Q():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         '98Q_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def volume_up():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'Vol_Up_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def volume_max():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'Vol_Max_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def volume_min():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'Vol_Min_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def volume_down():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'Vol_Down_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def no_toast():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'No_Toast_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def dualit():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'Dualit_128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def dualitN():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'Dualit_Neville.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def main():
    today_last_time = "Unknown"
    seconds = 2.5
    start = time.time()
    if time.time() - start < seconds:
        now = datetime.now()
        today_date = now.strftime("%d %b %y")
        today_time = now.strftime("%H:%M")
        if today_time != today_last_time:
            today_last_time = today_time
            with canvas(device) as draw:
                now = datetime.now()
                today_date = now.strftime("%d %b %y")


                draw.text((5, 5), today_date, fill="white",font=large_font)
                draw.text((32,35), today_time, fill="white", font=large_font)

        time.sleep(0.05)
    
