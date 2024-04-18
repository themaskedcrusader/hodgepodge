package com.themaskedcrusader.advent15.days;

import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;

public class Day_02 extends AdventDay {
    String problem = "day_2";

    @Override
    public void execute(File directory) {
        ArrayList<String> input = utils.getInputArray(directory, problem);
        partOne(input);
        partTwo(input);
    }

    private void partOne(ArrayList<String> input) {
        int totalSurfaceArea = 0;
        for (String info : input) {
            Box b = new Box(info);
            totalSurfaceArea += b.getRequiredWrappingPaper();
        }

        System.out.println("Total square feet required : " + totalSurfaceArea);
    }

    private void partTwo(ArrayList<String> input) {
        int totalRibbonLength = 0;
        for (String info : input) {
            Box b = new Box(info);
            totalRibbonLength += b.getRequireRibbonLength() + b.getRequireBowRibbonLength();
        }

        System.out.println("Total ribbon length required : " + totalRibbonLength);

    }

}

class Box{
    private int length;
    private int width;
    private int height;

    Box(String dimensions) {
        String[] d = dimensions.split("x");
        length = Integer.parseInt(d[0]);
        width  = Integer.parseInt(d[1]);
        height = Integer.parseInt(d[2]);
    }

    int getRequiredWrappingPaper() {
        int[] sideArea = new int[3];
        sideArea[0] = length * width;
        sideArea[1] = width  * height;
        sideArea[2] = length * height;
        Arrays.sort(sideArea);
        return sideArea[0] + 2 * (sideArea[0] + sideArea[1] + sideArea[2]);
    }

    int getRequireRibbonLength() {
        int[] sizes = new int[3];
        sizes[0] = length;
        sizes[1] = width;
        sizes[2] = height;
        Arrays.sort(sizes);
        return 2 * (sizes[0] + sizes[1]);
    }

    int getRequireBowRibbonLength() {
        return length * width * height;
    }

}