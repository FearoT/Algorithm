{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a8622a11-aba4-42d9-b6bc-79ea06fd1197",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Minimum number of directories to delete: 4\n"
     ]
    }
   ],
   "source": [
    "# Recursive function to perform depth-first search (DFS)\n",
    "def dfs(node, deleted, adjacency_list):\n",
    "    deleted.add(node)  # Mark the current node as deleted\n",
    "    for child in adjacency_list[node]:\n",
    "        dfs(child, deleted, adjacency_list)  # Recursively delete child directories\n",
    "\n",
    "# Function to find the minimum number of directories to delete\n",
    "def find_minimum_deletions(N, directory_list):\n",
    "    # Create an adjacency list to represent the directory tree\n",
    "    adjacency_list = [[] for _ in range(N + 1)]\n",
    "\n",
    "    # Build the adjacency list from the directory list\n",
    "    for parent, child in directory_list:\n",
    "        adjacency_list[parent].append(child)\n",
    "\n",
    "    deleted = set()  # Set to store deleted directories\n",
    "    for directory in directory_list:\n",
    "        if directory[0] not in deleted:\n",
    "            dfs(directory[0], deleted, adjacency_list)\n",
    "\n",
    "    # Count the number of directories that need to be deleted\n",
    "    min_deletions = len(deleted) - 1  # Exclude the root directory\n",
    "\n",
    "    return min_deletions\n",
    "\n",
    "# Example usage\n",
    "N = 5  # Number of directories\n",
    "directory_list = [(1, 2), (1, 3), (2, 4), (3, 5)]  # List of directory relationships\n",
    "\n",
    "min_deletions = find_minimum_deletions(N, directory_list)\n",
    "print(\"Minimum number of directories to delete:\", min_deletions)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "81cf01fb-8fe4-414b-aebe-c413e5c31184",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 4\n",
      " 1 2 3 6 \n"
     ]
    },
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-ff04cd003b31>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     20\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     21\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 22\u001b[1;33m     \u001b[0mtree\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mpar\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     23\u001b[0m \u001b[0mm\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     24\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mIndexError\u001b[0m: list index out of range"
     ]
    }
   ],
   "source": [
    "#Directory Deletion\n",
    "def solve(node):\n",
    "\n",
    "    if node in d:\n",
    "\n",
    "        return 1\n",
    "\n",
    "    x=0\n",
    "\n",
    "    for child in tree[node]:\n",
    "\n",
    "        x=x+solve(child)\n",
    "\n",
    "    return x      \n",
    "\n",
    "n=int(input())\n",
    "\n",
    "par=[int(x) for x in input().split()]\n",
    "tree=[[] for i in range(n+1)]\n",
    "\n",
    "for i in range(1,n):\n",
    "\n",
    "    tree[par[i]].append(i+1)\n",
    "m=int(input())\n",
    "\n",
    "arr=[int(x) for x in input().split()]\n",
    "\n",
    "d={}\n",
    "\n",
    "for i in arr:\n",
    "\n",
    "    d[i]=1\n",
    "print(solve(1))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
