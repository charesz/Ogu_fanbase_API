from .database import SessionLocal
from . import models


def seed_data():
    db = SessionLocal()

    # prevent reseeding
    if db.query(models.Character).first():
        db.close()
        return

    # =====================================================
    # CHARACTERS (Story Entities)
    # =====================================================
    characters = [
        {
            "name": "Baby Ogu",
            "role": "main_character",
            "description": "A pure and adventurous baby platypus. Baby Ogu embarks on the journey equipped with a hat and a butterfly net. Known as the \"White Warrior,\" he travels through different worlds, making many friends along the way. If left idle for a while, Baby Ogu sways side to side. ",
            "is_playable": True
        },
        {
            "name": "Ogu",
            "role": "support_character",
            "description": "The adoptive parent of Baby Ogu. Before Baby Ogu sets off on his adventure, Ogu gives Baby Ogu advice and hugs him before he leaves.",
            "is_playable": False
        },
        {
            "name": "The Great One",
            "role": "deity",
            "description": "The Great One is the supreme deity of the Secret Forest whose power maintains the balance of the world. Before the events of the game, the Great One's power was shattered into six magical stones known as Sigils .Because this power was lost, the world began to fall into corruption and decay. Baby Ogu's main quest is to recover these six pieces (Sigil of the Sun, Moon, Earth, etc.) and return them to the Heart of the World to restore the Great One’s full strength.",
            "is_playable": False
        },
        {
            "name": "Black Bird",
            "role": "support_character",
            "description": "A mysterious, 'weird-looking' guide you meet in your hometown . It tricks or leads Baby Ogu into the portal to the Secret Forest and continues to appear throughout the game to give hints and direction.",
            "is_playable": False
        },
        {
            "name": "White Bird",
            "role": "support_character",
            "description": "Recurring character often found in the Ocean Region or Central Forest areas.",
            "is_playable": False
        }
    ]

    db.add_all([models.Character(**c) for c in characters])

    # =====================================================
    # DIVINE BEASTS (CORE GAME SYSTEM ENTITIES)
    # =====================================================
    divine_beasts = [
        {
            "name": "Batt",
            "title": "Divine Beast of Earth",
            "domain": "Central Forest",
            "element": "Earth",
            "description": "In-game, Batt is often the last of the beasts to be rescued. He is a significant, mystical creature encountered within the game's lore and story, specifically in the western part of the central forest area.",
            "legacy": "Batt's Hat.The hat is essential for progressing through certain hidden story. Players can also offer any Earth element item to enter Batt’s divine beast room where the player can obtain any gemstones for collectibles or equipment enhancements.",
            "attribute": "Strength & Stability"
        },
        {
            "name": "Enki",
            "title": "Divine Beast of the Sea",
            "domain": "Ocean Region / Snowfield",
            "element": "Water",
            "description": "Enki is worshipped as the divine beast of the sea and is closely associated with the Ocean region and the Legendary Fisherman.",
            "legacy": "Enki Hat grants Evil God resistance. Players can access Enki’s divine beast room by offering any fish item on a pedestal. Entering this room provides access to a large amount of Grade 1 fish that jump out of the water.",
            "attribute": "Protection & Tides "
        },
        {
            "name": "Rahno",
            "title": "Divine Beast of the Sky",
            "domain": "Sky Island / Desert Region",
            "element": "Air",
            "description": "A majestic creature associated with the heavens and the winds. Rahnno oversees the highest points of the map and the creatures that inhabit the clouds. ",
            "legacy": ". Rahno is associated with powerful telekinetic abilities, allowing Baby Ogu to teleport between special slates while wearing Rahno's Hat. Rahno is the Divine Beast of the Sky, and meeting it allows interaction with these insect-focused divine beast rooms to collect regional bugs.",
            "attribute": "Teleportation"
        },
        {
            "name": "Tau",
            "title": "Divine Beast of Wisdom",
            "domain": "Jungle Region/ Moon Forest",
            "element": "Wisdom",
            "description": "A divine beast that has been corrupted and become a a monstrous enemy located in the Central Forest, corrupted by the power of an Evil God after polluting the Sigil of the Tree",
            "legacy": "The Tau Hat is tied to the Museum questline. ",
            "attribute": "Lore boss / Intellect & History"
        }
    ]

    db.add_all([models.DivineBeast(**b) for b in divine_beasts])

    # =====================================================
    # COMPANIONS (GAMEPLAY HELPERS)
    # =====================================================
    companions = [
        {
            "name": "Doogee",
            "region": "Baby Ogu's Hometown",
            "ability": "Digs dirt",
            "type": "Helper",
            "description": "A kind mole in our neighborhood. He's the first friend that the player can acquire, but he exists solely for the tutorial, so the player cannot interact with him during actual gameplay."
        },
        {
            "name": "Arthur Jr.",
            "region": "Ocean -  Hermit Crab Village ",
            "ability": "Break hard corals",
            "type": "Helper",
            "description": "Arthur's son, who's helping the shipwrecked sailors of Hermit Crab Village."
        },
        {
            "name": "Commander Poco",
            "region": "Jungle - Village of the Sun",
            "ability": "Break rocks",
            "type": "Helper",
            "description": "The commander monkey of the Village of the Sun. Handles explosive fruits masterfully and can easily crush huge rocks."
        },
        {
            "name": "Cricke",
            "region": "Moon Forest - Light laboratory ",
            "ability": "Dig dirt",
            "type": "Helper",
            "description": "A mole cricket who used to work at the mines of Moonlight Village."
        },
        {
            "name": "Pango",
            "region": "Desert Region - Shrew Village",
            "ability": "Breaks cacti",
            "type": "Helper",
            "description": "An armadillo that came to Shrew Village from Flame Village."
        },
        {
            "name": "Kary",
            "region": "Snowfield Region - Crystal Mines Entrance",
            "ability": "Break ice",
            "type": "Helper",
            "description": "A reindeer who likes to crush ice."
        }
    ]

    db.add_all([models.Companion(**c) for c in companions])

    # =====================================================
    # NPCs (LORE + CHAT SYSTEM)
    # =====================================================
    npcs = [
        #JUNGLE NPCs
        {
            "name": "Bosong",
            "region": "Jungle Region - Eastern Canyon",
            "description": "A monkey who's enthusiastic about hot springs. Wants to visit all the hot springs in the world, but currently has no intention to walk out of the Monkey Warehouse hot spring.",
            "chat": "I heard, in the Remains of Memory, there are only rare jungle fishes, such as Short Marlin, Leaf Fish, and Solar Fish."
        },
        {
            "name": "Leo",
            "region": "Jungle Region - Village of the Sun",
            "description": "A tourist lizard in Village of the Sun. He's traveling around with his brother, Pard.",
            "chat": "If you wander around the central forest, you can see various peddlers.There are also people selling rare items, so be sure to check them out when you're in Central Forest!"
        },
        {
            "name": "Orang",
            "region": "Jungle Region - Village of the Sun",
            "description": "A very proud mask craftsman of Village of the Sun. Player can complete hidden quest if player buys all Orang’s masks",
            "chat": "TOh hey, Did you know? There is a space behind the Waterfall of Meditation"
        },
        {
            "name": "Taril",
            "region": "Jungle Region - Village of the Sun",
            "description": "A warrior who protects the northern gate of the Village of the Sun. Very strong and swole. ",
            "chat": " Last time, I encountered a monster that self-destructs and deals poison damage. Apparently when it explodes, it hits other monsters too. When you come across one, make good use of it."
        },
        {
            "name": "Layla",
            "region": "Jungle Region - Village of the Sun",
            "description": "A rich koala in the Village of the Sun. Doesn't want to work or do any activities due to her laziness",
            "chat": "I heard that there is a great sword master in the north of Western Forest. I might cut the grass better once I learned that swordcraft. But never mind, I’m still too lazy to do that."
        },

        #MOON FOREST NPCs
        {
            "name": "Laddie ",
            "region": "Moon Forest - Moonlight Village Entrance ",
            "description": "A yellow ladybug that is enthusiastic about history.",
            "chat": "I once accidentally went to Dusk Forest when I got lost at the Moon Forest Entrance.I heard that a very rare fish called “ Moonlight Fish” lives in a pond there."
        },
        {
            "name": "Leddie",
            "region": "Moon Forest - Moonlight Village Entrance ",
            "description": "A red ladybug that is enthusiastic about gastronomy.",
            "chat": "Did you know? Brocade carps shine brighter if you cook them with Glowing reed leaves."
        },
        {
            "name": "Silk Moth Hero",
            "region": "Moon Forest - Temple of the Moon Crossroad",
            "description": "The Silk Moth Hero of Moonlight Village. Became smaller after being purified.",
            "chat": " I hope to repay my debt to you someday."
        },
        #DESERT REGION NPCs
        {
            "name": "Hochie",
            "region": "Desert Region - Flame Village",
            "description": "A racer of Flame Village. Must be careful of his spiky thorns.",
            "chat": "Did you know rolling could save your life? It's an essential skill, especially in the desert where many threatening monsters inhabit."
        },
        {
            "name": "Dochie",
            "region": "Desert Region - Flame Village",
            "description": "A small but very fast racer. Even left his family for the race.",
            "chat": "As you know, you can't eat the same dish one after another. So, prepare many different dishes just in case! *spits* "
        },
        {
            "name": "Alma",
            "region": "Desert Region - Flame Village",
            "description": "A racer of Flame Village a.k.a the Invincible Unstoppable Tank. Taught Baby Ogu how to race.",
            "chat": "Somewhere in the Shrew's Cave, there should be a relic called the Volcano Hat. With that hat, you can summon a volcano that explodes upon contact with enemies. "
        },
        {
            "name": "Shrew Leader",
            "region": "Desert Region - Shrew Village",
            "description": "The leader of Shrew Village. Has a small body, but a strong mind.",
            "chat": "Have you heard of a hidden relic called the Thorn Hat? If you wear it, you can roll and attack your enemies. If you find all five ancient shrew relics of the desert, you can enter the temple where a secret relic is hidden."
        },
         {
            "name": "Chief Priest of the Desert ",
            "region": "Desert Region - Silent Desert",
            "description": "The chief priest who watches over the Sky Crocodile's Temple (Rahno). Was caught in a sandstorm and buried beneath the desert sands.",
            "chat": "If you are looking for another chief priest, go to the places where it snows heavily and where there is a lot of water! "
         },
         {
            "name": "Shrew Archeologist",
            "region": "Desert Region - Temple of Fire Entry",
            "description": "A small shrew archaeologist who has been searching for traces of ancient shrews for many years. May be small but has a big dream.",
            "chat": "Apparently, you can catch a pretty rare bug called the Fire Chafer beyond the Burning Desert."
         },
         #OCEAN REGION NPCs
          {
            "name": "Arthur ",
            "region": "Ocean Region - Fierce Sea",
            "description": "Arthur Jr.'s Dad. Helps the stranded villagers at the sea.",
            "chat": " I heard there is a hat which creates a bubble shields in a wreck somewhere in Vast Sea. It must be very useful."
         },
         {
            "name": "Toby",
            "region": "Ocean Region - Fierce Sea",
            "description": "A brave sea otter. Lost one arm in a battle against the giant barnacle.",
            "chat": " A fish called Coral Pufferfish lives in the Silent Sea. It’s easy to catch since it just floats on the sea surface, but you must be careful of its poison!"
         },
         {
            "name": "Chief Priest of Water",
            "region": "Ocean Region - Lonely Sea ",
            "description": "The chief priest who worships Enki, the divine beast of the sea. Seems somewhat relaxed ",
            "chat": "If you have a chance, try cooking a Conch with Grade 1 Fish. The soup will detox your body completely!"
         },
         #SNOWFIELD REGION NPCs
         {
            "name": "Dolf",
            "region": "Snowfield - Snowflake Village ",
            "description": "A reindeer with impressively large antlers that enjoys riding mine carts.",
            "chat": " While exploring Crystal MInes, I stumbled upon a really dark spot. I think I spotted what looked like a hat made of ice! If only my nose shined, I would have checked it myself."
         },
         {
            "name": "Paul",
            "region": "Snowfield - Snowflake Village ",
            "description": "A detective in Snowflake Village with a small body but great observing and reasoning skills.",
            "chat": "Somewhere in the mountains of the Fierce Snow Field, there’s a pond where you can catch a Snow Carp."
         },
          {
            "name": "Chief Priest of Snow",
            "region": "Snowfield - Fierce Snow Field",
            "description": "The chief priest who worships Rahno, the divine beast of the sky. Dances very well.",
            "chat": " Yellowfin tuna only lives in Snow Field! It pairs perfectly with Grade 1 Fruits"
         },
         #CENTRAL FOREST NPCs
         {
            "name": "Moltese",
            "region": "Central Forest - Northern Crossroad",
            "description": "A painter puppy that travels around the world and paints pictures. Very talented.",
            "chat": "Seeing all your work in the atelier makes me so proud! Im sure there are only a few people who love this world as much as you do."
         },
         #HARBOR TOWN NPCs
         {
            "name": "Kenin ",
            "region": "Harbor Town - Thunder Island",
            "description": "A small puppy who works at the dock of Harbor Town. Uncovered the secret of Thunder Island with Baby Ogu.",
            "chat": "I saw an Angler Fish for the first time when I went fishing in the Thunder Island, and I freaked out! It looked super scary! When  I was young, the other crew members used to mock me and call me an anglerfish. How mean of them…"
         },
         {
            "name": "Soongsoong No.31",
            "region": "Harbor Town - Soongsoong Express Headquarters",
            "description": "The 31st Soongsoong to join the company. Got rescued while being stranded on Thunder Island.",
            "chat": " When you catch Sunfish in Harbour Town, try cooking it with Grade 1 Root. That’s the recipe for Soongsoong delicacy!"
         } 
    ]

    db.add_all([models.NPC(**n) for n in npcs])

    # =====================================================
    # ITEMS (TOTEMS / EQUIPMENT)
    # =====================================================
    items = [
        {
            "name": "Totem of Abundance", 
            "effect": " Every time you eat fruit, your attack power increases according to the fruit's grade. (Grade 3: 5 sec, Grade 2: 10 sec, Grade 1: 15 sec) ", 
            "region": "Central Forest"
         },
        {
            "name": "Totem of Happiness", 
            "effect": "When you dance, your HP replenishes by 2.", 
            "region": "Ocean"
         },
        {
            "name": "Totem of Gluttony", 
            "effect": "When you eat a cooked meal, all effects of the meal increase by 10%.", 
            "region": "Ocean"
        },

        {
            "name": "Totem of Sacrifice", 
            "effect": "When you take damage, you lose a Grade 3 fish by 25% chance and replenish your HP by the amount of damage taken.", 
            "region": "Ocean"
        },
        {
            "name": "Totem of Wind", 
            "effect": "When you take damage, your speed increases for 5 seconds by 30% chance.", 
            "region": "Sky Island"
        },
        {
            "name": "Totem of Survival", 
            "effect": "Cooldown for rolling decreases by 20%.", 
            "region": "Desert"
        },
        {
            "name": "Totem of Tenacity", 
            "effect": "You strike critical hit every 8th swing for 100%.", 
            "region": "Jungle"
        },
        {
            "name": "Totem of Protection", 
            "effect": "When you wear a hat without any special ability, god mode after taking damage lasts longer. (Except special edition hats)", 
            "region": "Jungle"
        },
        {
            "name": "Totem of Vigor", 
            "effect": "When Baby Ogu strikes a critical hit, HP replenishes by 1.", 
            "region": "Central Forest"
        },
        {
            "name": "Totem of Vitality", 
            "effect": "Chances of landing a critical hit increases by 10% in Excited status.", 
            "region": "Ocean"
        },
        {
            "name": "Totem of Lunacy", 
            "effect": "The headbutt recharges quicker in Excited status, and you can charge it up to four times.", 
            "region": "Sky Island"
        },
        {
            "name": "Totem of Pleasure", 
            "effect": "When you dance, you will summon monkey souls that will distract enemies and projectiles.", 
            "region": "Jungle"
        },
    ]

    db.add_all([models.Item(**i) for i in items])

    # =====================================================
    # COLLECTIBLES (BUGS / WORLD ITEMS)
    # =====================================================
    collectibles = [
        #AIR BUGS
        {
            "name": "Cabbage Butterfly",
            "type": "air_bug",
            "region": "All",
            "location": "Various",
            "rarity": "common"
        },
        {
            "name": "Tiger Swallowtail",
            "type": "air_bug",
            "region": "All",
            "location": "Various",
            "rarity": "common"
        },
        {
            "name": "Aquamarine Butterfly",
            "type": "air_bug",
            "region": "Jungle Region",
            "location": "Remains of Memory; Remains of Memory Entrance",
            "rarity": "rare"
        },
        {
            "name": "Leaf Dragonfly",
            "type": "air_bug",
            "region": "Jungle Region",
            "location": "Temple of the Sun Entrance; Eastern Jungle; Eastern Canyon",
            "rarity": "rare"
        },
        {
            "name": "Bell Butterfly",
            "type": "air_bug",
            "region": "Moon Forest",
            "location": "Miner’s Hot Spring; The Ruins; Dusk Intersection; Mine Shortcut; Moonlight Village Entrance; Forest of Wonder; Silent Field of Reeds",
            "rarity": "rare"
        },
        {
            "name": "Jade Dragonfly",
            "type": "air_bug",
            "region": "Moon Forest",
            "location": "Miner’s Hot Spring; The Ruins; Mine Shortcut",
            "rarity": "rare"
        },
        {
            "name": "Snowflower Butterfly",
            "type": "air_bug",
            "region": "Snowfield",
            "location": "Cold Snow Field",
            "rarity": "rare"
        },
        {
            "name": "Aurora Butterfly",
            "type": "air_bug",
            "region": "Snowfield",
            "location": "Fierce Snow Field, West Sky Crocodile Temple",
            "rarity": "rare"
        },
        {
            "name": "Water Butterfly",
            "type": "air_bug",
            "region": "Harbor",
            "location": "Harbor Town; Thunder Island",
            "rarity": "rare"
        },
        {
            "name": "Red Dragonfly",
            "type": "air_bug",
            "region": "Harbor",
            "location": "Harbor Town; Thunder Island",
            "rarity": "rare"
        },
        {
            "name": "Sky Butterfly",
            "type": "air_bug",
            "region": "Sky Island",
            "location": "Sky Island North; Sky Island South",
            "rarity": "rare"
        },
        #TREE BUGS
        {
            "name": "Stag Beetle",
            "type": "tree_bug",
            "region": "All",
            "location": "Various",
            "rarity": "common"
        },
        {
            "name": "Rhino Beetle",
            "type": "tree_bug",
            "region": "All",
            "location": "Various",
            "rarity": "common"
        },
        {
            "name": "Sun Beetle",
            "type": "tree_bug",
            "region": "Jungle Region",
            "location": "Remains of Memory; Eastern Canyon",
            "rarity": "rare"
        },
        {
            "name": "Bombardier Beetle",
            "type": "tree_bug",
            "region": "Jungle Region",
            "location": "Remains of Memory; Eastern Jungle; Village of the Sun Entrance",
            "rarity": "rare"
        },
        {
            "name": "Red Longhorn Beetle",
            "type": "tree_bug",
            "region": "Moon Forest",
            "location": "The Ruins; Light Laboratory; Dusk Forest; Silent Field of Reeds",
            "rarity": "rare"
        },
        {
            "name": "Blue Longhorn Beetle",
            "type": "tree_bug",
            "region": "Moon Forest",
            "location": "Miner’s Hot Spring; The Ruins; Light Laboratory; ; Dusk Forest",
            "rarity": "rare"
        },
        {
            "name": "Green Longhorn Beetle",
            "type": "tree_bug",
            "region": "Moon Forest",
            "location": "Miner’s Hot Spring; The Ruins; Light Laboratory; Temple of the Moon Entrance; Dusk Forest",
            "rarity": "rare"
        },
        {
            "name": "Ancient Beetle",
            "type": "tree_bug",
            "region": "Desert Region",
            "location": "Wild Desert; Silent Desert; Temple of Fire entrance; Temple of Fire Entry; Burning Desert",
            "rarity": "rare"
        },
        {
            "name": "Snowman Beetle",
            "type": "tree_bug",
            "region": "Snowfield",
            "location": "Sky Road; Crystal Mines Entrance; Snow Field Crossroad; Fierce Snow Field",
            "rarity": "rare"
        },
        {
            "name": "Maple Beetle",
            "type": "tree_bug",
            "region": "Harbor",
            "location": "Harbor Town",
            "rarity": "rare"
        }
    ]

    db.add_all([models.Collectible(**c) for c in collectibles])

    # commit everything once
    db.commit()
    db.close()