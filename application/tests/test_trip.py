import json


def test_signup_pessenger(client):
    pessenger_data = {
        'name': "Saifullah Khan",
        'email': "saifkhan912@gmail.com"
    }
    response = client.post("/pessenger/register", data=pessenger_data)
    response_json = parse_response(response)
    assert response_json['email'] == "saifkhan912@gmail.com"

def test_signup_driver(client):
    driver_data = {
        'name': "Amaan Khan - Driver",
        'email': "amankhan@gmail.com"
    }
    response = client.post("/driver/register", data=driver_data)
    response_json = parse_response(response)
    assert response_json['email'] == "amankhan@gmail.com"
    
def test_get_pessenger_trips(client):
    response = client.get("/pessenger/trips")
    response_json = parse_response(response)
    assert 'trips' in response_json


def parse_response(response):
    data = json.loads(response.get_data(as_text=True))
    # print('data:', data)
    return data
