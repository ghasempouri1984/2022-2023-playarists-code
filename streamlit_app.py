import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.express as px
import numpy as np


# Load data
country_df = pd.read_csv('SSH_Publications_and_Journals_by_Country.csv')
disciplines_df = pd.read_csv('SSH_Publications_by_Discipline.csv')

uk_data = pd.read_csv("uk_data.csv")
us_data = pd.read_csv("us_data.csv")

uk_data = uk_data.sort_values('Publications_in_venue', ascending=False)
us_data = us_data.sort_values('Publications_in_venue', ascending=False)

uk_disc = pd.read_csv("uk_disciplines_count.csv")
us_disc = pd.read_csv("us_disciplines_count.csv")

# First Viz
def viz1():
    total_erih_plus = 11128
    total_oc_meta = 8689
    coverage_percentage = (total_oc_meta / total_erih_plus) * 100
    remaining = 100 - coverage_percentage
    coverage_data = [coverage_percentage, remaining]
    labels = ['Covered in OpenCitations Meta', 'Not in OpenCitations Meta']
    #plt.title('ERIH Plus Journals in OC Meta Coverage')
    sns.set_style("whitegrid")
    plt.pie(coverage_data, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    st.pyplot(plt)

# Second Viz
def viz2():
    meta_coverage_df = pd.read_csv('SSH_Publications_in_OC_Meta_and_Open_Access_status.csv')  # replace '<your file>' with your actual file path
    access_counts = meta_coverage_df['Open Access'].value_counts()
    plt.figure(figsize=(6, 6))
    sns.set_style("whitegrid")
    plt.pie(access_counts, labels=access_counts.index, autopct='%1.1f%%')
    #plt.title('Open Access Status')
    st.pyplot(plt)

# Third Viz
def viz3():
    color_scale = [
        [0.0, '#f7fbff'],
        [0.001, '#deebf7'],
        [0.002, '#c6dbef'],
        [0.005, '#9ecae1'],
        [0.10, '#6baed6'],
        [0.20, '#4292c6'],
        [0.30, '#2171b5'],
        [0.40, '#08519c'],
        [0.50, '#08306b'],
        [1.0, '#081d58'],
    ]
    fig = px.choropleth(country_df, locations='Country',
                        locationmode='country names',
                        color='Publication_count',
                        hover_name='Country',
                        color_continuous_scale=color_scale,
                        title='')
    st.plotly_chart(fig)

# Fourth viz
def viz4():
    all_countries = country_df.sort_values(by='Publication_count', ascending=False)
    countries = all_countries.iloc[:30]
    plt.figure(figsize=(10, 8))
    sns.barplot(x='Publication_count', y='Country', data=countries, palette='flare')
    plt.xscale('log')
    plt.xlabel('Publication Count')
    plt.ylabel('Countries')
    plt.title('Publications by Country (Top 30)')
    plt.grid(axis="x", linewidth=0.2)
    x_values = np.array([100, 1000, 10000, 100000, 1000000])
    plt.xticks(x_values, x_values)

    st.pyplot(plt)
    
# Fifth viz
def viz5():
    all_countries = country_df.sort_values(by='Journal_count', ascending=False)
    countries = all_countries.iloc[:30]
    plt.figure(figsize=(10, 8))
    sns.barplot(x='Journal_count', y='Country', data=countries, palette='flare')
    plt.xlabel('Journal Count')
    plt.ylabel('Countries')
    plt.title('Journals by Country (Top 30)')
    plt.grid(axis="x", linewidth=0.2)

    st.pyplot(plt)

# Sixth viz
def viz6():
    all_countries = country_df.sort_values(by='Publication_count', ascending=False)
    last_countries = all_countries.iloc[-30:]
    plt.figure(figsize=(10, 8))
    sns.barplot(x='Publication_count', y='Country', data=last_countries, palette='viridis')
    plt.xlabel('Publication Count')
    plt.ylabel('Countries')
    plt.title('Publications by Country  (Last 30)')
    plt.grid(axis="x", linewidth=0.2)

    st.pyplot(plt)
    
# Seventh viz
def viz7():
    all_countries = country_df.sort_values(by='Journal_count', ascending=False)
    last_countries = all_countries.iloc[-30:]
    plt.figure(figsize=(10, 8))
    sns.barplot(x='Journal_count', y='Country', data=last_countries, palette='viridis')
    plt.xlabel('Journal Count')
    plt.ylabel('Countries')
    plt.title('Journals by Country (Last 30)')
    plt.grid(axis="x", linewidth=0.2)

    st.pyplot(plt)

# Eight viz
def viz8():

    colors = ['steelblue', 'skyblue', 'lightskyblue', 'deepskyblue', 'dodgerblue', 'cornflowerblue',
              'mediumblue', 'royalblue', 'mediumslateblue', 'slateblue', 'blueviolet', 'darkviolet',
              'mediumorchid', 'indigo', 'purple', 'darkmagenta', 'palegreen', 'limegreen', 'forestgreen',
              'darkgreen', 'gold', 'goldenrod', 'darkorange', 'chocolate', 'sienna', 'saddlebrown',
              'tomato', 'orangered', 'firebrick', 'crimson', 'maroon']

    sns.set()  # Imposta le impostazioni predefinite di seaborn

    plt.figure(figsize=(10, 6))
    sns.barplot(data=disciplines_df, x='Publication_count', y='Discipline', palette=colors)
    plt.xlabel('Publications')
    plt.ylabel('Discipline')
    plt.title('Publications by Disciplines')
    plt.grid(axis="x", linewidth=0.2)

    st.pyplot(plt)
    
# UK
def viz9():
    plt.figure(figsize=(20, 7))
    
    plt.title("UK - correlation between number of Disciplines and number of Publications per Journal", fontweight="bold", fontsize=15)
    
    # Define a colormap - You can choose any colormap you like
    cmap = plt.get_cmap('viridis')
    
    # Customize scatterplot style
    plt.scatter(
        uk_data["Publications_in_venue"],
        uk_data["disc_count"],
        marker='s',                     # Use squares as markers
        c=uk_data["Publications_in_venue"],        # Set marker color based on x-axis values
        cmap=cmap,                      # Use the defined colormap
        s=50,                           # Set marker size to 50
        alpha=0.7,                      # Set marker transparency to 0.7
        vmin=0,                         # Minimum value for color mapping
        vmax=15000                      # Maximum value for color mapping
    )
    
    
    plt.xlabel("number of Publications in venue")
    plt.ylabel("number of disciplines per venue")
    
    # Set custom x and y axis ranges
    plt.xlim(0, 15000)
    plt.ylim(0, 23)  # Shorten the y-axis range to 0-10
    
    # Set custom x and y ticks
    plt.xticks(range(0, 15000, 1000))  # One tick every 1000 on the x-axis
    plt.yticks(range(23))  # One tick every integer on the y-axis
    
    # Adjust the spacing around the plot
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
    
    #plt.show()
    st.pyplot(plt)
# US
def viz10():
    plt.figure(figsize=(20, 7))

    plt.title("US - correlation between number of Disciplines and number of Publications per Journal", fontweight="bold", fontsize=15)
    
    # Define a colormap - You can choose any colormap you like
    cmap = plt.get_cmap('viridis')
    
    # Normalize the x-axis values to the range [0, 1] to use them for color mapping
    '''x_values = uk_data["Publications_in_venue"]
    x_min, x_max = np.min(x_values), np.max(x_values)
    x_normalized = (x_values - x_min) / (x_max - x_min)'''
    
    # Customize scatterplot style
    plt.scatter(
        us_data["Publications_in_venue"],
        us_data["disc_count"],
        marker='s',                     # Use squares as markers
        c=us_data["Publications_in_venue"],        # Set marker color based on x-axis values
        cmap=cmap,                      # Use the defined colormap
        s=50,                           # Set marker size to 50
        alpha=0.7,                      # Set marker transparency to 0.7
        vmin=0,                         # Minimum value for color mapping
        vmax=15000                      # Maximum value for color mapping
    )
    
    plt.xlabel("number of Publications in venue")
    plt.ylabel("number of disciplines per venue")
    
    # Set custom x and y axis ranges
    plt.xlim(0, 36000)
    plt.ylim(0, 23)  # Shorten the y-axis range to 0-10
    
    # Set custom x and y ticks
    plt.xticks(range(0, 36000, 2000))  # One tick every 1000 on the x-axis
    plt.yticks(range(23))  # One tick every integer on the y-axis
    
    # Adjust the spacing around the plot
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)

    st.pyplot(plt)



