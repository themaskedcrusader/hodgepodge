package com.themaskedcrusader.advent15.days;

import java.awt.*;
import java.io.File;
import java.util.HashMap;

public class Day_03 extends AdventDay {
    String problem = "day_3";

    @Override
    public void execute(File directory) {
        String input = utils.get_first_line(directory, problem);
        partOne(input);
        partTwo(input);
    }

    void partOne(String input) {
        Point santa = new Point(0,0);
        HashMap<String, Boolean> visits = new HashMap<>();
        visits.put(getPointCoords(santa), true);
        for (Character move : input.toCharArray()) {
            movePoint(santa, move);
            visits.put(getPointCoords(santa), true);
        }

        System.out.println("Part 1: Number of unique visits : " + visits.size());
    }

    void partTwo(String input) {
        Point santa = new Point(0,0 );
        Point robot = new Point(0,0 );
        HashMap<String, Boolean> visits = new HashMap<>();
        visits.put(getPointCoords(santa), true);
        int who = 0;
        for (Character move : input.toCharArray()) {
            if (who % 2 == 0) {
                moveAndRecord(santa, move, visits);
            } else {
                moveAndRecord(robot, move, visits);
            }
            who++;
        }
        System.out.println("Part 2: Number of unique visits : " + visits.size());
    }

    void movePoint(Point point, char move) {
        int dx = 0;
        int dy = 0;
        switch (move) {
            case '>' : dx++; break;
            case '<' : dx--; break;
            case '^' : dy++; break;
            case 'v' : dy--; break;
        }
        point.translate(dx, dy);
    }

    void moveAndRecord(Point point, char move, HashMap<String, Boolean> visits) {
        movePoint(point, move);
        visits.put(getPointCoords(point), true);
    }

    String getPointCoords(Point point) {
        return "" + point.x + "," + point.y;
    }
}
