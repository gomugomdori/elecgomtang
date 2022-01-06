import discord
import asyncio
from gtts import gTTS
from discord.utils import get
from discord.ext import commands
import pickle

bot = commands.Bot(command_prefix='')

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=None)



@bot.command()
async def 출근(ctx, *, channel: discord.VoiceChannel=None):    
    try:
        channel = ctx.author.voice.channel
        global vc
        vc=await ctx.message.author.voice.channel.connect()
        await ctx.send(f'{channel}에 출근했다곰')
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
            await ctx.send(f'**{channel}**에 출장간다곰')
        except:
            await ctx.send('너부터 출근해라곰')

    

@bot.command(name="\'")
async def say(ctx, *, text=None):
    
    if not text:
        await ctx.send(f"[어이, {ctx.author.mention}.. 말로 해라..]")
        return

    vc = ctx.voice_client # We use it more then once, so make it an easy variable
    if not vc:
        # We are not currently in a voice channel
        await ctx.send("음성 채널에 참여하라곰")
        return

    # Lets prepare our text, and then save the audio ctx.gomfile
    tts = gTTS(text=text, lang="ko")
    tts.save("text.mp3")

    try:
        # Lets play that mp3 ctx.gomfile in the voice channel
        vc.play(discord.FFmpegPCMAudio('text.mp3'), after=lambda e: print(f"Finished playing: {e}"))

        # Lets set the volume to 1
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 1

    # Handle the exceptions that can occur
    except ClientException as e:
        await ctx.send(f"A client exception occured:\n`{e}`")
    except TypeError as e:
        await ctx.send(f"TypeError exception:\n`{e}`")
    except OpusNotLoaded as e:
        await ctx.send(f"OpusNotLoaded exception: \n`{e}`")



@bot.command()
async def 퇴근(ctx):
    try:
        await vc.disconnect()
        await ctx.send('퇴근한다곰')
    except:
        await ctx.send('이미 퇴근했다곰')



@bot.command()
async def 배워(ctx, text1=None, *,text2=None):
    gomfile=open('d:\\파이썬 실전\\gomgom.p','rb')
    gomdic=pickle.load(gomfile)
    gomdic[text1]=text2
    gomfile.close()
    gomfile=open('d:\\파이썬 실전\\gomgom.p','wb')
    pickle.dump(gomdic,gomfile)
    gomfile.close()
    await ctx.send(text1+'..'+" "+text2+'..??')



@bot.command()
async def 곰탕아(ctx, *, text=None):
    gomfile=open('d:\\파이썬 실전\\gomgom.p','rb')
    gomdic=pickle.load(gomfile)
    respond=gomdic[text]
    await ctx.send(respond)



bot.run('OTIxNjg4ODY4MDI4Mjg0OTI4.Yb2jpg.9A29DuN3E2pI7DEdbFjmAzmXfEo')