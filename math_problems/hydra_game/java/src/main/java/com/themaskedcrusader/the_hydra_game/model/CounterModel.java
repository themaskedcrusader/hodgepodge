package com.themaskedcrusader.the_hydra_game.model;

import java.math.BigInteger;

public class CounterModel {
    private BigInteger steps = BigInteger.ZERO;

    public String getSteps() {
        return steps.toString();
    }

    public void setSteps(BigInteger steps) {
        this.steps = steps;
    }

    public void addStep() {
        this.steps = steps.add(BigInteger.ONE);
    }

    public void addSteps(BigInteger steps) {
        this.steps = this.steps.add(steps);
    }
}
