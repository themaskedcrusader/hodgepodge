package com.themaskedcrusader.advent15.days;

import com.themaskedcrusader.advent15.util.AdventUtils;

import java.io.File;

public abstract class AdventDay {
    AdventUtils utils = new AdventUtils();

    public abstract void execute(File directory);
}
