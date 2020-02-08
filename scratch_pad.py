
# order_id, Order_timestamp, order_amount, customer_email

# import boto3

# respose  = client("s3").get_object(bucket = "bucket_name",
#                                    key = "Path_to_the_CSV_file",
#                                    encryption= "KMS/sse256")

# df = spark.read.csv("s3://bucket_name/Path_to_the_CSV_file")
# df.createorReplaceTempView("df_order_data")
# df_info =spark.sql("""
# select customer_email from df where groupby order (order_amount == max(order_amount)) and Order_timestamp lessthan '09/01/2019'
# and greaterthan "07/31/2019"
# """)

import heapq
def monday():
    return "monday"
def tuesday():
    return "tuesday"
def wednesday():
    return "wednesday"
def thursday():
    return "thursday"
def friday():
    return "friday"
def saturday():
    return "saturday"
def sunday():
    return "sunday"
def default():
    return "Incorrect day"

switcher = {
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
    }

def switch(dayOfWeek):
    return switcher.get(dayOfWeek, default)()

print(switch(1))
print(switch(0))

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)


# if __name__ == '__main__':
#     f(3)

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])