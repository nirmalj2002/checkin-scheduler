
# Code Check-in Scheduler Utility

Automate scheduled code check-ins to GitHub or Bitbucket using git commands and a CSV schedule file.


## Features
- Reads a CSV file (`checkin_schedule.csv`) with scheduled check-ins
- Processes jobs with date **less than or equal to today** and status `scheduled` or `failed` (including past-due jobs)
- Executes git commands: pull, add, commit, push for each job
- Updates job status in the CSV file to `successful` or `failed`
- Logs all actions and errors to `scheduler.log`, including job date and row index for traceability
- Modular codebase for maintainability
- Unit tests included


## How It Works
1. Each row in `checkin_schedule.csv` represents a check-in job.
2. On each run, the utility processes all jobs with date **less than or equal to today** and status `scheduled` or `failed`.
3. For each job, it runs git commands and updates the status to `successful` or `failed`.
4. Failed jobs can be retried automatically.
5. All log entries include the job's date and row index for easy tracking.

## Setup & Usage
1. Create a repository on GitHub or Bitbucket and note the remote URL.
2. Prepare your local workspace and add sample code files as listed in the schedule.
3. Ensure your workspace is a git repository and the remote is set.
4. Update `checkin_schedule.csv` with your schedule details:
   - Use `|` to separate multiple files in the `files` column.
   - Example row:
     ```
     2025-09-27,C:/AI-POCs/schedule-checkin-util-testrepo1,https://github.com/your-username/your-repo,src/test1.txt|src/test2.txt,added text 1 and text 2,scheduled
     ```
5. Run the utility:
   ```powershell
   python scheduler.py
   ```
6. Check results in your repository and logs in `scheduler.log`.

## Error Handling
- If files listed in the schedule do not exist, the job will fail and be logged.
- Failed jobs can be retried by keeping their status as `failed`.
- Only jobs with status `scheduled` or `failed` are processed.

## Project Structure
```
checkin-scheduler/
├── scheduler.py
├── csv_handler.py
├── git_executor.py
├── logger.py
├── config.py
├── checkin_schedule.csv
├── tests/
│   └── test_csv_handler.py
└── README.md
```

## Configuration
- All configuration items are in `config.py`.
- Schedule file name: `checkin_schedule.csv`
- Log file name: `scheduler.log`

## License
MIT
