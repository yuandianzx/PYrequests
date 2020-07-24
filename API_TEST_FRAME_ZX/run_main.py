import unittest
import HTMLTestReportCN
import time
from config_utils import ConfigUtils

def get_all_cases_suite():
    discover = unittest.defaultTestLoader.discover(start_dir = 'test_case', pattern='test*.py')     # 根据各种标准加载测试用例，并将它们返回给测试套件discover
    all_cases_suite = unittest.TestSuite()
    all_cases_suite.addTest(discover)

    return all_cases_suite

all_cases_suite = get_all_cases_suite()     # 实例化测试套件函数，否则无法加载至unittest.main()中

# unittest.main(defaultTest = 'all_cases_suite', verbosity=2)
report_dir = ConfigUtils.read_config('path','report_path')
nowday = time.strftime("%Y-%m-%d")
now = time.strftime("%Y-%m-%d_%H%M%S")
report_name = report_dir +  '/' + now + '.html'
print(report_name)

fp = open(report_name,'wb')
runner_report = HTMLTestReportCN.HTMLTestRunner(stream=fp,tester='zx',title='我的测试报告',description = '这是一个测试报告的描述')
runner_report.run(all_cases_suite)
fp.close()