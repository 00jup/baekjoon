#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    double arr[n];
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    int max_num;
    max_num = max(arr[0], arr[n - 1]);

    double sum = 0;

    for (int i = 0; i < n; i++)
        sum += (arr[i] / max_num * 100);

    cout << sum / n << endl;
}