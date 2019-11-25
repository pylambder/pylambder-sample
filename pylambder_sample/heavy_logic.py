import pylambder_sample.utils.tasks as tasks

def get_id_done():
    print("Scheduling")
    task = tasks.task1.delay(123)
    return task.get_result()