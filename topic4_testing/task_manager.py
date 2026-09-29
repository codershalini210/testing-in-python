def count_completed(tasks):
    """Return the number of completed tasks."""
    return sum(1 for task in tasks if task["status"] == "completed")


def find_task(tasks, task_id):
    """Return the task with the given ID, or None if it does not exist."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def update_status(tasks, task_id, new_status):
    """Update the status of a task and return True if successful."""
    task = find_task(tasks, task_id)

    if task is None:
        return False

    task["status"] = new_status
    return True