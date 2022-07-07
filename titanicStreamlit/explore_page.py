import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data():
  st.title("Upload a CSV file")
  uploaded_file = st.file_uploader("Choose a file")
  if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

    # Add some matplotlib code !
    fig, ax = plt.subplots()
    df.hist(
      bins=8,
      column="Age",
      grid=False,
      figsize=(8, 8),
      color="#86bf91",
      zorder=2,
      rwidth=0.9,
      ax=ax,
    )
    st.write(fig)
  return df

data = load_data()

st.write('Dataframe info:')
st.write(data.info())
st.write('-'*100)
st.write('\nDataframe describe:\n')
st.write(data.describe())
st.write('-'*100)
st.write('\nDataframe head:\n')
st.write(data.head())
st.write('-'*100)
st.write('\nDataframe shape:\n')
shape = data.shape
st.write("Rows : {}\nColumns : {}".format(shape[0], shape[1]))
st.write('-'*50)
st.write('No of null values:')
st.write(data.isna().sum())
data.dtypes.value_counts(normalize=True).sort_values(ascending=False).head(10).plot(kind='pie')
st.pyplot()
st.subheader("amount of labels in whole dataset")
for col in data.columns[0:]:
    st.write(col,": ", len(data[col].unique()), "labels")


def visuals(data):
  st.write("select graph to plot:")
    
  n = st.selectbox(
  "histogram",
  "heatmap",
  "scatterplot"
  )
  if n == "histogram":
    for col in data.columns[0:]:
        print(col,": ", len(data[col].unique()), "labels")
    
    column = st.selectbox("select a column for histogram", col)

    selected_column = data.columns[int(column)]
    st.write("you have selected: ", selected_column, "for histogram")
    if st.button("histogram") == True:
      plt.hist(data[selected_column])
      st.pyplot()
    else:
      print("operation has finished")
  elif n == "heatmap":
    import seaborn as sns
    for col in data.columns[0:]:
        print(col,": ", len(data[col].unique()), "labels")
        data = np.random.randint(low=1,
                          high=100,
                          size=(10, 10))
        annot = True
        sns.heatmap(data, annot=annot)
        st.pyplot()
        continue
    else:
      print("operation is cancelled")
  else:
    st.write("have a good day!!!")
  return "done"
  








def fill_random(df, col):
    df[col+'_random'] = df[col]
    df[col+'_random'][df[col+'_random'].isnull()] = df[col].dropna().sample(df[col].isnull().sum()).values
    return 

#converting object datatype to integer
def objconverter(df):
    for j in df.columns.values.tolist(): # Iterate on columns of dataframe
      try:
          df[j] = df[j].astype('int') # Convert datatype from object to int, of columns having all integer values 
      except:
          pass
    df.info()
    st.write("-" * 50)
    n = input("check number of labels for each columns?: y/n")
    if n == 'y':
      for col in df.columns[0:]:
        print(col,": ", len(df[col].unique()), "labels")
    return df

def outputcolumns(df):
  for i in range(1, len(df.columns)):
      print(str(i)+". "+str(df.columns[i]))
  print("-" * 50)
  output = input("\n Which one is your output column? ")
  output_column = df.columns[int(output)]
  print("you have selected output feature: ", output_column)
  return output_column


def visualization(df):
  while True:
    st.write("select graph to plot:\n")
    
    n = st.selectbox(
    "histogram",
    "heatmap",
    "scatterplot"
    )
    if n == "histogram":
      for col in df.columns[0:]:
          print(col,": ", len(df[col].unique()), "labels")
      
      column = st.selectbox("select a column for histogram", col)

      selected_column = df.columns[int(column)]
      st.write("you have selected: ", selected_column, "for histogram")
      if st.button("histogram") == True:
        plt.hist(df[selected_column])
        plt.show()
        continue
      else:
        print("operation has finished")
    elif n == "heatmap":
      import seaborn as sns
      for col in df.columns[0:]:
          print(col,": ", len(df[col].unique()), "labels")
          data = np.random.randint(low=1,
                            high=100,
                            size=(10, 10))
          annot = True
          a = sns.heatmap(df, annot=annot)
          plt.show()
          continue
      else:
        print("operation is cancelled")
    else:
      st.write("have a good day!!!")
    return "done"


# def show_explore_page():
#   st.title("explore data")
#   st.write('''
#   Eydean INC
#   ''')

#   data = df[''].value_counts()

#   fig1, ax1 =plt.subplot()
#   a