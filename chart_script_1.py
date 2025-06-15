import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the data
df = pd.read_csv("risparmi_mensili.csv")

# Display the first few rows to understand the data structure
print("Data structure:")
print(df.head())
print("\nColumns:", df.columns.tolist())

# Create horizontal bar chart
fig = px.bar(df, 
             y='Area', 
             x='Risparmio_Euro_Mese',
             orientation='h',
             color='Risparmio_Euro_Mese',
             color_continuous_scale='Greens',
             title='Risparmi Mensili per Area di Intervento')

# Add text annotations at the end of each bar
for i, row in df.iterrows():
    fig.add_annotation(
        x=row['Risparmio_Euro_Mese'],
        y=row['Area'],
        text=f"€{row['Risparmio_Euro_Mese']:,.0f}",
        showarrow=False,
        xanchor='left',
        font=dict(size=10)
    )

# Update layout according to strict instructions
fig.update_layout(
    xaxis_title='Risparmio (€)',
    yaxis_title='Area',
    coloraxis_showscale=False  # Hide color scale legend for cleaner look
)

# Format x-axis values with abbreviations if needed
fig.update_xaxes(tickformat='.0f')

# Save the chart
fig.write_image('risparmi_mensili_chart.png')
fig.show()