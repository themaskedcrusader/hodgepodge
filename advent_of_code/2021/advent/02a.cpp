// Advent 02a
#include <iostream>
#include <fstream>

using namespace std;

int horizontal = 0;
int depth = 0;

int main(int argc, char ** argv) {
    std::ifstream input {argv[1]};
    std::string command;
    int value;

    while (input >> command >> value) {
        if (command == "forward") {
            horizontal += value;
        }

        if (command == "up") {
            depth -= value;
        }

        if (command == "down") {
            depth += value;
        }
    }

    cout << "Forward " << horizontal << " | depth " << depth << endl;
    cout << "Answer " << horizontal * depth << endl;

    return 0;
}