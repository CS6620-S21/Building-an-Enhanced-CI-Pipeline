from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

if __name__ == '__main__':
    scheduler = BlockingScheduler()

    scheduler.add_job(subprocess.run,
                      'interval',
                      hours=1,
                      args=([
                          "locust", "-f", "locustfile.py", "--host",
                          "http://34.102.157.148", "--users", "300",
                          "--spawn-rate", "2", "--run-time", "30s",
                          "--headless"
                      ], ))

    scheduler.start()