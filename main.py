debug_mode = False
CURRENT_VERSION = """
2.6.2
"""
CURRENT_VERSION = CURRENT_VERSION.replace("\n", "")


import os, sys, random, requests


def get_latest_version_info():
    try:
        response = requests.get(VERSION_CHECK_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestError as e:
        print(f"Error checking for updates: {e}")
        return None


def download_new_version(download_url, filename):
    try:
        response = requests.get(download_url)
        response.raise_for_status()

        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        with open(filename, "wb") as file:
            file.write(response.content)
    except Exception as e:
        print(f"Error saat mengunduh: {e}")


try:
    from colorama import init, Fore, Back, Style

    init()

    def color(text, fore=None, back=None):
        color_map = {
            (255, 0, 0): Fore.BLUE,
            (0, 255, 0): Fore.BLUE,
            (0, 0, 255): Fore.BLUE,
            (255, 255, 0): Fore.BLUE,
            (0, 255, 255): Fore.BLUE,
            (255, 0, 255): Fore.BLUE,
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result

    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem

    local_ip = requests.get("https://api.ipify.org").text
    response = requests.get(f"https://ipinfo.io/{local_ip}/json")
    data_jaringan = response.json()
except Exception as e:
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pystyle")

    from colorama import init, Fore, Back, Style

    init()

    def color(text, fore=None, back=None):
        color_map = {
            (0, 0, 255): Fore.BLUE,
            (0, 0, 255): Fore.BLUE,
            (0, 0, 255): Fore.BLUE,
            (0, 0, 255): Fore.BLUE,
            (0, 0, 255): Fore.BLUE,
            (0, 0, 255): Fore.BLUE,
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result

    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem

# text = """


banner = r"""                                                          
░█▄█▒█▀▄░▄▀▄▒█▀
▒█▒█░█▀▄░▀▄▀░█▀                                                                        
                           
 
                   █░█ ▄▀█ █▀▀ █▄▀ █▀▀ █▀█
                   █▀█ █▀█ █▄▄ █░█ ██▄ █▀▄
                    
░▄▀▀▒▄▀▄▒█▀▄░░▒█▀▄▒▄▀▄▒█▀▄░█▄▀░█░█▄░█░▄▀▒░░░█▄▒▄█░█▒█░█▒░░▀█▀░█▒█▀▄░█▒░▒▄▀▄░▀▄▀▒██▀▒█▀▄
░▀▄▄░█▀█░█▀▄▒░░█▀▒░█▀█░█▀▄░█▒█░█░█▒▀█░▀▄█▒░░█▒▀▒█░▀▄█▒█▄▄░▒█▒░█░█▀▒▒█▄▄░█▀█░▒█▒░█▄▄░█▀▄

                         ░█▄█▒█▀▄░▄▀▄▒█▀
                         ▒█▒█░█▀▄░▀▄▀░█▀                                                                    
"""[1:]


pyAnime.Fade(
    pyCenter.Center(banner), pyColors.red_to_blue, pyColorate.Vertical, enter=True
)


# pyAnime.Fade(pyCenter.Center(text), pyColors.purple_to_red, pyColorate.Vertical, enter=True)
# print(pyColorate.Horizontal(pyColors.red_to_blue, pyCenter.XCenter(text)))

pySystem.Clear()

# print("\n"*2    )
# print(pyColorate.Horizontal(pyColors.red_to_blue, pyCenter.XCenter(text)))
# print("\n"*2)


from pystyle import Box
import random
import requests
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate
from pystyle import Center
import datetime


from CPMHROF import CPMHROF

__CHANNEL_USERNAME__ = "HACKER_HROF"
__GROUP_USERNAME__ = "HACKER_HROF"
__BOT_RICK_NAME__ = "HHIDD12BOT"
_CHEATS_NAME = "👑 ﺕﻮـــﻤــــﻟﺍ ﻑﻭﺮـــﺣ  ﻚــﻤــﻋ  👑"


def signal_handler(sig, frame):
    print("\n وداعا وداعا...")
    sys.exit(0)


def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != " ":
                color_index = int(
                    (
                        (x / (width - 1 if width > 1 else 1))
                        + (y / (height - 1 if height > 1 else 1))
                    )
                    * 0.5
                    * (len(colors) - 1)
                )
                color_index = min(max(color_index, 0), len(colors) - 1)
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text


def modificar_todos_los_autos(cpm, hp, hp_interno, nm, torque):
    try:
        response = cpm.modificar_todos_los_autos(hp, hp_interno, nm, torque)
        if response:
            print(
                Colorate.Horizontal(
                    Colors.rainbow, "ﺡﺎﺠﻨﺑ ﺕﺍﺭﺎﻴﺴﻟﺍ ﻊﻴﻤﺟ ﻞﻳﺪﻌﺗ ﻢﺗ."
                )
            )
        else:
            print(Colorate.Horizontal(Colors.rainbow, "ﺕﺍﺭﺎﻴﺴﻟﺍ ﻞﻳﺪﻌﺗ ﺪﻨﻋ ﺄﻄﺧ."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.rainbow, f"خطأ: {e}"))


def banner(console):
    os.system("cls" if os.name == "nt" else "clear")

    brand_name = """                                                          
░█▄█▒█▀▄░▄▀▄▒█▀
▒█▒█░█▀▄░▀▄▀░█▀
                                                                                  
                    
    """

    colors = [
        "rgb(0,0,255)",  # Vermelho
        "rgb(0,0,255)",  # Vermelho-alaranjado
        "rgb(0,0,255)",  # Laranja
        "rgb(0,0,255)",  # Amarelo-alaranjado
        "rgb(0,0,255)",  # Amarelo
        "rgb(0,0,255)",  # Amarelo claro
    ]

    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(
        Colorate.Horizontal(
            Colors.blue_to_red,
            Center.XCenter(
                "─════════════════════════════[ تﻮﻤﻟا فﻭﺮﺣ  ]════════════════════════════─"
            ),
        )
    )

    print(
        Colorate.Horizontal(
            Colors.blue_to_red,
            Center.XCenter(
            f" ﻙﻮﺘﻜﻴﺗ: @{__CHANNEL_USERNAME__}"    
          ),
        )
    )

    print(
        Colorate.Horizontal(
            Colors.blue_to_red,
            Center.XCenter(
                f" ﻡﺍﺮﺠﻴﻠﻴﺗ: @{__CHANNEL_USERNAME__}"
            ),
        )
    )

    print(
        Colorate.Horizontal(
            Colors.blue_to_red,
            Center.XCenter(
                "─══════════════════════════[ تﻮﻤﻟا فﻭﺮﺣ ]══════════════════════════─"
            ),
        )
    )


def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get("ok"):
        data = response.get("data")
        if (
            isinstance(data, dict)
            and "floats" in data
            and "localID" in data
            and "money" in data
            and "coin" in data
        ):
            name = data.get("Name", "UNDEFINED")
            local_id = data.get("localID")
            money = data.get("money")
            coin = data.get("coin")
            print(
                Colorate.Horizontal(
                    Colors.blue_to_red,
                    Center.XCenter(
                        f"ﻢﺳﺍ: {name} <> ﻲﻠﺤﻣ ﻑﺮﻌﻣ: {local_id} <> ﻝﺎﻣ: {money} <> ﺔﻴﻧﺪﻌﻣ ﺕﻼﻤﻋ: {coin}"
                    ),
                )
            )
        else:
            print(
                Colorate.Horizontal(
                    Colors.blue_to_red,
                    "                            ! 👑 ﺕﻮـــﻤــــﻟﺍ ﻑﻭﺮـــﺣ  ﻚــﻤــﻋ  👑 !",
                )
            )
    else:
        print(
            Colorate.Horizontal(
                Colors.blue_to_red, "                           ! 👑 ﺕﻮـــﻤــــﻟﺍ ﻑﻭﺮـــﺣ  ﻚــﻤــﻋ  👑 !"
            )
        )


def load_key_data(cpm):

    data = cpm.get_key_data()

    print(
        Colorate.Horizontal(
            Colors.blue_to_red,
            Center.XCenter(
                "─══════════════════════[ تﻮﻤﻟا فﻭﺮﺣ ]══════════════════════─"
            ),
        )
    )

    

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(
                Colorate.Horizontal(
                    Colors.blue_to_red,
                    f"{tag} CANNOT BE EMPTY OR JUST SPACES, PLEASE TRY AGAIN",
                )
            )
        else:
            return value


def load_client_details():
    response = requests.get("http://ip-api.com/json")
    data = response.json()
    


def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i : i + 2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i : i + 2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(
        int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb)
    )
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)


def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f"[{interpolated_color}]{char}"
    return modified_string


if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[🎭] ﺏﺎﺴﺤﻠﻟ ﻲﻧﻭﺮﺘﻜﻟﻹﺍ ﺪﻳﺮﺒﻟﺍ", "Email", password=False)
        acc_password = prompt_valid_value(
            "[🎭] ﺮﺴﻟﺍ ﺔﻤﻠﻛ", "Password", password=False
        )
        acc_access_key = prompt_valid_value(
            "[🎭] ﻝﻮﺻﻮﻟﺍ ﺡﺎﺘﻔﻣ", "Access Key", password=False
        )
        console.print("[🔎] ﻝﻮﺧﺪﻟﺍ ﻞﻴﺠﺴﺗ ﺔﻟﻭﺎﺤﻣ: ", end=None)
        cpm = CPMHROF(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                print(Colorate.Horizontal(Colors.blue_to_red, "ACCOUNT NOT FOUND"))
                sleep(2)
                continue
            elif login_response == 101:
                print(Colorate.Horizontal(Colors.blue_to_red, "WRONG PASSWORD"))
                sleep(2)
                continue
            elif login_response == 103:
                print(Colorate.Horizontal(Colors.blue_to_red, "INVALID ACCESS KEY"))
                sleep(2)
                continue
            else:
                print(Colorate.Horizontal(Colors.blue_to_red, "TRY AGAIN"))
                print(
                    Colorate.Horizontal(
                        Colors.blue_to_red,
                        "! NOTE: MAKE SURE YOU FILLED OUT THE FIELDS",
                    )
                )
                sleep(2)
                continue
        else:
            print(Colorate.Horizontal(Colors.blue_to_red, "ﺢﺟﺎﻧ"))
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            load_client_details()
            choices = [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
                "30",
                "31",
                "32",
                "33",
                "34",
                "35",
                "36",
                "37",
                "38",
                "39",
                "40",
                "41",
                "42",
                "43",
                "44",
                "45",
                "46",
                "47",
                "48",
                "49",
            ]
            print(
                Colorate.Horizontal(
                    Colors.blue_to_red,
                    Center.XCenter(
                        Box.DoubleCube(
                            "➩ (01) ﻝﺎﻤﻟﺍ ﺓﺩﺎﻳﺯ                1.5K  |  ➩ (02) ﺔﻴﻧﺪﻌﻤﻟﺍ ﺕﻼﻤﻌﻟﺍ ﺓﺩﺎﻳﺯ                1.5K\n\n"
                            "➩ (03) ﻚﻠﻤﻟﺍ ﺔﺒﺗﺭ                     8K   |  ➩ (04) ﻑﺮﻌﻤﻟﺍ ﺮﻴﻴﻐﺗ                     4.5K\n\n"
                            "➩ (05) ﻢﺳﻻﺍ ﺮﻴﻴﻐﺗ                   100  |  ➩ (06) ﺡﺰﻗ ﺱﻮﻗ ﻢﺳﻻﺍ ﺮﻴﻴﻐﺗ          100\n\n"
                            "➩ (07) ﺕﺍﺭﺎﻴﺴﻟﺍ ﻡﺎﻗﺭﺃ ﺕﺎﺣﻮﻟ                 2K   |  ➩ (08) ﺏﺎﺴﺤﻟﺍ ﻑﺬﺣ                ﺎﻧﺎﺠﻣ\n\n"
                            "➩ (09) ﺏﺎﺴﺤﻟﺍ ﻞﻴﺠﺴﺗ              ﺎﻧﺎﺠﻣ |  ➩ (10) ﺀﺎﻗﺪﺻﻷﺍ ﻑﺬﺣ                500\n\n"
                            "➩ (11)(ﻂﻘﻓ SOi) ﻲﻨﻴﻏﺭﻮﺒﻣﻻ ﻞﻔﻗ ﺢﺘﻓ 5K  |  ➩ (12) ﺕﺍﺭﺎﻴﺴﻟﺍ ﻊﻴﻤﺟ ﺢﺘﻓ               6K\n\n"
                            "➩ (13) ﺕﺍﺭﺎﻴﺴﻟﺍ ﻲﻓ ﺭﺍﺬﻧﻹﺍ ﺕﺍﺭﺎﻔﺻ ﻊﻴﻤﺟ ﺢﺘﻓ         3.5K |  ➩ (14) ﻉﻮﻓﺪﻣ ﻙﺮﺤﻣ ﺢﺘ             4K\n\n"
                            "➩ (15) ﻕﺍﻮﺑﻷﺍ ﻊﻴﻤﺟ ﺢﺘﻓ              3K   |  ➩ (16) ﺭﺮﻀﻟﺍ ﻞﻴﻄﻌﺗ ﻞﻔﻗ ﺀﺎﻐﻟﺇ        3K\n\n"
                            "➩ (17) ﺩﻭﺪﺤﻣ ﺮﻴﻏ ﺩﻮﻗﻭ ﺢﺘﻓ         3K   |  ➩ (18) ﻝﺰﻨﻤﻟﺍ ﺢﺘﻓ 3                 4K\n\n"
                            "➩ (19) ﻥﺎﺧﺪﻟﺍ ﺢﺘﻓ                 4K   |  ➩ (20) ﺕﻼﺠﻌﻟﺍ ﺢﺘﻓ                4K\n\n"
                            "➩ (21) ﺔﻛﺮﺤﺘﻤﻟﺍ ﻡﻮﺳﺮﻟﺍ ﺢﺘ            2K   |  ➩ (22) ﻡ ﺕﺍﺪﻌﻤﻟﺍ ﺢﺘﻓ         3K\n\n"
                            "➩ (23) ﻑ ﺕﺍﺪﻌﻤﻟﺍ ﺢﺘﻓ         3K   |  ➩ (24) ﺯﻮﻔﻟﺍ ﻕﺎﺒﺳ ﺮﻴﻴﻐﺗ             1K\n\n"
                            "➩ (25) ﺮﺴﺨﻳ ﺮﻴﻴﻐﺘﻟﺍ ﻕﺎﺒﺳ            1K   |  ➩ (26) ﺏﺎﺴﺤﻟﺍ ﺥﺎﺴﻨﺘﺳﺍ                7K\n\n"
                            "➩ (27) ﻙﺮﺤﻣ ﺺﺼﺨﻣ                     2.5K |  ➩ (28) ﺔﺼﺼﺨﻣ ﺔﻳﻭﺍﺯ                1.5K\n\n"
                            "➩ (29) ﺺﺼﺨﻣ ﺕﺍﺭﺎﻃﺇ ﻕﺭﺎﺣ           1.5K |  ➩ (30) ﺔﺼﺼﺨﻣ ﺓﺭﺎﻴﺳ ﺔﻓﺎﺴﻣ          1.5K\n\n"
                            "➩ (31) ﺔﺼﺼﺨﻤﻟﺍ ﺓﺭﺎﻴﺴﻟﺍ ﻞﻣﺍﺮ             2K   |  ➩ (32) ﻲﻔﻠﺨﻟﺍ ﺪﺼﻤﻟﺍ ﺔﻟﺍﺯﺇ           2K\n\n"
                            "➩ (33) ﻲﻣﺎﻣﻷﺍ ﺪﺼﻤﻟﺍ ﺔﻟﺍﺯﺇ          2K   |  ➩ (34) ﺏﺎﺴﺤﻟﺍ ﺭﻭﺮﻣ ﺔﻤﻠﻛ ﺮﻴﻴﻐﺗ     2K\n\n"
                            "➩ (35) ﻲﻧﻭﺮﺘﻜﻟﻹﺍ ﺏﺎﺴﺤﻟﺍ ﺪﻳﺮﺑ ﺮﻴﻴﻐﺗ         2K   |  ➩ (36) ﺺﺼﺨﻤﻟﺍ ﺪﺴﻔﻤﻟﺍ              10K\n\n"
                            "➩ (37) ﺺﺼﺨﻣ ﻞﻜﻴﻫ ﻢﻘﻃ               10K  |  ➩ (38) ﺓﺰﻴﻤﻤﻟﺍ ﺕﻼﺠﻌﻟﺍ ﺢﺘﻓ       4.5K\n\n"
                            "➩ (39) ﻥﻭﺍﺮﻛ ﺎﺗﻮﻳﻮﺗ ﻞﻔﻗ ﺢﺘﻓ          2K   |  ➩ (40) ﺓﺮﻴﺸﻌﻟﺍ ﺔﻌﺒﻗ ﺢﺘﻓ (م)         3K\n\n"
                            "➩ (41) ﺮﻛﺬﻟﺍ ﺱﺃﺭ ﺔﻟﺍﺯﺇ             3K  |  ➩ (42) ﻰﺜﻧﻷﺍ ﺱﺃﺭ ﺔﻟﺍﺯﺇ         3K\n\n"
                            "➩ (43) ﺓﺮﻴﺸﻌﻟﺍ ﺔﻤﻗ ﺢﺘﻓ 1 (م)        3K   |  ➩ (44) ﺓﺮﻴﺸﻌﻟﺍ ﺔﻤﻗ ﺢﺘﻓ 2 (م)       3K\n\n"
                            "➩ (45) ﺓﺮﻴﺸﻌﻟﺍ ﺔﻤﻗ ﺢﺘﻓ 3 (M)        3K   |  ➩ (46) ﺓﺮﻴﺸﻌﻟﺍ ﺔﻤﻗ ﺢﺘﻓ 1 (ف م)      3K\n\n"
                            "➩ (47) ﺓﺮﻴﺸﻌﻟﺍ ﺔﻤﻗ ﺢﺘﻓ 2 (ف م)       3K   |  ➩ (48) SLC ﺱﺪﻴﺳﺮﻣ ﻞﻔﻗ ﺢﺘﻓ         4K\n\n"
                            "➩ (49) ﺕﺍﺭﺎﻴﺴﻟﺍ ﻊﻴﻤﺠﻟ ﺔﻋﺮﺴﻟﺍ ﻕﺍﺮﺘﺧﺍ         7.5K   |                  ➩{0}: ﺝﻭﺮﺧ \n\n"
                        )
                    ),
                )
            )

            print(
                Colorate.Horizontal(
                    Colors.blue_to_red, Center.XCenter(Box.DoubleCube(" ➩{0}: ﺝﻭﺮﺧ"))
                )
            )

            print(
                Colorate.Horizontal(
                    Colors.blue_to_red,
                    " ─═════════════════════════════════════[ ☆BEEKEEPER☆ ]══════════════════════════════════─",
                )
            )

            service = IntPrompt.ask(
                f"[bold] [?] SELECT A SERVICE[red][1-{choices[-1]} or 0][/red][/bold]",
                choices=choices,
                show_choices=False,
            )

            if service == 0:  # Exit
                console.print("[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]")
            elif service == 1:  # Increase Money
                console.print(
                    "[bold blue][bold white][?][/bold white] Insert how much money do you want[/bold blue]"
                )
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Saving your data: ", end=None)
                if amount > 0 and amount <= 500000000:
                    if cpm.set_player_money(amount):
                        console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                        console.print(
                            "[bold green]======================================[/bold green]"
                        )
                        answ = Prompt.ask(
                            "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            console.print(
                                "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                            )
                        else:
                            continue
                    else:
                        console.print("[bold red]FAILED (✘)[/bold red]")
                        console.print(
                            "[bold red]please try again later! (✘)[/bold red]"
                        )
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED (✘)[/bold red]")
                    console.print("[bold red]please use valid values! (✘)[/bold red]")
                    sleep(2)
                    continue
            elif service == 2:  # Increase Coins
                console.print(
                    "[bold blue][bold white][?][/bold white] Insert how much coins do you want[/bold blue]"
                )
                amount = IntPrompt.ask("[?] Amount")
                print("[ % ] Saving your data: ", end="")
                if amount > 0 and amount <= 500000:
                    if cpm.set_player_coins(amount):
                        console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                        console.print(
                            "[bold green]======================================[/bold green]"
                        )
                        answ = Prompt.ask(
                            "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            console.print(
                                "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                            )
                        else:
                            continue
                    else:
                        console.print("[bold red]FAILED[/bold red]")
                        console.print("[bold red]Please Try Again[/bold red]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print(
                        "[bold blue] 'Please use valid values[/bold blue]"
                    )
                    sleep(2)
                    continue
            elif service == 3:  # King Rank
                console.print(
                    "[bold red][!] Note:[/bold red]: if the king rank doesn't appear in game, close it and open few times.",
                    end=None,
                )
                console.print(
                    "[bold red][!] Note:[/bold red]: please don't do King Rank on same account twice.",
                    end=None,
                )
                sleep(2)
                console.print("[%] Giving you a King Rank: ", end=None)
                if cpm.set_player_rank():
                    console.print("[bold blue] 'ﺢﺟﺎﻧ[/bold blue]")
                    console.print(
                        "[bold blue] '======================================[/bold blue]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 4:  # Change ID
                console.print("[bold blue] '[?] Enter your new ID[/bold blue]")
                new_id = Prompt.ask("[?] ID")
                console.print("[%] Saving your data: ", end=None)
                if (
                    len(new_id) >= 8
                    and len(new_id)
                    <= 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                    and (" " in new_id) == False
                ):
                    if cpm.set_player_localid(new_id.upper()):
                        console.print("[bold blue] 'ﺢﺟﺎﻧ[/bold blue]")
                        console.print(
                            "[bold blue] '======================================[/bold blue]"
                        )
                        answ = Prompt.ask(
                            "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            console.print(
                                "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                            )
                        else:
                            continue
                    else:
                        console.print("[bold red]FAILED[/bold red]")
                        console.print("[bold red]Please Try Again[/bold red]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold blue] 'Please use valid ID[/bold blue]")
                    sleep(2)
                    continue
            elif service == 5:  # Change Name
                console.print("[bold blue] '[?] Enter your new Name[/bold blue]")
                new_name = Prompt.ask("[?] Name")
                console.print("[%] Saving your data: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(new_name):
                        console.print("[bold blue] 'ﺢﺟﺎﻧ[/bold blue]")
                        console.print(
                            "[bold blue] '======================================[/bold blue]"
                        )
                        answ = Prompt.ask(
                            "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            console.print(
                                "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                            )
                        else:
                            continue
                    else:
                        console.print("[bold red]FAILED[/bold red]")
                        console.print("[bold red]Please Try Again[/bold red]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print(
                        "[bold blue] 'Please use valid values[/bold blue]"
                    )
                    sleep(2)
                    continue
            elif service == 6:  # Change Name Rainbow
                console.print(
                    "[bold blue] '[?] Enter your new Rainbow Name[/bold blue]"
                )
                new_name = Prompt.ask("[?] Name")
                console.print("[%] Saving your data: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        console.print("[bold blue] 'ﺢﺟﺎﻧ[/bold blue]")
                        console.print(
                            "[bold blue] '======================================[/bold blue]"
                        )
                        answ = Prompt.ask(
                            "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            console.print(
                                "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                            )
                        else:
                            continue
                    else:
                        console.print("[bold red]FAILED[/bold red]")
                        console.print("[bold red]Please Try Again[/bold red]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print(
                        "[bold blue] 'Please use valid values[/bold blue]"
                    )
                    sleep(2)
                    continue
            elif service == 7:  # Number Plates
                console.print("[%] Giving you a Number Plates: ", end=None)
                if cpm.set_player_plates():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 8:  # Account Delete
                console.print(
                    "[bold blue] '[!] After deleting your account there is no going back !![/bold blue]"
                )
                answ = Prompt.ask(
                    "[?] Do You want to Delete this Account ?!",
                    choices=["y", "n"],
                    default="n",
                )
                if answ == "y":
                    cpm.delete()
                    console.print("[bold blue] 'ﺢﺟﺎﻧ[/bold blue]")
                    console.print(
                        "[bold blue] '======================================[/bold blue]"
                    )
                    console.print(
                        "[bold blue] f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}[/bold blue]"
                    )
                else:
                    continue
            elif service == 9:  # Account Register
                console.print("[bold blue] '[!] Registring new Account[/bold blue]")
                acc2_email = prompt_valid_value(
                    "[?] Account Email", "Email", password=False
                )
                acc2_password = prompt_valid_value(
                    "[?] Account Password", "Password", password=False
                )
                console.print("[%] Creating new Account: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    console.print("[bold blue] 'ﺢﺟﺎﻧ[/bold blue]")
                    console.print(
                        "[bold blue] '======================================[/bold blue]"
                    )
                    console.print(
                        "[bold blue] f'INFO: In order to tweak this account with Telmun[/bold blue]"
                    )
                    console.print(
                        "[bold blue] 'you most sign-in to the game using this account[/bold blue]"
                    )
                    sleep(2)
                    continue
                elif status == 105:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print(
                        "[bold blue] 'This email is already exists ![/bold blue]"
                    )
                    sleep(2)
                    continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 10:  # Delete Friends
                console.print("[%] Deleting your Friends: ", end=None)
                if cpm.delete_player_friends():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 11:  # Unlock All Lamborghinis
                console.print(
                    "[!] Note: this function takes a while to complete, please don't cancel.",
                    end=None,
                )
                console.print("[%] Unlocking All Lamborghinis: ", end=None)
                if cpm.unlock_all_lamborghinis():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 12:  # Unlock All Cars
                console.print("[%] Unlocking All Cars: ", end=None)
                if cpm.unlock_all_cars():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 13:  # Unlock All Cars Siren
                console.print("[%] Unlocking All Cars Siren: ", end=None)
                if cpm.unlock_all_cars_siren():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 14:  # Unlock w16 Engine
                console.print("[%] Unlocking w16 Engine: ", end=None)
                if cpm.unlock_w16():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 15:  # Unlock All Horns
                console.print("[%] Unlocking All Horns: ", end=None)
                if cpm.unlock_horns():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 16:  # Disable Engine Damage
                console.print("[%] Unlocking Disable Damage: ", end=None)
                if cpm.disable_engine_damage():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 17:  # Unlimited Fuel
                console.print("[%] Unlocking Unlimited Fuel: ", end=None)
                if cpm.unlimited_fuel():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 18:  # Unlock House 3
                console.print("[%] Unlocking House 3: ", end=None)
                if cpm.unlock_houses():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 19:  # Unlock Smoke
                console.print("[%] Unlocking Smoke: ", end=None)
                if cpm.unlock_smoke():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 20:  # Unlock Smoke
                console.print("[%] Unlocking Wheels: ", end=None)
                if cpm.unlock_wheels():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(8)
                    continue
            elif service == 21:  # Unlock Smoke
                console.print("[%] Unlocking Animations: ", end=None)
                if cpm.unlock_animations():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 22:  # Unlock Smoke
                console.print("[%] Unlocking Equipaments Male: ", end=None)
                if cpm.unlock_equipments_male():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 23:  # Unlock Smoke
                console.print("[%] Unlocking Equipaments Female: ", end=None)
                if cpm.unlock_equipments_female():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 24:  # Change Races Wins
                console.print(
                    "[bold blue] '[!] Insert how much races you win[/bold blue]"
                )
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Changing your data: ", end=None)
                if (
                    amount > 0
                    and amount
                    <= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                ):
                    if cpm.set_player_wins(amount):
                        console.print("[bold blue] 'ﺢﺟﺎﻧ[/bold blue]")
                        console.print(
                            "[bold blue] '======================================[/bold blue]"
                        )
                        answ = Prompt.ask(
                            "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            console.print(
                                "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                            )
                        else:
                            continue
                    else:
                        console.print("[bold red]FAILED[/bold red]")
                        console.print("[bold red]Please Try Again[/bold red]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print(
                        "[bold blue] '[!] Please use valid values[/bold blue]"
                    )
                    sleep(2)
                    continue
            elif service == 25:  # Change Races Loses
                console.print(
                    "[bold blue] '[!] Insert how much races you lose[/bold blue]"
                )
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Changing your data: ", end=None)
                if (
                    amount > 0
                    and amount
                    <= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                ):
                    if cpm.set_player_loses(amount):
                        console.print("[bold blue] 'ﺢﺟﺎﻧ[/bold blue]")
                        console.print(
                            "[bold blue] '======================================[/bold blue]"
                        )
                        answ = Prompt.ask(
                            "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                        )
                        if answ == "y":
                            console.print(
                                "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                            )
                        else:
                            continue
                    else:
                        console.print("[bold red]FAILED[/bold red]")
                        console.print(
                            "[bold blue] '[!] Please use valid values[/bold blue]"
                        )
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print(
                        "[bold blue] '[!] Please use valid values[/bold blue]"
                    )
                    sleep(2)
                    continue
            elif service == 26:  # Clone Account
                console.print(
                    "[bold blue] '[!] Please Enter Account Detalis[/bold blue]"
                )
                to_email = prompt_valid_value(
                    "[?] Account Email", "Email", password=False
                )
                to_password = prompt_valid_value(
                    "[?] Account Password", "Password", password=False
                )
                console.print("[%] Cloning your account: ", end=None)
                if cpm.account_clone(to_email, to_password):
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print(
                        "[bold blue] '[!] THAT RECIEVER ACCOUNT IS GMAIL PASSWORD IS NOT VALID OR THAT ACCOUNT IS NOT REGISTERED[/bold blue]"
                    )
                    sleep(2)
                    continue
            elif service == 27:
                console.print(
                    "[bold blue][!] Note[/bold blue]: original speed can not be restored!."
                )
                console.print("[bold blue][!] Enter Car Details.[/bold blue]")
                car_id = IntPrompt.ask("[bold][?] Car Id[/bold]")
                new_hp = IntPrompt.ask("[bold][?]Enter New HP[/bold]")
                new_inner_hp = IntPrompt.ask("[bold][?]Enter New Inner Hp[/bold]")
                new_nm = IntPrompt.ask("[bold][?]Enter New NM[/bold]")
                new_torque = IntPrompt.ask("[bold][?]Enter New Torque[/bold]")
                console.print(
                    "[bold blue][%] Hacking Car Speed[/bold blue]:", end=None
                )
                if cpm.hack_car_speed(car_id, new_hp, new_inner_hp, new_nm, new_torque):
                    console.print("[bold green]SUCCESFUL (✔)[/bold green]")
                    console.print("================================")
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print(
                        "[bold blue] '[!] Please use valid values[/bold blue]"
                    )
                    sleep(2)
                    continue
            elif service == 28:  # ANGLE
                console.print("[bold blue] '[!] ENTER CAR DETALIS[/bold blue]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold blue] '[!] ENTER STEERING ANGLE[/bold blue]")
                custom = IntPrompt.ask(
                    "[red][?]﻿ENTER THE AMOUNT OF ANGLE YOU WANT[/red]"
                )
                console.print("[red][%] HACKING CAR ANGLE[/red]: ", end=None)
                if cpm.max_max1(car_id, custom):
                    console.print("[bold blue] 'ﺢﺟﺎﻧ[/bold blue]")
                    answ = Prompt.ask(
                        "[red][?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ[/red] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 29:  # tire
                console.print("[bold blue] '[!] ENTER CAR DETALIS[/bold blue]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold blue] '[!] ENTER PERCENTAGE[/bold blue]")
                custom = IntPrompt.ask("[pink][?]﻿ENTER PERCENTAGE TIRES U WANT[/pink]")
                console.print("[red][%] Setting Percentage [/red]: ", end=None)
                if cpm.max_max2(car_id, custom):
                    console.print("[bold blue] 'ﺢﺟﺎﻧ[/bold blue]")
                    answ = Prompt.ask(
                        "[bold green][?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ[/bold green] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 30:  # Millage
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold]ENTER NEW MILLAGE![/bold]")
                custom = IntPrompt.ask(
                    "[bold blue][?]﻿ENTER MILLAGE U WANT[/bold blue]"
                )
                console.print(
                    "[bold red][%] Setting Percentage [/bold red]: ", end=None
                )
                if cpm.millage_car(car_id, custom):
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 31:  # Brake
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold]ENTER NEW BRAKE![/bold]")
                custom = IntPrompt.ask("[bold blue][?]﻿ENTER BRAKE U WANT[/bold blue]")
                console.print("[bold red][%] Setting BRAKE [/bold red]: ", end=None)
                if cpm.brake_car(car_id, custom):
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 32:  # Bumper rear
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print(
                    "[bold red][%] Removing Rear Bumper [/bold red]: ", end=None
                )
                if cpm.rear_bumper(car_id):
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 33:  # Bumper front
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print(
                    "[bold red][%] Removing Front Bumper [/bold red]: ", end=None
                )
                if cpm.front_bumper(car_id):
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 75:  # /testin endpoint
                console.print("[bold]ENTER CUSTOM FLOAT DATA[/bold]")
                custom = IntPrompt.ask(
                    "[bold][?] VALUE (e.g. 1 or 0)[/bold]"
                )  # This is the value
                console.print(
                    f"[bold red][%] Setting float key... [/bold red]", end=None
                )
                if cpm.testin(custom):
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold blue]FAILED[/bold blue]")
                    console.print("[bold blue]PLEASE TRY AGAIN[/bold blue]")
                    sleep(2)
                    continue
            elif service == 34:
                console.print("[bold]Enter New Password![/bold]")
                new_password = prompt_valid_value(
                    "[bold][?] Account New Password[/bold]", "Password", password=False
                )
                console.print("[bold red][%] Changing Password [/bold red]: ", end=None)
                if cpm.change_password(new_password):
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white]ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold blue]FAILED[/bold blue]")
                    console.print("[bold blue]PLEASE TRY AGAIN[/bold blue]")
                    sleep(2)
                    continue
            elif service == 36:  # telmunnongodz
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold]ENTER SPOILER ID![/bold]")
                custom = IntPrompt.ask("[bold blue][?]ENTER NEW SPOILER ID[/bold blue]")
                console.print("[bold red][%] SAVING YOUR DATA [/bold red]: ", end=None)
                if cpm.telmunnongodz(car_id, custom):
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 37:  # telmunnongonz
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold]ENTER BODYKIT ID![/bold]")
                custom = IntPrompt.ask("[bold blue][?]INSERT BODYKIT ID[/bold blue]")
                console.print("[bold red][%] SAVING YOUR DATA [/bold red]: ", end=None)
                if cpm.telmunnongonz(car_id, custom):
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 49:  # telmunnongonz
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold]ENTER VALUE FOR STANCE [/bold]")
                custom = IntPrompt.ask("[bold blue][?]INSERT VALUE[/bold blue]")
                console.print("[bold red][%] SAVING YOUR DATA [/bold red]: ", end=None)
                if cpm.incline(car_id, custom):
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 35:
                console.print("[bold]Enter New Email![/bold]")
                new_email = prompt_valid_value(
                    "[bold][?] Account New Email[/bold]", "Email"
                )
                console.print("[bold red][%] Changing Email [/bold red]: ", end=None)
                if cpm.change_email(new_email):
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    answ = Prompt.ask(
                        "[bold][?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ[/bold] ?",
                        choices=["y", "n"],
                        default="n",
                    )
                    if answ == "y":
                        console.print(
                            "[bold white]ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        break
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]EMAIL IS ALREADY REGISTERED [/bold red]")
                    sleep(4)
            elif service == 38:  # SHITTIN
                console.print("[%] Unlocking Premium Wheels..: ", end=None)
                if cpm.shittin():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 39:  # Unlock toyota crown
                console.print(
                    "[!] Note: this function takes a while to complete, please don't cancel.",
                    end=None,
                )
                console.print("[%] Unlocking Toyota Crown: ", end=None)
                if cpm.unlock_crown():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 40:  # Unlock Hat
                console.print("[%] Unlocking Clan Hat: ", end=None)
                if cpm.unlock_hat_m():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 41:  # remove head male
                console.print("[%] Removing Male head: ", end=None)
                if cpm.rmhm():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 42:  # remove head female
                console.print("[%] Removing Female Head: ", end=None)
                if cpm.rmhfm():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 43:  # Unlock TOPM
                console.print("[%] Unlocking Clan clothes Top 1: ", end=None)
                if cpm.unlock_topm():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 44:  # Unlock TOPMz
                console.print("[%] Unlocking Clan clothes Top 1: ", end=None)
                if cpm.unlock_topmz():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 46:  # Unlock TOPF
                console.print("[%] Unlocking Clan clothes Top: ", end=None)
                if cpm.unlock_topf():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 47:  # Unlock TOPFZ
                console.print("[%] Unlocking Clan clothes Top 1: ", end=None)
                if cpm.unlock_topfz():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 48:  # Unlock Mercedes Cls
                console.print("[%] Unlocking Mercedes Cls: ", end=None)
                if cpm.unlock_cls():
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print(
                        "[bold green]======================================[/bold green]"
                    )
                    answ = Prompt.ask(
                        "[?] ؟ﺝﻭﺮﺨﻟﺍ ﺪﻳﺮﺗ ﻞﻫ ?", choices=["y", "n"], default="n"
                    )
                    if answ == "y":
                        console.print(
                            "[bold white] ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ[/bold white]"
                        )
                    else:
                        continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 49:  # Modificar todos los autos
                console.print("[bold]ﺕﺍﺭﺎﻴﺴﻟﺍ ﻊﻴﻤﺟ ﻞﻳﺪﻌﺘﻟ ﻞﻴﺻﺎﻔﺘﻟﺍ ﻞﺧﺩﺃ![/bold]")
                new_hp = IntPrompt.ask("[bold][?] PH ﺔﻛﺮﺸﻟ ﺪﻳﺪﺟ ﻝﻮﺧﺩ[/bold]")
                new_inner_hp = IntPrompt.ask("[bold][?] ﺪﻳﺪﺟ ﻲﻠﺧﺍﺩ PH ﻞﺧﺪﻣ[/bold]")
                new_nm = IntPrompt.ask("[bold][?] MN ﺪﻳﺪﺟ ﻝﻮﺧﺩ[/bold]")
                new_torque = IntPrompt.ask("[bold][?] ﺪﻳﺪﺠﻟﺍ ﻥﺍﺭﻭﺪﻟﺍ ﻡﺰﻋ ﻞﺧﺩﺃ[/bold]")
                console.print(
                    "[bold red][%] ﺕﺍﺭﺎﻴﺴﻟﺍ ﻊﻴﻤﺟ ﻞﻳﺪﻌﺗ [/bold red]: ", end=None
                )
                modificar_todos_los_autos(cpm, new_hp, new_inner_hp, new_nm, new_torque)
                answ = Prompt.ask(
                    "[bold][?]ﻲﺗﺍﺩﺃ ﻡﺍﺪﺨﺘﺳﺍ ﻰﻠﻋ ﻚﻟ ﺍﺮﻜﺷ?[/bold] ?",
                    choices=["y", "n"],
                    default="n",
                )
                if answ == "y":
                    console.print("ﺓﺍﺩﻷﺍ ﻚﻣﺍﺪﺨﺘﺳﻻ ﺍﺮﻜﺷ")
                else:
                    continue
            else:
                continue
            break
        break
