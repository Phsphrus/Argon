#imports
import requests
import colorama
import time
import json
colorama.init()


# function to clear screen
def clear_screen():
    print("\033c", end="")

# main menu
while True:
  clear_screen()
  print(colorama.Fore.RED + """
██████╗░██╗░░░██╗███████╗███████╗███████╗██████╗░  ░██╗░░░░░░░██╗██╗░░██╗  ████████╗░█████╗░░█████╗░██╗░░░░░
██╔══██╗██║░░░██║██╔════╝██╔════╝██╔════╝██╔══██╗  ░██║░░██╗░░██║██║░░██║  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
██████╔╝██║░░░██║█████╗░░█████╗░░█████╗░░██████╔╝  ░╚██╗████╗██╔╝███████║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
██╔═══╝░██║░░░██║██╔══╝░░██╔══╝░░██╔══╝░░██╔══██╗  ░░████╔═████║░██╔══██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
██║░░░░░╚██████╔╝██║░░░░░██║░░░░░███████╗██║░░██║  ░░╚██╔╝░╚██╔╝░██║░░██║  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚═╝░░░░░░╚═════╝░╚═╝░░░░░╚═╝░░░░░╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝""" + colorama.Style.RESET_ALL)
  print(colorama.Fore.LIGHTCYAN_EX + """
║════════════════════════║════════════════════════║
║ [3] - Webhook messager ║ [4] - Credits          ║
║ [2] - Webhook spammer  ║ [5] - Webhook Checker  ║
║ [1] - Webhook deleter  ║ [6] - Webhook validity ║
║════════════════════════║════════════════════════║""" + colorama.Style.RESET_ALL)
  Mainmenu = input(colorama.Fore.LIGHTBLUE_EX + "Choose an option: " + colorama.Style.RESET_ALL)

# message sender-----------------------------------------------------------------------------
  if Mainmenu == "3":
        senderURL = input(colorama.Fore.LIGHTBLUE_EX + "What is the webhook url? " + colorama.Style.RESET_ALL)
        senderMessage = input(colorama.Fore.LIGHTBLUE_EX + "What is your message that will be sent? " + colorama.Style.RESET_ALL)
        discord_webhook_url = senderURL
        message = {"content": senderMessage}
        response = requests.post(discord_webhook_url, json=message)
        if response.status_code == 204:
            print(colorama.Fore.GREEN + "Webhook message sent successfully." + colorama.Style.RESET_ALL)
            print(colorama.Fore.LIGHTBLUE_EX + "Press 1 to goto the main menu" + colorama.Style.RESET_ALL)
        else:
            print(colorama.Fore.RED + f"Error sending webhook message. Status code: {response.status_code}" + colorama.Style.RESET_ALL)
            print(colorama.Fore.LIGHTBLUE_EX + "Press 1 to goto the main menu" + colorama.Style.RESET_ALL)
        SenderMenu = input(colorama.Fore.LIGHTBLUE_EX + "Choose an option: " + colorama.Style.RESET_ALL)
        if SenderMenu == "1":
            # go back to main menu
            time.sleep(1)
            clear_screen()
        continue
# deleter-------------------------------------------------------------------------------------
  if Mainmenu == "1":
        while True:
            webhookdel = input(colorama.Fore.LIGHTBLUE_EX + "Enter the webhook to delete: " + colorama.Style.RESET_ALL)
            response = requests.delete(webhookdel)
            if response.status_code == 204:
                print(colorama.Fore.GREEN + "Webhook deleted successfully." + colorama.Style.RESET_ALL)
            else: 
                print(colorama.Fore.RED + f"Error deleting webhook. Status code: {response.status_code}" + colorama.Style.RESET_ALL)
              
            print(colorama.Fore.LIGHTBLUE_EX + "Press 1 to goto the main menu " + colorama.Style.RESET_ALL)
            del_menu = input(colorama.Fore.LIGHTBLUE_EX + "Choose an option: " + colorama.Style.RESET_ALL)
            if del_menu == "1":
                # go back to main menu
                time.sleep(1)
                clear_screen()
                break

