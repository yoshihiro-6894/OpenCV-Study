#include <iostream>
#include "kazuate.h"

using namespace std;

int max_no = 9;

int main()
{
	initialize();
	cout << "�����ăQ�[���J�n\n";

	do
	{
		gen_no();
		int hantei;
		do
		{
			hantei = judge(input());
			if (hantei == 1)
				cout << "\a�����Ə������ł���\n";
			else if (hantei == 2)
				cout << "\a�����Ƒ傫���ł���\n";
		} while (hantei !=0);
		cout << "�����ł��I\n";
	} while (confirm_retry());
}