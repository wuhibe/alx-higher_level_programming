#include "lists.h"
/**
 * insert_node - function that inserts a number into a sorted list.
 * @head: pointer the head of linked list.
 * @number: number to insert into list
 * Return: pointer to new node on success and NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t)), *lead = *head;
	listint_t *prev = lead;

	if (!new_node)
		return (NULL);
	new_node->n = number;

	if (!lead)
	{
		new_node->next = lead, *head = new_node;
		return (new_node);
	}

	while (lead->next)
	{
		if (lead->n < number)
			prev = lead, lead = lead->next;
		else
			break;
	}
	new_node->next = (lead->next) ? lead : NULL;
	if (prev == lead)
		*head = new_node;
	else
	{
		if (lead->next)
			prev->next = new_node;
		else
			lead->next = new_node;
	}
	return (new_node);
}
