#pragma once
#include <vector>
#include <string>

class Entity
{
public:
	double Score1;
	double Score2;
	double Score3;
	int count;
	std::string name;
	std::vector<std::string> context;

	Entity(std::string name, int count)
	{
		this->name = name;
		this->count = count;
	}
};

class Cell
{
public:
	std::string mention;
	std::vector<Entity> candidates;

	Cell()
	{

	}

	void feed(std::string mention, std::vector<Entity> candidates)
	{
		this->mention = mention;
		this->candidates = candidates;
	}

};

class Table
{
public:
	int row;
	int col;
	Table(int row, int col)
	{
		this->row = row;
		this->col = col;

		cell = new Cell*[row];
		for (int r = 0; r < row; r++)
		{
			cell[r] = new Cell[col];
		}
	}

	Cell& operator()(int i, int j)
	{
		return cell[i][j];
	}

	void free()
	{
		for (int i = 0; i < row; i++)
		{
			delete[] cell[i];
		}
		delete[] cell;
	}

	//~Table()
	//{
	//	for (int i = 0; i < row; i++)
	//	{
	//		delete[] cell[i];
	//	}
	//	delete[] cell;
	//}

private:
	Cell** cell;

};