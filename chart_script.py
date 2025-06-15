import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the data
df = pd.read_csv("costi_sistema_domotico.csv")

# Group by category and sum costs
costs_by_category = df.groupby("Categoria")["Costo_Euro"].sum().reset_index()

# Sort by cost descending
costs_by_category = costs_by_category.sort_values("Costo_Euro", ascending=False)

# If more than 10 categories, group the smaller ones as "Other"
if len(costs_by_category) > 10:
    top_9 = costs_by_category.head(9)
    other_sum = costs_by_category.tail(len(costs_by_category) - 9)["Costo_Euro"].sum()
    other_row = pd.DataFrame({"Categoria": ["Altri"], "Costo_Euro": [other_sum]})
    costs_by_category = pd.concat([top_9, other_row], ignore_index=True)

# Define brand colors
colors = ['#1FB8CD', '#FFC185', '#ECEBD5', '#5D878F', '#D2BA4C', 
          '#B4413C', '#964325', '#944454', '#13343B', '#DB4545']

# Format costs with k abbreviation for display
costs_by_category['Cost_Display'] = costs_by_category['Costo_Euro'].apply(
    lambda x: f"{x/1000:.1f}k€" if x >= 1000 else f"{x:.0f}€"
)

# Create custom text for slices with both percentage and euro values
text_labels = []
total_cost = costs_by_category['Costo_Euro'].sum()
for i, row in costs_by_category.iterrows():
    percentage = (row['Costo_Euro'] / total_cost) * 100
    text_labels.append(f"{percentage:.1f}%<br>{row['Cost_Display']}")

# Create pie chart
fig = go.Figure(data=[go.Pie(
    labels=costs_by_category['Categoria'],
    values=costs_by_category['Costo_Euro'],
    text=text_labels,
    textinfo='text',
    textposition='inside',
    hovertemplate='<b>%{label}</b><br>' +
                  'Costo: %{customdata}<br>' +
                  'Percentuale: %{percent}<br>' +
                  '<extra></extra>',
    customdata=costs_by_category['Cost_Display'],
    marker=dict(colors=colors[:len(costs_by_category)])
)])

# Update layout with title under 40 characters
fig.update_layout(
    title="Investimento Sistema Domotico",
    uniformtext_minsize=14, 
    uniformtext_mode='hide'
)

# Save the chart
fig.write_image("sistema_domotico_costi.png")
print("Chart saved as sistema_domotico_costi.png")