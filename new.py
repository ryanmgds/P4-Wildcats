from flask import render_template
from restapi import restapi_bp
from models.lessons import menus
import requests



@restapi_bp.route('/covid19',  methods=['GET', 'POST'])
def covid19():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

    headers = {
        'x-rapidapi-key': "dec069b877msh0d9d0827664078cp1a18fajsn2afac35ae063",
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    world = response.json().get('world_total')
    countries = response.json().get('countries_stat')
    """
    print(world['total_cases'])
    for country in countries:
        print(country["country_name"])
    #return countries
    """
    return render_template("healthylunches.html", menus=menus, world=world,  countries=countries)

