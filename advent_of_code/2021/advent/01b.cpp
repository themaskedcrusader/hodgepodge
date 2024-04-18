// Advent 01b
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char ** argv) {
    std::ifstream input {argv[1]};
    int increases = -1, depth1, depth2 = -1, depth3 = -1, sum_previous = 0;

    while (input >> depth1) {
        if (depth3 != -1) {
            auto sum_next = depth1 + depth2 + depth3;
            if (sum_previous < sum_next) {
                increases++;
            }
            sum_previous = sum_next;
        }
        depth3 = depth2;
        depth2 = depth1;
    }

    cout << "Number of increases :: " << increases << endl;

    return 0;
}