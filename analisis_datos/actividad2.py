import seaborn as sns

diamonds = sns.load_dataset('diamonds')

print(diamonds)

sns.histplot(diamonds['price'], kde= False, binwidth=500)


