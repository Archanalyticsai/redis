from rq import Queue
from redis import Redis
from app import add

# Tell RQ what Redis connection to use
q = Queue('tasks', connection=Redis.from_url('redis://:<<password>>@1<<ip>>/<<db>>'))  # no args implies the default queue

# Delay execution of count_words_at_url('http://nvie.com')
job = q.enqueue(add.add, args=(3,4))
print(job.result)   # => None

# Now, wait a while, until the worker is finished
time.sleep(2)
print(job.result) 
