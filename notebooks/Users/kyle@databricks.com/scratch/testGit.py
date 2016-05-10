# Databricks notebook source exported at Tue, 10 May 2016 20:12:37 UTC
df = sqlContext.sql("select * from diamonds limit 10").cache().count()

# COMMAND ----------

df.count()