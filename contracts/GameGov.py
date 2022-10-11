import smartpy as sp

NFTandVault = sp.io.import_script_from_url(
    "https://raw.githubusercontent.com/toptal126/CoC-tezos-p2e-game/e459673b8f9a5a83ba1bd4c2fadd9b99a09b1d87/contracts/NFTandVault.py")


FA2 = sp.io.import_script_from_url("https://smartpy.io/templates/fa2_lib.py")
Utils = sp.io.import_script_from_url(
    "https://raw.githubusercontent.com/RomarQ/tezos-sc-utils/main/smartpy/utils.py")


T_BALANCE_OF_REQUEST = sp.TRecord(owner=sp.TAddress, token_id=sp.TNat).layout(
    ("owner", "token_id")
)

SECONDS_PER_DAY = 60
# SECONDS_PER_DAY = 86400

T_CITY_RESOURCE = sp.TRecord(
    city_level=sp.TNat,
    population_limit=sp.TNat,
    faith=sp.TNat,
    beauty=sp.TNat,
    food=sp.TNat,
    wood=sp.TNat,
    stone=sp.TNat,
    iron=sp.TNat,
    aurum=sp.TNat,

    last_claim_time=sp.TTimestamp,

    food_per_epoch=sp.TNat,
    wood_per_epoch=sp.TNat,
    stone_per_epoch=sp.TNat,
    iron_per_epoch=sp.TNat,
    building_list=sp.TList(sp.TNat)
)
# .layout('city_level', 'faith', 'beauty',
#          'food', 'wood', 'stone', 'iron', 'aurum',
#          'last_claim_time',
#          'food_per_epoch', 'wood_per_epoch', 'stone_per_epoch', 'iron_per_epoch')


T_BUILDING_CATEGORY = sp.TRecord(
    # Upgrading buildings
    # Resource producing buildings
    # Unit producing buildings
    # Other Buildings

    building_kind=sp.TNat,
    # Unique if for each building type
    # building_kind=sp.TNat,
    # Costs per level
    resource_updates=sp.TMap(sp.TNat, sp.TRecord(

        food_cost=sp.TNat,
        wood_cost=sp.TNat,
        stone_cost=sp.TNat,
        iron_cost=sp.TNat,
        aurum_cost=sp.TNat,

        food_per_epoch=sp.TNat,
        wood_per_epoch=sp.TNat,
        stone_per_epoch=sp.TNat,
        iron_per_epoch=sp.TNat,

        population_plus=sp.TNat,
        population_minus=sp.TNat,
        faith_plus=sp.TNat,
        beauty_plus=sp.TNat,
    ))
)

