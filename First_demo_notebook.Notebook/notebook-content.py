# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "931e7e1a-e8f6-4904-a44c-971437495e23",
# META       "default_lakehouse_name": "demo_lakehouse",
# META       "default_lakehouse_workspace_id": "8a652689-8317-412f-a058-8487233f780e",
# META       "known_lakehouses": [
# META         {
# META           "id": "931e7e1a-e8f6-4904-a44c-971437495e23"
# META         }
# META       ]
# META     },
# META     "warehouse": {}
# META   }
# META }

# CELL ********************


df = spark.read.option("header", True).csv(
    "abfss://8a652689-8317-412f-a058-8487233f780e@onelake.dfs.fabric.microsoft.com/931e7e1a-e8f6-4904-a44c-971437495e23/Files"
)

display(df.head(5))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.write.mode("overwrite").format("delta").saveAsTable("demo_table")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT *
# MAGIC FROM demo_table
# MAGIC LIMIT 5


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
