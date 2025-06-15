import plotly.graph_objects as go
import plotly.io as pio

# Data from the provided JSON
categories = ["Mobile Responsiveness", "Velocità Sito", "SEO Optimization", "User Experience", 
              "Funzionalità Interactive", "Sistema Prenotazioni", "Integrazione Social", 
              "Analytics & Tracking", "Sicurezza", "Gestione Contenuti"]
current_scores = [1, 2, 1, 2, 0, 0, 1, 0, 1, 2]
proposed_scores = [10, 9, 9, 10, 9, 10, 8, 9, 10, 9]

# Better abbreviations to meet 15-character limit while maintaining readability
abbreviated_cats = ["Mobile Resp", "Velocità Sito", "SEO Optimiz", "User Experience", 
                   "Funz Interactive", "Sist Prenotaz", "Integraz Social", 
                   "Analytics Track", "Sicurezza", "Gest Contenuti"]

# Create radar chart
fig = go.Figure()

# Add current scores trace (red as requested)
fig.add_trace(go.Scatterpolar(
    r=current_scores,
    theta=abbreviated_cats,
    fill='toself',
    name='Attuale',
    line_color='red',
    fillcolor='rgba(255, 0, 0, 0.2)'
))

# Add proposed scores trace (green as requested)
fig.add_trace(go.Scatterpolar(
    r=proposed_scores,
    theta=abbreviated_cats,
    fill='toself',
    name='Proposto',
    line_color='green',
    fillcolor='rgba(0, 128, 0, 0.2)'
))

# Update layout
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 10]
        )),
    title="Confronto Funzionalità Tecniche",
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

# Save the chart
fig.write_image("radar_chart_restaurant.png")