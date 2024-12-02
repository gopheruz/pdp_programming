#include <iostream>
using namespace std;
int main(){
    for(int i = 1; i < 1000; i++){
        int k = i;
        int summa = 0;
        while (k > 0)
        {
            int qoldiq = k % 10;
            summa += qoldiq;
            if (summa > 15){
                break;
            }
            k /= 10;
        }
        if (summa == 15){
            cout << i << endl;
        }
    }
    return 0;
}