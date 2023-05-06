import statistics
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

columns_dataset1 = ['Complete TCGA ID', 'Gender', 'Age at Initial Pathologic Diagnosis', 'ER Status', 'PR Status',
                    'HER2 Final Status', 'Tumor', 'Tumor--T1 Coded', 'Node', 'Node-Coded', 'Metastasis',
                    'Metastasis-Coded', 'AJCC Stage', 'Converted Stage', 'Survival Data Form', 'Vital Status',
                    'Days to Date of Last Contact', 'Days to date of Death', 'OS event', 'OS Time', 'PAM50 mRNA',
                    'SigClust Unsupervised mRNA', 'SigClust Intrinsic mRNA', 'miRNA Clusters', 'methylation Clusters',
                    'RPPA Clusters', 'CN Clusters', 'Integrated Clusters (with PAM50)', 'Integrated Clusters (no exp)',
                    'Integrated Clusters (unsup exp)']
dataset1 = pd.read_csv('dataset1.csv')


print('============== Age ===============')
age = dataset1['Age at Initial Pathologic Diagnosis']
mean_age = age.mean()

print('Median:', age.median())
print('Mean:', mean_age)
print('Mode:', statistics.mode(age))

plt.figure(figsize=(10, 8))
plt.hist(age, bins=20)
plt.axvline(mean_age, color='red', linestyle='dashed', linewidth=2)
plt.xlabel('age')
plt.ylabel('count')
plt.title('Age distribution in the dataset')
plt.savefig('age.png')


print('============== Tumor ===============')
tumor = dataset1['Tumor']
tumor_mode = statistics.mode(tumor)
print('Mode:', tumor_mode)

plt.figure(figsize=(10, 8))
plt.hist(tumor)
plt.axvline(tumor_mode, color='red', linestyle='dashed', linewidth=2)
plt.xlabel('tumor')
plt.ylabel('count')
plt.title('Tumor distribution in the dataset')
plt.savefig('tumor.png')


print('============== Node ===============')
node = dataset1['Node']
node_mode = statistics.mode(node)
print('Mode:', node_mode)

plt.figure(figsize=(10, 8))
plt.hist(node)
plt.axvline(node_mode, color='red', linestyle='dashed', linewidth=2)
plt.xlabel('node')
plt.ylabel('count')
plt.title('Node distribution in the dataset')
plt.savefig('node.png')


print('============== AJCC Stage ===============')
AJCCStage = dataset1['AJCC Stage']
AJCCStage_mode = statistics.mode(AJCCStage)
print('Mode:', AJCCStage_mode)

plt.figure(figsize=(10, 8))
plt.hist(AJCCStage)
plt.axvline(AJCCStage_mode, color='red', linestyle='dashed', linewidth=2)
plt.xlabel('AJCCStage')
plt.ylabel('count')
plt.title('AJCCStage distribution in the dataset')
plt.savefig('AJCCStage.png')


# ============ boxplot ==============
plt.figure(figsize=(10, 8))
sns.boxplot(x='Age at Initial Pathologic Diagnosis', y='Tumor', data=dataset1)
plt.savefig('Boxplot Age & Tumor.png')

plt.figure(figsize=(10, 8))
sns.boxplot(x='Age at Initial Pathologic Diagnosis', y='AJCC Stage', data=dataset1)
plt.savefig('Boxplot Age & AJCC Stage.png')
