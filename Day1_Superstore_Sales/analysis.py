import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/prabhavihemachandra/Desktop/Day1_Project/Sample - Superstore.csv', encoding='latin1')
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Analysis 1- Sales and Profit by Category

category_analysis = df.groupby('Category')[['Sales', 'Profit']].sum().round(2)
category_analysis = category_analysis.sort_values('Profit', ascending=False)
print("\n" +"="*50)
print("Analysis 1 - Sales and Profit by Category")
print("\n" +"="*50)
print(category_analysis)


""" 

df — take the whole dataset

groupby('Category') — group all rows by Category — so all Furniture rows together, all Technology rows together,
 all Office Supplies rows together

[['Sales', 'Profit']] — from those groups, only look at Sales and Profit columns .
 Ignore everything else

sum() — add up all the Sales and Profit numbers in each group

round(2) — round the result to 2 decimal places

sort_values('Profit') — sort the results by Profit column

ascending=False — show highest profit first — descending order
"""

# Analysis 2 - Sales and Profit by Region

region_analysis = df.groupby('Region')[['Sales', 'Profit']].sum().round(2)
region_analysis = region_analysis.sort_values('Profit', ascending=False)
print("\n" +"="*50)
print("Analysis 2 - Sales and Profit by Region")
print("\n" +"="*50)
print(region_analysis)

# Analysis 3  - Top 10 Loss Making Products
product_analysis = df.groupby('Product Name')[[ 'Profit']].sum().round(2)
loss_products = product_analysis[product_analysis['Profit']<0]
loss_products = loss_products.sort_values('Profit', ascending = True)
loss_products= loss_products.head(10)
print("\n" +"="*50)
print("Analysis 3  - Top 10 Loss Making Products")
print("\n" +"="*50)
print(loss_products)

"""take the whole dataset. group all rows by Product Name like so all product-1 rows together, all  all product-2 rows together,
 all  all product-3 rows together ect.From those groups, only look at  Profit column .
 Ignore everything else.Add up all the  Profit numbers in each group. Round the result to 2 decimal places.

 now product_analysis has two columns as Product Name and Profit. Go to 'Profit' column of it and get the rows where 'Profit' is less than zero
(here profit means the total profit of each product). Ater that assign it to loss_product. Then sort that that table in to the ascending order 
of profit in loss_product and reasign it to loss_product. Again take the top 10 from current loss_product, and reassign it as final loss_product.

head(10) takes the first 10 rows. Since we sorted ascending, the first 10 rows are the 10 products with the biggest losses
"""



# ================================================
# CHARTS
# ================================================

# Chart 1 - Sales and Profit by Category

fig, ax= plt.subplots(figsize = (10,6))
x= range(len(category_analysis))
width = 0.35

bars1 = ax.bar(x,category_analysis['Sales'], width, label ='Sales',color='steelblue')
bars2 = ax.bar([i + width for i in x],category_analysis['Profit'], width, label ='Profit',color='darkorange')
ax.set_title('Sales and Profit by Category', fontsize=14)
ax.set_xlabel('Category')
ax.set_ylabel('Amount ($)')
ax.set_xticks([i + width/2 for i in x])
ax.set_xticklabels(category_analysis.index)
ax.legend()

plt.tight_layout()
plt.savefig('/Users/prabhavihemachandra/Desktop/Day1_Project/chart1_category.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 1 saved!")


# Chart 2 - Sales and Profit by Region

fig, ax= plt.subplots(figsize = (10,6))
x= range(len(region_analysis))
width = 0.35

bars1 = ax.bar(x,region_analysis['Sales'], width, label ='Sales',color='steelblue')
bars2 = ax.bar([i + width for i in x],region_analysis['Profit'], width, label ='Profit',color='darkorange')
ax.set_title('Sales and Profit by Region', fontsize=14)
ax.set_xlabel('Region')
ax.set_ylabel('Amount ($)')
ax.set_xticks([i + width/2 for i in x])
ax.set_xticklabels(region_analysis.index)
ax.legend()

plt.tight_layout()
plt.savefig('/Users/prabhavihemachandra/Desktop/Day1_Project/chart2_category.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 2 saved!")

# Chart 3 - Top 10 Loss Making Products
fig, ax = plt.subplots(figsize=(12,8))

ax.barh(loss_products.index,loss_products['Profit'],color='crimson')
ax.set_title('Top 10 Loss Making Products by Profit', fontsize=14)
ax.set_xlabel('Total Profit ($)')
ax.set_ylabel('Product Name')

plt.tight_layout()
plt.savefig('/Users/prabhavihemachandra/Desktop/Day1_Project/chart3_category.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 3 saved!")