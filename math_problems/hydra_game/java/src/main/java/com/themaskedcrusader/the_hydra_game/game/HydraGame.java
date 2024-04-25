package com.themaskedcrusader.the_hydra_game.game;

import com.themaskedcrusader.the_hydra_game.model.CounterModel;
import com.themaskedcrusader.the_hydra_game.model.HydraModel;

public class HydraGame {

    public void playGame() {
        CounterModel counter = new CounterModel();
        int initialHeads = 6;

        HydraModel hydra = new HydraModel(initialHeads);

        while (hydra.hasHeads()) {
            if (hydra.areAllHeadsAtOne()) {
                hydra.lopHead(counter);
            } else {
                hydra.removeRightMostHead(counter);
            }
        }

        counter.addStep();
        System.out.println("Steps: " + counter.getSteps());
    }
}
