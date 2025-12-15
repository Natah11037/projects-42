#include "ft_printf.h"

int main(void)
{
int ret_printf, ret_ft_printf;

    char c = 'A';
    char *str = "Hello 42!";
    char *null_str = NULL;

    int d = -4242;
    int i = 4242;
    unsigned int u = 424242;

    void *p = str;
    void *null_ptr = NULL;

    int x = 0xabcdef;

    printf("\n===== TEST COMPARATIF printf vs ft_printf =====\n\n");

    // --- %c ---
    printf("Test %%c :\n");
    ret_printf = printf("printf    : [%c]\n", c);
    ret_ft_printf = ft_printf("ft_printf : [%c]\n\n", c);

    // --- %s ---
    printf("Test %%s (normal) :\n");
    ret_printf = printf("printf    : [%s]\n", str);
    ret_ft_printf = ft_printf("ft_printf : [%s]\n\n", str);

    printf("Test %%s (NULL) :\n");
    ret_printf = printf("printf    : [%s]\n", null_str);
    ret_ft_printf = ft_printf("ft_printf : [%s]\n\n", null_str);

    // --- %d ---
    printf("Test %%d :\n");
    ret_printf = printf("printf    : [%d]\n", d);
    ret_ft_printf = ft_printf("ft_printf : [%d]\n\n", d);

    // --- %i ---
    printf("Test %%i :\n");
    ret_printf = printf("printf    : [%i]\n", i);
    ret_ft_printf = ft_printf("ft_printf : [%i]\n\n", i);

    // --- %u ---
    printf("Test %%u :\n");
    ret_printf = printf("printf    : [%u]\n", u);
    ret_ft_printf = ft_printf("ft_printf : [%u]\n\n", u);

    // --- %p ---
    printf("Test %%p (normal) :\n");
    ret_printf = printf("printf    : [%p]\n", p);
    ret_ft_printf = ft_printf("ft_printf : [%p]\n\n", p);

    printf("Test %%p (NULL) :\n");
    ret_printf = printf("printf    : [%p]\n", null_ptr);
    ret_ft_printf = ft_printf("ft_printf : [%p]\n\n", null_ptr);
    printf("%d et %d", ret_printf, ret_ft_printf);

    // --- %x ---
    printf("Test %%x :\n");
    ret_printf = printf("printf    : [%x]\n", x);
    ret_ft_printf = ft_printf("ft_printf : [%x]\n\n", x);

    // --- %X ---
    printf("Test %%X :\n");
    ret_printf = printf("printf    : [%X]\n", x);
    ret_ft_printf = ft_printf("ft_printf : [%X]\n\n", x);

    // --- %% ---
    printf("Test %%%% :\n");
    ret_printf = printf("printf    : [%%]\n");
    ret_ft_printf = ft_printf("ft_printf : [%%]\n\n");

    printf("===== FIN DES TESTS =====\n");

}