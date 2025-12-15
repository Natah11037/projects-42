# .SILENT:

NAME = libft.a
OBJ_DIR = Obj

# SOURCES

# memory
MEM = \
		ft_bzero.c \
		ft_calloc.c \
		ft_memchr.c \
		ft_memcmp.c \
		ft_memcpy.c \
		ft_memmove.c \
		ft_memset.c

# char
CHAR = \
		ft_isalnum.c \
		ft_isalpha.c \
		ft_isascii.c \
		ft_isdigit.c \
		ft_isprint.c \
		ft_tolower.c \
		ft_toupper.c

# bonus
LST = \
		ft_lstnew_bonus.c \
		ft_lstadd_front_bonus.c \
		ft_lstadd_back_bonus.c \
		ft_lstclear_bonus.c \
		ft_lstdelone_bonus.c \
		ft_lstiter_bonus.c \
		ft_lstlast_bonus.c \
		ft_lstmap_bonus.c \
		ft_lstsize_bonus.c

# string
STR = \
		ft_strchr.c \
		ft_strdup.c \
		ft_striteri.c \
		ft_strjoin.c \
		ft_strlcat.c \
		ft_strlcpy.c \
		ft_strlen.c \
		ft_strmapi.c \
		ft_strncmp.c \
		ft_strnstr.c \
		ft_strrchr.c \
		ft_strtrim.c \
		ft_substr.c \
		ft_split.c \
		ft_itoa.c \
		ft_atoi.c

# file descriptor
FD = \
		ft_putchar_fd.c \
		ft_putendl_fd.c \
		ft_putnbr_fd.c \
		ft_putstr_fd.c

# source general
SRCS = \
		$(FD) \
		$(MEM) \
		$(STR) \
		$(CHAR)


# compilation
CC = cc
CFLAGS = -Wall -Werror -Wextra

OBJS = $(SRCS:%.c=$(OBJ_DIR)/%.o)

BONUS_OBJS = $(LST:%.c=$(OBJ_DIR)/%.o)

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

bonus: $(BONUS_OBJS)
	ar -rcs $(NAME) $(BONUS_OBJS)