def viz11():
    # remove outliers from data US
    outliers = [470652, 341568, 341841, 343110]
    filtered_us_data = us_data.sort_values("Publications_in_venue", ascending=False)
    
    for idx, row in filtered_us_data.iterrows():
        if row["EP_id"] in outliers:
            filtered_us_data.drop(filtered_us_data[filtered_us_data['EP_id'] == row["EP_id"]].index, inplace=True)
    # US
    import plotly.graph_objects as go
    import plotly.io as pio
    
    # Define a colormap - You can choose any colormap you like
    cmap = plt.get_cmap('viridis')
    
    # Create a trace for the scatter plot
    scatter_trace = go.Scatter(
        x=filtered_us_data["Publications_in_venue"],
        y=filtered_us_data["disc_count"],
        mode='markers',
        marker=dict(size=10, color=filtered_us_data["Publications_in_venue"], colorscale='viridis'),
        text=filtered_us_data["Original Title"],  # Use the 'metadata' column from us_data for tooltips
        hoverinfo='text'
    )
    
    # Create the layout for the plot
    layout = go.Layout(
        title="US - correlation between number of Disciplines and number of Publications per Journal",
        xaxis_title="number of Publications in venue",
        yaxis_title="number of disciplines per venue",
        width=1000,              # Adjust the width of the plot
        height=500,             # Adjust the height of the plot
        margin=dict(l=50, r=50, t=80, b=50),  # Adjust the margins around the plot
    )
    
    # Create the figure and add the trace and layout
    fig = go.Figure(data=[scatter_trace], layout=layout)
    # Display the interactive scatter plot
    st.plotly_chart(fig)


