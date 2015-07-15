import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf

import org.apache.spark.graphx._
import org.apache.spark.rdd.RDD

object PageRank {
	def main(args: Array[String]) {
		val sc = new SparkContext("local", "pagerank-test", new SparkConf)

		// Load the edges as a graph
		val graph = GraphLoader.edgeListFile(sc, "hdfs:///data/patents/example/followers.txt")
		// Run PageRank
		val ranks = graph.pageRank(0.01).vertices
		// Join the ranks with the usernames
		val users = sc.textFile("hdfs:///data/patents/example/users.txt").map { line =>
		  val fields = line.split(",")
		  (fields(0).toLong, fields(1))
		}
		val ranksByUsername = users.join(ranks).map {
		  case (id, (username, rank)) => (username, rank)
		}
		// Print the result
		println(ranksByUsername.collect().mkString("\n"))
	}
}
