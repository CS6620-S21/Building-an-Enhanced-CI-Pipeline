# Advanced Python Scheduler

Advanced Python Scheduler (APScheduler) is a Python library to schedule Python code to be executed later, either just once or periodically.

Document: 
https://apscheduler.readthedocs.io/en/stable/userguide.html

In our continous testing system, we can write serveral testing.py files and manage them using APScheduler.

```Python
from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

if __name__ == '__main__':
    scheduler = BlockingScheduler()

    scheduler.add_job(subprocess.run,
                      'cron',
                      hour=4,
                      args=([
                          "locust", "-f", "locustfile.py", "--host",
                          "http://34.102.157.148", "--users", "300",
                          "--spawn-rate", "2", "--run-time", "30s",
                          "--headless"
                      ], ))

    scheduler.start()
```
1. We only run the scheduler program in our process. So We choose to use BlockingScheduler. It will block the process till the scheduler program finish.
2. Since we need to run different files, we introduce subprocess. And we can run the files we choose using args. And we can add more jobs in this scheduler.
3. We choose to use Cron-style scheduling and run the test at 4am everyday. It also has an optional start and end date.
    Doc: https://apscheduler.readthedocs.io/en/stable/modules/triggers/cron.html#module-apscheduler.triggers.cron