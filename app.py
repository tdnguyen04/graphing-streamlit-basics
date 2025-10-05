import streamlit as st
import plotly.express as px
import pandas as pd


# y = 2x + 3

start_point = -50
step = 0.25
num_points = int(abs(start_point) / step * 2)

a = 2
b = 3

x_vals = [start_point + i * step for i in range(num_points)]
y_vals = [a * x + b for x in x_vals]

df = pd.DataFrame({"x": x_vals, "y": y_vals})

print(df)
fig = px.line(df, x="x", y="y", labels={"x": "X-axis", "y": "Y-axis"})

fig.update_xaxes(
    range=[-5, 5],
    zeroline=True,
    zerolinewidth=2,
    zerolinecolor="LightGray",
    ticks="outside",
    tickwidth=2,
    ticklen=10,
    tickcolor="black",
)
fig.update_yaxes(
    range=[-5, 5],
    zeroline=True,
    zerolinewidth=2,
    zerolinecolor="LightGray",
    ticks="outside",
    tickwidth=2,
    ticklen=10,
    tickcolor="black",
    scaleanchor="x"
)

st.plotly_chart(fig)
