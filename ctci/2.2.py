class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def sol(head, k):
	leader = head
	follower = head
	for _ in range(k):
		leader = leader.next

	while leader.next is not None:
		leader = leader.next
		follower = follower.next

	return follower