def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(Sup_year, Sup_month):
  """
  Take a year and month and return the number of days
  """
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  
  flag = is_leap(Sup_year)
  if flag == True and Sup_month == 2:
    return 29
  return month_days[Sup_month-1]
  
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












