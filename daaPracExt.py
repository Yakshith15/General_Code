#divide and conquer

# def func(l,i,j):
#     if i==j:
#         return l[i],l[j]
#     elif i==j-1 or i-1==j:
#         return max(l[i],l[j]),min(l[i],l[j])
#     else:
#         mid=(i+j)//2
#         max1,min1=func(l,i,mid)
#         max2,min2=func(l,mid+1,j)
#         return max(max1,max2),min(min1,min2)

# print("Enter the list: ")
# l=list(map(int,input().split()))
# i,j=map(int,input("Enter the range to get max and min value: ").split())
# print(func(l,i,j))

#Greedy Knapsack

# class Item:
#     def __init__(self,w,p):
#         self.w=w
#         self.p=p

# def func(arr,W):
#     arr=sorted(arr,key=lambda x:(x.p/x.w),reverse=True)
#     ans=0
#     for i in arr:
#         if W>i.w:
#             ans+=i.p
#             W-=i.w
#         else:
#             ans+= (W*i.p)/i.w
#             break
#     return ans

# W=int(input("Enter the max weight of the knapsack: "))
# p=list(map(int,input("Enter the profit list: ").split()))
# wei=list(map(int,input("Enter the weights list: ").split()))
# arr=[]
# for i in range(len(p)):
#     arr.append(Item(wei[i],p[i]))
# print(func(arr,W))

#0 1 knapsack
# class Item:
#     def __init__(self,p,w):
#         self.w=w
#         self.p=p

# def func(arr,W):
#     dp=[0]*(W+1)
#     # print(dp)
#     for i in range(len(arr)):
#         for j in range(W,0,-1):
#             dp[j]=max(dp[j],dp[j-arr[i].w]+arr[i].p)
#     return dp[W]

# print("Enter the max weight: ")
# W=int(input())
# pro=list(map(int,input("ENter the profit array: ").split()))
# wei=list(map(int,input("Enter the weight array: ").split()))
# arr=[]
# for i in range(len(pro)):
#     arr.append(Item(pro[i],wei[i]))
# print(func(arr,W))

# class Item:
#     def __init__(self,n,d,p):
#         self.n=n
#         self.d=d
#         self.p=p

# def func(arr,t):
#     arr=sorted(arr,key=lambda x:x.p,reverse=True)
#     ans=["YOHOHO"]*t
#     temp=[False]*t
#     for i in range(len(arr)):
#         for j in range(min(t-1,arr[i].d-1),-1,-1):
#             if temp[j] is False:
#                 temp[j]=True
#                 ans[j]=arr[i].n
#                 break
#     return ans

# names=list(input("Enter the names of the jobs: ").split())
# dl=list(map(int,input("Enter the deadlines of the jobs: ").split()))
# pro=list(map(int,input("Enter the profits of the jobs: ").split()))
# arr=[]
# for i in range(len(pro)):
#     arr.append(Item(names[i],dl[i],pro[i]))
# # print(arr)
# print(func(arr,3))

#LCS
# def func(s1,s2,ind1,ind2,dp):
#     if ind1<0 or ind2<0:
#         return 0
#     if dp[ind1][ind2]!=-1:
#         return dp[ind1][ind2]
#     if s1[ind1]==s2[ind2]:
#         return 1+func(s1,s2,ind1-1,ind2-1,dp)
#     return max(func(s1,s2,ind1-1,ind2,dp),func(s1,s2,ind1,ind2-1,dp))

# s1=input("Enter the string 1: ")
# s2=input("Enter the string 2: ")
# dp=[[-1 for i in range(len(s2))] for i in range(len(s1))]
# print(func(s1,s2,len(s1)-1,len(s2)-1,dp))

#prims algo
# import heapq

# def func(V,adj):
#     pq=[(0,0)]
#     vis=[0]*V
#     ans=0
#     while pq:
#         wt,node=heapq.heappop(pq)

