import plotly.graph_objects as go
import json

# Data from JSON
data = {
    "metrics": ["Tempo caricamento", "Tasso conversione", "Prenotazioni online", "Traffico organico", "Engagement rate", "Mobile users", "Tempo permanenza", "Bounce rate", "Lead generation", "Social shares"],
    "improvements": [-75, 250, 500, 400, 300, 200, 180, -60, 400, 600],
    "current_values": ["8 sec", "2%", "0/mese", "100/mese", "15%", "30%", "45 sec", "80%", "5/mese", "2/mese"],
    "target_values": ["2 sec", "7%", "30/mese", "500/mese", "60%", "90%", "2 min", "32%", "25/mese", "14/mese"]
}

# Abbreviate metric names to fit 15 character limit
abbreviated_metrics = [
    "Tempo caric.", "Tasso conv.", "Prenotazioni", "Traffico org.", "Engagement", 
    "Mobile users", "Tempo perm.", "Bounce rate", "Lead gen.", "Social shares"
]

# Create colors: strong green for positive improvements, red for negative improvements
colors = []
for improvement in data["improvements"]:
    if improvement < 0:
        colors.append("#B4413C")  # Red for negative improvements (good for business)
    else:
        colors.append("#1FB8CD")  # Strong cyan/green for positive improvements

# Create simplified text labels with percentage and compact absolute values
text_labels = []
for i, improvement in enumerate(data["improvements"]):
    current = data["current_values"][i]
    target = data["target_values"][i]
    # Simplify the format to be more readable
    text_labels.append(f"{improvement}%<br>({current}→{target})")

# Create hover text with detailed information
hover_text = []
for i, metric in enumerate(data["metrics"]):
    hover_text.append(f"{metric}<br>Da: {data['current_values'][i]}<br>A: {data['target_values'][i]}<br>Miglioramento: {data['improvements'][i]}%")

# Create the bar chart
fig = go.Figure()

fig.add_trace(go.Bar(
    x=abbreviated_metrics,
    y=data["improvements"],
    marker_color=colors,
    text=text_labels,
    textposition='auto',
    textfont=dict(size=10),
    hovertemplate='%{hovertext}<extra></extra>',
    hovertext=hover_text,
    cliponaxis=False
))

# Update layout
fig.update_layout(
    title="Metriche Performance Post-Refactoring",
    xaxis_title="Metriche",
    yaxis_title="Miglioramento %",
    showlegend=False
)

# Update axes
fig.update_xaxes(tickangle=45)
fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='gray')

# Save the chart
fig.write_image("performance_metrics_chart.png")