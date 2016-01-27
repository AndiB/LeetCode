/*
Difficulty: Easy
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/* Note, no access to beginning of linked list */
void deleteNode(struct ListNode* node) {
    //shift left until we reach the end
    while (node->next->next != NULL) { 
        node->val = node->next->val;
        node = node->next;
    }
    node->val = node->next->val ;
    node->next = NULL;
}   
