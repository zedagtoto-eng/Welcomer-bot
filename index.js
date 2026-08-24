 const {
  Client,
  GatewayIntentBits,
  EmbedBuilder
} = require("discord.js");

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMembers
  ]
});

const WELCOME_CHANNEL_ID = "1541096586883367143";

client.once("ready", () => {
  console.log(`✅ ${client.user.tag} is online!`);
});

client.on("guildMemberAdd", async (member) => {
  const channel = member.guild.channels.cache.get(WELCOME_CHANNEL_ID);

  if (!channel) {
    console.log("❌ Welcome channel not found.");
    return;
  }

  const avatar = member.user.displayAvatarURL({
    extension: "png",
    size: 256
  });

  const embed = new EmbedBuilder()
    .setTitle("A New Trader Has Arrived")
    .setDescription(
      `**Welcome ${member} to ${member.guild.name}.**\n\n` +

      `🤝 **Secure Middleman Service**\n` +
      `Protect your trades! Use our trusted MM system for all high-value deals.\n\n` +

      `📜 **Server Rules & Terms**\n` +
      `Please review our trading policies before making your first offer.\n\n` +

      `🎟️ **Need Help?**\n` +
      `Open a support ticket anytime to talk directly with staff.\n\n` +

      `**Member #${member.guild.memberCount} | ID: ${member.id}**`
    )
    .setThumbnail(avatar)
    .setColor("#8B4513")
    .setTimestamp();

  await channel.send({
    content: `${member}`,
    embeds: [embed]
  });
});

client.login(process.env.TOKEN);
