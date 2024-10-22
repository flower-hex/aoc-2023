#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int calibrator(string file_name){
    string rawtxt;
    ifstream rawfile(file_name);

    unsigned long long running_total = 0;
    int l_int;
    int r_int;
    while (getline(rawfile, rawtxt)){
        l_int = 0;
        r_int = 0;
        for (char c : rawtxt) {
            if ((c <= '9') and (c >= '1')){
                if (l_int == 0) l_int = static_cast<int>(c-48);
                r_int = static_cast<int>(c-48);
            };
        }
        running_total += (l_int * 10) + r_int;
        // cout << l_int << r_int << endl;
    }
    return running_total;
}

int main() {
    if (calibrator("example") == 142){
        cout << "passed testing" << endl << "solution should be " << calibrator("input") << endl;
    };
}
