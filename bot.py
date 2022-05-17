import discord

intents = discord.Intents.default()
intents.members = True #So you can use on_member_join event

client = discord.Client(intents=intents)

banlist = ["Massa"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    print(f'New member {member.name}, joined the server!')
    #if any(banned in member.name for banned in banlist):
    if member.name.lower() == "massa":
        print(f'{member.name} matches the target string!')
        try:
            print(f'Banning {member.name}!')
            await member.ban(reason='[your_ban_reason_here]')
        except:
            print(f'Failed to ban {member.name}... :c')
        return
    else:
        print(f'No need to ban {member.name}, does not match the target string!')

client.run('token_here')
