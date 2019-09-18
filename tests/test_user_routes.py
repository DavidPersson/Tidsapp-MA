import unittest
import json
import os
from timer import app


class TestCreateProject(unittest.TestCase):
    def setUp(self):
        from dotenv import load_dotenv
        load_dotenv()
        self.app = app.test_client()
        self.token = os.getenv("token")

    def test_user_status(self):
        """
        This checks the users status.
        Expected outcome is a return status of 200 and a message saying:
        `Data successfully gathered. Toggle status is active / inactive.
         You have worked for x hours today, and y hours this week.
         You're currently working on project z and part of the team xyz.`
        """
        # Python dictionary
        payload = {
            "token": self.token
        }
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POST request to the endpoint "/user_status/" with the payload of json_obj.
        rv = self.app.post('/user_status/', json=json_obj)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is what is expected.
        self.assertTrue(len(rv.data) > 0)

    def test_bad_token_user_status(self):
        """
        This tries to check a users status with a bad token.
        Expected outcome is a return status of 200 and an error message saying.
        `Error has occurred, The specified token is invalid`
        """
        # Python dictionary
        payload = {
            "token": self.token
        }
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POST request to the endpoint "/user_status/" with the payload of json_obj.
        rv = self.app.post('/user_status/', json=json_obj)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is what is expected.
        self.assertEqual(rv.data, "Error has occurred, The specified token is invalid")

    def test_user_track(self):
        """
        This toggles tracking the users time.
        Expected outcome is a return status of 200 and a message saying one of two things.
        `Success. Time tracking is now active.` or `Success. Time tracking is now inactive.`
        """
        # Python dictionary
        payload = {
            "token": self.token
        }
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POST request to the endpoint "/user_status/" with the payload of json_obj.
        rv = self.app.post('/user_track/', json=json_obj)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is what is expected.
        self.assertTrue(rv.data == ("Success. Time tracking is now active." or
                                    "Success. Time tracking is now inactive."))

    def test_bad_token_user_track(self):
        """
        This tries toggling tracking the users time with a bad token.
        Expected outcome is a return status of 200 and an error message saying.
        `Error has occurred, The specified token is invalid`
        """
        # Python dictionary
        payload = {
            "token": self.token
        }
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POST request to the endpoint "/user_status/" with the payload of json_obj.
        rv = self.app.post('/user_track/', json=json_obj)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is what is expected.
        self.assertEqual(rv.data, "Error has occurred, The specified token is invalid")

    def test_user_join_project(self):
        """
        This allows the user to join a project of their choosing.
        Expected outcome is a return status of 200 and a message saying:
        `Project successfully joined.`
        """
        # Python dictionary
        payload = {
            "token": self.token
        }
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POST request to the endpoint "/user_status/" with the payload of json_obj.
        rv = self.app.post('/user_join_project/', json=json_obj)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is what is expected.
        self.assertEqual(rv.data, "Project successfully joined.")

    def test_user_join__nonexistent_project(self):
        """
        This tries to join a nonexistent project
        Expected outcome is a return status of 200 and an error message saying:
        `Error has occured. The specified project does not exist`
        """
        # Python dictionary
        payload = {
            "token": self.token
        }
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POST request to the endpoint "/user_status/" with the payload of json_obj.
        rv = self.app.post('/user_join_project/', json=json_obj)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is what is expected.
        self.assertEqual(rv.data, "Error has occured. The specified project does not exist")

    def test_user_join_team(self):
        """
        This allows the user to join a team of their choosing.
        Expected outcome is a return status of 200 and a message saying:
        `Team successfully joined.`
        """
        # Python dictionary
        payload = {
            "token": self.token,
            "text": "test_team"
        }
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POST request to the endpoint "/user_status/" with the payload of json_obj.
        rv = self.app.post('/user_join_team/', json=json_obj)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is what is expected.
        self.assertEqual(rv.data, "Team successfully joined.")

    def test_user_join__nonexistent_team(self):
        """
        This tries to join a nonexistent team
        Expected outcome is a return status of 200 and an error message saying:
        `Error has occured. The specified team does not exist`
        """
        # Python dictionary
        payload = {
            "token": self.token,
            "text": "test_team0"
        }
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POST request to the endpoint "/user_status/" with the payload of json_obj.
        rv = self.app.post('/user_join_team/', json=json_obj)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is what is expected.
        self.assertEqual(rv.data, "Error has occured. The specified team does not exist")
