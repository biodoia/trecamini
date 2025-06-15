import plotly.graph_objects as go
import plotly.io as pio

# Define node positions and types
nodes = {
    # Entry points (circles)
    'Google': {'x': 0, 'y': 3, 'type': 'circle', 'label': 'Google'},
    'Social': {'x': 0, 'y': 2, 'type': 'circle', 'label': 'Social Media'},
    'Word': {'x': 0, 'y': 1, 'type': 'circle', 'label': 'Passaparola'},
    
    # Homepage (rectangle)
    'Homepage': {'x': 2, 'y': 2, 'type': 'rectangle', 'label': 'Homepage'},
    
    # Decision point (diamond)
    'Decision': {'x': 4, 'y': 2, 'type': 'diamond', 'label': 'Navigazione'},
    
    # Path A - Info
    'Info': {'x': 6, 'y': 3.5, 'type': 'rectangle', 'label': 'Info'},
    'ChiSiamo': {'x': 8, 'y': 3.5, 'type': 'rectangle', 'label': 'Chi Siamo'},
    'Location': {'x': 10, 'y': 3.5, 'type': 'rectangle', 'label': 'Location'},
    
    # Path B - Menu
    'Menu': {'x': 6, 'y': 2, 'type': 'rectangle', 'label': 'Menu'},
    'Piatti': {'x': 8, 'y': 2, 'type': 'rectangle', 'label': 'Piatti'},
    
    # Path C - Events
    'Eventi': {'x': 6, 'y': 0.5, 'type': 'rectangle', 'label': 'Eventi'},
    'Matrimoni': {'x': 8, 'y': 0.5, 'type': 'rectangle', 'label': 'Matrimoni'},
    
    # Conversion points
    'Prenotazione': {'x': 12, 'y': 2.75, 'type': 'circle', 'label': 'Prenotazione'},
    'Preventivo': {'x': 12, 'y': 0.5, 'type': 'circle', 'label': 'Preventivo'},
    
    # Post-conversion
    'PostConv': {'x': 14, 'y': 1.6, 'type': 'circle', 'label': 'Post-Conv'}
}

# Define connections with colors
connections = [
    # Entry to homepage
    ('Google', 'Homepage', '#1FB8CD'),
    ('Social', 'Homepage', '#1FB8CD'),
    ('Word', 'Homepage', '#1FB8CD'),
    
    # Homepage to decision
    ('Homepage', 'Decision', '#FFC185'),
    
    # Path A - Info
    ('Decision', 'Info', '#ECEBD5'),
    ('Info', 'ChiSiamo', '#ECEBD5'),
    ('ChiSiamo', 'Location', '#ECEBD5'),
    ('Location', 'Prenotazione', '#ECEBD5'),
    
    # Path B - Menu
    ('Decision', 'Menu', '#5D878F'),
    ('Menu', 'Piatti', '#5D878F'),
    ('Piatti', 'Prenotazione', '#5D878F'),
    
    # Path C - Events
    ('Decision', 'Eventi', '#D2BA4C'),
    ('Eventi', 'Matrimoni', '#D2BA4C'),
    ('Matrimoni', 'Preventivo', '#D2BA4C'),
    
    # Post-conversion
    ('Prenotazione', 'PostConv', '#B4413C'),
    ('Preventivo', 'PostConv', '#B4413C')
]

# Create figure
fig = go.Figure()

# Add connections (lines)
for start, end, color in connections:
    fig.add_trace(go.Scatter(
        x=[nodes[start]['x'], nodes[end]['x']],
        y=[nodes[start]['y'], nodes[end]['y']],
        mode='lines',
        line=dict(color=color, width=3),
        showlegend=False,
        hoverinfo='skip'
    ))

# Add nodes with different shapes
for node_id, node_data in nodes.items():
    symbol = 'circle' if node_data['type'] == 'circle' else 'square' if node_data['type'] == 'rectangle' else 'diamond'
    color = '#1FB8CD' if node_data['type'] == 'circle' else '#FFC185' if node_data['type'] == 'rectangle' else '#ECEBD5'
    
    fig.add_trace(go.Scatter(
        x=[node_data['x']],
        y=[node_data['y']],
        mode='markers+text',
        marker=dict(
            symbol=symbol,
            size=20,
            color=color,
            line=dict(width=2, color='white')
        ),
        text=node_data['label'],
        textposition='middle center',
        textfont=dict(size=10, color='black'),
        showlegend=False,
        hoverinfo='text',
        hovertext=f"{node_data['label']}<br>Tipo: {node_data['type']}"
    ))

# Update layout
fig.update_layout(
    title="User Journey Antico Casale",
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    plot_bgcolor='white',
    showlegend=False
)

# Save the chart
fig.write_image("user_journey_flow.png")