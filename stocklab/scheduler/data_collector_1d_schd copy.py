import time
import inspect
from multiprocessing import Process
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler 

from stocklab.agent.ebest import EBest
from stocklab.agent.data import Data
from stocklab.db_handler.mongodb_handler import MongoDBHandler
"""
def test_get_stock_price_by_code(self):
        print(inspect.stack()[0][3])
        result = self.ebest.get_stock_price_by_code("005930", "30")
        assert result is not None
        print(result)
"""


def run_process_collect_code_list():
    print(inspect.stack()[0][3])
    p = Process(target=collect_code_list)
    p.start()
    p.join()

def run_process_collect_stock_info():
    print(inspect.stack()[0][3])
    p = Process(target=collect_stock_info)
    p.start()
    p.join()

def collect_stock_info():
    ebest = EBest("DEMO")
    mongodb = MongoDBHandler()
    ebest.login()
    code_list = mongodb.find_items({}, "stocklab", "code_info")
    target_code = set([item["단축코드"] for item in code_list])
    today = datetime.today().strftime("%Y%m%d")
    print(today)
    collect_list = mongodb.find_items({"날짜":today}, "stocklab", "price_info") \
                            .distinct("code")
        target_code.remove(col)
        time.sleep(1)
        print("code:005930")
        result_price = ebest.get_stock_price_by_code("005930", "1000")
        if len(result_price) > 0:
            print(result_price)
            mongodb.insert_items(result_price, "stocklab", "price_info")

        result_credit = ebest.get_credit_trend_by_code("005930", today)
        
    
if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=run_process_collect_stock_info, trigger="cron", 
                    day_of_week="mon-fri", hour="*", minute="*/1", id="2")
    scheduler.start()
    while True:
        print("running", datetime.now())
        time.sleep(1)
        