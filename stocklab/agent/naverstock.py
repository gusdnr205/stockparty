import configparser
import win32com.client
import pythoncom
from datetime import datetime
import time
import unittest
from stocklab.agent.ebest import EBest
import inspect
import time
from multiprocessing import Process
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler 
from stocklab.agent.ebest import EBest
from stocklab.agent.data import Data
from stocklab.db_handler.mongodb_handler import MongoDBHandler

class XQuery_t1305:
    
    def __init__(self):
        self.is_data_received = False
        self.date = ""
        self.ebest = EBest("DEMO")
        self.ebest.login()
        self.dwmcode="1"
        self.idx=""
        self.cnt="300"
        #in_params = {"shcode":code, "dwmcode": "1", "date":"", "idx":"", "cnt":cnt}

    def OnReceiveData(self, tr_code):
        self.is_data_received = True
        count = self.GetBlockCount("t1305OutBlock1") # 반복데이터(Occurs) 갯수 가져오기
        print("count = {0}".format(count))
        print("TR code ==> {0}".format(tr_code))

        for i in range(count):
            date = self.GetFieldData("t1305OutBlock1", "date", i)
            open = self.GetFieldData("t1305OutBlock1", "open", i)
            high= self.GetFieldData("t1305OutBlock1", "high", i)
            low= self.GetFieldData("t1305OutBlock1", "low", i)
            close= self.GetFieldData("t1305OutBlock1", "close", i)
            sign= self.GetFieldData("t1305OutBlock1", "sign", i)
            change= self.GetFieldData("t1305OutBlock1", "dachangete", i)
            diff= self.GetFieldData("t1305OutBlock1", "diff", i)
            volume= self.GetFieldData("t1305OutBlock1", "volume", i)
            diff_vol= self.GetFieldData("t1305OutBlock1", "diff_vol", i)
            chdegree= self.GetFieldData("t1305OutBlock1", "chdegree", i)
            sojinrate= self.GetFieldData("t1305OutBlock1", "sojinrate", i)
            changerate= self.GetFieldData("t1305OutBlock1", "changerate", i)
            fpvolume= self.GetFieldData("t1305OutBlock1", "fpvolume", i)
            covolume= self.GetFieldData("t1305OutBlock1", "covolume", i)
            shcode= self.GetFieldData("t1305OutBlock1", "shcode", i)
            value= self.GetFieldData("t1305OutBlock1", "value", i)
            ppvolume= self.GetFieldData("t1305OutBlock1", "ppvolume", i)
            o_sign= self.GetFieldData("t1305OutBlock1", "o_sign", i)
            o_chang= self.GetFieldData("t1305OutBlock1", "o_chang", i)
            o_diff= self.GetFieldData("t1305OutBlock1", "o_diff", i)
            h_sign= self.GetFieldData("t1305OutBlock1", "h_sign", i)
            h_change= self.GetFieldData("t1305OutBlock1", "h_change", i)
            h_diff= self.GetFieldData("t1305OutBlock1", "h_diff", i)
            l_sign= self.GetFieldData("t1305OutBlock1", "l_sign", i)
            l_change= self.GetFieldData("t1305OutBlock1", "l_change", i)
            l_diff= self.GetFieldData("t1305OutBlock1", "l_diff", i)
            marketcap= self.GetFieldData("t1305OutBlock1", "marketcap", i)
            print("{3} - 거래시간;{0}, 현재가;{1},누적거래량;{2}".format(date, open, high, i))
        self.date = self.GetFieldData("t1305OutBlock", "date", 0)
        print("--{0}--".format(self.date))

        if self.date != "": # self.date 값이 존재하면, 연속 data 가 있다는 의미...
            time.sleep(0.5) # TR 횟수 제한때문에...
            self.continue_search(self.date)

    def occurs_request(self, stockcode,dwmcode="1",idx="",date="",cnt="300"):
        self.ResFileName = "C:\\eBEST\\xingAPI\\Res\\t1305.res" # RES 파일 등록
        self.SetFieldData("t1305InBlock", "shcode",0,stockcode)
        self.SetFieldData("t1305InBlock", "dwmcode",0,dwmcode)
        self.SetFieldData("t1305InBlock", "date",0,date)
        self.SetFieldData("t1305InBlock", "shcode",0,idx)
        self.SetFieldData("t1305InBlock", "cnt",0,cnt)
        err_code = self.Request(False) # data 요청하기 -- 연속조회인경우만 True

        if err_code < 0:
            print("error... {0}".format(err_code))

    def continue_search(self, date):
        """
        연속조회하기
        """
        print("-----------------------------------------")
        self.is_data_received = False
        self.SetFieldData("t1305InBlock", "date", 0, date)
        err_code = self.Request(True) # 연속조회인경우만 True

        if err_code < 0:
            print("error... {0}".format(err_code))
    @classmethod
    def get_instance(cls):
        xq_t1305 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", cls)
        return xq_t1305



if __name__ == "__main__":
    def get_occurs_continue_data():
        xq_t1305 = XQuery_t1305.get_instance()
        xq_t1305.occurs_request("005930")

        while xq_t1305.is_data_received == False:
            pythoncom.PumpWaitingMessages()
    get_occurs_continue_data()