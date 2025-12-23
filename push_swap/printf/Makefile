# .SILENT:

NAME = libftprintf.a
OBJ_DIR = Obj

# SOURCES

SRCS = \
		ft_bzero.c \
		ft_calloc.c \
		ft_printf.c \
		ft_itoa_base.c \
		ft_putchar_fd.c \
		ft_putnbr_fd.c \
		ft_putstr_fd.c \
		ft_strlen.c \
		ft_intlen_base.c \
		next_to_percent.c
		


# compilation
CC = cc
CFLAGS = -Wall -Werror -Wextra

OBJS = $(SRCS:%.c=$(OBJ_DIR)/%.o)

# Rules
all: $(NAME)

$(NAME): $(OBJS)
	ar -rcs $(NAME) $(OBJS)

$(OBJ_DIR)/%.o: %.c | $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(OBJ_DIR): 
	mkdir -p $(OBJ_DIR)

clean:
	rm -rf $(OBJS)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