def viz12():
    filtered_uk_data = uk_data[uk_data['EP_id'] != 422484]
    # UK
    # Define a colormap - You can choose any colormap you like
    cmap = plt.get_cmap('viridis')
    
    # Create a trace for the scatter plot
    scatter_trace = go.Scatter(
        x=filtered_uk_data["Publications_in_venue"],
        y=filtered_uk_data["disc_count"],
        mode='markers',
        marker=dict(size=10, color=filtered_uk_data["Publications_in_venue"], colorscale='viridis'),
        text=filtered_us_data["Original Title"],  # Use the 'metadata' column from us_data for tooltips
        hoverinfo='text'
    )
    
    # Create the layout for the plot
    layout = go.Layout(
        title="US - correlation between number of Disciplines and number of Publications per Journal",
        xaxis_title="number of Publications in venue",
        yaxis_title="number of disciplines per venue",
        width=1000,              # Adjust the width of the plot
        height=500,             # Adjust the height of the plot
        margin=dict(l=50, r=50, t=80, b=50),  # Adjust the margins around the plot
    )
    
    # Create the figure and add the trace and layout
    fig = go.Figure(data=[scatter_trace], layout=layout)
    # Display the interactive scatter plot
    st.plotly_chart(fig)

def viz13():
    # Set width of bar
    barWidth = 0.25
    fig = plt.subplots(figsize=(12, 8))
    
    # Set height of bar
    UK = uk_disc["Publication_count"]
    US = us_disc["Publication_count"]
    
    # Set position of bar on Y axis
    br1 = np.arange(len(UK))
    br2 = [x + barWidth for x in br1]
    
    # Make the plot
    plt.barh(br1, UK, color='b', height=barWidth, edgecolor='black', label='UK')
    plt.barh(br2, US, color='y', height=barWidth, edgecolor='black', label='US')
    
    # Adding Yticks
    plt.ylabel("Comparing US and UK Publication type", fontweight='bold', fontsize=15)
    plt.xlabel('Disciplines by Publications', fontweight='bold', fontsize=15)
    plt.yticks([r + barWidth for r in range(len(UK))], uk_disc["Disciplines"])
    
    plt.gca().invert_yaxis()
    
    plt.legend()
    st.pyplot()

def viz14():
    # Set width of bar
    uk_disc = uk_disc.sort_values('Journal_count', ascending=False)    
    us_disc = us_disc.sort_values('Journal_count', ascending=False)    
    
    barWidth = 0.25
    fig = plt.subplots(figsize=(12, 8))
    
    # Set height of bar
    UK = uk_disc["Journal_count"]
    US = us_disc["Journal_count"]
    
    # Set position of bar on Y axis
    br1 = np.arange(len(UK))
    br2 = [x + barWidth for x in br1]
    
    # Make the plot
    plt.barh(br1, UK, color='b', height=barWidth, edgecolor='black', label='UK')
    plt.barh(br2, US, color='y', height=barWidth, edgecolor='black', label='US')
    
    # Adding Yticks
    plt.ylabel("Comparing US and UK Journal type", fontweight='bold', fontsize=15)
    plt.xlabel('Disciplines by Journals', fontweight='bold', fontsize=15)
    plt.yticks([r + barWidth for r in range(len(UK))], uk_disc["Disciplines"])
    
    plt.gca().invert_yaxis()
    
    plt.legend()
    st.pyplot()

# Streamlit code
def main():
  
    st.title("Article")
    
    st.markdown(
        """
        [Here is a link to our article](https://doi.org/10.5281/zenodo.7979806)
        """,
        unsafe_allow_html=True,
    )

    st.title("Software GitHub Repo")

    st.markdown(
        """
        [Here is a link to our software GitHub repo to reproduce](https://github.com/open-sci/2022-2023-playarists-code)
        """,
        unsafe_allow_html=True,
    )
      
    st.title("Visualizations")
    
    st.header("The coverage of publications in SSH journals (according to ERIH-PLUS) included in OpenCitations Meta")
    viz1()
    
    st.header("Open Access Status")
    viz2()
    
    st.header("Publications by Discipline")
    viz8()
    
    st.header("Publications by Country")
    viz3()
    
    st.header("Publications by Country Top 30")
    viz4()
    
    st.header("Journals by Country Top 30")
    viz5()
    
    st.header("Publications by Country Last 30")
    viz6()
    
    st.header("Journals by Country Last 30")
    viz7()
    
    st.header("Scatterplot for Correlation bw Number of Disciplines and Number of Publications per Journal")
    viz9()
    viz11()
    viz10()
    viz12()


    st.header("Barchart for disciplines by Publications and Journals, comparing the two countries")
    viz13()
    viz14()
    
    

if __name__ == "__main__":
    main()
