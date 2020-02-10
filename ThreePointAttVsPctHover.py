# Bokeh Libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, NumeralTickFormatter, HoverTool

# Import the data
from read_nba_data import three_takers

# Output to file
output_file('three_point_att_vs_pct.html',
            title='Three-Point Attempts vs. Percentage')

# Store the data in a ColumnDataSource
three_takers_cds = ColumnDataSource(three_takers)

# Specify the selection tools to be made available
select_tools = ['box_select','lasso_select','poly_select','tap','reset']

# Format the tooltip
tooltips = [
    ('Player','@name'),
    ('Three-Pointers Made','@play3PM'),
    ('Three-Pointers Attempted', '@play3PA'),
    ('Three-Point Percentage', '@pct3PM{00.0%}')  
]

# Create the figure
fig = figure(plot_height=400,
             plot_width=600,
             x_axis_label='Three-Point Shots Attempted',
             y_axis_label='Percentage Made',
             title='3PT Shots Attempted vs. Percentage Made (min. 100 3PA), 2017-18',
             toolbar_location='below',
             tools=select_tools)

# Format the y-axis tick label as percentage
fig.yaxis[0].formatter = NumeralTickFormatter(format='00.0%')

# Add square representing each player
fig.square(x='play3PA',
            y='pct3PM',
            source=three_takers_cds,
            color='royalblue',
            selection_color='deepskyblue',
            nonselection_color='lightgray',
            nonselection_alpha=0.3)

# Configure a renderer to be used upon hover
hover_glyph = fig.circle(x='play3PA',
                        y='pct3PM',
                        source=three_takers_cds,
                        size=15,
                        alpha=0,
                        hover_fill_color='black',
                        hover_alpha=0.5)

# Add the HoverTool 
fig.add_tools(HoverTool(tooltips=tooltips,renderers=[hover_glyph]))

show(fig)