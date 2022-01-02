**Standalone模式下**

```shell
# Standalone模式启动
$ sbin/start-all.sh

# 客户端运行
$ bin/spark-shell --master spark://mzj01.m.com:8081

# 集群运行
$ bin/spark-submit --master spark://mzj01.m.com:8081 --deploy-mode cluster /opt/jars/test.jar file:///opt/datas/weblog.log

```

**Spark Streaming vs Storm**

|      | Spark Streaming                | Storm                 |
| ---- | :----------------------------- | :-------------------- |
|      | 准实时 - 小时间内的数据形成RDD | 实时 - 来一条处理一条 |
|      | 不可动态调整并行度             | 动态调整并行度        |
|      | 基于batch，吞吐量大            | 基于一条一条          |
|      | 一站式大数据处理功能           | 兼容性 - 非一站式     |

**Spark SQL vs Hive**

> SSQL不能完全代替Hive，Hive是基于HDFS的大数据仓库
>
> SSQL能够替代的是Hive的查询引擎，查询速度快，Spark本身不提供存储
>
> SSQL支持大量不同数据源，与其他组件无缝衔接

