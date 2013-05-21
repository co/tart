import math
import random
import numpy
import sys

#for
class Kmeans(object):
	def __init__(self, distanceFunction):
		self.distance = distanceFunction

	def cluster(self, k, dataPoints):
		centroids = random.sample(dataPoints, k)
		
# Initial cluster configuration does not matter.
		clusters = [[] for c in range(k)]
		clusters[0] = dataPoints
		print self.kmeansIteration(centroids, clusters)

	@staticmethod
	def flatten(clusters):
		result = []
		for cluster in clusters:
			for point in cluster:
				result.append(point)
		return result

	def kmeansIteration(self, centroids, clusters):

		dataPoints = Kmeans.flatten(clusters)
		k = len(clusters)
		newClusters = [[] for c in range(k)]

		for dataPoint in dataPoints:
			minimalDistance = sys.maxint
			closestCentroid = None
			for clusterId in range(k):
				print "clusterId", clusterId
				print "dataPoint", dataPoint
				print "centroid", centroids[clusterId]
				print "------------------------------------------------"
				distance = self.distance(centroids[clusterId], dataPoint)
				if distance < minimalDistance:
					minimalDistance = distance
					closestCentroid = clusterId
			newClusters[closestCentroid].append(dataPoint)
		for i in range(k):
			if (Kmeans.areListsEqual(clusters[i], newClusters[i])):
				return newClusters
		centroids = Kmeans.calculateNewCentroids(dataPoints)
		return self.kmeansIteration(centroids, newClusters)

	@staticmethod
	def areListsEqual(list1, list2):
		if(not(len(list1) == len(list2))):
			return False
		size = len(list1)
		if(len(set(list1) & set(list2)) == size):
			return True
		return False

	@staticmethod
	def calculateNewCentroids(clusters):
		centroids = [] * len(clusters)
		k = len(centroids)
		dimensions = 3
		for clusterId in range(k):
			tot = [0]* dimensions
			for point in cluster[clusterId]:
				tot = map(sum, zip(tot,point))
			centroids[clusterId] = [tot[i]/float(k) for i in range(dimensions)]
		return centroids



testData = [
		[1, 0, 0],
		[2, 0, 0],
		[3, 0, 0],
		[4, 0, 0],
		[3, 0, 0],
		[2, 0, 0],
		[0, 0, 2],
		[0, 0, 3],
		[0, 0, 4],
		[0, 0, 5],
		[0, 0, 1]]

class EuclideanDistance(object):
	def __init__(self):
		return

	def __call__(self, p1, p2):
		dimensions = len(p1)
		return (math.sqrt(sum([(p1[i]-p2[i])**2 for i in range(dimensions)])))

kmeans = Kmeans(EuclideanDistance())
kmeans.cluster(2, testData)