# Webhook checker-----------------------------------------------------------------------------
  if Mainmenu == "5":
    while True:
        webhook_url = input(colorama.Fore.LIGHTBLUE_EX + "Enter the Discord webhook URL: " + colorama.Style.RESET_ALL)
        # Converts the json request to readable text
        response = requests.get(webhook_url)
        response_json = json.loads(response.text)
        if 'user' in response_json and 'username' in response_json['user'] and 'discriminator' in response_json['user']:
            makersuser = response_json['user']['username']
            makerstag = response_json['user']['discriminator']
            makersid = response_json['user']['id']
            avatar_url = f"https://cdn.discordapp.com/avatars/{makersid}/{response_json['user']['avatar']}.png"
            makersbanner = response_json['user']['banner_color']
            pubflags = response_json['user']['public_flags']
            prvflags = response_json['user']['flags']
            avatardecoration = response_json['user']['avatar_decoration']
            print(colorama.Fore.RED + "WEBHOOK INFO" + colorama.Style.RESET_ALL)
            print(colorama.Fore.LIGHTBLUE_EX + f"Person that made the webhook: {makersuser}#{makerstag}" + colorama.Style.RESET_ALL)
            print(colorama.Fore.LIGHTBLUE_EX + f"Person that made the webhook id: {makersid}" + colorama.Style.RESET_ALL)
            print(colorama.Fore.LIGHTBLUE_EX + f"Person that made the webhook banner: {makersbanner}" + colorama.Style.RESET_ALL)
            print(colorama.Fore.LIGHTBLUE_EX + f"Person that made the webhook avatar decoration: {avatardecoration}" + colorama.Style.RESET_ALL)
            print(colorama.Fore.LIGHTBLUE_EX + f"Person that made the webhook public flags: {pubflags}" + colorama.Style.RESET_ALL)
            print(colorama.Fore.LIGHTBLUE_EX + f"Person that made the webhook prv flags: {prvflags}" + colorama.Style.RESET_ALL)
            print(colorama.Fore.LIGHTBLUE_EX + f"Avatar URL: {avatar_url}" + colorama.Style.RESET_ALL)
          
            print(colorama.Fore.LIGHTBLUE_EX + "Press 1 to goto the main menu" + colorama.Style.RESET_ALL)
        CheckMenu = input(colorama.Fore.LIGHTBLUE_EX + "Choose an option: " + colorama.Style.RESET_ALL)
        if CheckMenu == "1":
            # go back to main menu
            time.sleep(1)
            clear_screen()
            break   
          # webhook validity------------------------------------------------------------------------
  if Mainmenu == "6":
        senderURL = input(colorama.Fore.LIGHTBLUE_EX + "What is the webhook url? " + colorama.Style.RESET_ALL)
        message = {"content": "Test"}
        response = requests.post(senderURL, json=message)
        if response.status_code == 204:
            print(colorama.Fore.GREEN + "Webhook is alive." + colorama.Style.RESET_ALL)
            print(colorama.Fore.LIGHTBLUE_EX + "Press 1 to goto the main menu" + colorama.Style.RESET_ALL)
        else:
            print(colorama.Fore.RED + f"""Webhook Is not working, Code: {response.status_code}
            404 = Does Not Exist (deleted)
            429 = Rate Limited (too many messages sent)
            401 Invalid Webhook Token (never existed)""" + colorama.Style.RESET_ALL)
            print(colorama.Fore.LIGHTBLUE_EX + "Press 1 to goto the main menu" + colorama.Style.RESET_ALL)
        SenderMenu = input(colorama.Fore.LIGHTBLUE_EX + "Choose an option: " + colorama.Style.RESET_ALL)
        if SenderMenu == "1":
            # go back to main menu
            time.sleep(1)
            clear_screen()
        continue

# credits-------------------------------------------------------------------------------------
  if Mainmenu == "4":
        while True:
            clear_screen()
            print(colorama.Fore.LIGHTCYAN_EX + """
║════════════════════════║
║ just a pufferfish#1234 ║
║ Phsphrus - github      ║
║ Replit - Easy Testing  ║
║ [1] Back               ║
║════════════════════════║""" + colorama.Style.RESET_ALL)
            credit_menu = input(colorama.Fore.LIGHTBLUE_EX + "Choose an option: " + colorama.Style.RESET_ALL)
            if credit_menu == "1":
                # go back to main menu
                time.sleep(1)
                clear_screen()
                break
# Webhook spammer-----------------------------------------------------------------------------
if Mainmenu == "2":
    senderURL = input(colorama.Fore.LIGHTBLUE_EX + "What is the webhook url? " + colorama.Style.RESET_ALL)
    senderMessage = input(colorama.Fore.LIGHTBLUE_EX + "What is your message that will be sent? " + colorama.Style.RESET_ALL)
    print(colorama.Fore.RED + "WARNING YOU MUST RELOAD THE PROGRAM TO GET TO THE MAIN MENU" + colorama.Style.RESET_ALL)
    while True:
        discord_webhook_url = senderURL
        message = {"content": senderMessage}
        response = requests.post(discord_webhook_url, json=message)
        if response.status_code == 204:
            print(colorama.Fore.GREEN + "Webhook message sent successfully." + colorama.Style.RESET_ALL)
        else:     
            print(colorama.Fore.RED + f"Error sending webhook message. Status code: {response.status_code}" + colorama.Style.RESET_ALL)
        time.sleep(0.4)
    # Made with love fuck the skids made by Liam or Phsphrus on git