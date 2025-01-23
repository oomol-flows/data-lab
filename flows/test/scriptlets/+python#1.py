from oocana import Context
import pandas as pd

def main(params: dict, context: Context):

  # 创建示例数据
  data = {
      'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
      'Category A': [10, 15, 13, 17, 21, 25, 22, 29, 31, 35],
      'Category B': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
      'Category C': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
  }

  df = pd.DataFrame(data)
  

  return { "df": df }
