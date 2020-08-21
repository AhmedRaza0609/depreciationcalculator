from calcfunc import *
import streamlit as st
import time

dep_type = st.selectbox('Select Depreciation type', ['Straight Line Method', 'Reducing Balance Method'])

cost = float(st.text_input('Purchase Cost', '0'))
rate = float(st.text_input('Depreciation Rate (enter out of hundred and not 0-1)', '0'))
yearofpur = int(st.text_input('Year of Purchase', '0'))
yearofsale = int(st.text_input('Year of Sale', '0'))
if dep_type == 'Reducing Balance Method':
    accum = float(st.text_input('Enter Accumulated cost', '0'))
else:
    accum = 0

st.success(f'The Netbook Value is: {int(depreciation(cost, rate, yearofpur, yearofsale, dep_type, accum))}')


if st.checkbox('Show Solution'):
    depn_sol(cost, rate, yearofpur, yearofsale, dep_type, 1, accum)
    if st.checkbox('Help Me!'):
        help_depn_sol(cost, rate, yearofpur, yearofsale, dep_type, 1, accum)
    depn_sol(cost, rate, yearofpur, yearofsale, dep_type, 2, accum)
    if st.checkbox('Help Me!‎'):
        help_depn_sol(cost, rate, yearofpur, yearofsale, dep_type, 2, accum)
