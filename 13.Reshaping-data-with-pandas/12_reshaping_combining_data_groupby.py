import pandas as pd

# Values ordered by year, then sex (Female, Male)
data = [
    [20.2, 15.3, 15.3],  # 1995, Female
    [16.8, 8.9, 12.8],   # 1995, Male
    [24.2, 20.1, 18.1],  # 2005, Female
    [21.5, 13.2, 16.9],  # 2005, Male
    [28.5, 24.9, 20.8],  # 2015, Female
    [26.8, 18.0, 21.5],  # 2015, Male
]
index = pd.MultiIndex.from_product(
    [[1995, 2005, 2015], ["Female", "Male"]], names=["year", "biological_sex"]
)
columns = pd.MultiIndex.from_product(
    [["perc_obesity"], ["Argentina", "Brazil", "France"]], names=[None, "country"]
)
obesity = pd.DataFrame(data, index=index, columns=columns)

print(obesity)

# - Row index levels: year, biological_sex
# - Column index levels: (top) None with label perc_obesity, (next) country (Argentina, Brazil, France)
#                     perc_obesity              
# country                Argentina Brazil France
# year biological_sex                           
# 1995 Female                 20.2   15.3   15.3
#      Male                   16.8    8.9   12.8
# 2005 Female                 24.2   20.1   18.1
#      Male                   21.5   13.2   16.9
# 2015 Female                 28.5   24.9   20.8
#      Male                   26.8   18.0   21.5


# obesity.stack(level="country")
# pushes the country from the column into the row index 
# • - Row index levels: year, biological_sex, country
# • - Columns: perc_obesity

# print(obesity.stack(level='country'))
#                                perc_obesity
# year biological_sex country                
# 1995 Female         Argentina          20.2
#                     Brazil             15.3
#                     France             15.3
#      Male           Argentina          16.8
#                     Brazil              8.9
#                     France             12.8
# 2005 Female         Argentina          24.2
#                     Brazil             20.1
#                     France             18.1
#      Male           Argentina          21.5
#                     Brazil             13.2
#                     France             16.9
# 2015 Female         Argentina          28.5
#                     Brazil             24.9
#                     France             20.8
#      Male           Argentina          26.8
#                     Brazil             18.0
#                     France             21.5


# to use mean(), median() etc. we need to stack and groupby
# looks the same as obesity in the beginning 
# print(obesity.stack(level='country').groupby(level='country'))
#                     perc_obesity              
# country                Argentina Brazil France
# year biological_sex                           
# 1995 Female                 20.2   15.3   15.3
#      Male                   16.8    8.9   12.8
# 2005 Female                 24.2   20.1   18.1
#      Male                   21.5   13.2   16.9
# 2015 Female                 28.5   24.9   20.8
#      Male                   26.8   18.0   21.5

# Stack country level, group by country and get the mean
obesity_median = obesity.stack(level='country').groupby(level='country').median()
print(obesity_median)
#            perc_obesity
# country                
# Argentina         22.85
# Brazil            16.65
# France            17.50