#         if vis[node]==1:
#             continue
#         vis[node]=1
#         ans+=wt
#         for i in adj[node]:
#             adjnode,edgeW=i[0],i[1]
#             if not vis[adjnode]:
#                 heapq.heappush(pq,(edgeW,adjnode))
#     return ans
# V=5
# edges = [[0, 1, 2], [0, 2, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 2, 2]]
# adj=[[] for _ in range(V)]
# for i in edges:
#     adj[i[0]].append([i[1],i[2]])
#     adj[i[1]].append([i[0],i[2]])

# print(func(V,adj))

# import heapq

# def func(V,adj):
#     pq=[(0,0)]
#     dist=[1e9] * V
#     dist[0]=0
    
#     # while pq:
#     #     wei,node= heapq.heappop(pq)
#     #     for adjnode,W in adj[node]:
#     #         vis[adjnode]=min(vis[adjnode],vis[node]+W)
#     #         heapq.heappush(pq,(vis[adjnode],adjnode))

#     # for i in range(V):
#     #     print(f"{i} \t\t {vis[i]}")
#     while pq:
#         d, u = heapq.heappop(pq)

#         for v, weight in adj[u]:
#             if dist[v] > dist[u] + weight:
#                 dist[v] = dist[u] + weight
#                 heapq.heappush(pq, (dist[v], v))

#     for i in range(V):
#         print(f"{i} \t\t {dist[i]}")
# V=5
# edges = [[0, 1, 2], [0, 2, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 2, 2]]
# adj=[[] for _ in range(V)]
# for i in edges:
#     adj[i[0]].append([i[1],i[2]])
#     adj[i[1]].append([i[0],i[2]])
# func(V,adj)
# # V = 9
# # adj = [[] for _ in range(V)]

# # def addEdge(adj, u, v, w):
# #     adj[u].append((v, w))
# #     adj[v].append((u, w))
# # addEdge(adj, 0, 1, 4)
# # addEdge(adj, 0, 7, 8)
# # addEdge(adj, 1, 2, 8)
# # addEdge(adj, 1, 7, 11)
# # addEdge(adj, 2, 3, 7)
# # addEdge(adj, 2, 8, 2)
# # addEdge(adj, 2, 5, 4)
# # addEdge(adj, 3, 4, 9)
# # addEdge(adj, 3, 5, 14)
# # addEdge(adj, 4, 5, 10)
# # addEdge(adj, 5, 6, 2)
# # addEdge(adj, 6, 7, 1)
# # addEdge(adj, 6, 8, 6)
# # addEdge(adj, 7, 8, 7)

# func(V,adj)



#Floyd
# def shortest_distance(matrix):
#     n = len(matrix)

#     for i in range(n):
#         for j in range(n):
#             if matrix[i][j] == -1:
#                 matrix[i][j] = float('inf')
#             if i == j:
#                 matrix[i][j] = 0

#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

#     for i in range(n):
#         for j in range(n):
#             if matrix[i][j] == float('inf'):
#                 matrix[i][j] = -1

# if __name__ == "__main__":
#     V = 4
#     matrix = [[-1] * V for _ in range(V)]
#     matrix[0][1] = 2
#     matrix[1][0] = 1
#     matrix[1][2] = 3
#     matrix[3][0] = 3
#     matrix[3][1] = 5
#     matrix[3][2] = 4

#     shortest_distance(matrix)

#     for row in matrix:
#         for cell in row:
#             print(cell, end=" ")
#         print()


#bellmanFord

# def func(V,edges,S):
#     dist=[float('inf')]*V
#     dist[S]=0

#     for i in range(V-1):
#         for edge in edges:
#             u,v,wt=edge
#             if dist[u]!=float('inf') and dist[v]>dist[u]+wt:
#                 dist[v]=dist[u]+wt
#     for edge in edges:
#             u,v,wt=edge
#             if dist[u]!=float('inf') and dist[v]>dist[u]+wt:
#                 return [-1]
#     return dist

# V = 6
# edges = [
#     [3, 2, 6],
#     [5, 3, 1],
#     [0, 1, 5],
#     [1, 5, -3],
#     [1, 2, -2],
#     [3, 4, -2],
#     [2, 4, 3]
# ]

# S = 0
# dist = func(V, edges, S)

# for d in dist:
#     print(d, end=" ")

