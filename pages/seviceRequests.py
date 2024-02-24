import requests
import streamlit as st
from pyarxaas import Dataset

url = "http://localhost:8080"
analyseUrl = "http://localhost:8080/api/analyze"

data2 = st.session_state.dtst._payload()
st.write(data2)
st.write(st.session_state.dtst)

data = {"data" : [ [ "age", "gender", "zipcode" ], [ "34", "male", "81667" ], [ "35", "female", "81668" ], [ "36", "male", "81669" ], [ "37", "female", "81670" ], [ "38", "male", "81671" ], [ "39", "female", "81672" ], [ "40", "male", "81673" ], [ "41", "female", "81674" ], [ "42", "male", "81675" ], [ "43", "female", "81676" ], [ "44", "male", "81677" ] ],
  "attributes" : [ {
    "field" : "age",
    "attributeTypeModel" : "IDENTIFYING",
    "hierarchy" : None
  }, {
    "field" : "gender",
    "attributeTypeModel" : "SENSITIVE",
    "hierarchy" : None
  }, {
    "field" : "zipcode",
    "attributeTypeModel" : "QUASIIDENTIFYING",
    "hierarchy" : None
  } ],
  "privacyModels" : None,
  "suppressionLimit" : None
}
data1 =  {"data" : [ [ "age", "gender", "zipcode" ], [ "34", "male", "81667" ], [ "35", "female", "81668" ], [ "36", "male", "81669" ], [ "37", "female", "81670" ], [ "38", "male", "81671" ], [ "39", "female", "81672" ], [ "40", "male", "81673" ], [ "41", "female", "81674" ], [ "42", "male", "81675" ], [ "43", "female", "81676" ], [ "44", "male", "81677" ] ],
  "attributes" : [ {
    "field" : "age",
    "attributeTypeModel" : "IDENTIFYING",
    "hierarchy" : None
  }, {
    "field" : "gender",
    "attributeTypeModel" : "SENSITIVE",
    "hierarchy" : None
  }, {
    "field" : "zipcode",
    "attributeTypeModel" : "QUASIIDENTIFYING",
    "hierarchy" : None
  } ], # type: ignore
  "privacyModels" : None,
  "suppressionLimit" : None
} 

response = requests.post(analyseUrl,json=data2)

st.write(response.text)


# dataframe --> dicr = {"data":[[columns], [...], [...]]
#                        "attributes":[{
#                                            "field" : "age",
#                                            "attributeTypeModel" : "IDENTIFYING",
#                                            "hierarchy" : None
#                                     }, {...}]
#                       }