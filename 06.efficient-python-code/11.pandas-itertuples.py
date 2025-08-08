# .itertuples() is a faster row-wise loop that returns each row as a namedtuple
import pandas as pd

rangers_df = pd.DataFrame(
    {
        "Team": ["TEX"] * 37,
        "League": ["AL"] * 37,
        "Year": [
            2012,
            2011,
            2010,
            2009,
            2008,
            2007,
            2006,
            2005,
            2004,
            2003,
            2002,
            2001,
            2000,
            1999,
            1998,
            1997,
            1996,
            1993,
            1992,
            1991,
            1990,
            1989,
            1988,
            1987,
            1986,
            1985,
            1984,
            1983,
            1982,
            1980,
            1979,
            1978,
            1977,
            1976,
            1975,
            1974,
            1973,
        ],
        "RS": [
            808,
            855,
            787,
            784,
            901,
            816,
            835,
            865,
            860,
            826,
            843,
            890,
            848,
            945,
            940,
            807,
            928,
            835,
            682,
            829,
            676,
            695,
            637,
            823,
            771,
            617,
            656,
            639,
            590,
            756,
            750,
            692,
            767,
            616,
            714,
            690,
            619,
        ],
        "RA": [
            707,
            677,
            687,
            740,
            967,
            844,
            784,
            858,
            794,
            969,
            882,
            968,
            974,
            859,
            871,
            823,
            799,
            751,
            753,
            814,
            696,
            714,
            735,
            849,
            743,
            785,
            714,
            609,
            749,
            752,
            698,
            632,
            657,
            652,
            733,
            698,
            844,
        ],
        "W": [
            93,
            96,
            90,
            87,
            79,
            75,
            80,
            79,
            89,
            71,
            72,
            73,
            71,
            95,
            88,
            77,
            90,
            86,
            77,
            85,
            83,
            83,
            70,
            75,
            87,
            62,
            69,
            77,
            64,
            76,
            83,
            87,
            94,
            76,
            79,
            83,
            57,
        ],
        "G": [
            162,
            162,
            162,
            162,
            162,
            162,
            162,
            162,
            162,
            162,
            162,
            162,
            162,
            162,
            162,
            162,
            163,
            162,
            162,
            162,
            162,
            162,
            161,
            162,
            162,
            161,
            161,
            163,
            162,
            163,
            162,
            162,
            162,
            162,
            162,
            161,
            162,
        ],
        "Playoffs": [
            1,
            1,
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            1,
            1,
            0,
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
    }
)

# Team League  Year   RS   RA   W    G  Playoffs
# 0   TEX     AL  2012  808  707  93  162         1
# 1   TEX     AL  2011  855  677  96  162         1
# 2   TEX     AL  2010  787  687  90  162         1
# 3   TEX     AL  2009  784  740  87  162         0
# 4   TEX     AL  2008  901  967  79  162         0
# 5   TEX     AL  2007  816  844  75  162         0
# 6   TEX     AL  2006  835  784  80  162         0
# 7   TEX     AL  2005  865  858  79  162         0
# 8   TEX     AL  2004  860  794  89  162         0
# 9   TEX     AL  2003  826  969  71  162         0
# 10  TEX     AL  2002  843  882  72  162         0
# 11  TEX     AL  2001  890  968  73  162         0
# 12  TEX     AL  2000  848  974  71  162         0
# 13  TEX     AL  1999  945  859  95  162         1

for row in rangers_df.itertuples():
    print(row)

# Pandas(Index=0, Team='TEX', League='AL', Year=2012, RS=808, RA=707, W=93, G=162, Playoffs=1)
# Pandas(Index=1, Team='TEX', League='AL', Year=2011, RS=855, RA=677, W=96, G=162, Playoffs=1)
# Pandas(Index=2, Team='TEX', League='AL', Year=2010, RS=787, RA=687, W=90, G=162, Playoffs=1)

for row in rangers_df.itertuples():
    i = row.Index
    year = row.Year
    wins = row.W

    if row.Playoffs == 1:
        print(i, year, wins)

# 0 2012 93
# 1 2011 96
# 2 2010 90
# 13 1999 95
# 14 1998 88
# 16 1996 90


###

run_diffs = []

for row in rangers_df.itertuples():

    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = runs_scored - runs_allowed

    run_diffs.append(run_diff)

# Append new column
rangers_df["RD"] = run_diffs
print(rangers_df)

#    Team League  Year   RS   RA   W    G  Playoffs   RD
# 0   TEX     AL  2012  808  707  93  162         1  101
# 1   TEX     AL  2011  855  677  96  162         1  178
# 2   TEX     AL  2010  787  687  90  162         1  100
# 3   TEX     AL  2009  784  740  87  162         0   44
# 4   TEX     AL  2008  901  967  79  162         0  -66
# 5   TEX     AL  2007  816  844  75  162         0  -28
# 6   TEX     AL  2006  835  784  80  162         0   51
# 7   TEX     AL  2005  865  858  79  162         0    7
# 8   TEX     AL  2004  860  794  89  162         0   66
# 9   TEX     AL  2003  826  969  71  162         0 -143
# 10  TEX     AL  2002  843  882  72  162         0  -39
# 11  TEX     AL  2001  890  968  73  162         0  -78
# 12  TEX     AL  2000  848  974  71  162         0 -126
# 13  TEX     AL  1999  945  859  95  162         1   86
