#include <iostream>
#include "dateType.h"
using namespace std;

int main()
{

	int m, d, y, numDays, passed, remain;

	dateType date(0, 0, 0);

	cout << "Enter Month as a number:";
	cin >> m;
	cout << "Enter Day:";
	cin >> d;
	cout << "Enter Year:";
	cin >> y;

	date.setYear(y);

	bool check = date.isLeapYear(y);

	if (check)
		cout << "Leap year" << endl;

	numDays = date.setMonth(m);
	cout << "Number of days in the month is:" << numDays << endl;
	passed = date.totalNumOfpassedDays(m, d);

	cout << "Total number of days passed are:" << passed << endl;
	remain = date.RemainingDays(y);

	cout << "Total number of days remaining are:" << remain << endl;

	date.NewDate(3, 18, 2017, 25);
	date.printDate();

	system("pause");
	return 0;
}