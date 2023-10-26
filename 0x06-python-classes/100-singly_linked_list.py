#!/usr/bin/python3
"""Write a class Node that defines a node of a singly linked list,
And, write a class SinglyLinkedList that defines a singly linked list"""


class Node:
    """class that defines a node of a linked list"""
    def __init__(self, data, next_node=None):
        """initializes the private attributes of a Node instance"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """retrieves the data of the linked list"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets the value of the linked list"""
        if not isinstance(self.__data, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """retrieves the next node of a linked list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the next node of list to value given"""
        if not (isinstance(value, Node) or value is None):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """class that defines a singly-linked list"""
    def __init__(self):
        """initializes the list"""
        self.__head = None

    def __str__(self):
        """prints to stdout values of data in list"""
        list_data = []
        temp = self.__head
        while temp is not None:
            list_data.append("{:d}".format(temp.data))
            temp = temp.next_node
        return "\n".join(list_data)

    def sorted_insert(self, value):
        """sorts the list in increasing order"""
        temp = self.__head
        new_node = Node(value)
        if temp is None:
            self.__head = new_node
            return
        if temp.data >= value:
            new_node.next_node = temp
            self.__head = new_node
            return

        while temp.next_node is not None and value > temp.next_node.data:
            temp = temp.next_node
        new_node.next_node = temp.next_node
        temp.next_node = new_node
