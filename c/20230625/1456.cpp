#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    double arr[n];
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    int max_num = arr[0];
    for (int i = 0; i < n; i++)
    {
        if (arr[i + 1] > max_num)
        {
            max_num = arr[i + 1];
        }
    }
    double sum = 0;

    for (int i = 0; i < n; i++)
        sum += (arr[i] / max_num * 100);

    cout << sum / double(n) << endl;
}