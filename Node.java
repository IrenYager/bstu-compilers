public class Node {
    String data;
    Node next;
    Node previous;

    public Node() {

    }

    public Node(String data) {
        this.data = data;
        next = null;
        previous = null;
    }

    public Node(Node aPrev, Node aNext, String data) {
        this.data = data;
        next = aNext;
        previous = aPrev;
    }
}

