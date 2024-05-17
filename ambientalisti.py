import discord
from discord.ext import commands
import random
import time
import os
intents = discord.Intents.default()
intents.message_content = True
num1=0
num2=1
bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l-accesso come {bot.user}')
@bot.command()
async def malattie(ctx):
    await ctx.send ("Le mallatie si trovano nei rifiuti organici buttatti nelle discariche a cielo aperto,possono fermentare e creare infenzioni batteriche o raramente parrssiti che attaccano gli umani")
@bot.command()
async def spreco_cibo(ctx):
    await ctx.send ("Nel 2022, la FAO ha riportato alcuni dati globali piuttosto drammatici. Il 14 percento del cibo viene perso prima della commercializzazione mentre il 17%, pari a 931 milioni di tonnellate, viene sprecato dai consumatori e/o retail")
@bot.command()
async def spreco_plastica(ctx):
    await ctx.send ("Tuttavia, solo una piccola frazione di questa valanga di rifiuti di plastica viene riciclata – il 9%, appunto – mentre il 19% viene incenerito e quasi il 50 percento finisce nelle discariche legali.")
@bot.command()
async def provenienza_serra(ctx):
    await ctx.send ("L'uso di energia è responsabile del 77,1 percento delle emissioni di gas effetto serra, circa un terzo del quale attribuibile ai trasporti. La quota rimanente di emissioni proviene per il 10,55 percento dall'agricoltura, per il 9,10% dai processi industriali e di utilizzo del prodotto e per il 3,32 percento dalla gestione dei rifiuti.")
@bot.command()
async def plastiturismo(ctx):
    await ctx.send ("Con l'inquinamento dei mari, il turismo diminuisce perchè dove c'era aria fresca o spiaggie pulite ora c'è una discarica.")
@bot.command()
async def pesticidi(ctx):
    await ctx.send ("i pesticidi possono essere dei potenti inquinanti. Essi causano inquinamento, specialmente inquinamento idrico. Grazie alle piogge, finiscono con il penetrare nelle falde acquifere, contaminando corsi d'acqua, laghi e mare. Possono causare la moria di pesci e piccoli organismi, animali e vegetali.")
bot.run("TOKEN")
