package com.themaskedcrusader.the_hydra_game.model;

import java.math.BigInteger;

public class HydraModel {
    private NodeModel topHead;

    public HydraModel(int heads) {
        NodeModel node = new NodeModel(1);
        for (int i = 1; i < heads; i++) {
            NodeModel nextHead = new NodeModel(1);
            node.setNext(nextHead);
            nextHead.setPrevious(node);
            node = nextHead;
        }
        topHead = getTopHead(node);
    }

    private NodeModel getTopHead(NodeModel node) {
        while (node.getPrevious() != null) {
            node = node.getPrevious();
        }
        return node;
    }

    public boolean areAllHeadsAtOne() {
        NodeModel checkNode = topHead;
        while (checkNode != null) {
            if (!checkNode.getHeads().equals(BigInteger.ONE)) {
                return false;
            }
            checkNode = checkNode.getNext();
        }
        return true;
    }

    public void lopHead(CounterModel counter) {
        if (!topHead.getHeads().equals(BigInteger.ONE)) {
            System.err.println("Cannot Lop Head!");
            System.exit(2);
        }

        NodeModel newHead = topHead.getNext();
        if (newHead != null) {
            if (newHead.getNext() != null) {
                counter.addStep();
                newHead.getNext().addHeads(new BigInteger(counter.getSteps()));
            }
            newHead.setPrevious(null);
            topHead = newHead;
        }
    }

    public boolean hasHeads() {
        return topHead.getNext() != null;
    }

    private NodeModel getNodeWithMostHeads() {
        NodeModel checkNode = topHead;
        NodeModel ret = null;
        BigInteger mostHeads = BigInteger.ZERO;

        while (checkNode != null) {
            if (mostHeads.compareTo(checkNode.getHeads()) < 0) {
                mostHeads = new BigInteger(checkNode.getHeads().toString());
                ret = checkNode;
            }
            checkNode = checkNode.getNext();
        }
        return ret;
    }

    public void removeRightMostHead(CounterModel counter) {
        // Right Most Head is defined as the highest numbered head on the node with the most nodes. This may not
        // match the actual right-most-head as described in the YouTube video, but it is how I've chosen to define it

        NodeModel nodeWithMostHeads = getNodeWithMostHeads();
        NodeModel parent = nodeWithMostHeads.getNext();
        if (parent == null) {
            BigInteger childHeads = BigInteger.ZERO;
            NodeModel childNode = nodeWithMostHeads.getPrevious();
            while (childNode != null) {
                if (childHeads.compareTo(new BigInteger(childNode.getHeads().toString())) < 0) {
                    childHeads = childNode.getHeads();
                }
                childNode = childNode.getPrevious();
            }
            BigInteger headsToChop = nodeWithMostHeads.getHeads().subtract(childHeads);
            counter.addSteps(headsToChop);
            nodeWithMostHeads.removeHeads(headsToChop);

        } else {
            nodeWithMostHeads.removeHead();
            counter.addStep();
            parent.addHeads(new BigInteger(counter.getSteps()));
        }
    }
}
