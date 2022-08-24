#include <iostream>
#include "kazuate.h"

using namespace std;


static void prompt()
{
	cout << "0~" << max_no << "の数 :";
}

/// <summary>
/// 回答の入力
/// </summary>
/// <returns>回答</returns>
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
/// 続行の確認
/// </summary>
/// <returns></returns>
bool confirm_retry()
{
	int cont;
	cout << "もう一度しますか？\n"
		<< "<Yes...1 / No...0> :";
	cin >> cont;
	if (cont > 0)
		return true;
	else
		return false;
	return static_cast<bool>(cout);
}