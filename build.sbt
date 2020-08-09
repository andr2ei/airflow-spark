name := "airflow-spark"

version := "0.1"

scalaVersion := "2.11.10"

libraryDependencies += "org.apache.spark" %% "spark-core" % "2.3.3" % "provided"
libraryDependencies += "org.apache.spark" %% "spark-sql" % "2.3.3" % "provided"