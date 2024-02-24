from pyarxaas import ARXaaS
from pyarxaas.privacy_models import KAnonymity, LDiversityDistinct
from pyarxaas import AttributeType
from pyarxaas import Dataset
from pyarxaas.hierarchy import RedactionHierarchyBuilder, IntervalHierarchyBuilder
import pandas as pd
from sklearn import datasets

arxaas = ARXaaS("http://localhost:8080/")

df=pd.read_csv('insuranceRoundedBmiClean.csv')
df['bmi'] = df['bmi'].astype(int)
dataset = Dataset.from_pandas(df)
attrList = df.columns.to_list()

#set ATTR type
#dataset.set_attribute_type(AttributeType.IDENTIFYING, 'Unnamed: 0')
dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'age')
dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'sex')
dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'bmi')
dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'children')
dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'smoker')
dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'region')
dataset.set_attribute_type(AttributeType.SENSITIVE, 'charges')

interval_based = IntervalHierarchyBuilder()
intervalList = [(0,10,'1'),(11,20,'2'),(21,30,'3'),(31,40,'4'),(41,50,'5'),(51,60,'6')]
intevalNames = ['name1','name2','name3','name4','name5','name6','name7']

age_hier = pd.read_csv('insurance-real_hierarchy_age.csv', sep=',', header=None)
sex_hier = pd.read_csv('insurance-real_hierarchy_sex.csv', sep=',', header=None)
bmi_hier = pd.read_csv('insurance-real_hierarchy_bmi.csv', sep=',', header=None)
childern_hier = pd.read_csv('insurance-real_hierarchy_children.csv', sep=',', header=None)
region_hier = pd.read_csv('insurance-real_hierarchy_region.csv', sep=',', header=None)
smoker_hier = pd.read_csv('insurance-real_hierarchy_smoker.csv', sep=',', header=None)

dataset.set_hierarchy('age', age_hier)
dataset.set_hierarchy('sex', sex_hier)
dataset.set_hierarchy('bmi', bmi_hier)
dataset.set_hierarchy('smoker', smoker_hier)
dataset.set_hierarchy('region', region_hier)
dataset.set_hierarchy('children', childern_hier)

print('/n')

kanon1 = KAnonymity(5)
kanon2 = LDiversityDistinct(2, 'charges')

anon_result = arxaas.anonymize(dataset, [kanon1, kanon2])
print('\n')
print(anon_result.risk_profile.re_identification_risk)
print(anon_result.anonymization_metrics.attribute_generalization)

