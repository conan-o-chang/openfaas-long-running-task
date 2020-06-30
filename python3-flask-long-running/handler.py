import time

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    sleep_time = int(req)
    time.sleep(sleep_time)
    return f'sleep job done for {req} s'
