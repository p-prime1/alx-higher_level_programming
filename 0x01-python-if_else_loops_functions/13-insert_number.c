#include "lists.h"

/**
 * add_nodeint - adds a node into a sorted list
 * @h: Head of the list
 * @number: Number to be added in the list
 * Return: Returns The new node on success and NULL on failure
 */


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	if (*head == NULL)
		return (NULL);
	new_node->n = number;
	temp = *head;
	if(temp->next->n >= number || (*head)->next == NULL)
	{
		*head = new_node;
		new_node->next = temp;
		return (new_node);
	}
	while(temp != NULL && temp->next != NULL)
	{
		if (temp->next->n < number)
		{
			temp = temp->next;
		}
		else
		{
			new_node->next = temp->next;
			temp->next = new_node;
			return (new_node);
		}
	}
	if(temp->next == NULL)
	{
		temp->next = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	return (NULL);
}

