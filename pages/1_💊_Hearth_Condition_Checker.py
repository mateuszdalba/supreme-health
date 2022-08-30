import pandas as pd
import streamlit as st
import pickle


st.title('Please fill in below information about your health in order to predict your hearth condition')



col1, col2, col3 = st.columns(3)


with col1:
    st.markdown('Have you ever had coronary heart disease (CHD) or myocardial infarction (MI) ?')
    #0 - No, 1 - Yes
    var_heart_disease = st.selectbox(label='CHD or MI', options=('No','Yes'))

    st.markdown('Body Mass Index (BMI)')
    var_bmi = st.slider(label='BMI',min_value=12, value=25, step=1, max_value=95)

    st.markdown('Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes]')
    #0 - No, 1 - Yes
    var_smoke = st.radio(label='Smoking',options=('No','Yes'), index=0)

with col2:
    st.markdown('Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week')
    #0 - No, 1 - Yes
    var_drink = st.selectbox(label='Drinking', options=('No','Yes'), index=0)

    st.markdown('Do you have serious difficulty walking or climbing stairs?')
    #0 - No, 1 - Yes
    diff_walking = st.selectbox(label='Difficulty Walking', options=('No','Yes'), index=0)

    st.markdown('Are you male or female?')
    # 0 - Female, 1 - Male
    var_sex = st.radio(label='Smoking',options=('Female','Male'), index=0)
    

with col3:
    st.markdown('Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30')
    var_physical_health = st.slider(label='PhysicalHealth',min_value=0, value=10, step=1, max_value=30)

    st.markdown('Thinking about your mental health, for how many days during the past 30 days was your mental health not good?')
    var_mental_health = st.slider(label='MentalHealth',min_value=0, value=10, step=1, max_value=30)

    st.markdown('Fourteen-level age category')
    #65-69 - 9 , 60-64 - 8 , 70-74 - 10, 55-59 - 7, 50-54  - 6, 80 or older - 12, 45-49 - 5, 75-79 - 11, 18-24 - 0, 40-44 - 4, 35-39 - 3, 30-34 - 2, 25-29-1
    var_age_category = st.selectbox(label='Age', options=('18-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80 or older'), index=0)

st.markdown('Imputed race/ethnicity value')
#White - 5, Hispanic - 3, Black - 2, Other - 4, Asian - 1, American Indian/Alaskan Native - 0
var_race = st.selectbox(label='Race', options=('American Indian/Alaskan Native','Asian','Black','Hispanic','Other','White'), index=0)

st.markdown('(Ever told) (you had) diabetes?')
#0 - No, Yes - 2, No, borderline diabetes - 1, 
var_race = st.selectbox(label='Diabetic', options=('No','Yes','No, borderline diabetes','Yes (during pregnancy)'), index=0)

st.markdown('Adults who reported doing physical activity or exercise during the past 30 days other than their regular job')
#Yes - 1 , No - 0
var_psychical_activity = st.selectbox(label='psychical activity', options=('No','Yes'), index=0)

st.markdown('Would you say that in general your health is...')
# 4 = Very Good, 2 = Good, 0 = Excellent, 1 = Fair, 3 = Poor 
var_general_health = st.selectbox(label='gen health', options=('Poor','Fair','Good','Very Good','Excellent'), index=0)

st.markdown('On average, how many hours of sleep do you get in a 24-hour period?')
var_sleep = st.slider(label='sleep time',min_value=1, value=8, step=1, max_value=24)

st.markdown('(Ever told) (you had) asthma?')
# 0 - No, 1 - Yes
var_asthma = st.selectbox(label='asthma',options=('No','Yes'))

st.markdown('Not including kidney stones, bladder infection or incontinence, were you ever told you had kidney disease?')
# 0 - No, 1 - Yes
var_kidney = st.selectbox(label='kidney disease',options=('No','Yes'))

st.markdown('(Ever told) (you had) skin cancer?')
# 0 - No, 1 - Yes
var_skin_cancer = st.selectbox(label='skin cancer',options=('No','Yes'))



pred_button = st.button('Check your heart CONDITION')


if pred_button:

    #Load model
    loaded_model = pickle.load(open('models/first_try_model', 'rb'))


    loaded_model.predict([[prod_year, parking_assist, car_cat, horse_power, automatic_gearbox,
                                    engine_capacity, car_mileage, fuel_gasoline,fuel_gasoline_cng,fuel_gasoline_lpg,fuel_diesel,fuel_hybrid]])

    st.success(f"""The price of this car should be around: ***{np.round(price[0],2)}*** PLN """)





