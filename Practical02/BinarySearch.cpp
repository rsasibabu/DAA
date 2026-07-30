#include <iostream>
using namespace std;

int main() {
    int n, key;

    cout << "Enter number of elements: ";
    cin >> n;

    int arr[n];

    cout << "Enter sorted array elements: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cout << "Enter element to search: ";
    cin >> key;

    int low = 0;
    int high = n - 1;
    int mid;
    int pos = -1;

    while (low <= high) {
        mid = (low + high) / 2;

        if (arr[mid] == key) {
            pos = mid;
            break;
        }
        else if (arr[mid] < key) {
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }

    if (pos != -1)
        cout << "Element found at index " << pos;
    else
        cout << "Element not found.";

    return 0;
}
