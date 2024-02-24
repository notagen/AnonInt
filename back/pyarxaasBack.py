from pyarxaas import ARXaaS
from pyarxaas.privacy_models import KAnonymity
from pyarxaas import AttributeType
from pyarxaas import Dataset
from pyarxaas.hierarchy import RedactionHierarchyBuilder, IntervalHierarchyBuilder
import pandas as pd
import streamlit as st

arxaas = ARXaaS("http://localhost:8080/")

df = st.session_state.template
#dataset = Dataset.from_pandas(df)

def setAttrType(myAttr, myAttrType, dataset):
    if myAttrType == "Identifying":
        dataset.set_attribute_type(AttributeType.IDENTIFYING, myAttr)
    if myAttrType == "Quasiidentifiyng":
        dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, myAttr)
    if myAttrType == "Sensitive":
        dataset.set_attribute_type(AttributeType.SENSITIVE, myAttr)
    if myAttrType == "Insensitive":
        dataset.set_attribute_type(AttributeType.INSENSITIVE, myAttr)
    return dataset

def setReductHierarch(myAttr):
    myList = df[myAttr].tolist()
    reduction_based = RedactionHierarchyBuilder(
        redaction_char='~',
        redaction_order=RedactionHierarchyBuilder.Order.LEFT_TO_RIGHT
    )
    reduction_hierarchy = arxaas.hierarchy(reduction_based, myList)
    return reduction_hierarchy

def setIntervHierarch(myAttr, interval_list):
    myList = df[myAttr].tolist()
    print(myList)
    interval_based = IntervalHierarchyBuilder()
    for i in interval_list:
        interval_based.add_interval(int(interval_list[0][0]),int(interval_list[0][1]),interval_list[0][2])
    interval_hierarchy = arxaas.hierarchy(interval_based, myList)
    return interval_hierarchy