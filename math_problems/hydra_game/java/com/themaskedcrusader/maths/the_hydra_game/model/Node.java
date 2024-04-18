package com.themaskedcrusader.maths.the_hydra_game.model;

public class Node {
    int heads;
    Node previous;
    Node next;

    public Node(int heads) {
        this.heads = heads;
        previous = null;
        next = null;
    }
}
