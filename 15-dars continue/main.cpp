#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    cin >> n;
    string pattern;

    for (int i = n / 2; i < n; i += 2) {
        for (int j = 1; j < n - i; j += 2) {
            pattern += " ";
        }
        for (int j = 1; j <= i; j++) {
            pattern += "*";
        }
        for (int j = 1; j <= n - i; j++) {
            pattern += " ";
        }
        for (int j = 1; j <= i; j++) {
            pattern += "*";
        }
        pattern += "\n";
    }

    for (int i = n; i > 0; i--) {
        for (int j = 0; j < n - i; j++) {
            pattern += " ";
        }
        for (int j = 1; j < i * 2; j++) {
            pattern += "*";
        }
        pattern += "\n";
    }

    cout << pattern;

    return 0;
}
