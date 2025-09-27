def main():
    from datetime import datetime
    from config import SCHEDULE_DATA_FILE
    from logger import setup_logger
    from git_executor import execute_git_sequence
    from csv_handler import read_schedule, update_status
    logger = setup_logger()
    today = datetime.today().strftime('%Y-%m-%d')
    schedule = read_schedule(SCHEDULE_DATA_FILE)
    job_id = 1
    jobs_found = False
    from datetime import datetime
    for idx, entry in enumerate(schedule):
        entry_date = entry['date']
        try:
            entry_dt = datetime.strptime(entry_date, '%Y-%m-%d')
            today_dt = datetime.strptime(today, '%Y-%m-%d')
        except Exception as e:
            logger.error(f"[Row {idx+1}] Invalid date format: {entry_date}. Skipping.")
            continue
        if entry_dt <= today_dt and entry['status'].lower() in ['scheduled', 'failed']:
            jobs_found = True
            logger.info(f"[Job {job_id} | Row {idx+1} | Date {entry_date}] Processing check-in for workspace: {entry['local_workspace_folder']}")
            success = execute_git_sequence(entry, logger)
            new_status = 'successful' if success else 'failed'
            update_status(SCHEDULE_DATA_FILE, entry, new_status)
            logger.info(f"[Job {job_id} | Row {idx+1} | Date {entry_date}] Check-in status updated to: {new_status}")
            job_id += 1
    if not jobs_found:
        logger.info(f"No scheduled or failed jobs found for date {today}. Nothing to process.")

if __name__ == "__main__":
    main()
