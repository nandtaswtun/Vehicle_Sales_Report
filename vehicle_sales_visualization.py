# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
sales_each_year = pd.read_csv("C:\\Users\\Lenovo\\Downloads\\sales.csv")
sales = sales_each_year.groupby('YEAR_ID')['TOTAL_SALES'].sum()
sales

# %%
classic_cars = pd.read_csv("C:\\Users\\Lenovo\\Downloads\\classic cars.csv")
classic_cars

# %%
classic_cars_pivot = classic_cars[
    (classic_cars['PRODUCTLINE'].isin([
        'Classic Cars',
        'Motorcycles',
        'Planes',
        'Ships',
        'Trains',
        'Trucks and Buses',
        'Vintage Cars']))
].groupby('COUNTRY')['TOTAL_SALES'].sum()

print(classic_cars_pivot)

# %%
september_march_count = pd.read_csv("C:\\Users\\Lenovo\\Downloads\\total sales.csv")
september_march_count

# %%
september_march_sales = september_march_count[
    (september_march_count['YEAR_ID'].isin([2003, 2005])) & 
    (september_march_count['MONTH_ID'].isin([9, 10, 11, 12, 1, 2, 3]))
].groupby('PRODUCTLINE')['TOTAL_QUANTITYORDERED'].sum()

print(september_march_sales)

# %%
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(30,10))
sns.barplot(x=sales.index, y=sales.values, palette='viridis', ax=axes[0])
axes[0].set_title('Total Sales')
axes[0].set_xlabel('Year')
axes[0].set_ylabel('Total')
axes[0].tick_params(axis='x', rotation=0)

sns.barplot(x=classic_cars_pivot.index, y=classic_cars_pivot.values, palette='plasma', ax=axes[1])
axes[1].set_title('Classic Cars Sales')
axes[1].set_xlabel('Country')
axes[1].set_ylabel('Total')
axes[1].tick_params(axis='x', rotation=45)

sns.barplot(x=september_march_sales.index, y=september_march_sales.values, palette='coolwarm', ax=axes[2])
axes[2].set_title('September - March Sales')
axes[2].set_xlabel('Product')
axes[2].set_ylabel('Total')
axes[2].tick_params(axis='x', rotation=45)

plt.show()


