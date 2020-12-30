#pragma once
#include <iostream>
#include <cstdlib>

using namespace std;
class dateType
{
public:
	void setDate(int month, int day, int year);
	int getMonth() const;
	int getDay() const;
	int getYear() const;
	void printDate() const;

	dateType(int month = 8, int day = 3, int year = 2017);
	bool leapYear(int);

private:
	int dMonth;
	int dYear;
	int dDay;
};