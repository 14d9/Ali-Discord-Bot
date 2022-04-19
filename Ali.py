# Libraries #
import disnake
from disnake import Embed
from disnake.ext import commands
import requests

# BOT Prefix #
bot = commands.Bot(command_prefix='!')

# On Ready #
@bot.event
async def on_ready():
    print("""
   ___  _ _  __    __     ___  ____  ______
  / _ \(_) |/_/__ / /    / _ )/ __ \/_  __/
 / ___/ />  </ -_) /__  / _  / /_/ / / /   
/_/  /_/_/|_|\__/____/ /____/\____/ /_/    
                                           
    """)
    print("The Bot Is Online!")
    print(f'Your Bot Name : {bot.user}')
    print("Thank you for using my bot <3")
    print("Created By PiXeL#1337")
    activity = disnake.Game(name="Created By PiXeL#1337")
    await bot.change_presence(status=disnake.Status.idle, activity=activity)

# Help #
@bot.command()
async def helpme(ctx):
  embed = Embed(title='Ali | Help', description=f'**Bot Commands :\n\n!ip [IP]\n!discord [ServerLink]\n!tellonym [username]\n!cfx [FiveMServerCFX]\n\nAli : https://discord.gg/ali\nSelix : https://discord.gg/ZPNQkWHpAQ\nWe Love You <3**', color=0x000000)
  embed.set_image(url='https://cdn.discordapp.com/attachments/838674685452484608/939825250714152970/600x200.png')
  embed.set_footer(text="Created By Ali || PiXeL#1337", icon_url="https://cdn.discordapp.com/attachments/838674685452484608/939825286021787708/0.png")
  await ctx.send(embed=embed)

# Get IP information #
@bot.command()
async def ip(ctx, *, arg):
  req = requests.get(f"http://ipwhois.app/json/{arg}")
  latitude = req.json()["latitude"]
  longitude = req.json()["longitude"]
  fortheflag = str(req.json()["country_code"]).lower()
  embed = Embed(title='Ali | Get IP information', description=f'**IP : {req.json()["ip"]}\nIP -> Success : {req.json()["success"]}\nIP -> Type : {req.json()["type"]}\nIP -> Country : {req.json()["country"]}\nIP -> Country Flag : **:flag_{fortheflag}:**\nIP -> Country Code : {req.json()["country_code"]}\nIP -> Country Capital : {req.json()["country_capital"]}\nIP -> Country Phone : {req.json()["country_phone"]}\nIP -> Region : {req.json()["region"]}\nIP -> City : {req.json()["city"]}\nIP ->  Google Maps : https://www.google.com/maps/search/{latitude},+{longitude}\nIP -> TimeZone : {req.json()["timezone"]}\nIP -> TimeZone Name : {req.json()["timezone_name"]}\nIP -> TimeZone dst Offset : {req.json()["timezone_dstOffset"]}\nIP -> TimeZone gmt Offset : {req.json()["timezone_gmtOffset"]}\nIP -> TimeZone gmt : {req.json()["timezone_gmt"]}\nIP -> Currency : {req.json()["currency"]}\nIP -> Currency Code : {req.json()["currency_code"]}\nIP -> Currency Symbol : {req.json()["currency_symbol"]}\nIP -> Currency Plural : {req.json()["currency_plural"]}\nIP -> Continent : {req.json()["continent"]}\nIP -> Continent Code : {req.json()["continent_code"]}**', color=0x000000)
  embed.set_image(url='https://cdn.discordapp.com/attachments/838674685452484608/939825250714152970/600x200.png')
  embed.set_footer(text="Created By Ali || PiXeL#1337", icon_url="https://cdn.discordapp.com/attachments/838674685452484608/939825286021787708/0.png")
  await ctx.send(embed=embed)

# Get FiveM Server information #
@bot.command()
async def cfx(ctx, *, arg):
  fheaders = {
    'path': f'/api/servers/single/{arg}',
    'accept': 'application/json',
    'accept-language': 'en',
    'user-agent': 'ios:2.65.0:488:14:iPhone13,3',
  }
  req = requests.get(f"https://servers-frontend.fivem.net/api/servers/single/{arg}",headers=fheaders)
  if req.status_code == 200:
    embed = Embed(title='Ali | Get FiveM Server information', description=f'**IP : {req.json()["Data"]["connectEndPoints"]}\nServer Name : {req.json()["Data"]["hostname"]}\nPlayers : {req.json()["Data"]["clients"]}\nUpVotes : {req.json()["Data"]["upvotePower"]}\nMax Players : {req.json()["Data"]["sv_maxclients"]}\nOwner Name : {req.json()["Data"]["ownerName"]}\nOwner Profile : {req.json()["Data"]["ownerProfile"]}\nBanner Connecting : {req.json()["Data"]["vars"]["banner_connecting"]}\nBanner Detail : {req.json()["Data"]["vars"]["banner_detail"]}\nsv_projectName : {req.json()["Data"]["vars"]["sv_projectName"]}\nsv_projectDesc : {req.json()["Data"]["vars"]["sv_projectDesc"]}\nonesync_enabled : {req.json()["Data"]["vars"]["onesync_enabled"]}\nLocale : {req.json()["Data"]["vars"]["locale"]}**', color=0x000000)
    embed.set_image(url='https://cdn.discordapp.com/attachments/838674685452484608/939825250714152970/600x200.png')
    embed.set_footer(text="Created By Ali || PiXeL#1337", icon_url="https://cdn.discordapp.com/attachments/838674685452484608/939825286021787708/0.png")
    await ctx.send(embed=embed)
  elif req.status_code == 404:
    isnt = "'"
    embed = Embed(title='Ali | Get FiveM Server information', description=f'**:x: Sorry, this Server isn{isnt}t available.**', color=0x000000)
    embed.set_image(url='https://cdn.discordapp.com/attachments/838674685452484608/939825250714152970/600x200.png')
    embed.set_footer(text="Created By Ali || PiXeL#1337", icon_url="https://cdn.discordapp.com/attachments/838674685452484608/939825286021787708/0.png")
    await ctx.send(embed=embed)

