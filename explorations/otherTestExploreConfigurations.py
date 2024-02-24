from pyarxaas import ARXaaS
from pyarxaas.privacy_models import KAnonymity, LDiversityDistinct, TClosenessEqualDistance
from pyarxaas import AttributeType
from pyarxaas import Dataset
from pyarxaas.hierarchy import RedactionHierarchyBuilder, IntervalHierarchyBuilder
import pandas as pd
from sklearn import datasets

arxaas = ARXaaS("http://localhost:8080/")


df=pd.read_csv('synthetic datasets\insuranceGaussianBmiInt.csv')
df['bmi'] = df['bmi'].astype(int)
dataset = Dataset.from_pandas(df)
attrList = df.columns.to_list()
newdf = pd.DataFrame()
indexdf=pd.DataFrame()
transdf = pd.DataFrame()

dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'age')
dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'sex')
dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'bmi')
dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'children')
dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'smoker')
dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'region')
dataset.set_attribute_type(AttributeType.SENSITIVE, 'charges')

age_hier = pd.read_csv('hierarchiesGaussian\insurance-gaussian_hierarchy_age.csv', sep=',', header=None)
sex_hier = pd.read_csv('hierarchiesGaussian\insurance-gaussian_hierarchy_sex.csv', sep=',', header=None)
bmi_hier = pd.read_csv('hierarchiesGaussian\insurance-gaussian_hierarchy_bmi.csv', sep=',', header=None)
childern_hier = pd.read_csv('hierarchiesGaussian\insurance-gaussian_hierarchy_children.csv', sep=',', header=None)
region_hier = pd.read_csv('hierarchiesGaussian\insurance-gaussian_hierarchy_region.csv', sep=',', header=None)
smoker_hier = pd.read_csv('hierarchiesGaussian\insurance-gaussian_hierarchy_smoker.csv', sep=',', header=None)

dataset.set_hierarchy('age', age_hier)
dataset.set_hierarchy('sex', sex_hier)
dataset.set_hierarchy('bmi', bmi_hier)
dataset.set_hierarchy('smoker', smoker_hier)
dataset.set_hierarchy('region', region_hier)
dataset.set_hierarchy('children', childern_hier)

#privacy models results

for k in (5,10,12,15,18):
    for l in (2,4,6,8,10,12,15):
        kanon1 = KAnonymity(k)
        kanon2 = LDiversityDistinct(l, 'charges')
        anon_result = arxaas.anonymize(dataset, [kanon1, kanon2])
        indexdf=indexdf.append([[k,l]], ignore_index=True)
        newdf=newdf.append(anon_result.risk_profile.re_identification_risk, ignore_index=True)
        transdf=transdf.append([[anon_result.anonymization_metrics.attribute_generalization[0]['generalizationLevel'],
                anon_result.anonymization_metrics.attribute_generalization[1]['generalizationLevel'],
                anon_result.anonymization_metrics.attribute_generalization[2]['generalizationLevel'],
                anon_result.anonymization_metrics.attribute_generalization[3]['generalizationLevel'],
                anon_result.anonymization_metrics.attribute_generalization[4]['generalizationLevel'],
                anon_result.anonymization_metrics.attribute_generalization[5]['generalizationLevel']]]
                , ignore_index=True)
     
"""
for k in (5,10,12,15,18):
    for t in (0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1):
        kanon1 = KAnonymity(k)
        kanon4=TClosenessEqualDistance(t,'charges')
        anon_result = arxaas.anonymize(dataset, [kanon1, kanon4])
        indexdf=indexdf.append([[k,t]], ignore_index=True)
        newdf=newdf.append(anon_result.risk_profile.re_identification_risk, ignore_index=True)
        transdf=transdf.append([[anon_result.anonymization_metrics.attribute_generalization[0]['generalizationLevel'],
                anon_result.anonymization_metrics.attribute_generalization[1]['generalizationLevel'],
                anon_result.anonymization_metrics.attribute_generalization[2]['generalizationLevel'],
                anon_result.anonymization_metrics.attribute_generalization[3]['generalizationLevel'],
                anon_result.anonymization_metrics.attribute_generalization[4]['generalizationLevel'],
                anon_result.anonymization_metrics.attribute_generalization[5]['generalizationLevel']]]
                , ignore_index=True)

    """             

finaldf = pd.concat([indexdf, newdf], axis=1)
finaldf = pd.concat([finaldf,transdf], axis=1)
print(finaldf)
finaldf.to_csv('klExploreCtganInsurance.csv')