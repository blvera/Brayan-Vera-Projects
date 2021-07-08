# Target library
lib := libuthread.a
objs := queue.o sem.o thread.o tps.o
CC = gcc
CFLAGS := -Wall -Werror
CFLAGS += -g

ifneq ($(V),1)
Q = @
endif
#$@ name of target
#$< first prereq
#$< all prereqs
#%.o: %.c gen any file.o from file.c
all: $(lib)

deps := $(patsubst %.o,%.d,$(objs))
-include $(deps)
DEPFLAGS = -MMD -MF $(@:.o=.d)

$(lib): $(objs)
	ar rcs $@ $^

%.o: %.c
	$(Q)$(CC) $(CFLAGS) -c -o $@ $< $(DEPFLAGS)

clean:
	@echo "CLEAN"
	$(Q)rm -f $(lib) $(objs)
