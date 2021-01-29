import joblib
import pandas as pd
import streamlit as st
import joblib
from reportlab.pdfgen import canvas
import os
import base64
import pickle
import lightgbm as lgb

model = joblib.load('final2.pkl')

st.title('Kardiyovasküler Hastalık Riski Tahmini')


st.markdown('Sefa Kocakalay Tez Projesi')



age_year = st.number_input('Yaşınız',
                      value= 36)

gender = st.multiselect('Cinsiyetiniz',
                        ['Kadın', 'Erkek'],
                        default = 'Kadın')

height = st.number_input('Boyunuz',
                         value= 180)

weight = st.number_input('Kilonuz',
                         value= 75)

st.markdown('**> Muayene Bilgileri **')

ap_hi = st.number_input('Sistolik Kan Basıncı (mm/hg)',
                        value= 120)

ap_lo = st.number_input('Distolik Kan Basıncı (mm/hg)',
                        value= 40)

cholesterol = st.number_input('Kolestrol (mg/dL)',
                       value= 150)

gluc = st.number_input('Glikoz (mg/dL)',
                       value= 100)

st.markdown('**> Hastanın Alışkanlıkları**')

smoke = st.multiselect('Sigara içiyor musunuz',
                       ['Hayır', 'Evet'],
                       default = 'Evet')

alco = st.multiselect('Alkol tüketiyor musunuz',
                      ['Hayır', 'Evet'],
                      default = 'Evet')


active = st.multiselect('Fiziksel Aktivite yapıyor musunuz',
                        ['Hayır', 'Evet'],
                        default = 'Evet')



height_m = height
weight_m = weight

age_m = age_year
age_m = 1 if (age_m < 45) else age_m
age_m = 2 if (age_m >= 45) and (age_m < 55) else age_m
age_m = 3 if (age_m >= 45) and (age_m < 60) else age_m
age_m = 4 if (age_m >= 60) else age_m

gender_m = 1 if (gender[0] == 'Kadın') else 2

chol_m = cholesterol
chol_m = 1 if (chol_m < 200) else chol_m
chol_m = 2 if (chol_m >= 200) and (chol_m < 240) else chol_m
chol_m = 3 if (chol_m >= 240) else chol_m

gluc_m = gluc
gluc_m = 1 if (gluc_m < 100) else gluc_m
gluc_m = 2 if (gluc_m >= 100) and (gluc_m < 125) else gluc_m
gluc_m = 3 if (gluc_m >= 125) else gluc_m

smoke_m = 1 if (smoke[0] == 'Evet') else 0

alco_m = 1 if (alco[0] == 'Evet') else 0

active_m = 1 if (active[0] == 'Evet') else 0

bmi_m = weight/((height/100) ** 2)
bmi_m = 1 if (bmi_m < 18.5) else bmi_m
bmi_m = 2 if (bmi_m >= 18.5) and (bmi_m < 25) else bmi_m
bmi_m = 3 if (bmi_m >= 25) and (bmi_m < 30) else bmi_m
bmi_m = 4 if (bmi_m >= 30) else bmi_m

bpc_m = 'tansiyon'
bpc_m = 1 if (ap_hi < 120) and (ap_lo < 80) else bpc_m
bpc_m = 2 if (ap_hi >= 120 and ap_hi < 130
             ) and (ap_lo < 80) else bpc_m
bpc_m = 3 if (ap_hi >= 130 and ap_hi < 140
             ) or (ap_lo >= 80 and ap_lo < 90) else bpc_m
bpc_m = 4 if (ap_hi >= 140 and ap_hi < 180
             ) or (ap_lo >= 90 and ap_lo < 120) else bpc_m
bpc_m = 5 if (ap_hi >= 180) or (ap_lo >= 120) else bpc_m


st.markdown('**> Tahmin Yap**')


predict_button = st.button("Rapor Oluştur")

if predict_button:
    result = model.predict_proba([[age_m, height_m, weight_m, gender_m,
                                   chol_m, gluc_m,
                                   smoke_m, alco_m,
                                   active_m, bmi_m,
                                   bpc_m]])
    #st.write([age_m, height_m, weight_m, gender_m,chol_m, gluc_m,smoke_m, alco_m,active_m, bmi_m,bpc_m])
    
    if result[0][0] >= 0.5:
        risc = 'Negatif Risk'
    else:
        risc = 'Pozitif Risk'
    
    st.write(risc)
    st.write('Olasılık:',
             round(result[0][1]*100, 1), '%')
