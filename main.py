import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# 0. configure the page
st.set_page_config(
    page_title="Apple Stock Analysis App",
    page_icon="🍏",
    layout="wide",
)

# 1. load the data
@st.cache_data
def load_data():
    # Update the path to the apple_stock.csv file
    file_path = 'data/apple_stock.csv'
    df = pd.read_csv(file_path, parse_dates=['Date'])
    return df

# 2. build the UI
st.title("Apple Stock Analysis App")
with st.spinner("Loading data..."):
    df = load_data()

st.header("Apple Stock Dataset")
st.info("Raw data in Dataframe")
st.dataframe(df, use_container_width=True)

st.success("Column information of the dataset")
cols = df.columns.tolist()
st.subheader(f'Total columns {len(cols)} ➡  {", ".join(cols)}')

# 3. add some graphs and widgets
st.header("Data Visualization")

# Graph 1: Line Chart for Closing Price Over Time
fig1 = px.line(df, x='Date', y='Close', title='Closing Price Over Time')

# Graph 2: scatter Plot for Closing Price vs Date
fig2 = px.scatter(df, x='Date', y='Close', title='Scatter Plot: Closing Price vs Date')

# Graph 3: Scatter Plot for Volume vs Date
fig3 = px.scatter(df, x='Date', y='Volume', title='Scatter Plot: Volume vs Date')

# Graph 4: Box Plot for Distribution of Closing Price
fig4 = px.box(df, y='Close', title='Box Plot: Distribution of Closing Price')

# Graph 5: Histogram for Distribution of Closing Price
fig5 = px.histogram(df, x='Close', title='Histogram: Distribution of Closing Price')

# Graph 6: Area Chart for Closing Price Over Time
fig6 = px.area(df, x='Date', y='Close', title='Area Chart: Closing Price Over Time')
# Graph 7: Violin Plot for Closing Price Distribution
fig7 = px.violin(df, y='Close', title='Violin Plot: Closing Price Distribution')

# Graph 8: Heatmap for Correlation Matrix
corr_matrix = df.corr()
fig8 = px.imshow(corr_matrix, color_continuous_scale='Viridis', title='Heatmap: Correlation Matrix')

# Graph 9: Pie Chart for Proportion of Trading Days
fig9 = px.pie(df, names='Volume', title='Pie Chart: Proportion of Trading Days')

# Graph 10: 3D Scatter Plot for Closing Price vs Date vs Volume
fig10 = px.scatter_3d(df, x='Date', y='Close', z='Volume', title='3D Scatter Plot: Closing Price vs Date vs Volume')

# Displaying graphs
st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig3, use_container_width=True)
st.plotly_chart(fig4, use_container_width=True)
st.plotly_chart(fig5, use_container_width=True)
st.plotly_chart(fig6, use_container_width=True)
st.plotly_chart(fig7, use_container_width=True)
st.plotly_chart(fig8, use_container_width=True)
st.plotly_chart(fig9, use_container_width=True)
st.plotly_chart(fig10, use_container_width=True)

# 4. adjust layout
t1, t2, t3 = st.tabs(["Bivariate", "Trivariate", 'About'])
num_cols = df.select_dtypes(include=np.number).columns.tolist()

with t1:
    c1, c2 = st.columns(2)
    col1 = c1.radio("Select the first column for scatter plot", num_cols)
    col2 = c2.radio("Select the second column for scatter plot", num_cols)
    fig = px.scatter(df, x=col1, y=col2, title=f'{col1} vs {col2}')
    st.plotly_chart(fig, use_container_width=True)

with t2:
    c1, c2, c3 = st.columns(3)
    col1 = c1.selectbox("Select the first column for 3D plot", num_cols)
    col2 = c2.selectbox("Select the second column for 3D plot", num_cols)
    col3 = c3.selectbox("Select the third column for 3D plot", num_cols)
    fig = px.scatter_3d(df, x=col1, y=col2, z=col3, title=f'{col1} vs {col2} vs {col3}', height=700)
    st.plotly_chart(fig, use_container_width=True)

# About Section
with t3:
    st.title("About the App")
    st.write(
        """
        Welcome to the Apple Stock Analysis App! This web application allows you to explore and visualize the Apple stock dataset.

        *Data Source:*
        The dataset used in this app contains information about Apple's stock, including date, open, high, low, close prices, volume, and trading days.

        *Data Visualization:*
        The app provides various visualizations to help you analyze the stock data, including line charts, candlestick charts, scatter plots, box plots, histograms, area charts, violin plots, a heatmap, a pie chart, and a 3D scatter plot. You can explore trends over time, the distribution of closing prices, and relationships between different variables.

        *Bivariate and Trivariate Analysis:*
        The "Bivariate" and "Trivariate" tabs allow you to create scatter plots and 3D plots by selecting different columns from the dataset. This enables you to investigate relationships between specific numerical columns.

        *How to Use:*
        - In the "Bivariate" tab, choose two columns to generate a scatter plot.
        - In the "Trivariate" tab, select three columns to create a 3D scatter plot.

        Enjoy exploring the Apple stock dataset!
        Created By Adarsh Singh
        """
    )