DATA_BUILDINGS = sp.big_map(
    {
        0: sp.record(
            building_kind=sp.nat(0),  # Farm
            # Unique if for each building type
            # Costs per level
            resource_updates=sp.map(
                {
                    0: sp.record(
                        food_cost=sp.nat(15),
                        wood_cost=sp.nat(30),
                        stone_cost=sp.nat(0),
                        iron_cost=sp.nat(5),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(15),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(10),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                    1: sp.record(
                        food_cost=sp.nat(15),
                        wood_cost=sp.nat(100),
                        stone_cost=sp.nat(10),
                        iron_cost=sp.nat(5),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(17),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                    2: sp.record(
                        food_cost=sp.nat(15),
                        wood_cost=sp.nat(300),
                        stone_cost=sp.nat(0),
                        iron_cost=sp.nat(30),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(20),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(2),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    )
                })
        ),
        1: sp.record(
            building_kind=sp.nat(1),  # Lumber Mill
            # Unique if for each building type
            # Costs per level
            resource_updates=sp.map(
                {
                    0: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(30),
                        stone_cost=sp.nat(15),
                        iron_cost=sp.nat(15),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(10),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(7),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                    1: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(55),
                        stone_cost=sp.nat(105),
                        iron_cost=sp.nat(15),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(12),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                    2: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(100),
                        stone_cost=sp.nat(250),
                        iron_cost=sp.nat(45),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(15),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(1),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    )
                })
        ),
        2: sp.record(
            building_kind=sp.nat(2),  # Stonecutter
            # Unique if for each building type
            # Costs per level
            resource_updates=sp.map(
                {
                    0: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(30),
                        stone_cost=sp.nat(5),
                        iron_cost=sp.nat(15),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(10),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(5),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                    1: sp.record(

                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(30),
                        stone_cost=sp.nat(10),
                        iron_cost=sp.nat(45),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(12),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                    2: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(100),
                        stone_cost=sp.nat(150),
                        iron_cost=sp.nat(35),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(15),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(1),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    )
                })
        ),
        3: sp.record(
            building_kind=sp.nat(3),  # Forge
            # Unique if for each building type
            # Costs per level
            resource_updates=sp.map(
                {
                    0: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(30),
                        stone_cost=sp.nat(15),
                        iron_cost=sp.nat(5),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(10),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(5),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                    1: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(75),
                        stone_cost=sp.nat(15),
                        iron_cost=sp.nat(30),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(12),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                    2: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(150),
                        stone_cost=sp.nat(15),
                        iron_cost=sp.nat(5),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(15),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(1),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    )
                })
        ),
        4: sp.record(
            building_kind=sp.nat(4),  # House
            # Unique if for each building type
            # Costs per level
            resource_updates=sp.map(
                {
                    0: sp.record(
                        food_cost=sp.nat(15),
                        wood_cost=sp.nat(25),
                        stone_cost=sp.nat(15),
                        iron_cost=sp.nat(5),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(10),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                    1: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(50),
                        stone_cost=sp.nat(20),
                        iron_cost=sp.nat(5),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(2),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                    2: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(100),
                        stone_cost=sp.nat(45),
                        iron_cost=sp.nat(10),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(3),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    )
                })
        ),
        5: sp.record(
            building_kind=sp.nat(5),  # Marketplace
            # Unique if for each building type
            # Costs per level
            resource_updates=sp.map(
                {
                    0: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(45),
                        stone_cost=sp.nat(25),
                        iron_cost=sp.nat(0),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                    1: sp.record(
                        food_cost=sp.nat(200),
                        wood_cost=sp.nat(75),
                        stone_cost=sp.nat(50),
                        iron_cost=sp.nat(0),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                    2: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(300),
                        stone_cost=sp.nat(80),
                        iron_cost=sp.nat(0),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    )
                })
        ),
        6: sp.record(
            building_kind=sp.nat(6),  # Traning Center
            # Unique if for each building type
            # Costs per level
            resource_updates=sp.map(
                {
                    0: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(100),
                        stone_cost=sp.nat(50),
                        iron_cost=sp.nat(0),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                })
        ),
        7: sp.record(
            building_kind=sp.nat(7),  # Trees
            # Unique if for each building type
            # Costs per level
            resource_updates=sp.map(
                {
                    0: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(25),
                        stone_cost=sp.nat(0),
                        iron_cost=sp.nat(0),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(5),
                    ),
                })
        ),
        8: sp.record(
            building_kind=sp.nat(8),  # Chapel
            # Unique if for each building type
            # Costs per level
            resource_updates=sp.map(
                {
                    0: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(50),
                        stone_cost=sp.nat(150),
                        iron_cost=sp.nat(0),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(25),
                        beauty_plus=sp.nat(0),
                    ),
                })
        ),
        9: sp.record(
            building_kind=sp.nat(9),  # Keep
            # Unique if for each building type
            # Costs per level
            resource_updates=sp.map(
                {
                    0: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(0),
                        stone_cost=sp.nat(0),
                        iron_cost=sp.nat(0),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                })
        ),
        10: sp.record(
            building_kind=sp.nat(10),  # Archery center
            # Unique if for each building type
            # Costs per level
            resource_updates=sp.map(
                {
                    0: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(100),
                        stone_cost=sp.nat(100),
                        iron_cost=sp.nat(25),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                })
        ),
        11: sp.record(
            building_kind=sp.nat(11),  # Barracks
            # Unique if for each building type
            # Costs per level
            resource_updates=sp.map(
                {
                    0: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(50),
                        stone_cost=sp.nat(200),
                        iron_cost=sp.nat(45),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                })
        ),
        12: sp.record(
            building_kind=sp.nat(12),  # Church
            # Unique if for each building type
            # Costs per level
            resource_updates=sp.map(
                {
                    0: sp.record(
                        food_cost=sp.nat(100),
                        wood_cost=sp.nat(100),
                        stone_cost=sp.nat(500),
                        iron_cost=sp.nat(100),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(100),
                        beauty_plus=sp.nat(0),
                    ),
                })
        ),
        13: sp.record(
            building_kind=sp.nat(13),  # Statue
            # Unique if for each building type
            # Costs per level
            resource_updates=sp.map(
                {
                    0: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(0),
                        stone_cost=sp.nat(80),
                        iron_cost=sp.nat(10),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(50),
                    ),
                })
        ),
        14: sp.record(
            building_kind=sp.nat(14),  # Stables
            # Unique if for each building type
            # Costs per level
            resource_updates=sp.map(
                {
                    0: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(125),
                        stone_cost=sp.nat(50),
                        iron_cost=sp.nat(25),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                })
        ),
        15: sp.record(
            building_kind=sp.nat(15),  # Blacksmith
            # Unique if for each building type
            # Costs per level
            resource_updates=sp.map(
                {
                    0: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(25),
                        stone_cost=sp.nat(100),
                        iron_cost=sp.nat(125),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                })
        ),
        16: sp.record(
            building_kind=sp.nat(16),  # Fletcher
            # Unique if for each building type
            # Costs per level
            resource_updates=sp.map(
                {
                    0: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(25),
                        stone_cost=sp.nat(100),
                        iron_cost=sp.nat(125),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                })
        ),
        17: sp.record(
            building_kind=sp.nat(17),  # Siege Workshop
            # Unique if for each building type
            # Costs per level
            resource_updates=sp.map(
                {
                    0: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(400),
                        stone_cost=sp.nat(25),
                        iron_cost=sp.nat(100),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                })
        ),
        18: sp.record(
            building_kind=sp.nat(18),  # Rune Carver
            # Unique if for each building type
            # Costs per level
            resource_updates=sp.map(
                {
                    0: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(50),
                        stone_cost=sp.nat(300),
                        iron_cost=sp.nat(100),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                })
        ),
        19: sp.record(
            building_kind=sp.nat(19),  # Guild Barracks
            # Unique if for each building type
            # Costs per level
            resource_updates=sp.map(
                {
                    0: sp.record(
                        food_cost=sp.nat(0),
                        wood_cost=sp.nat(250),
                        stone_cost=sp.nat(180),
                        iron_cost=sp.nat(50),
                        aurum_cost=sp.nat(0),

                        food_per_epoch=sp.nat(0),
                        wood_per_epoch=sp.nat(0),
                        stone_per_epoch=sp.nat(0),
                        iron_per_epoch=sp.nat(0),

                        population_plus=sp.nat(0),
                        population_minus=sp.nat(0),
                        faith_plus=sp.nat(0),
                        beauty_plus=sp.nat(0),
                    ),
                })
        )
    })


