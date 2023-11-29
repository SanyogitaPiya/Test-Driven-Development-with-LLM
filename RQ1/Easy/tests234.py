
def test_palindrome_odd_nodes(self):
        # The code works. GIve me test cases for the code
        # Create a palindrome linked list with odd number of nodes
        head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(2)
        node5 = ListNode(1)
        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        # Initialize the class object
        solution = Solution()

        # Invoke the method 'isPalindrome'
        result = solution.isPalindrome(head)

        # Check if the result is True
        assert result == True