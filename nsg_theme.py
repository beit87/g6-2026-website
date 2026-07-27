import altair as alt

# Vaporwave color palette
background: str = "#2e2157"  # dark blue-grey
gridColor: str = "#043f6b"  # lighter blue-grey
textColor: str = "#d3d3d3"  # light grey
markColor: str = "#fe53bb"  # default color (pink)
defaultFont: str = 'IBM Plex Sans,system-ui,-apple-system,BlinkMacSystemFont,".sfnstext-regular",sans-serif'
condensedFont: str = 'IBM Plex Sans Condensed, system-ui, -apple-system, BlinkMacSystemFont, ".SFNSText-Regular", sans-serif'
fontWeight = 400

# Vaporwave palette
line_colors = [
    "#2de2e6",  # teal/cyan
    "#fe53bb",  # pink
    "#f5d300",  # yellow
    "#00ff41",  # matrix green
    "#ff6c11",  # hot orange
    "#fd1d53"  # hot red
]


@alt.theme.register('altair_vaporwave_theme', enable=True)
def altair_vaporwave_theme() -> alt.theme.ThemeConfig:
    return {
        'config': {
            'view': {
                'continuousWidth': 400,
                'continuousHeight': 300,
                'stroke':gridColor,
                'strokeWidth': 1,
            },
            'background': background,
            'mark': {'color': markColor},
            'arc': {'fill': markColor},
            'area': {
                'fill': markColor,
                'line': True,
                'fillOpacity': 0.1
            },
            'line': {
                'stroke': markColor,
                'strokeWidth': 2
            },
            'path': {'stroke': markColor},
            'rect': {'fill': markColor},
            'shape': {'stroke': markColor},
            'symbol': {'fill': markColor},

            'title': {
                'color': textColor,
                'anchor': 'start',
                'dy': -15,
                'fontSize': 16,
                'font': defaultFont,
                'fontWeight': 600,
            },

            'axisBand': {
                'grid': False,
            },
            'axis': {
                # Axis labels
                'labelColor': textColor,
                'labelFontSize': 12,
                'labelFont': condensedFont,
                'labelFontWeight': fontWeight,
                # Axis titles
                'titleColor': textColor,
                'titleFontWeight': 600,
                'titleFontSize': 12,

                # MISC
                'grid': True,
                'gridColor': gridColor,
                'labelAngle': 0,
                'domainColor': None,
                'tickColor': None,
                'labelPadding': 2,
                'tickSize': 5,
                'tickWidth': 0.5,
                # Make grid appear above marks (important for lines under grid)
                'gridOpacity': 1,
                'gridZ': 1
            },

            'axisX': {
                'gridDash': [6, 3],
                'gridWidth': 0.25,
                'gridColor': gridColor,
            },

            'axisY': {
                'gridDash': [6, 3],
                'gridWidth': 0.25,
                'gridColor': gridColor,
            },

            # This controls the layer order
            'layer': {
                'grid': 1,  # Higher z-index for grid (on top)
                'mark': 0  # Lower z-index for marks (below)
            },

            'legend': {
                'labelFontSize': 11,
                'padding': 1,
                'symbolType': 'square',
                'labelColor': textColor,
                'titleColor': textColor
            },
            'style': {
                'guide-label': {
                    'font': defaultFont,
                    'fill': textColor,
                    'fontWeight': fontWeight,
                },
                'guide-title': {
                    'font': defaultFont,
                    'fill': textColor,
                    'fontWeight': fontWeight,
                },
            },
            'range': {
                'category': line_colors,
            },
        }
    }