
# Nom de l'exécutable
NAME = push_swap

# Dossiers
OB_DIR = Objs
DIR = ./libft ./printf
AL = ./libft/libft.a
AP = ./printf/libftprintf.a

# Compilateur
CC = cc
CFLAGS = -Wall -Wextra -Werror

# Sources
OP = \
	push_and_swap.c \
	rotate.c

PARS = \
	parsing_initializer.c \
	parsing_utils.c \
	parsing_verifs.c \
	parsing_verifs2.c \
	prints.c \
	push_swap.c \
	main.c

ALL = $(OP) $(PARS)

# Objets
OBJS = $(ALL:%.c=$(OB_DIR)/%.o)

# ================= RULES =================

all: libs $(NAME)

# Compilation des libs (libft, printf)
libs:
	for i in $(DIR); do \
		$(MAKE) -C $$i; \
	done

# Création de l'exécutable
$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(NAME) $(AL) $(AP)

# Compilation des .c en .o
$(OB_DIR)/%.o: %.c | $(OB_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

# Création du dossier Objs
$(OB_DIR):
	mkdir -p $(OB_DIR)

# Nettoyage
clean:
	rm -rf $(OB_DIR)
	rm -rf a.out
	for i in $(DIR); do \
		$(MAKE) -C $$i clean; \
	done

fclean: clean
	rm -f $(NAME)
	for i in $(DIR); do \
		$(MAKE) -C $$i fclean; \
	done

re: fclean all

.PHONY: all clean fclean re libs