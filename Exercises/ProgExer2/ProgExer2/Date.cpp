#include "Date.h"
#include <iostream>

using namespace std;

int main()
{
	dateType d(2, 30, 2020);
	cout << "The date is: ";
	d.printDate();
	cout << endl;

	system("pause");
	return 0;
}