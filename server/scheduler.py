"""
    Defining scheduler module.
"""

import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from server import movies_info


def init_scheduler():
    """
    The function runs tasks periodically.

    :return: None
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        func=movies_info.update_movies_info, trigger="interval", minutes=1)
    scheduler.start()

    # Shut down the scheduler when exiting the app
    atexit.register(scheduler.shutdown)

    # Returning the scheduler for testing purposes
    return scheduler
