#!/usr/bin/env python
# encoding : UTF-8
"""
@author : Maximilian M
@file   : pyspark_install_test.py
@time   : 2022/1/1 19:21
@Description : TODO
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# 初始化
spark = SparkSession.builder.master("local[*]").appName("FirstApp").getOrCreate()

# 下面两句都可以获取0到9的数据
# data = spark.createDataFrame(map(lambda x: (x,), range(10)), ["id"])
data = spark.range(0, 10).select(col("id").cast("double"))

# 求和

data.agg({'id': 'sum'}).show()

# 关闭
spark.stop()

