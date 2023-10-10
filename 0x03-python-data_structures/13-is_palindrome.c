#include "lists.h"

/**
 * reverse_list - reverse a singly-linked list
 * @head: pointer to the head pointer
 *
 * Return: new head pointer
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *curr_node, *prev_node, *next_node;

    if (*head == NULL)
        return (NULL);

	curr_node = *head;
	prev_node = next_node = NULL;
	while (curr_node != NULL)
	{
		next_node = curr_node->next;
		curr_node->next = prev_node;
		prev_node = curr_node;
		curr_node = next_node;
	}
	*head = prev_node;
	return (*head);
}

/**
 * compare_lists - compares two lists
 * @first: pointer to the first pointer
 * @second: pointer to the second pointer
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int compare_lists(listint_t **first, listint_t **second)
{
    if (!first || !second)
        return (0);

	while ((*first)->next != NULL)
	{
		if ((*first)->n != (*second)->n)
		{
			return (0); /*not a palindrome*/
		}
		*first = (*first)->next;
		*second = (*second)->next;
	}
	return (1);
}

/**
 * is_palindrome - checks if a singly-linked list is a palindrome
 * @head: pointer to the head pointer
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int palindrome;
	/*traverse list*/
	listint_t *slow_node, *fast_node, *prev_node, *second_half;
	/*list with one or zero node is a palindrome*/
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	/*use fast_node and slow_node pointers to find middle of list*/
	slow_node = fast_node = *head;
	while (fast_node != NULL && fast_node->next != NULL)
	{
		prev_node = slow_node;
		fast_node = fast_node->next->next;
		slow_node = slow_node->next;
	}
	/*slow_node is at the middle position; so break first half*/
	prev_node->next = NULL;
	/*reverse the second half of the list*/
	second_half = reverse_list(&slow_node);
	/*compare both lists; (i.e first half and second half)*/
	palindrome = compare_lists(head, &second_half);

	return (palindrome);
}
