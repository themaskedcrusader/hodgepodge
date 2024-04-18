package com.themaskedcrusader.advent15;

import com.themaskedcrusader.advent15.days.*;

import java.io.File;

public class Main {

    private static void usage() {
        System.out.println("Usage Note: First parameter must be the full path to the input directory");
        System.out.println("The input file must be named: day_<number>.txt");
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            usage();
        } else {
            File inputDirectory = new File(args[0]);
//            new Day_01().execute(inputDirectory);
//            new Day_02().execute(inputDirectory);
//            new Day_03().execute(inputDirectory);
            new Day_04().execute(inputDirectory);
        }
    }
}
