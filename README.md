# color-plate-visualizer
Easy visualization of color plates using Plotly. Create, customize, and visualize color palettes with seamless gradients.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Modules and Functions](#modules-and-functions)
  - [display_color_plate](#display_color_plate)
  - [gradient](#gradient)
- [Usage Examples](#usage-examples)
- [License](#license)

## Introduction
"color-plate-visualizer" is a Python library designed for the easy visualization and creation of color palettes. It provides functionalities to display color palettes and create gradients between colors. The repository is built on [Plotly](https://github.com/plotly/plotly.py), a popular open-source graphing library, and offers a user-friendly way to work with color schemes in design, art, or any creative application. Special thanks to the [Plotly project](https://github.com/plotly/plotly.py) for providing the underlying visualization capabilities.

## Installation
You can install the "color-plate-visualizer" by cloning the repository or downloading the source code.

### Dependencies
- Plotly
- colour

### Installation Steps
1. Clone the repository or download the ZIP file.
2. Navigate to the directory and install the required dependencies.
   ```bash
   pip install plotly colour
   ```

## Modules and Functions

### `display_color_plate`
Displays a horizontal bar plot representing the given colors.

#### Parameters
- `colors`: A list of color codes in hexadecimal format.

#### Example
```python
from visualizer import display_color_plate
colors = ['#FF0000', '#00FF00', '#0000FF']
display_color_plate(colors)
```

### `gradient`
Generates a gradient between the given colors.

#### Parameters
- `colors`: The original list of color codes.
- `n_sampled`: The desired number of colors in the final gradient list.
- `shuffle_before_grad`: (Optional) Shuffle the original colors before creating the gradient. Default is `False`.
- `start_with_original`: (Optional) Include the original colors at the beginning of the final gradient list. Default is `True`.

#### Example
```python
from visualizer import gradient
colors = ['#FF0000', '#00FF00', '#0000FF']
gradient_colors = gradient(colors, n_sampled=9)
```

## Usage Examples
You can find comprehensive examples in the [example.py](./example.py) file, demonstrating how to visualize color palettes and create custom gradients.

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.