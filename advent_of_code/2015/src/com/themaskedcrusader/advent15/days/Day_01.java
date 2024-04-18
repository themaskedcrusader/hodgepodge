package com.themaskedcrusader.advent15.days;

import java.io.File;

public class Day_01 extends AdventDay {
    String problem = "day_1";

    @Override
    public void execute(File directory) {
        String input = utils.get_first_line(directory, problem);
        partOne(input);
        partTwo(input);
    }

    private void partOne(String input) {
        // Since this is simple math, the answer is the sum of ('s minus the sum of )'s
        long up   = input.chars().filter(c -> c == '(').count();
        long down = input.chars().filter(c -> c == ')').count();
        System.out.println("The instructions take Santa to floor " + (up - down));
    }

    private void partTwo(String input) {
        // A little harder, we have to count each character at a time and find the first time it goes negative
        int floor = 0;
        char[] charArray = input.toCharArray();
        for (int i = 1; i <= charArray.length; i++) {
            if (charArray[i-1] == '(') {
                floor++;
            } else if (charArray[i-1] == ')') {
                floor--;
            }
            if (floor < 0) {
                System.out.println("Santa entered the basement on position " + i);
                return;
            }
        }
    }
}
