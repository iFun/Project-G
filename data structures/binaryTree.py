class Node():
    """LinkedList node class"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    def __str__(self):
        """Override the default print behavior"""
        if self.next is not None:
            return (str(self.value) + ' -->')
        return str(self.value)

    def __eq__(self, other):
        """Override the default Equals behavior"""
        return self.value == other.value


class BinaryTree():
	"""docstring for ArrayList"""
	def __init__(self):
		self.__array = 
		