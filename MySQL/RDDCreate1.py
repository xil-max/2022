#!/usr/bin/env python
# encoding : UTF-8
"""
@author : Xil-max
@file   : RDDCreate1.py
@time   : 2022/1/2 22:43
@Description : 集合并行化创建RDD
"""

from pyspark import SparkContext

if __name__ == "__main__":

    # 1.初始化 SparkContext, 该对象是 Spark 程序的入口
    sc = SparkContext("local", "Simple App")

    # 2.创建一个1到8的列表List
    data = list(range(1, 9))

    # 3.通过 SparkContext 并行化创建RDD
    rdd = sc.parallelize(data)

    # 4.使用 rdd.collect() 收集 rdd 的内容
    rdd.collect()

    # 5.打印 rdd 的内容
    print(rdd.collect())

    # 6.停止 SparkContext
    sc.stop()
