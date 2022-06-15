import matplotlib.pyplot as plt
import pandas as pd
import os

expenditures = pd.read_csv(os.path.join(
  os.path.dirname(__file__), 'assets', 'eExpenditures_2022.csv'))

most_expensive = expenditures.nlargest(10, 'CheckAmt')
print(most_expensive)

Name = most_expensive["Category"]
Height = most_expensive["CheckAmt"]

# plt.figure(figsize=(15,8))
plt.bar(Name, Height, color='green')
plt.xlabel('Name of Thing')
plt.ylabel('Cost of Thing')
plt.title('Top Ten Things')
plt.show()
