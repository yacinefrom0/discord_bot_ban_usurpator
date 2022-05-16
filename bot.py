import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

banlist = ["Massa"]

@client.event
async def on_member_join(member):
    print("New member !")
    if any(banned in member.name for banned in banlist):
        print("Found the target !")
        try:
            print("Je banni le saligot !")
            await member.ban(reason="Vous avez banni car nous soupçonons que vous usurper Massa")
        except:
            print("Couldn't ban the target :(")
        return

client.run('votre_id_here')
