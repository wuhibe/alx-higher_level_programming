#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - check if a list is a palindrome
 * @head: double pointer to head of list
 * Return: 1 or 0 depends on the case
 */
int is_palindrome(listint_t **head)
{
	listint_t *tortoise = *head, *hare = *head, *prev = *head;
	listint_t *list_2 = NULL, *mid_list = NULL, *actual, *tmp;
	int ret = 0;

	if (hare == NULL || hare->next == NULL)
		return (1);
	while (hare != NULL && hare->next != NULL)
		hare = hare->next->next, prev = tortoise, tortoise = tortoise->next;
	if (hare != NULL)
		mid_list = tortoise, tortoise = tortoise->next;
	list_2 = tortoise, prev->next = NULL;
	prev = NULL, actual = list_2;
	while (actual)
		tmp = actual->next, actual->next = prev, prev = actual, actual = tmp;
	list_2 = prev;
	ret = cmp(*head, list_2);
	prev = NULL, actual = list_2;
	while (actual)
		tmp = actual->next, actual->next = prev, prev = actual, actual = tmp;
	list_2 = prev;
	if (mid_list)
		prev->next = mid_list, mid_list->next = list_2;
	else
		prev->next = list_2;
	return (ret);
}
/**
 * cmp - function to compare beginning and end of list
 * @h1: list from top
 * @h2: list from bottom
 * Return: Always zero
 */
int cmp(listint_t *h1, listint_t *h2)
{
	listint_t *tmp1 = h1, *tmp2 = h2;

	while (tmp1 && tmp2)
	{
		if (tmp1->n == tmp2->n)
			tmp1 = tmp1->next, tmp2 = tmp2->next;
		else
			return (0);
	}
	if (tmp1 == NULL && tmp2 == NULL)
		return (1);
	return (0);
}
