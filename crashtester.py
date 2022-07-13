import os,sys,subprocess,re,os,time
from discord_webhook import DiscordWebhook, DiscordEmbed
from configparser import ConfigParser
#startup message
print("""Made by n,#2896
      https://discord.gg/agS4YTzERs
      paypal > astroconfigs@gmail.com
      s/o slay
      """)

#configparser
parser = ConfigParser()
parser.read('config/settings.ini')
(parser.sections())
Client_Webhook = (parser.get('Settings', 'Webhook'))
#Embed
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/996674217951101018/dugTwBqLbSZk-zJyzodT7okgiXOEvheqbG9T7xUgwkPeTrM-N9adNeUdrvyEEyxgjLli')
embed = DiscordEmbed(title='Your Viridian Wasnt Running', description='Sucessfully Restarted', color='03b2f8')
embed.set_footer(text='n,#2896 | s/o slaysof')
webhook.add_embed(embed)


while True:
    if "Cry.ConsoleApp.exe" in str(os.popen('tasklist').read()):
        pass
    else:
        os.startfile('Cry.ConsoleApp.exe')
        try:
            response = webhook.execute()
        except:
            pass