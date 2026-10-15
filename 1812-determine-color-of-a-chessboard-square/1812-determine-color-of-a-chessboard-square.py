class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return bool((ord(coordinates[0]) + int(coordinates[1])) % 2) 
        #return (ord(coordinates[0]) + int(coordinates[1])) % 2 == 1