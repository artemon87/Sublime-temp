#include <iostream>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

void bubbleSort(vector<int> &i);
void selectSort(vector<int> &i);
void quickSort(std::vector<int> &v, int left, int right);
void quickSort2(std::vector<int> &v, int left, int right);
void bubbleSort2(std::vector<int> &v);
void merge(std::vector<int> &v, int size, int low, int mid, int high);
void mergeSort(std::vector<int> &v, int low, int high);
void merge2(std::vector<int> &v, int low, int mid, int high);
void mergeSort2(std::vector<int> &v, int low, int high);
void merge3(std::vector<int> &v, int low, int mid, int high);
void mergeSort3(std::vector<int> &v, int low, int high);
void quickSort3(std::vector<int> &v, int left, int right);
string removeChars(string, string);
int main()
{
	std::vector<int> v;
	v.push_back(3);
	v.push_back(2);
	v.push_back(9);
	v.push_back(1);
	v.push_back(0);
	string s = "hello word";
	string b = removeChars(s, "el");
	for(int i=0; i < v.size(); i++)
	{
		cout << v[i] << " ";
	}
	cout << endl;
	//bubbleSort2(v);
	//quickSort3(v, 0, v.size()-1);
	mergeSort3(v, 0, v.size() - 1);
	for(int i=0; i < v.size(); i++)
	{
		cout << v[i] << " ";
	}
	cout << endl;

	return 0;
}
void selectSort(vector<int> &v)
{
	int size = v.size();
	for(int i=size -1; i > 0; i--)
	{
		int j = 0;
		while(j < i)
		{
			if(v[i] < v[j])
			{
				int temp = v[j];
				v[j] = v[i];
			}
		}
	}
}
void bubbleSort(std::vector<int> &v)
{
	int size = v.size();
	bool runAgain = true;;
	for(int i = 0; i < size -1; i++)
	{
		runAgain = false;
		for(int j = 1; j < size - 1; j++)
		{
			int trav = 0;
			if(v[trav] < v[j])
			{
				trav = j;
				int temp = v[j];
				v[j] = v[j+1];
				v[j+1] = temp;
				runAgain = true;
			}
		}
		if(runAgain == false)
			break;
	}
}
void bubbleSort2(std::vector<int> &v)
{
	int size = v.size();
	bool runAgain = true;;
	for(int i = 0; i < size - 1; i++)
	{
		runAgain = false;
		for(int j = 1; j < size; j++)
		{
			if(v[j] < v[j-1])
			{
				int temp = v[j-1];
				v[j-1] = v[j];
				v[j] = temp;
				runAgain = true;
			}
		}
		if(runAgain == false)
			break;
	}
}
void quickSort(std::vector<int> &v, int left, int right)
{
	int i = left;
	int j = right;
	int pivot = v[(right+left) / 2];
	while(i <= j)
	{
		while(v[i] < pivot)
		{
			i++;
		}
		while(v[j] > pivot)
		{
			j--;
		}
		if(i <= j)
		{
			int temp = v[i];
			v[i] = v[j];
			v[j] = temp;
			i++;
			j--;
		}
	}
	if(i < right)
	{
		quickSort(v, i, right);
	}
	if(j > left)
	{
		quickSort(v, left, j);
	}
}
void mergeSort(std::vector<int> &v, int low, int high)
{
	if(low < high)
	{
		int mid = (high + low) / 2;
		mergeSort(v, low, mid);
		mergeSort(v, mid + 1, high);
		merge(v, high + 1, low, mid, high);
	}
}
void merge(std::vector<int> &v, int size, int low, int mid, int high)
{
	vector<int> temp (size);
	int first = low;
	int last = mid;
	int first2 = mid + 1;
	int last2 = high;
	int newFirst = first;
	while(first <= last && first2 <= last2)
	{
		if(v[first] < v[first2])
		{
			temp[newFirst] = v[first];
			first++;
		}
		else
		{
			temp[newFirst] = v[first2];
			first2++;
		}
		newFirst++;
	}
	while(first <= last)
	{
		temp[newFirst] = v[first];
		first++;
		newFirst++;
	}
	while(first2 <= last2)
	{
		temp[newFirst] = v[first2];
		first2++;
		newFirst++;
	}
	for(int i = low; i <= high; i++)
	{
		cout << temp[i] << "|";
		v[i] = temp[i];
	}
	cout << endl;
}
void quickSort2(std::vector<int> &v, int low, int high)
{
	int i = low;
	int j = high;
	int pivot = v[(low + high) / 2];
	while(i <= j)
	{
		while(v[i] < pivot)
		{
			i++;
		}
		while(v[j] > pivot)
		{
			j--;
		}
		if(i <= j)
		{
			int temp = v[i];
			v[i] = v[j];
			v[j] = temp;
			i++;
			j--;
		}
	}
	if(i < high)
	{
		quickSort2(v, i, high);
	}
	if(j > low)
	{
		quickSort2(v, low, j);
	}
	

}
void mergeSort2(std::vector<int> &v, int low, int high)
{
	if(low < high)
	{
		int mid = (low + high) / 2;
		mergeSort2(v, low, mid);
		mergeSort2(v, mid + 1, high);
		merge2(v, low, mid, high);
	}
}
void merge2(std::vector<int> &v, int low, int mid, int high)
{
	int first = low;
	int second = mid;
	int first2 = mid + 1;
	int second2 = high;
	int firstNew = first;
	std::vector<int> temp (high + 1);
	while(first <= second and first2 <= second2)
	{
		if(v[first] <= v[first2])
		{
			temp[firstNew] = v[first];
			first++;
		}
		else
		{
			temp[firstNew] = v[first2];
			first2++;
		}
		firstNew++;
	}
	while(first <= second)
	{
		temp[firstNew] = v[first];
		first++;
		firstNew++;
	}
	while(first2 <= second2)
	{
		temp[firstNew] = v[first2];
		first2++;
		firstNew++;
	}
	for(int i = low; i <= high; i++)
	{
		v[i] = temp[i];
	}
}
void quickSort3(std::vector<int> &v, int left, int right)
{
	int i = left;
	int j = right;
	int pivot = v[(left + right) / 2];
	while (i <= j)
	{
		while(v[i] < pivot)
		{
			i++;
		}
		while(v[j] > pivot)
		{
			j--;
		}
		if(i <= j)
		{
			int temp = v[i];
			v[i] = v[j];
			v[j] = temp;
			i++;
			j--;
		}
	}
	if(i < right)
	{
		quickSort3(v, i, right);
	}
	if(j > left)
	{
		quickSort3(v, left, j);
	}
}
void mergeSort3(std::vector<int> &v, int low, int high)
{
	if(low < high)
	{
		int middle = (low + high) / 2;
		mergeSort3(v, low, middle);
		mergeSort3(v, middle + 1, high);
		merge3(v, low, middle, high);
	}
}
void merge3(std::vector<int> &v, int low, int mid, int high)
{
	std::vector<int> temp (high + 1);
	int first = low;
	int last = mid;
	int first2 = mid + 1;
	int last2 = high;
	int newFirst = first;
	while(first <= last and first2 <= last2)
	{
		if(v[first] <= v[first2])
		{
			temp[newFirst] = v[first];
			first++;
		}
		else
		{
			temp[newFirst] = v[first2];
			first2++;
		}
		newFirst++;
	}
	while(first <= last)
	{
		temp[newFirst] = v[first];
		first++;
		newFirst++;
	}
	while(first2 <= last2)
	{
		temp[newFirst] = v[first2];
		first2++;
		newFirst++;
	}
	for(int i = low; i <= high; i++)
	{
		v[i] = temp[i];
	}
}
string removeChars(string str, string rem)
{
	char ch[str.size() + 1], r[rem.size() + 1], newCh[str.size() + 1];// = str.c_str();
	strcpy(ch, str.c_str());
	strcpy(r, rem.c_str());
	int des = 0;

	bool b[128];
	for(int i = 0; i < rem.size(); i++ )
	{

		b[r[i]] = true;
		cout << b[r[i]] << endl;
	}
	for(int i = 0; i < str.size(); i++)
	{

		if(!b[ch[i]])
		{
			cout << b['d'] << endl;
			newCh[des++] = ch[i];
		}
	}
	cout << endl;
	for(int i = 0; i < strlen(newCh); i++)
	{
		cout << newCh[i];
	}
	/*b[0] = false;
	cout << b[0];
	for(int i = 0; i < 128; i++)
	{
		b[i] = false;
	}*/

}