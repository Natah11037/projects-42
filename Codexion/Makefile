NAME = codexion
CC = cc
CFLAGS = -Wall -Wextra -Werror -pthread

SRCS = main.c \
	parser.c \
	error.c \
	codexion.c \
	codexion_2.c \
	coder_init.c \
	simulation.c \
	simulation_cleanup.c \
	simulation_externals_utils.c \
	compilation.c \
	heap_utils.c \
	init_time.c \
	monitoring.c \
	time_utils.c \
	utils.c

OBJS = $(SRCS:.c=.o)
HEADERS = codexion.h error.h monitoring.h parser.h utils.h

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(NAME)

%.o: %.c $(HEADERS)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
