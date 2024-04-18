package com.themaskedcrusader.maths.the_hydra_game.game;

import com.themaskedcrusader.maths.the_hydra_game.model.Counter;
import com.themaskedcrusader.maths.the_hydra_game.model.Hydra;
import com.themaskedcrusader.maths.the_hydra_game.model.Node;

public class TheHydraGame {


    public void play() {

        Hydra hydra = new Hydra(Counter.length);

        while (hydra.hasHeads()) {
            if (hydra.areAllHeadsAlone()) {
                hydra.lopHead();
            } else {
                Node headWithMostHeads = hydra.getHeadWithMostHeads();
                hydra.removeHead(headWithMostHeads);
            }
            if (Counter.steps < 0) {
                System.err.println("overflow");
                System.exit(2);
            }
        }

        System.out.println("Number of steps = " + Counter.steps);

        boolean pause = true;
    }
}
