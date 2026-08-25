import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = collections.defaultdict(set)
        for course, prereq in prerequisites:
            courses[prereq].add(course)
        
        # 0 -> 2, 1
        # 1 -> 0
        # 2 -> 1
        
        # Too slow
        # changed = True
        # while changed:
        #     changed = False
        #     for pre_req, next_courses in list(courses.items()):
        #         for course in next_courses.copy():
        #             for post in courses[course]:
        #                 if post == pre_req:
        #                     return False
        #                 if post not in courses[pre_req]:
        #                     courses[pre_req].add(post)
        #                     changed = True
        # return True

        for pre_req, course in list(courses.items()):
            if not self.dfs(pre_req, courses):
                return False
        return True

    def dfs(self, course, courses):
        visited = set()
        stack = [course]
        while stack:
            curr = stack.pop()
            visited.add(curr)
            for nxt in courses[curr]:
                if nxt not in visited:
                    stack.append(nxt)
                if nxt == course:
                    return False
        return True
