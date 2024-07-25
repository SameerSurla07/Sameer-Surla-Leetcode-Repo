class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # Process the current asteroid
            while stack and asteroid < 0 < stack[-1]:
                # Collision scenario
                if stack[-1] < -asteroid:
                    # Stack top asteroid is smaller, pop it and continue
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    # Both are equal, pop stack top and destroy both
                    stack.pop()
                # If the top of the stack asteroid is larger, destroy the current asteroid
                break
            else:
                # If no collision, simply add the asteroid to the stack
                stack.append(asteroid)

        return stack