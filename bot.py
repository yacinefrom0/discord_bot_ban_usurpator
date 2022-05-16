import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

banlist = ["word1", "word2"]

@client.event
async def on_member_join(member):
    print("New member !")
    if any(banned in member.name for banned in banlist):
        print("Found the target !")
        await member.ban()
        print("Il a été banni :D")
        return

client.run('Votre ID here')
