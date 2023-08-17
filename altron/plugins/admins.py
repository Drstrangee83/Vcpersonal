from pyrogram import Client
from pyrogram.types import Message
from helpers.command import commandpro
from config import call_py
from helpers.decorators import errors, sudo_users_only
from helpers.handlers import skip_current_song, skip_item
from helpers.queues import QUEUE, clear_queue


@Client.on_message(commandpro(["!skip", ".skip", "/skip", "/s", "S", "Skip"]))
@errors
@sudo_users_only
async def skip(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("**CHUD GYA?**")
        elif op == 1:
            await m.reply("**DAFAN HO GYA GUYS**")
        else:
            await m.reply(
                f"**⏩ BAHINCHOD RANDI** \n**🎶 KALAPNA START** - [{op[0]}]({op[1]}) | `{op[2]}`",
                disable_web_page_preview=True,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "**🗑️ DAFAA HO JAAA BAHINCHOD: -**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#⃣{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(commandpro(["!end", ".end", "/end", "!stop", ".stop", "/stop", "E", "End", "/e", "Stop"]))
@errors
@sudo_users_only
async def stop(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("**DAFAN DONE**")
        except Exception as e:
            await m.reply(f"**KYAA HUA....** \n`{e}`")
    else:
        await m.reply("**UFFF BAACHE HAI**")


@Client.on_message(commandpro(["!pause", ".pause", "/pause", "pause"]))
@errors
@sudo_users_only
async def pause(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                f"**KALAP GYA NA??**\n\n𝑻𝒐 𝒓𝒆𝒔𝒖𝒎𝒆 𝒑𝒍𝒂𝒚𝒃𝒂𝒄𝒌, 𝒖𝒔𝒆 𝒕𝒉𝒆 𝒄𝒐𝒎𝒎𝒂𝒏𝒅 » `!resume`"
            )
        except Exception as e:
            await m.reply(f"**GAND DE DE GF KA.....** \n`{e}`")
    else:
        await m.reply("**❌ DAFAN**")


@Client.on_message(commandpro(["!resume", ".resume", "/resume", "resume"]))
@errors
@sudo_users_only
async def resume(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                f"**▶ EXCEPTION OP**\n\n𝑻𝒐 𝒑𝒂𝒖𝒔𝒆 𝒑𝒍𝒂𝒚𝒃𝒂𝒄𝒌, 𝒖𝒔𝒆 𝒕𝒉𝒆 𝒄𝒐𝒎𝒎𝒂𝒏𝒅 » `!pause`"
            )
        except Exception as e:
            await m.reply(f"**𝑬𝒓𝒓𝒐𝒓....** \n`{e}`")
    else:
        await m.reply("**WAHI HU VAI**")
