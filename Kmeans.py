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
		clusters = self.kmeansIteration(centroids, clusters, 30)
		return clusters


	@staticmethod
	def flatten(clusters):
		result = []
		for cluster in clusters:
			for point in cluster:
				result.append(point)
		return result

	def kmeansIteration(self, centroids, clusters, iterationsLeft):
		print "centroids",centroids
		print "clusters",clusters

		dataPoints = Kmeans.flatten(clusters)
		print "dataPoints", dataPoints
		k = len(clusters)
		newClusters = [[] for c in range(k)]

		print dataPoints
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
			print "newClusters", newClusters
		for i in range(k):
			if (Kmeans.areListsEqual(clusters[i], newClusters[i]) or
					iterationsLeft == 0):
				return newClusters
		centroids = Kmeans.calculateNewCentroids(newClusters)
		return self.kmeansIteration(centroids, newClusters, iterationsLeft-1)

	@staticmethod
	def areListsEqual(list1, list2):
		print "list1", list1
		print "list2", list2
		if(not(len(list1) == len(list2))):
			return False
		for i in range(len(list1)):
			if(not(list1[i] == list2[i])):
				return False
		return True

	@staticmethod
	def calculateNewCentroids(clusters):
		print "old: ", clusters
		k = len(clusters)
		print "k:", k
		centroids = [None] * k
		print "centroids:", centroids
	
		dimensions = len(Kmeans.flatten(clusters)[0])
		print "dimensions:", dimensions
		for clusterId in range(k):
			tot = [0]* dimensions
			for point in clusters[clusterId]:
				tot = map(sum, zip(tot,point))
				print "tot:", tot
			centroids[clusterId] = [tot[i]/float(k) for i in range(dimensions)]
			print "centroid:", clusterId, centroids[clusterId]
		print "centroids: ", clusters
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
result = kmeans.cluster(2, testData)
print "*############################*"
print result[0]
print result[1]
