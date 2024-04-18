// Advent 03b
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char ** argv) {
    std::ifstream input {argv[1]};

    // 10 Load all rows into vector
    // 20 Calculate most / least common first bit
    // 30 loop through data set, saving most common bits to O2 gen vector
    // 35 loop through data set, saving least common bits to CO2 Scrubber vector
    // 40 loop through each vector calculating the values for second bit
    // 50 Trim vectors by throwing out their
    // if vector length > 1; goto 10
    // last value = OXGen Value

    // 20 calculate least common first bit
    // 30 loop through vector, saving only matching first bits into new vector
    // if vector length > 1; goto 10
    // last value = CO2 Scrubber

    // Shuffle these two algorithms and process them at the same time.

    return 0;
}
