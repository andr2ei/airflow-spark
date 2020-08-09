package ru.andronov.test

import org.apache.spark.sql.SparkSession

object Test {

  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder().getOrCreate()

    val rdd = spark.sparkContext.textFile("/spark-outputs/test_data")
    println(rdd.count())
    rdd.saveAsTextFile("/spark-outputs/test_data_output")
  }

}
