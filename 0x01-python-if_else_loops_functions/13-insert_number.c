#include "lists.h"

/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head: pointer to the head-node pointer
 * @number: number to be inserted
 *
 * Return: address of new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp, *current;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	temp = *head;
	while (temp && temp->n < number)
	{
            current = temp;
            temp = temp->next;
	}
	current->next = new_node;
    new_node->next = temp;
	return (new_node);
}
