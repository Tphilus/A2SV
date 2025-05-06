# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("G", "G")
        command = command.replace("()", "o")
        command = command.replace("(al)", "al")
        return command 