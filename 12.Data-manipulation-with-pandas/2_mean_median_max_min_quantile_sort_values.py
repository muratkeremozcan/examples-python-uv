from dataframes.sales import sales
from dataframes.sales_short import sales_short

# Key takeaways for DataFrame aggregations:
# .mean(), .median(), .min(), .max(), .std(), .var(), .count() - built-in aggregations
# .quantile(q) - get qth percentile (e.g., .quantile(0.75) for 75th percentile)
# .agg(func) - apply custom function to column(s)
# .agg([func1, func2]) - apply multiple functions
# .cumsum(), .cummax(), .cummin(), .cumprod() - cumulative operations
# df[['col1', 'col2']].agg(func) - apply function to multiple columns
# Column-oriented structure makes these operations very fast (vectorized)

print(sales.head())

print('\ninfo():')
print(sales.info())

print('\nmean():')
print(sales['weekly_sales'].mean())

print('\nmedian():')
print(sales['weekly_sales'].median())

print('\nmax():')
print(sales['date'].max())

print('\nmin():')
print(sales['date'].min())

print('\nusing custom function to apply to to the dataframe ( df.apply(fn) ):')
# inter-quartile range (75th percentile minus the 25th percentile)
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

print(sales['temperature_c'].agg(iqr))

print('\napply custom function to multiple columns:')
print(sales[['temperature_c', 'fuel_price_usd_per_l', 'unemployment']].agg(iqr))

print('\napply multiple functions to multiple columns:')
print(sales[['temperature_c', 'fuel_price_usd_per_l', 'unemployment']].agg([iqr, 'median']))

########

# sort sales by date
sales_by_date = sales_short.sort_values('date')

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
print('\ncumulative sum, cumsum() :')
sales_by_date['cum_weekly_sales'] = sales_by_date['weekly_sales'].cumsum()
# Get the cumulative max of weekly_sales, add as cum_max_sales col
print('cumulative max, cummax() :')
sales_by_date['cum_max_sales'] = sales_by_date['weekly_sales'].cummax()

print(sales_by_date[['date', 'weekly_sales','cum_weekly_sales', 'cum_max_sales']])
