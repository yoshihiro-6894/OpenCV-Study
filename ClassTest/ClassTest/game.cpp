# include <iostream>
# include <cstdlib>
#include "kazuate.h"

using namespace std;

static int kotae = 0;
extern int max_no;

/// <summary>
/// ‰Šú‰»
/// </summary>
void initialize()
{
	srand(time(NULL));
}

/// <summary>
/// –â‘è‚Ìì¬
/// </summary>
void gen_no()
{
	kotae = rand() % (max_no + 1);
}

/// <summary>
/// ‰ñ“š‚Ì”»’è
/// </summary>
/// <param name="cand">‰ñ“š</param>
int judge(int cand)
{
	if (cand == kotae)
		return 0;
	else if (cand > kotae)
		return 1;
	else
		return 2;
}