# print()


#Matrix Chain Multiplication

# import sys
# dp=[[-1 for i in range(100)] for j in range(100)]

# def func(arr,i,j):
#     if i==j:
#         return 0
#     if dp[i][j]!=-1:
#         return dp[i][j]
#     dp[i][j]=sys.maxsize
#     for k in range(i,j):
#         dp[i][j]=min(dp[i][j], func(arr,i,k)+func(arr,k+1,j)+arr[i-1]*arr[k]*arr[j] )
#     return dp[i][j]

# arr=list(map(int,input("Enter the array of dimnesions: ").split()))
# print(func(arr,1,len(arr)-1))

# #Kruskals
# def find(parent,i):
#     if parent[i]!=i:
#         parent[i]=find(parent,parent[i])
#     return parent[i]

# def union(parent,rank,x,y):
#     if rank[x]<rank[y]:
#         parent[x]=y
#     elif rank[x]>rank[y]:
#         parent[y]=x
#     else:
#         parent[y]=x
#         rank[x]+=1
    
# def func(V,edges):
#     i=0
#     e=0
#     result=[]
#     edges=sorted(edges,key=lambda x: x[2])
#     parent=[node for node in range(V)]
#     rank=[0]*V

#     while e<V-1:
#         u,v,w=edges[i]
#         i+=1
#         x=find(parent,u)
#         y=find(parent,v)
#         if x!=y:
#             e+=1
#             result.append([u,v,w])
#             union(parent,rank,x,y)
#     ans=0
#     for u,v,wt in result:
#         ans+=wt
#     print("The answer is : ",ans)


# vertices = 4
# edges = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]

# func(vertices, edges)


#NQueen's
# def solve(col,board,ans,leftrow,uppDiag,lowDiag,n):
#     if col==n:
#         ans.append(board[:])
#         return 
#     for row in range(n):
#         if leftrow[row]==0 and lowDiag[row+col]==0 and uppDiag[n-1+col-row]==0:
#             board[row]=board[row][:col]+'Q'+board[row][col+1:]
#             leftrow[row]=1
#             uppDiag[n-1+col-row]=1
#             lowDiag[col+row]=1
#             solve(col+1,board,ans,leftrow,uppDiag,lowDiag,n)            
#             board[row]=board[row][:col]+'.'+board[row][col+1:]
#             leftrow[row]=0
#             uppDiag[n-1+col-row]=0
#             lowDiag[col+row]=0
# n=int(input("ENter the number of columns or rows: "))
# ans=[]
# board=['.'*n for _ in range(n)]
# leftrow=[0]*n
# uppDiag=[0]*(2*n-1)
# lowDiag=[0]*(2*n-1)
# solve(0,board,ans,leftrow,uppDiag,lowDiag,n)
# print(ans)

# Huffman Code
# import heapq

# class node: 
# 	def __init__(self, freq, symbol, left=None, right=None): 
# 		self.freq = freq 
# 		self.symbol = symbol 
# 		self.left = left 
# 		self.right = right 
# 		self.huff = '' 
		
# 	def __lt__(self, nxt): 
# 		return self.freq < nxt.freq 
	
# def printNodes(node,val=''):
	
# 	newVal=str(node.huff)+val
# 	if node.left:
# 		printNodes(node.left,newVal)
# 	if node.right:
# 		printNodes(node.right,newVal)
# 	if not node.left and not node.right:
# 		print(f"{node.symbol} -> {newVal}")

# # freq=[]
# # char=[]
# chars = ['a', 'b', 'c', 'd', 'e', 'f'] 
# freq = [5, 9, 12, 13, 16, 45] 
# nodes = [] 

# for i in range(len(chars)):
# 	heapq.heappush(nodes,node(freq[i],chars[i]))

# while len(nodes)>1:
# 	left=heapq.heappop(nodes)
# 	right=heapq.heappop(nodes)
# 	left.huff=0
# 	right.huff=1
# 	newNode=node(left.freq+right.freq,left.symbol+right.symbol,left,right)
# 	heapq.heappush(nodes,newNode)
# printNodes(nodes[0])