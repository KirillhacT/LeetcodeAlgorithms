#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <vector>

using namespace std;


int random(int min, int max)
{
    int num = min + rand() % (max - min + 1);
    return num;
}

void swap(vector<int>& arr, int x, int y)
{
    int tmp = arr[x];
    arr[x] = arr[y];
    arr[y] = tmp;
}

void print(vector<int>& heap) 
{
    for (int i = 0; i < heap.size(); i++)
    {
        cout << heap[i] << " ";
    } 
    cout << endl;
}

void quicksort(vector<int>& arr, int left, int right)
{
    //quicksort without repeating characters
    if (right - left <= 1)
        return; 
    int random_num = random(left, right);
    // cout << random_num << endl;
    int pivot = arr[random_num];
    int middle = left;

    for (int i = left; i < right; i++)
    {
        if (arr[i] < pivot)
        {
            swap(arr, i, middle);
            middle++;
        }
    }
    quicksort(arr, left, middle);
    quicksort(arr, middle, right);
}

int main()
{
    vector<int> arr = {7, 1, 3, 8, 4, 5};
    quicksort(arr, 0, arr.size());
    print(arr);
}