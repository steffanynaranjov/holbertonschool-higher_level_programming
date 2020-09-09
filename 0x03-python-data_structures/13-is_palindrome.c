#include "lists.h"
listint_t *reverse_listint(listint_t **head);
int compare(listint_t *list_1, listint_t *list_2);
/**
 * is_palindrome - Check is the listint is a Palindrome
 * @head: type listint_s double pointer of node
 *
 * Return: 1 if is a pilndrome 0 if is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp_1, *tmp_2, *prev_tmp_1;

	tmp_1 = tmp_2 = prev_tmp_1 = *head;
	if (*head && (*head)->next)
	{
		while (tmp_2 && tmp_2->next)
		{
			tmp_2 = tmp_2->next->next;
			prev_tmp_1 = tmp_1;
			tmp_1 = tmp_1->next;
		}
		if (tmp_2)
			tmp_1 = tmp_1->next;

		prev_tmp_1->next = NULL;
	}
	return (compare(*head, reverse_listint(&tmp_1)));
}

/**
 * reverse_listint - Reverses a listint_t linked list
 * @head: Head
 *
 * Description: Reverses a listint_t linked list
 * Return: A pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *head1, *tail;

	if (!head && !*head)
		return (NULL);
	head1 = *head;
	*head = NULL;
	while (head1)
	{
		tail = head1;
		head1 = head1->next;
		tail->next = *head;
		*head = tail;
	}
	return (*head);
}

/**
 * compare - Reverses a listint_t linked list
 * @list_1: Linked list 1
 * @list_2: Linked list 2
 *
 * Description: Reverses a listint_t linked list
 * Return: 1 if is a pilndrome 0 if is not
 */
int compare(listint_t *list_1, listint_t *list_2)
{
	while (list_1 != NULL && list_2 != NULL)
	{
		if (list_1->n == list_2->n)
			list_1 = list_1->next, list_2 = list_2->next;
		else
			return (0);
	}
	if (!list_1 && !list_2)
		return (1);
	return (0);
}
