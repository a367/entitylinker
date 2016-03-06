#include<iostream>
#include<iomanip>
#include<cmath>
#include<algorithm>
#define dps 1e-8
using namespace std;

double D[10005][10005];
int** P;
int N;

bool cmp(int p[2], int q[2])
{
	if (p[0] > q[0])
	{
		return false;
	}
	return true;
}
double dis(int i, int j)
{
	int x1 = P[i][0];
	int y1 = P[i][1];
	int x2 = P[j][0];
	int y2 = P[j][1];
	return sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2));
}
double dp(int i, int j)
{
	if (j < i)
	{
		int temp = i;
		i = j;
		j = temp;
	}
	if (abs(D[i][j] + 1) > dps)
	{
		return D[i][j];
	}
	if (j > i + 1)
	{
		D[i][j] = dp(i + 1, j) + dis(i, i + 1);
		return D[i][j];
	}
	else
	{
		double min_t = dp(i + 1, j) + dis(i, i + 1);
		for (int k = i + 2; k < N; k++)
		{
			if (min_t > dp(k, j) + dis(i, k))
			{
				min_t = dp(k, j) + dis(i, k);
			}
		}
		D[i][j] = min_t;
		return D[i][j];
	}
}
int main()
{
	while (cin >> N)
	{
		P = new int*[N];
		for (int i = 0; i < N; i++)
		{
			P[i] = new int[2];
		}
		for (int i = 0; i < N; i++)
		{
			cin >> P[i][0] >> P[i][1];
		}
		sort(P, P + N, cmp);
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				D[i][j] = -1;
			}
		}
		D[N - 2][N - 1] = dis(N - 2, N - 1);
		D[N - 1][N - 1] = 0;
		cout << fixed << setprecision(2) << dp(0, 0) << endl;

		for (int i = 0; i < N; i++)
		{
			delete[] P[i];
		}
		delete[] P;
	}

	system("pause");
	return 0;
}