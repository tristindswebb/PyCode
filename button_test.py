import discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


#Should be selectClass, but I changed how the buttons worked and dont wish to change every reference right now.
#this class is basically a small "Hero Class" selector allowing the player to choose a class, its not very extensible but theres no need for that right now.
#This needs to be completely rewritten - user_to_db has no use at the moment - remember to change database
#Medium priority - TW 22/11/2023 9:00AM
class selectKnight(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Warrior!", style=discord.ButtonStyle.primary, emoji="🦾")
    async def button_warrior(self, interaction, button):
        for child in self.children:
            child.disabled=True
        await interaction.response.edit_message(view=self, content="You have picked Warrior!")
        user_to_db = interaction.user.id
        roles = await interaction.guild.fetch_roles()
        role = [role for role in roles if role.name == "Warrior"]
        await interaction.user.add_roles(role[0])

    @discord.ui.button(label="Ninja!", style=discord.ButtonStyle.primary, emoji="🥷")
    async def button_ninja(self, interaction, button):
        for child in self.children:
            child.disabled=True
        await interaction.response.edit_message(view=self, content="You have picked Ninja!")
        user_to_db = interaction.user.id
        roles = await interaction.guild.fetch_roles()
        role = [role for role in roles if role.name == "Ninja"]
        await interaction.user.add_roles(role[0])

    @discord.ui.button(label="Mage!", style=discord.ButtonStyle.primary, emoji="🧙")
    async def button_mage(self, interaction, button):
        for child in self.children:
            child.disabled=True
        await interaction.response.edit_message(view=self, content="You have picked Mage!")
        user_to_db = interaction.user.id
        roles = await interaction.guild.fetch_roles()
        role = [role for role in roles if role.name == "Mage"]
        await interaction.user.add_roles(role[0])

    @discord.ui.button(label="Archer!", style=discord.ButtonStyle.primary, emoji="🏹")
    async def button_archer(self, interaction, button):
        for child in self.children:
            child.disabled=True
        await interaction.response.edit_message(view=self, content="You have picked Archer!")
        user_to_db = interaction.user.id
        roles = await interaction.guild.fetch_roles()
        role = [role for role in roles if role.name == "Archer"]
        await interaction.user.add_roles(role[0])

    @discord.ui.button(label="None", style=discord.ButtonStyle.primary, emoji="❌")
    async def button_cancel(self, interaction, button:discord.ui.Button):
        for child in self.children:
            child.disabled=True
        await interaction.response.edit_message(view=self, content="You have not picked a class!")
        user_to_db = interaction.user.id

#This needs to be changed - it used to exit to get roles, however if the bot goes down the ID changes making it only useful for the initial creation of roles
#low priority - TW 23/11/2023 5:36PM
@client.event
async def on_setup(message):
    intents.message_content = True
    client = discord.Client(intents=intents)
    if message.author == client.user:
        return
    
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    global war_role
    global ninja_role
    global mage_role
    global archer_role

    war_role = await message.guild.create_role(name="Warrior", colour=discord.Colour.greyple())
    ninja_role = await message.guild.create_role(name="Ninja", colour=discord.Colour.dark_theme())
    mage_role = await message.guild.create_role(name="Mage", colour=discord.Colour.dark_purple())
    archer_role = await message.guild.create_role(name="Archer", colour=discord.Colour.dark_green())


