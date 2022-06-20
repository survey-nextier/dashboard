import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

import numpy as np

st.set_page_config(page_title="Unicef Media Mapping", page_icon=":radio:", layout="wide")

sheet = "https://drive.google.com/uc?id=1Z_GxrmNDcpoSO-ZtWrMIbjdTDi7Ijjtm"

df = pd.read_csv(sheet)


df['ESTIMATED AUDIENCE SIZE'] = df['ESTIMATED AUDIENCE SIZE'].astype(int)


# df['ESTIMATED AUDIENCE SIZE'].dtype



# eas = df['ESTIMATED AUDIENCE SIZE']

# eas.dtype

'''
# UNICEF Media Mapping
Brief description about this section
'''

# df.columns

left_column, right_column = st.columns(2)

# left_column.selectbox("Select State", df['MAIN STATE'].unique())

# right_column.selectbox("Select Media Type", df['MEDIA TYPE'].unique())

with left_column:
# st.sidebar.header("Please Select a filter")
    media_type = st.selectbox("Select Media Type", options=df['MEDIA TYPE'].unique(),  )


df =  df.sort_values(by=['ESTIMATED AUDIENCE SIZE'], ascending=False)



# media_type
df = df.query("`MEDIA TYPE` == @media_type")

cols = ['MEDIA OUTLET', 'MEDIA TYPE',  'ESTIMATED AUDIENCE SIZE', 'REGION', 'MAIN STATE', 'MAIN STATE %', 'MALE', 'FEMALE', 'CHILDREN (7 - 12)', 'TEENS (13 - 17)', 'YOUTH/YOUNG ADULTS (18 - 29)', 'MIDDLE AGED ADULTS (30 - 44)', 'OLDER ADULTS', 'UPPER CLASS', 'UPPER MIDDLE CLASS', 'LOWER MIDDLE CLASS', 'LOWER CLASS', 'BELOW SUBSISTENCE' 
    , 'MARRIED', 'SINGLE', 'PRIMARY ORLOWER', 'HIGH/SECONDARY SCHOOL', 'DIPLOMA/NCE', '   DEGREE, HND OR HIGHER'  
]

df_1 = df[cols]

AgGrid(df_1)


'''
## Section Two
Brief description of this section
'''


cols = ['MEDIA OUTLET', 'MEDIA TYPE', 'N30,000 OR LESS _ _',  'N30,000 TO N50,000 _ _', 'N50,000 TO N100,000 _ _', 'N100,000 TO N200,000 _', 'N200,000 TO N500,000 _', "   DON'T KNOW/REFUSED", "CHRISTIANITY",  "ISLAM", "OTHERS RELIGION"]

df_2 = df[cols]

AgGrid(df_2)


'''
## Section Three
Brief description of this section
'''


cols = ['MEDIA OUTLET', 'MEDIA TYPE', 'WORKING', 'SELF -MPLOYED', 'STUDENT/APPRENTICE', 'RETIRED/ FULL HOUSEWIFE', 'UNEMPLOYED'  ]

df_3 = df[cols]

AgGrid(df_3)


st.markdown(f'''
<a href="{sheet}">Download csv</a>
''', unsafe_allow_html=True)

