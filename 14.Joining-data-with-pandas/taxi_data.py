import pandas as pd

# Sample rows (top/bottom) from the taxi owner/vehicle tables.

# taxi_owners: 10-row slice from the 3,519-row table.
taxi_owners = pd.DataFrame(
    [
        {
            "rid": "T6285",
            "vid": 6285,
            "owner": "AGEAN TAXI LLC",
            "address": "4536 N. ELSTON AVE.",
            "zip": 60630,
        },
        {
            "rid": "T4862",
            "vid": 4862,
            "owner": "MANGIB CORP.",
            "address": "5717 N. WASHTENAW AVE.",
            "zip": 60659,
        },
        {
            "rid": "T1495",
            "vid": 1495,
            "owner": "FUNRIDE, INC.",
            "address": "3351 W. ADDISON ST.",
            "zip": 60618,
        },
        {
            "rid": "T4231",
            "vid": 4231,
            "owner": "ALQUSH CORP.",
            "address": "6611 N. CAMPBELL AVE.",
            "zip": 60645,
        },
        {
            "rid": "T5971",
            "vid": 5971,
            "owner": "EUNIFFORD INC.",
            "address": "3351 W. ADDISON ST.",
            "zip": 60618,
        },
        {
            "rid": "T4453",
            "vid": 4453,
            "owner": "IMAGIN CAB CORP",
            "address": "3351 W. ADDISON ST.",
            "zip": 60618,
        },
        {
            "rid": "T121",
            "vid": 121,
            "owner": "TRIBECA CAB CORP",
            "address": "4536 N. ELSTON AVE.",
            "zip": 60630,
        },
        {
            "rid": "T3465",
            "vid": 3465,
            "owner": "AMIR EXPRESS INC",
            "address": "3351 W. ADDISON ST.",
            "zip": 60618,
        },
        {
            "rid": "T1962",
            "vid": 1962,
            "owner": "KARY CAB COMPANY",
            "address": "4707 N. KENTON AVE.",
            "zip": 60630,
        },
        {
            "rid": "T1031",
            "vid": 1031,
            "owner": "NECT 42 LLC",
            "address": "6500 N. WESTERN AVE.",
            "zip": 60645,
        },
    ]
)

# taxi_veh: 10-row slice from the 3,519-row table.
taxi_veh = pd.DataFrame(
    [
        {
            "vid": 2767,
            "make": "TOYOTA",
            "model": "CAMRY",
            "year": 2013,
            "fuel_type": "HYBRID",
            "owner": "SEYED M. BADRI",
        },
        {
            "vid": 1411,
            "make": "TOYOTA",
            "model": "RAV4",
            "year": 2017,
            "fuel_type": "HYBRID",
            "owner": "DESZY CORP.",
        },
        {
            "vid": 6500,
            "make": "NISSAN",
            "model": "SENTRA",
            "year": 2019,
            "fuel_type": "GASOLINE",
            "owner": "AGAPH CAB CORP",
        },
        {
            "vid": 2746,
            "make": "TOYOTA",
            "model": "CAMRY",
            "year": 2013,
            "fuel_type": "HYBRID",
            "owner": "MIDWEST CAB CO, INC",
        },
        {
            "vid": 5922,
            "make": "TOYOTA",
            "model": "CAMRY",
            "year": 2013,
            "fuel_type": "HYBRID",
            "owner": "SUMETTI CAB CO",
        },
        {
            "vid": 5902,
            "make": "TOYOTA",
            "model": "CAMRY",
            "year": 2013,
            "fuel_type": "HYBRID",
            "owner": "SAFAR INC",
        },
        {
            "vid": 1407,
            "make": "HYUNDAI",
            "model": "ELANTRA",
            "year": 2018,
            "fuel_type": "GASOLINE",
            "owner": "MYKONOS CAB CORP.",
        },
        {
            "vid": 854,
            "make": "TOYOTA",
            "model": "CAMRY",
            "year": 2012,
            "fuel_type": "HYBRID",
            "owner": "JOELIZ CORP INC",
        },
        {
            "vid": 6274,
            "make": "TOYOTA",
            "model": "CAMRY",
            "year": 2012,
            "fuel_type": "HYBRID",
            "owner": "A K O S INC",
        },
        {
            "vid": 4675,
            "make": "FORD",
            "model": "ESCAPE",
            "year": 2011,
            "fuel_type": "FLEX FUEL",
            "owner": "MAJAZ CORP",
        },
    ]
)
