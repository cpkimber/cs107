#! /home/cam/anaconda3/bin/python3
"""
file: date.py
Cameron Kimber
date: 2018-10-24
Class: CSE107
Assignment:
"""

regular_months = {"January": 0,
                  "February": 31,
                  "March": 59,
                  "April": 89,
                  "May": 120,
                  "June": 150,
                  "July": 181,
                  "August": 212,
                  "September": 242,
                  "October": 273,
                  "November": 303,
                  "December": 334}

leap_months = {"January": 31,
               "February": 29,
               "March": 31,
               "April": 30,
               "May": 31,
               "June": 30,
               "July": 31,
               "August": 31,
               "September": 30,
               "October": 31,
               "November": 30,
               "December": 31}


def day_number(date):
    month, day, year = date.split(",")
    if eval(year) % 4 == 0 and eval(year) % 100 != 0 or eval(year) % 400 != 0:
        print("Day of the regular year: " +
              str(regular_months[month] + eval(day)))
    else:
        print("Day of the leap year: " +
              str(leap_months[month] + eval(day)))


def main():
    bday = "February, 16, 1990"
    day_number(bday)


if __name__ == "__main__":
    main()
