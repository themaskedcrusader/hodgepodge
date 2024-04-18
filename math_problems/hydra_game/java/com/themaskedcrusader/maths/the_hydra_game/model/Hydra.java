package com.themaskedcrusader.maths.the_hydra_game.model;

public class Hydra {
    Node head;
    Node tail;

    public Hydra(int length) {
        this.head = new Node(1);
        Node node1 = head;
        Node node2 = null;
        for (int i = 1; i < length; i++) {
            node2 = new Node(1);
            node1.next = node2;
            node2.previous = node1;
            node1 = node2;
        }

        tail = node2;
    }

    public boolean areAllHeadsAlone() {
        Node node = head;
        while (node != null) {
            if (node.heads != 1) return false;
            node = node.next;
        }
        return true;
    }

    public void removeHead(Node headNode) {
        Counter.steps++;
        Node parent = headNode.next;
        headNode.heads--;
        if (parent != null) {
            parent.heads += Counter.steps;
        }
    }

    public Node getHead() {
        return head;
    }

    public Node getHeadWithMostHeads() {
        Node checkNode = head;
        Node withMostHeads = null;
        int mostHeadsCount = 0;
        while (checkNode != null) {
            if (checkNode.heads > mostHeadsCount) {
                mostHeadsCount = checkNode.heads;
                withMostHeads = checkNode;
            }
            checkNode = checkNode.next;
        }
        return withMostHeads;
    }

    public void lopHead() {
        if (head == tail) {
            head = null;
            tail = null;
            return;
        }

        Counter.steps++;

        if (head.heads != 1) {
            System.err.println("Can't lop a head with remaining heads");
            System.exit(1);
        }
        Node newHead = head.next;
        newHead.previous = null;
        head = newHead;
        Node next = head.next;
        if (next != null) {
            next.heads += Counter.steps;
        }
    }

    public boolean hasHeads() {
        return head != null && tail != null;
    }
}
