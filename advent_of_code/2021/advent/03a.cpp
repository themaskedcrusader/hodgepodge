// Advent 03a
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char ** argv) {
    std::ifstream input {argv[1]};
    std::string row;

    input >> row;

    int ones[12] = {0};
    int zero[12] = {0};

    // calculate most common bits of input
    do {
        for( int i = 0; i < row.length() ; i++) {
            if (row[i] == '1') {
                ones[i]++;
            } else {
                zero[i]++;
            }
        }
    } while (input >> row);

    // process data into gamma rate and epsilon rate
    std::string gamma;
    std::string epsilon;

    for (int i = 0; i < 12; i++) {
        int o = ones[i];
        int z = zero[i];

        if (o > z) {
            gamma.append("1");
            epsilon.append("0");
        } else {
            gamma.append("0");
            epsilon.append("1");
        }
    }

    // convert binary values into integers
    int i_gamma = stoi(gamma,0, 2);
    int i_epsilon = stoi(epsilon, 0, 2);

    // Calculate answer
    cout << "Gamma " << i_gamma << " | epsilon " << i_epsilon << endl;
    cout << "Power Consumption " << i_gamma * i_epsilon << endl;

    return 0;
}