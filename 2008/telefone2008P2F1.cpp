#include <bits/stdc++.h>
using namespace std;

int main(){
    string cods = "2223334445556667778889999";
    
    string alphanum;
    cin >> alphanum;

    string response;

    for (char i : alphanum){
        if (i >= 'A' && i <= 'Z') {
            size_t index = static_cast<size_t>(i - 'A');
            response.push_back(cods[index]);
        } else {
            response.push_back(i);
        }
    }

    cout << response << endl;

    return 0;
}