#!/usr/bin/env python
# encoding : UTF-8
"""
@author : Xil-max
@file   : 使用Spark SQL统计各个研发单位研制战斗机占比.py
@time   : 2022/1/3 11:14
@Description : TODO
"""

# coding=utf-8

from pyspark.sql import SparkSession

# **********Begin**********#

# 创建SparkSession
spark = SparkSession \
    .builder \
    .appName("Python spark sql example") \
    .master("local") \
    .getOrCreate()

# 读取/root/jun.json中数据
df = spark.read.json("./dataset/jun.json").coalesce(1)

# 创建视图
df.createOrReplaceTempView("table1")

# 统计出全球各研发单位研制的战斗机在全球所有战斗机中的占比
sqlDF = spark.sql(
    "select   concat(round(count(`研发单位`)*100/(select count(`研发单位`) as num from table1 where `研发单位` is not null and `名称`is not null ),2),'%') as ratio, `研发单位` from table1  where  `研发单位` is not null and `名称`is not null group by  `研发单位`")

# "select concat(cast(round(count(`研发单位`)*100/(select count(`研发单位`) from table1 where `研发单位` is not null and `名称` is not null),2) as float ), '%') as proportion"
#    ", `研发单位` from table1 where `研发单位` is not null and `名称` is not group by `研发单位`"

# sqlDF.show(n=10)

# 保存结果
sqlDF.write.mode("overwrite").format("csv").save("./output/air_spark1/")


spark.stop()
