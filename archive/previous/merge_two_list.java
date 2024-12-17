/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
// class Solution {
//     public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
//         ListNode outputNode = new ListNode(0);
//         ListNode tail= outputNode;
//         while ((list1.next != null) && (list2.next != null)) {
//         if(list1.val > list2.val){
//             list.add(list1.val);
//         }
//         else if (list1.val < list2.val) {
//             list.add(list2.val);
//         }
//         else if (list1.val == list2.val) {
//             list.add(list1.val);
//             list.add(list2.val);
//         }
//         list1 = list1.next ;
//         list2 = list2.next ;

//     }
//     if (list1.next == null){
//         while (list2.next != null){
//             list.add(list2.val);
//             list2 = list2.next ;
//         }
//     }
//     else if (list2.next == null){
//         while (list1.next != null){
//             list.add(list1.val);
//             list1 = list1.next ;
//         }
    
//     }
//     return list;
//     }

// }
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode outputNode = new ListNode(0);
        ListNode tail= outputNode;
        while(list1 != null && list2 != null){
            if(list1.val < list2.val){
                tail.next = list1;
                list1 = list1.next;
            }else{
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;
        }
        if(list1 == null&& list2 != null){
            tail.next = list2;
            list2 = list2.next;
             
        }
        if(list1 != null&& list2 == null){
            tail.next = list1;
            list1 = list1.next;
           
        }
        return outputNode.next;
                
    }
}
