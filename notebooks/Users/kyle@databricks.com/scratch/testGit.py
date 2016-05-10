# Databricks notebook source exported at Tue, 10 May 2016 19:53:30 UTC
df = sqlContext.sql("select * from diamonds limit 10").count()

# COMMAND ----------

