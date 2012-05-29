NAME=$(shell awk '/Name/ { print $$2 }' iprediaos-gnome-shell-favorite-apps.spec)
VERSION=$(shell awk '/Version/ { print $$2 }' iprediaos-gnome-shell-favorite-apps.spec)

all:

install: 
	@install -D  org.gnome.shell.gschema.override ${PREFIX}/usr/share/glib-2.0/schemas/org.gnome.shell.gschema.override

archive:
	@git archive --prefix=$(NAME)-$(VERSION)/ HEAD -o $(NAME)-$(VERSION).tar
	@bzip2 -f $(NAME)-$(VERSION).tar
	@echo "$(NAME)-$(VERSION).tar.bz2 created"
clean:
	rm -f *~ *bz2
