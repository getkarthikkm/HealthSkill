import logging
import sys
import unittest
from unittest import TestCase
import csv
import json
import requests

base_url = 'http://127.0.0.1:5000/skill/health'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')


class TestSkillAssessment(TestCase):

    def test_skill_assessment(self):
        """
        Test case for testing the customer skill assessment.
        :return:
        """
        # Open CSV file to write the skill assessment
        csv_w_file = open('health_skills.csv', 'w')
        write_fieldnames = ['id', 'skill']
        writer = csv.DictWriter(csv_w_file, fieldnames=write_fieldnames)
        writer.writeheader()

        # Read input from the test csv file
        csv_r_file = open('health_customers.csv', 'r')
        read_fieldnames = ("id", "postcode", "age", "gender", "has_provider", "has_children",
                           "marital_status", "cover_type")
        reader = csv.DictReader(csv_r_file, read_fieldnames)

        skip_header = True
        for row in reader:
            if skip_header:
                skip_header = False
                continue

            logging.debug("read CSV row : {}".format(row))
            json_input = {
                "customer": {
                    "name": row['id'],
                    "postcode": row['postcode'],
                    "age": row['age'],
                    "gender": row['gender'],
                    "has_provider": row['has_provider'],
                    "has_children": row['has_children'],
                    "marital_status": row['marital_status'],
                    "cover_type": row['cover_type']
            }}

            # Dict to Json
            r = json.dumps(json_input)
            loaded_r = json.loads(r)

            # Invoke POST REST API request with json input
            response = requests.post(base_url, data=json.dumps(loaded_r))
            response_data = response.json()
            logging.debug("get JSON response : {}".format(response_data))

            # Write to result file
            writer.writerow({'id': row['id'], 'skill': response_data['skill']})


if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(stream=sys.stdout, verbosity=1), exit=False)
