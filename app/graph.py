import pandas as pd
import altair as alt
from altair import Chart, Tooltip


def chart(df: pd.DataFrame, x: str, y: str, target: str) -> Chart:
    """
    Creates an interactive chart using Altair with dynamic axes and color encoding.

    This function is designed to plot data from a pandas DataFrame and allows for 
    dynamic selection of different data columns for the x-axis, y-axis, and the 
    target variable used for color encoding. It automatically adapts to handle both 
    categorical and quantitative data for the target variable.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data to be visualized.
    x (str): The column name in df to be used for the x-axis.
    y (str): The column name in df to be used for the y-axis.
    target (str): The column name in df to be used for color encoding.

    Returns:
    Chart: An interactive Altair chart object.
    """


    title = f"{y} by {x} for {target}"

    # Check if the target is categorical (covers Rarity column)
    if df[target].dtype == object:
        target_type = 'N'  # Nominal (categorical) data type
        scale = alt.Scale(scheme='category10')  # Categorical color scheme
    else:
        target_type = 'Q'  # Quantitative data type
        scale = alt.Scale(scheme='purples')  # Quantitative color scheme

    graph = alt.Chart(
        df.sample(n=500, random_state=1),  # Sampling the data to avoid overplotting
        title=title,
        background="#1F1F1F"
    ).mark_circle(size=100).encode(
        x=alt.X(f"{x}:Q", axis=alt.Axis(title=x)),
        y=alt.Y(f"{y}:Q", axis=alt.Axis(title=y)),
        size=alt.Size('Energy:Q'),  # Size of circle marks based on 'Energy'
        color=alt.Color(f'{target}:{target_type}', scale=scale),  # Color encoding based on target
        tooltip=Tooltip(df.columns.to_list())  # Show all column values in the tooltip
    ).properties(
        width=600,
        height=450
    ).configure_title(
        fontSize=18,
        color="white"
    ).configure_axis(
        labelColor="gray",
        titleColor="white"
    ).configure_legend(
        labelColor="gray",
        titleColor="white"
    )
    
    # Return an interactive version of the chart
    return graph.interactive()
