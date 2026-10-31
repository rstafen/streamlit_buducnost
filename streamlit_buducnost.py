import random
import streamlit as st

otazka='chces vediet svoju buducnost?'
zoznam_odpovedi = [
        'budes bohaty',
        'budes chudobny',
        'stratis skolsku tasku',
        'rozbijes telku',
        'spadnes zo skaly',
        'stretnes medveda',
        'vyhras fortnite FNCS',
        'stratis sa v lese',
        'budes utekat pred besnym psom',
        'vylupis banku a chytia ta potom',
        'pojdes do vezenia na 5 rokov',
        'dozijes sa 95 rokov',
        'budes mudry',
        'budes hlupy',
        'spadnes do jamy',
        'budes vlastnit sukromne lietadlo',
        'rozbijes staru vazu',
        'strapnis sa pred celym svetom'      
    ]


def daj_odpoved():
    # vrati nahodnu hodnotu zo zoznamu
    odpoved = random.choice(zoznam_odpovedi)
    return f'Tvojou buducnostou je: {odpoved}!'

st.title('Objav svoju buducnost')

velkost_pisma = "28px"       # Napríklad: 20px, 32px, 40px...
farba_pisma = "#FF4B4B"      # Streamlit červená (Môžete použiť aj 'blue', 'green', 'orange'...)


# 4. Pridanie tlačidla a kontrola, či naň používateľ klikol
if st.button('Chces vediet svoju buducnost?'):
    # Volanie funkcie a uloženie výsledku
    vysledok = daj_odpoved()
else:
    vysledok = 'Nevahaj a klikni!!!!'
    
st.markdown(
    f"""
    <p style="font-size: {velkost_pisma}; color: {farba_pisma}; font-weight: bold;">
        {vysledok}
    </p>
    """, 
    unsafe_allow_html=True
)
#python -m streamlit run C:/Users/rasti/.spyder-py3/streamlit_buducnost.py
