import copy
import threading

def Singleton(cls):
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance


class Job:
    def __init__(self, data, start_time, job_lock:threading.Lock) -> None:
        self.input = data
        self.org_input = copy.deepcopy(data)
        self.output = None
        self.is_process = False
        self.is_timeout = start_time
        self.lock = job_lock

    def destroy(self):
        del self.org_input
        self.lock.release()

