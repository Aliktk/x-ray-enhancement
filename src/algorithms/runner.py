import os
from datetime import datetime

import imageio

from src.algorithms.unsharping_mask import UM

class AlgorithmRunner:
	def __init__(self, algorithm, image, images_path):
		self.algorithm		= algorithm
		self.image				= image
		self.images_path	= images_path
		self.results_path	= os.path.join("results", datetime.now())

		os.makedirs(self.results_path, exist_ok=True)

	def __del__(self):
		self.algorithm		= ''
		self.image				= ''
		self.images_path	= ''
		self.results_path	= ''

	def run(self):
		'''Runs the algorithm in the images.'''

		if self.images_path:
			images = os.listdir(self.images_path)
			path = self.images_path
		else:
			# We put in a list to be able to utilize the for loop
			images = [self.image]
			path = ""

		for image in images:
			image = self.__run_algorithm(image, path)
			imageio.imwrite(self.results_path, image)

	def __run_algorithm(self, image, path):
		'''Runs the algorithm in the image.

		Parameters:
			image: image filename.
			path: image directory.

		Returns the processed image.
		'''

		img = os.path.join(path, image)

		# UM (Unsharping Mask)
		if self.algorithm == 'um':
			alg = UM(img)
		# TODO: HEF
		# TODO: N-CLAHE

		image = alg.run()

		return image