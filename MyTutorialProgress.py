import numpy as np 

from bokeh.io import output_file
from bokeh.plotting import figure, show

# My word count data
day_num = np.linspace(1,10,10)
daily_words = [450,628,488,210,287,791,508,639,397,943]

cumulative_words = np.cumsum(daily_words)

# Output the visualization to a static HTML page
output_file('my_tutorial_progress.html',title='My Tutorial Progress')

# Create a figure with a datetime type x-axis
fig = figure(title='My Tutorial Progress',
            plot_height=400,plot_width=700,
            x_axis_label='Day Number',y_axis_label='Words Written',
            x_minor_ticks=2,y_range=(0,6000),
            toolbar_location=None)

# The daily words will be represented as Vertial bars
fig.vbar(x=day_num,bottom=0,top=daily_words,
        color='blue',width=0.75,
        legend='Daily')

# The cumulative sum will be a trend line
fig.line(x=day_num,y=cumulative_words,
        color='gray',line_width=1,
        legend='Cumulative')

fig.legend.location = 'top_left'

show(fig)