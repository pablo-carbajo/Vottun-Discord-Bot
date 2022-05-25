import discord
import asyncio 
import os 
from discord.ext import commands 
from discord_slash import SlashCommand
import urllib.request as ur 
import json
import keepalive


discord_token = os.environ["discord token"]
etherscan_api_keyn = os.environ["etherscan_api_key"]

bot = commands.Bot(
	command_prefix="k!", #  Prefix for the bot
	case_insensitive=True, #  case-sensitive
  intents=discord.Intents.all(), #  特權網關意圖(接收特殊事件)
  help_command=None #  No help command
)

slash = SlashCommand(bot, sync_commands=True)

## continue: https://replit.com/@PabloCarbajo/Kizmeow-NFT-Tracker-V2#main.py