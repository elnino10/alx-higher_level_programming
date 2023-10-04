#include "lists.h"

/**
 * check_cycle - checks if list contains a cycle
 * @list: pointer to list
 *
 * Return:  0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast_node = list;

	if (!list)
		return (0);
	while (fast_node->next && fast_node->next->next)
	{
		list = list->next;
		fast_node = fast_node->next->next;
		if (fast_node == list)
			return (1);
	}

	return (0);
}
