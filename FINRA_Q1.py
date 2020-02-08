# SAMPLE DATA in CSV FILE AS
# ORIGINAL_DATE
# 20190825
# 20190826
# 20190827
# 20190828
# 20190829
# 20190830
# 20190831
# 20190901
# 20191126
# 20190228
# 20190832



# Answer

# The code is written in jupyter notebook as a pyspark functionality from local drive

import findspark
findspark.init()
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()


date_df = spark.read.format("csv").option("header",True).load("/Users/apple/Desktop/Projects/Spark/original_date.csv")
date_df.createOrReplaceTempView("date_df_view") #creating a hive table on the original date dataframe

spark.sql("""
select date_format(a.ORIGINAL_DATE, "yyyyMMdd") as ORIGINAL_DATE
, date_format(case 
    when dayofweek(a.ORIGINAL_DATE) > 1 then date_add(a.ORIGINAL_DATE, (8 - dayofweek(a.ORIGINAL_DATE)))
    else  a.ORIGINAL_DATE
end, "yyyyMMdd") as END_OF_WEEK  
, date_format(last_day(a.ORIGINAL_DATE), "yyyyMMdd") as END_OF_MONTH
from (
select TO_DATE(CAST(UNIX_TIMESTAMP(ORIGINAL_DATE, 'yyyyMMdd') AS TIMESTAMP)) as ORIGINAL_DATE from orginal_date_tmp
) a
""").show()

# Will out put the below result

# +-------------+-----------+------------+
# |ORIGINAL_DATE|END_OF_WEEK|END_OF_MONTH|
# +-------------+-----------+------------+
# |     20190825|   20190825|    20190831|
# |     20190826|   20190901|    20190831|
# |     20190827|   20190901|    20190831|
# |     20190828|   20190901|    20190831|
# |     20190829|   20190901|    20190831|
# |     20190830|   20190901|    20190831|
# |     20190831|   20190901|    20190831|
# |     20190901|   20190901|    20190930|
# |     20191126|   20191201|    20191130|
# |     20190228|   20190303|    20190228|
# |         null|       null|        null|
# +-------------+-----------+------------+

# MYSQL Query
# This query will run against the database provided by the test creator.
# The database is reset to the initial state on every run.
# select
#   ORIGINAL_DATE,
#   case
#     when dayofweek(DATE_FORMAT(ORIGINAL_DATE, '%Y-%m-%d')) > 1
#       then date_add(DATE_FORMAT(ORIGINAL_DATE, '%Y-%m-%d'), INTERVAL (8 - dayofweek(DATE_FORMAT(ORIGINAL_DATE, '%Y-%m-%d'))) DAY)
#     ELSE DATE_FORMAT(ORIGINAL_DATE, '%Y-%m-%d') END as END_OF_WEEK,
#   last_day(date_format(ORIGINAL_DATE, '%Y-%m-%d')) as END_OF_MONTH
#   from random_dates;