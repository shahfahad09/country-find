import plotly.express as px
country = input("Enter your country name: ")
data = {
    'Country': [country],
    'Value': [100]
}
fig = px.choropleth(
    data,
    locations='Country',
    locationmode='country names',
    color='Value',
    color_continuous_scale='Inferno',
    title=f'Country Map Highlighting {country}'
)
fig.show()
