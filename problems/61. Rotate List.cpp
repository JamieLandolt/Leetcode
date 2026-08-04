/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head) {
            return head;
        }
        
        int len = 0;
        ListNode* curr = head;
        ListNode* prev;
        while (curr) {
            prev = curr;
            curr = curr->next;
            len++;
        }

        ListNode* last = prev;
        k %= len;
        curr = head;
        for (int i = 1; i < len - k; i++) {
            curr = curr->next;
        }

        if (k != 0) {
            cout << last->val << "|" << head->val << "\n";
            last->next = head;
            cout << curr->val;
            head = curr->next;
            curr->next = nullptr;
        }
        
        return head;
    }
};
