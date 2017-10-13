from libcpp cimport bool

cdef class PyMove:

	cdef Move cmove

	def __cinit__(self, uint16_t src, uint16_t dst, bool jump):
		self.cmove.src = src
		self.cmove.dst = dst
		self.cmove.jump = jump



cdef class PyGame:
	cdef Game* cgame

	def __cinit__(self, bool debug, bool interact):
		self.cgame = new Game(debug, interact)

	cdef int move(self, PyMove move):
		return self.cgame.move(move.cmove)

	def py_move(self, move):
		return self.move(move)


cdef class PyAI:
	cdef NewAI* ai
	
	def __cinit__(self, char difficulty):
		self.ai = new NewAI(difficulty)

	cdef generate_move(self, PyGame game):
		move = self.ai.evaluate_game(<Game&>(game.cgame[0]))
		return PyMove(move.src, move.dst, move.jump)

	def gen_move(self, game):
		#return None
		return self.generate_move(game)