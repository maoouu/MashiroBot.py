import discord
import json
import random
from discord.ext import commands


class BasicCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("MashiroBot is online.")

    @commands.command()
    async def add(self, ctx, left: int, right: int):
        await ctx.send(f'`{left} + {right} = {left + right}`')

    @commands.command(aliases=['8ball'])
    async def ask(self, ctx, *, question=None):
        # opens json file for bot responses
        file = open("botdata.json", "r")
        intents = json.load(file)

        # if user hasn't entered a question
        if question is None:
            random.shuffle(intents["blank"])
            # respond with the 'blank' intents
            await ctx.send(f'{random.choice(intents["blank"])}')
        else:
            random.shuffle(intents["responses"])
            # respond with the regular response intents
            await ctx.send(f'{random.choice(intents["responses"])}')

    """ 
    @commands.command()
    async def prefix(self, ctx, string=None):
    """
    

def setup(client):
    client.add_cog(BasicCommands(client))