class NftOwnerCheck:
    def __init__(self, nft_contract):
        self.update_initial_storage(
            nft_contract=nft_contract,
            temp_balances=sp.list(l=[],
                                  t=sp.TRecord(
                request=T_BALANCE_OF_REQUEST,
                balance=sp.TNat,
            ))
        )

    @sp.entry_point
    def set_balance_callback(self, balances):
        sp.verify(sp.sender == self.data.nft_contract, "Not authorised")
        with sp.for_("temp_balance", balances) as temp_balance:
            sp.verify(temp_balance.balance > 0, "Invalid Owner")

    def is_valid_owner(self, owner, token_id):
        contract = sp.contract(
            sp.TRecord(
                requests=sp.TList(
                    sp.TRecord(
                        owner=sp.TAddress,
                        token_id=sp.TNat
                    ).layout(("owner", "token_id"))
                ),
                callback=sp.TContract(
                    sp.TList(
                        sp.TRecord(
                            request=sp.TRecord(
                                owner=sp.TAddress,
                                token_id=sp.TNat
                            ).layout(("owner", "token_id")),
                            balance=sp.TNat
                        ).layout(("request", "balance"))
                    )
                )
            ).layout(("requests", "callback")),
            self.data.nft_contract,
            entry_point="balance_of").open_some()
        requests = sp.list([sp.record(owner=owner, token_id=token_id)])
        params = sp.record(callback=sp.self_entry_point(
            entry_point="set_balance_callback"), requests=requests)
        sp.transfer(params, sp.mutez(0), contract)


