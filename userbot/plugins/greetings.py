from .. import CMD_HELP
from ..utils import admin_cmd, edit_or_reply, sudo_cmd

R = (
    "██╗░░██╗██╗\n"
    "██║░░██║██║\n"
    "███████║██║\n"
    "██╔══██║██║\n"
    "██║░░██║██║\n"
    "╚═╝░░╚═╝╚═╝\n"
)

S = (
    "..... (¯`v´¯)♥️\n"
    ".......•.¸.•´\n"
    "....¸.•´  🅷🅸\n"
    "... (   BABYy\n"
    "☻/ \n"
    "/▌✿🌷✿\n"
    "/ \     \|/\n"
)


U = (
    "🌙.     *       ☄️      \n"
    "🌟   .  *       .         \n"
    "                       *   .      🛰     .        ✨      *\n"
    "  .     *   SLEEP WELL        🚀     \n"
    "      .              . . SWEET DREAMS 🌙\n"
    ". *       🌏 GOOD NIGHT         *\n"
    "                     🌙.     *       ☄️      \n"
    "🌟   .  *       .         \n"
    "                       *   .      🛰     .        ✨      *\n"
)

V = (
    "▃▃▃▃▃▃▃▃▃▃▃\n"
    "┊ ┊ ┊ ┊ ┊ ┊\n"
    "┊ ┊ ┊ ┊ ˚✩ ⋆｡˚ ✩\n"
    "┊ ┊ ┊ ✫\n"
    "┊ ┊ ✧🎂🍰🍫🍭\n"
    "┊ ┊ ✯\n"
    "┊ . ˚ ˚✩\n"
    "........♥️♥️..........♥️♥️_\n"
    ".....♥️........♥️..♥️........♥️_\n"
    "...♥️.............♥️............♥️\n"
    "......♥️.....Happy.......♥️__\n"
    "...........♥️..............♥️__\n"
    "................♥️.....♥️__\n"
    "......................♥️__\n"
    "...............♥️........♥️__\n"
    "..........♥️...............♥️__\n"
    ".......♥️..Birthday....♥️_\n"
    ".....♥️..........♥️...........♥️__\n"
    ".....♥️.......♥️_♥️.....♥️__\n"
    ".........♥️♥️........♥️♥️.....\n"
    ".............................................\n"
    "..... (¯`v´¯)♥️\n"
    ".......•.¸.•´STAY BLESSED\n"
    "....¸.•´      LOVE&FUN\n"
    "... (   YOU DESERVE\n"
    "☻/ THEM A LOT\n"
    "/▌✿🌷✿\n"
    r"/ \     \|/\n"
    "▃▃▃▃▃▃▃▃▃▃▃\n"
)

W = (
    "G🌷o🍃o🌷D\n"
    "M🍃o🌷r🍃N🌷i🍃N🌷g\n"
    "            \n"
    "No matter how good or \n"
    "bad your life is,\n"
    "wake up each morning\n"
    "and be thankful.\n"
    "You still have a new day.\n"
    "        \n"
    "🌞   \n"
    "         \n"
    "╱◥████◣\n"
    "│田│▓ ∩ │◥███◣\n"
    "╱◥◣ ◥████◣田∩田│\n"
    "│╱◥█◣║∩∩∩ 田∩田│\n"
    "║◥███◣∩田∩ 田∩田│\n"
    "│∩│ ▓ ║∩田│║▓田▓\n"
    "🌹🌷🌹🌷🌹🍃🌷🌹🌷🌹\n"
)

X = (
    ".......🦋🦋........🦋🦋\n"
    "...🦋.........🦋🦋.......🦋\n"
    "...🦋............💙..........🦋\n"
    ".....🦋🅣🅗🅐🅝🅚🅢 🦋\n"
    "....... 🦋.................🦋\n"
    "..............🦋......🦋\n"
    "...................💙\n"
)


@sparkzzz.on(admin_cmd(pattern=r"hy$"))
async def bluedevilhy(hy):
    await edit_or_reply(hy, R)


@sparkzzz.on(admin_cmd(pattern=r"baby$"))
async def bluedevilbaby(baby):
    await edit_or_reply(baby, S)


