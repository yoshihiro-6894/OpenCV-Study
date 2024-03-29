# include <iostream>
# include <cstdlib>
#include "kazuate.h"

using namespace std;

static int kotae = 0;
extern int max_no;

/// <summary>
/// 初期化
/// </summary>
void initialize()
{
	srand(time(NULL));
}

/// <summary>
/// 問題の作成
/// </summary>
void gen_no()
{
	kotae = rand() % (max_no + 1);
}

/// <summary>
/// 回答の判定
/// </summary>
/// <param name="cand">回答</param>
int judge(int cand)
{
	if (cand == kotae)
		return 0;
	else if (cand > kotae)
		return 1;
	else
		return 2;
}