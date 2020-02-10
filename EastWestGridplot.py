from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.layouts import gridplot

# Import the data
from read_nba_data import *

# Output to static HTML file
output_file('east__west_top_2_gridplot.html',
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
east_fig.plot_width = west_fig.plot_width = 300

# Edit the titles
east_fig.title.text = 'Eastern Conference'
west_fig.title.text = 'Western Conference'

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

# east_west_gridplot = gridplot([[west_fig,east_fig]],toolbar_location='right')
east_west_gridplot = gridplot([[west_fig,None],[None,east_fig]],toolbar_location='right')


# Show the plot
show(east_west_gridplot) 