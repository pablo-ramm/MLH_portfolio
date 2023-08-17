import unittest
import os
os.environ['TESTING'] = 'true'

from app import app
import requests

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        expected_title = 'name'
        assert f'<title>{expected_title}</title>' in html
        # TODO: Add more tests relating to the home page
        assert "<h1 class=\"pt-0\">Pablo Ram</h1>" in html
        assert "<a class=\"nav-item nav-link text-light\" href=\"/hobbies\">Hobbies</a>" in html
        assert "©Portfolio" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_post" in json
        assert len(json["timeline_post"]) == 0

        # TODOo: Add more tests relating to the /api/timeline_post GET and POST apis
        # Test POST method
        response2 = self.client.post("/api/timeline_post", data={
            'name': 'John Doe', 
            'email': 'john@example.com', 
            'content': 'Hello world, I\'m John!'
        })
        assert response2.status_code == 200
        assert response2.is_json
        json = response2.get_json()
        assert json['name'] == 'John Doe'
        assert json['email'] == 'john@example.com'
        assert json['content'] == 'Hello world, I\'m John!'

        # Test GET method
        response3 = self.client.get("/api/timeline_post")
        assert response3.status_code == 200
        assert response3.is_json
        json = response3.get_json()
        assert "timeline_post" in json
        assert len(json["timeline_post"]) == 1
        assert json['timeline_post'][0]['name'] == 'John Doe'
        assert json['timeline_post'][0]['email'] == 'john@example.com'
        assert json['timeline_post'][0]['content'] == 'Hello world, I\'m John!'

        

        

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html