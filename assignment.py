import datetime

#from pytz import utc, timezone
#from time import mktime

# 1. 'Month and Year' is in MM-DD-YYYY format convert it in DD-MM-YY.
def date_format(data,a):
    # strptime creates datetime object from given string
    date=map(lambda row: datetime.datetime.strptime(row[a],"%m\/%d\/%Y").strftime("%d/%m/%y"), data)
    print date


# 3. Calculate Number of days between 01-01-2020 and each 'Month and Year'
def no_of_days(date1,date2):
    date_difference=date2- date1
    print date_difference


# 8. Sort all entry by Numbers
def get_number(data):
    number=map(lambda row:int(row["Numbers"]),data)
    return sorted(number)









''' # 2.  print each 'Month and Year' in UTC format.
def utc_format(b):
    utc_date=map(lambda row: mktime(utc.localize(row[b].utctimetuple()), main.data)
    #mktime(timezone('US/Eastern').localize(row[b]).utctimetuple())
    print utc_date'''




# 4. Calculate summation of all 'Numbers'.
def sumOfNum(data,d):
    total=0
    for row in data:
        total=total+int(row[d])
    print total

# 5. Calculate cumulative summation of all 'Numbers' and store them into new key. Example : i/p: [{"num":1},{"num":2},{"num":3}] o/p : [{"num":1,"c1":1},{"num":2,"c1":3},{"num":3,"c1":6}]
def cummmu_sum(data,a):
    total = 0
    result=map(lambda row:total+int(row[a]),data)
    print result


# 6. delete 'FormSubmissionID' and 'FormID' from each entry.
def deleteValues(data,e):
    for row in data:
        del row[e]
    print data

# 9. Create a new key having concatenation of 'Category' and 'Sub-Category'Example : i/p  : [{"num":1,"c1":1},{"num":2,"c1":3},{"num":3,"c1":6}]o/p :  [{"num-c1":11},{"num-c1":23},{"num-c1":36}]
def concat_values(data,a,b):
    c = a + '-' + b
    for i in data:
        i[c] = i[a] + " " + i[b]
        del i[a]
        del i[b]
    print data


# 7. Find all entries having 'Type' as 'Actual', 'Forecast', 'Planned'
def type_entry(data,a,b):
    type_entry=filter(lambda row:row[a]==b,data)
    print type_entry





