#rocenting@gmail.com
CC = gcc
CXX = g++
CFLAGS = -O0 -Wall
# CXXFLAGS = -O0 -frtti -fexceptions -Wall
CXXFLAGS = -g -O0 -fno-strict-aliasing -Wno-write-strings -frtti -fexceptions -Wall -DDEBUG
INCPATH = -I/download/jsoncpp-src-0.5.0/include -I./libtexas -I/usr/local/include -I/usr/include/jsoncpp -I/usr/include/libev

LD = gcc
LFLAGS = #-static
#LIBS = -L. -L/usr/local/lib -L/usr/lib64 -lstdc++ -lev -ljsoncpp -lhiredis -liconv
LIBS = /usr/local/lib/libjsoncpp.a /usr/local/lib/libhiredis.a -L. -L/usr/local/lib -L/usr/lib64 -lstdc++ -lev -liconv

DESTDIR_TARGET = speaker
OBJECTS = speaker.o redis_client.o log.o daemonize.o server.o jpacket.o client.o player.o redis_sub.o eventlog.o charcoding.o wordfilter.o

all: $(DESTDIR_TARGET)

$(DESTDIR_TARGET): $(OBJECTS)
	$(LD) $(LFLAGS) -o $(DESTDIR_TARGET) $(OBJECTS) $(LIBS)

####### Implicit rules ######

.SUFFIXES: .cpp .cc .cxx .c
.cpp.o:
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o $@ $<

.cc.o:
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o $@ $<

.cxx.o:
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o $@ $<

.c.o:
	$(CC) -c $(CFLAGS) $(INCPATH) -o $@ $<

clean:
	rm -rf $(DESTDIR_TARGET) *.o
