"""
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.
In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix
Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.

Example 1:
Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Example 4:
Input: "/a/./b/../../c/"
Output: "/c"

Example 5:
Input: "/a/../../b/../c//.//"
Output: "/c"

Example 6:
Input: "/a//b////c/d//././/.."
Output: "/a/b/c"
"""

def simplify_path(p):
    stack = []
    add_func = [False, False]
    ignore_func = [True, False]
    pop_func = [True, True]
    i = 0
    n = len(p)
    # while we're not 2 before the end
    while i < n - 2:
        # if multiple / in a row, move on to the last one
        while p[i+1] == '/':
            i += 1
        # if we moved to index n - 2, do not continue
        if i == n - 2:
            if p[i+1] == '.':
                break
            else:
                stack.append(p[i+1])
                break
        # check which function we'll need to do
        func = [p[i+1] == '.', p[i+2] == '.']
        if func == add_func:
            path = ''
            # while the next character is not a /
            while i < n-1 and p[i+1] is not '/':
                # concatenate the path string char by char
                path += p[i+1]
                i += 1
            # once we find a /, append the path name to the stack
            stack.append(path)
        elif func == ignore_func:
            i += 2
        elif func == pop_func:
            if stack:
                stack.pop()
            i += 3
    # create path name that doesn't end with a /
    path = '/'
    if stack:
        for i in range(len(stack) - 1):
            path += (stack[i] + '/')
        path += stack[len(stack)-1]

    return path

print(simplify_path('/home/'))
print(simplify_path('/../'))
print(simplify_path('/home//foo/'))
print(simplify_path("/a/./b/../../c/"))
print(simplify_path('/a/../../b/../c//.//'))
print(simplify_path('/a//b////c/d//././/..'))
print(simplify_path('////aaaa/'))

def simplifyPath(path):
    stack = []
    # split the path into tokens at every /. Consecutive / get turned into ''
    for token in path.split('/'):
        # if token is either '' or . pass
        if token in ('', '.'):
            pass
        elif token == '..':
        # if stack is not empty, pop
            if stack: stack.pop()
        else:
        # any other character, push into stack
            stack.append(token)
    return '/' + '/'.join(stack)

print()
print(simplifyPath('/home/'))
print(simplifyPath('/../'))
print(simplifyPath('/home//foo/'))
print(simplifyPath("/a/./b/../../c/"))
print(simplifyPath('/a/../../b/../c//.//'))
print(simplifyPath('/a//b////c/d//././/..'))
print(simplifyPath('////aaaa/'))
