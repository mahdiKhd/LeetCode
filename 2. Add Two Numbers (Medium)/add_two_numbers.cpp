#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
  public:
      ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
          ListNode* answer = new ListNode(0);
          ListNode* temp = answer;
          int carry = 0;

          while (l1 != nullptr || l2 != nullptr || carry) {
            int l1Value = (l1 != nullptr)? l1->val: 0;
            int l2Value = (l2 != nullptr)? l2->val: 0;
            int sum = l1Value + l2Value + carry;

            carry = (sum > 9)? 1: 0;
            temp->next = new ListNode(sum - 10*carry);
            temp = temp->next;

            if (l1 != nullptr) l1 = l1->next;
            if (l2 != nullptr) l2 = l2->next;
          }
          return answer->next;
      }
  };


void printList(ListNode* node) {
    while (node != nullptr) {
        cout << node->val;
        if (node->next != nullptr) cout << " -> ";
        node = node->next;
    }
    cout << endl;
}
// Main function for testing
int main() {
    // Create first number: 2 -> 4 -> 3 (342)
    ListNode* l1 = new ListNode(2, new ListNode(4, new ListNode(3)));
    
    // Create second number: 5 -> 6 -> 4 (465)
    ListNode* l2 = new ListNode(5, new ListNode(6, new ListNode(4)));
    
    Solution solution;
    ListNode* result = solution.addTwoNumbers(l1, l2);
    
    // Output the result: should be 7 -> 0 -> 8
    printList(result);

    return 0;
}