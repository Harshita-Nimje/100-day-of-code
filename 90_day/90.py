class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(min(salary))
        salary.remove(max(salary))
        fun = sum(salary)
        dum= fun / len(salary)
        return dum