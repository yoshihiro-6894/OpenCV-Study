# include <iostream>
# include <cstdlib>
#include "kazuate.h"

using namespace std;

static int kotae = 0;
extern int max_no;

/// <summary>
/// ������
/// </summary>
void initialize()
{
	srand(time(NULL));
}

/// <summary>
/// ���̍쐬
/// </summary>
void gen_no()
{
	kotae = rand() % (max_no + 1);
}

/// <summary>
/// �񓚂̔���
/// </summary>
/// <param name="cand">��</param>
int judge(int cand)
{
	if (cand == kotae)
		return 0;
	else if (cand > kotae)
		return 1;
	else
		return 2;
}