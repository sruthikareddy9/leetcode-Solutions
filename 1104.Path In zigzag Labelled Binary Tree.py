class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = []

        level = label.bit_length() - 1

        while label >= 1:
            ans.append(label)

            start = 2 ** level
            end = 2 ** (level + 1) - 1

            # Convert zigzag label to normal label
            if level % 2 == 1:
                label = start + end - label

            label = label // 2
            level -= 1

            # Convert parent back to zigzag label
            if level >= 0 and level % 2 == 1:
                start = 2 ** level
                end = 2 ** (level + 1) - 1
                label = start + end - label

        ans.reverse()
        return ans
