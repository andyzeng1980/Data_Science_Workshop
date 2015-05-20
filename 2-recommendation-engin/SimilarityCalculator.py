import numpy
from scipy.sparse import dok_matrix

class SimilarityCalculator(object):

	def __init__(self, matrix):
		self.__matrix = matrix

	def calculateSimilarity(self):
		similarity_matrix = self.__matrix.dot(self.__matrix.T).todense()

		norm_matrix = self._generateNormMatrix(similarity_matrix)

		return self._calculateCosineMatrix(similarity_matrix,norm_matrix)

	def _generateNormMatrix(self, similarity_matrix):
		square_mag = numpy.diag(similarity_matrix)
		inv_square_mag = 1 / square_mag
		inv_square_mag[numpy.isinf(inv_square_mag)] = 0

		return numpy.diag(numpy.sqrt(inv_square_mag))

	def _calculateCosineMatrix(self,similarity_matrix,norm_matrix):
		cosine_matrix = similarity_matrix * norm_matrix
		cosine_matrix = cosine_matrix.T * norm_matrix

		return cosine_matrix