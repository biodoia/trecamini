import pandas as pd
import plotly.graph_objects as go

# Load the data
df = pd.read_csv("confronto_prestazioni.csv")

# Abbreviate metric names to fit 15 character limit
metric_abbreviations = {
    "Consumi Energetici (kWh/mese)": "Energy (kWh)",
    "Sprechi Alimentari (%)": "Food Waste (%)",
    "Incidenti Sicurezza (eventi/mese)": "Safety Events",
    "Tempo Controlli HACCP (ore/settimana)": "HACCP (hrs)",
    "Controllo Remoto (%)": "Remote Ctrl(%)"
}

# Apply abbreviations
df['Metrica_Short'] = df['Metrica'].map(metric_abbreviations)

# Create the grouped bar chart
fig = go.Figure()

# Add bars for "Prima_Automazione" (Before Automation) - using moderate red
fig.add_trace(go.Bar(
    name='Prima Auto',
    x=df['Metrica_Short'],
    y=df['Prima_Automazione'],
    marker_color='#B4413C',
    text=df['Prima_Automazione'],
    textposition='outside',
    cliponaxis=False
))

# Add bars for "Dopo_Automazione" (After Automation) - using light green
fig.add_trace(go.Bar(
    name='Dopo Auto',
    x=df['Metrica_Short'],
    y=df['Dopo_Automazione'],
    marker_color='#ECEBD5',
    text=df['Dopo_Automazione'],
    textposition='outside',
    cliponaxis=False
))

# Update layout
fig.update_layout(
    title='Automation Impact - Performance',
    xaxis_title='Metriche',
    yaxis_title='Valori',
    barmode='group',
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

# Save the chart
fig.write_image("performance_comparison.png")
fig.show()