import unittest
import os
from csv_handler import read_schedule, update_status

class TestCSVHandler(unittest.TestCase):
    TEST_CSV = 'test_schedule.csv'

    def setUp(self):
        with open(self.TEST_CSV, 'w', encoding='utf-8') as f:
            f.write('date,local_workspace_folder,remote_repo_url,files,comments,status\n')
            f.write('2025-09-27,C:/AI-POCs/sample-workspace,https://github.com/example/sample-repo.git,src/main.py|src/utils.py,Initial commit,scheduled\n')

    def tearDown(self):
        os.remove(self.TEST_CSV)

    def test_read_schedule(self):
        schedule = read_schedule(self.TEST_CSV)
        self.assertEqual(len(schedule), 1)
        self.assertEqual(schedule[0]['status'], 'scheduled')

    def test_update_status(self):
        schedule = read_schedule(self.TEST_CSV)
        entry = schedule[0]
        update_status(self.TEST_CSV, entry, 'successful')
        updated = read_schedule(self.TEST_CSV)
        self.assertEqual(updated[0]['status'], 'successful')

if __name__ == '__main__':
    unittest.main()
