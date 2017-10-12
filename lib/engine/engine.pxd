cimport numpy as np
from libcpp cimport bool

cdef extern from "<stdint.h>" nogil:
	ctypedef unsigned short uint16_t

cdef extern from "BitBoard.hpp":
	struct Move:
		uint16_t src
		uint16_t dst
		bool jump


cdef extern from "Game.hpp":
	cppclass Game:
		Game(bool debug, bool interact)	
		int move(Move& move)

cdef extern from "NewAI.hpp":
	cppclass NewAI:
		NewAI(char difficulty)
		Move evaluate_game(Game& game)


