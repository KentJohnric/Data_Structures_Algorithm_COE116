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

	if (m = 1)
	{
		cout << "Jan" << " " << d << "," << y << endl;
	}
	else if (m = 2)
	{
		cout << "Feb" << " " << d << "," << y << endl;
	}
	else if (m =3)
	{
		cout << "Mar" << " " << d << "," << y << endl;
	}
	else if (m = 4)
	{
		cout << "Apr" << " " << d << "," << y << endl;
	}
	else if (m = 5)
	{
		cout << "May" << " " << d << "," << y << endl;
	}
	else if (m = 6)
	{
		cout << "Jun" << " " << d << "," << y << endl;
	}
	else if (m = 7)
	{
		cout << "Jul" << " " << d << "," << y << endl;
	}
	else if (m = 8)
	{
		cout << "Aug" << " " << d << "," << y << endl;
	}
	else if (m = 9)
	{
		cout << "Sep" << " " << d << "," << y << endl;
	}
	else if (m = 10)
	{
		cout << "Oct" << " " << d << "," << y << endl;
	}
	else if (m = 11)
	{
		cout << "Nov" << " " << d << "," << y << endl;
	}
	else
	{
		cout << "Dec" << " " << d << "," << y << endl;
	}
	date.NewDate(3, 18, 2017, 25);
	date.printDate();

	system("pause");
	return 0;
}