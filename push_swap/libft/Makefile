
#Output (le fichier target donc a "executer" apres la compil)

NAME = libft.a
OB_DIR = Objs

#Sources (all files to compile)

SCHAR = \
		ft_isalnum.c \
		ft_isalpha.c \
		ft_isascii.c \
		ft_isdigit.c \
		ft_isprint.c \
		ft_tolower.c \
		ft_toupper.c \
		ft_itoa.c 

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
		ft_atoi.c 

MEM = \
		ft_calloc.c \
		ft_bzero.c \
		ft_memcpy.c \
		ft_memmove.c \
		ft_memcmp.c \
		ft_memchr.c \
		ft_memset.c 

FD = \
		ft_putchar_fd.c \
		ft_putstr_fd.c \
		ft_putendl_fd.c \
		ft_putnbr_fd.c 

SRCS = \
		$(SCHAR) \
		$(STR) \
		$(MEM) \
		$(FD) \
		$(BONUS)

BONUS = \
		ft_lstnew_bonus.c \
		ft_lstadd_front_bonus.c \
		ft_lstsize_bonus.c \
		ft_lstlast_bonus.c \
		ft_lstadd_back_bonus.c \
		ft_lstdelone_bonus.c \
		ft_lstclear_bonus.c \
		ft_lstiter_bonus.c \
		ft_lstmap_bonus.c

#Compilator

CC = cc
CFLAGS = -Wall -Wextra -Werror

OBJECTS = $(SRCS:%.c=$(OB_DIR)/%.o)
BON_OBJS = $(BONUS:%.c=$(OB_DIR)/%.o)

#Rules

#Execute la compilation
all: $(NAME)

$(NAME) : $(OBJECTS)
	ar -rcs $(NAME) $(OBJECTS)

$(OB_DIR)/%.o: %.c | $(OB_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(OB_DIR):
	mkdir -p $(OB_DIR)

#Supprime tous les objects (les .o) sans le NAME
clean:
	rm -rf $(OB_DIR)

#Supprime tous les objects (NAME inclus)
fclean: clean
	rm -f $(NAME)

#Recompile tout
re : fclean all

# Recompile tout en evitant les erreurs de compilation du style "target deja a jour donc aucune utilite de recompiler" (pas trop sur pour celle la)
.PHONY: all clean fclean re

bonus: $(BON_OBJS)
	ar -rcs $(NAME) $(BON_OBJS)
