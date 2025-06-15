import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

# Load the CSV file
df = pd.read_csv('funzionalita_sistema.csv')

# Display the first few rows to understand the data structure
print("Data structure:")
print(df.head())
print("\nColumns:", df.columns.tolist())
print("\nCategories:", df['Categoria'].unique())

# Group by category and calculate mean automation levels
automation_by_category = df.groupby('Categoria')['Automazione_Level'].mean().reset_index()
print("\nAutomation levels by category:")
print(automation_by_category)

# Create the radar chart
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=automation_by_category['Automazione_Level'],
    theta=automation_by_category['Categoria'],
    fill='tonext',
    fillcolor='rgba(31, 184, 205, 0.3)',  # Semi-transparent strong cyan
    line=dict(color='#1FB8CD', width=2),
    name='Automazione',
    cliponaxis=False
))

# Update layout
fig.update_layout(
    title='Livello di Automazione per Categoria',
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, max(automation_by_category['Automazione_Level']) * 1.1]
        )
    )
)

# Save the chart
fig.write_image('radar_automazione.png')
print("Chart saved as radar_automazione.png")