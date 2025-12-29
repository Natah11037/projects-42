
#Output

NAME = libftprintf.a
OB_DIR = Objs

#Sources (all files to compile)

SRCS = \
		ft_bzero.c \
		ft_calloc.c \
		ft_itoa_base.c \
		ft_printf.c \
		ft_putadress.c \
		ft_putchar.c \
		ft_putnbr.c \
		ft_putstr.c \
		ft_strlen.c \
		ft_next_to_percent.c \


#Compilator

CC = cc
CFLAGS = -Wall -Wextra -Werror

OBJECTS = $(SRCS:%.c=$(OB_DIR)/%.o)

#Rules

all: $(NAME)

$(NAME) : $(OBJECTS)
	ar -rcs $(NAME) $(OBJECTS)

$(OB_DIR)/%.o: %.c | $(OB_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(OB_DIR):
	mkdir -p $(OB_DIR)

clean:
	rm -rf $(OB_DIR)


fclean: clean
	rm -f $(NAME)

re : fclean all

.PHONY: all clean fclean re
