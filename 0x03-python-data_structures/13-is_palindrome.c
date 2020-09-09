#include "lists.h"
/**
* check_palindrome - recursive function
* @first: first node of list
* @last: last node of list
*
* Return: 0 or 1
*/
int check_palindrome(listint_t **first, listint_t *last)
{
	if (last == NULL)
		return (1);

	if (check_palindrome(first, last->next) == 1 && (*first)->n == last->n)
	{
		*first = (*first)->next;
		return (1);
	}

	return (0);
}

/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: list to check
*
* Return: 0 or 1
*/
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	return (check_palindrome(head, *head));
}
