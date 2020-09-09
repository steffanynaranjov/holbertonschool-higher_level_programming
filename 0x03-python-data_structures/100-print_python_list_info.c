#include <Python.h>
#include <stdio.h>
/**
* print_python_list_info - prints some basic info about Python lists
* @p: the python list
*
* Return: empty
*/
void print_python_list_info(PyObject *p)
{
	PyObject *item = NULL;
	PyListObject *list = (PyListObject *) p;
	long int x = 0;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", list->allocated);

	for (; x < Py_SIZE(p); x++)
	{
		item = PyList_GetItem(p, x);
		printf("Element %ld: %s\n", x, Py_TYPE(item)->tp_name);
	}
}
