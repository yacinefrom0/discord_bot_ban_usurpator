import discord
from discord import Member
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True #So you can use on_member_join event

client = discord.Client(intents=intents)

# === ↓ SETTINGS ↓ ============================================================
target_strings = [
    'verification',
    'massa',
    'vincent',
    'seb',
    'damir',
]

whitelisted_user_ids = [
    885846376045506560,  # your_admin_user_id_here
    123456789123456789,  # your_moderator_user_id_here
]

ban_reason = 'Verification, the server name or moderator names are not allowed in the username to prevent scammers.'
bot_token = 'your_token'
# === ↑ SETTINGS ↑ ============================================================

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member: Member):
    """
    Checks the member names against illegal names, bans if illegal names are found

    :param member: (Member) Object of said member
    """

    print(f'Checking member {member.name}...')
    member_names = [member.name, member.nick, member.display_name]
    member_banned = False

    if member.id not in whitelisted_user_ids:
        for target_string in target_strings:
            if member_banned is False:
                for member_name in member_names:

                    if (member_name is not None) and (target_string in member_name.lower()):
                        print(f'{member.name} matches the target string ({target_string})!')

                        try:
                            print(f'Banning {member.name}!')
                            await member.ban(reason=ban_reason)
                            member_banned = True
                            break
                        except:
                            print(f'Failed to ban {member.name}... :c')
    else:
        print(f'Member {member.name} is in whitelist, ignoring...')

    if member_banned is False:
        print(f'No need to ban {member.name}, does not match the target strings!')

@client.event
async def on_member_update(before: Member, after: Member):
    """
    Executes when a member updates their profiler

    :param before: (Member) Object of said member before the profile changes
    :param after: (Member) Object of said member after the profile changes
    """

    await on_member_join(member=after)

client.run(bot_token)
