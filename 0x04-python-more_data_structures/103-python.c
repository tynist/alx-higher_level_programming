#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - Prints list info
 * @p: Python Object
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}

/**
 * print_python_bytes - Prints bytes info.
 * @p: PyObject byte
 */
void print_python_bytes(PyObject *p)
{
        unsigned char i, size;
        PyBytesObject *bytes = (PyBytesObject *)p;

        printf("[.] bytes object info\n");
        if (strcmp(p->ob_type->tp_name, "bytes") != 0)
        {
                printf("  [ERROR] Invalid Bytes Object\n");
                return;
        }

        printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
        printf("  trying string: %s\n", bytes->ob_sval);

        if (((PyVarObject *)p)->ob_size > 10)
                size = 10;
        else
                size = ((PyVarObject *)p)->ob_size + 1;

        printf("  first %d bytes: ", size);
        for (i = 0; i < size; i++)
        {
                printf("%02hhx", bytes->ob_sval[i]);
                if (i == (size - 1))
                        printf("\n");
                else
                        printf(" ");
        }
}
