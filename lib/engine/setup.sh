# setup.sh
# Make the "myext" Python Module ("myext.so")
CC="gcc"   \
CXX="g++"   \
CFLAGS="-I./source -I../../../DEPENDENCIES/python3.5/inc -I../../../DEPENDENCIES/gsl-1.15"   \
LDFLAGS="-L /home/divserge/YaDisk/robots/chess/lib/engine/source/build"   \
    python3 setup.py build_ext --inplace