
# divide and conquer maxmin
# def func(l,i,j):
#     if i==j:
#         return l[i],l[j]
#     elif i==j-1 or i-1==j:
#         return max(l[i],l[j]),min(l[i],l[j])
#     else:
#         mid=(i+j)//2
#         a,b=func(l,i,mid)
#         c,d=func(l,mid+1,j)
#         return max(a,c),min(b,d)
# l=list(map(int,input('enter the array: ').split()))
# i,j=map(int,input('ENter the indices: ').split())
# print(func(l,i,j))

#Greedy Knapsack
# class Item:
#     def __init__(self, profit, weight):
#         self.profit = profit
#         self.weight = weight

# def func(arr,W):
#     ans=0
#     sorted(arr,key=lambda x:(x.profit/x.weight),reverse=True)
#     for i in arr:
#         if i.weight<=W:
#             ans+=i.profit
#             W-=i.weight
#         else:
#             ans+= (W*i.profit)//i.weight
#     return ans
# W=int(input("Enter the max weight of the knapsack: "))
# l=list(map(int,input("ENter the profits: ").split()))
# m=list(map(int,input("Enter the weights: ").split()))
# arr=[]
# for i in range(len(l)):
#     a=l[i]
#     b=m[i]
#     arr.append(Item(a,b))
# print(func(arr,W))




#Job scheduling
# def func(arr,t):
#     n=len(arr)
#     for i in range(n):
#         for j in range(n-1-i):
#             if arr[j][2]<arr[j+1][2]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     job = [-1]*t
#     res = [False]*t

#     for i in range(n):
#         for j in range( min(t-1,arr[i][1]-1),-1,-1 ):
#             if res[j] is False:
#                 res[j]=True
#                 job[j]=arr[i][0]
#                 break
#     print(job)
# if __name__ == '__main__':
# 	arr = [['a', 2, 100], # Job Array
# 			['b', 1, 19],
# 			['c', 2, 27],
# 			['d', 1, 25],
# 			['e', 3, 15]]


# 	print("Following is maximum profit sequence of jobs")
# 	func(arr, 3)



#dp Knapsack

# def func(W,wt,val,n):
#     dp =[0 for i in range(W+1)]
#     for i in range(1,n+1):
#         for w in range(W,0,-1):
#             dp[w]=max(dp[w],dp[w-wt[i-1]]+val[i-1])
#     return dp[W]
# profit = [60, 100, 120] 
# weight = [10, 20, 30] 
# W = 50
# n = len(profit) 
# print(func(W, weight, profit, n)) 



#TSP DP
# MAX=999999
# def TSP(mask,pos,graph,dp,n,visited):
#     if mask==visited:
#         return graph[pos][0]
#     if dp[mask][pos]!=-1:
#         return dp[mask][pos]
#     ans=MAX
#     for city in range(n):
#         if ((mask & (1<<city))==0):
#             new=TSP(mask|(1<<city),city,graph,dp,n,visited)+graph[pos][city]
#             ans=min(ans,new)
#     dp[mask][pos]=ans
#     return dp[mask][pos]

# n=int(input("Enter the number of vertices: "))
# print("Enter the matrix: ")
# graph=[]
# for i in range(n):
#     row=list(map(int,input().split()))
#     graph.append(row)
# visited= (1<<n)-1
# r,c=16,4
# dp=[[-1 for i in range(c)]for j in range(r)]
# for i in range(1<<n):
#     for j in range(n):
#         dp[i][j]=-1
# print(TSP(1,0,graph,dp,n,visited))


# A Huffman Tree Node 
import heapq 


class node: 
	def __init__(self, freq, symbol, left=None, right=None): 
		self.freq = freq 
		self.symbol = symbol 
		self.left = left 
		self.right = right 
		self.huff = '' 
		
	def __lt__(self, nxt): 
		return self.freq < nxt.freq 

def printNodes(node, val=''): 

	newVal = val + str(node.huff) 
	if(node.left): 
		printNodes(node.left, newVal) 
	if(node.right): 
		printNodes(node.right, newVal) 
	if(not node.left and not node.right): 
		print(f"{node.symbol} -> {newVal}") 

chars = ['a', 'b', 'c', 'd', 'e', 'f'] 
freq = [5, 9, 12, 13, 16, 45] 
nodes = [] 

for x in range(len(chars)): 
	heapq.heappush(nodes, node(freq[x], chars[x])) 

while len(nodes) > 1: 

	left = heapq.heappop(nodes) 
	right = heapq.heappop(nodes) 
	left.huff = 0
	right.huff = 1
	newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right) 

	heapq.heappush(nodes, newNode) 
printNodes(nodes[0]) 
