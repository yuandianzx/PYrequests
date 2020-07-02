# coding:utf-8
import unittest
def all_case():
    # 待执行用例的目录
    case_dir = "D:\\test\\yoyotest\\case"
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,
    pattern="test*.py",         # case_dir：待执行用例目录，pattern：这个是匹配脚本名称的规则，top_level_dir：这个是顶层目录的名称，一般默认等于 None 就行了
    top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    # discover 方法筛选出来的用例，循环添加到测试套件中
    # for test_suite in discover:
    # for test_case in test_suite:
    # testunit.addTests(test_case)
    # print(testunit)
    testcase.addTests(discover) # 直接加载 discover
    print(testcase)
    return testcase
if __name__ == "__main__":
    # 返回实例
    runner = unittest.TextTestRunner()
    # run 所有用例
    runner.run(all_case())