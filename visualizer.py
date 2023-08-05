import plotly.graph_objects as go
from colour import Color
import random
random.seed = 253

def display_color_plate(colors):
    # Create an array of ones, which is the y-value for all bars
    y_values = [1]*len(colors)
    # Create a marker dictionary where each color corresponds to one bar
    marker_dict = {'color': colors}

    fig = go.Figure(
        data=[go.Bar(
            x=list(range(len(colors))),
            y=y_values,
            marker=marker_dict,
            width=1,  # Adjusts the width of the bars
            showlegend=False
        )]
    )

    fig.update_layout(
        yaxis={'visible': False, 'showticklabels': False},
        xaxis={'visible': False, 'showticklabels': False},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        autosize=False,
        width=600,
        height=50,
        margin=dict(l=0, r=0, b=0, t=0, pad=0),
        )
    
    fig.show()


def gradient(colors, n_sampled, shuffle_before_grad =False, start_with_original=True):
    orig_colors = colors.copy()
    if n_sampled <= len(colors):
        return colors[:n_sampled]
    
    if shuffle_before_grad:
        random.shuffle(colors)

    # Define the size of the gradients between the colors
    gradient_size = n_sampled // (len(colors) - 1)
    gradient_colors = []

    for i in range(len(colors) - 1):
        start_color = Color(colors[i])
        end_color = Color(colors[i + 1])
        range_colors = list(start_color.range_to(end_color, gradient_size+2))[:-1]  # exclude end color
        gradient_colors += range_colors

    # Add the final color to the list
    gradient_colors.append(Color(colors[-1]))

    # If we have less colors than n_sampled, add some more colors at the end
    while len(gradient_colors) < n_sampled:
        gradient_colors.append(gradient_colors[-1])
    gradient_colors = [color.hex for color in gradient_colors]
    if start_with_original:
        only_new_colors = [color for color in gradient_colors if not color in orig_colors]
        gradient_colors = orig_colors + only_new_colors
    return gradient_colors[:n_sampled]

