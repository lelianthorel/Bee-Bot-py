import discord
from discord.ext import commands
import asyncio
import random


bot = commands.Bot(command_prefix="!")


class ErrorCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        try:
            # Si la commande n'est pas trouvé / n'existe pas.
            if isinstance(error, commands.CommandNotFound):
                embed_erreur = discord.Embed(title="<:x_:985826783159021628> Erreur !",
                                             description=f"La commande ``{ctx.message.content}`` n'existe pas. Veuillez réitérer votre demande.", color=0xD00000)

                embed_erreur.set_footer(
                    text="ce message sera supprimé dans 15 secondes.")
                msg = await ctx.reply(embed=embed_erreur)

                if ctx.channel.type == discord.ChannelType.private:
                    return

                await asyncio.sleep(15)
                await ctx.message.delete()
                await msg.delete()

            # Si la personne n'a pas les permissions nécésaires pour exécuter la commande.
            elif isinstance(error, commands.MissingPermissions):
                embed = discord.Embed(
                    description='⚠️ ┃ Tu n\'as pas les permissions nécessaires pour effectuer '
                                'cette commande.', color=0xd00000
                )
                embed.set_footer(
                    text="ce message sera supprimé dans 15 secondes.")
                msg = await ctx.reply(embed=embed)
                if ctx.channel.type == discord.ChannelType.private:
                    return
                await asyncio.sleep(15)
                await ctx.message.delete()
                await msg.delete()
            else:
                embed = discord.Embed(title="<:x_:985826783159021628> Erreur !",
                                      description=f"Contenue de l'erreur : ``{error}``", color=0xD00000)

                embed.set_footer(
                    text="Si tu vois ce message, contacte le développeur.")
                await ctx.reply(embed=embed)

        # Pour tout les autres types d'erreurs non géré au dessus.     
        except Exception as error:
            embed = discord.Embed(title="<:x_:985826783159021628> Erreur !",
                                  description=f"Contenue de l'erreur : ``{error}``", color=0xD00000)

            embed.set_footer(
                text="Si tu vois ce message, contacte le développeur.")
            await ctx.reply(embed=embed)
