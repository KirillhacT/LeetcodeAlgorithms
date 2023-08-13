#include <iostream>
#include <vector>

using namespace std;

void swap(int i, int j, vector<int>& heap)
{
    int tmp = heap[i];
    heap[i] = heap[j];
    heap[j] = tmp;
}


void print(vector<int>& heap) 
{
    for (int i = 0; i < heap.size(); i++)
    {
        cout << heap[i] << " ";
    } 
    cout << endl;
}

void shift_up(int i, vector<int>& heap)
{
    while (i > 0 && heap[i] > heap[(i - 1)/2])
    {
        swap(i, (i - 1) / 2, heap);
        i = (i - 1) / 2;
    }
}

void shift_down(int n, vector<int>& heap)
{
    int i = 0, j = 0;
    while (true)
    {
        for (int k = 1; k < 3; k++)
        {
            if ((2 * i) + k < n && heap[j] < heap[(2 * i) + k])
                j = (2 * i) + k;
        }
        if (i == j) break;
        swap(i, j, heap);
        i = j;
    }
}


int main()
{
    vector<int> nums = {3, 1, 5, 6, 2, 4, 1};

    for (int i = 0; i < nums.size(); i++)
    {
        shift_up(i, nums);
    }
    for (int n = nums.size()-1; n >= 0; n--)
    {
        swap(0, n, nums);
        shift_down(n, nums);
    }
    print(nums);
}