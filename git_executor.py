"""
Executes git commands for the scheduled check-in.
"""
import os
import subprocess

def execute_git_sequence(entry, logger):
    workspace = entry['local_workspace_folder']
    repo_url = entry['remote_repo_url']
    files = entry['files'].split('|')
    comments = entry['comments']
    try:
        logger.info(f"Running git commands in workspace: {workspace}")
        subprocess.run(['git', 'pull'], check=True, cwd=workspace)
        logger.info("Git pull successful")
        subprocess.run(['git', 'remote', 'set-url', 'origin', repo_url], check=True, cwd=workspace)
        logger.info(f"Set remote URL to {repo_url}")
        subprocess.run(['git', 'add'] + files, check=True, cwd=workspace)
        logger.info(f"Added files: {files}")
        subprocess.run(['git', 'commit', '-m', comments], check=True, cwd=workspace)
        logger.info(f"Committed with message: {comments}")
        subprocess.run(['git', 'push'], check=True, cwd=workspace)
        logger.info("Git push successful")
        return True
    except Exception as e:
        logger.error(f"Git operation failed: {e}")
        return False
