import webbrowser

import pandas as pd
import plotly
import plotly.express as px
import json
import folium


def run():
    df = pd.read_csv("gunData.csv")
    abbrv_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS",
              "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC",
              "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    by_state = df.groupby('state')['longitude'].count().reset_index()
    by_state.rename(columns={'longitude': 'Location Count'}, inplace=True)
    for i in by_state.index:
        by_state.at[i,'state'] = abbrv_states[i]
    fig = px.choropleth(by_state, locations='state',
                        color='Location Count',
                        locationmode="USA-states", scope="usa", color_continuous_scale='Viridis',
                        labels={'color': 'Location Count'}, title='Gun Violence by State')
    fig.write_html('Gun Violence by State.html')
    webbrowser.open("Gun Violence by State.html")




if __name__ == "__main__":
    run()
