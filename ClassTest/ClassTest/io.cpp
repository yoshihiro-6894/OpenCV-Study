#include <iostream>
#include "kazuate.h"

using namespace std;


static void prompt()
{
	cout << "0~" << max_no << "�̐� :";
}

/// <summary>
/// �񓚂̓���
/// </summary>
/// <returns>��</returns>
int input()
{
	int val;
	do
	{
		prompt();
		cin >> val;
	} while (val < 0 || val > max_no);

	return val;
}

/// <summary>
/// ���s�̊m�F
/// </summary>
/// <returns></returns>
bool confirm_retry()
{
	int cont;
	cout << "������x���܂����H\n"
		<< "<Yes...1 / No...0> :";
	cin >> cont;
	if (cont > 0)
		return true;
	else
		return false;
	return static_cast<bool>(cout);
}