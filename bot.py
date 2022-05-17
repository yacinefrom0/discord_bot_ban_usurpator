import discord

intents = discord.Intents.default()
intents.members = True #So you can use on_member_join event

client = discord.Client(intents=intents)
#banlist = ["Massa"] #If you want to ban every people that have "Massa" string in her username use that

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_member_join(member):
    print("New member !")
    #if any(banned in member.name for banned in banlist): #If you want to ban every people that have "Massa" string in her username use that
    if member.name == "Massa": #Only ban Massa username and let the others like MassaBot / MassaPaul etc
        print("Found the target !")
        try:
            print("Je banni le saligot !")
            await member.ban(reason="Vous avez été banni car votre username est interdit.")
        except:
            print("Couldn't ban the target :(")
        return

client.run('votre_id')
