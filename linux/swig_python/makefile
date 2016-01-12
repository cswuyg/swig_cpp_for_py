libtest: export_wrap.o export.o
	g++ $(CFLAGS) -shared -fPIC -o _my_mod.so export_wrap.o export.o -L/home/users/wuyinguang/.jumbo/lib -lpython2.7
export_wrap.o: export_wrap.cxx
	g++ $(CFLAGS) -fPIC -c export_wrap.cxx -I/home/users/wuyinguang/.jumbo/include/python2.7/  
export.o: export.cpp
	g++ $(CFLAGS) -fPIC -c export.cpp
clean:
	rm *.o
