#pragma once
#ifndef DATATYPE_H
#define DATATYPE_H

using namespace std;
class dateType
{
private:
	int dMonth;
	int dDay;
	int dYear;
	int noDays;
	int Passeddays;

public:
	int setMonth(int month);

	void setDay(int day);

	void setYear(int year);

	int getDay() const;

	int getMonth() const;

	int getYear() const;

	void printDate() const;

	bool isLeapYear(int year);

	int totalNumOfpassedDays(int, int);

	int RemainingDays(int);

	void NewDate(int, int, int, int);
	dateType(int month = 0, int day = 0, int year = 0);

};

dateType::dateType(int month, int day, int year)
{
	dMonth = month;
	dDay = day;
	dYear = year;
}

int dateType::totalNumOfpassedDays(int month, int day)
{
	return 0;
}

void dateType::NewDate(int month, int day, int year, int adddays)
{

	if ((day + adddays) % month)
	{

		dDay = day + adddays;
		dDay = abs(dDay - 31);
		month++;
		dMonth = month;
		
		dYear = year;
		if (month>12)
		{
			dMonth = 1;
			dYear++;
		}
	}
}

int dateType::RemainingDays(int year)
{
	int remainingDays;
	if (isLeapYear(year))
	{
		remainingDays = 366 - Passeddays;
	}

	else
		remainingDays = 365 - Passeddays;

	return remainingDays;

}

int dateType::setMonth(int month)
{
	int year1;
	year1 = dYear;
	if (month <= 12)
	{
		dMonth = month;
		switch (month)
		{
			
		case 1:
		case 3:

		case 5:

		case 7:

		case 8:

		case 10:

		case 12: noDays = 31;

			break;

		case 4:

		case 6:

		case 9:

		case 11:noDays = 30;

			break;

		case 2:if (isLeapYear(year1))
			noDays = 29;
			   else
				   noDays = 28;
		}

	}

	else
	{
		cout << "Invalid Month" << endl;
		dMonth = 0;
	}
	return noDays;

}

void dateType::setDay(int day)
{
	if (day <= noDays)
	{
		dDay = day;
	}
	else
	{
		cout << "Invalid Day" << endl;
		dDay = 0;
	}

}

void dateType::setYear(int year)
{
	dYear = year;
}

bool dateType::isLeapYear(int year)
{
	if (((year % 4 == 0) && (year % 100 == 0)) || (year % 400 == 0))
		return true;
	else
		return false;
}

void dateType::printDate()const
{
	cout << "DATE: DD/MM/YYYY : " << dDay << "/" << dMonth << "/" << dYear << endl;
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
#endif