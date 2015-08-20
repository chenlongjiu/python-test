'''
 epic-systems-interview-questions

Basket ball hit rates The hit rate of the basketball game is given by the number of hits divided by the number of chances. For example, you have 73 chances but hit 15 times,
then your hit rate is 15/73=0.205 (keep the last 3 digits). On average, you have 4.5 chances in each basketball game. Assume the total number of games is 162. Write a function for a basketball player. He will input the number of hits he has made, the number of chances he had, and the number of remaining games. The function should return the number of future hits,
so that he can refresh his hit rate to 0.45


'''



class Solution:
	def rateCounting(self, chance, made, game):
		rate = round(float(made)/chance , 3)
		print rate
		#(made + x)/(chance + 4.5*(162 - game)) = 0.45
		lHit = 0.45 * (chance + 4.5 * (162 - game)) - made
		print lHit
sol = Solution()
chance = input('chance is :')
made = input ('read is :')
game = input ('game is :')
sol.rateCounting(chance, made, game)