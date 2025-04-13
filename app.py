from flask import Flask, render_template, request
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    fig_html = ""
    if request.method == 'POST':
        country = request.form['country']
        data = {'Country': [country], 'Value': [100]}
        fig = px.choropleth(
            data,
            locations='Country',
            locationmode='country names',
            color='Value',
            color_continuous_scale='Inferno',
            title=f'Country Map Highlighting {country}'
        )
        fig_html = pio.to_html(fig, full_html=False)

    return render_template('index.html', plot=fig_html)

if __name__ == '__main__':
    app.run(debug=True)
