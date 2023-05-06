import statistics
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

columns_dataset2 = ['Employee Name', 'Job Title', 'Base Pay', 'Overtime Pay', 'Other Pay', 'Benefits', 'Total Pay',
                    'Total Pay & Benefits', 'Year', 'Notes', 'Agency', 'Status']

dataset2 = pd.read_csv('dataset2.csv')


print('============== Job Title ===============')
JobTitle = dataset2['Job Title']

print('Mode:', statistics.mode(JobTitle))
# print('Mode:', JobTitle.mode()[0])


print('============== Base Pay ===============')
BasePay = dataset2['Base Pay']
mean_BasePay = BasePay.mean()

print('Median:', BasePay.median())
print('Mean:', mean_BasePay)
print('Mode:', statistics.mode(BasePay))
# print('Mode:', BasePay.mode()[0])

# plt.figure(figsize=(10, 8))
# plt.hist(BasePay, bins=20)
# plt.axvline(mean_BasePay, color='red', linestyle='dashed', linewidth=2)
# plt.xlabel('Base Pay')
# plt.ylabel('count')
# plt.title('Base Pay distribution in the dataset')
# plt.savefig('BasePay.png')


print('============== Overtime Pay ===============')
OvertimePay = dataset2['Overtime Pay']
mean_OvertimePay = OvertimePay.mean()

print('Median:', OvertimePay.median())
print('Mean:', mean_OvertimePay)
print('Mode:', statistics.mode(OvertimePay))
# print('Mode:', OvertimePay.mode()[0])

# plt.figure(figsize=(10, 8))
# plt.hist(OvertimePay, bins=20)
# plt.axvline(mean_OvertimePay, color='red', linestyle='dashed', linewidth=2)
# plt.xlabel('Overtime Pay')
# plt.ylabel('count')
# plt.title('Overtime Pay distribution in the dataset')
# plt.savefig('OvertimePay.png')

plt.figure(figsize=(10, 8))
sns.boxplot(x='Overtime Pay', data=dataset2)
plt.savefig('Boxplot Overtime Pay.png')


print('============== Other Pay ===============')
OtherPay = dataset2['Other Pay']

print('Median:', OtherPay.median())
print('Mean:', OtherPay.mean())
print('Mode:', statistics.mode(OtherPay))
# print('Mode:', OtherPay.mode()[0])


print('============== Benefits ===============')
Benefits = dataset2['Benefits']

print('Median:', Benefits.median())
print('Mean:', Benefits.mean())
print('Mode:', statistics.mode(Benefits))
# print('Mode:', Benefits.mode()[0])

plt.figure(figsize=(10, 8))
sns.boxplot(x='Benefits', data=dataset2)
plt.savefig('Boxplot Benefits.png')


print('============== Total Pay ===============')
TotalPay = dataset2['Total Pay']

print('Median:', TotalPay.median())
print('Mean:', TotalPay.mean())
print('Mode:', statistics.mode(TotalPay))
# print('Mode:', TotalPay.mode()[0])

plt.figure(figsize=(10, 8))
sns.boxplot(x='Total Pay', data=dataset2)
plt.savefig('Boxplot Total Pay.png')


# ================= boxplot =================
# dataset2[['Job Title 1', 'Job Title 2', 'Job Title 3', 'Job Title 4']] = JobTitle.str.split(',', expand=True)
PROGRAMMER = dataset2[JobTitle.str.contains('PROGRAMMER')]
RESEARCH = dataset2[JobTitle.str.contains('RESEARCH')]
data = pd.concat([PROGRAMMER])

plt.figure(figsize=(30, 8))
plt.yticks(rotation=30, ha="right")
sns.boxplot(x='Total Pay & Benefits', y='Job Title', data=data)
plt.savefig('Boxplot Job Title PROGRAMMER & Total Pay & Benefits.png')