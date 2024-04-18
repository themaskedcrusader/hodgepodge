// Created by cschalk on 3/21/16.
// Challenge 19 : Bit Positions
#include <iostream>
#include <fstream>
using namespace std;

int getBit(int val, int bit) {
  return (val & (1 << bit)) >> bit;
}

bool bitPositions(int input, int pos1, int pos2) {
  return getBit(input, pos1 - 1) == getBit(input, pos2 - 1);
}

int main(int argc, char ** argv) {
  std::ifstream inFile {argv[1]};
  int digit, bitPosition1, bitPosition2;
  char gulp;
  while (inFile >> digit >> gulp >> bitPosition1 >> gulp >> bitPosition2){
    if (bitPositions(digit, bitPosition1, bitPosition2)) {
      std::cout << "true" << std::endl;
    } else {
      std::cout << "false" << std::endl;
    }
  }
  return 0;
}
