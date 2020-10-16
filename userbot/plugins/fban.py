# MIDHUN K M
# (C) BY MIDHUN
# FOR FRIDAY
import asyncio
from userbot.plugins.sql_helper.fban_sql import add_fed_in_db
from userbot.plugins.sql_helper.fban_sql import already_added_fed
from userbot.plugins.sql_helper.fban_sql import get_all_fed
from userbot.plugins.sql_helper.fban_sql import remove_fed
from userbot.utils import admin_cmd
from uniborgConfig import Config

log_fban = Config.PRIVATE_GROUP_ID

@borg.on(admin_cmd("fadd ?(.*)"))
async def addfed(event):
    if event.fwd_from:
        return
    sedlyf = event.pattern_match.group(1)
    if not already_added_fed(sedlyf):
        add_fed_in_db(sedlyf)
        await event.edit("`Fed Added`")
        await asyncio.sleep(3)
        await event.delete()

@borg.on(admin_cmd("frm ?(.*)"))
async def addfed(event):
    if event.fwd_from:
        return
    goodlyf = event.pattern_match.group(1)
    if not already_added_fed(goodlyf):
        await event.edit("`Fed Not In DB`")
        await asyncio.sleep(3)
        await event.delete()
    if already_added_fed(goodlyf):
        remove_fed(goodlyf)
        await event.edit("`Fed Removed From DB`")
        await asyncio.sleep(3)
        await event.delete()

@borg.on(admin_cmd("fban ?(.*)"))
async def addfed(event):
    if event.fwd_from:
        return
    starklyf = event.pattern_match.group(1)
    getmeallfed = get_all_fed()
    fban_count = 0
    kekbro = await event.edit("Starting Fban")
    sedbro = await kekbro.edit(f"Fbaning in Saved Feds. Total : {len(getmeallfed)} feds")
    for starkcast in getmeallfed:
        try:
            fban_count += 1
            await borg.send_message(log_fban, f"/joinfed {starkcast}")
            await borg.send_message(log_fban, f"/fban {starklyf}")
            await asyncio.sleep(0.2)
            await sedbro.edit(f"Completed fban in {fban_count}")
        except Exception as e:
            try:
                 await event.edit("Something went wrong \n{e}")
            except:
                 pass
    await sedbro.edit(f"Fban Completed Sucessfully in {fban_count} feds")

