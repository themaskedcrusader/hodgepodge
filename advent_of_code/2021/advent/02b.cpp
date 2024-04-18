// Advent 02b
#include <iostream>
#include <fstream>

using namespace std;

int horizontal = 0;
int depth = 0;
int aim = 0;

int main(int argc, char ** argv) {
    std::ifstream input {argv[1]};
    std::string command;
    int value;

    while (input >> command >> value) {
        if (command == "forward") {
            horizontal += value;
            depth += value * aim;
        }

        if (command == "up") {
            aim -= value;
        }

        if (command == "down") {
            aim += value;
        }
    }

    cout << "Forward " << horizontal << " | depth " << depth << endl;
    cout << "Answer " << horizontal * depth << endl;

    return 0;
}