# Get Discord Server information #
@bot.command()
async def discord(ctx, *, arg):
  dheaders = {
    'accept': 'application/json',
    'accept-language': 'en',
    'user-agent': 'ios:2.65.0:488:14:iPhone13,3',
  }
  req = requests.get(f"https://discord.com/api/v9/invites/{arg}?with_counts=true&with_expiration=true",headers=dheaders)
  if req.status_code == 200:
    id = req.json()["guild"]["id"]
    avatar = req.json()["guild"]["icon"]
    banner = req.json()["guild"]["banner"]
    splash = req.json()["guild"]["splash"]
    embed = Embed(title='Ali | Get Discord Server information', description=f'**Server Name : {req.json()["guild"]["name"]}\nServer Description : {req.json()["guild"]["description"]}\nServer ID : {req.json()["guild"]["id"]}\nServer Avatar : https://cdn.discordapp.com/icons/{id}/{avatar}.webp?size=96\nServer Banner : https://cdn.discordapp.com/banners/{id}/{banner}.webp?size=2048\nServer Invite Background : https://cdn.discordapp.com/splashes/{id}/{splash}.jpg?size=2048\nOnline Members : {req.json()["approximate_presence_count"]}\nAll Members : {req.json()["approximate_member_count"]}\nServer Boosts : {req.json()["guild"]["premium_subscription_count"]}\nCustom Invite Link : {req.json()["guild"]["vanity_url_code"]}\nServer Level : {req.json()["guild"]["verification_level"]}\nnsfw : {req.json()["guild"]["nsfw"]}\nnsfw Level : {req.json()["guild"]["nsfw_level"]}**', color=0x000000)
    embed.set_image(url='https://cdn.discordapp.com/attachments/838674685452484608/939825250714152970/600x200.png')
    embed.set_footer(text="Created By Ali || PiXeL#1337", icon_url="https://cdn.discordapp.com/attachments/838674685452484608/939825286021787708/0.png")
    await ctx.send(embed=embed)
  elif req.status_code == 404:
    isnt = "'"
    embed = Embed(title='Ali | Get Discord Server information', description=f'**:x: Sorry, this Server isn{isnt}t available.**', color=0x000000)
    embed.set_image(url='https://cdn.discordapp.com/attachments/838674685452484608/939825250714152970/600x200.png')
    embed.set_footer(text="Created By Ali || PiXeL#1337", icon_url="https://cdn.discordapp.com/attachments/838674685452484608/939825286021787708/0.png")
    await ctx.send(embed=embed)

# Get Tellonym Account information #
@bot.command()
async def tellonym(ctx, *, arg):
  tellonymheaders = {
    'accept': 'application/json',
    'accept-language': 'en',
    'user-agent': 'ios:2.65.0:488:14:iPhone13,3',
  }
  req = requests.get(f"https://api.tellonym.me/profiles/name/{arg}?limit=25",headers=tellonymheaders)
  if req.status_code == 200:
    tellonymflag = str(req.json()["countryCode"]).lower()
    embed = Embed(title='Ali | Get Tellonym Account information', description=f'**Username : {req.json()["username"]}\nDisplay Name : {req.json()["displayName"]}\nID : {req.json()["id"]}\nFollowing : {req.json()["followingCount"]}\nFollowers : {req.json()["followerCount"]}\nAboutMe : {req.json()["aboutMe"]}\nTells : {req.json()["tellCount"]}\nActive : {req.json()["isActive"]}\nCountry : **:flag_{tellonymflag}:**\nVerified : {req.json()["isVerified"]}**', color=0x000000)
    embed.set_thumbnail(url=f'https://userimg.tellonym.me/xs/{req.json()["avatarFileName"]}')
    embed.set_image(url='https://cdn.discordapp.com/attachments/838674685452484608/939825250714152970/600x200.png')
    embed.set_footer(text="Created By Ali || PiXeL#1337", icon_url="https://cdn.discordapp.com/attachments/838674685452484608/939825286021787708/0.png")
    await ctx.send(embed=embed)
  elif req.status_code == 404:
    isnt = "'"
    embed = Embed(title='Ali | Get Tellonym Account information', description=f'**:x: Sorry, this Account isn{isnt}t available.**', color=0x000000)
    embed.set_image(url='https://cdn.discordapp.com/attachments/838674685452484608/939825250714152970/600x200.png')
    embed.set_footer(text="Created By Ali || PiXeL#1337", icon_url="https://cdn.discordapp.com/attachments/838674685452484608/939825286021787708/0.png")
    await ctx.send(embed=embed)

# Your Token | You can get the token from : https://discord.com/developers/applications #
bot.run("YOURTOKEN")
