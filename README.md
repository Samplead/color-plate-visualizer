# color-plate-visualizer
Easy visualization of color plates using Plotly. Create, customize, and visualize color palettes with seamless gradients.

## Table of Contents
- [Introduction](#introduction)
- [Quickstart](#Quickstart)
  - [display_color_plate](#display_color_plate)
  - [gradient](#gradient)
- [Installation](#installation)
- [Usage Examples](#usage-examples)
- [License](#license)

## Introduction
"color-plate-visualizer" is a Python library designed for the easy visualization and creation of color palettes. It provides functionalities to display color palettes and create gradients between colors. The repository is built on [Plotly](https://github.com/plotly/plotly.py), a popular open-source graphing library, and offers a user-friendly way to work with color schemes in design, art, or any creative application. Special thanks to the [Plotly project](https://github.com/plotly/plotly.py) for providing the underlying visualization capabilities.

## Quickstart
### `display_color_plate`
Displays a horizontal bar plot representing the given colors.

#### Parameters
- `colors`: A list of color codes in hexadecimal format.

#### Example
```python
from visualizer import display_color_plate
colors = ['#19D3F3', '#FF6692', '#7D5DEF', '#FF97FF', '#FFA500']
display_color_plate(colors)
```
![Original Color Palette](original.png)


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
colors = ['#19D3F3', '#FF6692', '#7D5DEF', '#FF97FF', '#FFA500']
gradient_colors = gradient(colors, n_sampled=9)
```
![Gradient Colors](gradient.png)

## Installation
You can install the "color-plate-visualizer" by cloning the repository or downloading the source code.
1. Clone the repository or download the ZIP file.
2. Navigate to the directory and install the required dependencies.
   ```bash
   pip install plotly colour
   ```

## Usage Examples
You can find comprehensive examples in the [example.py](./example.py) file, demonstrating how to visualize color palettes and create custom gradients.

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Credits
Built with love by [Yotam Nahum](https://github.com/yotamnahum), utilizing the [Plotly project](https://github.com/plotly/plotly.py) for visualization. Special thanks to the Plotly team for their outstanding work.