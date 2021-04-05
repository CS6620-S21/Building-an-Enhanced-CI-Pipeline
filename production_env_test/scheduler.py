from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

if __name__ == '__main__':
    scheduler = BlockingScheduler()

    scheduler.add_job(subprocess.run, 'interval', minutes=30, args=(["locust" ,"-f","locustfile.py","--host", "http://35.239.70.253/", "--users", "300", "--spawn-rate", "2", "--run-time", "30s", "--headless"], ))

    scheduler.start()