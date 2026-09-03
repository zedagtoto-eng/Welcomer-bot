import os
import discord
from discord.ext import commands

# ============================================================
# CONFIG
# ============================================================

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

WELCOME_CHANNEL_ID = 1544932778079031410

# ============================================================
# BOT SETUP
# ============================================================

intents = discord.Intents.default()
intents.guilds = True
intents.members = True

bot = commands.Bot(
    command_prefix="$",
    intents=intents
)

# ============================================================
# READY
# ============================================================

@bot.event
async def on_ready():
    print(f"✅ {bot.user.tag} is online!")

# ============================================================
# WELCOME
# ============================================================

@bot.event
async def on_member_join(member):

    try:
        channel = await bot.fetch_channel(WELCOME_CHANNEL_ID)

    except discord.NotFound:
        print(f"❌ Channel ID {WELCOME_CHANNEL_ID} does not exist.")
        return

    except discord.Forbidden:
        print("❌ Bot does not have permission to access the welcome channel.")
        return

    except discord.HTTPException as e:
        print(f"❌ Discord API error: {e}")
        return

    # Make sure the channel is a text channel
    if not isinstance(channel, discord.TextChannel):
        print("❌ The welcome channel is not a text channel.")
        return

    avatar = member.display_avatar.replace(
        format="png",
        size=256
    ).url

    embed = discord.Embed(
        title="A New Trader Has Arrived",
        description=(
            f"**Welcome {member.mention} to {member.guild.name}.**\n\n"

            f"🤝 **Secure Middleman Service**\n"
            f"Protect your trades! Use our trusted MM system for all high-value deals.\n\n"

            f"📜 **Server Rules & Terms**\n"
            f"Please review our trading policies before making your first offer.\n\n"

            f"🎟️ **Need Help?**\n"
            f"Open a support ticket anytime to talk directly with staff.\n\n"

            f"**Member #{member.guild.member_count} | ID: {member.id}**"
        ),
        color=discord.Color.from_rgb(255, 105, 180)
    )

    embed.set_thumbnail(url=avatar)
    embed.timestamp = discord.utils.utcnow()

    await channel.send(
        content=member.mention,
        embed=embed
    )

# ============================================================
# LOGIN
# ============================================================

bot.run(DISCORD_TOKEN)
