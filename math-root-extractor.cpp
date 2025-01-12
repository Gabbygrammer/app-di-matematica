#include <cmath>
#include <fstream>
#include <iostream>
using namespace std;
#include <string>
#include <vector>

vector<string> getPowersThatEqualInt(int number) {
    vector<string> powers;
    int limit = sqrt(number);
    for (int i = 2; i <= limit; i++) {
        int power = 0;
        while (number % i == 0) {
            number /= i;
            power += 1;
        }
        if (power > 1) {
            powers.push_back(to_string(i) + "^" + to_string(power));
        }
    }
    return powers;
}

vector<int> getPowerRemainders(int number, vector<string> powers) {
    vector<int> remainders;

    for (string power : powers) {
        size_t caretPos = power.find("^");
        int intBase = stoi(power.substr(0, caretPos));
        int intPower = stoi(power.substr(caretPos + 1));
        number /= pow(intBase, intPower);
    }

    for (int i = 2; i <= number; i++) {
        if (number % i == 0) {
            number /= i;
            remainders.push_back(i);
        }
    }
    return remainders;
}

struct outsideFactorStruct {
    int outsideFactorInt;
    std::vector<int> remainders;
};

outsideFactorStruct calculateOutsideFactor(vector<string> powers, vector<int> remainders) {
    outsideFactorStruct result;
    result.outsideFactorInt = 1;
    result.remainders.clear();

    for (string power : powers) {
        size_t caretPos = power.find("^");
        int intBase = stoi(power.substr(0, caretPos));
        int intPower = stoi(power.substr(caretPos + 1));
        
        while (intPower > 0) {
            if (intPower % 2 == 0) {
                result.outsideFactorInt *= intBase;
                intPower -= 2;
            } else if (intPower % 2 == 1) {
                if (intPower != 1) {
                    result.outsideFactorInt *= intBase;
                    intPower -= 2;
                } else {
                    result.remainders.push_back(intBase);
                    intPower -= 1;
                }
            }
        }
    }

    for (int remainder : remainders) {
        result.remainders.push_back(remainder);
    }

    return result;
}

int main(int argc, char **argv) {
    int number;
    number = atoi(argv[1]);

    // CODICE DI TEST
    // cout << "Powers: " << endl;
    // for (string power : getPowersThatEqualInt(number)) {
    //     cout << power << endl;
    // }
    // cout << "Remainders: " << endl;
    // for (int remainder : getPowerRemainders(number)) {
    //     cout << remainder << endl;
    // }

    vector<string> powers = getPowersThatEqualInt(number);
    vector<int> oldRemainders = getPowerRemainders(number, powers);
    
    auto s = calculateOutsideFactor(powers, oldRemainders);
    int outsideFactor = s.outsideFactorInt;
    vector<int> remainders = s.remainders;

    int remainingRoot = 1;

    for (int remainder : remainders) {
        remainingRoot *= remainder;
    }

    if (powers.empty()) {
        cout << "La radice estratta di " << number << " = sqrt(" << number << ")";

        return 0;
    }

    if (remainingRoot > 1) {
        cout << "La radice estratta di " << number << " = " << outsideFactor << " * sqrt(" << remainingRoot << ")";
    } else {
        cout << "La radice estratta di " << number << " = " << outsideFactor;
    }

    return 0;
}