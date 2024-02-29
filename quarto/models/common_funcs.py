import pandas as pd
from IPython.display import display
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px

def df_show_rand_sample(df: pd.DataFrame):
    display(df.sample(frac=1)\
                .reset_index(drop=True)\
                .head()\
                .style.hide(axis="index")\
                        .format(formatter="{:.3g}")
    )

## Custom plotly plot styling

# Remove the red color in discrete color scale
px.colors.qualitative.Plotly = px.colors.qualitative.Plotly[:1] + px.colors.qualitative.Plotly[2:]

pio.templates["custom"] = go.layout.Template(
    layout=go.Layout(
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="lightgreen"),
        colorscale=dict(sequential="Viridis"),
        colorway=px.colors.qualitative.Plotly)
)

pio.templates.default = "plotly+custom"

# Settings for plot rendering, makes work with HTML output + jupyer lab + static output
pio.renderers.default = "plotly_mimetype+notebook_connected+png"
