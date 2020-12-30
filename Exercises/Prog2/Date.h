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

void dateType::setDate(int month, int day, int year)
{
	bool error = false;
	int max = 28;
	switch (month)
	{
	case 1:
	case 3:
	case 5:
	case 7:
	case 8:
	case 10:
	case 12:if (day > 31)
		error = true;
		break;
	case 4:
	case 6:
	case 9:
	case 11: if (day > 30)
		error = true;
		break;
	case 2: if (leapYear(year))
		max = 29;
		if (day > max)
			error = true;
	}
	if (error)
	{
		cout << "Invalid Date" << month << "|" << day << "|" << year << endl;
		month = 8;
		day = 3;
		year = 2017;
	}
	dMonth = month;
	dDay = day;
	dYear = year;
}
bool dateType::leapYear(int year)
{
	if (((year % 4 == 0) && (year % 100 == 0)) || (year % 400 == 0))
		return true;
	else
		return false;
}
int dateType::getDay() const
{
	return dDay;
}
int dateType::getMonth() const
{
	return dMonth;
}
int dateType::getYear() const
{
	return dYear;
}
void dateType::printDate() const
{
	cout << dMonth << "-" << dDay << "-" << dYear;
}
dateType::dateType(int month, int day, int year)
{
	setDate(month, day, year);
}
