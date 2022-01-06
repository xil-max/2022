#!/usr/bin/env python
# encoding : UTF-8
"""
@author : Xil-max
@file   : 使用SparkSQL统计战斗机飞行性能.py
@time   : 2022/1/3 10:18
@Description : TODO
"""

from pyspark.sql import SparkSession


# 创建SparkSession
spark = SparkSession \
    .builder \
    .appName("Python spark SQL basic example") \
    .master("local") \
    .getOrCreate()

# 读取/root/jun.json中数据
# df = spark.read.json("/data/workspace/myshixun/step1/jun.json")
df = spark.read.json("./dataset/jun.json").coalesce(1)

# 创建视图
df.createOrReplaceTempView("table1")

# 统计出全球飞行速度排名前三的战斗机
sqlDF = spark.sql(
    "select cast(regexp_replace(regexp_extract(`最大飞行速度`,'[\\\d,\\\.]+',0),'\\\,','') as float) as speed,`名称` from table1  order by cast(regexp_replace(regexp_extract(`最大飞行速度`,'[\\\d,\\\.]+',0),'\\\,','') as float)  DESC limit 3")

# sqlDF = spark.sql("select `名称` from table1")
# spark.sql("select cast(replace(regexp_ext\fract(`最大飞行速度`,'[\\\d,\\\.]+',0),',','') as float) as SPEED, `名称` from table1 order BY SPEED desc LIMIT 3")
# sqlDF.show()

# 保存结果
sqlDF.write.mode("overwrite").format("csv").save("./output/air_spark/")

spark.stop()
