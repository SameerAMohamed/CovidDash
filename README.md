# CovidDash - a Dashboard based on COVID data
COVID Dashboard with Dash (a work in progress)

## Next to work on:

1)Manage errors

2)Pretty the dashboard up (narrower buttons, cleaner boundaries, etc.)

3)Incorporate into Django (and upload to website)

4)Add more metrics

5)Use a script to update data with most up-to-date CSV. Potentially use Beautiful Soup?

## To run simply run main.py and follow the link in the console to open in browser

## How it works
This dashboard uses Dash from Plotly along with Pandas to manage and transform data from a .csv into interactive graphics that visualize multiple different metrics on COVID from different countries. All missing/null data is replaced with a 0 value as this is more common in smaller countries.
Once the entire .csv is imported, the empty values are filled with 0, the desired columns are isolated, and an array of all the country names is made. Then the layout is made with 2 dropdown menus and a graph. These inputs from the buttons and outputs for the graph are then accounted in the app callback. Then, the function to manipulate the graph is defined which connects the input to the graph output for visualization.
