package com.themaskedcrusader.the_hydra_game.model;

import java.math.BigInteger;

public class NodeModel {
    private BigInteger heads = BigInteger.ZERO;
    private NodeModel next;
    private NodeModel previous;

    public NodeModel(int heads) {
        this.heads = new BigInteger("" + heads);
    }

    public void setNext(NodeModel next) {
        this.next = next;
    }

    public void setPrevious(NodeModel previous) {
        this.previous = previous;
    }

    public BigInteger getHeads() {
        return heads;
    }

    public NodeModel getNext() {
        return next;
    }

    public NodeModel getPrevious() {
        return previous;
    }

    public void addHeads(BigInteger heads) {
        this.heads = this.heads.add(heads);
    }

    public void removeHead() {
        heads = heads.subtract(BigInteger.ONE);
    }

    public void removeHeads(BigInteger headsToChop) {
        this.heads = this.heads.subtract(headsToChop);
    }
}
