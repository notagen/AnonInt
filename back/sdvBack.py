import pandas as pd
from sdv.metadata import SingleTableMetadata
from sdv.single_table import GaussianCopulaSynthesizer


def createGaussian(data,n_rows):
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(data)
    metadata.validate()
    gaussSynth = GaussianCopulaSynthesizer(metadata)
    gaussSynth.fit(data)
    result = gaussSynth.sample(n_rows)
    return result

def concatHOR(data1, data2):
    new = pd.concat([data1,data2],axis=1)
    """l = {len(data1)<len(data2)?len(data1),len(data2)}"""
    if len(data1) < len(data2):
        l = len(data1)
    else:
        l = len(data2)
    new=new[:(len(data1))]
    return new

def concatVER(data1, data2):
    fil1=createGaussian(data2, len(data1))
    fil2=createGaussian(data1, len(data2))
    upData = concatHOR(data1,fil1)
    downData = concatHOR(fil2,data2)
    new = pd.concat([upData, downData],axis=0)
    return new

def catchDuplicates(df1, df2):
    return df1.columns.intersection(df2.columns).tolist()