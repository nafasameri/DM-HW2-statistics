import statistics
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


def boxplot(data, name):
    plt.figure(figsize=(24, 8))
    sns.boxplot(x='Total Pay & Benefits', y='Job Title', data=data)
    plt.yticks(rotation=30, ha="right")
    # plt.yticks(ha="left")
    plt.title(name)
    plt.savefig('Boxplot ' + name + '.png')



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
plt.title('Overtime Pay')
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
plt.title('Benefits')
plt.savefig('Boxplot Benefits.png')

print('============== Total Pay ===============')
TotalPay = dataset2['Total Pay']

print('Median:', TotalPay.median())
print('Mean:', TotalPay.mean())
print('Mode:', statistics.mode(TotalPay))
# print('Mode:', TotalPay.mode()[0])

plt.figure(figsize=(10, 8))
sns.boxplot(x='Total Pay', data=dataset2)
plt.title('Total Pay')
plt.savefig('Boxplot Total Pay.png')

print('============== Total Pay & Benefits ===============')
plt.figure(figsize=(10, 8))
sns.boxplot(x='Total Pay & Benefits', data=dataset2)
plt.title('Total Pay & Benefits')
plt.savefig('Boxplot Total Pay & Benefits.png')


# ================= boxplot =================
# dataset2[['Job Title 1', 'Job Title 2', 'Job Title 3', 'Job Title 4']] = JobTitle.str.split(',', expand=True)
# data['Job Title'] = data['Job Title'].str.lower()

# PROGRAMMER = dataset2[JobTitle.str.contains('PROGRAMMER')]
# data = pd.concat([PROGRAMMER])
# boxplot(data, 'PROGRAMMER & Total Pay & Benefits')
#
# COMPUTER = dataset2[JobTitle.str.contains('COMPUTER')]
# data = pd.concat([COMPUTER])
# boxplot(data, 'COMPUTER & Total Pay & Benefits')
#
# ENGINEERING = dataset2[JobTitle.str.contains('ENGINEERING')]
# data = pd.concat([ENGINEERING])
# boxplot(data, 'ENGINEERING & Total Pay & Benefits')
#
# # RESEARCHER = dataset2[JobTitle.str.contains('RESEARCHER')]
# # data = pd.concat([RESEARCHER])
# # boxplot(data, 'RESEARCHER & Total Pay & Benefits')
#
# PHYSICIANANDSURGEON = dataset2[JobTitle.str.contains('PHYSICIAN AND SURGEON')]
# data = pd.concat([PHYSICIANANDSURGEON])
# boxplot(data, 'PHYSICIAN AND SURGEON & Total Pay & Benefits')
#
# DENTIST = dataset2[JobTitle.str.contains('DENTIST')]
# data = pd.concat([DENTIST])
# boxplot(data, 'DENTIST & Total Pay & Benefits')




dataset2.loc[JobTitle.str.contains('PROGRAMMER'), 'Job Title'] = 'PROGRAMMER'
dataset2.loc[JobTitle.str.contains('DENTIST'), 'Job Title'] = 'DENTIST'
dataset2.loc[JobTitle.str.contains('COMPUTER'), 'Job Title'] = 'COMPUTER'
dataset2.loc[JobTitle.str.contains('ENGINEERING'), 'Job Title'] = 'ENGINEERING'
dataset2.loc[JobTitle.str.contains('PHYSICIAN AND SURGEON'), 'Job Title'] = 'PHYSICIAN AND SURGEON'


PROGRAMMER = dataset2[JobTitle.str.contains('PROGRAMMER')]
COMPUTER = dataset2[JobTitle.str.contains('COMPUTER')]
ENGINEERING = dataset2[JobTitle.str.contains('ENGINEERING')]
PHYSICIANANDSURGEON = dataset2[JobTitle.str.contains('PHYSICIAN AND SURGEON')]
DENTIST = dataset2[JobTitle.str.contains('DENTIST')]
data = pd.concat([DENTIST, PHYSICIANANDSURGEON, ENGINEERING, PROGRAMMER, COMPUTER])

boxplot(data, 'Job Title & Total Pay & Benefits')