@sparkzzz.on(admin_cmd(pattern=r"hpbd$"))
async def bluedevilhbd(hpbd):
    await edit_or_reply(hpbd, V)


@sparkzzz.on(admin_cmd(pattern=r"thanks$"))
async def bluedeviltnk(tnk):
    await edit_or_reply(tnk, X)



@sparkzzz.on(admin_cmd(pattern="gmg2$"))
async def gm(event):
    await edit_or_reply(
        event,
        "♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n╔══╗────╔╗──────────╔╗\n║╔═╬═╦═╦╝║╔══╦═╦╦╦═╦╬╬═╦╦═╗\n║╚╗║╬║╬║╬║║║║║╬║╔╣║║║║║║║╬║\n╚══╩═╩═╩═╝╚╩╩╩═╩╝╚╩═╩╩╩═╬╗║\n────────────────────────╚═╝\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛･",
    )


@sparkzzz.on(admin_cmd(pattern="gnt2$"))
async def gn(event):
    await edit_or_reply(
        event,
        "♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n╔══╗────╔╗╔═╦╦╗─╔╗╔╗\n║╔═╬═╦═╦╝║║║║╠╬═╣╚╣╚╗\n║╚╗║╬║╬║╬║║║║║║╬║║║╔╣\n╚══╩═╩═╩═╝╚╩═╩╬╗╠╩╩═╝\n──────────────╚═╝\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛･",
    )


@sparkzzz.on(admin_cmd(pattern=r"gmg3$"))
async def bluedevilgoodm(goodm):
    await edit_or_reply(goodm, W)


@sparkzzz.on(admin_cmd(pattern=r"gnt3$"))
async def bluedevilgoodn(goodn):
    await edit_or_reply(goodn, U)




@sparkzzz.on(admin_cmd(pattern=r"cheer$"))
async def cheer(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event,
        "💐💐😉😊💐💐\n☕ Cheer Up  🍵\n🍂 ✨ )) ✨  🍂\n🍂┃ (( * ┣┓ 🍂\n🍂┃*💗 ┣┛ 🍂 \n🍂┗━━┛  🍂🎂 For YOU  🍰\n💐💐😌😚💐💐",
    )


@sparkzzz.on(admin_cmd(pattern=r"getwell$"))
async def getwell(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event, "🌹🌹🌹🌹🌹🌹🌹🌹 \n🌹😷😢😓😷😢💨🌹\n🌹💝💉🍵💊💐💝🌹\n🌹 GetBetter Soon! 🌹\n🌹🌹🌹🌹🌹🌹🌹🌹"
    )


@sparkzzz.on(admin_cmd(pattern=r"luck$"))
async def luck(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event, "💚~🍀🍀🍀🍀🍀\n🍀╔╗╔╗╔╗╦╗✨🍀\n🍀║╦║║║║║║👍🍀\n🍀╚╝╚╝╚╝╩╝。 🍀\n🍀・・ⓁⓊⒸⓀ🍀\n🍀🍀🍀 to you💚"
    )


@sparkzzz.on(admin_cmd(pattern=r"sprinkle$"))
async def sprinkle(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event,
        "✨.•*¨*.¸.•*¨*.¸¸.•*¨*• ƸӜƷ\n🌸🌺🌸🌺🌸🌺🌸🌺\n Sprinkled with love❤\n🌷🌻🌷🌻🌷🌻🌷🌻\n ¨*.¸.•*¨*. ¸.•*¨*.¸¸.•*¨`*•.✨\n🌹🍀🌹🍀🌹🍀🌹🍀",
    )


CMD_HELP.update(
    {
        "greetings": "__**PLUGIN NAME :** Greetings__\
    \n\n📌** CMD ➥** `.hy` | `.baby` | `.hpbd` | `.thanks` |`.gmg2` | `.gnt2` | `.gnt3` | `.cheer` | `.getwell` | `.luck` | `.sprinkle`\
    \n\n**USAGE   ➥  **These are art bruh..Try & check yourself\
     \n\n📌** CMD ➥** `.hi` or `hi <emoji>`\
    \n\n**USAGE   ➥  **Send a hi with your custom emoji."
    }
)
