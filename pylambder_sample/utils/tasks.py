from pylambder_sample.pylambder import app

@app.task
def task1(arg1):
    return arg1 * 2

@app.task
def task2():
    return 444