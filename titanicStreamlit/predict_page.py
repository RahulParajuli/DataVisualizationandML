import streamlit as st
import pickle

def load_model():
  with open ('model (1).pkl','rb') as file:
    data = pickle.load(file)
  return data

data = load_model()

def show_predict_page():
  st.title("Eydean Inc")
  st.write("""### we need some information to predict the survival rate""")


  output = (
  'PassengerId',
  'Survived',
  'Pclass',
  'Name',
  'Sex',
  'Age',
  'SibSp',
  'Parch'
  'Ticket',
  'Fare',
  'Cabin',
  'Embarked',
  )

  task = (
    "Classification",
    "Regression",
    "Time series"
  )

  
  tasks = st.selectbox("select operation", task)
  output_column = st.selectbox("Output column", output)
  experience = st.slider("year", 0,50,3)

  ok = st.button("Calculate")
  if ok:
    salary = data.predict()
    st.subheader(f"the estimated salary is ${salary[0]}:.2f")

