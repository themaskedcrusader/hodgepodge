// Advent 01a
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char ** argv) {
    std::ifstream input {argv[1]};
    int increases = 0, depth_next, depth_previous = -1;

    while (input >> depth_next) {
        if (depth_previous != -1) {
            if (depth_previous < depth_next) {
                increases++;
            }
        }
        depth_previous = depth_next;
    }

    cout << "Number of increases :: " << increases << endl;

    return 0;
}