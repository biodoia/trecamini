import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# Define the tree structure with positions and icons
nodes = {
    # Root node
    'Homepage': {'x': 0, 'y': 7, 'level': 0, 'parent': None, 'icon': '🏠'},
    
    # Main sections (level 1) - spread wider
    'Chi Siamo': {'x': -4.5, 'y': 5, 'level': 1, 'parent': 'Homepage', 'icon': '👥'},
    'Menu': {'x': -3, 'y': 5, 'level': 1, 'parent': 'Homepage', 'icon': '🍽️'},
    'Location Sale': {'x': -1.5, 'y': 5, 'level': 1, 'parent': 'Homepage', 'icon': '🏛️'},
    'Eventi': {'x': 0, 'y': 5, 'level': 1, 'parent': 'Homepage', 'icon': '🎉'},
    'Prenotazioni': {'x': 1.5, 'y': 5, 'level': 1, 'parent': 'Homepage', 'icon': '📅'},
    'Contatti': {'x': 3, 'y': 5, 'level': 1, 'parent': 'Homepage', 'icon': '📞'},
    'Blog News': {'x': 4.5, 'y': 5, 'level': 1, 'parent': 'Homepage', 'icon': '📰'},
    
    # Chi Siamo subsections
    'Storia Casale': {'x': -5.5, 'y': 3, 'level': 2, 'parent': 'Chi Siamo', 'icon': '📚'},
    'Team Chef': {'x': -4.5, 'y': 3, 'level': 2, 'parent': 'Chi Siamo', 'icon': '👨‍🍳'},
    'Filosofia': {'x': -3.5, 'y': 3, 'level': 2, 'parent': 'Chi Siamo', 'icon': '💭'},
    
    # Menu subsections
    'Antipasti': {'x': -3.8, 'y': 3, 'level': 2, 'parent': 'Menu', 'icon': '🥗'},
    'Primi': {'x': -3, 'y': 3, 'level': 2, 'parent': 'Menu', 'icon': '🍝'},
    'Secondi': {'x': -2.2, 'y': 3, 'level': 2, 'parent': 'Menu', 'icon': '🥩'},
    'Dolci': {'x': -3.4, 'y': 2, 'level': 2, 'parent': 'Menu', 'icon': '🍰'},
    'Carta Vini': {'x': -2.6, 'y': 2, 'level': 2, 'parent': 'Menu', 'icon': '🍷'},
    
    # Location & Sale subsections
    'Sale Ricevi': {'x': -2.2, 'y': 3, 'level': 2, 'parent': 'Location Sale', 'icon': '🏰'},
    'Giardino': {'x': -1.5, 'y': 3, 'level': 2, 'parent': 'Location Sale', 'icon': '🌿'},
    'Cantina': {'x': -0.8, 'y': 3, 'level': 2, 'parent': 'Location Sale', 'icon': '🍾'},
    'Virtual Tour': {'x': -1.5, 'y': 2, 'level': 2, 'parent': 'Location Sale', 'icon': '🎥'},
    
    # Eventi subsections
    'Matrimoni': {'x': -0.8, 'y': 3, 'level': 2, 'parent': 'Eventi', 'icon': '💒'},
    'Eventi Aziend': {'x': 0, 'y': 3, 'level': 2, 'parent': 'Eventi', 'icon': '🏢'},
    'Cene Tema': {'x': 0.8, 'y': 3, 'level': 2, 'parent': 'Eventi', 'icon': '🎭'},
    'Wedding Plan': {'x': 0, 'y': 2, 'level': 2, 'parent': 'Eventi', 'icon': '💍'},
    
    # Prenotazioni subsections
    'Prenota Online': {'x': 0.8, 'y': 3, 'level': 2, 'parent': 'Prenotazioni', 'icon': '💻'},
    'Orari': {'x': 1.5, 'y': 3, 'level': 2, 'parent': 'Prenotazioni', 'icon': '⏰'},
    'Politiche': {'x': 2.2, 'y': 3, 'level': 2, 'parent': 'Prenotazioni', 'icon': '📋'},
    
    # Contatti subsections
    'Dove Siamo': {'x': 2.2, 'y': 3, 'level': 2, 'parent': 'Contatti', 'icon': '📍'},
    'Come Arrivare': {'x': 3, 'y': 3, 'level': 2, 'parent': 'Contatti', 'icon': '🚗'},
    'Contatti Dir': {'x': 3.8, 'y': 3, 'level': 2, 'parent': 'Contatti', 'icon': '📧'},
    
    # Blog & News subsections
    'Ricette Chef': {'x': 3.8, 'y': 3, 'level': 2, 'parent': 'Blog News', 'icon': '👨‍🍳'},
    'Eventi Pass': {'x': 4.5, 'y': 3, 'level': 2, 'parent': 'Blog News', 'icon': '📸'},
    'Novita': {'x': 5.2, 'y': 3, 'level': 2, 'parent': 'Blog News', 'icon': '🆕'}
}

# Create the figure
fig = go.Figure()

# Add connecting lines
for node_name, node_data in nodes.items():
    parent = node_data['parent']
    if parent:
        parent_data = nodes[parent]
        fig.add_trace(go.Scatter(
            x=[parent_data['x'], node_data['x']],
            y=[parent_data['y'], node_data['y']],
            mode='lines',
            line=dict(color='#5D878F', width=2),
            showlegend=False,
            hoverinfo='skip'
        ))

# Define colors for different levels
colors = ['#1FB8CD', '#FFC185', '#ECEBD5']

# Add nodes by level
for level in [0, 1, 2]:
    level_nodes = {k: v for k, v in nodes.items() if v['level'] == level}
    
    for node_name, node_data in level_nodes.items():
        # Set sizes and colors based on level
        if level == 0:
            size = 35
            color = colors[0]
            font_size = 12
        elif level == 1:
            size = 25
            color = colors[1]
            font_size = 10
        else:
            size = 18
            color = colors[2]
            font_size = 9
        
        # Add the node
        fig.add_trace(go.Scatter(
            x=[node_data['x']],
            y=[node_data['y']],
            mode='markers',
            marker=dict(size=size, color=color, line=dict(width=2, color='white')),
            showlegend=False,
            hovertemplate=f'<b>{node_name}</b><extra></extra>',
            cliponaxis=False
        ))
        
        # Add icon above the node
        fig.add_trace(go.Scatter(
            x=[node_data['x']],
            y=[node_data['y'] + 0.15],
            mode='text',
            text=[node_data['icon']],
            textfont=dict(size=font_size+2),
            showlegend=False,
            hoverinfo='skip',
            cliponaxis=False
        ))
        
        # Add text below the node
        fig.add_trace(go.Scatter(
            x=[node_data['x']],
            y=[node_data['y'] - 0.25],
            mode='text',
            text=[node_name],
            textfont=dict(size=font_size, color='black'),
            showlegend=False,
            hoverinfo='skip',
            cliponaxis=False
        ))

# Update layout
fig.update_layout(
    title='Architettura Sito Web - Antico Casale Tre Camini',
    showlegend=False,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        showgrid=False,
        showticklabels=False,
        zeroline=False,
        range=[-6.2, 6]
    ),
    yaxis=dict(
        showgrid=False,
        showticklabels=False,
        zeroline=False,
        range=[1.2, 7.8]
    )
)

# Save the chart
fig.write_image('restaurant_sitemap.png')