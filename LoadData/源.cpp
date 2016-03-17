#pragma comment(lib,"jsoncpp.lib")
#include "json\json.h"
#include "table.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;


vector<Table> loadData(string json)
{
	Json::Reader reader;
	Json::Value root;

	reader.parse(json, root);
	vector<Table> tables;

	for (int i = 0; i < root.size(); i++)
	{
		Json::Value table = root[i];
		Json::Value content = table["content"];
		int col = table["col"].asInt();
		int row = table["row"].asInt();

		Table m_table(row, col);


		for (int r = 0; r < row; r++)
		{
			for (int c = 0; c < col; c++)
			{
				Json::Value cell = content[r * row + c];
				Json::Value candidates = cell["candidates"];
				string mention = cell["mention"].asString();

				vector<Entity> VecCandidates;
				for (int j = 0; j < candidates.size(); j++)
				{
					string name = candidates[j]["name"].asString();
					int count = candidates[j]["count"].asInt();
					VecCandidates.push_back(Entity(name, count));
				}

				m_table(r,c).feed(mention, VecCandidates);
			}
		}

		tables.push_back(m_table);
	}
	return tables;
}

int main()
{
	fstream in("data.txt");

	istreambuf_iterator<char> beg(in), end;
	string str(beg, end);

	vector<Table> tables = loadData(str);
	Table t = tables[0];
	cout << t(0, 0).candidates[0].name << endl;

	system("pause");
	return 0;
}