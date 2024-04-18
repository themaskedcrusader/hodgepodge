#include <iostream>

struct node {
    unsigned int heads = 1;
    node *next;
};

void insert_at_front(node** head, int heads) {
    node* new_node = new node();
    new_node->heads = heads;

    new_node->next = (*head);

    (*head) = new_node;
}

bool are_all_heads_one(node** head) {
    auto check_node = (*head);
    while (check_node != nullptr) {
        if (check_node->heads != 1) return false;
        check_node = check_node->next;
    }
    return true;
}

void lop_head(node** head, int counter) {
    if ((*head)->heads != 1) {
        std::cout << "CANNOT LOP HEAD" << std::endl;
        exit(2);
    }

    node* new_head = (*head)->next;
    if (new_head != nullptr) {
        free(*head);
        (*head) = new_head;
        if ((*head)->next != nullptr) {
            (*head)->next->heads += counter;
        }
    }
}

node* get_node_with_most_heads(node** head) {
    auto check_node = (*head);
    node *withMostHeads;
    int mostHeadsCount = 0;
    while (check_node != nullptr) {
        if (check_node->heads > mostHeadsCount) {
            mostHeadsCount = check_node->heads;
            withMostHeads = check_node;
        }
        check_node = check_node->next;
    }
    return withMostHeads;
}

void remove_head(node** n, int counter) {
    node* parent = (*n)->next;
    (*n)->heads--;
    if (parent != nullptr) {
        parent->heads += counter;
    }
}

bool has_heads(node node1) {
    return node1.next != nullptr;
}

int main() {
    unsigned int steps = 0;
    unsigned int previous_steps;
    int length = 5;

    node *head = nullptr;

    for (int i = 0; i <= length; i++) {
        insert_at_front(&head, 1);
    }

    while (has_heads(*head)) {
        if (are_all_heads_one(&head)) {
            steps++;
            lop_head(&head, steps);
        } else {
            steps++;
            node* withMostHeads = get_node_with_most_heads(&head);
            remove_head(&withMostHeads, steps);
        }
        if (steps < previous_steps) {
            std::cout << "overflow" << std::endl;
            exit(3);
        }
        previous_steps = steps;

    }

    std::cout << "steps: " << steps << std::endl;

    return 0;
}
