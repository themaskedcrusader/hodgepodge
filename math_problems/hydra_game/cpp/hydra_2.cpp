#include <iostream>

struct node {
    unsigned long long int heads = 1;
    node *next;
    node *prev;
};

struct run_info {
    unsigned long long int steps = 0;
};

void insert_at_front(node** head, int heads) {
    node* new_node = new node();
    new_node->heads = heads;

    new_node->next = (*head);
    if (*head != nullptr) {
        (*head)->prev = new_node;
    }

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

void lop_head(node** head, run_info *counter) {
    if ((*head)->heads != 1) {
        std::cout << "CANNOT LOP HEAD" << std::endl;
        exit(2);
    }

    node* new_head = (*head)->next;
    delete (*head);
    if (new_head != nullptr) {
        (*head) = new_head;
        if ((*head)->next != nullptr) {
            (*head)->next->heads += ++counter->steps;
        }
        (*head)->prev = nullptr;
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

void remove_head(node** n, run_info *counter) {
    node* parent = (*n)->next;
    if (parent == nullptr) {
        unsigned long long int child_heads = 0;
        node* child_node = (*n)->prev;
        while (child_node != nullptr) {
            if (child_node->heads > child_heads) {
                child_heads = child_node->heads;
            }
            child_node = child_node->prev;
        }

        unsigned long long int heads_to_chop = (*n)->heads - child_heads;
        counter->steps += heads_to_chop;
        (*n)->heads = (*n)->heads - heads_to_chop;
    } else {
        (*n)->heads--;
        counter->steps++;
        parent->heads += counter->steps;
    }
}

bool has_heads(node node1) {
    return node1.next != nullptr;
}

int main() {
    run_info steps = run_info();
    unsigned long long int previous_steps = 0;
    int length = 5;

    node *head = nullptr;

    for (int i = 0; i <= length; i++) {
        insert_at_front(&head, 1);
    }

    while (has_heads(*head)) {
        if (are_all_heads_one(&head)) {
            lop_head(&head, &steps);
        } else {
            node* withMostHeads = get_node_with_most_heads(&head);
            remove_head(&withMostHeads, &steps);
        }
        if (steps.steps < previous_steps) {
            std::cout << "overflow" << std::endl;
            exit(3);
        }
        previous_steps = steps.steps;

    }

    std::cout << "steps: " << ++steps.steps << std::endl;

    return 0;
}

// Refactored the code from hydra.cpp so that if we're lopping off heads on the lowest stump
// (heads that won't grow new heads), we don't actually loop, we just count how many heads we
// can lop off before we have to go to another level and add heads. This is very fast, and we
// overflow the unsigned long long int steps very quickly...
//
// Overflows step counter after lopping off 12682198123326472190 heads