class BuildingCategories(sp.Contract):
    def __init__(self, building_categories):
        self.update_initial_storage(
            building_categories=building_categories
        )


class ResourceStorage(sp.Contract):
    def __init__(self):
        self.update_initial_storage(
            resource_map=sp.big_map(
                {}, tkey=sp.TNat, tvalue=T_CITY_RESOURCE),
            temp1=0,
            temp2=0,
            temp3=sp.timestamp(0),
            temp4=0
        )

    def is_active_city(self, token_id):
        sp.verify(self.data.resource_map.contains(token_id),
                  "No city information for provided token_id")

    def initialize_city(self, token_id):
        self.data.resource_map[token_id] = sp.record(
            city_level=0,
            population_limit=50,
            faith=0,
            beauty=0,
            food=0,
            wood=0,
            stone=0,
            iron=0,
            aurum=0,

            last_claim_time=sp.now,

            food_per_epoch=45,
            wood_per_epoch=30,
            stone_per_epoch=30,
            iron_per_epoch=30,

            building_list=[]
        )

    def upgrade_building(self, token_id, building_kind, to_level):
        building_cost = sp.local(
            'building_cost', self.data.building_categories[building_kind].resource_updates[to_level])
        self.is_resource_enough_for_building(
            building_cost,  token_id, building_kind, to_level)

        self.data.resource_map[token_id].food = sp.as_nat(self.data.resource_map[token_id].food -
                                                          building_cost.value.food_cost)
        self.data.resource_map[token_id].wood = sp.as_nat(self.data.resource_map[token_id].wood -
                                                          building_cost.value.wood_cost)
        self.data.resource_map[token_id].stone = sp.as_nat(self.data.resource_map[token_id].stone -
                                                           building_cost.value.stone_cost)
        self.data.resource_map[token_id].iron = sp.as_nat(self.data.resource_map[token_id].iron -
                                                          building_cost.value.iron_cost)
        self.data.resource_map[token_id].aurum = sp.as_nat(self.data.resource_map[token_id].aurum -
                                                           building_cost.value.aurum_cost)

        self.data.resource_map[token_id].food_per_epoch += building_cost.value.food_per_epoch
        self.data.resource_map[token_id].wood_per_epoch += building_cost.value.wood_per_epoch
        self.data.resource_map[token_id].stone_per_epoch += building_cost.value.stone_per_epoch
        self.data.resource_map[token_id].iron_per_epoch += building_cost.value.iron_per_epoch
        self.data.resource_map[token_id].faith += building_cost.value.faith_plus
        self.data.resource_map[token_id].beauty += building_cost.value.beauty_plus

        self.data.resource_map[token_id].population_limit += building_cost.value.population_plus
        self.data.resource_map[token_id].population_limit = sp.as_nat(
            self.data.resource_map[token_id].population_limit - building_cost.value.population_minus)

    def update_resource(self, token_id):
        self.is_active_city(token_id)
        duration_sec = sp.local('duration_sec', sp.now -
                                self.data.resource_map[token_id].last_claim_time)
        duration_day = sp.local('duration_day', sp.as_nat(
            duration_sec.value) // SECONDS_PER_DAY)

        self.data.resource_map[token_id].last_claim_time.add_seconds(
            duration_day.value * SECONDS_PER_DAY)
        self.data.resource_map[token_id].food += self.data.resource_map[token_id].food_per_epoch * duration_day.value
        self.data.resource_map[token_id].wood += self.data.resource_map[token_id].wood_per_epoch * duration_day.value
        self.data.resource_map[token_id].stone += self.data.resource_map[token_id].stone_per_epoch * duration_day.value
        self.data.resource_map[token_id].iron += self.data.resource_map[token_id].iron_per_epoch * duration_day.value

        self.data.temp1 = duration_sec.value
        self.data.temp2 = duration_day.value
        self.data.temp3 = self.data.resource_map[token_id].last_claim_time

    def is_resource_enough_for_building(self, building_cost,  token_id, building_kind, to_level):

        sp.verify(self.data.resource_map[token_id].food >=
                  building_cost.value.food_cost, "ResourceStorage: Not enough food")
        sp.verify(self.data.resource_map[token_id].wood >=
                  building_cost.value.wood_cost, "ResourceStorage: Not enough wood")
        sp.verify(self.data.resource_map[token_id].stone >=
                  building_cost.value.stone_cost, "ResourceStorage: Not enough stone")
        sp.verify(self.data.resource_map[token_id].iron >=
                  building_cost.value.iron_cost, "ResourceStorage: Not enough iron")
        sp.verify(
            self.data.resource_map[token_id].population_limit >= building_cost.value.population_minus, "ResourceStorage: Popluation is limited")

    # def harvest_resource(self, token_id):


class GameGov(FA2.Admin, FA2.WithdrawMutez, NftOwnerCheck, ResourceStorage, BuildingCategories):
    def __init__(self, admin, nft_contract, building_categories, **kwargs):
        FA2.Admin.__init__(self, admin)
        ResourceStorage.__init__(self)
        NftOwnerCheck.__init__(self, nft_contract)
        BuildingCategories.__init__(self, building_categories)

    @sp.entry_point
    def start_game(self, token_id):
        self.is_valid_owner(sp.sender, token_id)
        sp.set_type(token_id, sp.TNat)
        self.initialize_city(token_id)
        sp.trace(self.data.resource_map)

    @sp.entry_point
    def harvest_resource(self, token_id):
        self.is_valid_owner(sp.sender, token_id)
        self.is_active_city(token_id)

        self.update_resource(token_id)

    @sp.entry_point
    def setup_building(self, token_id, building_kind):
        self.is_valid_owner(sp.sender, token_id)
        self.is_active_city(token_id)
        self.update_resource(token_id)
        self.upgrade_building(token_id, building_kind, 0)
        pass


@ sp.add_test(name="Game Gov with Resource manager")
def test():
    sc = sp.test_scenario()
    nft_contract = NFTandVault.NftWithAdmin(
        admin=sp.address("tz1i66XefcqsNVSGa2iFsWb8qxokm3neVpFR"),
        metadata=sp.utils.metadata_of_url(
            "ipfs://bafkreigb6nsuvwc7vzx6oqzoaeaxno6liyr5rigbheg2ol7ndac75kawoe"
        ),
        token_metadata=[],
    )

    sc += nft_contract

    nft_contract.mint(
        [sp.record(to_=sp.address("tz1i66XefcqsNVSGa2iFsWb8qxokm3neVpFR"))]
    ).run(
        sender=sp.address("tz1i66XefcqsNVSGa2iFsWb8qxokm3neVpFR"), amount=sp.mutez(20500000))

    # nft_contract.mint([sp.address("tz1Zn3WK57gjcsk6WH8MD6jf4VEqXuRfgPFM")]).run(
    #     sender=sp.address("tz1Zn3WK57gjcsk6WH8MD6jf4VEqXuRfgPFM"), amount=sp.mutez(20500000))

    sc.show(nft_contract.data)

    c1 = GameGov(
        admin=sp.address("tz1i66XefcqsNVSGa2iFsWb8qxokm3neVpFR"),
        nft_contract=nft_contract.address,
        building_categories=sp.big_map(
            {}, tkey=sp.TNat, tvalue=T_BUILDING_CATEGORY)
    )
    sc += c1
    c1.start_game(0).run(sender=sp.address(
        "tz1i66XefcqsNVSGa2iFsWb8qxokm3neVpFR"))
    print(c1)


# A a compilation target (produces compiled code)
sp.add_compilation_target("GameGov_Compiled", GameGov(
    admin=sp.address("tz1i66XefcqsNVSGa2iFsWb8qxokm3neVpFR"),
    nft_contract=sp.address("KT1KFczzgYkxLqTGmhbBvmew12WN3qbkBq4E"),
    building_categories=DATA_BUILDINGS
))
