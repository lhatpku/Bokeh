from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.models.widgets import Tabs,Panel

# Import the data
from read_nba_data import *

# Output to static HTML file
output_file('east__west_top_2_tabbed_layout.html',
            title='Conference Top 2 Teams Wins Race')

# Create a ColumnDataSource
standings_cds = ColumnDataSource(standings)

# Create view for each team
celtics_view = CDSView(source=standings_cds,
                        filters=[GroupFilter(column_name='teamAbbr', group='BOS')])

raptors_view = CDSView(source=standings_cds,
                        filters=[GroupFilter(column_name='teamAbbr', group='TOR')])

rockets_view = CDSView(source=standings_cds,
                        filters=[GroupFilter(column_name='teamAbbr', group='HOU')])

warriors_view = CDSView(source=standings_cds,
                        filters=[GroupFilter(column_name='teamAbbr', group='GS')])

# Create and configure the figure
east_fig = figure(x_axis_type='datetime',
             plot_height=300,
             x_axis_label='Date', 
             y_axis_label='Wins',
             toolbar_location=None)

west_fig = figure(x_axis_type='datetime',
             plot_height=300,
             x_axis_label='Date', 
             y_axis_label='Wins',
             toolbar_location=None)

# Reduce the width of both figures
east_fig.plot_width = west_fig.plot_width = 800

# Render the race as step lines
east_fig.step('stDate', 'gameWon', 
         color='#007A33', legend='Celtics', 
         source=standings_cds, view=celtics_view)
east_fig.step('stDate', 'gameWon', 
         color='#CE1141', legend='Raptors', 
         source=standings_cds, view=raptors_view)

west_fig.step('stDate', 'gameWon', 
         color='#CE1141', legend='Rockets', 
         source=standings_cds, view=rockets_view)
west_fig.step('stDate', 'gameWon', 
         color='#006BB6', legend='Warriors', 
         source=standings_cds, view=warriors_view)

# Move the legend to the upper left corner
east_fig.legend.location = 'top_left'
west_fig.legend.location = 'top_left'

# Create two panels, one for each conference
east_panel = Panel(child=east_fig,title='Eastern Conference')
west_panel = Panel(child=west_fig,title='Western Conference')

# Assign the panels to Tabs
tabs = Tabs(tabs=[west_panel,east_panel])

# Show the plot
show(tabs) 